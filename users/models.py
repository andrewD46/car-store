import base64
import datetime
import hashlib
import random
import string

from django.contrib.auth.models import AbstractUser
from django.core.signing import TimestampSigner
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator

HOST = 'http://127.0.0.1:8000'


class User(AbstractUser):
    TOKEN_ALPHABET = (string.ascii_letters + string.digits) * 10
    TOKEN_LENGTH = 256

    signer = TimestampSigner()

    phone = models.CharField(max_length=12, validators=[MinLengthValidator(12)], null=True)
    is_email_verified = models.BooleanField(default=False)
    secret_email_token = models.CharField(max_length=TOKEN_LENGTH)
    verification_email_sent_at = models.DateTimeField(null=True)

    class Meta:
        ordering = ['username', 'email']

    def get_secret_token(self):
        return "".join(
            random.sample(self.TOKEN_ALPHABET, self.TOKEN_LENGTH)
        )

    def digest_token(self, token):
        return hashlib.md5(token.encode('utf-8')).hexdigest()

    def sign_token(self, token):
        return self.signer.sign(token)

    def unsign_token(self, token):
        return self.signer.unsign(token, max_age=datetime.timedelta(hours=1))

    def convert_token(self, token):
        return base64.b64encode(token.encode('utf-8')).decode('utf-8')

    def make_verify_link(self, token):
        return f"{HOST}/verify/?token={token}"

    def deconvert_token(self, token):
        return base64.b64decode(token.encode('utf-8')).decode('utf-8')

    def is_token_correct(self, token):
        deconverted = self.deconvert_token(token)
        unsigned = self.unsign_token(deconverted)
        return unsigned == self.digest_token(self.secret_email_token)

    def verify_email(self):
        self.is_email_verified = True
        self.save()

    def send_verification_email(self):
        token = self.get_secret_token()
        self.secret_email_token = token
        self.verification_email_sent_at = timezone.now()
        self.save()

        digested_token = self.digest_token(token)
        signed = self.sign_token(digested_token)
        converted = self.convert_token(signed)
        link = self.make_verify_link(converted)

        return send_mail(
            "Verify your email",
            f"Please follow this link: {link}",
            "admin@admin.com",
            [self.email]
        )


# class Avatar(models.Model):
#     user = models.ForeignKey(User, related_name='avatars', on_delete=models.CASCADE)
#     image = models.ImageField(upload_to="img")
#     create_at = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         get_latest_by = 'create_at'
#         ordering = ['create_at']
#
#     def __str__(self):
#         return f"{self.user.username} avatar"

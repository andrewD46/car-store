import django_filters
from ads.models import Ad


class AdsFilter(django_filters.FilterSet):

    CHOICES = (
        ('ascending', 'Сначала старые'),
        ('descending', 'Сначала новые'),
        ('cheap', 'Сначала дешевые'),
        ('uncheap', 'Сначала дорогие'),
    )

    ordering = django_filters.ChoiceFilter(label='Ordering', choices=CHOICES, method='filter_by_order')

    class Meta:
        model = Ad
        fields = ('brand', 'year')

    def filter_by_order(self, queryset, name, value):
        expression = 'created_at' if value == 'ascending' else '-created_at'
        expression2 = 'price' if value == 'cheap' else '-price'
        return queryset.order_by(expression, expression2)

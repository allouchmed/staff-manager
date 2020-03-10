import datetime
import logging
import re
from typing import Any, Optional

from django.db.models import QuerySet
from django.utils.translation import ugettext_lazy as _
from django_filters import FilterSet, CharFilter

logger = logging.getLogger(__name__)


class SearchFieldFilterSet(FilterSet):
    """
    Mixin for FilterSet adding complex search field "searching_fields".
    You specify filtered field by using "__": searching_fields = ['field', 'field__field'].
    "lookups" is for adding comparison method for fields.
    """

    search_field_placeholder: str = _('Search...')
    label: str = ''
    searching_fields: list = []
    lookups: dict = {}
    default_lookup: str = 'icontains'

    search = CharFilter(method='filter_search')

    def filter_search(self, queryset, name, value):
        raw_value = value
        additional_search_results = self.extend_search_results(queryset, value)

        if value and self.searching_fields:
            value_date = self._parse_date(value)
            if value_date:
                value = value_date

            qs = queryset.none()

            # search by string representation of objects from queryset, slow.
            # example: searching_fields = ['__str__', 'another_field']
            if '__str__' in self.searching_fields:
                self.searching_fields = [field for field in self.searching_fields if field != '__str__']
                pk_list = []
                for obj in queryset:
                    obj_string = str(obj)
                    if raw_value in obj_string or obj_string in raw_value:
                        pk_list.append(obj.pk)
                qs = queryset.filter(pk__in=pk_list)

            for field in self.searching_fields:
                # skipping fields when an error occurs, then they do not affect the search result.
                try:
                    lookup = self.lookups.get(field, self.default_lookup)
                    qs |= queryset.filter(**{'{0}__{1}'.format(field, lookup): value})
                except Exception as e:
                    logger.info(f'An error occurred while filtering with SearchFieldMixin: {e}')
        else:
            qs = queryset

        if additional_search_results:
            qs |= additional_search_results

        return qs

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form.fields['search'].label = self.label
        self.form.fields['search'].widget.attrs.update({'placeholder': self.search_field_placeholder})

    def _parse_date(self, value):
        # date parsing
        date_re = re.compile(r'(?P<day>\d{1,2}).(?P<month>\d{1,2}).(?P<year>\d{4})$')
        date_match = date_re.match(value)
        if date_match:
            kw = {k: int(v) for k, v in date_match.groupdict().items()}
            try:
                return datetime.date(**kw)
            except ValueError:
                return None

    def extend_search_results(self, qs: QuerySet, value: Any) -> Optional[QuerySet]:
        pass

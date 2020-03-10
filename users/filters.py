from typing import Optional

from dev_tools.template.mixins import HttpRequestType
from django.db.models import Q
from django.forms import CheckboxInput
from django.utils.translation import ugettext_lazy as _
from django_filters import OrderingFilter, BooleanFilter
from flex_forms.forms import FlexForm

from users.models import User, Country, City, Organization, Department
from utils.filters import SearchFieldFilterSet


class BaseFilterFlexFormMixin:
    """
    Mixin for filter forms with some static parameters.
    """

    css_classes = ['flex-object', 'js-filter_form']

    def _get_request(self) -> Optional[HttpRequestType]:
        return None


class EmployeesTableFilterFlexForm(BaseFilterFlexFormMixin, FlexForm):
    """
    Flex form for fast filter-fields position setup.
    """

    html_params = {'id': 'employee-filter', 'method': 'GET'}
    grid = {
        '_0': ['search'],
        '_1': ['city', 'city__country', 'organization', 'department'],
        '_2': ['department_exist', 'organization_exist']
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['search'].widget.attrs['class'] = 'flex-half-width'


class EmployeesTemplateTableFilter(SearchFieldFilterSet):
    """
    Filter for employees filtering and template table column sorting.
    """

    searching_fields = ['id', 'first_name', 'last_name']
    ordering = OrderingFilter(
        fields=(
            ('id', 'id'),
            ('first_name', 'first_name'),
            ('last_name', 'last_name'),
            ('city__country__name', 'city__country__name'),
            ('city__name', 'city__name'),
            ('organization__name', 'organization__name'),
            ('department__name', 'department__name'),
        )
    )

    department_exist = BooleanFilter(
        label=_('Department exist'), method='filter_department_exist', widget=CheckboxInput()
    )
    organization_exist = BooleanFilter(
        label=_('Organization exist'), method='filter_organization_exist', widget=CheckboxInput()
    )

    def filter_department_exist(self, queryset, name, value):
        if value:
            queryset = queryset.filter(~Q(department__isnull=value))
        return queryset

    def filter_organization_exist(self, queryset, name, value):
        if value:
            queryset = queryset.filter(~Q(organization__isnull=value))
        return queryset

    class Meta:
        model = User
        form = EmployeesTableFilterFlexForm
        fields = ['city', 'city__country', 'organization', 'department']


class IDAndNameTemplateTableFilterMixin:
    """
    Filter class for instances which need display their ID and Name fields only.
    """

    searching_fields = ['id', 'name']
    ordering = OrderingFilter(
        fields=(
            ('id', 'id'),
            ('name', 'name')
        )
    )


class CountriesTableFilterFlexForm(BaseFilterFlexFormMixin, FlexForm):
    """
    Flex form for fast filter-fields position setup.
    """

    html_params = {'id': 'countries-filter', 'method': 'GET'}
    grid = {
        '_0': ['search']
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['search'].widget.attrs['class'] = 'flex-half-width'


class CountriesTemplateTableFilter(IDAndNameTemplateTableFilterMixin, SearchFieldFilterSet):
    """
    Filter for Countries filtering and template table column sorting.
    """

    class Meta:
        model = Country
        form = CountriesTableFilterFlexForm
        fields = []


class CitiesTableFilterFlexForm(BaseFilterFlexFormMixin, FlexForm):
    """
    Flex form for fast filter-fields position setup.
    """

    html_params = {'id': 'cities-filter', 'method': 'GET'}
    grid = {
        '_0': ['search'],
        '_1': ['country']
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['search'].widget.attrs['class'] = 'flex-half-width'
        self.fields['country'].widget.attrs['class'] = 'flex-half-width'


class CitiesTemplateTableFilter(SearchFieldFilterSet):
    """
    Filter for Cities filtering and template table column sorting.
    """

    searching_fields = ['id', 'name', 'country__name']
    ordering = OrderingFilter(
        fields=(
            ('id', 'id'),
            ('country__name', 'country__name'),
            ('name', 'name')
        )
    )

    class Meta:
        model = City
        form = CitiesTableFilterFlexForm
        fields = ['country']


class OrganizationsTableFilterFlexForm(BaseFilterFlexFormMixin, FlexForm):
    """
    Flex form for fast filter-fields position setup.
    """

    html_params = {'id': 'organizations-filter', 'method': 'GET'}
    grid = {
        '_0': ['search']
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['search'].widget.attrs['class'] = 'flex-half-width'


class OrganizationsTemplateTableFilter(IDAndNameTemplateTableFilterMixin, SearchFieldFilterSet):
    """
    Filter for Organizations filtering and template table column sorting.
    """

    class Meta:
        model = Organization
        form = OrganizationsTableFilterFlexForm
        fields = []


class DepartmentsTableFilterFlexForm(BaseFilterFlexFormMixin, FlexForm):
    """
    Flex form for fast filter-fields position setup.
    """

    html_params = {'id': 'departments-filter', 'method': 'GET'}
    grid = {
        '_0': ['search'],
        '_1': ['organization']
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['search'].widget.attrs['class'] = 'flex-half-width'
        self.fields['organization'].widget.attrs['class'] = 'flex-half-width'


class DepartmentsTemplateTableFilter(SearchFieldFilterSet):
    """
    Filter for Departments filtering and template table column sorting.
    """

    searching_fields = ['id', 'name', 'organization__name']
    ordering = OrderingFilter(
        fields=(
            ('id', 'id'),
            ('organization__name', 'organization__name'),
            ('name', 'name')
        )
    )

    class Meta:
        model = Department
        form = DepartmentsTableFilterFlexForm
        fields = ['organization']


class DepartmentEmployeesTableFilterFlexForm(EmployeesTableFilterFlexForm):
    """
    Flex form for fast filter-fields position setup.
    """

    grid = {
        '_0': ['search'],
        '_1': ['city', 'city__country'],
        '_2': ['in_the_department']
    }


class DepartmentEmployeesTemplateTableFilter(EmployeesTemplateTableFilter):
    """
    Filter for Department Employees filtering and template table column sorting.
    """

    def __init__(self, *args, **kwargs):
        self.department = kwargs.pop('department')
        super().__init__(*args, **kwargs)
        # By default display only department's employees.
        if not self.data:
            self.queryset = self.queryset.filter(department=self.department)
            self.form.initial['in_the_department'] = True

    in_the_department = BooleanFilter(
        label=_('In the department'),
        method='filter_employees',
        widget=CheckboxInput(),
        help_text=_('Uncheck if need to add new employees to this department.')
    )

    def filter_employees(self, queryset, name, value):
        if value:
            queryset = queryset.filter(department=self.department)
        else:
            queryset = queryset.filter(
                Q(organization__isnull=True) | Q(organization=self.department.organization),
                department__isnull=True
            )
        return queryset

    class Meta(EmployeesTemplateTableFilter.Meta):
        form = DepartmentEmployeesTableFilterFlexForm
        fields = ['city', 'city__country']

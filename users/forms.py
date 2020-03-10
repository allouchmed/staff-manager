from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from flex_forms.components import FlexButton
from flex_forms.forms import FlexModelForm, StaticModelFieldset

from users.models import User, Country, City, Organization, Department
from utils.components import MaterialIcon, ARSimpleLink


class EmployeeCreateUpdateForm(FlexModelForm):
    """
    Form for creating or updating Employee instances.
    """

    html_params = {'id': 'employee-create-form', 'method': 'POST', 'novalidate': ''}
    css_classes = ['flex-object', 'js-detached_from']
    grid = {
        '_0': ['username'],
        '_1': ['email'],
        '_2': ['first_name', 'last_name'],
        'Location': ['city', 'city_create'],
        'Work': ['organization'],
        '_5': ['department', 'department_create']
    }

    city_create = FlexButton(
        icon=MaterialIcon('add'),
        css_classes=['custom-btn', 'btn-outline-light'],
        field_group_class='object-add-btn-container',
        html_params={
            'href': reverse_lazy('dashboard:city_create')
        },
        button_class=ARSimpleLink
    )
    department_create = FlexButton(
        icon=MaterialIcon('add'),
        css_classes=['custom-btn', 'btn-outline-light'],
        field_group_class='object-add-btn-container',
        html_params={
            'href': reverse_lazy('dashboard:department_create')
        },
        button_class=ARSimpleLink
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['organization'].disabled = True

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'city', 'organization', 'department')


class CountryCreateUpdateForm(FlexModelForm):
    """
    Form for create or update Country instances.
    """

    html_params = {'id': 'country-create-form', 'method': 'POST', 'novalidate': ''}
    css_classes = ['flex-object', 'js-detached_from']
    grid = {
        'Country Info': ['name'],
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'flex-half-width'

    class Meta:
        model = Country
        fields = ('name',)
        labels = {
            'name': _('Name')
        }


class CityCreateUpdateForm(FlexModelForm):
    """
    Form for create or update City instances.
    """

    html_params = {'id': 'city-create-form', 'method': 'POST', 'novalidate': ''}
    css_classes = ['flex-object', 'js-detached_from']
    grid = {
        'City Info': ['country', 'name']
    }

    class Meta:
        model = City
        fields = ('country', 'name')
        labels = {
            'name': _('Name')
        }


class OrganizationCreateUpdateForm(FlexModelForm):
    """
    Form for create or update Organization instances.
    """

    html_params = {'id': 'organization-create-form', 'method': 'POST', 'novalidate': ''}
    css_classes = ['flex-object', 'js-detached_from']
    grid = {
        'Organization Info': ['name']
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'flex-half-width'

    class Meta:
        model = Organization
        fields = ('name',)
        labels = {
            'name': _('Name')
        }


class DepartmentCreateUpdateForm(FlexModelForm):
    """
    Form for create or update Department instances.
    """

    html_params = {'id': 'department-create-form', 'method': 'POST', 'novalidate': ''}
    css_classes = ['flex-object', 'js-detached_from']
    grid = {
        'Department Info': ['organization', 'name']
    }

    class Meta:
        model = Department
        fields = ('organization', 'name')
        labels = {
            'name': _('Name')
        }


class DepartmentStaticFieldset(StaticModelFieldset):
    """
    Fieldset for displaying Department info.
    """

    grid = {
        'Department Info': ['organization', 'name']
    }
    labels = {
        'name': _('Name')
    }

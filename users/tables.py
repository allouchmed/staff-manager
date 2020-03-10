from typing import List, Any

from dev_tools.utils import safety_get_attribute as ga_
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from template_tables.components import BaseTemplateTable, TableRowType, TH, TR, TD

from users.models import User, City, Department
from utils.components import ARSimpleLink, ARMaterialIcon


class EmployeesTemplateTable(BaseTemplateTable):
    """
    A table class for Employees displaying on the dashboard page.
    """

    empty_table_text = _('No data')

    def get_header_rows(self) -> List[TableRowType]:
        cells = [
            TH(_('Employee ID'), ordering='id'),
            TH(_('First name'), ordering='first_name'),
            TH(_('Last name'), ordering='last_name'),
            TH(_('Country'), ordering='city__country__name'),
            TH(_('City'), ordering='city__name'),
            TH(_('Organization'), ordering='organization__name'),
            TH(_('Department'), ordering='department__name'),
            TH('', css_classes=['action-cell'])
        ]

        return [TR(cells)]

    def get_body_row(self, index: int, data_item: Any) -> TableRowType:
        employee = data_item  # type: User
        transition_btn = ARSimpleLink(
            icon=ARMaterialIcon('edit'),
            css_classes=['custom-btn', 'table-transition-btn'],
            html_params=dict(href=reverse('dashboard:employee_update', kwargs=dict(pk=employee.id)))
        )
        cells = [
            TD(employee.id),
            TD(employee.first_name),
            TD(employee.last_name),
            TD(ga_(employee, 'city__country')),
            TD(employee.city),
            TD(employee.organization),
            TD(employee.department),
            TD(transition_btn, css_classes=['action-cell'])
        ]

        return TR(cells)


class IDAndNameTemplateTable(BaseTemplateTable):
    """
    Template table class for instances which need display their ID and Name fields only.
    """

    update_url_pattern: str = ''
    empty_table_text = _('No data')

    def get_header_rows(self) -> List[TableRowType]:
        cells = [
            TH(_('ID'), ordering='id'),
            TH(_('Name'), ordering='name'),
            TH('', css_classes=['action-cell'])
        ]

        return [TR(cells)]

    def get_body_row(self, index: int, data_item: Any) -> TableRowType:
        transition_btn = ARSimpleLink(
            icon=ARMaterialIcon('edit'),
            css_classes=['btn-outline-light', 'custom-btn', 'table-transition-btn'],
            html_params=dict(href=reverse(self.update_url_pattern, kwargs=dict(pk=data_item.id)))
        )
        cells = [
            TD(data_item.id),
            TD(data_item.name),
            TD(transition_btn, css_classes=['action-cell'])
        ]

        return TR(cells)


class CountriesTemplateTable(IDAndNameTemplateTable):
    """
    A table class for Countries displaying on the dashboard page.
    """

    update_url_pattern = 'dashboard:country_update'


class CitiesTemplateTable(BaseTemplateTable):
    """
    A table class for Cities displaying on the dashboard page.
    """

    empty_table_text = _('No data')

    def get_header_rows(self) -> List[TableRowType]:
        cells = [
            TH(_('ID'), ordering='id'),
            TH(_('Name'), ordering='name'),
            TH(_('Country'), ordering='country__name'),
            TH('', css_classes=['action-cell'])
        ]

        return [TR(cells)]

    def get_body_row(self, index: int, data_item: Any) -> TableRowType:
        city = data_item  # type: City
        transition_btn = ARSimpleLink(
            icon=ARMaterialIcon('edit'),
            css_classes=['btn-outline-light', 'custom-btn', 'table-transition-btn'],
            html_params=dict(href=reverse('dashboard:city_update', kwargs=dict(pk=city.id)))
        )
        cells = [
            TD(city.id),
            TD(city.name),
            TD(city.country.name),
            TD(transition_btn, css_classes=['action-cell'])
        ]

        return TR(cells)


class OrganizationsTemplateTable(IDAndNameTemplateTable):
    """
    A table class for Organizations displaying on the dashboard page.
    """

    update_url_pattern = 'dashboard:organization_update'


class DepartmentTemplateTable(BaseTemplateTable):
    """
    A table class for Departments displaying on the dashboard page.
    """

    empty_table_text = _('No data')

    def get_header_rows(self) -> List[TableRowType]:
        cells = [
            TH(_('ID'), ordering='id'),
            TH(_('Name'), ordering='name'),
            TH(_('Organization'), ordering='organization__name'),
            TH('', css_classes=['action-cell'])
        ]

        return [TR(cells)]

    def get_body_row(self, index: int, data_item: Any) -> TableRowType:
        department = data_item  # type: Department
        employees_edit_btn = ARSimpleLink(
            icon=ARMaterialIcon('face'),
            css_classes=['btn-outline-light', 'custom-btn', 'table-transition-btn'],
            html_params=dict(href=reverse('dashboard:department_details', kwargs=dict(pk=department.id)))
        )
        edit_btn = ARSimpleLink(
            icon=ARMaterialIcon('edit'),
            css_classes=['btn-outline-light', 'custom-btn', 'table-transition-btn'],
            html_params=dict(href=reverse('dashboard:department_update', kwargs=dict(pk=department.id)))
        )
        cells = [
            TD(department.id),
            TD(department.name),
            TD(department.organization.name),
            TD(employees_edit_btn, css_classes=['action-cell']),
            TD(edit_btn, css_classes=['action-cell'])
        ]

        return TR(cells)


class DepartmentEmployeesTemplateTable(BaseTemplateTable):
    """
    A table class for Department Employees displaying on the dashboard page.
    """

    empty_table_text = _('No data')

    def __init__(self, *args, **kwargs):
        self.department_pk = kwargs.pop('department_pk')
        super().__init__(*args, **kwargs)

    def get_header_rows(self) -> List[TableRowType]:
        cells = [
            TH('', css_classes=['action-cell']),
            TH('', css_classes=['action-cell']),
            TH(_('Employee ID'), ordering='id'),
            TH(_('First name'), ordering='first_name'),
            TH(_('Last name'), ordering='last_name'),
            TH(_('Country'), ordering='city__country__name'),
            TH(_('City'), ordering='city__name'),
            TH('', css_classes=['action-cell'])
        ]

        return [TR(cells)]

    def get_body_row(self, index: int, data_item: Any) -> TableRowType:
        employee = data_item  # type: User
        add_employee = ARSimpleLink(
            icon=ARMaterialIcon('add'),
            css_classes=['btn-outline-light', 'custom-btn', 'table-transition-btn', 'js-table_item_add'],
            html_params={
                'data-url': reverse('utils:cache_table_item', kwargs=dict(key='employee_add', value=employee.id))
            }
        )
        delete_employee = ARSimpleLink(
            icon=ARMaterialIcon('delete'),
            css_classes=['custom-btn', 'red-btn', 'table-transition-btn', 'js-table_item_delete'],
            html_params={
                'data-url': reverse('utils:cache_table_item', kwargs=dict(key='employee_remove', value=employee.id))
            }
        )
        checked_for_adding_icon = ARMaterialIcon(
            'done_all', css_classes=['table-item-add-icon', 'js-table_item_add_icon']
        )
        checked_for_deletion_icon = ARMaterialIcon(
            'close', css_classes=['table-item-delete-icon', 'js-table_item_delete_icon']
        )

        ids_to_add = self.request.session.get('employee_add', '').split(',')
        ids_to_remove = self.request.session.get('employee_remove', '').split(',')

        if str(employee.id) in ids_to_add:
            checked_for_adding_icon.css_classes.append('active')
        if str(employee.id) in ids_to_remove:
            checked_for_deletion_icon.css_classes.append('active')

        cells = [
            TD(checked_for_adding_icon, css_classes=['action-cell']),
            TD(checked_for_deletion_icon, css_classes=['action-cell']),
            TD(employee.id),
            TD(employee.first_name),
            TD(employee.last_name),
            TD(ga_(employee, 'city__country__name')),
            TD(employee.city),
            TD(add_employee if (employee.department is None or employee.department.id != self.department_pk)
               else delete_employee, css_classes=['action-cell'])
        ]

        return TR(cells, html_params={'data-table-item-id': employee.id})

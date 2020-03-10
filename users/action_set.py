from action_set.action_set import BreadcrumbsSet, ActionSet
from action_set.components import ActionLink, ActionButton
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from utils.components import MaterialIcon


class DashboardBreadcrumbs(BreadcrumbsSet):
    """
    Dashboard breadcrumbs realization.
    """

    template = 'components/breadcrumbs.html'
    active_crumb_css_class = 'active-crumb'

    # Crumbs
    dashboard = ActionLink(_('Dashboard'))

    # Employees
    employees = ActionLink(_('Employees'), html_params={'href': reverse_lazy('dashboard:employees')})
    employee_create = ActionLink(_('Employee create'), html_params={'href': reverse_lazy('dashboard:employee_create')})
    employee_update = ActionLink(_('Employee update'))

    # Departments
    departments = ActionLink(_('Departments'), html_params={'href': reverse_lazy('dashboard:departments')})
    department_create = ActionLink(
        _('Department create'), html_params={'href': reverse_lazy('dashboard:department_create')}
    )
    department_update = ActionLink(_('Department update'))
    department_details = ActionLink(_('Department details'))

    # Countries
    countries = ActionLink(_('Countries'), html_params={'href': reverse_lazy('dashboard:countries')})
    country_create = ActionLink(_('Country create'), html_params={'href': reverse_lazy('dashboard:country_create')})
    country_update = ActionLink(_('Country update'))

    # Cities
    cities = ActionLink(_('Cities'), html_params={'href': reverse_lazy('dashboard:cities')})
    city_create = ActionLink(_('City create'), html_params={'href': reverse_lazy('dashboard:city_create')})
    city_update = ActionLink(_('City update'))

    # Organizations
    organizations = ActionLink(_('Organizations'), html_params={'href': reverse_lazy('dashboard:organizations')})
    organization_create = ActionLink(
        _('Organization create'), html_params={'href': reverse_lazy('dashboard:organization_create')}
    )
    organization_update = ActionLink(_('Organization update'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        crumbs = [
            'country_update', 'employee_update', 'city_update', 'organization_update', 'department_update',
            'department_details'
        ]
        for crumb in crumbs:
            if crumb in self.actions:
                self.actions[crumb].html_params = {
                    'href': reverse_lazy(f'dashboard:{crumb}', kwargs=self.view_kwargs)
                }


class DashboardActionSet(ActionSet):
    """
    Action Set for rendering dashboard actions.
    """

    create = ActionLink(
        _('Create'),
        icon=MaterialIcon('add'),
        css_classes=['btn-outline-light custom-btn content-block-toolbar-btn']
    )
    save_form = ActionButton(
        _('Save'),
        icon=MaterialIcon('save'),
        css_classes=['btn-outline-light', 'custom-btn', 'content-block-toolbar-btn'],
        html_params={
            'type': 'button',
            'data-form-submit': '.js-detached_from'
        }
    )
    save_table_selection = ActionButton(
        _('Save selection'),
        icon=MaterialIcon('assignment_turned_in'),
        css_classes=['btn-outline-light', 'custom-btn', 'content-block-toolbar-btn'],
        html_params={
            'type': 'button',
            'data-floating-window-open': 'confirm_action'
        }
    )
    reset_table_selection = ActionButton(
        _('Reset selection'),
        icon=MaterialIcon('delete'),
        css_classes=['btn-outline-light', 'custom-btn', 'content-block-toolbar-btn'],
        html_params={
            'type': 'button',
            'data-floating-window-open': 'confirm_action'
        }
    )
    delete = ActionButton(
        _('Delete'),
        icon=MaterialIcon('close'),
        css_classes=['btn-outline-light', 'custom-btn', 'red-btn', 'content-block-toolbar-btn'],
        html_params={
            'type': 'button',
            'data-floating-window-open': 'confirm_action'
        }
    )

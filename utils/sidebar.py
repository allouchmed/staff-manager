from action_set.action_set import ActionSetMenuMixin, ActionSet, ActionSetGroup
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from utils.components import MaterialIcon, SidebarActionLink


class SidebarBaseActionSet(ActionSetMenuMixin, ActionSet):
    """
    The base class for sidebar menu.
    """

    _MENU_ITEM_VIEW_ATTR = 'sidebar_active_items'


class MainMenuActionSet(SidebarBaseActionSet):
    """
    Action Set for "Main menu" sidebar group.
    """

    group_name: str = _('Main menu')

    employees = SidebarActionLink(
        _('Employees'),
        icon=MaterialIcon('face'),
        css_classes=['sidebar-btn', 'waves-btn'],
        html_params={'href': reverse_lazy('dashboard:employees')}
    )
    organizations = SidebarActionLink(
        _('Organizations'),
        icon=MaterialIcon('dns'),
        css_classes=['sidebar-btn', 'waves-btn'],
        html_params={'href': reverse_lazy('dashboard:organizations')}
    )
    departments = SidebarActionLink(
        _('Departments'),
        icon=MaterialIcon('storage'),
        css_classes=['sidebar-btn', 'waves-btn'],
        html_params={'href': reverse_lazy('dashboard:departments')}
    )


class RelatedObjectsActionSet(SidebarBaseActionSet):
    """
    Action Set for "Related objects" sidebar group.
    """

    group_name: str = _('Related objects')

    countries = SidebarActionLink(
        _('Countries'),
        icon=MaterialIcon('landscape'),
        css_classes=['sidebar-btn', 'waves-btn'],
        html_params={'href': reverse_lazy('dashboard:countries')}
    )
    cities = SidebarActionLink(
        _('Cities'),
        icon=MaterialIcon('assessment'),
        css_classes=['sidebar-btn', 'waves-btn'],
        html_params={'href': reverse_lazy('dashboard:cities')}
    )


class SidebarMenu(ActionSetGroup):
    """
    Action Set Group for grouping sidebar menu items.
    """

    main_menu = MainMenuActionSet
    related_objects = RelatedObjectsActionSet

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sidebar_is_open = self.request.session.get('main_sidebar_is_open')

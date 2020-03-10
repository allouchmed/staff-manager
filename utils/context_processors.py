from dev_tools.template.mixins import HttpRequestType
from django.urls import Resolver404

from utils.sidebar import SidebarMenu


def sidebar_context_processor(request: HttpRequestType):
    """
    Context processor for adding sidebar menu to the page.
    """

    try:
        sidebar = SidebarMenu(request=request)
    except Resolver404:
        sidebar = None

    return {'sidebar_menu': sidebar}

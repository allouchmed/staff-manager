from django.urls import path

from utils.views import SidebarModeSaveView, CacheTemplateTableItems

app_name = 'utils'

urlpatterns = [
    path('sidebar-mode/save/<sidebar_id>/<state>/', SidebarModeSaveView.as_view(), name='sidebar_mode_save'),
    path('cache-table-item/<key>/<value>/', CacheTemplateTableItems.as_view(), name='cache_table_item')
]

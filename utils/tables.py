from django.utils.translation import ugettext_lazy as _
from template_tables.components import TemplateTablePagination


class TemplateTableCustomPagination(TemplateTablePagination):
    """
    Custom class for tables pagination for customization.
    """

    translation: dict = {
        'page_range': _('Entries on the page'),
        'pages_info': f'%s / {_("Total entries")}: %s'
    }

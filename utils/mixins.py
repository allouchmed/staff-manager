from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django_filters.views import FilterView
from template_tables.mixins import TemplateTableViewMixin, TemplateTablePaginationMixin

from utils.tables import TemplateTableCustomPagination


class TemplateTableCustomPaginationMixin(TemplateTablePaginationMixin):
    """
    Custom pagination mixin view which provides custom pagination class.
    """

    pagination_class = TemplateTableCustomPagination


class CustomFilterTableView(TemplateTableViewMixin, TemplateTableCustomPaginationMixin, FilterView):
    """
    Mixin for template table with pagination and filter support.
    """

    strict = False


class TitleViewMixin:
    """
    Mixin for adding title to template's context.
    """

    title: str = ''

    def get_title(self) -> str:
        return self.title

    def get_context_data(self, **kwargs):
        return super().get_context_data(title=self.get_title(), **kwargs)


class POSTMessagesMixin:
    """
    Mixin for adding alert-messages to views (form views and delete view).
    """

    form_error_message: str = _('Some errors were found while saving form data! Please, check messages below.')
    form_success_message: str = _('Data has been saved successfully!')
    deletion_success_message: str = _('Object has been deleted successfully!')

    def form_invalid(self, form):
        self.set_form_error_message()
        return super().form_invalid(form)

    def form_valid(self, form):
        self.set_form_success_message()
        return super().form_valid(form)

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        self.set_deletion_success_message()
        return response

    def set_form_error_message(self) -> None:
        message = self.get_form_error_message()
        if message:
            messages.error(self.request, message)

    def set_form_success_message(self) -> None:
        message = self.get_form_success_message()
        if message:
            messages.success(self.request, message)

    def set_deletion_success_message(self) -> None:
        message = self.get_deletion_success_message()
        if message:
            messages.success(self.request, message)

    def get_deletion_success_message(self) -> str:
        return self.deletion_success_message

    def get_form_error_message(self) -> str:
        return self.form_error_message

    def get_form_success_message(self) -> str:
        return self.form_success_message

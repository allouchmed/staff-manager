from django.http import HttpResponse
from django.views import View


class SidebarModeSaveView(View):
    """
    View for saving sidebar mode (collapsed/expanded) into session.
    """

    def get(self, request, *args, **kwargs):
        state = self.kwargs.get('state')
        key = self.kwargs.get('sidebar_id', '')
        if state and key:
            key += '_is_open'
            request.session[key] = True if state == 'true' else False

        return HttpResponse('OK', status=200)


class CacheTemplateTableItems(View):
    """
    View for caching table item choices to session.
    """

    def get(self, request, *args, **kwargs):
        key = self.kwargs.get('key')
        value_to_add = self.kwargs.get('value')
        exist_values = self.request.session.get(key)
        new_value = [value_to_add]
        if exist_values:
            exist_values = exist_values.split(',')
            if value_to_add in exist_values:
                exist_values.remove(value_to_add)
                new_value = exist_values
            else:
                new_value += exist_values

        self.request.session[key] = ','.join(new_value)

        return HttpResponse('OK', status=200)

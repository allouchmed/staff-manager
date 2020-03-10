from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView

from utils.components import Img


class LandingView(TemplateView):
    """
    View for landing page.
    """

    template_name = 'landing.html'


_error_icon = Img(html_params={'src': '/assets/img/logo_big_anim_3.png', 'width': '200', 'height': '200'})


def error_400_view(request, *args, **kwargs):
    context = dict(
        message_subject=_('Error on server. Error Code: 400.'),
        message_text=_('Error processing request. Please try again later.'),
        message_icon=_error_icon
    )
    return render(request, 'system.html', context, status=400)


def error_403_view(request, *args, **kwargs):
    context = dict(
        message_subject=_('Access error. Error Code: 403.'),
        message_text=_('You do not have access to this page.'),
        message_icon=_error_icon
    )
    return render(request, 'system.html', context, status=404)


def error_404_view(request, *args, **kwargs):
    context = dict(
        message_subject=_('The requested page was not found. Error Code: 404.'),
        message_text=_('The path in the address bar may be incorrect or the page has been deleted.'),
        message_icon=_error_icon
    )
    return render(request, 'system.html', context, status=404)


def error_500_view(request, *args, **kwargs):
    context = dict(
        message_subject=_('Error on server. Error Code: 500.'),
        message_text=_('An unexpected error has occurred on the server. Please wait, it will be fixed soon.'),
        message_icon=_error_icon
    )
    return render(request, 'system.html', context, status=500)

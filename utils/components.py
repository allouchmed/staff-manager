from action_set.components import BaseAction
from dev_tools.template.components import BaseButton, BaseHTMLElement


# region Auto rendered elements

class MaterialIcon(BaseHTMLElement):
    """
    A class for "material-icon" icon
    """

    tag = 'i'
    default_css_classes = ['material-icons']


class ARMaterialIcon(MaterialIcon):
    """
    Material icon element.
    """

    def __str__(self):
        return self.render()


class ARSimpleButton(BaseButton):
    """
    Simple auto rendered button.
    """

    tag = 'button'
    default_html_params = {'type': 'button'}

    def __str__(self):
        return self.render()


class ARSimpleLink(BaseButton):
    """
    Simple auto rendered link.
    """

    tag = 'a'

    def __str__(self):
        return self.render()


class SidebarActionLink(BaseButton, BaseAction):
    """
    Link for use in the sidebar.
    """

    tag = 'a'
    html_string = '<%(tag)s %(html_params)s>' \
                  '%(icon)s <span class="title hide-on-sidebar-close">%(data)s</span>' \
                  '<span class="inner-btn-border-right"></span></%(tag)s>'


class Img(BaseHTMLElement):
    """
    HTML image.
    """

    tag = 'img'
    html_string = '<%(tag)s %(html_params)s>'

    def __init__(self, **kwargs) -> None:
        super().__init__(data='', **kwargs)

    def __str__(self):
        return self.render()

# endregion

# -*- coding: utf-8 -*-
from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives


def oneorzero(argument):
    """Conversion function for the various options that let you choose between 1 and 0."""
    return directives.choice(argument, ('0', '1'))


def theme(argument):
    """Conversion function for the "theme" option."""
    return directives.choice(argument, ('light', 'dark'))


def align(argument):
    """Conversion function for the "align" option."""
    return directives.choice(argument, ('left', 'center', 'right'))


class EmbedlyCard(Directive):
    required_arguments = 1
    optional_arguments = 10

    option_spec = {
        'title': directives.unchanged,
        'description': directives.unchanged,
        'via': directives.unchanged,
        'chrome': oneorzero,
        'theme': theme,
        'image': directives.unchanged,
        'embed': directives.unchanged,
        'controls': oneorzero,
        'width': directives.nonnegative_int,
        'align': align,
        'recommend': oneorzero,
        'key': directives.unchanged,
    }

    final_argument_whitespace = False
    has_content = False

    def run(self):
        url = self.arguments[0].strip()
        title = ""
        description = ""
        data_card_via = ""
        data_card_chrome = 0
        data_card_theme = "light"
        data_card_image = ""
        data_card_embed = ""
        data_card_controls = 1
        data_card_width = ""
        data_card_align = "center"
        data_card_recommend = 1
        data_card_key = ""

        if 'title' in self.options:
            title = self.options['title']
        if 'description' in self.options:
            description = self.options['description']
        if 'via' in self.options:
            data_card_via = self.options['via']
        if 'chrome' in self.options:
            data_card_chrome = self.options['chrome']
        if 'theme' in self.options:
            data_card_theme = self.options['theme']
        if 'image' in self.options:
            data_card_image = self.options['image']
        if 'embed' in self.options:
            data_card_embed = self.options['embed']
        if 'controls' in self.options:
            data_card_controls = self.options['controls']
        if 'width' in self.options:
            data_card_width = self.options['width']
        if 'align' in self.options:
            data_card_align = self.options['align']
        if 'recommend' in self.options:
            data_card_recommend = self.options['recommend']
        if 'key' in self.options:
            data_card_key = self.options['key']

        linkHTML = "<blockquote class='embedly-card' data-card-via='{via}' data-card-chrome='{chrome}' data-card-theme='{theme}' data-card-image='{image}' data-card-embed='{embed}' data-card-controls='{controls}' data-card-width='{width}' data-card-align='{align}' data-card-recommend='{recommend}' data-card-key='{key}'><h4><a href='{url}'>{title}</a></h4><p>{description}</p></blockquote>".format(url=url, title=title, description=description, via=data_card_via, chrome=data_card_chrome, theme=data_card_theme, image=data_card_image, embed=data_card_embed, controls=data_card_controls, width=data_card_width, align=data_card_align, recommend=data_card_recommend, key=data_card_key)  # noqa

        scriptHTML = """
            <script>
            !function(a){
                var b="embedly-platform",c="script";
                if(!a.getElementById(b)){
                    var d=a.createElement(c);
                    d.id=b;
                    d.src=("https:"===document.location.protocol?"https":"http")+"://cdn.embedly.com/widgets/platform.js";
                    var e=document.getElementsByTagName(c)[0];e.parentNode.insertBefore(d,e)}
                }(document);
            </script>
            """

        return [nodes.raw('', linkHTML, format='html'),
                nodes.raw('', scriptHTML, format='html')]


def register():
    directives.register_directive('embedly-card', EmbedlyCard)

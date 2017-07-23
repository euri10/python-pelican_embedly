# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from docutils import nodes
from docutils.parsers.rst import directives, Directive


def oneorzero(argument):
    """Conversion function for the various options that let you choose between 1 and 0."""
    return directives.choice(argument, ('0', '1'))


def theme(argument):
    """Conversion function for the "data-card-theme" option."""
    return directives.choice(argument, ('light', 'dark'))


def align(argument):
    """Conversion function for the "data-card-align" option."""
    return directives.choice(argument, ('left', 'center', 'right'))


class EmbedlyCard(Directive):
    required_arguments = 1
    optional_arguments = 0

    option_spec = {
        'title': directives.unchanged,
        'data-card-via': directives.unchanged,
        'data-card-chrome': oneorzero,
        'data-card-theme': theme,
        'data-card-image': directives.unchanged,
        'data-card-embed': directives.unchanged,
        'data-card-controls': oneorzero,
        'data-card-width': directives.nonnegative_int,
        'data-card-align': align,
        'data-card-recommend': oneorzero,
        'data-card-key': directives.unchanged,
    }

    final_argument_whitespace = True
    has_content = True

    def run(self):
        url = self.arguments[0].strip()
        title = ""
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
        if 'data-card-via' in self.options:
            data_card_via = self.options['data-card-via']
        if 'data-card-chrome' in self.options:
            data_card_chrome = self.options['data-card-chrome']
        if 'data-card-theme' in self.options:
            data_card_theme = self.options['data-card-theme']
        if 'data-card-image' in self.options:
            data_card_image = self.options['data-card-image']
        if 'data-card-embed' in self.options:
            data_card_embed = self.options['data-card-embed']
        if 'data-card-controls' in self.options:
            data_card_controls = self.options['data-card-controls']
        if 'data-card-width' in self.options:
            data_card_width = self.options['data-card-width']
        if 'data-card-align' in self.options:
            data_card_align = self.options['data-card-align']
        if 'data-card-recommend' in self.options:
            data_card_recommend = self.options['data-card-recommend']
        if 'data-card-key' in self.options:
            data_card_key = self.options['data-card-key']

        linkHTML = "<a class='embedly-card' data-card-via='{2}' data-card-chrome='{3}' data-card-theme='{4}' data-card-image='{5}' data-card-embed='{6}' data-card-controls='{7}' data-card-width='{8}' data-card-align='{9}' data-card-recommand='{10}' data-card-key='{11}' href='{0}'>{1}</a>".format(url, title, data_card_via, data_card_chrome, data_card_theme, data_card_image, data_card_embed, data_card_controls, data_card_width, data_card_align, data_card_recommend, data_card_key)
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

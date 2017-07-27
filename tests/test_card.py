import pytest
from docutils.core import publish_string
from docutils.parsers.rst import directives

from pelican_embedly.card_rst import EmbedlyCard

HTML = [
    b"<blockquote class='embedly-card' data-card-via='' data-card-chrome='0' data-card-theme='light' data-card-image='' data-card-embed='' data-card-controls='1' data-card-width='' data-card-align='left' data-card-recommend='1' data-card-key=''>",  # noqa
    b"<h4><a href='http://example.com'>myTitle</a></h4>",
]


def test_directive_simple():
    directives.register_directive('embedly-card', EmbedlyCard)
    d = '.. embedly-card:: http://example.com\n\t:title: myTitle\n\t:align: left\n\t'
    res = publish_string(d, writer_name='html', )

    passed = True

    for line in HTML:
        if line not in res:
            passed = False
            break
    assert passed

# TODO bad user input on restricted stuff like align


@pytest.mark.parametrize("url", ['http://embed.ly', ])
@pytest.mark.parametrize("via", ['http://viaurl1.com', 'http://viaurl2.com'])
@pytest.mark.parametrize("chrome", ['0', '1'])
@pytest.mark.parametrize("theme", ['light', 'dark'])
@pytest.mark.parametrize("image", ['http://imageurl1.com', 'http://imageurl2.com'])
@pytest.mark.parametrize("embed", ['http://embedurl1.com', 'http://embedurl2.com'])
@pytest.mark.parametrize("controls", ['0', '1'])
@pytest.mark.parametrize("width", ['100'])
@pytest.mark.parametrize("align", ['center', 'left', 'right'])
@pytest.mark.parametrize("recommend", ['0', '1'])
@pytest.mark.parametrize("key", ['', 'embedkey'])
def test_directive_args(url, via, chrome, theme, image, embed, controls, width, align, recommend, key):
    directives.register_directive('embedly-card', EmbedlyCard)
    title = 'title'
    description = 'description'
    # d = '.. embedly-card:: {url}'.format(url=url) + ''.join(['\n\t:' + k+': '+v for k, v in class_options.items()]) +\
    #      '\n\t:align: ' + align + '\n\t:theme: ' + theme
    d = '.. embedly-card:: {url}'.format(url=url) + '\n\t:via: ' + via + '\n\t:chrome: ' + chrome + '\n\t:theme: ' +\
        theme + '\n\t:image: ' + image + '\n\t:embed: ' + embed + '\n\t:controls: ' + controls + '\n\t:width: ' +\
        width + '\n\t:align: ' + align + '\n\t:recommend: ' + recommend + '\n\t:key: ' + key

    res = publish_string(d, writer_name='html', )
    HTML_RESULT = "<blockquote class='embedly-card' data-card-via='{via}' data-card-chrome='{chrome}' " \
                  "data-card-theme='{theme}' data-card-image='{image}' data-card-embed='{embed}' " \
                  "data-card-controls='{controls}' data-card-width='{width}' data-card-align='{align}' " \
                  "data-card-recommend='{recommend}' data-card-key='{key}'>".format(title=title,
                                                                                    description=description,
                                                                                    via=via,
                                                                                    chrome=chrome,
                                                                                    theme=theme,
                                                                                    image=image,
                                                                                    embed=embed,
                                                                                    controls=controls,
                                                                                    width=width,
                                                                                    align=align,
                                                                                    recommend=recommend,
                                                                                    key=key)
    assert HTML_RESULT.encode() in res

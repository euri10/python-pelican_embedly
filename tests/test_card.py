from docutils.core import publish_string
from docutils.parsers.rst import directives
from pelican_embedly.card_rst import EmbedlyCard

# TEST_DIR = os.path.dirname(__file__)
# DATA_PATH = os.path.join(TEST_DIR, 'data')

HTML = [
    b"<blockquote class='embedly-card' data-card-via='' data-card-chrome='0' data-card-theme='light' data-card-image='' data-card-embed='' data-card-controls='1' data-card-width='' data-card-align='left' data-card-recommand='1' data-card-key=''>",  # noqa
    b"<h4><a href='http://example.com'>myTitle</a></h4>",
]

# TODO add parametrized pytest

def test_directive():
    directives.register_directive('embedly-card', EmbedlyCard)
    d = '.. embedly-card:: http://example.com\n\t:title: myTitle\n\t:align: left\n\t'
    res = publish_string(d, writer_name='html', )

    passed = True

    for line in HTML:
        if line not in res:
            passed = False
            break
    assert passed

import os

from pelican import Pelican, readers
from pelican.settings import DEFAULT_CONFIG
from pelican.utils import SafeDatetime

from pelican_embedly.card_rst import EmbedlyCard

TEST_DIR = os.path.dirname(__file__)
DATA_PATH = os.path.join(TEST_DIR, 'data')


def get_settings(**kwargs):
    settings = DEFAULT_CONFIG.copy()
    for key, value in kwargs.items():
        settings[key] = value
    return settings

def _path(*args):
    return os.path.join(DATA_PATH, *args)


def read_content_metadata(path, **kwargs):
    r = EmbedlyCard(settings=get_settings(**kwargs))
    return r.read(_path(path))


def read_file(path, **kwargs):
    r = readers.Readers(settings=get_settings(**kwargs))
    return r.read_file(base_path=DATA_PATH, path=path)


def assert_dict_contains(tested, expected):
    assert set(expected).issubset(set(tested)), 'Some keys are missing'
    for key, value in expected.items():
        assert tested[key] == value
    # assert all(item in superset.items() for item in subset.items())


def test_read_markdown_and_metadata():
    page = read_file('page.rst')
    assert page
    assert page.title == 'Some page'
    assert page.content == '<p>This is a simple markdown file</p>'


def test_typed_metadata():
    content, metadata = read_content_metadata('metadata.md')
    expected = {
        'title': 'Metadata',
        'list': ['a', 'b', 'c'],
        'date': SafeDatetime(2017, 1, 6, 22, 24),
        'int': 42,
        'bool': False,
        'summary': '<p>a summary</p>',
    }
    assert_dict_contains(metadata, expected)

def test_pelican_registeration():
    settings = get_settings(PLUGINS=['pelican_embedly'])
    Pelican(settings)


from pelican_embedly.cli import main


def test_main():
    assert main([]) == 0

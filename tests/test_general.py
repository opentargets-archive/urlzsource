from opentargets_urlzsource import URLZSource


def test_file():
    with URLZSource('tests/general.txt').open() as source:
        content = source.readlines()
        assert content == ["Foo"]
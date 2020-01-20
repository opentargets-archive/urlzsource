from opentargets_urlzsource import URLZSource


def test_file():
    with URLZSource('tests/general.txt').open() as source:
        content = source.readlines()
        assert content == ["Foo"]


def test_file_gz():
    with URLZSource('tests/general.txt.gz').open() as source:
        content = source.readlines()
        assert content == ["Foo"]


def test_file_zip():
    with URLZSource('tests/general.txt.zip').open() as source:
        content = source.readlines()
        assert content == ["Foo"]


def test_url():
    url = "https://raw.githubusercontent.com/opentargets/urlzsource/master/tests/general.txt"
    with URLZSource(url).open() as source:
        content = source.readlines()
        assert content == ["Foo"]


def test_file_url():
    with URLZSource('file://./tests/general.txt').open() as source:
        content = source.readlines()
        assert content == ["Foo"]

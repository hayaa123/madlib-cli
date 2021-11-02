from madlib_cli import __version__

from madlib_cli.madlib import parse_template , read_template , merge_function

def test_version():
    assert __version__ == '0.1.0'


def test_read_template():
    expected = "It was a {Adjective} and {Adjective} {Noun}."
    actual =  read_template("madlib_cli/assets/test.txt")
    assert expected == actual

def test_parse_template():
    expected = ["Adjective","Adjective","Noun"]
    actual = parse_template("It was a {Adjective} and {Adjective} {Noun}.")
    assert expected == actual

def test_merge_function():
    expected = "It was a fun and cool journy."
    actual = merge_function("It was a {Adjective} and {Adjective} {Noun}.",["fun","cool","journy"])
    assert expected == actual
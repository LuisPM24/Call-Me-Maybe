from src import Parser
from pytest import MonkeyPatch
import os


def test_parser1(monkeypatch: MonkeyPatch) -> None:
    """
    Test parser 1
    \n
    Checks if the parser can get the default values.
    """
    monkeypatch.setattr(
        "sys.argv",
        ["call-me-maybe"]
    )

    parser: Parser = Parser.get_args()

    assert parser.functions_definition_file == (
        "data/input/functions_definition.json"
    )
    assert parser.input_file == (
        "data/input/function_calling_tests.json"
    )
    assert parser.output_file == (
        "data/output/function_calling_results.json"
    )


def test_parser2(monkeypatch: MonkeyPatch) -> None:
    """
    Test parser 2
    \n
    Checks if the flag '--functions_definition' is functional.
    """
    monkeypatch.setattr(
        "sys.argv",
        [
            "call-me-maybe",
            "--functions_definition",
            "data/input/test.json"
        ]
    )

    with open("data/input/test.json", 'w') as fd:
        fd.write("")

    parser: Parser = Parser.get_args()

    assert parser.functions_definition_file == (
        "data/input/test.json"
    )
    assert parser.input_file == (
        "data/input/function_calling_tests.json"
    )
    assert parser.output_file == (
        "data/output/function_calling_results.json"
    )

    os.remove("data/input/test.json")


def test_parser3(monkeypatch: MonkeyPatch) -> None:
    """
    Test parser 3
    \n
    Checks if the flag '--input' is functional.
    """
    monkeypatch.setattr(
        "sys.argv",
        [
            "call-me-maybe",
            "--input",
            "data/input/test.json"
        ]
    )

    with open("data/input/test.json", 'w') as fd:
        fd.write("")

    parser: Parser = Parser.get_args()

    assert parser.functions_definition_file == (
        "data/input/functions_definition.json"
    )
    assert parser.input_file == "data/input/test.json"
    assert parser.output_file == (
        "data/output/function_calling_results.json"
    )

    os.remove("data/input/test.json")


def test_parser4(monkeypatch: MonkeyPatch) -> None:
    """
    Test parser 4
    \n
    Checks if the flag '--output' is functional.
    """
    monkeypatch.setattr(
        "sys.argv",
        [
            "call-me-maybe",
            "--output",
            "data/output/test.json"
        ]
    )

    with open("data/input/test.json", 'w') as fd:
        fd.write("")

    parser: Parser = Parser.get_args()

    assert parser.functions_definition_file == (
        "data/input/functions_definition.json"
    )
    assert parser.input_file == (
        "data/input/function_calling_tests.json"
    )
    assert parser.output_file == ("data/output/test.json")

    os.remove("data/input/test.json")

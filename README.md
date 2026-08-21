*This project has been created as part of the 42 curriculum by lupalomi*

# Description

## Algorithm explanation

## Design decisions
### Parser - Pydantic and argparse
The parser class implements **Pydantic** and **argparse** to set the given values. Argparse set the provided flags while Pydantic validates.

### Parser - Default values

| Flag command | Default value |
|:------------|:-------------|
| *--functions_definition* | data/input/functions_definition.json |
| *--input* | data/input/function_calling_tests.json |
| *--output* | data/output/function_calling_results.json |

## Performance analysis

## Challenges faced
### Parser - Argparse
Since this is the first project where I implement *argparse* library, it took me many hours to understand how it works and how to implement it on my code.

## Testing strategy

## Example usage

# Instructions

# Resources

- [How to create your pyproject](https://docs.squarecloud.app/es/articles/how-to-create-your-pyproject)
- [Pytest documentation](https://docs.pytest.org/en/stable/)
- [Argparser function documentation](https://docs.python.org/es/3/library/argparse.html)
- [Validate file permissions and access](https://labex.io/es/tutorials/python-how-to-verify-python-file-access-422110)

# Bonus
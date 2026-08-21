import argparse
import os
from pydantic import BaseModel, model_validator, Field
from typing import Optional


class Parser(BaseModel):
    """
    Parser class:
    \n
    This class is mainly used to take the arguments provided by the user and
    validate them.
    """
    functions_definition_file: Optional[str] = Field(default=None)
    input_file: Optional[str] = Field(default=None)
    output_file: Optional[str] = Field(default=None)

    @model_validator(mode="after")
    def validate_parser(self) -> "Parser":
        if self.functions_definition_file is None:
            self.functions_definition_file = "data/input/" \
                "functions_definition.json"
        if self.input_file is None:
            self.input_file = "data/input/function_calling_tests.json"
        if self.output_file is None:
            self.output_file = "data/output/function_calling_results.json"

        permissions = {
            "functions": os.access(self.functions_definition_file, os.R_OK),
            "input": os.access(self.input_file, os.R_OK),
            "output": os.access(self.output_file, os.W_OK)
        }
        if permissions["functions"] is False:
            raise OSError(f"Cannot read {self.functions_definition_file}")
        if permissions["input"] is False:
            raise OSError(f"Cannot read {self.input_file}")
        if os.path.exists(self.output_file) and permissions["output"] is False:
            raise OSError(f"Cannot write on {self.output_file}")
        return self

    @classmethod
    def get_args(cls) -> "Parser":
        new_args = argparse.ArgumentParser()

        new_args.add_argument(
            "--functions_definition",
            dest="functions_definition_file",
            type=str,
            default=None
        )

        new_args.add_argument(
            "--input",
            dest="input_file",
            type=str,
            default=None
        )

        new_args.add_argument(
            "--output",
            dest="output_file",
            type=str,
            default=None
        )

        args = new_args.parse_args()

        return cls(**vars(args))

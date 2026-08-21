from classes import Parser


def main() -> None:
    """Main function. Runs the application"""
    try:
        parser = Parser().get_args()
        print("Functions definition file: "
              f"{parser.functions_definition_file}")
        print(f"Input file: {parser.input_file}")
        print(f"Output file: {parser.output_file}")
    except Exception as e:
        print(f"Error - {e}")


if __name__ == "__main__":
    main()

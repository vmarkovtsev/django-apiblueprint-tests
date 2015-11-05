import argparse
import os

from .generator import TestsGenerator


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--template", help="Jinja2 template to use",
                        default=os.path.abspath(os.path.join(
                            os.path.dirname(__file__), "tests.jinja2")))
    parser.add_argument("-b", "--base-class",
                        help="Fully qualified base class for tests")
    parser.add_argument("-c", "--no-comments", action="store_true",
                        help="Do not add docstrings to classes and methods")
    parser.add_argument("-o", "--output", help="Output Python file with tests")
    parser.add_argument("-g", "--html2text", action="store_true",
                        help="Use html2text to convert descriptions (makes "
                             "this program licensed under GPLv3!)")
    parser.add_argument("input", nargs='+', help="Input APIBlueprint files")
    args = parser.parse_args()
    generator = TestsGenerator(
        args.template, include_comments=not args.no_comments,
        base_class=args.base_class, html2text=args.html2text, *args.input)
    generator.generate(args.output)

if __name__ == "__main__":
    main()

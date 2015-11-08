# -*- coding: utf-8 -*-
"""
Django REST framework tests generator which is based on API Blueprint
(https://apiblueprint.org/) documents.
Released under New BSD License.

Copyright © 2015, Vadim Markovtsev :: AO InvestGroup
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of the AO InvestGroup nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL VADIM MARKOVTSEV BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
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
    parser.add_argument("--disable-html2text", action="store_true",
                        help="Do not use html2text to convert descriptions "
                             "(otherwise it makes this program licensed under "
                             "GPLv3!)")
    parser.add_argument("input", nargs='+', help="Input APIBlueprint files")
    args = parser.parse_args()
    generator = TestsGenerator(
        args.template, include_comments=not args.no_comments,
        base_class=args.base_class, html2text=not args.disable_html2text,
        *args.input)
    generator.generate(args.output)

if __name__ == "__main__":
    main()

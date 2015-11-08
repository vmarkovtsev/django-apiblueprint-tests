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

import codecs
from jinja2 import Environment, FileSystemLoader
from markdown import Markdown
import sys
from transliterate import translit
from transliterate.exceptions import LanguageDetectionError


class TestsGenerator(object):
    def __init__(self, templatefile, *apifiles, **kwargs):
        if len(apifiles) == 0:
            raise ValueError("There must be at least one APIBlueprint file "
                             "specified")
        include_comments = kwargs.pop("include_comments", True)
        base_class = kwargs.pop("base_class", None)
        if base_class is None:
            base_class = "rest_framework.test.APITestCase"
        self._use_html2text = kwargs.pop("html2text", False)
        m = Markdown(extensions=["plueprint"])
        m.set_output_format("apiblueprint")
        with codecs.open(apifiles[0], "r", "utf-8") as fin:
            self._api = m.convert(fin.read())
        for f in apifiles[1:]:
            with codecs.open(f, "r", "utf-8") as fin:
                self._api.merge(m.convert(fin.read()))
        env = Environment(loader=FileSystemLoader(templatefile),
                          autoescape=False, trim_blocks=True,
                          lstrip_blocks=True,
                          extensions=("jinja2.ext.loopcontrols",))
        env.filters["symbolize"] = self._symbolize
        env.filters["html2text"] = self._html2text
        self._template = env.get_template("")
        self._include_comments = include_comments
        self._base_class = base_class[base_class.rfind('.') + 1:]
        self._base_module = base_class[:-len(self._base_class) - 1]
        self._counter = 1

    def _html2text(self, value, indent):
        if self._use_html2text:
            from html2text import html2text
            value = html2text(value)
        return "\n" \
            .join("%s%s" % (" " * indent, l) for l in value.split("\n")) \
            .strip()

    def _symbolize(self, value):
        if sys.version_info[0] < 3:
            try:
                value = translit(value, reversed=True)
            except LanguageDetectionError:
                pass
        while not value[0].isalpha() and value[0] != "_":
            value = value[1:]
        i = 1
        while i < len(value):
            if not value[i].isalnum() and value[i] != "_":
                value = value[:i] + value[i + 1:]
            else:
                i += 1
        if not value:
            value = "FixMyName%d" % self._counter
            self._counter += 1
        return value

    @staticmethod
    def _underline(txt, with_char):
        return with_char * len(txt) if txt else ""

    def generate(self, output_file):
        self._template.stream(
            api=self._api, include_comments=self._include_comments,
            class_base_module=self._base_module, class_base=self._base_class,
            underline=self._underline) \
            .dump(output_file)

django-apiblueprint-tests
=========================

This is a tool to automatically generate tests for a Django REST framework based
applications from [APIBlueprint](https://apiblueprint.org/) documents.

It uses [plueprint](https://github.com/vmarkovtsev/plueprint) parser and
[Jinja2](http://jinja.pocoo.org) templates.

Released under New BSD license.

### Usage
```
python -m django-apiblueprint-tests api_blueprint1.md api_blueprint2.md -o tests.py
python -m django-apiblueprint-tests --help
```
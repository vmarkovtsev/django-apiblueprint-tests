from setuptools import setup
import os


def parse_requirements():
    with open(os.path.join(os.path.dirname(__file__),
                           "requirements.txt"), "r") as fin:
        return fin.read().split("\n")


setup(
    name="plueprint",
    description="Django REST framework tests generator which is based on API "
                "Blueprint (https://apiblueprint.org/) documents.",
    version="0.1.0",
    license="New BSD",
    author="Vadim Markovtsev",
    author_email="gmarkhor@gmail.com",
    url="https://github.com/vmarkovtsev/django-apiblueprint-tests",
    download_url='https://github.com/vmarkovtsev/django-apiblueprint-tests',
    packages=["django-apiblueprint-tests"],
    package_dir={"django-apiblueprint-tests": "."},
    keywords=["blueprint", "apiblueprint"],
    install_requires=parse_requirements(),
    package_data={'': ['requirements.txt', 'LICENSE', 'README.md',
                       'tests.jinja2']},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Software Development :: Libraries"
    ]
)

#!/usr/bin/env python3

from pathlib import Path

from setuptools import setup

root = Path(__file__).parent
long_description = (root / "README.md").read_text()

setup(
    name = "go-parse-a2l",
    version = "1.1.0",
    description = "A script to parse an a2l file and turn it into json",
    url="https://github.com/GOcontroll/go-parse-a2l",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="GOcontroll",
    author_email="info@gocontroll.com",
    maintainer="Maud Spierings",
    packages=["go_parse_a2l"],
    entry_points={
        "console_scripts": [
            "go-parse-a2l = go_parse_a2l.parse_a2l:parse_a2l",
        ]
    },
    python_requires=">=3.9",
)

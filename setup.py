# -*- utf-8 -*-

from setuptools import setup


setup(
    name="Sleeper",
    description="Super secret things.",
    version=0.1,
    author="Tanner Lake, Jake Anderson",
    license="MIT",
    py_modules=[
        "scrape_it",
    ],
    package_dir={"": "src"},
    install_requires=[
        "bs4",
        "selenium"
    ],
    extras_require={
        "test": [
            "pytest",
            "pytest-cov",
            "tox",
        ],
    },
)

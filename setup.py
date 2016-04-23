# -*- utf-8 -*-

from setuptools import setup


tests_require = [
    'pytest',
    'pytest-cov',
    'tox',
]


setup(
    name="Sleeper",
    description="Super secret things.",
    version=0.1,
    author="Tanner Lake, Jake Anderson",
    license="MIT",
    py_modules=[
        "sleeper",
    ],
    package_dir={"": "src"},
    test_suite="test",
    install_requires=[
        'slacker',
    ],
    extras_require={
        "test": tests_require,
    },
)

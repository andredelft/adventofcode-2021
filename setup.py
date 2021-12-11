from setuptools import setup

setup(
    name="aoc_cli",
    version="0.1.0",
    py_modules=["aoc_cli"],
    install_requires=[
        "Click",
        "PyYAML",
    ],
    entry_points={
        "console_scripts": [
            "new-day = aoc_cli.cli:gen_day",
            "run-day = aoc_cli.cli:run_day",
        ],
    },
)

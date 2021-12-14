import click
import yaml
from pathlib import Path
import os
import re

CDIR = Path(__file__).parent

TEMPLATE_FILE = CDIR / "_template.py"
TEST_TEMPLATE_FILE = CDIR / "_test_template.py"
ENTRYPOINTS_FILE = Path("day_entrypoints.yml")

with TEMPLATE_FILE.open() as f:
    TEMPLATE = f.read()

with TEST_TEMPLATE_FILE.open() as f:
    TEST_TEMPLATE = f.read()

with ENTRYPOINTS_FILE.open() as f:
    ENTRYPOINTS = yaml.safe_load(f)


def add_entrypoint(day_number: int, filename: Path) -> None:
    ENTRYPOINTS[day_number] = str(filename.stem)
    with open(ENTRYPOINTS_FILE, "w") as f:
        yaml.dump(ENTRYPOINTS, f)


def gen_day_dir(day_number: int) -> Path:
    return Path(f"day_{day_number:>02}")


@click.command()
@click.argument("module_name")
def gen_day(module_name):
    day_number = 1
    while gen_day_dir(day_number).is_dir():
        day_number += 1

    module_name = Path(module_name).stem
    filename = Path(module_name).with_suffix(".py")

    add_entrypoint(day_number, filename)

    day_dir = gen_day_dir(day_number)
    day_dir.mkdir(parents=True, exist_ok=True)

    # Main code file
    with (day_dir / filename).open("w") as f:
        f.write(TEMPLATE)

    # Blank input file
    with (day_dir / "input.txt").open("w") as f:
        pass

    # Test file
    test_template = re.sub(r"(?<!\w)_template(?!\w)", module_name, TEST_TEMPLATE)

    with (day_dir / f"test_{day_dir.stem}.py").open("w") as f:
        f.write(test_template)


@click.command()
@click.argument("day_number", type=int)
def run_day(day_number):
    entrypoint = ENTRYPOINTS.get(day_number)
    if not entrypoint:
        raise click.ClickException(f"No entrypoint found for day {day_number}")
    os.system(f'python {gen_day_dir(day_number) / Path(entrypoint).with_suffix(".py")}')


@click.command()
@click.argument("day_number", type=int)
def test_day(day_number):
    day_dir = gen_day_dir(day_number)
    test_file = f"test_{day_dir.stem}.py"
    os.system(f"python {day_dir / test_file}")

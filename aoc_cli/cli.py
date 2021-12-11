import click
import yaml
from pathlib import Path
import os

CDIR = Path(__file__).parent

TEMPLATE_FILE = CDIR / "_template.py"
ENTRYPOINTS_FILE = CDIR / "day_entrypoints.yml"

with open(TEMPLATE_FILE) as f:
    TEMPLATE = f.read()

with open(ENTRYPOINTS_FILE) as f:
    ENTRYPOINTS = yaml.safe_load(f)


def add_entrypoint(day_number: int, filename: Path) -> None:
    ENTRYPOINTS[day_number] = str(filename.stem)
    with open(ENTRYPOINTS_FILE, "w") as f:
        yaml.dump(ENTRYPOINTS, f)


def gen_day_dir(day_number: int) -> Path:
    return Path(f"day_{day_number:>02}")


@click.command()
@click.argument("filename")
def gen_day(filename):
    day_number = 1
    while gen_day_dir(day_number).is_dir():
        day_number += 1

    filename = Path(filename)
    if not filename.suffix:
        filename = filename.with_suffix(".py")

    add_entrypoint(day_number, filename)

    day_dir = gen_day_dir(day_number)
    day_dir.mkdir(parents=True, exist_ok=True)
    with (gen_day_dir(day_number) / filename).open("w") as f:
        f.write(TEMPLATE)


@click.command()
@click.argument("day_number", type=int)
def run_day(day_number):
    entrypoint = ENTRYPOINTS.get(day_number)
    if not entrypoint:
        raise click.ClickException(f"No entrypoint found for day {day_number}")
    os.system(f'python {gen_day_dir(day_number) / Path(entrypoint).with_suffix(".py")}')

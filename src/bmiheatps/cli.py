"""Command-line interface for bmi-heat-study """

import os
import click

from .config import BmiHeatStudyConfig
from .study import BmiHeatParameterStudy


@click.group(chain=True)
@click.version_option()
@click.option(
    "--cd",
    default=".",
    type=click.Path(exists=True, file_okay=False, dir_okay=True, readable=True),
    help="Change to a directory, then execute.",
)
def main(cd) -> None:
    """Set up and run a parameter study on the BmiHeat model."""
    os.chdir(cd)


@main.command()
@click.argument(
    "config-file",
    type=click.Path(exists=True),
)
@click.pass_context
def setup(ctx, config_file):
    """Generate a set of BmiHeat config files for a parameter study."""
    setup = BmiHeatStudyConfig(config_file)
    setup.setup_study()
    setup.generate_study()


@main.command()
@click.argument(
    "config-file",
    type=click.Path(exists=True),
)
@click.option(
    "--show",
    is_flag=True,
    help="Show the final temperature field.",
)
@click.pass_context
def run(ctx, config_file, show):
    """Run the BmiHeat model for a set of parameters."""
    study = BmiHeatParameterStudy(config_file, show)
    study.run()
    if study._show:
        study.show()
    study.output()

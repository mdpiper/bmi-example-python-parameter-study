"""Command-line interface for bmi-heat-study """

import click

from .study import BmiHeatParameterStudy


@click.command()
@click.argument(
    "config-file",
    type=click.Path(exists=True),
)
@click.option(
    "--show",
    is_flag=True,
    help="Show the final temperature field.",
)
def main(config_file, show):
    """Run a parameter study on the BmiHeat model."""
    study = BmiHeatParameterStudy(config_file, show)
    study.run()
    if study._show:
        study.show()
    study.output()

"""Set up a BmiHeat parameter study from a config file."""

import yaml


def read_config_file(config_file: str) -> dict: 
    with open(config_file, "r") as fp:
        config = yaml.safe_load(fp).get("bmiheat-parameter-study", {})
    return config


class BmiHeatStudyConfig(object):
    pass

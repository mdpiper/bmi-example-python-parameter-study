"""Set up a BmiHeat parameter study from a config file."""

import yaml


def read_config_file(config_file: str) -> dict: 
    with open(config_file, "r") as fp:
        config = yaml.safe_load(fp)
    return config


def write_config_file(config: dict, config_file: str) -> None:
    with open(config_file, "w") as fp:
        yaml.safe_dump(data=config, stream=fp)


class BmiHeatStudyConfig(object):
    pass

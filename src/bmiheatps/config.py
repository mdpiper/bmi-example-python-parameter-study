"""Set up a BmiHeat parameter study from a config file."""

import numpy as np
import pathlib
import yaml

HERE = pathlib.Path(__file__)
ROOT = HERE.parent.parent.parent
HEAT_CONFIG_FILE = ROOT / "tests" / "data" / "heat-config.yaml"


def read_config_file(config_file: str) -> dict: 
    with open(config_file, "r") as fp:
        config = yaml.safe_load(fp)
    return config


def write_config_file(config: dict, config_file: str) -> None:
    with open(config_file, "w") as fp:
        yaml.safe_dump(data=config, stream=fp)


class BmiHeatStudyConfig(object):

    def __init__(self, study_config_file: str) -> None:
        self.heat_config = None
        self.study_config_file = study_config_file
        self.study_config = None
        self.alpha = None

    def setup_study(self) -> None:
        self.heat_config = read_config_file(HEAT_CONFIG_FILE)
        self.study_config = read_config_file(self.study_config_file)
        self.alpha = np.linspace(self.study_config["alpha_start"], self.study_config["alpha_stop"], num=self.study_config["n_steps"], endpoint=True)

    def generate_study(self) -> None:
        for i in range(self.study_config["n_steps"]):
            self.heat_config["alpha"] = float(self.alpha[i])
            write_config_file(self.heat_config, f"heat-config-{i+1}.yaml")

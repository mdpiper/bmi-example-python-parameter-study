"""Test the config module."""

import yaml

from bmiheatps.config import read_config_file

CONFIG_FILE = "study-config.yaml"


def test_read_config_file(shared_datadir):
    config = read_config_file(shared_datadir / CONFIG_FILE)
    assert config["run_duration"] == 2.0
    assert config["max_value"] == 100.0
    assert config["alpha_start"] == 0.5
    assert config["step_size"] == 0.5
    assert config["n_steps"] == 10

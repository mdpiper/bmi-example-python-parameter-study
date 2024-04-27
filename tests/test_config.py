"""Test the config module."""

from bmiheatps.config import read_config_file, write_config_file

STUDY_CONFIG_FILE = "study-config.yaml"
HEAT_CONFIG_FILE = "heat-config.yaml"


def test_read_study_config_file(shared_datadir):
    config = read_config_file(shared_datadir / STUDY_CONFIG_FILE)
    assert config["run_duration"] == 2.0
    assert config["max_value"] == 100.0
    assert config["alpha_start"] == 0.5
    assert config["step_size"] == 0.5
    assert config["n_steps"] == 10


def test_read_heat_config_file(shared_datadir):
    config = read_config_file(shared_datadir / HEAT_CONFIG_FILE)
    assert config["shape"] == [11, 11]
    assert config["spacing"] == [1.0, 1.0]
    assert config["origin"] == [0.0, 0.0]
    assert config["alpha"] == 5.0


def test_write_heat_config_file(tmpdir, shared_datadir):
    config = {"alpha": 1.0}
    with tmpdir.as_cwd():
        write_config_file(config, "new-config.yaml")
        new = read_config_file("new-config.yaml")
    assert new["alpha"] == 1.0

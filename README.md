# bmi-example-python-parameter-study

A parameter study of the *Heat* model
from the Python [Basic Model Interface][bmi] (BMI) [example][example],
run through its BMI.

## Install

To install the *bmiheat-parameter-study* package,
clone this repository,
set up a virtual environment,
and run `pip install`.
```bash
pip install -e .
```

## Setup

Run the `setup` subcommand to generate a set of *BmiHeat* configuration files for the parameter study.
```bash
bmiheat-parameter-study setup study-config.yaml
```

## Run

Use the `run` subcommand to run the *BmiHeat* model through each of the parameter sets defined in the configuration files.
```bash
bmiheat-parameter-study run heat-config-1.yaml
bmiheat-parameter-study run heat-config-2.yaml
bmiheat-parameter-study run heat-config-3.yaml
...
```

Each call to the `run` subcommand writes a statistic to the console.
Collect these statistics to complete the parameter study.

<!-- Links -->

[bmi]: https://bmi.readthedocs.io
[example]: https://github.com/csdms/bmi-example-python

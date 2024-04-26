"""A parameter study of the BmiHeat model."""

import numpy as np
from heat import BmiHeat

CONFIG_FILE = "heat.yaml"


class BmiHeatParameterStudy(object):

    RUN_DURATION = 2.0
    VAR_NAME = "plate_surface__temperature"
    MAX_VALUE = 100.

    def __init__(self, config_file: str) -> None:
        self._bmi = BmiHeat()
        self._bmi.initialize(config_file)

        grid_id = self._bmi.get_var_grid(self.VAR_NAME)
        rank = self._bmi.get_grid_rank(grid_id)
        self._shape = np.ndarray(rank, dtype=int)
        self._bmi.get_grid_shape(grid_id, self._shape)

        self._temperature = np.zeros(self._shape).flatten()
        self.set_initial_values()

    def set_initial_values(self) -> None:
        max_value_index = self._shape[1] // 2 * (self._shape[0] + 1)
        self._temperature[max_value_index] = self.MAX_VALUE
        self._bmi.set_value(self.VAR_NAME, self._temperature)

    def run(self) -> None:
        while self._bmi.get_current_time() < self.RUN_DURATION:
            self._bmi.update()

    def output(self) -> None:
        self._bmi.get_value(self.VAR_NAME, self._temperature)
        print(self._temperature.sum())

    def show(self):
        self._bmi.get_value(self.VAR_NAME, self._temperature)
        with np.printoptions(formatter={"float": "{: 5.1f}".format}):
            print(self._temperature.reshape(self._shape))


def main() -> None:
    m = BmiHeatParameterStudy(CONFIG_FILE)
    m.run()
    m.show()
    m.output()


if __name__ == "__main__":
    main()

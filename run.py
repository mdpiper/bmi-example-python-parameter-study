import numpy as np
from heat import BmiHeat

CONFIG_FILE = "heat.yaml"
END_TIME = 2.0


m = BmiHeat()
m.initialize(CONFIG_FILE)

grid_id = m.get_var_grid("plate_surface__temperature")
rank = m.get_grid_rank(grid_id)
shape = np.ndarray(rank, dtype=int)
m.get_grid_shape(grid_id, shape)

temperature = np.zeros(shape)
temperature[shape[0] // 2, shape[1] // 2] = 100.0
m.set_value("plate_surface__temperature", temperature)

while m.get_current_time() < END_TIME:
    m.update()

final_temperature = np.empty_like(temperature).flatten()
m.get_value("plate_surface__temperature", final_temperature)

with np.printoptions(formatter={"float": "{: 5.1f}".format}):
    print(final_temperature.reshape(shape))

print(final_temperature.sum())

m.finalize()

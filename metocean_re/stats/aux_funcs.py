"""
Helper functions: reading metocean data.

The functions in metocean-re use NORA3 column names, as written by
metocean-api (heights z in m):

    wind_speed_{z}m          wind speed [m/s]
    wind_direction_{z}m      wind direction [deg, from]
    air_temperature_{z}m     air temperature [K]
    relative_humidity_{z}m   relative humidity [0-1]
    density_{z}m             air density [kg/m3]
    tke_{z}m                 turbulent kinetic energy [m2/s2]
    sea_surface_temperature  [K]
    hs, tp                   significant wave height [m], peak period [s]

See examples/download_nora3.py and examples/build_dataset.py for how the
test dataset in tests/data was made.
"""

import pandas as pd


def read_metocean_csv(file):
    """Read a CSV file written by metocean-api (or by examples/build_dataset.py)."""
    df = pd.read_csv(file, comment="#", index_col=0, parse_dates=True)
    df.index.name = "time"
    return df

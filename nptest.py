import numpy as np
import datetime

bars_dtype = [
    # use datetime64 may improve performance/memory usage, but it's hard to talk with other modules, like TimeFrame
    ("frame", "O"),
    ("open", "f4"),
    ("high", "f4"),
    ("low", "f4"),
    ("close", "f4"),
    ("volume", "f8"),
    ("amount", "f8"),
    ("factor", "f4"),
]

bars = np.array(
    [
        (
            datetime.date(2019, 1, 5),
            5.1,
            5.2,
            5.0,
            5.15,
            1000000,
            100000000,
            1.23,
        ),
        (
            datetime.date(2019, 1, 6),
            5.1,
            5.2,
            5.0,
            5.15,
            1000000,
            100000000,
            1.23,
        ),
    ],
    dtype=bars_dtype,
)

print(bars['frame'])
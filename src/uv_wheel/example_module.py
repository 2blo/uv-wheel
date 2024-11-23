import pandas as pd
from deutils import example_function as deutils_example_function


def example_function():
    return deutils_example_function(pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]}))


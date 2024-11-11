from typing import Optional

# Task 1
def str_to_float(string: str)->Optional[float]:
    try:
        return float(string)
    except ValueError:
        return None







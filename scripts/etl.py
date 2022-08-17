def etl(values: dict) -> dict:
    return {v.lower(): k for k in values for v in values[k]}

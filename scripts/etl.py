def etl(values: dict) -> dict:
    scores = {}
    for k in values.keys():
        print(values[k])
        for v in values[k]:
            v = v.lower()
            scores[v] = k
    return scores

def etl(values: dict) -> dict:
    scores = {}
    for k in values.keys():
        print(values[k])
        for v in values[k]:
            scores[v] = k
    return scores


v = {1: ["A"]}
print(etl(v))

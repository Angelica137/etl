from scripts.etl import etl


values = {
    1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
    2: ["D", "G"],
    3: ["B", "C", "M", "P"],
    4: ["F", "H", "V", "W", "Y"],
    5: ["K"],
    8: ["J", "X"],
    10: ["Q", "Z"],
}


def test_return_value_of_a():
    v = {1: ["A"]}
    assert etl(v) == {"A": 1}


def test_returns_new_system_for_U_and_T():
    v = {1: ["A", "U",  "T"]}
    assert etl(v) == {"A": 1, "U": 1, "T": 1}

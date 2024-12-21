#p5 McCulloch-Pitts

def mcculloch_pitts(inputs, weights, threshold):
    assert len(inputs) == len(weights)
    weighted_sum = sum(x * w for x, w in zip(inputs, weights))
    output = 1 if weighted_sum >= threshold else 0
    return output

def test_logic_gate(logic_gate):
    print(f"Testing {logic_gate} gate:")
    if logic_gate == "AND":
        inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
        weights = (1, 1)
        threshold = 2
    elif logic_gate == "OR":
        inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
        weights = (1, 1)
        threshold = 1
    elif logic_gate == "XOR":
        inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
        weights_and = (1, 1)
        weights_or = (1, 1)
        weights_not = (-1,)
        threshold = 1
        for input_pair in inputs:
            input1, input2 = input_pair
            and_result = mcculloch_pitts(input_pair, weights_and, threshold)
            or_result = mcculloch_pitts(input_pair, weights_or, threshold)
            not_result = mcculloch_pitts((and_result,), weights_not, threshold)
            xor_result = mcculloch_pitts((or_result, not_result), weights_and, threshold)
            print(f"{input_pair}: {xor_result}")
        return
    elif logic_gate == "AND NOT":
        inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
        weights = (1, -1)
        threshold = 0
    else:
        print("Invalid logic gate.")
        return
    for input_pair in inputs:
        result = mcculloch_pitts(input_pair, weights, threshold)
        print(f"{input_pair}: {result}")

test_logic_gate("AND")
test_logic_gate("OR")
test_logic_gate("XOR")
test_logic_gate("AND NOT")
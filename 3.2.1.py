def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, \
        f"expected {expected_result}, got {actual_result}"

expected_result = input()
actual_result = input()

test_input_text(expected_result, actual_result)
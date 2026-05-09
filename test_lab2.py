import ex6 as mcd

def test_min_max():
    result = []
    input_arr = [670, 100, 476]
    result = mcd.find_min_max(input_arr)
    expected_result = [100, 670]
    assert (result == expected_result)

def test_ave():
    result = []
    input_arr = [2, 4, 6, 4]
    result = mcd.calc_average(input_arr)
    expected_result = 4.00

    assert (result == expected_result)

def test_median_temp():
    result = []
    input_arr = [25, 30, 20, 35, 40]
    result = mcd.calc_median_temp(input_arr)
    expected_result = 20

    assert (result == expected_result)
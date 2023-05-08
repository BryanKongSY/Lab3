import Lab3

print("Test_Lab3")

def test_bubble_sort_greater_than_10():
    test_arr = [11, 12, 22, 25, 34, 64, 98, 87, 81, 10, 11]
    result = Lab3.bubble_sort(test_arr, Lab3.SORT_ASCENDING)

    assert (result == 1)
def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    test_arr = [64, 34, 25, 12, 22.0, 11, 90]
    result = Lab3.bubble_sort(test_arr, 3)

    assert (result == 2)

def test_bubble_sort_0_numbers():
    test_arr = []
    result = Lab3.bubble_sort(test_arr, Lab3.SORT_ASCENDING)

    assert (result == 0)
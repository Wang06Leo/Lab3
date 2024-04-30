import Lab3

print("Test_Lab3")


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




#REQ-01
def test_bubble_sort_ascending_REQ_01():
    result = []
    input_arr = [1,3,4,2,7,6,8,9,5]
    test_arr = [1,2,3,4,5,6,7,8,9]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

#REQ-02
def test_bubble_sort_descending_REQ_02():
    result = []
    input_arr = [1,5,8,9,7,2,4,3]
    test_arr = [9,8,7,5,4,3,2,1]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

#REQ-03

def test_bubble_sort_return_value_REQ_03():
    input_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    
    
    assert result == 1

#REQ-04
import Lab3
def test_bubble_sort_empty_array():
    # Input array with 0 numbers
    input_arr = []
    
    # Call the bubble_sort() function
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    
    # Assert that the result is equal to 0
    assert result == 0
#REQ-05
def test_bubble_sort_invalid_input():
    # Invalid input array with non-integer values
    input_arr = [64, 'abc', 25, 12, 22, 11, 90]

    # Call the bubble_sort() function
    result = Lab3.bubble_sort(input_arr, 3)

    # Assert that the result is equal to 2
    assert result == 2



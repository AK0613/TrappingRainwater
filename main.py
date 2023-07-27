# Trapping rain water
# Empty or under 2 elements

# optimal solution

# Optimal solution to find how much water can be gathered by the given array
def get_result(input):
    # Initialize values
    water = max_left = max_right = 0
    # Left and right pointers that start on opposite ends of the array
    left = 0
    right = len(input) - 1
    # While we can move inward
    while (left < right):
        # If the left wall is smaller
        if input[left] <= input[right]:
            # If the current value for max_left is smaller than the value at index left, then replace max_left
            if input[left] > max_left:
                max_left = input[left]
            # The result calculates the current water height for the left side based on the wall to the left
            # minus the current value at index [left]
            res = max_left - input[left]
            # Move pointer towards the right
            left += 1
        # if the right wall is smaller
        else:
            # If the current value for max_right is smaller than the value at index right, then replace max_right
            if input[right] > max_right:
                max_right = input[right]
            # The result calculates the current water height for the right side based on the wall to the right
            # minus the current value at index [right]
            res = max_right - input[right]
            right -= 1
        # If the result of both calculations is a number > 0 then add it to the accumulated water
        if res > 0:
            water += res
    return water


input = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]
print(get_result(input))

# def get_result(input):
#     size = len(input)
#     water = 0
#     if size > 3:
#         for a in range(size):
#             max_left = max_right = 0
#             if a == 0:
#                 max_left = 0
#                 max_right = max(input[a + 1::])
#
#             elif a == size - 1:
#                 max_right = 0
#                 max_left = max(input[a - 1:0:-1])
#
#             elif a == 1:
#                 max_left = input[0]
#                 max_right = max(input[a + 1::])
#
#             else:
#                 max_left = max(input[a - 1:0:-1])
#                 max_right = max(input[a + 1::])
#
#             result = min(max_right, max_left) - input[a]
#             print(f'result: {result}')
#             if result > 0:
#                 water += result
#                 print(f'water: {water}')
#
#     return water

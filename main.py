# Trapping rain water
# Empty or under 2 elements

# optimal solution

def get_result(input):
    water = max_left = max_right = 0
    left = 0
    right = len(input) - 1

    while (left < right):
        if input[left] <= input[right]:
            if input[left] > max_left:
                max_left = input[left]
            res = max_left - input[left]
            left += 1
        else:
            if input[right] > max_right:
                max_right = input[right]
            res = max_right - input[right]
            right -= 1

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

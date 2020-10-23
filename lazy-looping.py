# numbers = [1,2,3,5,7]
# for number in numbers:
#     print(number)

# double_numbers = []
# for n in numbers:
#     double_numbers.append(n * 2)

# doubled_numbers = [
#     n * 2
#     for n in numbers
#     if n % 2 != 1
# ]


def get_vowel_names(list_of_names):
    vowel_list = ["A", "E", "I", "O", "U"]
    names_starting_with_vowel = []

    for name in list_of_names:
        # Need to check if each name contains A, E, I, O, U
        for vowel in vowel_list:
            if name[1].contains(vowel) or name[1].contains(vowel.islower):
                names_starting_with_vowel.append(name)

    return names_starting_with_vowel

def sum_all(matrix):
    matrix_sum = 0
    # My way...
    # for lists in matrix:
    #     for value in lists:
    #         matrix_sum = matrix_sum + value

    # Can make it into a list comprehension but less memory efficient
    # () around your list makes it a generator
    return sum(
        n
        for row in matrix
        for n in row
    )

    #return matrix_sum


def unique(iterable):
    for item in iterable:
        yield item


def float_range(start, stop, step = 1):
    curr_step = start
    while curr_step != stop:
        yield curr_step
        curr_step = curr_step + step


if __name__ == "__main__":
    # names = ["Scott", "arthur", "Jan", "Elizabeth"]
    # get_vowel_names(names)

    # matrix = [[1, 2, 3], [4, 5, 6]] # Should sum to 21
    # print(sum_all(matrix))

    # unique_list = list(unique([6, 7, 0, 9, 0, 1, 2, 7, 7, 9]))
    # print(unique_list)
    test_gen = float_range(0, 4)
    test_list = list(test_gen)
    print(test_list)
    print(list(float_range(0, 10)))
    print(list(float_range(2.5, 5, 0.5)))
    print(list(float_range(2.5, 5, step=0.5)))
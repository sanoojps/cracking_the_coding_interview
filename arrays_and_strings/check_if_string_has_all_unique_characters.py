# Implement an algorithm to determine if a string has all unique characters.
#  What if you can not use additional data structures?

# LOGIC
# ******
# enumerate through character in the outer loop
# enumerate in the inner loop
# compare each character for duplicates
# skip the character at the current index of outer loop in the inner loop
# ORDER O(n2)
def check_if_string_has_unique_characters(string):
    is_unique = False
    for outer_index,outer_char in enumerate(string):
        for inner_index,inner_char in enumerate(string):
            if inner_index is not outer_index:
                if outer_char is inner_char:
                    return is_unique
            
    is_unique = True
    return is_unique

print(
    "{} {}".format(
        "b,6",
        check_if_string_has_unique_characters(
            "b,6"
            )
    )
)

print(
    "{} {}".format(
        "b,b",
        check_if_string_has_unique_characters(
            "b,b"
            )
    )
)

print(
    "{} {}".format(
        "abcd",
        check_if_string_has_unique_characters(
            "abcd"
            )
    )
)

print(
    "{} {}".format(
        "bbcd",
        check_if_string_has_unique_characters(
            "bbcd"
            )
    )
)


# ORDER O(n log n)
# LOGIC
# ******
# sort the string
# and check if any of the adjacent values repeat
def check_if_string_has_unique_characters_O_n(string):
    sorted_string = "".join(sorted(string))
    is_unique = False

    for index in range(0,len(sorted_string) - 1):
        lhs = sorted_string[index]
        rhs = sorted_string[index + 1]
        if lhs is rhs:
            return is_unique

    is_unique = True
    return is_unique

print(
    "{} {}".format(
        "b,6",
        check_if_string_has_unique_characters_O_n(
            "b,6"
            )
    )
)

print(
    "{} {}".format(
        "b,b",
        check_if_string_has_unique_characters_O_n(
            "b,b"
            )
    )
)

print(
    "{} {}".format(
        "abcd",
        check_if_string_has_unique_characters_O_n(
            "abcd"
            )
    )
)

print(
    "{} {}".format(
        "bbcd",
        check_if_string_has_unique_characters_O_n(
            "bbcd"
            )
    )
)

# UNITTEST
import unittest
class TestingUniqueCharactersOn(unittest.TestCase):

    def test_string_pattern_not_unique(self):
        string_pattern = "bbcd"
        self.assertFalse(
            expr=check_if_string_has_unique_characters_O_n(string_pattern),
            msg="string {} is unique".format(string_pattern)   
        )
        string_pattern = "bbbb"
        self.assertFalse(
            expr=check_if_string_has_unique_characters_O_n(string_pattern),
            msg="string {} is unique".format(string_pattern)   
        )
        string_pattern = "bb"
        self.assertFalse(
            expr=check_if_string_has_unique_characters_O_n(string_pattern),
            msg="string {} is unique".format(string_pattern)   
        )
        string_pattern = "b00_"
        self.assertFalse(
            expr=check_if_string_has_unique_characters_O_n(string_pattern),
            msg="string {} is unique".format(string_pattern)   
        )

    def test_string_pattern_is_unique(self):
        string_pattern = "abcd"
        self.assertTrue(
            expr=check_if_string_has_unique_characters_O_n(string_pattern),
            msg="string {} is not unique".format(string_pattern)   
        )
        string_pattern = "a"
        self.assertTrue(
            expr=check_if_string_has_unique_characters_O_n(string_pattern),
            msg="string {} is not unique".format(string_pattern)   
        )
        string_pattern = "ab"
        self.assertTrue(
            expr=check_if_string_has_unique_characters_O_n(string_pattern),
            msg="string {} is not unique".format(string_pattern)   
        )

unittest.main()
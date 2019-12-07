# Design an algorithm and write code to remove the duplicate characters 
# in a string without using any additional buffer. 
# NOTE: One or two additional variables are fine. An extra copy of the array is not.
# FOLLOW UP
# Write the test cases for this method.

def remove_duplicate_characters(word):
    char_list = list(word)
    current_duplicate_char = None    
    for o_index,o_char in enumerate(char_list):
        found_char = None 
        for i_index,i_char in enumerate(char_list):
            if o_char == i_char:
                if found_char == None:
                    found_char = o_char
                else:
                    char_list.pop(i_index)

    print(char_list)


remove_duplicate_characters("ssssstring")

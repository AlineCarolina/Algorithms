def anagram(str):
    anagram_dict = {}
    for char in str.lower():
        if char in anagram_dict:
            anagram_dict[char] += 1
        else:
            anagram_dict[char] = 1
    return anagram_dict


def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    if anagram(first_string) != anagram(second_string):
        return False
    return True

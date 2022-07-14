def is_palindrome_iterative(word):
    # https://stackoverflow.com/questions/509211/understanding-slicing
    return True if len(word) > 0 and word == word[::-1] else False

string = 'abacdef,'
def has_unique_chars(string):
    log = dict()
    for char in string:
        log[char] = log.get(char,0) + 1
        if log[char] > 1:
            return False
    return True

has_unique_chars(string)
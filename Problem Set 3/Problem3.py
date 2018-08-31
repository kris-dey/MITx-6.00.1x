def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string

    all = string.ascii_lowercase
    s = ''

    for char in all:
        if char not in lettersGuessed:
            s = s + char
    return s
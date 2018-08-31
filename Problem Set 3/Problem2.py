def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    g = ''
    for char in secretWord:
        if char not in lettersGuessed:
            g = g + ' _ '
        else: 
            g = g + char
    return g
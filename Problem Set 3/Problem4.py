def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is "+ str(len(secretWord)) + " letters long.")
    print("-----------")
    
    mistakesMade = 0
    Win = False
    availableLetters = ''
    lettersGuessed = []
    
    while True:
        if mistakesMade == 8:
            Win = False
            break
        elif isWordGuessed(secretWord, lettersGuessed):
            Win = True
            break
        
        availableLetters = getAvailableLetters(lettersGuessed)
        print("You have " + str(8-mistakesMade) + " guesses left.")
        print("Available letters: " + availableLetters)
        inputLetter = str(input("Please guess a letter: "))

        if inputLetter in availableLetters:
            lettersGuessed.append(inputLetter)
            if inputLetter in secretWord:
                guessedWord = getGuessedWord(secretWord,lettersGuessed)
                print("Good guess: " +  guessedWord)
            else:
                mistakesMade+=1
                guessedWord = getGuessedWord(secretWord,lettersGuessed)
                print("Oops! That letter is not in my word: " + guessedWord)    
        else:
            print("Oops! You've already guessed that letter: " + guessedWord)
        
        print("-----------")
        
    if Win:
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was " + secretWord + ". ")

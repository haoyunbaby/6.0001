# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    times=0
    for char in secret_word:
        for c in letters_guessed:
            if char==c:
                times+=1
                break
    if times==len(secret_word):
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    s=""
    for char in secret_word:
        t=0
        for c in letters_guessed:
            if char==c:
                t+=1
                break
        if t==1:
            s+=char
        else:
            s+="_ "
    return s
                
    


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    s=""
    for char in string.ascii_lowercase:
        t=0
        for c in letters_guessed:
            if char==c:
                t+=1
                break
        if t!=1:
            s+=char
    return s
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses_remaining=6
    warnings_remaining=3
    score=1
    letters_guessed=""
    secret_word=input("Set secret the word manually:")
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is",len(secret_word),"letters long.")
    print("You have",warnings_remaining,"warnings left.")
    while (not is_word_guessed(secret_word, letters_guessed)) and guesses_remaining>0:
        print("-------------")
        print("You have",guesses_remaining,"guesses left.")
        print("Available letters:",get_available_letters(letters_guessed))
        t=input("Please guess a letter:")  
        #qwer = input("Test for input, can the 2 line w/o newline")
        if str.isalpha(t):
            t=str.lower(t)
            guessed=0
            for i in letters_guessed:
                if i==t:
                    guessed+=1
                    break
            if guessed==1:
                if warnings_remaining>0:
                    warnings_remaining-=1
                    print("Oops! You've already guessed that letter. You have",warnings_remaining,"warnings left:")
                    print(get_guessed_word(secret_word, letters_guessed))
                else:
                    # if guesses_remaining>1:
                        guesses_remaining-=1
                        print("Oops! You've already guessed that letter. You have no warnings left")
                        print("so you lose one guess:",get_guessed_word(secret_word, letters_guessed))  
                    # else:
                    #     print("Sorry, you ran out of guessed. The word was else.")       
            else:
                letters_guessed+=t
                ans=0
                for char in secret_word:
                    if char==t:
                        ans+=1
                        break
                if ans==1:
                    print("Good guess:",get_guessed_word(secret_word, letters_guessed))
                elif t=="a" or t=="e" or t=="i" or t=="o":
                    # if guesses_remaining>2:
                        guesses_remaining-=2
                        print("Oops! That letter is not in my word:",get_guessed_word(secret_word, letters_guessed))
                        #print("Please guess a letter:",get_guessed_word(secret_word, letters_guessed))
                        
                    # else:
                    #     print("Sorry, you ran out of guessed. The word was else.")
                else:
                    # if guesses_remaining>1:
                        guesses_remaining-=1
                        print("Oops! That letter is not in my word:",get_guessed_word(secret_word, letters_guessed))
                        
                    # else:
                    #     print("Sorry, you ran out of guessed. The word was else.")

                    
                    
        else:
           if warnings_remaining>0:
               warnings_remaining-=1
               print("Oops! That is not a valid letter. You have",warnings_remaining,"warnings left:",get_guessed_word(secret_word, letters_guessed))
               #print(get_guessed_word(secret_word, letters_guessed))
           else:
               # if guesses_remaining>0:
                   guesses_remaining-=1
                   print("Oops! That is not a valid letter. You have no warnings left")
                   print("so you lose one guess:",get_guessed_word(secret_word, letters_guessed))
                   
               # else:
               #     print("Sorry, you ran out of guessed. The word was else.")
    print("-------------")
    if guesses_remaining<=0:
        print("Sorry, you ran out of guesses. The word was else.") 
    else:
        unique_char=0
        for i in range(len(secret_word)):
            same=0
            for j in range(i+1,len(secret_word)):
                if secret_word[i]==secret_word[j]:
                    same+=1
                    break
            if same==0:
                unique_char+=1
                #print("Unique letter is",secret_word[i])
        score=guesses_remaining*unique_char
        print("Congratulations, you won!")
        print("Your total score for this game is:",score)
        
            
          
                 
            
        

                
        
        



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    t=""
    for char in my_word:
        if char!=" ":
            t+=char
    #print(t)
    if len(t)==len(other_word):
        for i in range(len(t)):
            if t[i]!="_":
                if t[i]!=other_word[i]:
   #                 print(i)
                    return False
        return True
    else:
        #print("different length my_word is",len(t),"other_word is",len(other_word))
        return False



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    match=0
    for i in range(len(wordlist)):
        if match_with_gaps(my_word, wordlist[i]):
            print(wordlist[i],end=" ")
            match+=1
    if match==0:
        print("No matches found")
        
        
        
def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses_remaining=6
    warnings_remaining=3
    score=1
    letters_guessed=""
    #secret_word=input("Set secret the word manually:")
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is",len(secret_word),"letters long.")
    print("You have",warnings_remaining,"warnings left.")
    while (not is_word_guessed(secret_word, letters_guessed)) and guesses_remaining>0:
        print("-------------")
        print("You have",guesses_remaining,"guesses left.")
        print("Available letters:",get_available_letters(letters_guessed),end="")
        t=input("Please guess a letter:")  
        #qwer = input("Test for input, can the 2 line w/o newline")
        if str.isalpha(t):
            t=str.lower(t)
            guessed=0
            for i in letters_guessed:
                if i==t:
                    guessed+=1
                    break
            if guessed==1:
                if warnings_remaining>0:
                    warnings_remaining-=1
                    print("Oops! You've already guessed that letter. You have",warnings_remaining,"warnings left:")
                    print(get_guessed_word(secret_word, letters_guessed))
                else:
                    # if guesses_remaining>1:
                        guesses_remaining-=1
                        print("Oops! You've already guessed that letter. You have no warnings left")
                        print("so you lose one guess:",get_guessed_word(secret_word, letters_guessed))  
                    # else:
                    #     print("Sorry, you ran out of guessed. The word was else.")       
            else:
                letters_guessed+=t
                ans=0
                for char in secret_word:
                    if char==t:
                        ans+=1
                        break
                if ans==1:
                    print("Good guess:",get_guessed_word(secret_word, letters_guessed))
                elif t=="a" or t=="e" or t=="i" or t=="o":
                    # if guesses_remaining>2:
                        guesses_remaining-=2
                        print("Oops! That letter is not in my word:",get_guessed_word(secret_word, letters_guessed))
                        #print("Please guess a letter:",get_guessed_word(secret_word, letters_guessed))
                        
                    # else:
                    #     print("Sorry, you ran out of guessed. The word was else.")
                else:
                    # if guesses_remaining>1:
                        guesses_remaining-=1
                        print("Oops! That letter is not in my word:",get_guessed_word(secret_word, letters_guessed))
                        
                    # else:
                    #     print("Sorry, you ran out of guessed. The word was else.")

                    
                    
        else:
           if t=="*":
               # print(match_with_gaps("a_ ple", "apple"))
               my_word=get_guessed_word(secret_word, letters_guessed)
               print("Possible word matches are:")
               show_possible_matches(my_word)
               print("")
           else: 
               if warnings_remaining>0:
                   warnings_remaining-=1
                   print("Oops! That is not a valid letter. You have",warnings_remaining,"warnings left:",get_guessed_word(secret_word, letters_guessed))
               #print(get_guessed_word(secret_word, letters_guessed))
               else:
               # if guesses_remaining>0:
                   guesses_remaining-=1
                   print("Oops! That is not a valid letter. You have no warnings left")
                   print("so you lose one guess:",get_guessed_word(secret_word, letters_guessed))
                   
               # else:
               #     print("Sorry, you ran out of guessed. The word was else.")
    print("-------------")
    if guesses_remaining<=0:
        print("Sorry, you ran out of guesses. The word was.",secret_word) 
    else:
        unique_char=0
        for i in range(len(secret_word)):
            same=0
            for j in range(i+1,len(secret_word)):
                if secret_word[i]==secret_word[j]:
                    same+=1
                    break
            if same==0:
                unique_char+=1
                #print("Unique letter is",secret_word[i])
        score=guesses_remaining*unique_char
        print("Congratulations, you won!")
        print("Your total score for this game is:",score)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)

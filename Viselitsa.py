import random
correctLetters = ""
wrongLetters = ""
Frames = []
words = """соска фифер хых пельмешка повар ардуино кубик робофест яблоко апельсин пятерочка сено пивко водичка баня
сауна еветри коллектив корпоратив зависимость цгб фсб пту дгту физмат вконтакте одноклассники аська твиттер""".split()
Frames.append(
"""

        
      
   
          
_ _ _  
       """)
Frames.append(
    """

      |
      |
      |
      |     
_ _ _ |
       """)
Frames.append(
    """
_ _ _ _
      |
      |
      |
      |     
_ _ _ |
       """)
Frames.append(
    """
_ _ _ _
  |   |
      |
      |
      |     
_ _ _ |  
       """)
Frames.append(
    """
_ _ _ _
  |   |
  O   |
      |
      |     
_ _ _ | 
       """)
Frames.append(
    """
_ _ _ _
  |   |
  O   |
  |   |
      |     
_ _ _ |
       """)
Frames.append(
    """
_ _ _ _
  |   |
  O   |
 /|   |
      |     
_ _ _ |
       """)
Frames.append(
    """
_ _ _ _
  |   |
  O   |
 /|\  |
      |     
_ _ _ |
       """)
Frames.append(
    """
_ _ _ _
  |   |
  O   |
 /|\  |
 /    |     
_ _ _ |
       """)

Frames.append(
    """
_ _ _ _
  |   |
  O   |
 /|\  |
 / \  |     
_ _ _ |
       """)
def GetRandomWord(WordList):
    i = random.randint(0, len(WordList) -1)
    return WordList[i]
    
def PlayAgain():
    print("Do you want play again? y or n")
    return input().lower().startswith("y")


def GetLetter():
    while True:
        Letter = input("Please input one word => ")
        Letter = Letter.lower()
        if len(Letter) != 1:
            print("Sir, you stupid. Ye. This true. Input one word")
        elif Letter not in "йцукенгшщзхъфывапролджэячсмитьбюё":
            print("Change language or print word!")
        elif Letter == "":
            print("I say word!")
        else:
            return Letter

def drawField(word, correctLetters, wrongLetters):
    print(Frames[len(wrongLetters)])
    print(wrongLetters)
    print(correctLetters)
    blanks = "_" * len(word)
    for i in range(len(word)):
        if word[i] in correctLetters:
            blanks = blanks[:i] + word[i] + blanks[i + 1:]
    for letter in blanks:
        print(letter, end = " ")
        
print("___WELCOME TO VISELITSA___")
secretWord = GetRandomWord(words)
wrongLetters = ' '
correctLetters = ' '
gameIsDone = False

while True:
    drawField(secretWord, correctLetters, wrongLetters)
    guess  = GetLetter()
    if guess in secretWord:
        correctLetters = correctLetters + guess
        FoundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                FoundAllLetters = False
        if FoundAllLetters:
            gameIsDone = True
            print("YOU WIN!")
    else:
        wrongLetters = wrongLetters + guess
        if len(wrongLetters) == len(Frames) - 1:
            drawField(wrongLetters, correctLetters, secretWord)
            print("Try's is end!\n After " + str(len(wrongLetters)) + " wrong try's and " + str(len(correctLetters)) + " correct, but correct equal " + secretWord + "")
            gameIsDone = True
    if gameIsDone:
        if PlayAgain():
            secretWord = GetRandomWord(words)
            wrongLetters = ' '
            correctLetters = ' '
            gameIsDone = False
        else:
            break
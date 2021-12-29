def getCorrectResponse(answer):
    if (answer != "A") and (answer != "B") and (answer != "C"):
        return 1
    else:
        return 0
    
def main():
    question = ["1. The Statue of Liberty was a gift from where?", "2. Who paid for Christopher Columbus’ explorations?", "3. What is the largest country by size?", "4. Who is the creator of the classic book characters Tom Sawyer and Huckleberry Finn?", "5. The Earth is at least how many billion years old?"]
    choiceA = ["A) Germany", "A) The Spanish Royals", "A) China", "A) Henry James", "A) 200 billion years"]
    choiceB = ["B) Canada", "B) Queen Elizabeth", "B) Russia", "B) Charles Dickens", "B) 4 billion years"]
    choiceC = ["C) France", "C) William Shakespeare", "C) Australia", "C) Mark Twain", "C) 10 years"]
    correctAnswer = ["C", "A", "B", "C", "B"]

    start = str(input("Please enter \"yes or y\" to start my quiz or enter any other key to exit: "))
    start = start.lower()
    if (start == "yes") or (start == "y"):
               i = 0
               x = 0
               while i < len(question):
                   print(question[i])
                   print(choiceA[i])
                   print(choiceB[i])
                   print(choiceC[i])
                   answer = str(input("Please enter the correct letter: "))
                   answer = answer.upper()
                   if answer == correctAnswer[i]:
                      print("Correct!")
                      print("")
                      i += 1
                      x += 1
                   elif getCorrectResponse(answer) == 1:
                      print("INVALID RESPONSE. PLEASE TRY AGAIN.")
                      print("")
                      i = i
                   else:
                      print("Wrong! The correct answer is " + correctAnswer[i])
                      print("")
                      i += 1
    else:
        print("Have a great day!")

    if (start == "yes") or (start == "y"):
        print("Congratulations! You got " + str(x) + " out of " + str(i) + " correct. Thank you for playing!")

main()      
           
           


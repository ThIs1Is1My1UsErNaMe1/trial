#algorithm here:
"""
algorithm SM-2 is
    input:  user grade q
            repetition number n
            easiness factor EF
            interval I
    output: updated values of n, EF, and I

    if q ≥ 3 (correct response) then
        if n = 0 then
            I ← 1
        else if n = 1 then
            I ← 6
        else
            I ← round(I × EF)
        end if
        increment n
    else (incorrect response)
        n ← 0
        I ← 1
    end if
    
    EF ← EF + (0.1 − (5 − q) × (0.08 + (5 − q) × 0.02))
    if EF < 1.3 then
        EF ← 1.3
    end if
    
    return (n, EF, I)
"""
"""
question_bank = {
            '1+1': '2',
            '2+2': '4',
            '3+3': '6',
            '4+4': '8',
            '5+5': '10',
            '6+6': '12',
            '7+7': '14',
            '8+8': '16',
            '9+9': '18',
            '10+10': '20'
        }
"""


import math
question_bank = {}


class Flashcards:

    def __init__(self, flashcard_top, flashcard_bottom, q):
        self.flashcard_top = flashcard_top
        self.flashcard_bottom = flashcard_bottom
        self.q = 0
        self.n = 1
        self.EF = 2.5
        self.i = 1

    def interval():
      if q >= 3:  # correct ans
        if n == 0:
          I = 1
        elif n == 1:
          I = 6
        else:
          I = math.ceil(I * self.EF)

      else:  # incorrect ans
        n = 0
        I = 1

      return n, I
              
    def easiness_factor():
      EF = EF + (0.1 - (5 - q) * (0.08 + (5 - q) * 0.02))
      if EF < 1.3:
        EF = 1.3
            # end of if statement
      return EF

mode = input(
    "select a mode. if you want to practice, type 'practice'. If you want to add questions, type 'add' "
)
# q = int(input())
if mode.lower() == "practice":
    def practice():

        def algorithm(q, n, EF, I):

            if q >= 3:  # correct ans
                if n == 0:
                    I = 1
                elif n == 1:
                    I = 6
                else:
                    I = math.ceil(I * EF)
                n += 1

            else:  # incorrect ans
                n = 0
                I = 1

            #end of if statement
            EF = EF + (0.1 - (5 - q) * (0.08 + (5 - q) * 0.02))
            if EF < 1.3:
                EF = 1.3
            # end of if statement
            return n, EF, I

        for i in range(len(question_bank)):
            question_list = list(question_bank.keys())
            question = question_list[i]
            answer = question_bank[question]

            user_answer = str(input(f"{question} = "))
            print(f"the correct answer was {answer}.")
            q = int(input("please select a user grade between 1 and 5 based on your answer. "))
            if q > 5 or q < 1:
                print("not a valid user grade")
            print(algorithm(q, n, EF, I))
    practice()

flashcard_bank = []


if mode.lower() == "add":
    print("when you want to stop adding questions, type 'stop'")
    #question_bank = {}
    user_question = input("add question here: ")
    while user_question.lower() != "stop":
        user_answer = input("add answer here: ")
        new_flashcard = Flashcards(user_question,user_answer)
        flashcard_bank.append(new_flashcard)
        user_question = input("add question here: ")
    practice()

else:
    print("not a valid mode type")

# things to do:
# figure out how to increment n for each individual card (shouldnt be an input)
# also we need to decide on an inital EF value - I don't think it should be 0 since if the user put the question in, then they surely know a bit about it?
# error correction
# need a way to stop getting questions

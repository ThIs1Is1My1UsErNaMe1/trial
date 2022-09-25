import math
import json
import datetime

#q = user grade, n = repetition number, EF = easiness factor, I =interval

json_file = open('questions.json', 'r')
json_data = json_file.read()
obj = json.loads(json_data)


def practice():
    last_practiced = datetime.date.today()
    def algorithm(n, q, EF, I):
      if q >= 3:
          if n == 0:
              I = 1
          elif n == 1:
              I = 6
          else:
              I = math.ceil(I * EF)
          n += 1
      else:
          n = 0
          I = 1

      EF = EF + (0.1 - (5 - q) * (0.08 + (5 - q) * 0.02))
      if EF < 1.3:
          EF = 1.3

      obj[i]["q"] = q
      obj[i]["n"] = n
      obj[i]["I"] = I
      obj[i]["EF"] = EF
      obj[i]["last_practiced"] = last_practiced

      with open('questions.json', 'w') as json_file2:
          json.dump(obj, json_file2, indent=4)

      return I, EF, n
    
    #list of cards to practice today
    practice_list = {}
    #creating daytime algorithm (commented)
    '''def daytime_algorithm():
      day_today = daytime.date.today()
      for obj in jason_file():
        loaded = json_file.loads(obj)
        interval = int(loaded[2])
        lp = int(loaded[4])
        year = []
        month = []
        day = []
        for i in range(0,9):
          if i<=3:
            year.append(lp[i])
          if i==5 or i==6:
            month.append(lp[i])
          if i==8 or i==9:
            day.append(lp[i])
        n.year = int("".join(year))
        n.month = int("".join(month))
        n.day = int("".join(day))
        date = datetime.date(n.year,n.month,n.day)
        if date + datetime.timedelta(days=interval) == day_today:
          practice_list.append(obj["top"],obj["bottom"])'''
        
    # end of algorithm. this is where practice() starts:

    if len(obj) == 0:  # check if there are 0 flashcards
        print("no flashcards saved")
    else:  # printing each question and answer
        for i in range(0, len(obj)):
            array = obj[i]
            user_input = input(f"{array['top']} ")
            if user_input.lower() == "stop":
                break
            else:
                print(f"the answer is {array['bottom']}")
                grade = int(input("input a grade between 1 and 5: "))
                obj[i]['q'] = grade
                print(
                    algorithm(obj[i]['n'], obj[i]['q'], obj[i]['EF'],
                              obj[i]['I']))


def add():
    while True:
      q = input("input question here: ")
      if q.lower() == 'stop':
          break
      else:
          a = input("input answer here: ")
          obj.append({'top': q, 'bottom': a, 'n': 0})
          # adding new question to 'questions.json' file:
          with open('questions.json', 'w') as json_file:
              json.dump(obj, json_file, indent=4, separators=(',', ': '))


def edit(card_num):
    edit_val = input("do you want to edit question or answer or both? ")
    for i in range(0, len(obj)):
        if i + 1 == card_num:
            if edit_val.lower() == "question":
                new_question = input("type new question here: ")
                obj[i]["top"] = new_question
            elif edit_val.lower() == "answer":
                new_ans = input("type new answer here: ")
                obj[i]["bottom"] = new_ans
            elif edit_val.lower() == "both":
                new_question = input("type new question here: ")
                obj[i]["top"] = new_question
                new_ans = input("type new answer here: ")
                obj[i]["bottom"] = new_ans
            else:
                print("not a valid edit value")
        else:
            continue
    with open('questions.json', 'w') as json_file3:
        json.dump(obj, json_file3, indent=4)


#add the while true loop to get valid inputs

# i commented this out cuz im not sure how it will work with the new method, but i think it should work with this as well. right now, the practice function is called above and every flashcard is called once

while True:
    mode = input("Practice or Add or Edit (when you want to stop, type stop):")
    if mode.lower() == "practice":
        practice()
    elif mode.lower() == "add":
        add()
    elif mode.lower() == "edit":
        card_num = int(input("which card do you want to edit (type an integer. e.g. '1' if you want to edit the first card"))
        edit(card_num)
    elif mode.lower() == "stop":
        break
    else:
        print("not a valid mode")


# note: the 'while True loop' is clever, but the only thing is that it repeats questions a lot (since the loop keeps restarting) so we have to take practice mode out of the loop so that questions don't repeat. also the typing stop thing doesn't really work...we need a better way to stop practice/adding of questions.

# 1. calculate interval
# 2. calculate EF
# 3. increment n

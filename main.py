# OK SO HABIT APP
# CRITERIA FOR ME:
    # make a class such that you can make tasks with the class, and set them to different things
    # a displaying function that displays the classes, probably store in a list? Can snatch from data management
    # uhhhhhhhhhhhhh
    # when you make a task:
        # Name of task
        # Type of task (repeatable daily, habits to gain or lose, to do)
        # should you be able to change this stuff???????????
    #*maybe* ***maybe*** make a challenge/battle event
    #need to work on the scoring system,

# inishi

import json

task_list = []




# MAINN
def main():
    
    loadsaved()
    
    menuloop = True

    # menu loop
    while menuloop:

        print("\n-Habit Tracker-")
        print(f"(tthissl be thee stats/health)")
        print("1: NEW TASK")
        print("2: TASKS")
        print("3: EDIT TASKS")
        print("4: MANAGE REWARDS")
        print("5: Tutorial")
        print("0: SAVE AND EXIT")
        # INPUT
        selection = input("> ")

        # ACTION
        # Tasks
        if selection == "1":
            create_new_task()

        # display and edit lissts
        elif selection == "2":
            display_all(task_list)
            # here you can add/remove tasks or change their details, difficulty, etc
            ynreply = input("did you do something? Y/N\n> ")
            if ynreply.lower() == "y":
                donetask()
            elif ynreply.lower() == "n":
                pass
            else:
                print("bad input")

        # 
        elif selection == "3":
            display_all

        elif selection == "4":
            pass
            # create rewards and spend on them

        # 
        elif selection == "5":
            print("Welcome to [insert app name]! Heres some key notes on what the aspects of this app are.")
            print(" 1. Tasks: Tasks are divided into [3] categories and [4] levels of difficulty. Lets go over task types first.\n    a) Daily task: Dailys are repeatable and will increase your [score] when completed. To remove a task you will need to go to Edit to delete them, because they will be persistent otherwise \n    b) Habit: Habits can be positive ones that you want to break or negative ones that you want to break. Registering that you've done a negative habit will decrease your [score]. \n    c) To Do: To Do's are one and done tasks, completing them will remove them from the to do list permanently.")
            print("Now about difficulties. Difficulty, or ease, will be set when you create a task. This will determine how much your [score] increase or decrease when you complete the task (or fail to). The scale is incremental, 1=Trivial,2=Easy, 3=Medium, 4=Hard.")

        # SAVE AND EXIT
        elif selection == "0":
            menuloop = False
            save()
            print("\nCome again soon!")

        # ERROR MESSAGE FOR NON APPLICABLE INPUTS
        else:
            print("\nERR please enter a valid number")

        # wait before continuing
        input("\n[press enter]")


#                     ##########################classes
class Task:
    typeOptions = ["daily", "habit", "to do"]
    def __init__(self, name, ease):
        self.name = name
        self.ease = ease
        #self.completed = False

    # methods
    def changetype(self, newease):
        self.ease = newease

    def kys(self):
        task_list.remove(self)


class Daily(Task):
    # repeats and can be completed multiple times or has a completion length
    def __init__(self, name, ease):
        super().__init__(name, ease)
        self.type = "daily"

class Habit(Task):
    # can be pos or neg for habits to make or break, can plus or minus one
    def __init__(self, name, ease, goodness):
        super().__init__(name, ease)
        self.type = "habit"
        self.goodness = goodness
    
    def thing():
        pass

class ToDo(Task):
    # does not repeat, can be completed once
    def __init__(self, name, ease):
        super().__init__(name, ease)
        self.type = "to-do"


class Player:
    def __init__(self):
        self.healthmax = 50
        self.health = 50
        self.exproof = 500
        self.exp = 500
        self.lvl = 0
        self.wallet = 15
    
    def hurt(self, dmg):
        self.health += dmg
    
    def heal(self, health):
        self.health += health
        self.exp += health * 1.4


#                     ##########################functions


def create_new_task():

    # difficulty dictionary
    easedict = {
        1: "trivial",
        2: "easy",
        3: "medium",
        4: "hard"
    }
    # habit good or bad dict
    gbdict = {
        1: "good",
        2: "bad"
    }
    
    # select task type & invalid repeats
    name = input("input the name of your task\n> ")
    typeselect = int(input("what num type would you like 1.daily 2.habit 3.todo\n> "))
    while True:
        if typeselect not in range(1,4):
            print("Invalid input.")
            typeselect = int(input("what num type would you like 1.daily 2.habit 3.todo\n> "))
        else: break

    # select task ease & invalid repeats
    easeselect = int(input("on a scale from 1-4, how difficult will this task be to complete? (1=trivial- 4=hard)\n> "))
    while True:
        if typeselect not in range(1,5):
            print("Invalid input.")
            easeselect = int(input("on a scale from 1-4, how difficult will this task be to complete? (1=trivial- 4=hard)\n> "))
        else: break

    easeact = easedict[easeselect]

    # create task
    if typeselect == 1:
        newtask = Daily(name,easeact)
        task_list.append(newtask)

    # ask for goodness if it's a habit
    elif typeselect == 2:
        goodness = int(input("Is this 1. A Good habit to Make? or 2. A Bad habit to Break?\n> "))
        while True:
            if typeselect not in range(1,3):
                print("Invalid input.")
                goodness = int(input("Is this 1. A Good habit to Make? or 2. A Bad habit to Break?\n> "))
            else: break
        goodnessact = gbdict[goodness]
        newtask = Habit(name,easeact,goodnessact)
        task_list.append(newtask)

    elif typeselect == 3:
        newtask = ToDo(name,easeact)
        task_list.append(newtask)

    print(f"NEW TASK CREATED:\nTitle- {name}, Type- {newtask.type}", end = ", ")
    if newtask.type == "habit":
        print(f"Goodness- {newtask.goodness}", end=", ")
    print(f"Ease- {newtask.ease}")
# -act as in actual

def donetask():
    int(input("which would u like to have done"))
    try:
        taskathand = task_list[input-1]
        # handle each type of task
        # handle daily
        if taskathand.type == "daily":
            print(f"Congratulations! You've done {taskathand.name}")
            input(f"")
        # handle habits
        elif taskathand.type == "habit":
            if taskathand.goodnes == "good":
                input(f"Congratulations! You've done ")



    except ValueError or IndexError:
        print("Invalid.")

#print off each item in list
def display_all(list):
    for i in range(len(list)):
        n = list[i].name

        print(f"\n{i+1}. {n}:\n    {list[i].type.upper()}", end = " ")
        if list[i].type == "habit":
            print(f"Goodness: {list[i].goodness}", end=", ")
        print(f"Ease: {list[i].ease}")


#saving stuff
def loadsaved():
    with open("savedtasks.json", "r") as file:
        task_dicts = json.load(file)
        for task in task_dicts:
            if task["type"] == "daily":
                newtask = Daily(task["name"],task["ease"])
                task_list.append(newtask)
            elif task["type"] == "to-do":
                newtask = ToDo(task["name"],task["ease"])
                task_list.append(newtask)
            elif task["type"] == "habit":
                newtask = Habit(task["name"],task["ease"],task["goodness"])
                task_list.append(newtask)

def save():
    with open("savedtasks.json", "w") as file_object:
        task_list2 = [task.__dict__ for task in task_list]
        json.dump(task_list2, file_object)


main()



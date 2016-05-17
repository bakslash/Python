import time
global apples
global gold
gold = 0

def start():
    print "hello welcome"
    name = raw_input("what is your name")
    print "welcome, "+name+"!"
    print "collect apples"
    print "sell apples"
    choice = raw_input("do you want to play y/n")
    if choice == "y":
        begin()
    if choice == "n":
        print "bye"
def begin():
    global apples
    global gold
    print"lets get started..."
    if gold > 99:
        print "you have won the game"
        play = raw_input("do you want to play again")
        if play == "y":
            begin()
        if play == "n":
            print "congrats"
    pick = raw_input("do you want to pick an apple y/n")
    if pick == "y":
        time.sleep(1)
        print"you pick an apple"
        apples=apples+1
        print "you currently have ",apples,"apples"
        begin()
    if pick =="n":
        sell = raw_input("do u want to sell ur apples")
        if sell == "y":
            global gold
            global apples
            print "you currently have"+apples+"apples"
            print "you have sold your apples"
            gold=apples*10
            apples=0
            print"your apples is now "+gold
        
    
start()

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
    print"lets get started"
start()

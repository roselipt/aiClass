#  hw2.10  Implement the farmer, fox, goose and grain problem

#  The program's goal is to move all four across the river using
#  only a reflex-based agent testing against four illegal states
#  (or two illegal states in two possible locations)

#  In an effort to write python that doesn't just look like code
#  I would write in another language I decided NOT to represent
#  the two sides of river as a boolean but to instead use two lists. 
start = ["farmer", "fox", "goose", "grain"]
finish = []

#  Given a list as parameter this function tests if the list
#  contains an illegal pair if the farmer were to leave it as is.
def check (l) :
    if "fox" in l and "goose" in l : return False
    elif "goose" in l and "grain" in l : return False
    else : return True

#  Since the farmer always moves, any action may be expressed by
#  the thing which he takes.
#  This function takes an item to move as parameter, checks which
#  side the farmer is on and moves both across the river.
#  I had trouble accommodating the farmer moving with no cargo here
#  so I left that in the main program body.
#  Given more time I'd fix this arrangement.
def move (item) :
    if "farmer" in start :
        start.remove("farmer")
        start.remove(item)
        finish.append("farmer")
        finish.append(item)
    else :# "farmer" in finish :
        finish.remove("farmer")
        finish.remove(item)
        start.append("farmer")
        start.append(item)

#  Main program body : Should you always make a main in python?
#  I didn't need one so I didn't

print(start, "   //   ", finish)

#  Repeat until start is empty
while len(start) > 0 :    
    # if farmer is on start side
    if "farmer" in start :
        # Test if taking each item would leave a legal arrangement 
        for each in start :
            if each != "farmer" :
                test_list = start.copy()
                test_list.remove(each)
                if check(test_list) :
                    move(each)
    #  else farmer is on finish side
    else : 
        #  Make copy of finish list to test
        test_list = finish.copy()
        #  Try to leave all and return farmer to start alone as default
        if check(test_list) :
            #  move farmer back to start alone
            finish.remove("farmer")
            start.append("farmer")
        #  Check if taking something back works
        else :
            #  Repeat until legal arrangement to leave behind is found
            while not check(test_list) :                
                if test_list[0] != "farmer" :
                    return_with = test_list.pop(0)
                    if check(test_list) : move (return_with)
                    else : test_list.append(return_with)
                                
    #  Print each move (each iteration of while loop)                
    print(start, "   //   ", finish)
    
#end

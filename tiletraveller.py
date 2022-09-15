#leikreglur

"""Leikurinn virkar þannig að ..."""



print("You can travel (N)orth.")
travel = input("Direction: ")

x = 1
y = 1

def move(x,y):
    if (travel == "n") or (travel == "N"):
        y + 1
        x = x
        return "You can travel (N)orth or (E)ast or (S)outh."
    else:
        return "Not a valid direction!"
               
print(move(x,y))
    

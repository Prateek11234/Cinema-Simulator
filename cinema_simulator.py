films = {
    "Finding Dory":[3,5],
    "Bourne":[18,5],
    "Tarzan":[15,5],
    "Ghost Busters":[12,5]
    }

while True:

    choice=input("what film would you like to watch?: ").strip().title()

#check user age
    if choice in films:   
        age = int(input("how old are you?: ").strip())   #int is used coz when the input is taken it takes input as a string only if it gives the value as an integer also. so, that's why int keyword is used in order to convert the strings into int.
        if age >= films[choice][0]:
            #check enough seats
            if films[choice][1]>0:
                print("you can watch the film.. ")
            films[choice][1] = films[choice][1]-1
            else:
                print("sorry,we are sold out.. ")
        else:
            print("you are too young to watch the film")
    else:
        print("film not found")

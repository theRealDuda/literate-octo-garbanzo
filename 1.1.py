def find_repetitions(firstl, secondl):
    repeated = []
    for item in firstl:
        if item in secondl:
            repeated.append(item)
    return repeated

def main():
    firstlist = []
    secondlist = []
    action = 0
    new_list = []
    while action != "4":
        print(
            "Choose an action: \
                \n1) Edit the first list. \
                \n2) Edit the second list. \
                \n3) Check repeated members. \
                \n5) Quit.\n"
        )
        action = input()
        if action == "1":
            new_list = input("Input the new list. Members must be separated by spaces: ").split() 
        if action == "2":
            new_list = input("Input the new list. Members must be separated by spaces: ").split() 
        if action == "3":
            print(find_repetitions(firstlist, secondlist))
        if action == "4":
            return 0
        else:
            print("Choose another action.")
    return 0

if __name__=="__main__":
    main()
   

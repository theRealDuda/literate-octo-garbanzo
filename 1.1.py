def find_repetitions(firstl, secondl):
    repeated = set() 
    for item in firstl:
        if firstl.count(item) > 1 and item in secondl:
            repeated = repeated.union(item)
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
                \n4) Quit.\n"
        )
        action = input()
        if action == "1":
            new_list = input("Input the new list. Members must be separated by spaces: ").split() 
            firstlist = new_list
        if action == "2":
            new_list = input("Input the new list. Members must be separated by spaces: ").split() 
            secondlist = new_list
        if action == "3":
            print("Here are the repetitions: ")
            for repeat in find_repetitions(firstlist, secondlist):
                print(repeat, end = " ")
            print("\n")
        if action == "4":
            return 0

if __name__=="__main__":
    main()
   

"""Get the items that repeat in two lists"""
def find_same(firstl, secondl):
    """Finds the items that are in b and a"""
    same = set()
    for item in firstl:
        if item in secondl:
            same = same.union(item)
    return same

def main():
    """Main function implementing a menu"""
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
            new_list = input("Input the new list.\
            Members must be separated by spaces: ").split()
            firstlist = new_list
        if action == "2":
            new_list = input("Input the new list.\
            Members must be separated by spaces: ").split()
            secondlist = new_list
        if action == "3":
            print("Here are the same items: ")
            for repeat in find_same(firstlist, secondlist):
                print(repeat, end = " ")
            print("\n")

if __name__=="__main__":
    main()

def getList():
    lst = []
    print('Enter numbers one at a time. Enter 0 to stop.')
    x = int(input('num: '))
    while x != 0:
        lst.append(x)
        x = int(input('num: '))
    return lst

def getChoice(data):
    print('Here is the data:')
    print(data)

    choice = ''
    while True:
        choice = input('Select an option. 1-sum  2-min  3-max  4-quit  ')
        choiceOption(data, choice)

def choiceOption(data, choice):
    if choice == '1':
        print(f"The sum is {sum(data)}")
    elif choice == '2':
        print(f"The min is {min(data)}")
    elif choice == '3':
        print(f"Not supported yet")
    elif choice == '4':
        print('Goodbye')
        exit(0)

def main():
    print("Hello, World")
    getChoice(getList())

if __name__ == "__main__":
    main()
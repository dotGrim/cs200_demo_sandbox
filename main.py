def func1():
    lst = []
    print('Enter numbers one at a time. Enter 0 to stop.')
    x = int(input('num:'))
    while x != 0:
        lst.append(x)
        x = int(input('num:'))
    return lst

def func2(data):

    choice = ''
    while True:
        choice = input('Select an option. 1-sum  2-min  3-max  4-quit')
        choiceOption(data, choice)

def choiceOption(data, choice):
    if choice == '1':
        print(f"The sum is {sum(data)}")
    elif choice == '2':
        print(f"The min is {min(data)}")
    elif choice == '3':
        print(f"The max is {max(data)}")
    elif choice == '4':
        print('Goodbye')
        exit(0)

def main():
    data = func1()
    print(f"Original List: {data}")
    func2(data)

if __name__ == "__main__":
    main()
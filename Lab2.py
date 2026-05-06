def display_main_menu():
    print("Please enter numbers separated by commas, eg. 5, 67, 32.")


def get_user_input():
    userStr = input("Numbers: ")
    userList = []
    for number in userStr.split(", "):
        userList.append(number)

    return userList


def calc_average(numList):
    sum = 0.00
    for number in numList:
        sum += float(number)

    return round((sum / len(numList)), 2)


def find_min_max(numList):
    min = 100
    max = 0 

    for number in numList:
        if float(number) > max:
            max = float(number)
        
        if float(number) < min:
            min = float(number)

    return [min, max]


def sort_temperature(numList):
    return sorted(numList)


def calc_median_temp(numList):
    listItems = len(numList)
    median = 0

    if listItems % 2 != 0:
        median = numList[listItems // 2]
    else:
        firstNum = listItems // 2 - 1
        secondNum = listItems // 2
        median = (float(numList[firstNum]) + float(numList[secondNum])) / 2.0

    return median 


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python Programming")
    display_main_menu()
    num_list = get_user_input()

    avg_temp = calc_average(num_list)
    print(f"Average: {avg_temp}")

    minNMax = find_min_max(num_list)
    print(minNMax)
    
    sortedList = sort_temperature(num_list)
    print(calc_median_temp(sortedList))


if name=="main":
    main()
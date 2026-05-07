def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    #bmi calc
    bmi = weight/(height*height)
    if (bmi < 18.5):
        return -1
    elif (18.5 <= bmi <= 25.0 ):
        return 0
    elif(bmi>25.0):
        return 1
calculate_bmi(weight=57, height=1.73)
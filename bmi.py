def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    #bmi calc
    bmi = weight/(height*height)
    if (bmi < 18.5):
        print ("Under Weight")
    elif (18.5 <= bmi <= 25.0 ):
        print ("Normal Weight")
    elif(bmi>25.0):
        print("Over Weight")

calculate_bmi(weight=57, height=1.73)
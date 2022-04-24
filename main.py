# Description: Determine an individual's BMI

# TODO: Turn everything into functions, get a GUI, and generally make this
# slightly more sophisticated than it is now (not hard).




if __name__ == "__main__":
    # Get the user's weight in pounds and height in inches.
    weight = float(input("Enter your weight in pounds: "))
    height = float(input("Enter your height in inches: "))
    
    # Calculate the BMI.
    # Apparently, for small exponents, x * x is faster than pow(x, 2).
    # Anyway, this is using the US customary system.
    bmi = round((weight * 703) / (height * height), 0)
    
    print("Your BMI is", bmi)
    
    # Determine the category of the BMI.
    # Categories based on US for those 21 and older.
    if bmi > 0:
        if bmi < 16:
            print("You are severely underweight.")
        elif bmi < 18.5:
            print("You are underweight.")
        elif bmi < 25:
            print("You are normal.")
        elif bmi < 30:
            print("You are overweight.")
        elif bmi < 35:
            print("You are obese.")
        else:
            print("...this is advanced obesity.")
    else:
        print("Really? Height:", height, "inches and Weight:", weight, "pounds?\nHard doubt.")

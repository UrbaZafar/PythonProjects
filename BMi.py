def calculate_bmi(weigh, height):
    """Calculate BMI."""
    return weigh / (height ** 2)  # Return the BMI value

def classify_bmi(bmi):
    """Classify BMI into categories."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    """Run the BMI calculator."""
    print("BMI Calculator")
    print("--------------")

    # Get user input for weight and height
    weigh = float(input("Enter your weigh (kg): "))  # Weight in kg
    height = float(input("Enter your height (m): "))  # Height in meters

    # Calculate and classify BMI
    bmi = calculate_bmi(weigh, height)  # Calculate BMI
    category = classify_bmi(bmi)     

    # Display results
    print(f"Your BMI is: {bmi:.2f}")  # 2 decimal places
    print(f"You are: {category}")     #  category

if __name__ == "__main__":
    main()  

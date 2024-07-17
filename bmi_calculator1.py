def calculate_bmi(weight, height):
    """
    Calculate BMI given weight in kilograms and height in meters.
    """
    if height <= 0:
        raise ValueError("Height must be greater than zero.")
    if weight <= 0:
        raise ValueError("Weight must be greater than zero.")
    
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def get_bmi_category(bmi):
    """
    Determine the BMI category.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

if __name__ == "__main__":
    try:
        # Get user input for weight and height
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        
        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        
        # Get BMI category
        category = get_bmi_category(bmi)
        
        # Display the result
        print(f"Your BMI is: {bmi}")
        print(f"Health status: {category}")
    
    except ValueError as e:
        print(f"Error: {e}")

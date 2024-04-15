import math

def degrees_to_radians(degrees):
    """
    Convert degrees to radians.
    
    Arguments:
    degrees -- Angle in degrees
    
    Returns:
    Angle in radians
    """
    return degrees * (math.pi / 180)

def radians_to_degrees(radians):
    """
    Convert radians to degrees.
    
    Arguments:
    radians -- Angle in radians
    
    Returns:
    Angle in degrees
    """
    return radians * (180 / math.pi)

def main():
    print("Degree and Radian Converter")
    print("---------------------------")
    angle_degrees = float(input("Enter the angle in degrees: "))
    angle_radians = degrees_to_radians(angle_degrees)
    print(f"{angle_degrees} degrees is equal to {angle_radians:.2f} radians.")

    angle_radians = float(input("Enter the angle in radians: "))
    angle_degrees = radians_to_degrees(angle_radians)
    print(f"{angle_radians:.2f} radians is equal to {angle_degrees} degrees.")

if __name__ == "__main__":
    main()

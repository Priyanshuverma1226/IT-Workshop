# Write a function called calculate_slope which return the slope of a linear equation

def calculate_slope(x1,y1,x2,y2):
    m=(y2-y1)/(x2-x1)
    return m
    
print(calculate_slope(2,2,3,5))
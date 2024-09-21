import math
#https://hive.blog/hive-196387/@juecoree/forward-and-reverse-kinematics-for-3r-planar-manipulator
def revKinematics(l1, l2, l3, l4, x, y, z, orientation):
    x3 = x - l4 * math.cos(orientation)
    z3 = z - l4 * math.cos(orientation)

    alpha = math.acos((x3**2 + (z3-l1)**2 - l2**2 - l3**2) / (2 * l2 * l3))
    beta = math.asin(l2 * math.sin(alpha) / math.sqrt(x3**2 + (z3-l1)**2))
    theta1 = math.atan((z3-l1)/x3) + beta 
    theta2 = 180 - (-180 - alpha)
    theta3 = orientation - theta1 - theta2
    phi = math.acos(math.sqrt(x**2 + y**2 + z**2))
    
    return theta1, theta2, theta3, phi

def main():
    print("Enter l1: ")
    l1 = input()
    print("Enter l2: ")
    l2 = input()
    print("Enter 3l: ")
    l3 = input()
    print("Enter l4: ")
    l4 = input()
    print("Enter x: ")
    x = input()
    print("Enter y: ") 
    y = input()
    print("Enter z: ")
    z = input()
    print("Enter orientation")
    orientation = input()

    print(revKinematics(l1, l2, l3, l4, x, y, z, orientation))


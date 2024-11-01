import math
#https://hive.blog/hive-196387/@juecoree/forward-and-reverse-kinematics-for-3r-planar-manipulator
def rev_kine(l1, l2, l3, l4, x, y, z, orientation):
    x3 = x - l4 * math.cos(math.radians(orientation))
    z3 = z - l4 * math.cos(math.radians(orientation))

    alpha = math.acos((x3**2 + (z3-l1)**2 - l2**2 - l3**2) / (2 * l2 * l3))
    beta = math.asin(l2 * math.sin(alpha) / math.sqrt(x3**2 + (z3-l1)**2))
    theta1 = math.atan((z3-l1)/x3) + beta 
    theta2 = -(180 - alpha)
    theta3 = orientation - theta1 - theta2
    phi = math.atan(x / y)
    
    return { "theta1": math.degrees(theta1), "theta2": math.degrees(theta2), "theta3": math.degrees(theta3), "phi": math.degrees(phi) }

def kine(l1, l2, l3, l4, theta1, theta2, theta3, phi):
    x = l2 * math.cos(math.radians(theta1)) + l3 * math.cos(math.radians(theta2)) + l4 * math.cos(math.radians(theta3))
    z = l2 * math.sin(math.radians(theta1)) + l3 * math.sin(math.radians(theta2)) + l4 * math.cos(math.radians(theta3))
    d = math.sqrt(x**2 + z**2);
    z += l1

    x = d * math.sin(math.radians(phi))
    y = d * math.cos(math.radians(phi))

    orientation = theta1 + theta2 + theta3
    
    return { 'x': x, 'y': y, 'z': z, 'orientation': math.degrees(orientation) }

def main():
    a = { "l1": 1, "l2": 1, "l3": 1, "l4": 1, "t1": 15, "t2": 30, "t3": 25, "phi": 45 }
    res = kine( a["l1"], a["l2"], a["l3"], a["l4"], a["t1"], a["t2"], a["t3"], a["phi"]);
    res2 = rev_kine(a["l1"], a["l2"], a["l3"], a["l4"], res["x"], res["y"], res["z"], res["orientation"])
    print (res, res2)

    print(kine(0,1,1,1,0,0,0,90));
    print(rev_kine(0,1,1,1,3,0,0,0));

main()

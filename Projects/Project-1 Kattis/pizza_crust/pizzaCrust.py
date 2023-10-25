# Problem was 1.9 difficulty at time of completion

pi = 3.14

def pizza_time(c,r)->float:
    cheese = r - c
    total_area = pi * (r**2)
    cheese_area = pi * (cheese**2)
    cheese_percent = (cheese_area/total_area) * 100
    return cheese_percent

if(__name__ == "__main__"):
    radius, crust = input().split()
    crust = int(crust)
    radius = int(radius)
    print("{:.6f}".format(pizza_time(crust,radius)))

import math
pos = [0,0]
while True:
    s = input()
    if not s:
        break
    movement = s.split(" ")   
    direction = movement[1]
    steps = int(movement[2])     #since up and down in an axis is on the y axis and left and right is on the x axis, we have the the first pos
    if direction=="UP":          #
        pos[1]+=steps #5
    elif direction=="DOWN":  #5-3 = 2 2^2 = 4
        pos[1]-=steps #3
    elif direction=="LEFT":
        pos[0]-=steps #3
    elif direction=="RIGHT": #2-3+2 = 1 1^2 = 1
        pos[0]+=steps #2
    else:
        pass

print(int(round(math.sqrt(pos[1]**2+pos[0]**2))))
# pos 1^2 + pos 0^2 then square root answer then round up to nearest integer
# 25+36 = 61sqrt = 7.8 = 8
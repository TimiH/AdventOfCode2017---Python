# --- Day 11: Hex Ed ---
#
# Crossing the bridge, you've barely reached the other side of the stream when a program comes up to you, clearly in distress. "It's my child process," she says, "he's gotten lost in an infinite grid!"
#
# Fortunately for her, you have plenty of experience with infinite grids.
#
# Unfortunately for you, it's a hex grid.
#
# The hexagons ("hexes") in this grid are aligned such that adjacent hexes can be found to the north, northeast, southeast, south, southwest, and northwest:
#
#   \ n  /
# nw +--+ ne
#   /    \
# -+      +-
#   \    /
# sw +--+ se
#   / s  \
#
# You have the path the child process took. Starting where he started, you need to determine the fewest number of steps required to reach him. (A "step" means to move from the hex you are in to any adjacent hex.)
#
# For example:
#
#     ne,ne,ne is 3 steps away.
#     ne,ne,sw,sw is 0 steps away (back where you started).
#     ne,ne,s,s is 2 steps away (se,se).
#     se,sw,se,sw,sw is 3 steps away (s,s,sw).
#
# To begin, get your puzzle input.



def Main():
    data = open("day11_input.txt","r")
    instructions = data.read().strip().split(",")

    #3d
    x = 0
    y = 0
    z = 0

    distances = []

    for c in instructions:
        if c == 'n':
            y +=1
            z -=1
        if c == 's':
            y -=1
            z +=1
        if c == 'ne':
            y+=1
            x-=1
        if c == 'nw':
            z-=1
            x+=1
        if c == 'se':
            z+=1
            x-=1
        if c == 'sw':
            y-=1
            x+=1
        distances.append(max(abs(x),abs(y), abs(z)))

    #print x, y, z

    steps2 = max(abs(x),abs(y), abs(z))
    maxi = max(distances)
    print "Last Distance: " , steps2
    print "Max Distanc: ", maxi

if __name__ == '__main__':
    Main()



















                                                                                                                                                                                                                                                                                                                                                                                                                                                                        

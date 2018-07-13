from Node import Node
from random import randint,choice
import os

# # Prototype v1
# def move_down(position):
#     temp = position
#     while temp.below is not None:
#         if temp.below.data == temp.data or temp.below.data == 0:
#             temp.below.data += temp.data
#             temp.data = 0
#         temp = temp.below

# Prototype v2
def move_down(position):
    for kali in range(1,4):
        temp = position
        while temp.over is not None:
            if temp.over.data == temp.data:
                temp.data += temp.over.data
                temp.over.data = 0
            elif temp.data == 0 and temp.over.data != 0:
                sementara = temp.over.data 
                temp.data = sementara
                temp.over.data = 0
            temp = temp.over

# # Prototype v1
# def move_up(position):
#     temp = position
#     while temp.over is not None:
#         if temp.over.data == temp.data or temp.over.data == 0:
#             temp.over.data += temp.data
#             temp.data = 0
#         temp = temp.over

# Prototype v2
def move_up(position):
    for kali in range(1,4):
        temp = position
        while temp.below is not None:
            if temp.below.data == temp.data:
                temp.data += temp.below.data
                temp.below.data = 0
            elif temp.data == 0 and temp.below.data != 0:
                sementara = temp.below.data 
                temp.data = sementara
                temp.below.data = 0
            temp = temp.below

# #prototype v1
# def move_right(position):
#     temp = position
#     while temp.right is not None:
#         # print(temp.data)
#         if temp.right.data == temp.data or temp.right.data == 0:
#             temp.right.data += temp.data
#             temp.data = 0
#         temp = temp.right
# Prototype v2
def move_right(position):
    for kali in range(1,4):
        temp = position
        while temp.left is not None:
            if temp.left.data == temp.data:
                temp.data += temp.left.data
                temp.left.data = 0
            elif temp.data == 0 and temp.left.data != 0:
                sementara = temp.left.data 
                temp.data = sementara
                temp.left.data = 0
            temp = temp.left
# # Prototype v1
# def move_left(position):
#     temp = position
#     while temp.left is not None:
#         # print(temp.data)
#         if temp.left.data == temp.data or temp.left.data == 0:
#             temp.left.data += temp.data
#             temp.data = 0
#         temp = temp.left

# Prototype v2
def move_left(position):
    for kali in range(1,4):
        temp = position
        while temp.right is not None:
            if temp.right.data == temp.data:
                temp.data += temp.right.data
                temp.right.data = 0
            elif temp.data == 0 and temp.right.data != 0:
                sementara = temp.right.data 
                temp.data = sementara
                temp.right.data = 0
            temp = temp.right


#Setup da Nodes
p1 = Node() 
p2 = Node()
p3 = Node()
p4 = Node()
p5 = Node()
p6 = Node()
p7 = Node()
p8 = Node()
p9 = Node()
p10 = Node()
p11 = Node()
p12 = Node()
p13 = Node()
p14 = Node()
p15 = Node()
p16 = Node()

#Setup Node Location
# p1
p1.cornerUpLeft(p2,p5)
#p2
p2.upEdge(p1,p3,p6)
#p3
p3.upEdge(p2,p4,p7)
#p4
p4.cornerUpRight(p3,p8)
#p5
p5.leftEdge(p6,p1,p9)
#p6
p6.center(p5,p7,p2,p10)
#p7
p7.center(p6,p8,p3,p11)
#p8
p8.rightEdge(p7,p4,p12)
#p9
p9.leftEdge(p10,p5,p13)
#p10
p10.center(p9,p11,p6,p14)
#p11
p11.center(p10,p12,p7,p15)
#p12
p12.rightEdge(p11,p8,p16)
#p13
p13.cornerBottomLeft(p14,p9)
#p14
p14.bottomEdge(p13,p15,p10)
#p15
p15.bottomEdge(p14,p16,p11)
#p16
p16.cornerBottomRight(p15,p12)
# board ->  1 \ 2 \ 3 \ 4 \
#           5 \ 6 \ 7 \ 8 |
#           9 | 10| 11| 12|
#           13| 14| 15| 16|

#Pinggirifikasi
pinggir = [p1,p2,p3,p4,p8,p12,p16,p15,p14,p13,p9,p5]
#All data
allData = [p1.data,p2.data,p3.data,p4.data,p5.data,p6.data,p7.data,p8.data,p9.data,p10.data,p11.data,p12.data,p13.data,p14.data,p15.data,p16.data]
while True:
    os.system("clear")
    # Choosing Random int
    while True:
        while True:
            randomizer = choice(pinggir) # randint(1,17) cuman buat test
            if randomizer.data == 0:
                break
        #Randomizing number 2 / 4
        randomizer1 = randint(2,4)  # Generate number 2 / 4 
        if randomizer1 == 3:        #agar angka yang muncul 2 / 4 saja
            randomizer1 +=1
        randomizer.data = randomizer1
        break
    print(""" 
=================================
| {0:^5d} | {1:^5d} | {2:^5d} | {3:^5d} |
=================================
| {4:^5d} | {5:^5d} | {6:^5d} | {7:^5d} |
=================================
| {8:^5d} | {9:^5d} | {10:^5d} | {11:^5d} |
=================================
| {12:^5d} | {13:^5d} | {14:^5d} | {15:^5d} |
=================================""".format(p1.data,p2.data,p3.data,p4.data,p5.data,p6.data,p7.data,p8.data,p9.data,p10.data,p11.data,p12.data,p13.data,p14.data,p15.data,p16.data))
    if 0 not in allData:
        print("Game End !")
        break
    
    #Inputan gerak
    masukan = input("w/a/s/d = ")
    
    #Moving Stances
    if masukan == "s":
    # Move Down
        # move_down(p1)
        # move_down(p2)
        # move_down(p3)
        # move_down(p4)
        move_down(p13)
        move_down(p14)
        move_down(p15)
        move_down(p16)
    elif masukan == "w":
    # Move Up
        # move_up(p13)
        # move_up(p14)
        # move_up(p15)
        # move_up(p16)
        move_up(p1)
        move_up(p2)
        move_up(p3)
        move_up(p4)
    elif masukan == "a":
    # Nove Left
        # move_left(p4)
        # move_left(p8)
        # move_left(p12)
        # move_left(p16)
        move_left(p1)
        move_left(p5)
        move_left(p9)
        move_left(p13)
    elif masukan == "d":
    # Move Right
        # move_right(p1)
        # move_right(p5)
        # move_right(p9)
        # move_right(p13)
        move_right(p4)
        move_right(p8)
        move_right(p12)
        move_right(p16)

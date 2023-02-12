import keyboard
import time 

# while True:
#     if keyboard.is_pressed("a"):
#         print("1")
#     if keyboard.is_pressed("b"):
#         print("2")


# # keyboard.add_hotkey('ctrl+a','s')
# # while True:
# #     keyboard.on_press(print("hello"))
# #     time.sleep(2)

#User Input and Table Setup:
row_num = int(input("Row num: "))
column_num = int(input("Column num: "))
ar = []
(x,y)=1,1


for j in range(column_num):
    ar.append([])
    for i in range(row_num):
        ar[j].append(0)

#Display function

def display():
    print(5*'\n')
    for j in range(column_num):
        print(ar[j])

#Movement Function
def up(x,y):
    if y<column_num:
        ar[y][x] = 0
        y -= 1

def down(x,y):
    if y>0:
        ar[y][x] = 0
        y += 1

def left(x,y):
    if x>0:
        ar[y][x] = 0
        x -= 1

def right(x,y):
    if x<row_num:
        ar[y][x] = 0
        x += 1


    
ar[y][x]=1    
display()



while True:
    
    event=keyboard.read_event()
    if event.name == "up":
        print("up")
        up(x,y)
    if event.name == "down":
        down(x,y)
        print("down")
    if event.name == "left":
        left(x,y)
        print("left")
    if event.name == "right":
        right(x,y)
        print("right")
    time.sleep(0.2)
    
    ar[y][x]=1

    display()


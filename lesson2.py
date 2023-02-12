
import keyboard, time

row_num = int(input("Put row num: "))
column_num = int(input("Put column num: "))

ar = []
x,y = (1, 1)


for i in range(column_num):
    ar.append([])
    for j in range(row_num):
        ar[i].append(0)

#Display function
def display():
    global x, y, ar
    print(5*"\n")
    ar[y][x] = 1
    for i in range(column_num):
        print(ar[i])
    
    


print(ar)

display()

#Movement functions
def up():
    global x, y, ar
    ar[y][x]=0
    y -= 1
    

def down():
    global x, y, ar
    ar[y][x]=0
    y += 1

def left():
    global x, y, ar
    ar[y][x]=0
    x -= 1

def right():
    global x, y, ar
    ar[y][x]=0
    x += 1

    
# Name(a,b)



running = True
while running:
    event = keyboard.read_event()
    if event.name == "up":
        up()
    if event.name == "down":
        down()
    if event.name == "left":
        left()
    if event.name == "right":
        right()



    time.sleep(0.2)

    display()



#baslalalalalalal


#this is another update
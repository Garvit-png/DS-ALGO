# recursion - when a function keeps calling itself until a specified condition is met 

# agr base condition nahi doge toh function kbhi complete hi ni ho payega and keeps on calling, and at the end it will do the segmentation -  STACK OVERFLOW


# the condition you use the stop the recursion is called the base condition


count = 0

def counter():
    global count

    if count >= 10:
        return

    print(count)
    count += 1
    counter()

counter()
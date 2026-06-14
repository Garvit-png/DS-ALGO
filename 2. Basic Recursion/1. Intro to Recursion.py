# Recursion - when a function call itself , until a specified condition is met




#printing 1 with recursion with no base condition

# def f():
#     print(1)
#     f()

# f()




# Stack overflow - jab recursion mein ek function call hota hai , and then voh dubara khud ko hi call krta hai  , toh pichla function waiting mein chla jata hai , because voh kabhi poora hi nahi hua, yeh wait bar bar ek stack mein bhrta jata hai , and at the end , stack overflow ho jata hai 


#|    f()   |
#|    f()   |
#|    f()   |
#|    f()   |  stack overflow hogya 
#|____f()___|






def f(count):
    if count==1002:
        return 
    print(count)
    count+=1
    f(count)
f(0)
# name - Gourav khurana 
# Roll no - 17EEBCS028
# Iot lab Examination 
# Date- 19 Feb 2021 

def foo(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        return 0
x = (int)(input("Enter x: "))
y = (int)(input("Enter y: "))        
print(foo(x,y))
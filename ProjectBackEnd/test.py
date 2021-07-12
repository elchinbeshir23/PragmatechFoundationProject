# # -Write a Python function to multiply all the numbers in a list.

# def numberlist():
#     numbers=[8, 2, 3, -1, 7]
#     cem=1
#     for i in numbers:
#         cem *=i
#         print(cem)
#     return cem
# numberlist()


# -Write a function called returnDay. This function takes in one parameter ( a number from 1-7)
# and returns the day of the week ( 1 is Sunday, 2 is Monday etc.). If the number is less than 1 or
# greater
# than 7, the function should return None.


# def returnsday():
#     weekday=int(input("eded daxil edin : "))
#     weekdays={1:"Monday",2"Thursday","wednesday":3,"thoursday":4,"friday":5,"saturday":6,"sunday":7}
#     if 1<=weekday<=7:
#         print(weekdays[weekday])
#     else:
#         print("bir le yeddi araliginda reqem yazin")
    

# returnsday()

# def numbers(listtt):
#     if len(listtt)>0:
#         print(listtt[-1])
#     else:
#         print(None)
# numbers([1,2,3,4,5,6,7,8])

def evenNumbers(numbers):
     evenNums=[]
     for i in numbers:
         if i%2==0:
             evenNums.append(i)
     print(*evenNums)

evenNumbers([1,2,3,4,5,6,7,8,9])


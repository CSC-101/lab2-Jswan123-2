# Create a welcome message.
# Input: a name as a string
# Result: a string
def welcome_message(name:str) -> str:
   message = "Hello, " + name + "."
   return message


def smallest (n:float, m:float) -> float:
   if n < m:
      return n          #For which calls below is this statement evaluated? Only for the Second Call.
   else:
      return m


def function2(a:int, b:int, c:int) -> int:
   if a>b and a>c:
      return a-b     #In general when will a call to this function evaluate this statement? when the first interger is greater than the 2nd and 3rd.
   elif b>c:
      return b+c     #In general, when will a call to this function evaluate this statement? A call to this function will be made if the 1st interger is not greater than both b or c but b is greater than c.
   else:
      return 2*c     #In general when will a call to this fucntion evaluate this statment? Whenever all other circumstances for example a is not greater than both b and c and b is not greater than c.

message = welcome_message("Jaswan@calpoly.edu")
print(message)

first = smallest(3,2)     #What is the value of the first? 2
second = smallest(2,2)    #What is the value of the second? Is this a reasonable result? Why or why not? 2 and no because both of the values are the same so smallest value is an incorrect categorization.
print(first)
print(second)

answer1= function2(3,2,1)     #What is the value of answer1? 2
answer2= function2(2,3,1)     #What is the value of function2? 4
answer3= function2(2,1,3)     #What is the value of answer 3? 6
print(answer1)
print(answer2)
print(answer3)

from typing import Optional             # gain access to the Optional[X] type hint


def checked_access(L:list[int], idx:int) -> Optional[int]:
    test = idx >= 0 and idx < len(L)    # What is the value of test on each call? is it greater than or equal to 0.
    if test:                            # What is this check preventing? Any scores above 1
        return L[idx]
    else:
        return None


first = checked_access([1, 0, 1], 9)     # What is the value of first? None
second = checked_access([1, 0, 1], 2)    # What is the value of second? 1
print(first)
print (second)


def length_sum(L: list[str]) -> int:
   if len(L) > 2:
      result = len(L[0]) + len(L[1]) + len(L[2])  # For which call below is this statement evaluated
   elif len(L) > 1:  # and what are the values being added? the first statement and its each word.
      result = len(L[0]) + len(L[1])  # For which call below is this statement evaluated
   elif len(L) > 0:  # and what are the values being added?
      result = len(L[0])  # For which call below is this statement evaluated
   else:  # and what are the values being added?
      result = 0
   return result


first = length_sum(["this", "is", "the", "first", "call"])
second = length_sum(["second call"])
third = length_sum(["another", "call"])
print()


def surprising(L: list[str], other: str) -> list[str]:
   L.append(other.upper())
   return L


words = ["this", "is", "confusing", "code."]
first = surprising(words, "Avoid")
second = surprising(words, "such.")
# What is the value of words at this point?
# What are the values of first and second at this point?
# What happened?
print(first)
print(second)
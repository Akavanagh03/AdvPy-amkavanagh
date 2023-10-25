import sys
from typing import List

jonCount = 0
docCount = 0

def countA(answer):
    i = 0
    while(answer[i] == "a"):
        i+=1
    return i

def compare(j,d)->str:
    if(d > j):
        return("no")
    if(d<=j):
        return("go")
    
def goOrNo(a,b) -> str:
    jonCount = intake(a)
    docCount = intake(b)
    return(compare(jonCount,docCount))

def intake(person):
    count = countA(person)
    return(count)
    

# As of 9/5/23 this problem was a 2.1 on kattis.com
if __name__ == "__main__":
    jon = input()
    doctor = input()
    print(goOrNo(jon,doctor))


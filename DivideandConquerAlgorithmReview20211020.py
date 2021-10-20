# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 08:50:33 2021

@author: men_l
"""
#Number Factor
def numberFactor(n):
    if n in [0,1,2]:
        return 1
    elif n == 3:
        return 2 
    else:
        subP1 = numberFactor(n-1)
        subP2 = numberFactor (n-3)
        subP3 = numberFactor(n-4)
        return subP1 + subP2 + subP3

#HouseRobber
def RobHouse(houses, currentIndex):
    if currentIndex >= len(houses):
        return 0
    else:
        stealFirstHouse = houses[currentIndex] + RobHouse(houses, currentIndex+2)
        skipFirstHouse = RobHouse(houses, currentIndex+1)
        return max(stealFirstHouse, skipFirstHouse)
        
houses = [6,7,1,30,8,2,4]
# print(RobHouse(houses, 0)) 

def ConvertOneStringToAnother(s1,s2,index1,index2):
    if len(s1) == index1:
        return len(s2) - index2
    if len(s2) == index2:
        return len(s1) - index1
    if s1[index1] == s2[index2]:
        return ConvertOneStringToAnother(s1, s2, index1+1, index2+1)
    else:
        deleteOp = 1 + ConvertOneStringToAnother(s1, s2, index1, index2+1)
        insertOp = 1 + ConvertOneStringToAnother(s1, s2, index1 +1 , index2)
        replaceOp = 1 + ConvertOneStringToAnother(s1, s2, index1 + 1, index2 + 1)
        return min (deleteOp, insertOp, replaceOp)
        
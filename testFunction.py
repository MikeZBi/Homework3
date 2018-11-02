import math

##########################
#
# Summary: Functions works the same as before, but to accomodate for no mutation we used list slicing.
#          We took a copy of the list by slicing the list into left, right and node we are attempting
#          to change. We then concatenate the currentNode to change with the value to insert and this
#          makes it so that we can insert into a copy without mutating the original.
#
#
#
##########################
def recNodeBreak(theString, nodeSize, numberInNode, whichNode, listOfLists, i):

    if (len(theString) == 1):
        #listOfLists[whichNode].insert(0, (int(theString[i])))
        leftList = listOfLists[:whichNode]
        middleList = [[int(theString[i])] + listOfLists[whichNode]]
        rightList = listOfLists[whichNode+1:]

        combinedList = leftList + middleList + rightList
        #print(combinedList)
        return combinedList
    elif (i == -1):
        #print(listOfLists)
        #print(type(listOfLists))
        return listOfLists
    elif (i > -1 and numberInNode < nodeSize):
        #listOfLists[whichNode].insert(0, (int(theString[i])))
        leftList = listOfLists[:whichNode]
        middleList = [[int(theString[i])] + listOfLists[whichNode]]
        rightList = listOfLists[whichNode+1:]

        combinedList = leftList + middleList + rightList
        #print(combinedList)
        return(recNodeBreak(theString, nodeSize, numberInNode + 1, whichNode, combinedList, i - 1))
    elif (i > -1 and numberInNode == nodeSize):
        #whichNode -= 1
        #numberInNode = 0
        #listOfLists[whichNode-1].insert(0, (int(theString[i])))
        leftList = listOfLists[:whichNode-1]
        middleList = [[int(theString[i])] + listOfLists[whichNode-1]]
        rightList = listOfLists[whichNode:]

        combinedList = leftList + middleList + rightList
        #print(combinedList)
        return(recNodeBreak(theString, nodeSize, 1 ,whichNode -1, combinedList, i - 1))


####################################################################################
#  Summary: Similar as before, but no mutation of the orginal passed in list, used list slicing and
#           and concatenation of lists to achieve this instead of insertions
#
#
#
####################################################################################


def zeroPad(whichNode, nodeSize, listA, listB):
    if (len(listA) == len(listB) and whichNode == len(listA)):
        # print("if")
        return listA

    elif (len(listA) != len(listB)):
        # print("elif1")
        if (len(listA) < len(listB)):
            #listA.insert(0, [])
            leftList = [[]]
            rightList = listA
            combined = leftList + rightList
            return(zeroPad(whichNode, nodeSize, combined, listB))
        else:
            #listB.insert(0, [])
            leftList = [[]]
            rightList = listB
            combined = leftList + rightList
            return(zeroPad(whichNode, nodeSize, listA, combined))

    elif (len(listA[whichNode]) < nodeSize or len(listB[whichNode]) < nodeSize):
        # print("elif2", whichNode)
        # print(listA)
        # print(listB)

        if (len(listA[whichNode]) < nodeSize):
            # print("elif2 if")

            #listA[whichNode].insert(0, 0)
            leftList = listA[:whichNode]
            middleList = [[0] + listA[whichNode]]
            rightList = listA[whichNode + 1:]

            combinedList = leftList + middleList + rightList

            # print(listA)
            return(zeroPad(whichNode, nodeSize, combinedList, listB))
        else:
            # print("elif2 else")

            #listB[whichNode].insert(0, 0)
            leftList = listB[:whichNode]
            middleList = [[0] + listB[whichNode]]
            rightList = listB[whichNode + 1:]

            combinedList = leftList + middleList + rightList

            # print(listB)
            return(zeroPad(whichNode, nodeSize, listA, combinedList))

    elif (len(listA[whichNode]) == nodeSize and len(listB[whichNode]) == nodeSize):
        # print("elif3")

        #whichNode += 1
        return(zeroPad(whichNode+1, nodeSize, listA, listB))
    
    
####################################################################################
#  Summary: This time no slice is needed, we just make a copy of the listC which is
#           the list that is holding the current sum of the numbers so far. Then
#           concatenate that with the value of the next numbers that are added, and
#           pass this into the function instead of insertions
#
#
#
####################################################################################
def recAdd(listA, listB, listC, whichNode, numberInNode, nodeSize, carryOver):
    if (whichNode == -1):
        # print("if")
        #listC.insert(0, carryOver)
        #print(listC)
        leftList = [carryOver]
        rightList = listC


        combinedList = leftList + rightList
        #return listC
        return combinedList
    elif (whichNode > -1 and numberInNode > -1):

        # print("elif1")
        # print(whichNode, numberInNode)

        toInsert = (listA[whichNode][numberInNode] + listB[whichNode][numberInNode] + carryOver) % 10
        # print(toInsert)
        # print(carryOver)
        carryOver = (listA[whichNode][numberInNode] + listB[whichNode][numberInNode] + carryOver) // 10
        # print(carryOver)
        #numberInNode -= 1
        #listC.insert(0, toInsert)

        leftList = toInsert
        rightList = listC

        combinedList = [leftList] + rightList

        #print(combinedList)
        return recAdd(listA, listB, combinedList, whichNode, numberInNode-1, nodeSize, carryOver)
    elif (whichNode >= -1 and numberInNode == -1):
        # print("elif2")
        whichNode -= 1
        numberInNode = len(listA[0]) - 1
        # print(whichNode, numberInNode)
        if (whichNode == -1):
            return recAdd(listA, listB, listC, whichNode, numberInNode, nodeSize, carryOver)
        else:
            # print(whichNode, numberInNode)
            toInsert = (listA[whichNode][numberInNode] + listB[whichNode][numberInNode] + carryOver) % 10
            carryOver = (listA[whichNode][numberInNode] + listB[whichNode][numberInNode] + carryOver) // 10
            #listC.insert(0, toInsert)
            leftList = toInsert
            rightList = listC

            combinedList = [leftList] + rightList
            #print(listC)
            #numberInNode -= 1
            return recAdd(listA, listB, combinedList, whichNode, numberInNode-1, nodeSize, carryOver)



myString = "123456789"
nodeSize = 3
numberInNode = 0
whichNode = (math.ceil(len(myString) / nodeSize)) - 1
# Initialize a 2dList, create another variable called numberOfNodes for ease of use
numberOfNodes = (math.ceil(len(myString) / nodeSize))
listOfLists = [0] * (numberOfNodes)
for i in range(numberOfNodes):
    listOfLists[i] = []
i = len(myString) - 1

c = recNodeBreak(myString, nodeSize, numberInNode, whichNode, listOfLists, i)
print(c)


myString1 = "1234"
nodeSize1 = 3
numberInNode1 = 0
whichNode1 = (math.ceil(len(myString1) / nodeSize1)) - 1
# Initialize a 2dList, create another variable called numberOfNodes for ease of use
numberOfNodes1 = (math.ceil(len(myString1) / nodeSize1))
listOfLists1 = [0] * (numberOfNodes1)
for i in range(numberOfNodes1):
    listOfLists1[i] = []
j = len(myString1) - 1


# this is the recursion driver method, uncommet the prints in the method to show the process
d = recNodeBreak(myString1, nodeSize1, numberInNode1, whichNode1, listOfLists1, j)
print(d)


thisNode = 0
h = zeroPad(thisNode, nodeSize, c, d)
z = zeroPad(thisNode, nodeSize, d, c)

print(h)
print(z)



# #print(listOfLists)
# originalList = [[0,0],[1,2],[4],[5,6]]
# listLeft = originalList[:2]
# #print(listLeft)
#
# listRight = originalList[3:]
# #print(listRight)
#
# listMiddle =  [ [3] + originalList[2] ]
# #print(listMiddle)

# listCombine = listLeft+ listMiddle+ listRight
#print(listCombine)






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
        print(listOfLists)
        print(type(listOfLists))
        return listOfLists
    elif (i > -1 and numberInNode < nodeSize):
        #listOfLists[whichNode].insert(0, (int(theString[i])))
        leftList = listOfLists[:whichNode]
        middleList = [[int(theString[i])] + listOfLists[whichNode]]
        rightList = listOfLists[whichNode+1:]

        combinedList = leftList + middleList + rightList
        #print(combinedList)
        recNodeBreak(theString, nodeSize, numberInNode + 1, whichNode, combinedList, i - 1)
    elif (i > -1 and numberInNode == nodeSize):
        #whichNode -= 1
        #numberInNode = 0
        #listOfLists[whichNode-1].insert(0, (int(theString[i])))
        leftList = listOfLists[:whichNode-1]
        middleList = [[int(theString[i])] + listOfLists[whichNode-1]]
        rightList = listOfLists[whichNode:]

        combinedList = leftList + middleList + rightList
        #print(combinedList)
        recNodeBreak(theString, nodeSize, 1 ,whichNode -1, combinedList, i - 1)

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




# this is the recursion driver method, uncommet the prints in the method to show the process
listCombiner = recNodeBreak(myString, nodeSize, numberInNode, whichNode, listOfLists, i)
#print(listCombiner)


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






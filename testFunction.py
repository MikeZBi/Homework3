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

def toMultiply(listA, listB, listC, whichNodeA, whichNodeB, indexA, indexB, indexC, carryOver, carryOverAdd, n):
    if (whichNodeA == 0 and whichNodeB == 0 and indexA == 0 and indexB == 0):
        # print("if")
        toInsert = (listA[whichNodeA][indexA] * listB[whichNodeB][indexB] + carryOver) % 10
        carryOver = (listA[whichNodeA][indexA] * listB[whichNodeB][indexB] + carryOver) // 10
        # listC.insert(0, toInsert)
        # print("this is the value to insert", toInsert)
        # print("value of carryOver", carryOver)
        # print("value of carryOverAdd", carryOverAdd)
        toAdd = listC[indexC]
        # print("value of listC: ", listC)
        # print("value of indexC", indexC)
        # print("value of listC at indexC", listC[indexC])
        #listC[indexC] = (toAdd + toInsert + carryOverAdd) % 10
        leftList = listC[:indexC]
        middleList = [(toAdd + toInsert + carryOverAdd) % 10]
        rightList = listC[indexC + 1:]

        combinedList = leftList + middleList + rightList

        #carryOverAdd = (toAdd + toInsert + carryOverAdd) // 10
        carryOverLeft = combinedList[:indexC - 1]
        carryOverMiddle = [((toAdd + toInsert + carryOverAdd) // 10)+carryOver]
        carryOverRight = combinedList[indexC:]

        finalCombinedList = carryOverLeft + carryOverMiddle + carryOverRight

        # print("value of carryOverAdd", carryOverAdd)
        #listC[indexC - 1] = carryOverAdd + carryOver

        return finalCombinedList





    # for some list B with one node and one item, and be able to multiply through listA that has one node and many items
    elif (whichNodeB >= 0 and indexB >= 0 and whichNodeA > -1 and indexA > 0 and indexC >= 0):
        # print("elif1: traversing the current node")
        # print("here is indexC", indexC, " and value at indexC", listC[indexC])
        # print("which NodeA:", whichNodeA, "which indexA: ", indexA, " number mult: ", listA[whichNodeA][indexA])
        # print("which NodeB:", whichNodeB, "which indexB: ", indexB, " n mult: ", listB[whichNodeB][indexB])
        # print("current carry over: ", carryOver)
        toInsert = (listA[whichNodeA][indexA] * listB[whichNodeB][indexB] + carryOver) % 10
        carryOver = (listA[whichNodeA][indexA] * listB[whichNodeB][indexB] + carryOver) // 10
        # print("new carry over: ", carryOver)
        # print("number toInsert: ", toInsert)
        #listC.insert(0, toInsert)
        toAdd = listC[indexC]

        #listC[indexC] = (toAdd + toInsert + carryOverAdd) % 10
        leftList = listC[:indexC]
        middleList = [(toAdd + toInsert + carryOverAdd) % 10]
        rightList = listC[indexC+1:]

        combinedList = leftList + middleList + rightList

        # print("number in listC: ", listC[indexC])
        carryOverAdd = (toAdd + toInsert + carryOverAdd) // 10
        # print("carryOverAdd: ", carryOverAdd)
        # print("numbers in listC: ", listC)
        #print(listC)
        return toMultiply(listA, listB, combinedList, whichNodeA, whichNodeB, indexA - 1, indexB, indexC - 1, carryOver, carryOverAdd,
                   n)


    # this is to loop through nodes in listA
    elif (whichNodeB >= 0 and indexB >= 0 and whichNodeA > 0 and indexA == 0):
        # print("elif2: the max of a node has been reached, we multiplying the last index of current node")
        # print("then after this, we should have changed to the next node of listA")
        # print("which NodeA:", whichNodeA, "which indexA: ", indexA, " number mult: ", listA[whichNodeA][indexA])
        # print("which NodeB:", whichNodeB, "which indexB: ", indexB, " n mult: ", listB[whichNodeB][indexB])

        # print("current carry over: ", carryOver)
        toInsert = (listA[whichNodeA][indexA] * listB[whichNodeB][indexB] + carryOver) % 10
        carryOver = (listA[whichNodeA][indexA] * listB[whichNodeB][indexB] + carryOver) // 10
        # print("new carry over: ", carryOver)
        # print("number toInsert: ", toInsert)
        # print("value of index C", indexC)

        toAdd = listC[indexC]
        #listC[indexC] = (toAdd + toInsert + carryOverAdd) % 10
        leftList = listC[:indexC]
        middleList = [(toAdd + toInsert + carryOverAdd) % 10]
        rightList = listC[indexC + 1:]

        combinedList = leftList + middleList + rightList



        # print("number in listC: ", listC[indexC])
        carryOverAdd = (toAdd + toInsert + carryOverAdd) // 10
        # print("carryOverAdd: ", carryOverAdd)

        #whichNodeA -= 1
        #indexA = len(listA[whichNodeA]) - 1
        # if(whichNodeA == -1 and indexA == 1 and carryOver != 0):
        #     print("elif2 if")
        #     listC.insert(indexC, carryOver)
        #     carryOver = 0

        # print("numbers in listC", listC)
        # print("which NodeA:", whichNodeA, "which indexA: ", indexA, " number mult: ", listA[whichNodeA][indexA])
        # print("which NodeB:", whichNodeB, "which indexB: ", indexB, " n mult: ", listB[whichNodeB][indexB])
        #print(listC)
        return toMultiply(listA, listB, combinedList, whichNodeA-1, whichNodeB, len(listA[whichNodeA]) - 1, indexB, indexC - 1, carryOver, carryOverAdd, n)


    # loop through index in listB; this happens when we are on the last index of the last node in listA
    elif (whichNodeB >= 0 and indexB > 0 and whichNodeA == 0 and indexA == 0):
        # print("elif3: this will process the 0th index of the 0th node in listA")
        # print("it will also change nodeA back to the left most once it has finished")
        # print("which NodeA:", whichNodeA, "which indexA: ", indexA)
        # print("which NodeB:", whichNodeB, "which indexB: ", indexA)

        toInsert = (listA[whichNodeA][indexA] * listB[whichNodeB][indexB] + carryOver) % 10
        carryOver = (listA[whichNodeA][indexA] * listB[whichNodeB][indexB] + carryOver) // 10

        # this is attempting that, since the carryOver will be max of 8 (ie. 9*9 = 81) and max of carryOverAdd = 1
        # we can just add them together and even if both are 0, it will be bad since its at the very end, and
        # will be the largest current number, as indexC will constantly be pushed to the left each elif3
        toAdd = listC[indexC]
        #listC[indexC] = (toAdd + toInsert + carryOverAdd) % 10
        leftList = listC[:indexC]
        middleList = [(toAdd + toInsert + carryOverAdd) % 10]
        rightList = listC[indexC + 1:]

        combinedList = leftList + middleList + rightList


        carryOverAdd = (toAdd + toInsert + carryOverAdd) // 10

        #listC[indexC - 1] = carryOverAdd + carryOver
        carryOverLeft = combinedList[:indexC-1]
        carryOverMiddle = [carryOverAdd + carryOver]
        carryOverRight = combinedList[indexC:]

        finalCombinedList = carryOverLeft+ carryOverMiddle + carryOverRight
        # Need to reset the carryOver and carryOverAdd back to 0
        #carryOver = 0
        #carryOverAdd = 0
        # reset node back to the furthest left element
        #whichNodeA = len(listA) - 1
        # reset the indexA to the size of the next node value
        #indexA = len(listA[whichNodeA]) - 1
        # move the index of B left one
        #indexB = indexB - 1
        # to move where we are adding by left 1 index each time we traverse an index of B
        #indexC = len(listC) - (n + 1)
        # change the value of n so that we subtract a larger n
        #n += 1
        # print("A entire multiplication has finished, reseting whichNodeA back to right most node:", whichNodeA)

        # print("indexA:", indexA)
        # print("whichNodeA", whichNodeA)
        # print(listC)
        #print(listC)
        return toMultiply(listA, listB, finalCombinedList, len(listA) - 1, whichNodeB, len(listA[whichNodeA]) - 1, indexB-1, len(listC) - (n + 1), 0, 0, n+1)


    # finally need to be able to change the node in B
    elif (whichNodeB > 0 and indexB == 0 and whichNodeA == 0 and indexA == 0):
        # print("elif4: the last item in listA has been reached, and it is the last item in current nodeB")
        # print(
        #    "we process the current item, and will reset back to furthest A, and onto the next node when this is done")
        toInsert = (listA[whichNodeA][indexA] * listB[whichNodeB][indexB] + carryOver) % 10
        carryOver = (listA[whichNodeA][indexA] * listB[whichNodeB][indexB] + carryOver) // 10

        toAdd = listC[indexC]
        #listC[indexC] = (toInsert + toAdd + carryOverAdd) % 10
        leftList = listC[:indexC]
        middleList = [(toAdd + toInsert + carryOverAdd) % 10]
        rightList = listC[indexC + 1:]

        combinedList = leftList + middleList + rightList

        carryOverAdd = (toInsert + toAdd + carryOverAdd) // 10
        # since this is still the end of a listA multiplication, we need to make sure the carryOver and carryOverAdd are just inserted to the front most of the current index




        #listC[indexC - 1] = carryOverAdd + carryOver

        carryOverLeft = combinedList[:indexC - 1]
        carryOverMiddle = [((toAdd + toInsert + carryOverAdd) // 10) + carryOver]
        carryOverRight = combinedList[indexC:]

        finalCombinedList = carryOverLeft + carryOverMiddle + carryOverRight






        #carryOverAdd = 0
        #carryOver = 0

        # finished a lsitA multiply, so reset back to last node and right most element in that node
        #whichNodeA = len(listA) - 1
        #indexA = len(listA[whichNodeA]) - 1

        # change the node for B
        #whichNodeB -= 1
        # change the index to the right most index of that list
        #indexB = len(listB[whichNodeB]) - 1

        # need to reset where the indexC, as we have finished a multiply and need to start a new line, the index must start one left since we have to add a 0 in signifigance
        #indexC = len(listC) - (n + 1)
        #n += 1
        # print("here is listC: ", listC)
        #print(listC)
        return toMultiply(listA, listB, finalCombinedList, len(listA) - 1, whichNodeB-1, len(listA[whichNodeA]) - 1, len(listB[whichNodeB]) - 1, len(listC) - (n + 1), 0, 0, n+1)

def destroyLeadingZero(listA):
    if (listA[0] != 0) or (len(listA) == 1):
        return listA
    else:
        #del listA[0]
        rightList = listA[1:]
        return destroyLeadingZero(rightList)
    
 
def recToString(listC, listLen, i):
    if (i == listLen - 1):
        # print(i)
        theReturnedString = listC[i]
        print(theReturnedString)
        return str(theReturnedString)
    elif (i < listLen):
        # print(i)
        theReturnedString = listC[i]
        print(theReturnedString)
        return str(theReturnedString) + recToString(listC, listLen, i + 1)


        
        

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






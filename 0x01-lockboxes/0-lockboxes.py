#!/usr/bin/python3
"""given a number of boxes, write a program to check if all boxes can be opened
"""


def canUnlockAll(boxes):
    """check if all boxes can be opened"""
    boxState = []
    for i in range(len(boxes)):
        boxState.append(False)

    numBefore = 0
    boxState[numBefore] = True
    allKeys = [0]
    for box in boxes:
        if boxes.index(box) in allKeys:
            for key in box:
                allKeys.append(key)
        numBefore += 1

    print(set(allKeys))
    boxNum = 0

    for box in boxes:
        if boxNum in allKeys:
            for key in box:
                if key < len(boxes):
                    boxState[key] = True
        boxNum += 1
    for box in boxState:
        if box is False:
            return False
    return True

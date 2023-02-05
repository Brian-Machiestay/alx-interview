#!/usr/bin/python3
"""given a number of boxes, write a program to check if all boxes can be opened
"""


def canUnlockAll(boxes):
    """check if all boxes can be opened"""
    boxState = []
    for i in range(len(boxes)):
        for box in boxes:
            for key in box:
                if key == i:
                    boxState.append(True)
                    break
            if len(boxState) == i + 1:
                break
        if len(boxState) == i + 1:
            continue
        boxState.append(False)

    boxNum = 0
    boxState[boxNum] = True
    for box in boxes:
        if boxState[boxNum] is True:
            for key in box:
                if key < len(boxes):
                    boxState[key] = True
        boxNum += 1
    for box in boxState:
        if box is False:
            return False
    return True

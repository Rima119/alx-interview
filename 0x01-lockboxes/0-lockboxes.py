#!/usr/bin/python3
"""a mathod that determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """
    Return True if all boxes can be opened, else return False
    """
    n = len(boxes)
    stack = [0]
    unlocked_box = [1] + [0] * (n - 1)
    a = 0

    if n == 0:
        return True
    while stack:
        b = stack.pop()
        for idx in boxes[b]:
            if idx > 0 and idx < n and unlocked_box[idx] == 0:
                unlocked_box[idx] = 1
                stack.append(idx)
        a = a + 1
    if 0 in unlocked_box:
        return False
    return True

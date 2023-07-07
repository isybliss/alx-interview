#!/usr/bin/python3
"""Determine if all boxes can be unlocked"""


def canUnlockAll(boxes):
    """
    boxes: boxes to be unlocked
    Return: True or False
    """

    """
    box_len = len(boxes)
    queue = [0]
    unlocked_box = [1] + [0] * (box_len - 1)
    i = 0

    if box_len == 0:
        return True

    while queue:
        j = queue.pop()
        for index in boxes[j]:
            if index > 0 and index < box_len and unlocked_box[index] == 0:
                unlocked_box[index] = 1
                queue.append(index)
        i = i + 1
    if 0 in unlocked_box:
        return False
    return True
    """

    box_len = len(boxes)
    unlocked = [False] * box_len
    unlocked[0] = True
    queue = [0]

    while queue:
        box_index = queue.pop(0)
        keys = boxes[box_index]
        for key in keys:
            if key < box_len and not unlocked[key]:
                unlocked[key] = True
                queue.append(key)
    return all(unlocked)

#!/usr/bin/python3
"""
A Function for determining if all boxes in a given list can be opened.
"""

def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked.

    Args:
        boxes (list of list): A list of lists representing the boxes and their keys.

    Returns:
        bool: True if all boxes can be unlocked, otherwise False.
    """

    if not boxes:
        return False

    num_boxes = len(boxes)
    unlocked_boxes = [False] * num_boxes
    unlocked_boxes[0] = True  
    keys = boxes[0]

    for key in keys:
        if 0 <= key < num_boxes and not unlocked_boxes[key]:
            unlocked_boxes[key] = True
            keys += boxes[key]

    return all(unlocked_boxes)

#!/usr/bin/python3
"""determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """Check if all boxes can be opened
    """

    keys = [0]
    for key in keys:
        for box_key in boxes[key]:
            if box_key not in keys and boxKey < len(boxes):
                keys.append(box_key)
    if len(keys) == len(boxes):
        return True
    return False

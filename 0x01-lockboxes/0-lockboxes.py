#!/usr/bin/python3
'''
============== Lockboxes =======================
You have n number of locked boxes in front of you. Each box
is numbered sequentially from 0 to n - 1 and each box may
contain keys to the other boxes.

  - Write a method that determines if all the boxes can be opened.

    * Prototype: def canUnlockAll(boxes)
    * boxes is a list of lists
    * A key with the same number as a box opens that box
    * You can assume all keys will be positive integers
    * There can be keys that do not have boxes
    * The first box boxes[0] is unlocked
    * Return True if all boxes can be opened, else return False
'''


def canUnlockAll(boxes):
    """ canUnlockAll(boxes) """
    boxes_len = len(boxes)
    valid_boxes = [0]
    inValideBoxes = set(boxes[0]).difference(set([0]))

    while len(inValideBoxes) > 0:
        n_boxes = inValideBoxes.pop()
        if not n_boxes or n_boxes >= boxes_len or n_boxes < 0:
            continue
        if n_boxes not in valid_boxes:
            inValideBoxes = inValideBoxes.union(boxes[n_boxes])
            valid_boxes.append(n_boxes)
    return boxes_len == len(valid_boxes)

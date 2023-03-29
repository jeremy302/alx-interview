#!/usr/bin/python3
''' lock boxes module '''


def canUnlockAll(boxes):
    ''' checks if all boxes can be unlocked '''
    box_count = len(boxes)
    unlocked = [0 for v in range(box_count)]
    unlocked_count = 0
    queue = []
    if boxes:
        unlocked[0] = 1
        unlocked_count += 1
        queue.append(0)

    while queue:
        box_id = queue[0]
        box = boxes[box_id]
        for key in box:
            if key >= box_count or unlocked[key]:
                continue
            unlocked[key] = 1
            unlocked_count += 1
            queue.append(key)
        queue.remove(box_id)
    return unlocked_count == box_count
    # return all(unlocked)

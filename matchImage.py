#! /usr/bin/env python
import numpy as np
import cv2

def matchImage(fileName, type, maxVal=130000000):
    # load the puzzle and waldo images
    puzzle = cv2.imread(fileName)
    waldo = cv2.imread(type)
    (waldoHeight, waldoWidth) = waldo.shape[:2]

    # find the waldo in the puzzle
    result = cv2.matchTemplate(puzzle, waldo, cv2.TM_CCOEFF)
    (min_val, max_val, minLoc, maxLoc) = cv2.minMaxLoc(result)
    print('Match value', max_val)
    if max_val <= maxVal:
        return False, False
    # grab the bounding box of waldo and extract him from
    # the puzzle image
    topLeft = maxLoc
    botRight = (topLeft[0] + waldoWidth, topLeft[1] + waldoHeight)
    roi = puzzle[topLeft[1]:botRight[1], topLeft[0]:botRight[0]]

    print('Click point', topLeft[0] + waldoWidth / 2, topLeft[1] + waldoHeight / 2)
    return topLeft[0] + waldoWidth / 2, topLeft[1] + waldoHeight / 2 
    # construct a darkened transparent 'layer' to darken everything
    # in the puzzle except for waldo
    # mask = np.zeros(puzzle.shape, dtype = "uint8")
    # puzzle = cv2.addWeighted(puzzle, 0.25, mask, 0.75, 0)

    # put the original waldo back in the image so that he is
    # 'brighter' than the rest of the image
    # puzzle[topLeft[1]:botRight[1], topLeft[0]:botRight[0]] = roi
    # cv2.imshow("Puzzle", puzzle)
    # cv2.imshow("Waldo", waldo)
    # cv2.waitKey(0)

# matchImage('inZoom.png','demon.png')  
# print matchImage('inRoom.png','isInMap.png')  
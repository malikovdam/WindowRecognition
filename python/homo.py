import cv2
import numpy as np

p1 = np.array([[0., 0], [0., 1], [1., 1], [1., 0]])
p2 = np.array([[0, 0], [0.2, 1], [0.8, 1], [1, 0]])

h = cv2.findHomography(p1, p2)[0]

print h

print h.dot([0, 1, 1])


def norm(point):
    ret = h.dot(np.append(point, [1]))
    ret /= ret[2]
    return ret[:2]


def denorm(point):
    ret = np.linalg.inv(h).dot(np.append(point, [1]))
    ret /= ret[2]
    return ret[:2]


print np.linalg.inv(h).dot([0.8,1,1])

print np.linalg.norm(denorm(p2[1]) - denorm(p2[0]))
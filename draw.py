import cv2
import math

import numpy as np
import numpy.typing as npt


class DrawLineOnImage:
    def __init__(self, image: np.ndarray, width: int = 200, alpha: int = 0) -> None:
        self.original_image = image
        self.w = width
        self.alpha = alpha

        # start drawing at the center
        self.x = int(0.5 * image.shape[0])
        self.y = int(0.5 * image.shape[1])

        # create opencv window
        self.windowName = "Barrier on Railway Crossing"
        cv2.namedWindow(self.windowName, cv2.WINDOW_AUTOSIZE)

        # create trackbars
        cv2.createTrackbar('Width', self.windowName, self.w, image.shape[0], self.update_parameters)
        cv2.createTrackbar('Middle point x', self.windowName, self.x, image.shape[0], self.update_parameters)
        cv2.createTrackbar('Middle point y', self.windowName, self.y, image.shape[1], self.update_parameters)
        cv2.createTrackbar('Alpha', self.windowName, self.alpha, 180, self.update_parameters)

    def update_parameters(self, *args) -> None:
        self.w = cv2.getTrackbarPos('Width', self.windowName)
        self.x = cv2.getTrackbarPos('Middle point x', self.windowName)
        self.y = cv2.getTrackbarPos('Middle point y', self.windowName)
        self.alpha = cv2.getTrackbarPos('Alpha', self.windowName)

        self.update_image()

    def calc_line(self):
        d = self.w / 2
        alpha_radians = math.radians(self.alpha)
        sin_alpha = math.sin(alpha_radians)
        cos_alpha = math.cos(alpha_radians)

        self.x1 = self.x - (d * cos_alpha)
        self.x1 = int(self.x1)

        self.y1 = self.y + (d * sin_alpha)
        self.y1 = int(self.y1)

        self.x2 = self.x + (d * cos_alpha)
        self.x2 = int(self.x2)

        self.y2 = self.y - (d * sin_alpha)
        self.y2 = int(self.y2)

    def update_image(self) -> None:
        # clear the image
        image = self.original_image.copy()
        cv2.imshow(self.windowName, image)

        # draw line
        self.calc_line()
        cv2.line(image, (self.x1, self.y1), (self.x2, self.y2), (0, 255, 0), thickness=2)

        # draw middle point
        cv2.circle(image, (self.x, self.y), 5, (0, 0, 0), thickness=-1, lineType=cv2.LINE_AA)

        # show updated image
        cv2.imshow(self.windowName, image)

    def show_image(self) -> None:
        self.update_image()
        c = cv2.waitKey(0)
        cv2.destroyAllWindows()

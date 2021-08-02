# Author: Joe Thompson
# Date: 8/1/2021
# Description:

class Gear:
    def __init__(self, teeth, id):
        self._num_teeth = teeth
        self._angle = 0
        self._id = id

    def get_num_teeth(self):
        return self._num_teeth

    def get_angle(self):
        return self._angle

    def get_id(self):
        return self._id

    def rotate(self, angle):
        self._angle += angle
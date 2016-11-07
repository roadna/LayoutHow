import numpy as np


class Analyze:
    text = ""
    text_length = 0
    letter_count = {}
    letter_freq = {}

    def __init__(self, filename):
        self.text = open(filename, 'r').read().replace(" ", "").lower()
        self.text_length = len(self.text)
        for ascii_code in range(ord("a"), ord("z") + 1):
            counter_result = self.text.count(chr(ascii_code))
            self.letter_count[chr(ascii_code)] = counter_result

        for ascii_code in range(ord("a"), ord("z") + 1):
            letter = chr(ascii_code)
            self.letter_freq[letter] = "%.2f" % (self.letter_count[letter] / self.text_length * 100)

    def heat_map(self, layout):
        h_map = np.zeros((3, 10))
        for row in range(0, 3):
            for col in range(0, 10):
                if ord("a") <= ord(layout[row][col]) <= ord("z"):
                    h_map[row][col] = self.letter_freq[layout[row][col]]
        return h_map

    def finger_usage(self, layout, heat_map=None):
        if heat_map is None:
            heat_map = self.heat_map(layout)
        calc_m = np.array([[1, 1, 1]])
        col_sum = np.dot(calc_m, heat_map)
        finger_usage = np.zeros((1, 8))
        for col in range(0, 10):
            if 3 <= col <= 6:
                if col == 3:
                    finger_usage[0][col] = col_sum[0][col] + col_sum[0][col + 1]
                elif col == 6:
                    finger_usage[0][col - 2] = col_sum[0][col] + col_sum[0][col - 1]
            elif col < 3:
                finger_usage[0][col] = col_sum[0][col]
            elif col > 6:
                finger_usage[0][col - 2] = col_sum[0][col]
        return finger_usage

    def middle_usage(self, layout, heat_map=None):
        if heat_map is None:
            heat_map = self.heat_map(layout)
        m_usage = np.zeros((1, 2))
        m_usage[0][0] = heat_map[0][4] + heat_map[1][4] + heat_map[2][4]
        m_usage[0][1] = heat_map[0][5] + heat_map[1][5] + heat_map[2][5]
        return m_usage

    def grade(self, layout, heat_map=None):
        if heat_map is None:
            heat_map = self.heat_map(layout)
        grading_scale = np.array([[5,   2, 2, 3, 4.5, 4.5, 3, 2, 2, 5],
                                  [1.5, 1, 1, 1, 3,   3,   1, 1, 1, 1.5],
                                  [4.5, 4, 3, 2, 4,   4,   2, 3, 4, 4.5]])
        grade_matrix = heat_map * grading_scale
        grades = 0
        for row in range(3):
            for col in range(10):
                grades += grade_matrix[row][col]
        return grade_matrix, grades

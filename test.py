import sys
import numpy as np
import LayoutAnalysis
import Layouts

la = LayoutAnalysis.Analyze(sys.argv[1])

# finger_usage = la.finger_usage(Layouts.qwerty, heat_map)
# print(finger_usage)
heat_map = la.heat_map(Layouts.qwerty)
grades = la.grade(Layouts.qwerty, heat_map)
middle_usage = la.middle_usage(Layouts.qwerty, heat_map)
print("qwerty", grades, middle_usage)
index = la.get_index(Layouts.qwerty)
print(la.grade_string("hello world", Layouts.qwerty))
print(la.grade_string("ing th ly est er", Layouts.qwerty))

heat_map = la.heat_map(Layouts.norman)
grades = la.grade(Layouts.norman, heat_map)
middle_usage = la.middle_usage(Layouts.norman, heat_map)
print("norman", grades, middle_usage)
print(la.grade_string("hello world", Layouts.norman))
print(la.grade_string("ing th ly est er", Layouts.norman))

import sys
import numpy as np
import LayoutAnalysis
import Layouts

la = LayoutAnalysis.Analyze(sys.argv[1])

#finger_usage = la.finger_usage(Layouts.qwerty, heat_map)
#print(finger_usage)
heat_map = la.heat_map(Layouts.qwerty)
grades = la.grade(Layouts.qwerty, heat_map)
middle_usage = la.middle_usage(Layouts.qwerty, heat_map)
print("qwerty", grades[1], middle_usage)

heat_map = la.heat_map(Layouts.dvorak)
grades = la.grade(Layouts.dvorak, heat_map)
middle_usage = la.middle_usage(Layouts.dvorak, heat_map)
print("dvorak", grades[1], middle_usage)

heat_map = la.heat_map(Layouts.colemak)
grades = la.grade(Layouts.colemak, heat_map)
middle_usage = la.middle_usage(Layouts.colemak, heat_map)
print("colemak", grades[1], middle_usage)

heat_map = la.heat_map(Layouts.norman)
grades = la.grade(Layouts.norman, heat_map)
middle_usage = la.middle_usage(Layouts.norman, heat_map)
print("norman", grades[1], middle_usage)

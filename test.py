import sys
import numpy as np
import LayoutAnalysis
import Layouts

la = LayoutAnalysis.Analyze(sys.argv[1])
print(Layouts.qwerty)

heat_map = la.heat_map(Layouts.qwerty)
print(heat_map)

#finger_usage = la.finger_usage(Layouts.qwerty, heat_map)
#print(finger_usage)
grades = la.grade(Layouts.qwerty, heat_map)
print(grades[1])
middle_usage = la.middle_usage(Layouts.qwerty, heat_map)
print(middle_usage)

grades = la.grade(Layouts.dvorak)
print(grades[1])
middle_usage = la.middle_usage(Layouts.dvorak)
print(middle_usage)

grades = la.grade(Layouts.colemak)
print(grades[1])
middle_usage = la.middle_usage(Layouts.colemak)
print(middle_usage)

grades = la.grade(Layouts.norman)
print(grades[1])
middle_usage = la.middle_usage(Layouts.norman)
print(middle_usage)

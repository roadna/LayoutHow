import numpy as np

qwerty = np.array([["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"],
                   ["a", "s", "d", "f", "g", "h", "j", "k", "l", ";"],
                   ["z", "x", "c", "v", "b", "n", "m", ",", ".", "/"]])

dvorak = np.array([["'", ",", ".", "p", "y", "f", "g", "c", "r", "l"],
                   ["a", "o", "e", "u", "i", "d", "h", "t", "n", "s"],
                   [";", "q", "j", "k", "x", "b", "m", "w", "v", "z"]])

colemak = np.array([["q", "w", "f", "p", "g", "j", "l", "u", "y", ";"],
                    ["a", "r", "s", "t", "d", "h", "n", "e", "i", "o"],
                    ["z", "x", "c", "v", "b", "k", "m", ".", ",", "/"]])

norman = np.array([["q", "w", "d", "f", "k", "j", "u", "r", "l", ";"],
                   ["a", "s", "e", "t", "g", "y", "n", "i", "o", "h"],
                   ["z", "x", "c", "v", "b", "p", "m", ",", ".", "/"]])

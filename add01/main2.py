import random

from conf import latex_file
from equation2 import Equation
from latex2 import Latex

list = []
for inx in range(300):
    a = random.randint(0, 15)
    b = random.randint(0, 10)    
    list = Equation(a, b).get(list)

print("Start")

random.shuffle(list)
nm_eq_per_page = 19 * 3
latex = Latex()
with open(latex_file, "w", encoding="utf-8") as f:
    for str in latex.begin_documet:
        f.write(str + "\n")
    size = len(list)
    nm_pages = size // nm_eq_per_page
    inx = 0
    for _ in range(nm_pages):
        f.write(latex.begin_tabular + "\n")
        for _ in range(nm_eq_per_page // 3):                     
            f.write(list[inx] + "&" + list[inx + 1] + "&" + list[inx + 2] + "\\\\ \n")
            inx = inx + 3
            # f.write(latex.hline + "\n")
        f.write(latex.end_tabular + "\n")
    f.write(latex.end_document + "\n")

print("End")
class Equation:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get(self, list):
        d = self.a + self.b + self.c
        list.append(f"{self.a} & + & {self.b} & + & {self.c} & = & {d} ")
        list.append(f"{self.a} & + & {self.b}                & = & {d} & - & {self.c} ")
        list.append(f"{self.a} & + & {self.b}                & = & {d} & - & {self.c} ")
        list.append(f"{self.a} & + & {self.c}                & = & {d} & - & {self.b} ")
        list.append(f"{self.a} & + & {self.c}                & = & {d} & - & {self.b} ")
        list.append(f"{self.b} & + & {self.c}                & = & {d} & - & {self.a} ")
        list.append(f"{self.b} & + & {self.c}                & = & {d} & - & {self.a} ")
        return list

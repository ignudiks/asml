class Equation:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.empty = r"\fbox{\rule{0pt}{1em}\makebox[1em]{}}  "

    def get(self, list):
        c = self.a + self.b
        list.append(f"{self.empty} & + & {self.b}     & = & {c} ")
        list.append(f"{self.a}     & + & {self.empty} & = & {c} ")
        list.append(f"{self.a}     & + & {self.b}     & = & {self.empty} ")

        list.append(f"{self.empty} &                    = & {c} & - & {self.b} ")
        list.append(f"{self.a}     &                    = & {self.empty} & - & {self.b} ")
        list.append(f"{self.a}     &                    = & {c} & - & {self.empty} ")

        list.append(f"               {self.empty} &     = & {c} & - & {self.a} ")
        list.append(f"               {self.b} &         = & {self.empty} & - & {self.a} ")
        list.append(f"               {self.b} &         = & {c} & - & {self.empty} ")



        # list.append(f"{self.a} & + & {self.b} & = & {c} ")
        # list.append(f"{self.a} &                = & {c} & - & {self.b} ")
        # list.append(f"{self.a} &                = & {c} & - & {self.b} ")
        # list.append(f"               {self.b} & = & {c} & - & {self.a} ")
        # list.append(f"               {self.b} & = & {c} & - & {self.a} ")
        return list

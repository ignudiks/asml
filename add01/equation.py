
class Equation:

    def __init__(self, a, b):
        self.a = a
        self.b = b
  

    def level1(self):
        c = self.a + self.b
        print(f"{self.a} + {self.b} = ")
        print(f"                    = {c} - {self.b}")
        print(f"                    = {c} - {self.a}")

    def level2(self):
        c = self.a + self.b
        print(f"{self.a} + {self.b} = ")
        print(f"                    = {c} - {self.b}")
        print(f"                    = {c} - {self.a}")
        

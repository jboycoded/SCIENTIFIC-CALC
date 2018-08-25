def seven(self,event = None):
    word = self.entry_Var.get() + "7"
    self.entry_Var.set(word)
def eight(self,event = None):
    word = self.entry_Var.get() + "8"
    self.entry_Var.set(word)
def nine(self,event = None):
    word = self.entry_Var.get() + "9"
    self.entry_Var.set(word)
def four(self,event = None):
    word = self.entry_Var.get() + "4"
    self.entry_Var.set(word)
def five(self,event = None):
    word = self.entry_Var.get() + "5"
    self.entry_Var.set(word)
def six(self,event = None):
    word = self.entry_Var.get() + "6"
    self.entry_Var.set(word)
def times(self,event = None):
    word = self.entry_Var.get() + "*"
    self.entry_Var.set(word)
def divide(self,event = None):
    word = self.entry_Var.get() + "/"
    self.entry_Var.set(word)
def one(self,event = None):
    word = self.entry_Var.get() + "1"
    self.entry_Var.set(word)
def two(self,event = None):
    word = self.entry_Var.get() + "2"
    self.entry_Var.set(word)
def three(self,event = None):
    word = self.entry_Var.get() + "3"
    self.entry_Var.set(word)
def plus(self,event = None):
    word = self.entry_Var.get() + "+"
    self.entry_Var.set(word)
def minus(self,event = None):
    word = self.entry_Var.get() + "-"
    self.entry_Var.set(word)
def zero(self,event = None):
    word = self.entry_Var.get() + "0"
    self.entry_Var.set(word)
def dot(self,event = None):
    word = self.entry_Var.get() + "."
    self.entry_Var.set(word)
def exponent(self,event = None):
    word = self.entry_Var.get() + "**"
    self.entry_Var.set(word)
def raised(self,arg):
    word = "("+self.entry_Var.get()+")**"+arg
    self.entry_Var.set(word)
    self.solve()
def modulus(self,event = None):
    word = self.entry_Var.get() + "/100"
    self.entry_Var.set(word)
    self.solve()
def ln(self):
    word = "math.log("+self.entry_Var.get()+")"
    self.entry_Var.set(word)
    self.solve()
def log(self):
    word = "math.log10("+self.entry_Var.get()+")"
    self.entry_Var.set(word)
    self.solve()
def sqrt(self):
    word = "math.sqrt("+self.entry_Var.get()+")"
    self.entry_Var.set(word)
    self.solve()
def sine(self):
    word = "math.sin(math.radians("+self.entry_Var.get()+"))"
    self.entry_Var.set(word)
    self.solve()
def inverse_log(self):
    word = "math.exp("+self.entry_Var.get()+")"
    self.entry_Var.set(word)
    self.solve()
def cosine(self):
    word = "math.cos(math.radians("+self.entry_Var.get()+"))"
    self.entry_Var.set(word)
    self.solve()
def tangent(self):
    word = "math.tan(math.radians("+self.entry_Var.get()+"))"
    self.entry_Var.set(word)
    self.solve()
def opened_bracket(self):
    word = self.entry_Var.get() + "("
    self.entry_Var.set(word)
def closed_bracket(self):
    word = self.entry_Var.get() + ")"
    self.entry_Var.set(word)
def arcsine(self):
    word = "math.degrees(math.asin("+self.entry_Var.get()+"))"
    self.entry_Var.set(word)
    self.solve()
def arc_cos(self):
    word = "math.degrees(math.acos("+self.entry_Var.get()+"))"
    self.entry_Var.set(word)
    self.solve()
def arctan(self):
    word = "math.degrees(math.atan("+self.entry_Var.get()+"))"
    self.entry_Var.set(word)
    self.solve()
def factorial(self):
    word = "math.factorial("+self.entry_Var.get()+")"
    self.entry_Var.set(word)
    self.solve()
def hsine(self):
    word = "math.sinh(math.radians("+self.entry_Var.get()+"))"
    self.entry_Var.set(word)
    self.solve()
def hcos(self):
    word = "math.cosh(math.radians("+self.entry_Var.get()+"))"
    self.entry_Var.set(word)
    self.solve()
def htan(self):
    word = "math.tanh(math.radians("+self.entry_Var.get()+"))"
    self.entry_Var.set(word)
    self.solve()
def pi(self):
    pie = 3.141592654
    word = self.entry_Var.get()+str(pie)
    self.entry_Var.set(word)
def cube_root(self):
    word = "("+self.entry_Var.get()+")**(1/3)"
    self.entry_Var.set(word)
    self.solve()
def arc_hsine(self):
    word = "math.degrees(math.asinh("+self.entry_Var.get()+"))"
    self.entry_Var.set(word)
    self.solve()
def arc_hcos(self):
    word = "math.degrees(math.acosh("+self.entry_Var.get()+"))"
    self.entry_Var.set(word)
    self.solve()
def arc_htan(self):
    word = "math.degrees(math.atanh("+self.entry_Var.get()+"))"
    self.entry_Var.set(word)
    self.solve()
def antilog(self):
    word = "10**("+self.entry_Var.get()+")"
    self.entry_Var.set(word)
    self.solve()
def inverse(self):
    word = "1/("+self.entry_Var.get()+")"
    self.entry_Var.set(word)
    self.solve()


def others(self):
    pass

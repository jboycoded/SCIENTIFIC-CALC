from commands import *
def binding(self):
    self.master.bind_all("7",lambda event:seven(self))
    self.master.bind_all("8",lambda event:eight(self))
    self.master.bind_all("9",lambda event:nine(self))
    self.master.bind_all("<BackSpace>",self.delete)
    self.master.bind_all("4",lambda event:four(self))
    self.master.bind_all("5",lambda event:five(self))
    self.master.bind_all("6",lambda event:six(self))
    self.master.bind_all("<asterisk>",lambda event:times(self))
    self.master.bind_all("<slash>",lambda event:divide(self))
    self.master.bind_all("1",lambda event:one(self))
    self.master.bind_all("2",lambda event:two(self))
    self.master.bind_all("3",lambda event:three(self))
    self.master.bind_all("<plus>",lambda event:plus(self))
    self.master.bind_all("<minus>",lambda event:minus(self))
    self.master.bind_all("0",lambda event:zero(self))
    self.master.bind_all("<period>",lambda event:dot(self))
    self.master.bind_all("<equal>",self.solve)
    self.master.bind_all("<enter>",self.solve)
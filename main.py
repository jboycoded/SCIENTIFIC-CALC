"""A scientific calculator made with tkinter and can run on systsems having pytohn 3.0 and above"""

__author__ = "Johnson Onoja <johnsononoja60@yahoo.com"

from tkinter import *
import math
from commands import *

class calc(Frame):
    """init method of the calc class initilises the frame and puts the window on the screen"""
    def __init__(self,master):
        Frame.__init__(self,master,bg = "blue")
        self.pack(expand = TRUE,fill = BOTH)
        self.top = None
        
        self.master = master
        self.master.title("Sci-Calc")
        self.master.maxsize(300,300)
        self.master.minsize(350,360)

        #positions the app at the center of the screen.
        w = 250; h = 250
        x = (self.master.winfo_screenwidth()-w)/2
        y = (self.master.winfo_screenheight()-h)/2
        self.master.geometry("%dx%d+%d+%d" %(w,h,x,y))

        self.labels()
        self.entry_Var = StringVar()
        self.entry = Label(self,bg = "pink",fg = "blue",width = 46,relief=SUNKEN,anchor="w",
                           borderwidth = 5,state = NORMAL,textvariable = self.entry_Var)
        self.entry.grid(row = 1,pady = 5,padx = 5,columnspan = 5)
        
        self.commands()
        self.start()
        self.bindings()

    def bindings(self):
        #bindings for all neccessary on-screen buttons.
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
        self.master.bind_all("<Return>",self.solve)
        self.master.bind_all("<parenleft>",lambda event:opened_bracket(self))
        self.master.bind_all("<parenright>",lambda event:closed_bracket(self))
        
    def other_binding(self,event):
        if self.entry_Var.get() == "Error.":
            self.entry_Var.set("")
        #if self.shift_label.cget("state")=="normal":
            #self.shift_label["state"] = "disabled"

    def labels(self):
        self.shift_label = Label(self,bg = "blue",text = "shift",disabledforeground = "blue",state = DISABLED)
        self.shift_label.grid(sticky = S)
        
        self.deg_label = Label(self,bg = "blue",text = "deg",disabledforeground = "blue")
        self.deg_label.grid(sticky = S,row = 0,column = 1)

        self.rad_label = Label(self,bg = "blue",text = "rad",state = DISABLED,disabledforeground = "blue")
        self.rad_label.grid(row = 0,column = 2,sticky = S)
        
        self.grad_label = Label(self,bg = "blue",text = "grad",disabledforeground = "blue",state = DISABLED)
        self.grad_label.grid(row = 0,column = 3,sticky = S)

        self.current_switch = self.deg_label

    def drg(self,event = None):
        if self.current_switch == self.deg_label:
            self.current_switch = self.rad_label
            self.deg_label["state"] = "disabled"
            self.rad_label["state"] = "normal"
        elif self.current_switch == self.rad_label:
            self.current_switch = self.grad_label
            self.rad_label["state"] = "disabled"
            self.grad_label["state"] = "normal"
        else:
            self.current_switch = self.deg_label
            self.grad_label["state"] = "disabled"
            self.deg_label["state"] = "normal"

    def commands(self):
        shift = self.shift_label
        
        self.command_list = [None,lambda:shift.config(state="normal" if shift.cget("state")=="disabled" else "disabled"),
                             self.drg,lambda:inverse_log(self),lambda:ln(self),lambda:log(self),self.constants,lambda:sqrt(self),
                             lambda:sine(self),lambda:cosine(self),lambda:tangent(self),lambda:opened_bracket(self),
                             lambda:closed_bracket(self),lambda:arcsine(self),lambda:arc_cos(self),lambda:arctan(self),
                             lambda:modulus(self),lambda:factorial(self),lambda:hsine(self),lambda:hcos(self),lambda:htan(self),
                             lambda:pi(self),lambda:cube_root(self),lambda:arc_hsine(self),lambda:arc_hcos(self),lambda:arc_htan,
                             lambda:raised(self,"3"),lambda:raised(self,"2"),lambda:exponent(self),lambda:antilog(self),
                             lambda:inverse(self)]
        
        self.other = [None,lambda:seven(self),lambda:eight(self),lambda:nine(self),self.delete,lambda:self.entry_Var.set(""),
                      lambda:four(self),lambda:five(self),lambda:six(self),lambda:times(self),lambda:divide(self),lambda:one(self),
                      lambda:two(self),lambda:three(self),lambda:plus(self),lambda:minus(self),lambda:zero(self),None,
                      lambda:dot(self),None,self.solve]
        
    def delete(self,event = None):
        word = self.entry_Var.get()
        if word:
            word = list(word)
            del word[-1]
            word = "".join(word)
            self.entry_Var.set(word)

    def solve(self,event = None):
        def process_float(ans):
            check = str(ans)
            index = check.index(".")+1
            if (len(check)-index)>5:
                ans = "{:.5f}".format(ans)
                ans = float(ans)
            return ans
        
        word = self.entry_Var.get()
        if word:
            try:
                ans = eval(word)
                if isinstance(ans,float):
                    ans = process_float(ans)
                self.entry_Var.set(ans)
            except BaseException as e:
                self.entry_Var.set("Error.")
            
    def start(self):
        texts = [None,"SHIFT","DRG","e^x","ln","log","CONST","sqrt","sin","cos","tan","(",")","asin",
                 "acos","atan","%","n!","sinh","cosh","tanh","pi","cube-rt","asinh","acosh","atanh",
                 "x^3","x^2","y^x","10^x","1/x"]
        row = 2
        column = 0
        for i in range(1,30+1):
            self.make_buttons(texts[i],row,column,self.command_list[i],6)
            column += 1
            if i%5 == 0:
                column = 0
                row += 1
              
        other_texts = [None,"7","8","9","DEL","AC","4","5","6","*","/","1","2","3","+","-",
                       "0","+/-",".","EXP","="]
        row += 1
        column = 0
        for i in range(1,20+1):
            self.make_buttons(other_texts[i],row,column,self.other[i],6)
            column += 1
            if i%5 == 0:
                column = 0
                row += 1

    def constants_main(self,x,y):
        if self.top:
            self.top.destroy()
        self.top = Toplevel(self,bg = "black")
        self.top.transient(self)
        
        #grabs windows focus so any activity on the screen will be directed
        #to the current screen/Toplevel widget
        self.top.grab_set()
        
        self.top.title("Constants")
        self.top.maxsize(x,y)
        self.top.minsize(x,y)

        #aligns the Toplevel widget geometry to the centre of the screen.
        w = 250; h = 250
        x = (self.top.winfo_screenwidth()-w)/2
        y = (self.top.winfo_screenheight()-h)/2
        self.top.geometry("%dx%d+%d+%d" %(w,h,x,y))

    def constants(self):
        #menu for classification of constants.
        self.constants_main(150,120)
        texts = [None,"Universal","Electromagnetic","Atomic & Nuclear","Physico-Chemical","Others"]
        commands = [None,self.universal_constants,self.em_constants,self.atomic_constants,self.physics_constants,self.other_constants]

        self.constants_list = {"universal":[None,"3*10**(8)","6.67408*10**(-11)","6.626*10**(-34)","1.05457*10**(-34)"],
                               "em":[None,"1.256637*10**(-6)","8.8541878*10**(-12)","1.602*10**(-19)","7.748*10**(-5)","2.0678*10**(-15)"],
                               "atomic":[None,"9.10938*10**(-31)","1.6726*10**(-27)","10973731.57","5.29177*10**(-11)","2.81794*10**(-15)"],
                               "physics":[],
                               "other":"9.80"}
        for i in range(1,6):
            Label(self.top,text=str(i),bg="black",fg="blue").grid()
        for i in range(1,6):
            self.make_constants(texts[i],i-1,commands[i])
        self.master.wait_window(self.top)

    def universal_constants(self):
        self.constants_main(150,120)
        texts = [None,"Speed of light","Gravitational Constant","Planck Constant","Reduced Planck Constant"]
        labels = [None,"c","G","h","h"]
        commands = [None,lambda:self.display_constant("universal",1),lambda:self.display_constant("universal",2),
                    lambda:self.display_constant("universal",3),lambda:self.display_constant("universal",4)]

        for i in range(1,5):
            Label(self.top,text = labels[i],bg = "black",fg = "blue",anchor = "w").grid()
        for i in range(1,5):
            self.make_constants(texts[i],i-1,commands[i])
        Button(self.top,text = "Back",fg="white",bg="red",width=18,command=self.constants,
               anchor="center").grid(row=4,column=1)

    def em_constants(self):
        self.constants_main(150,150)
        texts = [None,"Magnetic Constant","Electric Constant","Elementary Charge","Conductance Quantum","Magnetic Flux Quantum"]
        labels = [None,"m","E","e","cq","mf"]
        commands = [None,lambda:self.display_constant("em",1),lambda:self.display_constant("em",2),
                    lambda:self.display_constant("em",3),lambda:self.display_constant("em",4),
                    lambda:self.display_constant("em",5)]

        for i in range(1,6):
            Label(self.top,text = labels[i],bg = "black",fg = "blue",anchor = "w").grid()
        for i in range(1,6):
            self.make_constants(texts[i],i-1,commands[i])
        Button(self.top,text = "Back",fg="white",bg="red",width=18,command=self.constants,
               anchor="center").grid(row=5,column=1)

    def atomic_constants(self):
        self.constants_main(150,150)
        texts = [None,"Electron Mass","Proton Mass","Rydberg Constant","Bohr Radius","Electron Radius"]
        labels = [None,"Mp","Me","R","a","Re"]
        commands = [None,lambda:self.display_constant("atomic",1),lambda:self.display_constant("atomic",2),
                    lambda:self.display_constant("atomic",3),lambda:self.display_constant("atomic",4),
                    lambda:self.display_constant("atomic",5)]

        for i in range(1,6):
            Label(self.top,text = labels[i],bg = "black",fg = "blue",anchor = "w").grid()
        for i in range(1,6):
            self.make_constants(texts[i],i-1,commands[i])#lambda:self.display_constant("atomic",n))
        Button(self.top,text = "Back",fg="white",bg="red",width=18,command=self.constants,
               anchor="center").grid(row=5,column=1)

    def physics_constants(self):
        self.constants_main(170,200)
        texts = [None,"Atomic Mass Unit","Avogadro Constant","Faraday Constant","Molar Gas Constant","Boltzmann Constant",
                 "Stefan-Boltzmann Constant","Electron Volt"]
        labels = [None,"u","Na","F","R","k","sg","eV"]
        commands = [None,None]

        for i in range(1,8):
            Label(self.top,text = labels[i],bg = "black",fg = "blue",anchor = "w").grid()
        for i in range(1,8):
            self.make_constants(texts[i],i-1,commands[1])
        Button(self.top,text = "Back",fg="white",bg="red",width=18,command=self.constants,
               anchor="center").grid(row=8,column=1)

    def other_constants(self):
        self.constants_main(50,50)
        Label(self.top,text = "g",bg = "black",fg = "blue").grid()
        Button(self.top,text = "gravity",fg = "white",bg = "black",width = 19,borderwidth=0,anchor="w",
               command=lambda:self.display_constant("other",None)).grid(row=0,column=1)
        Button(self.top,text = "Back",fg="white",bg="red",width=18,command=self.constants,
               anchor="center").grid(row=1,column=1)

    def display_constant(self,arg,i):
        if arg=="other":
               word = self.entry_Var.get()+self.constants_list[arg]
        else:
            word = self.entry_Var.get()+self.constants_list[arg][i]
        self.entry_Var.set(word)
        self.top.destroy()

    def make_constants(self,text,row,command):
        Button(self.top,text = text,fg = "white",bg = "black",width = 19,borderwidth=0,anchor="w",
               command=command).grid(row=row,column=1)
    
    def make_buttons(self,text,row,column,command,width):
        button = Button(self,text = text,command = command,width = width,relief = RAISED,borderwidth = 2,
                        bg = "black",fg = "white")
        button.grid(row = row,column = column,pady = 2,sticky=N+S+E+W)
        button.bind("<Button-3>",self.other_binding)
        button.bind("<Button-1>",self.other_binding)

if __name__ == "__main__":
    master=Tk()
    calc(master)
    master.mainloop()

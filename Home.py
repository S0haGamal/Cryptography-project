import tkinter as tk
import tkinter.font as tkFont
class homeApp:
    def __init__(self, root):
        root.title("Main Form")
        width=755
        height=576
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        self.root = root
      

        GButton_749=tk.Button(root)
        GButton_749["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=38)
        GButton_749["font"] = ft
        GButton_749["fg"] = "#89ABE3"
        GButton_749["justify"] = "center"
        GButton_749["text"] = "ROT13"
        GButton_749.place(x=40,y=460,width=155,height=45)
        GButton_749["command"] = self.open_ro_app
        
        GButton_769=tk.Button(root)
        GButton_769["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=38)
        GButton_769["font"] = ft
        GButton_769["fg"] = "#89ABE3"
        GButton_769["justify"] = "center"
        GButton_769["text"] = "Subsitution"
        GButton_769.place(x=450,y=460,width=250,height=50)
        GButton_769["command"] =self.open_su_app

        GButton_769=tk.Button(root)
        GButton_769["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=38)
        GButton_769["font"] = ft
        GButton_769["fg"] = "#89ABE3"
        GButton_769["justify"] = "center"
        GButton_769["text"] = "VIGENERE"
        GButton_769.place(x=380,y=280,width=260,height=50)
        GButton_769["command"] =self.open_vi_app
        

        GButton_610=tk.Button(root)
        GButton_610["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=38)
        GButton_610["font"] = ft
        GButton_610["fg"] = "#89ABE3"
        GButton_610["justify"] = "center"
        GButton_610["text"] = "casear"
        GButton_610.place(x=40,y=280,width=155,height=50)
        GButton_610["command"] = self.open_ca_app

        GLabel_502=tk.Label(root)
        ft = tkFont.Font(family='Times',size=58)
        GLabel_502["font"] = ft
        GLabel_502["fg"] = "#c71585"
        GLabel_502["justify"] = "center"
        GLabel_502["text"] = ""
        GLabel_502.place(x=250,y=140,width=451,height=30)

        GLabel_917=tk.Label(root)
        GLabel_917["anchor"] = "s"
        GLabel_917["disabledforeground"] = "#ffb800"
        ft = tkFont.Font(family='Times',size=58)
        GLabel_917["font"] = ft
        GLabel_917["fg"] = "#EA738D"
        GLabel_917["justify"] = "center"
        GLabel_917["text"] = "Crptography"
        GLabel_917["relief"] = "raised"
        GLabel_917.place(x=30,y=90,width=521,height=76)

        GLineEdit_475=tk.Entry(root)
        GLineEdit_475["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_475["font"] = ft
        GLineEdit_475["fg"] = "#333333"
        GLineEdit_475["justify"] = "center"
        GLineEdit_475["text"] = "Entry"
        GLineEdit_475.place(x=820,y=220,width=70,height=25)
        

    def GButton_749_command(self):
          from Rot13_f import ro
          root = tk.Tk()
          app = ro(root)
          root.mainloop()


    def GButton_769_command(self):
         from Vignere_f import vi
         root = tk.Tk()
         app = vi(root)
         root.mainloop()


    def GButton_610_command(self):
        from caesar_f import ca
        root = tk.Tk()
        app = ca(root)
        root.mainloop()
        
    def GButton_61_command(self):
        from sub_f import su
        root = tk.Tk()
        app = su(root)
        root.mainloop()
        
    def open_ro_app(self):
        from Rot13_f import ro
        self.root.withdraw()  
        self.new_window = tk.Toplevel(self.root)
        app = ro(self.new_window)
        
    def open_vi_app(self):
        from Vignere_f import vi
        self.root.withdraw()  
        self.new_window = tk.Toplevel(self.root)
        app = vi(self.new_window)

    def open_ca_app(self):
        from caesar_f import ca
        self.root.withdraw() 
        self.new_window = tk.Toplevel(self.root)
        app = ca(self.new_window)
    
    def open_su_app(self):
        from sub_f import su
        self.root.withdraw()  
        self.new_window = tk.Toplevel(self.root)
        app = su(self.new_window)
    
    

if __name__ == "__main__":
    root = tk.Tk()
    app = homeApp(root)
    root.mainloop()

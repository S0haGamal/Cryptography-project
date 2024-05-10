import tkinter as tk
import tkinter.font as tkFont
import Rot13
from tkinter import filedialog



class ro:
    message=''
    def __init__(self, root):
        root.title("Rot13")
        width=933
        height=589
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        self.root = root
        GLabel_674=tk.Label(root)
        ft = tkFont.Font(family='Times',size=28)
        GLabel_674["font"] = ft
        GLabel_674["fg"] = "#ea738d"
        GLabel_674["justify"] = "center"
        GLabel_674["text"] = "Enter The Message For Encryption: "
        GLabel_674.place(x=160,y=160,width=532,height=38)

        GLabel_988=tk.Label(root)
        ft = tkFont.Font(family='Times',size=43)
        GLabel_988["font"] = ft
        GLabel_988["fg"] = "#ea738d"
        GLabel_988["justify"] = "center"
        GLabel_988["text"] = "Rot13 Cipher"
        GLabel_988.place(x=100,y=10,width=726,height=61)

        GLineEdit_843=tk.Entry(root)
        GLineEdit_843["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_843["font"] = ft
        GLineEdit_843["fg"] = "#333333"
        GLineEdit_843["justify"] = "center"
        GLineEdit_843["text"] = "Entry"
        GLineEdit_843.place(x=170,y=210,width=497,height=272)

        GMessage_815=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_815["font"] = ft
        GMessage_815["fg"] = "#333333"
        GMessage_815["justify"] = "center"
        GMessage_815["text"] = "Message"
        GMessage_815.place(x=940,y=150,width=30,height=30)

        GButton_156=tk.Button(root)
        GButton_156["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=23)
        GButton_156["font"] = ft
        GButton_156["fg"] = "#89abe3"
        GButton_156["justify"] = "center"
        GButton_156["text"] = "Encrypt"
        GButton_156.place(x=240,y=530,width=112,height=30)
        GButton_156["command"] = self.GButton_156_command
        GButton_156["command"] = lambda :  encrypt(GLineEdit_843.get())
        
        GButton_156=tk.Button(root)
        GButton_156["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=23)
        GButton_156["font"] = ft
        GButton_156["fg"] = "#89abe3"
        GButton_156["justify"] = "center"
        GButton_156["text"] = "Decrypt"
        GButton_156.place(x=40,y=530,width=112,height=30)
        GButton_156["command"] = self.GButton_156_command
        GButton_156["command"] = lambda :  decrypt(GLineEdit_843.get())

        GButton_849=tk.Button(root)
        GButton_849["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=23)
        GButton_849["font"] = ft
        GButton_849["fg"] = "#89abe3"
        GButton_849["justify"] = "center"
        GButton_849["text"] = "Upload File"
        GButton_849.place(x=480,y=530,width=156,height=30)
        GButton_849["command"] = self.GButton_849_command
        GButton_849["command"] = lambda: upload(GLineEdit_843.get())
        

        GButton_287=tk.Button(root)
        GButton_287["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=23)
        GButton_287["font"] = ft
        GButton_287["fg"] = "#89abe3"
        GButton_287["justify"] = "center"
        GButton_287["text"] = "Back"
        GButton_287.place(x=10,y=20,width=105,height=30)
        GButton_287["command"] = self.back_to_home

    def GButton_156_command(self):
        print("command")


    def GButton_849_command(self):
        print("command")


    def GButton_287_command(self):
         from Home import homeApp
         root = tk.Tk()
         app = homeApp(root)
         root.mainloop()
    def back_to_home(self):
        from Home import homeApp
        self.root.withdraw()  # Hide the current window
        self.new_window = tk.Toplevel(self.root)
        app = homeApp(self.new_window)    

def download(contant):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    with open(file_path, 'w') as file:
          file.write(contant) 


        
def encrypt(msg):
        pltxt=Rot13.Rot13_encryption(msg)
        calculation_window = tk.Toplevel()
        calculation_window.title("Decryption Result")
        label = tk.Label(calculation_window, width=70, height=30, bg="white", text=f"{pltxt}")
        result_label3 = tk.Button(calculation_window, font=10, width=12, height=2, text="DownLoad", command=lambda: download(label.cget("text")))
        label.pack()
        result_label3.pack()
        
def decrypt(msg):
        pltxt=Rot13.Rot13_decryption(msg)
        calculation_window = tk.Toplevel()
        calculation_window.title("Decryption Result")
        label = tk.Label(calculation_window, width=70, height=30, bg="white", text=f"{pltxt}")
        result_label3 = tk.Button(calculation_window, font=10, width=12, height=2, text="DownLoad", command=lambda: download(label.cget("text")))
        label.pack()
        result_label3.pack()
        
        
def upload(content):
    file_path = filedialog.askopenfilename()
    with open(file_path, 'r') as file:
        content = file.read()
        calculation_window = tk.Toplevel()
        calculation_window.title("Perform Calculation")
        label = tk.Label(calculation_window, width=70, height=20, bg="white", text=f"{content}")
        label.pack()
        
        def encrypt_content():
            encrypt(content)
        
        
        def decrypt_content():
            decrypt(content)
            
        
        result_label1 = tk.Button(calculation_window, font=10, width=12, height=2, text="Encryption", command=encrypt_content)
        result_label2 = tk.Button(calculation_window, font=10, width=12, height=2, text="Decryption" , command=decrypt_content)
        result_label1.pack()
        result_label2.pack()
    
    


if __name__ == "__main__":
    root = tk.Tk()
    app = ro(root)
    root.mainloop()

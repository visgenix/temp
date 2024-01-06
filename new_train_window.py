import tkinter as tk
from tkinter import ttk
from tkinter import *
import customtkinter as ctk
from Capture_Image import takeImages
from training import training
from new_del_operation import delete_data

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def show_train_window():
    rootT = ctk.CTk()
    rootT.geometry("480x320")
    rootT.title('Training')
    rootT.attributes('-fullscreen', True)

    nm = StringVar(rootT)
    rn = StringVar(rootT)
    
    title = ctk.CTkLabel(rootT, text='Training Details', font=('Helvetica', 16, 'bold'))
    title.place(x=170, y=20)
    
    nameInstr = ctk.CTkLabel(rootT, text='Name :', font=('Helvetica', 14))
    nameInstr.place(x=10, y=70)
    #name = ctk.CTkEntry(rootT, width=250, textvariable=nm, font=('Ubuntu', 16))
    #name.place(x=120, y=70)
    
    rnoInstr = ctk.CTkLabel(rootT, text='ID :', font=('Helvetica', 14))
    rnoInstr.place(x=10, y=120)
    rno = ctk.CTkEntry(rootT, width=90, textvariable=rn, font=('Ubuntu', 16))
    rno.place(x=120, y=120)
    with open('D:\Projects\FAR_device\mainblock2\Departments.txt', 'r') as f:
        departments = f.read().split(',')
    dept = ttk.Combobox(rootT, width=15, height=5, values=departments)
    dept.current([0])
    dept.place(x=250, y=120)

    def check_boxes():
        name=combo_box.get()
        if(rn.get()==""):
            label.configure(text="Enter the  ID ")
            return 1
        if(name==""):
            label.configure(text="Enter the  Name ")
            return 1
        return 0




    def check_exist():
        name=combo_box.get()
        if name in lst:
            c=check_boxes()
            print("This is C1:",c)
            if c!=1:
                delete_data(name,rn.get())
                call_image_capture()
        else:
            c=check_boxes()
            print("This is C2:",c)
            if c!=1:
                call_image_capture()


    def call_image_capture():
        takeImages('_'.join([nm.get(),  dept.get(), rn.get()]))
        training()

    trainBtn1 = ctk.CTkButton(rootT, text='Train', font=('Ubuntu', 14), width=200, height=40, command=check_exist)
    trainBtn1.place(x=145, y=180)

    def back_to_menu():
        rootT.destroy()

    cancelBtn = ctk.CTkButton(rootT, text='Cancel', font=('Ubuntu', 14), fg_color='#EB455F', width=200, height=35, command=back_to_menu)
    cancelBtn.place(x=145, y=240)

    def check_input(event):
        value = event.widget.get()
        if value == '':
            combo_box['values'] = lst
        else:
            data = []
            for item in lst:
                if value.lower() in item.lower():
                    data.append(item)
            combo_box['values'] = data

    with open('staff_name.csv', 'r') as f:
        lst = f.read().split('\n')

            
    combo_box = ttk.Combobox(rootT,width=30, height=5)
    combo_box['values'] = lst
    combo_box.bind('<KeyRelease>', check_input)
    combo_box.place(x=150, y=70)

    label = ctk.CTkLabel(rootT, text="Count/Delete", font=("Helvetica", 16))
    label.place(x=80, y=280)

    rootT.mainloop()

show_train_window()    





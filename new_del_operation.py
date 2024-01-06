import tkinter as tk
from tkinter import *
import customtkinter as ctk
from tkinter import ttk
from PIL import Image, ImageTk
import pickle
import regex as re 

def del_id(s_name,s_id):
    x = pickle.load(open("D:/Projects/FAR_device/model/X.sav", "rb"))
    y = pickle.load(open("D:/Projects/FAR_device/model/Y.sav", "rb"))
    count=0
    for id in y:
        if re.search(s_id, str(id)):
            count+=1
            start = y.index(id)
    if(count<110):
        end = start+count+1
        del x[start:end]
        del y[start:end]
        print("Deleted")
        count=0
        for id in y:
            if re.search(s_id, str(id)):
                count+=1
                print("Index: ",y.index(id))
        print("Count: ",count," ID: ",s_id)
        pickle.dump(x,open("D:/Projects/FAR_device/model/X.sav", "wb"))
        pickle.dump(y,open("D:/Projects/FAR_device/model/Y.sav", "wb"))
    else:
        del_name(s_name)

def del_name(s_name):
    x = pickle.load(open("D:/Projects/FAR_device/model/X.sav", "rb"))
    y = pickle.load(open("D:/Projects/FAR_device/model/Y.sav", "rb"))
    count=0
    for id in y:
        if re.search(s_name, str(id)):
            count+=1
            start = y.index(id)
    end = start+count+1
    del x[start:end]
    del y[start:end]
    print("Deleted")
    count=0
    for id in y:
        if re.search(s_name, str(id)):
            count+=1
            print("Index: ",y.index(id))
    print("Count: ",count," NAME: ",s_name)
    pickle.dump(x,open("D:/Projects/FAR_device/model/X.sav", "wb"))
    pickle.dump(y,open("D:/Projects/FAR_device/model/Y.sav", "wb"))



def delete_data(name,id_no):
    del_id(name,id_no)
    
    




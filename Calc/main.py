# -*- coding: utf-8 -*-

#kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.button import Label

#KivyMD
import Toolbar kivymd.toolbar.Toolbar
import ThemeManager kivymd.theming.ThemeManager

#Reg
import numpy as np
import matplotlib.pyplot as plt 




class mainApp(App):
    
    def build(self):
        return Label(text="hello")


kv = mainApp()
kv.run()

mode = ""

def graph(formula):  
    x = np.array(range(-10,11))  
    y = eval(bytes([ord(z) for z in formula]))
   
    plt.plot(x, y)  
    plt.show()

def standard():
    print("Currently in Standard Mode.")
    print("Press 'Q' to quit")
    print("Press 'G' for graphing mode")
    userIn = ""
    while userIn != "q":
        try:
            userIn = input("Input: ")
            print(eval(userIn)) 
        except NameError:
            if userIn == "Q" or userIn == "q":
                mode = "q"
                SystemExit
            elif userIn == "g" or userIn == "G":
                print("switched to Graphing mode")
                mode = "2"
                graphing()
            else: 
                print("Invalid Input")
        except ZeroDivisionError:
            print("Cannot Divide by Zero")
        except SyntaxError:
            print("Invalid Input")
 

def graphing():
    print("Currently in Graphing Mode.")
    print("Press 'Q' to quit.")
    print("Press 'S' for standard mode.")
    print("Press 'W' to alter the window settings.")
    userIn = ""

    while userIn != "q":
        try:
            userIn = input("Function: f(x) =  ")
            graph(userIn)
        except ZeroDivisionError:
            print("Cannot Divide by Zero")
        except:
            print("Invalid Input")

standard()
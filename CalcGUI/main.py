import kivy
import kivymd

from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.config import Config

Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '370')
Config.set('graphics', 'height', '400')

#KivyMD
from kivymd.bottomsheet import MDListBottomSheet, MDGridBottomSheet
from kivymd.button import MDIconButton
from kivymd.date_picker import MDDatePicker
from kivymd.dialog import MDDialog
from kivymd.label import MDLabel
from kivymd.list import ILeftBody, ILeftBodyTouch, IRightBodyTouch, BaseListItem
from kivymd.material_resources import DEVICE_TYPE
from kivymd.navigationdrawer import MDNavigationDrawer, NavigationDrawerHeaderBase
from kivymd.selectioncontrols import MDCheckbox
from kivymd.snackbar import Snackbar
from kivymd.theming import ThemeManager
from kivymd.time_picker import MDTimePicker

#Reg
import numpy as np
import matplotlib.pyplot as plt 




class Calculator(GridLayout):
    mode = ""
    def standard(self, equation):
        print(self.mode)
        try:
            self.display.text = str(eval(equation))
        except:
            self.display.text = "Error"

    def graphing(self, formula):
        try:
            x = np.array(range(-10,11))  
            y = eval(bytes([ord(z) for z in formula]))
   
            plt.plot(x, y)  
            plt.show()
        except:
            self.display.text = "Error"
class CalcApp(App):
    theme_cls = ThemeManager()
    title = "Calculator"
    mode = ""
    def build(self):
        return Calculator()


if __name__ == '__main__':
    CalcApp().run()
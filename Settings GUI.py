# -*- coding: utf8 -*-

import remi.gui as gui
from remi.gui import *
from remi import start, App
import DBConnection as db
import datetime
import Notify as mail


#written 2018 by Christian Kueken, Germany 

#Example for App with menu and content Area with switchable content
#written with remI Library


#    +-----self.baseContainer-----------------------------------+
#    |                                                          +
#    | +--menuContainer--+  +--contentContainer---------------+ |
#    | |                 |  |                                 | |
#    | | btnscreen1      |  | +--self.screen1/self.screen2--+ | |
#    | | btnscreen2      |  | | changing content defined    | | |
#    | |                 |  | | in separate classes         | | |
#    | |                 |  | +-----------------------------+ | |
#    | +-----------------+  +---------------------------------+ |
#    +----------------------------------------------------------+
#

#class definitions for the content. These classes could also be put into separate
#files like "screen1.py" and be imported into the main app. If the App is very
#sophisticated this could clean up the code a little

#class definition for content "screen1" (inherits from remi.gui.Widget)
#these definitions are made with the remI Editor
#we just pick the definitions from the constructUI Method and put it into an __init__ method

class screen1Widget(Widget):
    def __init__(self,**kwargs):
        super(screen1Widget,self).__init__(**kwargs)
        self.style['position'] = "absolute"
        self.style['overflow'] = "auto"
        self.style['background-color'] = "#ffff80"
        self.style['left'] = "10px"
        self.style['top'] = "10px"
        self.style['margin'] = "0px"
        self.style['width'] = "427px"
        self.style['display'] = "block"
        self.style['height'] = "480px"
        #Create the save relay 1 button
        btnSave1 = Button('Save')
        #btnSave1.style['position'] = "absolute"
        btnSave1.style['overflow'] = "auto"
        btnSave1.style['left'] = "10px"
        btnSave1.style['top'] = "10px"
        btnSave1.style['margin'] = "5px"
        btnSave1.style['width'] = "150px"
        btnSave1.style['display'] = "block"
        btnSave1.style['height'] = "20px"
        #Create the save relay 2 button
        btnSave2 = Button('Save')
        #btnSave2.style['position'] = "absolute"
        btnSave2.style['overflow'] = "auto"
        btnSave2.style['left'] = "10px"
        btnSave2.style['top'] = "10px"
        btnSave2.style['margin'] = "5px"
        btnSave2.style['width'] = "150px"
        btnSave2.style['display'] = "block"
        btnSave2.style['height'] = "20px"
        #Create Settings tag
        settingslabel = Label("Settings")
        relay1result = Label("")
        relay2result = Label("")
        #Create the start labels
        relay1startlabel = Label("Relay 1 start time: (HH:MM:SS)")
        relay2startlabel = Label("Relay 2 start time: (HH:MM:SS)")
        #Create the finish labels
        relay1finishlabel = Label("Relay 1 finish time: (HH:MM:SS)")
        relay2finishlabel = Label("Relay 2 finish time: (HH:MM:SS)")
        #Create the start inputs
        relay1startinput = TextInput(single_line=True,hint="HH:MM:SS, 24hr format.")
        relay2startinput = TextInput(single_line=True,hint="HH:MM:SS, 24hr format.")
        #Create the finish inputs
        relay1finishinput = TextInput(single_line=True,hint="HH:MM:SS, 24hr format.")
        relay2finishinput = TextInput(single_line=True,hint="HH:MM:SS, 24hr format.")

        
        #Agrego el label Settings
        self.append(settingslabel,'settingslabel')

        #Agrego el label y input de relay1
        self.append(relay1startlabel, 'relay1startlabel')
        self.append(relay1startinput,'relay1startinput')
        #Agrego el label y input de relay1
        self.append(relay1finishlabel, 'relay1finishlabel')
        self.append(relay1finishinput,'relay1finishinput')
        self.append(btnSave1, 'btnSave1')
        self.append(relay1result, 'relay1result')
        

        #Agrego el label y input de relay2
        self.append(relay2startlabel, 'relay2startlabel')
        self.append(relay2startinput,'relay2startinput')
        #Agrego el label y input de relay2
        self.append(relay2finishlabel, 'relay2finishlabel')
        self.append(relay2finishinput,'relay2finishinput')
        self.append(btnSave2, 'btnSave2')
        self.append(relay2result, 'relay2result')
        
#class definition for content "screen2" (inherits from remi.gui.Widget)


#Acá insertar la matriz de datos.
class screen2Widget(Widget):
    def __init__(self,**kwargs):
        super(screen2Widget,self).__init__(**kwargs)
        self.style['position'] = "absolute"
        self.style['overflow'] = "auto"
        self.style['background-color'] = "#ffff80"
        self.style['left'] = "10px"
        self.style['top'] = "10px"
        self.style['margin'] = "0px"
        self.style['width'] = "427px"
        self.style['display'] = "block"
        self.style['height'] = "480px"
        testlabel = Label("This is Screen 2!")
        mytextbox = TextInput(single_line=True,hint="Write something to be send to screen 1")
        btnsend = Button("Send Text Input to Screen 1")
        self.append(testlabel,'testlabel')
        self.append(mytextbox,'mytextbox')
        self.append(btnsend,'btnsend')


#class definition for the App

class multiscreen(App):
    def __init__(self, *args, **kwargs):
        if not 'editing_mode' in kwargs.keys():
            super(multiscreen, self).__init__(*args)

    def idle(self):
        #idle function called every update cycle
        pass
    
    def main(self):
        
        #The root Container
        baseContainer = Widget()
        baseContainer.attributes['class'] = "Widget"
        baseContainer.attributes['editor_baseclass'] = "Widget"
        baseContainer.attributes['editor_varname'] = "baseContainer"
        baseContainer.attributes['editor_tag_type'] = "widget"
        baseContainer.attributes['editor_newclass'] = "False"
        baseContainer.attributes['editor_constructor'] = "()"
        baseContainer.style['position'] = "absolute"
        baseContainer.style['overflow'] = "auto"
        baseContainer.style['left'] = "100px"
        baseContainer.style['top'] = "120px"
        baseContainer.style['margin'] = "0px"
        baseContainer.style['border-style'] = "solid"
        baseContainer.style['width'] = "670px"
        baseContainer.style['display'] = "block"
        baseContainer.style['border-width'] = "1px"
        baseContainer.style['height'] = "550px"
        
        #The menuContainer on the left side
        menuContainer = Widget()
        menuContainer.attributes['class'] = "Widget"
        menuContainer.attributes['editor_baseclass'] = "Widget"
        menuContainer.attributes['editor_varname'] = "menuContainer"
        menuContainer.attributes['editor_tag_type'] = "widget"
        menuContainer.attributes['editor_newclass'] = "False"
        menuContainer.attributes['editor_constructor'] = "()"
        menuContainer.style['position'] = "absolute"
        menuContainer.style['overflow'] = "auto"
        menuContainer.style['left'] = "10px"
        menuContainer.style['top'] = "10px"
        menuContainer.style['margin'] = "0px"
        menuContainer.style['border-style'] = "solid"
        menuContainer.style['width'] = "180px"
        menuContainer.style['display'] = "block"
        menuContainer.style['border-width'] = "1px"
        menuContainer.style['height'] = "500px"
        btnScreen2 = Button('View')
        btnScreen2.attributes['class'] = "Button"
        btnScreen2.attributes['editor_baseclass'] = "Button"
        btnScreen2.attributes['editor_varname'] = "btnScreen2"
        btnScreen2.attributes['editor_tag_type'] = "widget"
        btnScreen2.attributes['editor_newclass'] = "False"
        btnScreen2.attributes['editor_constructor'] = "('Screen 2')"
        btnScreen2.style['position'] = "absolute"
        btnScreen2.style['overflow'] = "auto"
        btnScreen2.style['left'] = "5px"
        btnScreen2.style['top'] = "60px"
        btnScreen2.style['margin'] = "0px"
        btnScreen2.style['width'] = "150px"
        btnScreen2.style['display'] = "block"
        btnScreen2.style['height'] = "30px"
        #menuContainer.append(btnScreen2,'btnScreen2')
        btnScreen1 = Button('Settings')
        btnScreen1.attributes['class'] = "Button"
        btnScreen1.attributes['editor_baseclass'] = "Button"
        btnScreen1.attributes['editor_varname'] = "btnScreen1"
        btnScreen1.attributes['editor_tag_type'] = "widget"
        btnScreen1.attributes['editor_newclass'] = "False"
        btnScreen1.attributes['editor_constructor'] = "('Screen 1')"
        btnScreen1.style['position'] = "absolute"
        btnScreen1.style['overflow'] = "auto"
        btnScreen1.style['left'] = "5px"
        btnScreen1.style['top'] = "10px"
        btnScreen1.style['margin'] = "0px"
        btnScreen1.style['width'] = "150px"
        btnScreen1.style['display'] = "block"
        btnScreen1.style['height'] = "30px"
        menuContainer.append(btnScreen1,'btnScreen1')
        
        #Add the menuContainer to the baseContainer and define the listeners for the menu elements
        baseContainer.append(menuContainer,'menuContainer')
        #baseContainer.children['menuContainer'].children['btnScreen2'].set_on_click_listener(self.onclick_btnScreen2)
        baseContainer.children['menuContainer'].children['btnScreen1'].set_on_click_listener(self.onclick_btnScreen1)
        
        #The contentContainer 
        contentContainer = Widget()
        contentContainer.attributes['class'] = "Widget"
        contentContainer.attributes['editor_baseclass'] = "Widget"
        contentContainer.attributes['editor_varname'] = "contentContainer"
        contentContainer.attributes['editor_tag_type'] = "widget"
        contentContainer.attributes['editor_newclass'] = "False"
        contentContainer.attributes['editor_constructor'] = "()"
        contentContainer.style['position'] = "absolute"
        contentContainer.style['overflow'] = "auto"
        contentContainer.style['left'] = "200px"
        contentContainer.style['top'] = "10px"
        contentContainer.style['margin'] = "0px"
        contentContainer.style['border-style'] = "solid"
        contentContainer.style['width'] = "450px"
        contentContainer.style['display'] = "block"
        contentContainer.style['border-width'] = "1px"
        contentContainer.style['height'] = "500px"
        
        
        #Create top Level instances for the content Widgets.
        #By defining these as top Level the Widgets live even if they are not shown

        self.screen1 = screen1Widget()   
        self.screen2 = screen2Widget()   
        
        #Add the initial content to the contentContainer
        contentContainer.append(self.screen1,'screen1')

        #Define the listeners for GUI elements which are contained in the content Widgets
        #We can't define it in the Widget classes because the listeners wouldn't have access to other GUI elements outside the Widget
        self.screen2.children['btnsend'].set_on_click_listener(self.send_text_to_screen1)
        self.screen1.children['btnSave1'].set_on_click_listener(self.save_relay_1)
        self.screen1.children['btnSave2'].set_on_click_listener(self.save_relay_2)
        
        #Add the contentContainer to the baseContainer
        baseContainer.append(contentContainer,'contentContainer')
                
        #Make the local "baseContainer" a class member of the App
        self.baseContainer = baseContainer
        
        #return the baseContainer as root Widget
        return self.baseContainer
    

    #Define the callbacks for the listeners

    def onclick_btnScreen2(self,emitter):
        #Remove Screen 1 Widget from the contentWidget, screen1 will still exist in memory
        if 'screen1' in self.baseContainer.children['contentContainer'].children.keys():
            self.baseContainer.children['contentContainer'].remove_child(self.baseContainer.children['contentContainer'].children['screen1'])
        #Add Screen2 to the contentWidget
        self.baseContainer.children['contentContainer'].append(self.screen2,'screen2')      
        
    def onclick_btnScreen1(self,emitter):
        #Remove Screen 2 Widget from the contentWidget, screen1 will still exist in memory
        if 'screen2' in self.baseContainer.children['contentContainer'].children.keys():
            self.baseContainer.children['contentContainer'].remove_child(self.baseContainer.children['contentContainer'].children['screen2'])
        #Add Screen1 to the contentWidget
        self.baseContainer.children['contentContainer'].append(self.screen1,'screen1')      
        
    def send_text_to_screen1(self,emitter):
        #Take the text of the TextBox in screen2 and put it into the TextBox in screen1
        self.screen1.children['mytextbox'].set_text(self.screen2.children['mytextbox'].get_text())

    def save_relay_1(self,emitter):
        print('save 1')
        time1 = self.screen1.children['relay1startinput'].get_text()
        time2 = self.screen1.children['relay1finishinput'].get_text()
        if (time1 == '' or time2==''):
            return self.screen1.children['relay1result'].set_text("Please fill in the fields.")
        now = datetime.date.today()
        start = str(now)+" "+time1
        finish = str(now)+" "+time2
        db.insertConfig('1',start,finish)
        self.screen1.children['relay1result'].set_text("Successfully modified relay 1.")
        mail.notify("The start for relay 1 has been set to "+ str(start)+
                    " and the finish time has been set to "+str(finish))
        
    def save_relay_2(self,emitter):
        print('save 2')
        time1 = self.screen1.children['relay2startinput'].get_text()
        time2 = self.screen1.children['relay2finishinput'].get_text()
        if (time1 == '' or time2==''):
            return self.screen1.children['relay2result'].set_text("Please fill in the fields.")
        now = datetime.date.today()
        start = str(now)+" "+time1
        finish = str(now)+" "+time2
        db.insertConfig('2',start,finish)
        self.screen1.children['relay2result'].set_text("Successfully modified relay 2.")
        mail.notify("The start for relay 1 has been set to "+ str(start)+
                    " and the finish time has been set to "+str(finish))


#Configuration
configuration = {'config_port': 8081, 'config_address': '0.0.0.0', 'config_resourcepath': './res/', 'config_enable_file_cache': True, 'config_multiple_instance': True, 'config_project_name': 'multiscreen', 'config_start_browser': True}

if __name__ == "__main__":
    # start(MyApp,address='127.0.0.1', port=8081, multiple_instance=False,enable_file_cache=True, update_interval=0.1, start_browser=True)
    start(multiscreen, address=configuration['config_address'], port=configuration['config_port'], 
                        multiple_instance=configuration['config_multiple_instance'], 
                        enable_file_cache=configuration['config_enable_file_cache'],
                        start_browser=configuration['config_start_browser'])

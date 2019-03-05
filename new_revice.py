# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 19:47:25 2019

@author: atiqu
"""

from Tkinter import *
import serial
from PIL import ImageTk, Image
import os
import time


class com(object):
    
    def __init__(self):
        
        self.root = Tk()
        self.root.geometry("340x242")
        
        self.top_frame = Frame(self.root, bg='grey', width=450, height=150, pady=3)
        self.center = Frame(self.root, bg='purple', width=50, height=40)#, padx=3, pady=3)
        self.ctr_left = Frame(self.center, bg='violet', width=200, height=245)#, padx=3, pady=3)
        self.ctr_right = Frame(self.center, bg='blue3', width=200, height=245)#, padx=3, pady=3)
        self.ctr_left.grid(row=0, column=0, sticky="nsew")
        self.ctr_right.grid(row=0, column=1, sticky="nsew")
        #self.btm_frame = Frame(self.root, bg='white', width=450, height=45, pady=3)
        #self.btm_frame2 = Frame(self.root, bg='lavender', width=450, height=60, pady=3)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        #center frame
        self.center.grid_rowconfigure(1, weight=1)
        self.center.grid_columnconfigure(0, weight=1)
        #center left frame
        self.ctr_left.grid_rowconfigure(1, weight=1)
        self.ctr_left.grid_columnconfigure(0, weight=1)
        #center left frame
        self.ctr_right.grid_rowconfigure(1, weight=1)
        self.ctr_right.grid_columnconfigure(0, weight=1)
        self.top_frame.grid(row=0, sticky="ewns")
        self.center.grid(row=1, sticky="ewns")
        #labels
        self.widget()
        self.model_label = Label(self.top_frame, text='configuration'.upper())
        self.model_label.grid(row=0, column=0,columnspan=3)
        self.root.mainloop()
    
    def widget(self):
        self.port_label = Label(self.top_frame,text="port".upper())
        self.port_label.config(height=1,width=9)
        self.baud_label = Label(self.top_frame,text="Baud Rate".upper())
        self.baud_label.config(height=1,width=9)
        self.port_label.grid(row=1,column=0,sticky= "w")
        self.baud_label.grid(row=2,column=0,sticky= "w")
        self.PORT = Spinbox(self.top_frame,values=("COM1","COM2","COM3","COM4","COM8"))
        self.BAUD = Spinbox(self.top_frame,values=(9600,19200, 38400, 57600, 115200))
        self.PORT.grid(row = 1,column=1)
        self.BAUD.grid(row = 2,column=1)
        self.start_USART_button = Button(self.top_frame,text="start".upper(),command=self.check_cond)
        self.start_USART_button.config(height=3,width=5)
        self.start_USART_button.grid(column=2,row=1,rowspan=2,padx=10,pady=10)
        self.stop_USART_button = Button(self.top_frame,text="stop".upper(),command=self.stop)
        self.stop_USART_button.config(height=3,width=5)
        self.stop_USART_button.grid(column=4,row=1,rowspan=2,padx=10,pady=10)
        
        
        
    def stop(self):
        self.ser.close()
        
    def data(self):
        self.name = ["r1","r2","r","t1","t2","v_l","v_r","v"]
        self.a = {'r1':0,'r2':0,'r':0,'t1':0,'t2':0,"v_l":0,"v_r":0,"v":0}
        self.a_d  = {'r1':0,'r2':0,'r':0,'t1':0,'t2':0,"v_l":0,"v_r":0,"v":0}
        '''for i in range(7):
            self.a[name[i]]=data[3*i:3*(i+1)]'''
                 
    def check_cond(self):
         self.frame_left()
         self.ser = serial.Serial("COM3",9600)
         self.update_label()
         #RX = ser.read() # REC 24 NO DATA
         '''while(True):
             self.data()
             self.frame_right() 
         print("loop exited")'''
         
    def update_label(self):
        data= self.ser.readline()
        self.data()
        if(data == 'r1\n'):
            n = self.ser.readline()
            self.a["r1"] = n
            self.r1.config(text=self.a['r1'])

        if(data == 'r2\n'):
            n = self.ser.readline()
            self.a["r2"] = n
            self.r2.config(text=self.a['r2'])

        if(data == 'r\n'):
            n = self.ser.readline()
            self.a["r"] = n
            self.r.config(text=self.a['r'])

        if(data == 't1\n'):
            n = self.ser.readline()
            self.a["t1"] = n
            self.t1.config(text=self.a['t1'])

        if(data == 't2\n'):
            n = self.ser.readline()
            self.a["t2"] = n
            self.t2.config(text=self.a['t2'])
        self.root.after(500, self.update_label)
        
    def frame_left(self): 
        l_1 = Label(self.ctr_left,text="port name:".upper())#,bg="violet")
        l_1.config(height=1,width=10)
        l_1.grid(row=0,column=0,sticky="w")
        l_2 = Label(self.ctr_left,text="baud rate:".upper())#,bg="violet")
        l_2.config(height=1,width=10)
        l_2.grid(row=1,column=0,sticky="w")
        Label_port = Label(self.ctr_left,text=self.PORT.get())
        Label_baud = Label(self.ctr_left,text=self.BAUD.get())
        Label_port.grid(row=0,column=1,sticky="w")
        Label_baud.grid(row=1,column=1,sticky="w")
        self.frame_right()
    
    def frame_right(self):
        Label(self.ctr_right,text="Recieved data".upper()).grid(row=0,column=0,columnspan=2,sticky="ns")
        Label(self.ctr_right,text="R1:".upper()).grid(row=1,column=0,sticky="w")
        Label(self.ctr_right,text="r2:".upper()).grid(row=2,column=0,sticky="w")
        Label(self.ctr_right,text="ro:".title()).grid(row=3,column=0,sticky="w")
        Label(self.ctr_right,text="t1:".upper()).grid(row=4,column=0,sticky="w")
        Label(self.ctr_right,text="t2:".upper()).grid(row=5,column=0,sticky="w")
        #data to be displayed
        self.r1 = Label(self.ctr_right)#,text=self.a["r1"])
        self.r1.grid(row=1,column=1,padx=3,pady=3)
        self.r2 = Label(self.ctr_right)#,text=self.a["r2"])
        self.r2.grid(row=2,column=1)
        self.r = Label(self.ctr_right)#,text=self.a["r"])
        self.r.grid(row=3,column=1,padx=3,pady=3)
        self.t1 = Label(self.ctr_right)#,text=self.a["t1"])
        self.t1.grid(row=4,column=1)
        self.t2 = Label(self.ctr_right)#,text=self.a["t2"])
        self.t2.grid(row=5,column=1,padx=3,pady=3)
        
a = com()
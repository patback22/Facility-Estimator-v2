from curses import getwin, window
from random import *
import secrets
from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.font import BOLD
import tkinter as tk
from tkinter.messagebox import RETRY
from tkinter.scrolledtext import ScrolledText
from tkinter.tix import ButtonBox
from tokenize import Name
from turtle import ScrolledCanvas, title, width
from unicodedata import name
from webbrowser import get
from ScrolledWindow  import ScrolledWindow
from tkinter import Listbox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 
from matplotlib.figure import Figure
import pandas as pd
import numpy as np
import time
import math
import matplotlib.patches as mpatches
#from ScrolloBaro import ScrollBar

'''
continue putting in grape[zelda - 1][1] in edit function
'''



colors = ("white", "green", "yellow", "blue", "red", "orange", "purple") 
rcolors = secrets.choice(colors)

class Todo:
        def __init__(self):
            self.conn = sqlite3.connect('Surfaces2.db')
            self.c = self.conn.cursor()
            self.create_task_table()

            global win
            global room
            global variable
            global windows
            global desk
            global tables
            
        def create_task_table(self):
            self.c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY,
                        RoomName TEXT NOT NULL,
                        RoomType TEXT NOT NULL,
                        FloorType TEXT NOT NULL,
                        RoomSize INTEGER NOT NULL,
                        windows INTEGER NOT NULL,
                        desks INTEGER NOT NULL,
                        tables INTEGER NOT NULL,
                        Chairs INTEGER NOT NULL,
                        ChalkWhiteBoards INTEGER NOT NULL,
                        Computers INTEGER NOT NULL,
                        Toilets INTEGER NOT NULL,
                        Urinals INTEGER NOT NULL,
                        Sinks INTEGER NOT NULL,
                        HandDryers INTEGER NOT NULL,
                        Mirrors INTEGER NOT NULL,
                        ShowersTubs INTEGER NOT NULL,
                        Largecan INTEGER NOT NULL,
                        smallcan INTEGER NOT NULL,
                        saninap INTEGER NOT NULL,
                        toiletpaperdis INTEGER NOT NULL,
                        papertoweldis INTEGER NOT NULL,
                        handsanidis INTEGER NOT NULL,
                        handsoapdis INTEGER NOT NULL,
                        seatcoverdis INTEGER NOT NULL,
                        walkoffmat INTEGER NOT NULL,
                        cafetables INTEGER NOT NULL,
                        beds INTEGER NOT NULL,
                        vendingmach INTEGER NOT NULL,
                        Zone TEXT NOT NULL

                        );''')

            print("table connect")
        
        def add_room(self):

            global RoomName
            global FloorType

           
            RoomName=room.get()
            RoomType=roomType.get()
            RoomSize=roomsize.get("1.0","end-1c")
            FloorType=variable.get()
            window=windows.get("1.0","end-1c")
            desks=desk.get("1.0","end-1c")
            table=tables.get("1.0","end-1c")
            Chairs=chairs.get("1.0","end-1c")
            Chalkwhiteboard=chalkwhiteboard.get("1.0","end-1c")
            Computers=computers.get("1.0","end-1c")
            Toilets=toilets.get("1.0","end-1c")
            Urinals=urinals.get("1.0","end-1c")
            Sinks=sinks.get("1.0","end-1c")
            Handdryers=handdryers.get("1.0","end-1c")
            Mirrors=mirrors.get("1.0","end-1c")
            Showerstubs=showerstubs.get("1.0","end-1c")   
            Largecan=largecan.get("1.0","end-1c")
            Smallcan=smallcan.get("1.0","end-1c")
            Saninap=saninap.get("1.0","end-1c")
            Toiletpaperdis=toiletpaperdis.get("1.0","end-1c")
            Papertoweldis=papertoweldis.get("1.0","end-1c")
            Handsanidis=handsanidis.get("1.0","end-1c")
            Handsoapdis=handsoapdis.get("1.0","end-1c") 
            Seatcoverdis=seatcoverdis.get("1.0","end-1c")
            Walkoffmat=walkoffmat.get("1.0","end-1c") 
            Cafetables=cafetables.get("1.0","end-1c")
            Beds=beds.get("1.0","end-1c")
            Vendingmach=vendingmach.get("1.0","end-1c") 
            Zone=Zone.get("1.0","end-1c") 
            
               
                

            print("Room Added")

            print(str(RoomName))
            print(RoomType)
            #print(str(FloorType))
            print(window)
            print(desks)
            print(table)

            
            
            if RoomName == "":
                tk.messagebox.showwarning("Warning", "Must have Room Name")
                print("Sheeeeesh")
                Open_Add_Room_Window()

            else:
                pass

            

            try:
                table = int(table)
            except ValueError:
                print("not a valid integer")
                tk.messagebox.showwarning("Warning", "Tables must be a number")
                print("int biatch")
                Open_Add_Room_Window()
            else:
                pass

            
            try:
                window = int(window)
            except ValueError:
                print("not a valid integer")
                tk.messagebox.showwarning("Warning", "Windows must be a number")
                Open_Add_Room_Window()
            else:
                pass

            
            try:
                desks = int(desks)
            except ValueError:
                tk.messagebox.showwarning("Warning", "Desks must be a number")
                Open_Add_Room_Window()
            else:
                pass
            
                self.c.execute('INSERT INTO tasks (RoomName, RoomType, FloorType, RoomSize, windows, desks, tables, Chairs, ChalkWhiteBoards, Computers, Toilets, Urinals, Sinks, HandDryers, Mirrors, ShowersTubs, largecan, smallcan, saninap, toiletpaperdis, papertoweldis, handsoapdis, handsanidis, seatcoverdis, walkoffmat, cafetables, beds, vendingmach, Zone) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', (RoomName, RoomType, FloorType, RoomSize ,window, desks, table, Chairs, Chalkwhiteboard, Computers, Toilets, Urinals, Sinks, Handdryers, Mirrors, Showerstubs, Largecan, Smallcan, Saninap, Toiletpaperdis, Papertoweldis, Handsoapdis, Handsanidis, Seatcoverdis, Walkoffmat, Cafetables, Beds, Vendingmach, Zone))
                self.conn.commit()

                print("abdication")
            
            '''
            windowTotal_Label.configure(text="Window Totals" + " " + str(sum(getWindowTotals())))
            deskTotal_Label.configure(text="Desk Totals" + " " + str(sum(getDeskTotals())))
            tableTotal_Label.configure(text="Table Totals" + " " + str(sum(getTableTotals())))
            Total_CostperYear.configure(text="Total Cost Yearly" + " " + str(Building_Cost * 180))
            '''
            
            win.destroy()   
               

app = Todo()

def getWindowTotals():

    app.c.execute('SELECT windows FROM tasks')
    wT = [job[0] for job in app.c.execute('SELECT windows FROM tasks')]

    
    return wT



window_totals_list = getWindowTotals()
window_totals = sum(window_totals_list)
print(window_totals)


def getDeskTotals():
    
    app.c.execute('SELECT desks FROM tasks')
    dT = [job[0] for job in app.c.execute('SELECT desks FROM tasks')]

    
    return dT


desk_totals_list = getDeskTotals()
desk_totals = sum(desk_totals_list)
print(desk_totals)

def getTableTotals():
    
    app.c.execute('SELECT tables FROM tasks')
    tT = [job[0] for job in app.c.execute('SELECT tables FROM tasks')]

   
    return tT


table_totals_list = getTableTotals()
table_totals = sum(table_totals_list)

def get_Surface_Totals():
    window_totals = sum(window_totals_list)
    desk_totals = sum(desk_totals_list)
    table_totals = sum(table_totals_list)
    print("totals mate")


def Open_Add_Room_Window():
    global room
    global variable
    global roomType
    global roomsize
    global windows
    global desk
    global tables
    global chairs
    global chalkwhiteboard
    global computers
    global toilets
    global urinals
    global sinks
    global handdryers
    global mirrors
    global showerstubs
    global largecan
    global smallcan
    global saninap
    global toiletpaperdis
    global papertoweldis
    global handsanidis
    global handsoapdis
    global seatcoverdis
    global walkoffmat
    global cafetables
    global beds
    global vendingmach



    global OPTIONS3

    global win

    win=Toplevel()
    
    # Set the geometry
    win.geometry("695x500")
    win.configure()

    addRoom_RoomsFrame = Frame(win, height=600, width=600, padx=10, pady=10)
    addRoom_RoomsFrame.grid(row=0, column=0)

    addRoom_RoomsFrame2 = Frame(win, height=600, width=600, padx=10, pady=10)
    addRoom_RoomsFrame2.grid(row=0,column=1, sticky=N)

    # Room Name text widget
    room=Entry(addRoom_RoomsFrame)   
    room.insert(END, "")
    room.grid(row=0, column=1)
    room_name_label = Label(addRoom_RoomsFrame, text = "Room Name").grid(row=0, column=0)         

    # Flooring Type text widget
       
    OPTIONS3 = [
    "Classroom",
    "Restroom",
    "Hallway",
    "Lobby",
    "Office",
    "Gym",
    "Cafeteria"
    ] #etc

    roomType = StringVar(addRoom_RoomsFrame)
    roomType.set(OPTIONS3[0]) # default value

    w2 = OptionMenu(addRoom_RoomsFrame, roomType, *OPTIONS3)
    w2.grid(row=1, column=1)

    Room_type_Label = Label(addRoom_RoomsFrame, text = "Room Type").grid(row=1, column=0)         

    OPTIONS = [
    "VCT",
    "Carpet",
    "Estry",
    "Rubber",
    "Wood"
    ] #etc

    variable = StringVar(addRoom_RoomsFrame)
    variable.set(OPTIONS[0]) # default value

    w = OptionMenu(addRoom_RoomsFrame, variable, *OPTIONS)
    w.grid(row=2, column=1)

    floor_type_label = Label(addRoom_RoomsFrame, text = "Floor Type").grid(row=2, column=0)  

    roomsize=Text(addRoom_RoomsFrame, width=20, height=1)
    roomsize.insert(END, 0)
    roomsize.grid(row=3, column=1)
    roomsize_label = Label(addRoom_RoomsFrame, text = "Room Size").grid(row=3, column=0)  
    roomsize_label2 = Label(addRoom_RoomsFrame, text = "ft. squared").grid(row=3, column=2)

    surfaces_label = Label(addRoom_RoomsFrame, text="Surfaces", font=BOLD).grid(columnspan=2, rowspan=2, row=4, column=0)

    # Windows text widget
    windows=Text(addRoom_RoomsFrame, width=20, height=1)
    windows.insert(END, 0)
    windows.grid(row=6, column=1)
    windows_label = Label(addRoom_RoomsFrame, text = "Windows").grid(row=6, column=0)           

    # Desk text widget
    desk=Text(addRoom_RoomsFrame, width=20, height=1)
    desk.insert(END, 0)
    desk.grid(row=7, column=1)
    Desk_label = Label(addRoom_RoomsFrame, text = "Desk").grid(row=7, column=0)            

    # Tables text widget
    tables=Text(addRoom_RoomsFrame, width=20, height=1)
    tables.insert(END, 0)
    tables.grid(row=8, column=1)
    table_label = Label(addRoom_RoomsFrame, text = "Tables").grid(row=8, column=0)  

    chairs=Text(addRoom_RoomsFrame, width=20, height=1)
    chairs.insert(END, 0)
    chairs.grid(row=9, column=1)
    chairs_label = Label(addRoom_RoomsFrame, text = "Chairs").grid(row=9, column=0)

    chalkwhiteboard=Text(addRoom_RoomsFrame, width=20, height=1)
    chalkwhiteboard.insert(END, 0)
    chalkwhiteboard.grid(row=10, column=1)
    chalkwhiteboard_label = Label(addRoom_RoomsFrame, text = "Chalk/Whiteboards").grid(row=10, column=0)

    computers=Text(addRoom_RoomsFrame, width=20, height=1)
    computers.insert(END, 0)
    computers.grid(row=11, column=1)
    computers_label = Label(addRoom_RoomsFrame, text = "Computers").grid(row=11, column=0)    

    restrooms_label = Label(addRoom_RoomsFrame, text="Restrooms", font=BOLD).grid(columnspan=2, rowspan=2, row=12, column=0)  

    toilets=Text(addRoom_RoomsFrame, width=20, height=1)
    toilets.insert(END, 0)
    toilets.grid(row=14, column=1)
    toilets_label = Label(addRoom_RoomsFrame, text = "Toilets").grid(row=14, column=0)

    urinals=Text(addRoom_RoomsFrame, width=20, height=1)
    urinals.insert(END, 0)
    urinals.grid(row=15, column=1)
    urinals_label = Label(addRoom_RoomsFrame, text = "Urinals").grid(row=15, column=0)

    sinks=Text(addRoom_RoomsFrame, width=20, height=1)
    sinks.insert(END, 0)
    sinks.grid(row=16, column=1)
    sinks_label = Label(addRoom_RoomsFrame, text = "Sinks").grid(row=16, column=0)

    mirrors=Text(addRoom_RoomsFrame, width=20, height=1)
    mirrors.insert(END, 0)
    mirrors.grid(row=17, column=1)
    mirrors_label = Label(addRoom_RoomsFrame, text = "Mirrors").grid(row=17, column=0)

    handdryers=Text(addRoom_RoomsFrame, width=20, height=1)
    handdryers.insert(END, 0)
    handdryers.grid(row=18, column=1)
    handdryers_label = Label(addRoom_RoomsFrame, text = "Hand Dryers").grid(row=18, column=0)

    showerstubs=Text(addRoom_RoomsFrame, width=20, height=1)
    showerstubs.insert(END, 0)
    showerstubs.grid(row=19, column=1)
    showerstubs_label = Label(addRoom_RoomsFrame, text = "Showers/Tubs").grid(row=19, column=0)

    Recepticals_label = Label(addRoom_RoomsFrame2, text="Recepticals", font=BOLD).grid(columnspan=2, rowspan=2, row=0, column=0)

    largecan=Text(addRoom_RoomsFrame2, width=20, height=1)
    largecan.insert(END, 0)
    largecan.grid(row=2, column=1)
    largecan_label = Label(addRoom_RoomsFrame2, text = "Large Trash Can").grid(row=2, column=0)

    smallcan=Text(addRoom_RoomsFrame2, width=20, height=1)
    smallcan.insert(END, 0)
    smallcan.grid(row=3, column=1)
    smallcan_label = Label(addRoom_RoomsFrame2, text = "Small Trash Can").grid(row=3, column=0)

    saninap=Text(addRoom_RoomsFrame2, width=20, height=1)
    saninap.insert(END, 0)
    saninap.grid(row=4, column=1)
    saninap_label = Label(addRoom_RoomsFrame2, text = "Sanitary Napkin").grid(row=4, column=0)

    Dispensers_label = Label(addRoom_RoomsFrame2, text="Dispensers", font=BOLD).grid(columnspan=2, rowspan=2, row=5, column=0)

    toiletpaperdis=Text(addRoom_RoomsFrame2, width=20, height=1)
    toiletpaperdis.insert(END, 0)
    toiletpaperdis.grid(row=7, column=1)
    toiletpaperdis_label = Label(addRoom_RoomsFrame2, text = "Toilet Paper").grid(row=7, column=0)

    papertoweldis=Text(addRoom_RoomsFrame2, width=20, height=1)
    papertoweldis.insert(END, 0)
    papertoweldis.grid(row=8, column=1)
    papertoweldis_label = Label(addRoom_RoomsFrame2, text = "Paper Towel").grid(row=8, column=0)

    handsoapdis=Text(addRoom_RoomsFrame2, width=20, height=1)
    handsoapdis.insert(END, 0)
    handsoapdis.grid(row=9, column=1)
    handsoapdis_label = Label(addRoom_RoomsFrame2, text = "Hand Soap").grid(row=9, column=0)

    handsanidis=Text(addRoom_RoomsFrame2, width=20, height=1)
    handsanidis.insert(END, 0)
    handsanidis.grid(row=10, column=1)
    handsanidis_label = Label(addRoom_RoomsFrame2, text = "Hand Sanitizer").grid(row=10, column=0)

    seatcoverdis=Text(addRoom_RoomsFrame2, width=20, height=1)
    seatcoverdis.insert(END, 0)
    seatcoverdis.grid(row=11, column=1)
    seatcoverdis_label = Label(addRoom_RoomsFrame2, text = "Toilet Seat Cover").grid(row=11, column=0)

    Misc_label = Label(addRoom_RoomsFrame2, text="Miscellaneous", font=BOLD).grid(columnspan=2, rowspan=2, row=12, column=0)

    walkoffmat=Text(addRoom_RoomsFrame2, width=20, height=1)
    walkoffmat.insert(END, 0)
    walkoffmat.grid(row=14, column=1)
    walkoffmat_label = Label(addRoom_RoomsFrame2, text = "Walk Off Mats").grid(row=14, column=0)

    cafetables=Text(addRoom_RoomsFrame2, width=20, height=1)
    cafetables.insert(END, 0)
    cafetables.grid(row=15, column=1)
    cafetables_label = Label(addRoom_RoomsFrame2, text = "Cafeteria Tables").grid(row=15, column=0)

    vendingmach=Text(addRoom_RoomsFrame2, width=20, height=1)
    vendingmach.insert(END, 0)
    vendingmach.grid(row=16, column=1)
    vendingmach_label = Label(addRoom_RoomsFrame2, text = "Vending Machines").grid(row=16, column=0)

    beds=Text(addRoom_RoomsFrame2, width=20, height=1)
    beds.insert(END, 0)
    beds.grid(row=17, column=1)
    beds_label = Label(addRoom_RoomsFrame2, text = "Beds").grid(row=17, column=0)

    OPTIONSZ = [
    "Classroom",
    "Restroom",
    "Hallway",
    "Lobby",
    "Office",
    "Gym",
    "Cafeteria"
    ] #etc

    roomType = StringVar(addRoom_RoomsFrame)
    roomType.set(OPTIONS3[0]) # default value

    w2 = OptionMenu(addRoom_RoomsFrame, roomType, *OPTIONS3)
    w2.grid(row=1, column=1)

    Room_type_Label = Label(addRoom_RoomsFrame, text = "Room Type").grid(row=1, column=0)  


    b = Button(win, text = "Add Room", image = photo) # bg="white", borderwidth=0, compound=CENTER, fg="white", command=app.add_room)
    b.grid()  #columnspan=2)




def Pullroom_windows():
    app.c.execute('SELECT windows FROM tasks')
    RwT = [job[0] for job in app.c.execute('SELECT windows FROM tasks')]

    print(RwT)

def edit_room_info():
    pass

def create_rooms_inTab2():

        global rN
        global RwT
        global DwT
        global TwT
        global RtwT
        global WwT
        global grant
        global zelda
        global Room_Cost
        global cost_perDesk
        global cost_perWindow
        global cost_perTable
        global Total_CostperYear
        global Building_Cost
        global SurfaceList
        global TimeList
        global SurfaceNameList
        global SurfaceNameListLength
        global roomTypeList
        global RTL
        global Classroom
        global Restroom
        global Hallway
        global Lobby 
        global Office
        global Gym
        global Cafeteria
        global NewTimeList
        global FTwT
        global TotalSurfaceTime2DP
        global Average_Wage
        global FSwT

        Average_Wage = 15.00

        app.c.execute('SELECT RoomName FROM tasks')
        rN = [job[0] for job in app.c.execute('SELECT RoomName FROM tasks')]

        FSwT = [job[0] for job in app.c.execute('SELECT RoomSize FROM tasks')]

        RtwT = [job[0] for job in app.c.execute('SELECT RoomType FROM tasks')]

        FTwT = [job[0] for job in app.c.execute('SELECT FloorType FROM tasks')]

        WwT = [job[0] for job in app.c.execute('SELECT windows FROM tasks')]
        time_perWindow = 1/60
        cost_perWindow = Average_Wage * time_perWindow

        DwT = [job[0] for job in app.c.execute('SELECT desks FROM tasks')]
        time_perDesk = .8/60
        cost_perDesk = Average_Wage * time_perDesk
        
        TwT = [job[0] for job in app.c.execute('SELECT tables FROM tasks')]
        time_perTable = .5/60
        cost_perTable = Average_Wage * time_perTable

        CwT = [job[0] for job in app.c.execute('SELECT chairs FROM tasks')]
        time_perChair = .4/60
        cost_perChair = Average_Wage * time_perChair

        CWBwT = [job[0] for job in app.c.execute('SELECT ChalkWhiteBoards FROM tasks')]
        time_perChalkWhiteboard = 1.5/60
        cost_perChalkWhiteboard = Average_Wage * time_perChalkWhiteboard

        CPwT = [job[0] for job in app.c.execute('SELECT Computers FROM tasks')]
        time_perComputer = .3/60
        cost_perComputer = Average_Wage * time_perComputer

        TOwT = [job[0] for job in app.c.execute('SELECT Toilets FROM tasks')]
        time_perToilet = 3.83/60
        cost_perToilet = Average_Wage * time_perToilet

        UwT = [job[0] for job in app.c.execute('SELECT Urinals FROM tasks')]
        time_perUrinal = 3/60
        cost_perUrinal = Average_Wage * time_perUrinal

        SwT = [job[0] for job in app.c.execute('SELECT Sinks FROM tasks')]
        time_perSink = 3/60
        cost_perSink = Average_Wage * time_perSink

        HDwT = [job[0] for job in app.c.execute('SELECT Handdryers FROM tasks')]
        time_perHanddryer = .5/60
        cost_perHanddryer = Average_Wage * time_perHanddryer

        MIwT = [job[0] for job in app.c.execute('SELECT Mirrors FROM tasks')]
        time_perMirrors = 1/60
        cost_perMirrors = Average_Wage * time_perMirrors

        STwT = [job[0] for job in app.c.execute('SELECT Showerstubs FROM tasks')]
        time_perShowerstubs = 6/60
        cost_perShowerstubs = Average_Wage * time_perShowerstubs

        LCwT = [job[0] for job in app.c.execute('SELECT largecan FROM tasks')]
        time_perLargecan = 1/60
        cost_perLargecan = Average_Wage * time_perLargecan

        SCwT = [job[0] for job in app.c.execute('SELECT smallcan FROM tasks')]
        time_perSmallcan = 0.8/60
        cost_perSmallcan = Average_Wage * time_perSmallcan

        SNwT = [job[0] for job in app.c.execute('SELECT saninap FROM tasks')]
        time_perSaninap = 0.33/60
        cost_perSaninap = Average_Wage * time_perSaninap

        TPDwT = [job[0] for job in app.c.execute('SELECT toiletpaperdis FROM tasks')]
        time_perToiletpaperdis = .5/60
        cost_perToiletpaperdis = Average_Wage * time_perToiletpaperdis

        PTDwT = [job[0] for job in app.c.execute('SELECT papertoweldis FROM tasks')]
        time_perPapertoweldis = .5/60
        cost_perPapertoweldis = Average_Wage * time_perPapertoweldis

        HSDwT = [job[0] for job in app.c.execute('SELECT handsanidis FROM tasks')]
        time_perHandsanidis = .5/60
        cost_perHandsanidis = Average_Wage * time_perHandsanidis

        HDwT = [job[0] for job in app.c.execute('SELECT handsoapdis FROM tasks')]
        time_perHandsoadis = .5/60
        cost_perHandsoadis = Average_Wage * time_perHandsoadis
        
        SCDwT = [job[0] for job in app.c.execute('SELECT seatcoverdis FROM tasks')]
        time_perSeatcoverdis = .5/60
        cost_perSeatcoverdis = Average_Wage * time_perSeatcoverdis

        WMwT = [job[0] for job in app.c.execute('SELECT walkoffmat FROM tasks')]
        time_perWalkoffmat = 1.08/60
        cost_perWalkoffmat= Average_Wage * time_perWalkoffmat

        CTwT = [job[0] for job in app.c.execute('SELECT cafetables FROM tasks')]
        time_perCafetables = 3/60
        cost_perCafetables = Average_Wage * time_perCafetables

        BwT = [job[0] for job in app.c.execute('SELECT beds FROM tasks')]
        time_perBeds = 3/60
        cost_perBeds = Average_Wage * time_perBeds

        VMwT = [job[0] for job in app.c.execute('SELECT vendingmach FROM tasks')]
        time_perVendingmach = 1/60
        cost_perVendingmach = Average_Wage * time_perVendingmach



        SurfaceList = [WwT, TwT, DwT, CwT, CWBwT, CPwT, TOwT, UwT, SwT, HDwT, MIwT, STwT, LCwT, SCwT, SNwT, TPDwT, 
                       PTDwT, HSDwT, HDwT, SCDwT, WMwT, CTwT, BwT, VMwT]    
        TimeList = [time_perWindow, time_perTable, time_perDesk, time_perChair, time_perChalkWhiteboard, time_perComputer, time_perToilet, 
                    time_perUrinal, time_perSink, time_perHanddryer, time_perMirrors, time_perShowerstubs, time_perLargecan,
                    time_perSmallcan, time_perSaninap, time_perToiletpaperdis, time_perPapertoweldis, time_perHandsanidis,
                    time_perHandsoadis, time_perSeatcoverdis, time_perWalkoffmat, time_perCafetables, time_perBeds, time_perVendingmach] 

        #NewTimeList = list(TimeList)            
        SurfaceNameList = ('Windows', 'Tables', 'Desks', 'Chairs', 'Chalk/White Boards', 'Computers', 'Toilets', 'Urinals', 'Sinks', 'Hand Dryers', 
                           'Mirrors', 'Showers/Tubs', 'Large Cans', 'Small Cans', 'Sanitary Napkin Dispensers', 'Toilet Paper Dispensers', 'Paper Towel Dispensers',
                           'Hand Sanitizer Dispensers', 'HandSoap Dispensers', 'SeatCover Dispensers', 'Walk Off Mats', 'Cafeteria Tables', 'Beds', 'Vending Machines') 
        SurfaceNameListLength = len(SurfaceNameList)

        #return rN
        print(rN)
       
        print(round(len(rN)/4))

        
        grant = 0



        Building_Cost = float((cost_perDesk * sum(DwT)) + (cost_perTable * sum(TwT)) + (cost_perWindow * sum(WwT)))
        print(Building_Cost)

        CostPerYear = Building_Cost * 180

        currencyCostPerYear = "{:0,.2f}".format(float(CostPerYear))

        Total_CostperYearLabel = Label(tab1, text="Total Cost Yearly" + " $" + str(currencyCostPerYear), font=("Ariel", 14), padx=20, pady=20)
        Total_CostperYearLabel.pack(anchor=SE)


        Classroom = 0
        Restroom = 0 
        Hallway = 0
        Lobby = 0
        Office = 0
        Gym = 0
        Cafeteria = 0


        for Names in range(len(rN)):

                    Room_Cost = float((cost_perDesk * DwT[grant]) + (cost_perTable * TwT[grant]) + (cost_perWindow * WwT[grant]))
                    print(Room_Cost)

                    GGG = LabelFrame(Borking2, labelanchor = W, bg="black")
                    GGG.grid(sticky=W)  #row=jack, column=diane, sticky=W)

                    ButtonColor = "green"
   
                    if str(RtwT[grant]) == "Classroom":
                        ButtonColor = "White"
                        Classroom += 1
        
                    elif str(RtwT[grant]) == "Restroom":
                        ButtonColor = "Red"
                        Restroom += 1

                    elif str(RtwT[grant]) == "Office":
                        ButtonColor = "Orange"
                        Office += 1

                    elif str(RtwT[grant]) == "Lobby":
                        ButtonColor = "Blue"
                        Lobby += 1

                    elif str(RtwT[grant]) == "Cafeteria":
                        ButtonColor = "Purple"
                        Cafeteria += 1

                    elif str(RtwT[grant]) == "Gym":
                        ButtonColor = "Grey"
                        Gym += 1

                    elif str(RtwT[grant]) == "Hallway":
                        ButtonColor = "Aqua"
                        Hallway += 1

                    else:
                        ButtonColor = "yellow"

                    roomTypeList = (Classroom, Restroom, Hallway, Lobby, Office, Gym, Cafeteria)

                    PPP = Button(GGG, text="Room:  " + rN[grant], bg=ButtonColor)
                    PPP.grid(row=grant, column=0, sticky=W, padx=10, pady=10)                 #pack(side=LEFT, padx=10, pady=10)    
                    print(rN[grant])

                    RRR = Label(GGG, text="Room Type:  " + str(RtwT[grant]))
                    RRR.grid(row=grant, column=1, padx=10, pady=10)                                         #pack(side=LEFT, padx=10, pady=10)
                    
                    WWW = Label(GGG, text="Windows:  " + str(WwT[grant]))
                    WWW.grid(row=grant, column=2,  padx=10, pady=10)      #pack(side=LEFT, padx=10, pady=10)

                    DDD = Label(GGG, text="Desks:  " + str(DwT[grant]))
                    DDD.grid(row=grant, column=3, padx=10, pady=10)           #pack(side=LEFT, padx=10, pady=10)

                    TTT = Label(GGG, text="Tables:  " + str(TwT[grant]))
                    TTT.grid(row=grant, column=4, padx=10, pady=10)         #pack(side=LEFT, padx=10,pady=10)

                    Surface_Totals = Label(GGG, text=("Totals:  " + str(WwT[grant] + DwT[grant] + TwT[grant])))
                    Surface_Totals.grid(row=grant, column=5, padx=10, pady=10)           #pack(side=LEFT, padx=10,pady=10)
                     
                    grant_count = Label(GGG, text=grant + 1)
                    grant_count.grid(row=grant, column=6, padx=10, pady=10)            #pack(side=LEFT, padx=10, pady=10)

                    currency = "{:0,.2f}".format(float(Room_Cost))

                    Room_Cost_Label = Label(GGG, text="$" + str(currency))
                    Room_Cost_Label.grid(row=grant, column=6, padx=10, pady=10)        #pack(side=LEFT, padx=10, pady=10)

                    Edit_data_button = Button(GGG, text="Edit", bg=ButtonColor, command = lambda text=grant:ButtonClick(text))
                    Edit_data_button.bind(Edit_Room)
                    Edit_data_button.grid(row=grant, column=7, padx=10, pady=10, sticky=E)          #pack(side=LEFT, padx=10, pady=10)    #row=grant, column=3)   #row=row, column=column)
                    
                    grant += 1

                               

def Surface_Addition():

    global TimeCost

    print(SurfaceNameList[6])

    num = 0

    for surface in SurfaceList:

        global HourValue

        HourValue = (int(sum(SurfaceList[num])) * float(TimeList[num]))
        TotalSurfaceTime2DP = f'{HourValue: .2f}'

        TimeCost = []
        TimeCost.append(HourValue)

        SurfaceLabel = Label(nimFrame1, text=(str(SurfaceNameList[num]) + ":  " + str(sum(SurfaceList[num]))) + "  Total Time to Clean: "
                             + (str(TotalSurfaceTime2DP)) + " Hours", bg="pink")
        SurfaceLabel.grid(row=int(num), column=0, sticky=W)

        SurfaceTimeLabel = Label(nimFrame1, text=(str(SurfaceNameList[num]) + ': ' + (str(int(sum(SurfaceList[num])) * float(TimeList[num])))), bg='pink')
        
       
        num += 1
        



def ButtonClick(grant):

    global zelda

    print(grant + 1)
    zelda = grant + 1
    Edit_Room()
    return zelda                    
                   



def Add_edited_data():



    global QRoomType

    QRoomName=Qroom.get()
    QRoomType=QroomType.get()
    QFloorType=Qvariable.get()
    QRoomSize=Qroomsize.get("1.0","end-1c")
    Qwindow=Qwindows.get("1.0","end-1c")
    Qdesks=Qdesk.get("1.0","end-1c")
    Qtable=Qtables.get("1.0","end-1c")
    QChairs=Qchairs.get("1.0","end-1c")
    QChalkwhiteboard=Qchalkwhiteboard.get("1.0","end-1c")
    QComputers=Qcomputers.get("1.0","end-1c")
    QToilets=Qtoilets.get("1.0","end-1c")
    QUrinals=Qurinals.get("1.0","end-1c")
    QSinks=Qsinks.get("1.0","end-1c")
    QHanddryers=Qhanddryers.get("1.0","end-1c")
    QMirrors=Qmirrors.get("1.0","end-1c")
    QShowerstubs=Qshowerstubs.get("1.0","end-1c")  
    QLargecan=Qlargecan.get("1.0","end-1c")
    QSmallcan=Qsmallcan.get("1.0","end-1c")
    QSaninap=Qsaninap.get("1.0","end-1c")
    QToiletpaperdis=Qtoiletpaperdis.get("1.0","end-1c")
    QPapertoweldis=Qpapertoweldis.get("1.0","end-1c")
    QHandsanidis=Qhandsanidis.get("1.0","end-1c")
    QHandsoapdis=Qhandsoapdis.get("1.0","end-1c") 
    QSeatcoverdis=Qseatcoverdis.get("1.0","end-1c")
    QWalkoffmat=Qwalkoffmat.get("1.0","end-1c") 
    QCafetables=Qcafetables.get("1.0","end-1c")
    QBeds=Qbeds.get("1.0","end-1c")
    QVendingmach=Qvendingmach.get("1.0","end-1c") 




    print(QRoomName)
    print(QFloorType)

    print("JRJRJRJRJRJR" + str(zelda))

    SQL_UpDate = ('''UPDATE tasks SET RoomName =?, RoomType = ?, FloorType = ?, windows = ?, desks = ?, tables = ?, Chairs = ?, ChalkWhiteBoards = ?, Computers = ?, Toilets = ?, Urinals = ?, Sinks = ?, HandDryers = ?, Mirrors = ?, ShowersTubs = ?, Largecan = ?, Smallcan = ?, Saninap = ?, Toiletpaperdis = ?, Papertoweldis = ?, Handsanidis = ?, Handsoapdis = ?, Seatcoverdis = ?, Walkoffmat = ?, Cafetables = ?, Beds = ?, Vendingmach = ? WHERE id == ?;''')
    app.c.execute(SQL_UpDate, (QRoomName, QRoomType, QFloorType, Qwindow, Qdesks, Qtable, QChairs, QChalkwhiteboard, QComputers, QToilets, QUrinals, QSinks, QHanddryers, QMirrors, QShowerstubs, QLargecan, QSmallcan, QSaninap, QToiletpaperdis, QPapertoweldis, QHandsanidis, QHandsoapdis, QSeatcoverdis, QWalkoffmat, QCafetables, QBeds, QVendingmach, zelda))

    app.conn.commit()

    print("JRJRJRJRJRJR" + str(zelda))

    editRoomWin.destroy()

def Edit_Room():

            global Qroom
            global QroomType
            global Qvariable
            global Qroomsize
            global Qdesk
            global Qtables
            global Qwindows
            global Qchairs
            global Qchalkwhiteboard
            global Qcomputers
            global Qtoilets
            global Qurinals
            global Qsinks
            global Qhanddryers
            global Qmirrors
            global Qshowerstubs  
            global Qlargecan
            global Qsmallcan
            global Qsaninap
            global Qtoiletpaperdis
            global Qpapertoweldis
            global Qhandsanidis
            global Qhandsoapdis
            global Qseatcoverdis
            global Qwalkoffmat
            global Qcafetables
            global Qbeds
            global Qvendingmach      
            global editRoomWin
            global grape


            print(str(zelda) + "Heytherebigboy")
            
            statement = '''SELECT * FROM tasks'''

            app.c.execute(statement)

            grape = app.c.fetchall()
            print(grape[zelda - 1])

            editRoomWin=Toplevel()
    
            # Set the geometry
            editRoomWin.geometry("695x500")
            editRoomWin.configure(bg="white")

            QaddRoom_RoomsFrame = Frame(editRoomWin, height=600, width=600)
            QaddRoom_RoomsFrame.grid(row=0, column=0)

            QaddRoom_RoomsFrame2 = Frame(editRoomWin, height=600, width=600, padx=10, pady=10)
            QaddRoom_RoomsFrame2.grid(row=0,column=1, sticky=N)

            # Room Name text widget
            Qroom=Entry(QaddRoom_RoomsFrame)   
            Qroom.insert(END, grape[zelda - 1][1])
            Qroom.grid(row=0, column=1)
            Qroom_name_label = Label(QaddRoom_RoomsFrame, text = "Room Name").grid(row=0, column=0)         

            # Flooring Type text widget
       
            QOPTIONS3 = [
            "Classroom",
            "Restroom",
            "Hallway",
            "Lobby",
            "Office",
            "Gym",
            "Cafeteria"
            ] #etc

            QroomType = StringVar(QaddRoom_RoomsFrame)
            QroomType.set(grape[zelda - 1][2]) # default value

            Qw2 = OptionMenu(QaddRoom_RoomsFrame, QroomType, *QOPTIONS3)
            Qw2.grid(row=1, column=1)

            QRoom_type_Label = Label(QaddRoom_RoomsFrame, text = "Room Type").grid(row=1, column=0)         

            QOPTIONS = [
            "VCT",
            "Carpet",
            "Estry",
            "Rubber",
            "Wood"
            ] #etc

            Qvariable = StringVar(QaddRoom_RoomsFrame)
            Qvariable.set(grape[zelda - 1][3]) # default value

            Qw = OptionMenu(QaddRoom_RoomsFrame, Qvariable, *QOPTIONS)
            Qw.grid(row=2, column=1)

            Qfloor_type_label = Label(QaddRoom_RoomsFrame, text = "Floor Type").grid(row=2, column=0)  

            Qroomsize=Text(QaddRoom_RoomsFrame, width=20, height=1)
            Qroomsize.insert(END, grape[zelda - 1][4])
            Qroomsize.grid(row=3, column=1)
            Qroomsize_label = Label(QaddRoom_RoomsFrame, text = "Room Size").grid(row=3, column=0)  
            Qroomsize_label2 = Label(QaddRoom_RoomsFrame, text = "ft. squared").grid(row=3, column=2)

            Qsurfaces_label = Label(QaddRoom_RoomsFrame, text="Surfaces", font=BOLD).grid(columnspan=2, rowspan=2, row=4, column=0)

    # Windows text widget
            Qwindows=Text(QaddRoom_RoomsFrame, width=20, height=1)
            Qwindows.insert(END, grape[zelda - 1][5])
            Qwindows.grid(row=6, column=1)
            Qwindows_label = Label(QaddRoom_RoomsFrame, text = "Windows").grid(row=6, column=0)           

    # Desk text widget
            Qdesk=Text(QaddRoom_RoomsFrame, width=20, height=1)
            Qdesk.insert(END, grape[zelda - 1][6])
            Qdesk.grid(row=7, column=1)
            QDesk_label = Label(QaddRoom_RoomsFrame, text = "Desk").grid(row=7, column=0)            

    # Tables text widget
            Qtables=Text(QaddRoom_RoomsFrame, width=20, height=1)
            Qtables.insert(END, grape[zelda - 1][7])
            Qtables.grid(row=8, column=1)
            Qtable_label = Label(QaddRoom_RoomsFrame, text = "Tables").grid(row=8, column=0)  

            Qchairs=Text(QaddRoom_RoomsFrame, width=20, height=1)
            Qchairs.insert(END, grape[zelda - 1][8])
            Qchairs.grid(row=9, column=1)
            Qchairs_label = Label(QaddRoom_RoomsFrame, text = "Chairs").grid(row=9, column=0)

            Qchalkwhiteboard=Text(QaddRoom_RoomsFrame, width=20, height=1)
            Qchalkwhiteboard.insert(END, grape[zelda - 1][9])
            Qchalkwhiteboard.grid(row=10, column=1)
            Qchalkwhiteboard_label = Label(QaddRoom_RoomsFrame, text = "Chalk/Whiteboards").grid(row=10, column=0)

            Qcomputers=Text(QaddRoom_RoomsFrame, width=20, height=1)
            Qcomputers.insert(END, grape[zelda - 1][10])
            Qcomputers.grid(row=11, column=1)
            Qcomputers_label = Label(QaddRoom_RoomsFrame, text = "Computers").grid(row=11, column=0)    

            Qrestrooms_label = Label(QaddRoom_RoomsFrame, text="Restrooms", font=BOLD).grid(columnspan=2, rowspan=2, row=12, column=0)  

            Qtoilets=Text(QaddRoom_RoomsFrame, width=20, height=1)
            Qtoilets.insert(END, grape[zelda - 1][11])
            Qtoilets.grid(row=14, column=1)
            Qtoilets_label = Label(QaddRoom_RoomsFrame, text = "Toilets").grid(row=14, column=0)

            Qurinals=Text(QaddRoom_RoomsFrame, width=20, height=1)
            Qurinals.insert(END, grape[zelda - 1][12])
            Qurinals.grid(row=15, column=1)
            Qurinals_label = Label(QaddRoom_RoomsFrame, text = "Urinals").grid(row=15, column=0)

            Qsinks=Text(QaddRoom_RoomsFrame, width=20, height=1)
            Qsinks.insert(END, grape[zelda - 1][13])
            Qsinks.grid(row=16, column=1)
            Qsinks_label = Label(QaddRoom_RoomsFrame, text = "Sinks").grid(row=16, column=0)

            Qmirrors=Text(QaddRoom_RoomsFrame, width=20, height=1)
            Qmirrors.insert(END, grape[zelda - 1][14])
            Qmirrors.grid(row=17, column=1)
            Qmirrors_label = Label(QaddRoom_RoomsFrame, text = "Mirrors").grid(row=17, column=0)

            Qhanddryers=Text(QaddRoom_RoomsFrame, width=20, height=1)
            Qhanddryers.insert(END, grape[zelda - 1][15])
            Qhanddryers.grid(row=18, column=1)
            Qhanddryers_label = Label(QaddRoom_RoomsFrame, text = "Hand Dryers").grid(row=18, column=0)

            Qshowerstubs=Text(QaddRoom_RoomsFrame, width=20, height=1)
            Qshowerstubs.insert(END, grape[zelda - 1][16])
            Qshowerstubs.grid(row=19, column=1)
            Qshowerstubs_label = Label(QaddRoom_RoomsFrame, text = "Showers/Tubs").grid(row=19, column=0)

            QRecepticals_label = Label(QaddRoom_RoomsFrame2, text="Recepticals", font=BOLD).grid(columnspan=2, rowspan=2, row=0, column=0)

            Qlargecan=Text(QaddRoom_RoomsFrame2, width=20, height=1)
            Qlargecan.insert(END, grape[zelda - 1][17])
            Qlargecan.grid(row=2, column=1)
            Qlargecan_label = Label(QaddRoom_RoomsFrame2, text = "Large Trash Can").grid(row=2, column=0)

            Qsmallcan=Text(QaddRoom_RoomsFrame2, width=20, height=1)
            Qsmallcan.insert(END, grape[zelda - 1][18])
            Qsmallcan.grid(row=3, column=1)
            Qsmallcan_label = Label(QaddRoom_RoomsFrame2, text = "Small Trash Can").grid(row=3, column=0)

            Qsaninap=Text(QaddRoom_RoomsFrame2, width=20, height=1)
            Qsaninap.insert(END, grape[zelda - 1][19])
            Qsaninap.grid(row=4, column=1)
            Qsaninap_label = Label(QaddRoom_RoomsFrame2, text = "Sanitary Napkin").grid(row=4, column=0)

            QDispensers_label = Label(QaddRoom_RoomsFrame2, text="Dispensers", font=BOLD).grid(columnspan=2, rowspan=2, row=5, column=0)

            Qtoiletpaperdis=Text(QaddRoom_RoomsFrame2, width=20, height=1)
            Qtoiletpaperdis.insert(END, grape[zelda - 1][20])
            Qtoiletpaperdis.grid(row=7, column=1)
            Qtoiletpaperdis_label = Label(QaddRoom_RoomsFrame2, text = "Toilet Paper").grid(row=7, column=0)

            Qpapertoweldis=Text(QaddRoom_RoomsFrame2, width=20, height=1)
            Qpapertoweldis.insert(END, grape[zelda - 1][21])
            Qpapertoweldis.grid(row=8, column=1)
            Qpapertoweldis_label = Label(QaddRoom_RoomsFrame2, text = "Paper Towel").grid(row=8, column=0)

            Qhandsoapdis=Text(QaddRoom_RoomsFrame2, width=20, height=1)
            Qhandsoapdis.insert(END, grape[zelda - 1][22])
            Qhandsoapdis.grid(row=9, column=1)
            Qhandsoapdis_label = Label(QaddRoom_RoomsFrame2, text = "Hand Soap").grid(row=9, column=0)

            Qhandsanidis=Text(QaddRoom_RoomsFrame2, width=20, height=1)
            Qhandsanidis.insert(END, grape[zelda - 1][23])
            Qhandsanidis.grid(row=10, column=1)
            Qhandsanidis_label = Label(QaddRoom_RoomsFrame2, text = "Hand Sanitizer").grid(row=10, column=0)

            Qseatcoverdis=Text(QaddRoom_RoomsFrame2, width=20, height=1)
            Qseatcoverdis.insert(END, grape[zelda - 1][24])
            Qseatcoverdis.grid(row=11, column=1)
            Qseatcoverdis_label = Label(QaddRoom_RoomsFrame2, text = "Toilet Seat Cover").grid(row=11, column=0)

            Misc_label = Label(QaddRoom_RoomsFrame2, text="Miscellaneous", font=BOLD).grid(columnspan=2, rowspan=2, row=12, column=0)

            Qwalkoffmat=Text(QaddRoom_RoomsFrame2, width=20, height=1)
            Qwalkoffmat.insert(END, grape[zelda - 1][25])
            Qwalkoffmat.grid(row=14, column=1)
            Qwalkoffmat_label = Label(QaddRoom_RoomsFrame2, text = "Walk Off Mats").grid(row=14, column=0)

            Qcafetables=Text(QaddRoom_RoomsFrame2, width=20, height=1)
            Qcafetables.insert(END, grape[zelda - 1][26])
            Qcafetables.grid(row=15, column=1)
            Qcafetables_label = Label(QaddRoom_RoomsFrame2, text = "Cafeteria Tables").grid(row=15, column=0)

            Qvendingmach=Text(QaddRoom_RoomsFrame2, width=20, height=1)
            Qvendingmach.insert(END, grape[zelda - 1][28])
            Qvendingmach.grid(row=16, column=1)
            Qvendingmach_label = Label(QaddRoom_RoomsFrame2, text = "Vending Machines").grid(row=16, column=0)

            Qbeds=Text(QaddRoom_RoomsFrame2, width=20, height=1)
            Qbeds.insert(END, grape[zelda - 1][27])
            Qbeds.grid(row=17, column=1)
            Qbeds_label = Label(QaddRoom_RoomsFrame2, text = "Beds").grid(row=17, column=0)

            b = Button(editRoomWin, text = "Add Edited Room", image = photo, bg="white", borderwidth=0, fg="white", command=Add_edited_data)
            b.grid(columnspan=2)

class Employee():

    def __init__(self, name, zone, wage):
        self.name = name
        self.zone = zone
        self.wage = wage

def Work_Loading():
        

    WLFrame = Frame(tab4, bg='pink')
    WLFrame.grid()

    EmployeeLabel = Label(WLFrame, text = 'Employees')
    EmployeeLabel.grid(row=0, column=0, columnspan=2)

    nameGUI=Text(WLFrame, width=20, height=1)
    nameGUI.insert(END, 0)
    nameGUI.grid(row=1, column=1)
    nameLabel = Label(WLFrame, text = "Name").grid(row=1, column=0)     

    zoneGUI=Text(WLFrame, width=20, height=1)
    zoneGUI.insert(END, 0)
    zoneGUI.grid(row=2, column=1)
    zoneLabel = Label(WLFrame, text = "Wage").grid(row=2, column=0)   

    wageGUI=Text(WLFrame, width=20, height=1)
    wageGUI.insert(END, 0)
    wageGUI.grid(row=3, column=1)
    wageLabel = Label(WLFrame, text = "Zone").grid(row=3, column=0)    

def Zones():
    pass

#Create a button to get the text input

global nimFrame1
global nim
global photo
global tab1
global tab2
global tab4
global Borking
global Borking2
global SWT2

# Create an instance of tkinter frame
nim=Tk()

background1 = PhotoImage(file = "/home/kinglyon976/Estimator1/background1.png")
photo = PhotoImage(file = "/home/kinglyon976/Estimator1/purpleButton.png")

nim.title("Tab Widget")
tabControl = ttk.Notebook(nim)
  
tab1 = Frame(tabControl, bg="pink")
tab2 = Frame(tabControl)
tab3 = Frame(tabControl)
tab4 = Frame(tabControl)

Borking = Canvas(tab2)
Borking.pack(side=LEFT, fill=BOTH, expand=1)

tabControl.add(tab1, text ='Dashboard')
tabControl.add(tab2, text ='Rooms')
tabControl.add(tab3, text ='Quick Estimator')
tabControl.add(tab4, text ='Work Loading')
tabControl.pack(expand = 1, fill=BOTH)

SWT2 = Scrollbar(tab2, bg="navy", orient=VERTICAL, command=Borking.yview)

nimFrame1 = Frame(tab1, bg="pink")
nimFrame1.pack(anchor=SW)

#Borking3 = Canvas(nimFrame1, bg="green")
#Borking3.pack(side=LEFT, fill=BOTH, expand=1)

# Set the geometry
nim.geometry("1200x600")

#background_Label = Label(nim, image = background1, justify=CENTER)
#background_Label.place(x=0, y=0, relwidth=1, relheight=1)
#background_Label.lower()

#main_label = Label(tab1, text="Estimator", font=("Ariel", 50))
#main_label.pack()

#ScrollTotals = Scrollbar(nimFrame1, orient=VERTICAL, command=Borking3.yview)

#SWT2._bound_to_mousewheel("<MouseWheel>")
#SWT2._configure_window(400)
SWT2.pack(side=RIGHT, fill=Y)

#ScrollTotals.pack(side=LEFT, fill=Y)

Borking.configure(yscrollcommand=SWT2.set)
Borking.bind("<Configure>", lambda e: Borking.configure(scrollregion=Borking.bbox('all')))

Borking2 = Frame(Borking)
Borking2.grid()

Borking.create_window((0,0), window=Borking2, anchor="nw")

#Borking3.configure(yscrollcommand=ScrollTotals.set)
#Borking3.bind("<Configure>", lambda f: Borking3.configure(scrollregion=Borking3.bbox('all')))

#Borking4 = Frame(Borking3, bg="orange")
#Borking4.pack()

#Borking3.create_window((0,0), window=Borking4, anchor="nw")

t = Button(tab2, text="Add Room", image=photo, borderwidth=0, command = Open_Add_Room_Window)
t.pack(side=RIGHT, padx=10, pady=10)

w = Button(tab1, text = "Update", image = photo, bg="pink", borderwidth=0, compound = CENTER, command = Surface_Addition)
w.pack(anchor=W)

#y = Button(nimFrame1, text = "Print", image = photo, bg="#d2bcdc", borderwidth=0, compound = CENTER, command = create_rooms_inTab2)
#y.pack(padx=10, pady=10)


create_rooms_inTab2()
Surface_Addition()

print(SurfaceNameListLength)

#print("Room Types" + str(roomTypeList))

PieFrame = Canvas(nimFrame1, bg='pink')
PieFrame.grid(row=1, column=6, rowspan=16)

BarFrame = Canvas(nimFrame1, bg='pink')
BarFrame.grid(row=1, column=7, rowspan=16)

PieFrame2 = Canvas(nimFrame1, bg='olive')
PieFrame2.grid(row=16, column=7, rowspan=16)

PieFrame3 = Canvas(nimFrame1, bg='grey')
PieFrame3.grid(row=16, column=6, rowspan=16)

def Chart_Chart():
    print(FSwT)

    Rose = 0

    VCTAmount = 0
    CarpetAmount = 0
    EstryAmount = 0
    RubberAmount = 0
    WoodAmount = 0

    for floor in FTwT:
        if floor == 'VCT':
            VCTAmount += FSwT[Rose]
        elif floor == 'Carpet':
            CarpetAmount += FSwT[Rose]
        elif floor == 'Estry':
            EstryAmount += FSwT[Rose]
        elif floor == 'Rubber':
            RubberAmount += FSwT[Rose]
        elif floor == 'Wood':
            WoodAmount += FSwT[Rose]
        else:
            continue

        Rose += 1

    FloorSizeAmounts = [VCTAmount, CarpetAmount, EstryAmount, RubberAmount, WoodAmount]

    print(FloorSizeAmounts)


    fig = plt.figure(figsize=(5,5), dpi=65, facecolor='pink')
    fig.set_size_inches(5,3.5)

    # create data
    
    #roomList = list(roomTypeList)

    names3 = ['Surfaces', 'Restrooms', 'Recepticals', 'Dispensers', 'Misc']
    colors2=['red','green','violet','skyblue','orange','pink','slateblue']

    # Create a circle at the center of the plot
    my_circle2 = plt.Circle( (0,0), 0.5, color='white')
    

    plt.pie(FloorSizeAmounts, colors=colors2, wedgeprops = { 'linewidth' : 7, 'edgecolor' : 'white' })
    plt.axis('equal')
    #plt.show(block=FALSE)
    p = plt.gcf()
    p.gca().add_artist(my_circle2)
    plt.ion()
    # Show the graph
    #plt.show(block=TRUE)
    PieCanvas3 = FigureCanvasTkAgg(fig, PieFrame3)
    PieCanvas3.draw()
    time.sleep(0.0001)
    PieCanvas3.get_tk_widget().pack(side=RIGHT, fill=BOTH, expand=1)

    red_patch = mpatches.Patch(color = 'red', label='VCT')
    green_patch = mpatches.Patch(color = 'green', label='Carpet')
    violet_patch = mpatches.Patch(color = 'violet', label='Estry')
    skyblue_patch = mpatches.Patch(color = 'skyblue', label='Rubber')
    orange_patch = mpatches.Patch(color = 'orange', label='Wood')
    

    time.sleep(0.0001)
    plt.title(label='Square Footage', fontsize=16)
    plt.legend(handles=[red_patch, green_patch, violet_patch, skyblue_patch, orange_patch])        #bbox_to_anchor=(1.05,1), loc='best', borderaxespad=0.)
    plt.close()

    print(FloorSizeAmounts)

    

def Pie_Plot2():

    global SurfaceList
    global TimeList

    NewList = []

    for list in SurfaceList:
       
        NewList.append(str(sum(list)))

    print(NewList)

    TotalsXTimes = []

    John = 0

    for item in NewList:
        TotalsXTimes.append((float(TimeList[John]) * int(NewList[John]) * Average_Wage))
        John += 1

    Surfaces = sum(TotalsXTimes[0:5])
    Restrooms = sum(TotalsXTimes[5:12])
    Recepticals = sum(TotalsXTimes[12:15])
    Dispensers = sum(TotalsXTimes[15:19])
    Misc = sum(TotalsXTimes[19:24])

    fig = plt.figure(figsize=(5,5), dpi=65, facecolor='pink')
    fig.set_size_inches(5,3.5)

    # create data
    SurfacesSurfaces = [Surfaces, Restrooms, Recepticals, Dispensers, Misc]
    #roomList = list(roomTypeList)

    names2 = ['Surfaces', 'Restrooms', 'Recepticals', 'Dispensers', 'Misc']
    colors2=['red','green','violet','skyblue','orange','pink','slateblue']

    # Create a circle at the center of the plot
    my_circle2 = plt.Circle( (0,0), 0.5, color='white')
    

    plt.pie(SurfacesSurfaces, colors=colors2, wedgeprops = { 'linewidth' : 7, 'edgecolor' : 'white' })
    plt.axis('equal')
    #plt.show(block=FALSE)
    p = plt.gcf()
    p.gca().add_artist(my_circle2)
    plt.ion()
    # Show the graph
    #plt.show(block=TRUE)
    PieCanvas2 = FigureCanvasTkAgg(fig, PieFrame2)
    PieCanvas2.draw()
    time.sleep(0.0001)
    PieCanvas2.get_tk_widget().pack(side=RIGHT, fill=BOTH, expand=1)

    red_patch = mpatches.Patch(color = 'red', label='Surfaces')
    green_patch = mpatches.Patch(color = 'green', label='Restrooms')
    violet_patch = mpatches.Patch(color = 'violet', label='Recepticals')
    skyblue_patch = mpatches.Patch(color = 'skyblue', label='Dispensers')
    orange_patch = mpatches.Patch(color = 'orange', label='Misc')
    

    time.sleep(0.0001)
    plt.title(label='Area Cost', fontsize=16)
    plt.legend(handles=[red_patch, green_patch, violet_patch, skyblue_patch, orange_patch])        #bbox_to_anchor=(1.05,1), loc='best', borderaxespad=0.)
    plt.close()

def Bar_Plot():
    
    fred=0
    VCT = 0
    Carpet = 0
    Estry = 0
    Rubber = 0
    Wood = 0
    for floor in FTwT:
        
        fred += 1

        if floor == 'VCT':
            VCT += 1
        elif floor == 'Carpet':
            Carpet += 1
        elif floor == 'Estry':
            Estry += 1
        elif floor == 'Rubber':
            Rubber += 1
        elif floor == 'Wood':
            Wood += 1
        else:
            continue

    FloorTypeList = [VCT, Carpet, Estry, Rubber, Wood]

    f = Figure(figsize=(5,4), dpi=65, facecolor='pink')
    ax = f.add_subplot(111)
    
    ind = ['VCT', 'Carpet', 'Estry', 'Rubber', 'Wood']  
    width = .5

    colors2=['red','green','blue','skyblue','orange','pink','slateblue']

    rects1 = ax.bar(ind, FloorTypeList, color=colors2)

    canvas = FigureCanvasTkAgg(f, master=BarFrame)
    canvas.draw()
    time.sleep(0.0001)
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    time.sleep(0.0001)
    


def Donut_Plot():

    global colors2

    fig = plt.figure(figsize=(5,5), dpi=65, facecolor='pink')
    fig.set_size_inches(5,3.5)

    # create data
    roomTypeList = (Classroom, Restroom, Hallway, Lobby, Office, Gym, Cafeteria)
    nack = 0
    roomList = list(roomTypeList)

    names = ['Classroom', 'Restroom', 'Hallway', 'Lobby', 'Office', 'Gym', 'Cafeteria']
    colors2=['red','green','blue','skyblue','orange','pink','slateblue']

    # Create a circle at the center of the plot
    my_circle = plt.Circle( (0,0), 0.5, color='white')

    plt.pie(roomTypeList, colors=colors2, wedgeprops = { 'linewidth' : 7, 'edgecolor' : 'white' })
    plt.axis('equal')
    #plt.show(block=FALSE)
    p = plt.gcf()
    p.gca().add_artist(my_circle)
    plt.ion()
    # Show the graph
    #plt.show(block=TRUE)
    PieCanvas = FigureCanvasTkAgg(fig, PieFrame)
    PieCanvas.draw()
    time.sleep(0.0001)
    PieCanvas.get_tk_widget().pack(side=RIGHT, fill=BOTH, expand=1)

    red_patch = mpatches.Patch(color = 'red', label='Classroom')
    green_patch = mpatches.Patch(color = 'green', label='Restroom')
    blue_patch = mpatches.Patch(color = 'blue', label='Hallway')
    skyblue_patch = mpatches.Patch(color = 'skyblue', label='Lobby')
    orange_patch = mpatches.Patch(color = 'orange', label='Office')
    pink_patch = mpatches.Patch(color = 'pink', label='Gym')
    slateblue_patch = mpatches.Patch(color = 'slateblue', label='Cafeteria')

    plt.title(label='Area Type', fontsize=16)
    time.sleep(0.0001)
    plt.legend(handles=[red_patch, green_patch, blue_patch, skyblue_patch, orange_patch, pink_patch, slateblue_patch])        #bbox_to_anchor=(1.05,1), loc='best', borderaxespad=0.)
    plt.close()


Work_Loading()
Chart_Chart()    
Pie_Plot2()
Bar_Plot()    
Donut_Plot()
Pullroom_windows()
nim.mainloop()


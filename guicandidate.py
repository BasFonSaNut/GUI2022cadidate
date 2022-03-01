#! /usr/bin/env python
#  -*- coding: utf-8 -*-

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import guicandidate_action

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1199x610+-76+373")
        top.minsize(120, 1)
        top.maxsize(1200, 768)
        top.resizable(1,  1)
        top.title("Toplevel 0")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top
        self.CidVar = tk.StringVar()
        self.FullnameVar = tk.StringVar()
        self.BdateVar = tk.StringVar()
        self.RdateVar = tk.StringVar()
        self.BtimeVar = tk.StringVar()
        self.RtimeVar = tk.StringVar()
        self.ExtratimeVar = tk.StringVar()
        self.ExtrachargeVar = tk.StringVar()
        self.CidSearchVar = tk.StringVar()
        self.selectedButton = tk.IntVar()

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.008, rely=0.016, relheight=0.926
                , relwidth=0.148)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Button_cowtransaction = tk.Button(self.Frame1)
        self.Button_cowtransaction.place(relx=0.051, rely=0.018, height=144
                , width=147)
        self.Button_cowtransaction.configure(activebackground="#ececec")
        self.Button_cowtransaction.configure(activeforeground="#000000")
        self.Button_cowtransaction.configure(background="#00ff80")
        self.Button_cowtransaction.configure(command=guicandidate_action.makeCowtransaction)
        self.Button_cowtransaction.configure(compound='top')
        self.Button_cowtransaction.configure(disabledforeground="#a3a3a3")
        self.Button_cowtransaction.configure(font="-family {AngsanaUPC} -size 20 -weight bold")
        self.Button_cowtransaction.configure(foreground="#0000ff")
        self.Button_cowtransaction.configure(highlightbackground="#ffffff")
        self.Button_cowtransaction.configure(highlightcolor="black")
        photo_location = "./images/GuiCandidate/cow.png"
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.Button_cowtransaction.configure(image=_img0)
        self.Button_cowtransaction.configure(pady="0")
        self.Button_cowtransaction.configure(text='''ยืมวัว''')

        self.Button_bufftransaction = tk.Button(self.Frame1)
        self.Button_bufftransaction.place(relx=0.056, rely=0.301, height=144
                , width=147)
        self.Button_bufftransaction.configure(activebackground="#ececec")
        self.Button_bufftransaction.configure(activeforeground="#000000")
        self.Button_bufftransaction.configure(background="#ff80c0")
        self.Button_bufftransaction.configure(command=guicandidate_action.makeBuffalotran)
        self.Button_bufftransaction.configure(compound='top')
        self.Button_bufftransaction.configure(disabledforeground="#a3a3a3")
        self.Button_bufftransaction.configure(font="-family {AngsanaUPC} -size 20 -weight bold")
        self.Button_bufftransaction.configure(foreground="#0000ff")
        self.Button_bufftransaction.configure(highlightbackground="#ffffff")
        self.Button_bufftransaction.configure(highlightcolor="black")
        photo_location = "./images/GuiCandidate/buff1.png"
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        self.Button_bufftransaction.configure(image=_img1)
        self.Button_bufftransaction.configure(pady="0")
        self.Button_bufftransaction.configure(text='''ยืมควาย''')

        self.Button_createDb = tk.Button(self.Frame1)
        self.Button_createDb.place(relx=0.056, rely=0.584, height=144, width=147)
        self.Button_createDb.configure(activebackground="#ececec")
        self.Button_createDb.configure(activeforeground="#000000")
        self.Button_createDb.configure(background="#55aaff")
        self.Button_createDb.configure(command=guicandidate_action.createDb)
        self.Button_createDb.configure(compound='top')
        self.Button_createDb.configure(disabledforeground="#a3a3a3")
        self.Button_createDb.configure(font="-family {AngsanaUPC} -size 20 -weight bold")
        self.Button_createDb.configure(foreground="#0000ff")
        self.Button_createDb.configure(highlightbackground="#ffffff")
        self.Button_createDb.configure(highlightcolor="black")
        photo_location = "./images/GuiCandidate/transaction.png"
        global _img2
        _img2 = tk.PhotoImage(file=photo_location)
        self.Button_createDb.configure(image=_img2)
        self.Button_createDb.configure(pady="0")
        self.Button_createDb.configure(text='''สร้างฐานข้อมูล''')

        self.Button_exit = tk.Button(self.Frame1)
        self.Button_exit.place(relx=0.056, rely=0.85, height=74, width=147)
        self.Button_exit.configure(activebackground="#ececec")
        self.Button_exit.configure(activeforeground="#000000")
        self.Button_exit.configure(background="#7373b9")
        self.Button_exit.configure(command=guicandidate_action.exitProgram)
        self.Button_exit.configure(compound='top')
        self.Button_exit.configure(disabledforeground="#a3a3a3")
        self.Button_exit.configure(font="-family {AngsanaUPC} -size 20 -weight bold")
        self.Button_exit.configure(foreground="#0000ff")
        self.Button_exit.configure(highlightbackground="#ffffff")
        self.Button_exit.configure(highlightcolor="black")
        photo_location = "./images/GuiCandidate/exit.png"
        global _img3
        _img3 = tk.PhotoImage(file=photo_location)
        self.Button_exit.configure(image=_img3)
        self.Button_exit.configure(pady="0")
        self.Button_exit.configure(text='''ออก''')

        self.Frame2 = tk.Frame(self.top)
        self.Frame2.place(relx=0.158, rely=0.066, relheight=0.27, relwidth=0.823)

        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#d9d9d9")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")

        self.Label_cid = tk.Label(self.Frame2)
        self.Label_cid.place(relx=0.01, rely=0.061, height=40, width=113)
        self.Label_cid.configure(activebackground="#f9f9f9")
        self.Label_cid.configure(activeforeground="black")
        self.Label_cid.configure(background="#d9d9d9")
        self.Label_cid.configure(compound='left')
        self.Label_cid.configure(disabledforeground="#a3a3a3")
        self.Label_cid.configure(font="-family {AngsanaUPC} -size 21 -weight bold")
        self.Label_cid.configure(foreground="#000000")
        self.Label_cid.configure(highlightbackground="#d9d9d9")
        self.Label_cid.configure(highlightcolor="black")
        self.Label_cid.configure(justify='right')
        self.Label_cid.configure(relief="ridge")
        self.Label_cid.configure(text='''บัตรประชาชน''')

        self.Entry_cid = tk.Entry(self.Frame2)
        self.Entry_cid.place(relx=0.142, rely=0.061, height=40, relwidth=0.203)
        self.Entry_cid.configure(background="#f4fff4")
        self.Entry_cid.configure(disabledforeground="#a3a3a3")
        self.Entry_cid.configure(font="-family {AngsanaUPC} -size 20")
        self.Entry_cid.configure(foreground="#000000")
        self.Entry_cid.configure(highlightbackground="#d9d9d9")
        self.Entry_cid.configure(highlightcolor="black")
        self.Entry_cid.configure(insertbackground="black")
        self.Entry_cid.configure(selectbackground="blue")
        self.Entry_cid.configure(selectforeground="white")
        self.Entry_cid.configure(textvariable=self.CidVar)

        self.Label_4suffix = tk.Label(self.Frame2)
        self.Label_4suffix.place(relx=0.344, rely=0.061, height=40, width=63)
        self.Label_4suffix.configure(activebackground="#f9f9f9")
        self.Label_4suffix.configure(activeforeground="black")
        self.Label_4suffix.configure(background="#d9d9d9")
        self.Label_4suffix.configure(compound='left')
        self.Label_4suffix.configure(disabledforeground="#a3a3a3")
        self.Label_4suffix.configure(font="-family {AngsanaUPC} -size 21 -weight bold")
        self.Label_4suffix.configure(foreground="#000000")
        self.Label_4suffix.configure(highlightbackground="#d9d9d9")
        self.Label_4suffix.configure(highlightcolor="black")
        self.Label_4suffix.configure(justify='right')
        self.Label_4suffix.configure(relief="ridge")
        self.Label_4suffix.configure(text='''9999''')

        self.Label_fullname = tk.Label(self.Frame2)
        self.Label_fullname.place(relx=0.01, rely=0.364, height=40, width=113)
        self.Label_fullname.configure(activebackground="#f9f9f9")
        self.Label_fullname.configure(activeforeground="black")
        self.Label_fullname.configure(background="#d9d9d9")
        self.Label_fullname.configure(compound='left')
        self.Label_fullname.configure(disabledforeground="#a3a3a3")
        self.Label_fullname.configure(font="-family {AngsanaUPC} -size 21 -weight bold")
        self.Label_fullname.configure(foreground="#000000")
        self.Label_fullname.configure(highlightbackground="#d9d9d9")
        self.Label_fullname.configure(highlightcolor="black")
        self.Label_fullname.configure(justify='right')
        self.Label_fullname.configure(relief="ridge")
        self.Label_fullname.configure(text='''ชื่อ-สกุล''')

        self.Entry_fullname = tk.Entry(self.Frame2)
        self.Entry_fullname.place(relx=0.142, rely=0.364, height=40
                , relwidth=0.263)
        self.Entry_fullname.configure(background="white")
        self.Entry_fullname.configure(disabledforeground="#a3a3a3")
        self.Entry_fullname.configure(font="TkFixedFont")
        self.Entry_fullname.configure(foreground="#000000")
        self.Entry_fullname.configure(highlightbackground="#d9d9d9")
        self.Entry_fullname.configure(highlightcolor="black")
        self.Entry_fullname.configure(insertbackground="black")
        self.Entry_fullname.configure(selectbackground="blue")
        self.Entry_fullname.configure(selectforeground="white")
        self.Entry_fullname.configure(textvariable=self.FullnameVar)

        self.Label_borrowdate = tk.Label(self.Frame2)
        self.Label_borrowdate.place(relx=0.425, rely=0.061, height=40, width=105)

        self.Label_borrowdate.configure(activebackground="#f9f9f9")
        self.Label_borrowdate.configure(activeforeground="black")
        self.Label_borrowdate.configure(background="#d9d9d9")
        self.Label_borrowdate.configure(compound='left')
        self.Label_borrowdate.configure(disabledforeground="#a3a3a3")
        self.Label_borrowdate.configure(font="-family {AngsanaUPC} -size 21 -weight bold")
        self.Label_borrowdate.configure(foreground="#000000")
        self.Label_borrowdate.configure(highlightbackground="#d9d9d9")
        self.Label_borrowdate.configure(highlightcolor="black")
        self.Label_borrowdate.configure(justify='right')
        self.Label_borrowdate.configure(relief="ridge")
        self.Label_borrowdate.configure(text='''วันที่ยืม''')

        self.Entry_borrowdate = tk.Entry(self.Frame2)
        self.Entry_borrowdate.place(relx=0.536, rely=0.061, height=40
                , relwidth=0.203)
        self.Entry_borrowdate.configure(background="white")
        self.Entry_borrowdate.configure(disabledforeground="#a3a3a3")
        self.Entry_borrowdate.configure(font="-family {AngsanaUPC} -size 20")
        self.Entry_borrowdate.configure(foreground="#000000")
        self.Entry_borrowdate.configure(highlightbackground="#d9d9d9")
        self.Entry_borrowdate.configure(highlightcolor="black")
        self.Entry_borrowdate.configure(insertbackground="black")
        self.Entry_borrowdate.configure(selectbackground="blue")
        self.Entry_borrowdate.configure(selectforeground="white")
        self.Entry_borrowdate.configure(textvariable=self.BdateVar)

        self.Label_returndate = tk.Label(self.Frame2)
        self.Label_returndate.place(relx=0.425, rely=0.364, height=40
                , width=104)
        self.Label_returndate.configure(activebackground="#f9f9f9")
        self.Label_returndate.configure(activeforeground="black")
        self.Label_returndate.configure(background="#d9d9d9")
        self.Label_returndate.configure(compound='left')
        self.Label_returndate.configure(disabledforeground="#a3a3a3")
        self.Label_returndate.configure(font="-family {AngsanaUPC} -size 21 -weight bold")
        self.Label_returndate.configure(foreground="#000000")
        self.Label_returndate.configure(highlightbackground="#d9d9d9")
        self.Label_returndate.configure(highlightcolor="black")
        self.Label_returndate.configure(justify='right')
        self.Label_returndate.configure(relief="ridge")
        self.Label_returndate.configure(text='''วันที่คืน''')

        self.Entry_returndate = tk.Entry(self.Frame2)
        self.Entry_returndate.place(relx=0.536, rely=0.364, height=40
                , relwidth=0.203)
        self.Entry_returndate.configure(background="white")
        self.Entry_returndate.configure(disabledforeground="#a3a3a3")
        self.Entry_returndate.configure(font="-family {AngsanaUPC} -size 20")
        self.Entry_returndate.configure(foreground="#000000")
        self.Entry_returndate.configure(highlightbackground="#d9d9d9")
        self.Entry_returndate.configure(highlightcolor="black")
        self.Entry_returndate.configure(insertbackground="black")
        self.Entry_returndate.configure(selectbackground="blue")
        self.Entry_returndate.configure(selectforeground="white")
        self.Entry_returndate.configure(textvariable=self.RdateVar)

        self.Label_borrowtime = tk.Label(self.Frame2)
        self.Label_borrowtime.place(relx=0.769, rely=0.061, height=40, width=98)
        self.Label_borrowtime.configure(activebackground="#f9f9f9")
        self.Label_borrowtime.configure(activeforeground="black")
        self.Label_borrowtime.configure(background="#d9d9d9")
        self.Label_borrowtime.configure(compound='left')
        self.Label_borrowtime.configure(disabledforeground="#a3a3a3")
        self.Label_borrowtime.configure(font="-family {AngsanaUPC} -size 21 -weight bold")
        self.Label_borrowtime.configure(foreground="#000000")
        self.Label_borrowtime.configure(highlightbackground="#d9d9d9")
        self.Label_borrowtime.configure(highlightcolor="black")
        self.Label_borrowtime.configure(justify='right')
        self.Label_borrowtime.configure(relief="ridge")
        self.Label_borrowtime.configure(text='''เวลายืม''')

        self.Label_returntime = tk.Label(self.Frame2)
        self.Label_returntime.place(relx=0.769, rely=0.364, height=40, width=95)
        self.Label_returntime.configure(activebackground="#f9f9f9")
        self.Label_returntime.configure(activeforeground="black")
        self.Label_returntime.configure(background="#d9d9d9")
        self.Label_returntime.configure(compound='left')
        self.Label_returntime.configure(disabledforeground="#a3a3a3")
        self.Label_returntime.configure(font="-family {AngsanaUPC} -size 21 -weight bold")
        self.Label_returntime.configure(foreground="#000000")
        self.Label_returntime.configure(highlightbackground="#d9d9d9")
        self.Label_returntime.configure(highlightcolor="black")
        self.Label_returntime.configure(justify='right')
        self.Label_returntime.configure(relief="ridge")
        self.Label_returntime.configure(text='''เวลาคืน''')

        self.Entry_borrowtime = tk.Entry(self.Frame2)
        self.Entry_borrowtime.place(relx=0.881, rely=0.061, height=40
                , relwidth=0.101)
        self.Entry_borrowtime.configure(background="white")
        self.Entry_borrowtime.configure(disabledforeground="#a3a3a3")
        self.Entry_borrowtime.configure(font="-family {AngsanaUPC} -size 20")
        self.Entry_borrowtime.configure(foreground="#000000")
        self.Entry_borrowtime.configure(highlightbackground="#d9d9d9")
        self.Entry_borrowtime.configure(highlightcolor="black")
        self.Entry_borrowtime.configure(insertbackground="black")
        self.Entry_borrowtime.configure(selectbackground="blue")
        self.Entry_borrowtime.configure(selectforeground="white")
        self.Entry_borrowtime.configure(textvariable=self.BtimeVar)

        self.Entry_returntime = tk.Entry(self.Frame2)
        self.Entry_returntime.place(relx=0.881, rely=0.364, height=40
                , relwidth=0.101)
        self.Entry_returntime.configure(background="white")
        self.Entry_returntime.configure(disabledforeground="#a3a3a3")
        self.Entry_returntime.configure(font="-family {AngsanaUPC} -size 20")
        self.Entry_returntime.configure(foreground="#000000")
        self.Entry_returntime.configure(highlightbackground="#d9d9d9")
        self.Entry_returntime.configure(highlightcolor="black")
        self.Entry_returntime.configure(insertbackground="black")
        self.Entry_returntime.configure(selectbackground="blue")
        self.Entry_returntime.configure(selectforeground="white")
        self.Entry_returntime.configure(textvariable=self.RtimeVar)

        self.Label_borrowhour = tk.Label(self.Frame2)
        self.Label_borrowhour.place(relx=0.769, rely=0.667, height=40, width=90)
        self.Label_borrowhour.configure(activebackground="#f9f9f9")
        self.Label_borrowhour.configure(activeforeground="black")
        self.Label_borrowhour.configure(background="#d9d9d9")
        self.Label_borrowhour.configure(compound='left')
        self.Label_borrowhour.configure(disabledforeground="#a3a3a3")
        self.Label_borrowhour.configure(font="-family {AngsanaUPC} -size 21 -weight bold")
        self.Label_borrowhour.configure(foreground="#000000")
        self.Label_borrowhour.configure(highlightbackground="#d9d9d9")
        self.Label_borrowhour.configure(highlightcolor="black")
        self.Label_borrowhour.configure(justify='right')
        self.Label_borrowhour.configure(relief="ridge")
        self.Label_borrowhour.configure(text='''ชม. ยืม''')

        self.Entry_borrowhour = tk.Entry(self.Frame2)
        self.Entry_borrowhour.place(relx=0.881, rely=0.667, height=40
                , relwidth=0.101)
        self.Entry_borrowhour.configure(background="white")
        self.Entry_borrowhour.configure(disabledforeground="#a3a3a3")
        self.Entry_borrowhour.configure(font="-family {AngsanaUPC} -size 20")
        self.Entry_borrowhour.configure(foreground="#000000")
        self.Entry_borrowhour.configure(highlightbackground="#d9d9d9")
        self.Entry_borrowhour.configure(highlightcolor="black")
        self.Entry_borrowhour.configure(insertbackground="black")
        self.Entry_borrowhour.configure(selectbackground="blue")
        self.Entry_borrowhour.configure(selectforeground="white")
        self.Entry_borrowhour.configure(textvariable=self.ExtratimeVar)

        self.Button_save = tk.Button(self.Frame2)
        self.Button_save.place(relx=0.142, rely=0.667, height=44, width=97)
        self.Button_save.configure(activebackground="#ececec")
        self.Button_save.configure(activeforeground="#000000")
        self.Button_save.configure(background="#00ff80")
        self.Button_save.configure(command=guicandidate_action.doTransaction)
        self.Button_save.configure(compound='left')
        self.Button_save.configure(disabledforeground="#a3a3a3")
        self.Button_save.configure(font="-family {AngsanaUPC} -size 15 -weight bold")
        self.Button_save.configure(foreground="#000000")
        self.Button_save.configure(highlightbackground="#d9d9d9")
        self.Button_save.configure(highlightcolor="black")
        self.Button_save.configure(pady="0")
        self.Button_save.configure(text='''บันทึกรายการ''')

        self.Button_calculatepayment = tk.Button(self.Frame2)
        self.Button_calculatepayment.place(relx=0.658, rely=0.667, height=44
                , width=97)
        self.Button_calculatepayment.configure(activebackground="#ececec")
        self.Button_calculatepayment.configure(activeforeground="#000000")
        self.Button_calculatepayment.configure(background="#00ff80")
        self.Button_calculatepayment.configure(command=guicandidate_action.doCancelreturn)
        self.Button_calculatepayment.configure(compound='left')
        self.Button_calculatepayment.configure(disabledforeground="#a3a3a3")
        self.Button_calculatepayment.configure(font="-family {AngsanaUPC} -size 15 -weight bold")
        self.Button_calculatepayment.configure(foreground="#000000")
        self.Button_calculatepayment.configure(highlightbackground="#d9d9d9")
        self.Button_calculatepayment.configure(highlightcolor="black")
        self.Button_calculatepayment.configure(pady="0")
        self.Button_calculatepayment.configure(text='''ยกเลิกการคืน''')

        self.Button_updatestatus = tk.Button(self.Frame2)
        self.Button_updatestatus.place(relx=0.304, rely=0.667, height=44
                , width=97)
        self.Button_updatestatus.configure(activebackground="#ececec")
        self.Button_updatestatus.configure(activeforeground="#000000")
        self.Button_updatestatus.configure(background="#3399ff")
        self.Button_updatestatus.configure(command=guicandidate_action.doReturn)
        self.Button_updatestatus.configure(compound='left')
        self.Button_updatestatus.configure(disabledforeground="#a3a3a3")
        self.Button_updatestatus.configure(font="-family {AngsanaUPC} -size 15 -weight bold")
        self.Button_updatestatus.configure(foreground="#000000")
        self.Button_updatestatus.configure(highlightbackground="#d9d9d9")
        self.Button_updatestatus.configure(highlightcolor="black")
        self.Button_updatestatus.configure(pady="0")
        self.Button_updatestatus.configure(text='''ทำรายการคืน''')

        self.Label_payment = tk.Label(self.Frame2)
        self.Label_payment.place(relx=0.425, rely=0.667, height=40
                , width=104)
        self.Label_payment.configure(activebackground="#f9f9f9")
        self.Label_payment.configure(activeforeground="black")
        self.Label_payment.configure(background="#d9d9d9")
        self.Label_payment.configure(compound='left')
        self.Label_payment.configure(disabledforeground="#a3a3a3")
        self.Label_payment.configure(font="-family {AngsanaUPC} -size 21 -weight bold")
        self.Label_payment.configure(foreground="#000000")
        self.Label_payment.configure(highlightbackground="#d9d9d9")
        self.Label_payment.configure(highlightcolor="black")
        self.Label_payment.configure(justify='right')
        self.Label_payment.configure(relief="ridge")
        self.Label_payment.configure(text='''ชำระ''')

        self.Entry_payment = tk.Entry(self.Frame2)
        self.Entry_payment.place(relx=0.536, rely=0.667, height=40
                , relwidth=0.111)
        self.Entry_payment.configure(background="white")
        self.Entry_payment.configure(disabledforeground="#a3a3a3")
        self.Entry_payment.configure(font="-family {AngsanaUPC} -size 20")
        self.Entry_payment.configure(foreground="#000000")
        self.Entry_payment.configure(highlightbackground="#d9d9d9")
        self.Entry_payment.configure(highlightcolor="black")
        self.Entry_payment.configure(insertbackground="black")
        self.Entry_payment.configure(selectbackground="blue")
        self.Entry_payment.configure(selectforeground="white")
        self.Entry_payment.configure(textvariable=self.ExtrachargeVar)

        self.Button_delete = tk.Button(self.Frame2)
        self.Button_delete.place(relx=0.243, rely=0.667, height=44, width=57)
        self.Button_delete.configure(activebackground="#ececec")
        self.Button_delete.configure(activeforeground="#000000")
        self.Button_delete.configure(background="#ff80ff")
        self.Button_delete.configure(command=guicandidate_action.deleteTransaction)
        self.Button_delete.configure(compound='left')
        self.Button_delete.configure(disabledforeground="#a3a3a3")
        self.Button_delete.configure(font="-family {AngsanaUPC} -size 15 -weight bold")
        self.Button_delete.configure(foreground="#000000")
        self.Button_delete.configure(highlightbackground="#d9d9d9")
        self.Button_delete.configure(highlightcolor="black")
        self.Button_delete.configure(pady="0")
        self.Button_delete.configure(text='''ลบ''')

        self.TSeparator1 = ttk.Separator(self.Frame2)
        self.TSeparator1.place(relx=0.065, rely=0.612,  relheight=0.727)
        self.TSeparator1.configure(orient="vertical")

        self.Label_headerbar = tk.Label(self.top)
        self.Label_headerbar.place(relx=0.117, rely=-0.197, height=41, width=854)

        self.Label_headerbar.configure(activebackground="#f9f9f9")
        self.Label_headerbar.configure(activeforeground="black")
        self.Label_headerbar.configure(background="#6464ff")
        self.Label_headerbar.configure(compound='center')
        self.Label_headerbar.configure(disabledforeground="#a3a3a3")
        self.Label_headerbar.configure(font="-family {AngsanaUPC} -size 23 -weight bold")
        self.Label_headerbar.configure(foreground="#fff2f9")
        self.Label_headerbar.configure(highlightbackground="#d9d9d9")
        self.Label_headerbar.configure(highlightcolor="black")
        self.Label_headerbar.configure(relief="groove")
        self.Label_headerbar.configure(text='''โปรแกรม ยืม-คืน ไอ้โค ไอ้บือ''')

        self.Label_activedatetime = tk.Label(self.top)
        self.Label_activedatetime.place(relx=0.858, rely=0.0, height=41
                , width=164)
        self.Label_activedatetime.configure(activebackground="#f9f9f9")
        self.Label_activedatetime.configure(activeforeground="black")
        self.Label_activedatetime.configure(anchor='e')
        self.Label_activedatetime.configure(background="#2222ff")
        self.Label_activedatetime.configure(compound='left')
        self.Label_activedatetime.configure(disabledforeground="#a3a3a3")
        self.Label_activedatetime.configure(font="-family {AngsanaUPC} -size 21 -weight bold")
        self.Label_activedatetime.configure(foreground="#ffff00")
        self.Label_activedatetime.configure(highlightbackground="#d9d9d9")
        self.Label_activedatetime.configure(highlightcolor="black")
        self.Label_activedatetime.configure(justify='right')
        self.Label_activedatetime.configure(relief="ridge")
        self.Label_activedatetime.configure(text='''25-02-2022 | 15:15''')

        self.Frame3 = tk.Frame(self.top)
        self.Frame3.place(relx=0.158, rely=0.344, relheight=0.598
                , relwidth=0.822)
        self.Frame3.configure(relief='groove')
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief="groove")
        self.Frame3.configure(background="#d9d9d9")
        self.Frame3.configure(highlightbackground="#d9d9d9")
        self.Frame3.configure(highlightcolor="black")

        self.Frame4 = tk.Frame(self.Frame3)
        self.Frame4.place(relx=0.793, rely=0.0, relheight=0.91, relwidth=0.196)
        self.Frame4.configure(relief='groove')
        self.Frame4.configure(borderwidth="2")
        self.Frame4.configure(relief="groove")
        self.Frame4.configure(background="#d9d9d9")
        self.Frame4.configure(highlightbackground="#d9d9d9")
        self.Frame4.configure(highlightcolor="black")

        self.Label_search = tk.Label(self.Frame4)
        self.Label_search.place(relx=0.0, rely=0.0, height=44, width=196)
        self.Label_search.configure(activebackground="#f9f9f9")
        self.Label_search.configure(activeforeground="black")
        self.Label_search.configure(background="#6464ff")
        self.Label_search.configure(compound='left')
        self.Label_search.configure(disabledforeground="#a3a3a3")
        self.Label_search.configure(font="-family {AngsanaUPC} -size 21 -weight bold")
        self.Label_search.configure(foreground="#ffff00")
        self.Label_search.configure(highlightbackground="#d9d9d9")
        self.Label_search.configure(highlightcolor="black")
        self.Label_search.configure(justify='right')
        self.Label_search.configure(relief="ridge")
        self.Label_search.configure(text='''ค้นหา''')

        self.Label_cidsearch = tk.Label(self.Frame4)
        self.Label_cidsearch.place(relx=0.073, rely=0.163, height=45, width=167)
        self.Label_cidsearch.configure(activebackground="#f9f9f9")
        self.Label_cidsearch.configure(activeforeground="black")
        self.Label_cidsearch.configure(background="#d9d9d9")
        self.Label_cidsearch.configure(compound='left')
        self.Label_cidsearch.configure(disabledforeground="#a3a3a3")
        self.Label_cidsearch.configure(font="-family {AngsanaUPC} -size 21 -weight bold")
        self.Label_cidsearch.configure(foreground="#000000")
        self.Label_cidsearch.configure(highlightbackground="#d9d9d9")
        self.Label_cidsearch.configure(highlightcolor="black")
        self.Label_cidsearch.configure(justify='right')
        self.Label_cidsearch.configure(text='''บัตรประชาชน''')

        self.Entry_cidsearch = tk.Entry(self.Frame4)
        self.Entry_cidsearch.place(relx=0.104, rely=0.295, height=30
                , relwidth=0.798)
        self.Entry_cidsearch.configure(background="white")
        self.Entry_cidsearch.configure(disabledforeground="#a3a3a3")
        self.Entry_cidsearch.configure(font="TkFixedFont")
        self.Entry_cidsearch.configure(foreground="#000000")
        self.Entry_cidsearch.configure(highlightbackground="#d9d9d9")
        self.Entry_cidsearch.configure(highlightcolor="black")
        self.Entry_cidsearch.configure(insertbackground="black")
        self.Entry_cidsearch.configure(selectbackground="blue")
        self.Entry_cidsearch.configure(selectforeground="white")
        self.Entry_cidsearch.configure(textvariable=self.CidSearchVar)

        self.Button_search = tk.Button(self.Frame4)
        self.Button_search.place(relx=0.104, rely=0.425, height=96, width=65)
        self.Button_search.configure(activebackground="#ececec")
        self.Button_search.configure(activeforeground="#000000")
        self.Button_search.configure(anchor='sw')
        self.Button_search.configure(background="#00ff80")
        self.Button_search.configure(command=guicandidate_action.searchTransaction)
        self.Button_search.configure(compound='top')
        self.Button_search.configure(disabledforeground="#a3a3a3")
        self.Button_search.configure(font="-family {AngsanaUPC} -size 17 -weight bold")
        self.Button_search.configure(foreground="#000000")
        self.Button_search.configure(highlightbackground="#d9d9d9")
        self.Button_search.configure(highlightcolor="black")
        photo_location = "./images/GuiCandidate/search1.png"
        global _img4
        _img4 = tk.PhotoImage(file=photo_location)
        self.Button_search.configure(image=_img4)
        self.Button_search.configure(pady="0")
        self.Button_search.configure(text='''ค้นหา''')
        
        self.Button_export = tk.Button(self.Frame4)
        self.Button_export.place(relx=0.57, rely=0.425, height=96, width=65)
        self.Button_export.configure(activebackground="#ececec")
        self.Button_export.configure(activeforeground="#000000")
        self.Button_export.configure(anchor='sw')
        self.Button_export.configure(background="#ff80c0")
        self.Button_export.configure(command=guicandidate_action.export)
        self.Button_export.configure(compound='top')
        self.Button_export.configure(disabledforeground="#a3a3a3")
        self.Button_export.configure(font="-family {AngsanaUPC} -size 17 -weight bold")
        self.Button_export.configure(foreground="#000000")
        self.Button_export.configure(highlightbackground="#d9d9d9")
        self.Button_export.configure(highlightcolor="black")
        photo_location = "./images/GuiCandidate/export.png"
        global _img5
        _img5 = tk.PhotoImage(file=photo_location)
        self.Button_export.configure(image=_img5)
        self.Button_export.configure(pady="0")
        self.Button_export.configure(text='''ส่งออก''')

        self.Radiobutton_exportchoice = tk.Radiobutton(self.Frame4)
        self.Radiobutton_exportchoice.place(relx=0.104, rely=0.786, relheight=0.084
                , relwidth=0.301)
        self.Radiobutton_exportchoice.configure(activebackground="#ececec")
        self.Radiobutton_exportchoice.configure(activeforeground="#000000")
        self.Radiobutton_exportchoice.configure(anchor='w')
        self.Radiobutton_exportchoice.configure(background="#d9d9d9")
        self.Radiobutton_exportchoice.configure(compound='left')
        self.Radiobutton_exportchoice.configure(disabledforeground="#a3a3a3")
        self.Radiobutton_exportchoice.configure(font="-family {AngsanaUPC} -size 13 -weight bold")
        self.Radiobutton_exportchoice.configure(foreground="#000000")
        self.Radiobutton_exportchoice.configure(highlightbackground="#d9d9d9")
        self.Radiobutton_exportchoice.configure(highlightcolor="black")
        self.Radiobutton_exportchoice.configure(justify='left')
        self.Radiobutton_exportchoice.configure(text='''CSV''')
        self.Radiobutton_exportchoice.configure(variable=self.selectedButton)
        self.Radiobutton_exportchoice.configure(value=1)
        
        self.Radiobutton_exportchoice = tk.Radiobutton(self.Frame4)
        self.Radiobutton_exportchoice.place(relx=0.57, rely=0.786, relheight=0.084
                , relwidth=0.301)
        self.Radiobutton_exportchoice.configure(activebackground="#ececec")
        self.Radiobutton_exportchoice.configure(activeforeground="#000000")
        self.Radiobutton_exportchoice.configure(anchor='w')
        self.Radiobutton_exportchoice.configure(background="#d9d9d9")
        self.Radiobutton_exportchoice.configure(compound='left')
        self.Radiobutton_exportchoice.configure(disabledforeground="#a3a3a3")
        self.Radiobutton_exportchoice.configure(font="-family {AngsanaUPC} -size 13 -weight bold")
        self.Radiobutton_exportchoice.configure(foreground="#000000")
        self.Radiobutton_exportchoice.configure(highlightbackground="#d9d9d9")
        self.Radiobutton_exportchoice.configure(highlightcolor="black")
        self.Radiobutton_exportchoice.configure(justify='left')
        self.Radiobutton_exportchoice.configure(text='''JSON''')
        self.Radiobutton_exportchoice.configure(value=2)
        self.Radiobutton_exportchoice.configure(variable=self.selectedButton)
        
        self.Label_transactionitem = tk.Label(self.Frame3)
        self.Label_transactionitem.place(relx=0.0, rely=0.0, height=45
                , width=777)
        self.Label_transactionitem.configure(activebackground="#f9f9f9")
        self.Label_transactionitem.configure(activeforeground="black")
        self.Label_transactionitem.configure(background="#6464ff")
        self.Label_transactionitem.configure(compound='left')
        self.Label_transactionitem.configure(disabledforeground="#a3a3a3")
        self.Label_transactionitem.configure(font="-family {AngsanaUPC} -size 21 -weight bold")
        self.Label_transactionitem.configure(foreground="#ffff00")
        self.Label_transactionitem.configure(highlightbackground="#d9d9d9")
        self.Label_transactionitem.configure(highlightcolor="black")
        self.Label_transactionitem.configure(justify='right')
        self.Label_transactionitem.configure(relief="ridge")
        self.Label_transactionitem.configure(text='''รายการ''')

        self.style.configure('Treeview',  font="TkDefaultFont")
        self.Scrolledtreeview_transaction = ScrolledTreeView(self.Frame3)
        self.Scrolledtreeview_transaction.place(relx=0.01, rely=0.137
                , relheight=0.734, relwidth=0.761)
        self.Scrolledtreeview_transaction.configure(columns="Col1 Col2 Col3 Col4 Col5 Col6 Col7 Col8 Col9 Col10 Col11")
        # build_treeview_support starting.
        self.Scrolledtreeview_transaction.heading("#0",text="Tree")
        self.Scrolledtreeview_transaction.heading("#0",anchor="center")
        self.Scrolledtreeview_transaction.column("#0",width="49")
        self.Scrolledtreeview_transaction.column("#0",minwidth="20")
        self.Scrolledtreeview_transaction.column("#0",stretch="1")
        self.Scrolledtreeview_transaction.column("#0",anchor="w")
        
        self.Scrolledtreeview_transaction.heading("Col1",text="Id")
        self.Scrolledtreeview_transaction.heading("Col1",anchor="center")
        self.Scrolledtreeview_transaction.column("Col1",width="51")
        self.Scrolledtreeview_transaction.column("Col1",minwidth="20")
        self.Scrolledtreeview_transaction.column("Col1",stretch="1")
        self.Scrolledtreeview_transaction.column("Col1",anchor="w")
        
        self.Scrolledtreeview_transaction.heading("Col2",text="บัตรประชาชน")
        self.Scrolledtreeview_transaction.heading("Col2",anchor="center")
        self.Scrolledtreeview_transaction.column("Col2",width="51")
        self.Scrolledtreeview_transaction.column("Col2",minwidth="20")
        self.Scrolledtreeview_transaction.column("Col2",stretch="1")
        self.Scrolledtreeview_transaction.column("Col2",anchor="w")
        
        self.Scrolledtreeview_transaction.heading("Col3",text="ชื่อ-สกุล")
        self.Scrolledtreeview_transaction.heading("Col3",anchor="center")
        self.Scrolledtreeview_transaction.column("Col3",width="51")
        self.Scrolledtreeview_transaction.column("Col3",minwidth="20")
        self.Scrolledtreeview_transaction.column("Col3",stretch="1")
        self.Scrolledtreeview_transaction.column("Col3",anchor="w")
        
        
        self.Scrolledtreeview_transaction.heading("Col4",text="วันที่ยิม")
        self.Scrolledtreeview_transaction.heading("Col4",anchor="center")
        self.Scrolledtreeview_transaction.column("Col4",width="51")
        self.Scrolledtreeview_transaction.column("Col4",minwidth="20")
        self.Scrolledtreeview_transaction.column("Col4",stretch="1")
        self.Scrolledtreeview_transaction.column("Col4",anchor="w")
        
        self.Scrolledtreeview_transaction.heading("Col5",text="เวลายืม")
        self.Scrolledtreeview_transaction.heading("Col5",anchor="center")
        self.Scrolledtreeview_transaction.column("Col5",width="47")
        self.Scrolledtreeview_transaction.column("Col5",minwidth="20")
        self.Scrolledtreeview_transaction.column("Col5",stretch="1")
        self.Scrolledtreeview_transaction.column("Col5",anchor="w")
        
        self.Scrolledtreeview_transaction.heading("Col6",text="วันที่คืน")
        self.Scrolledtreeview_transaction.heading("Col6",anchor="center")
        self.Scrolledtreeview_transaction.column("Col6",width="51")
        self.Scrolledtreeview_transaction.column("Col6",minwidth="20")
        self.Scrolledtreeview_transaction.column("Col6",stretch="1")
        self.Scrolledtreeview_transaction.column("Col6",anchor="w")
        
        self.Scrolledtreeview_transaction.heading("Col7",text="เวลาคืน")
        self.Scrolledtreeview_transaction.heading("Col7",anchor="center")
        self.Scrolledtreeview_transaction.column("Col7",width="52")
        self.Scrolledtreeview_transaction.column("Col7",minwidth="20")
        self.Scrolledtreeview_transaction.column("Col7",stretch="1")
        self.Scrolledtreeview_transaction.column("Col7",anchor="w")
        
        self.Scrolledtreeview_transaction.heading("Col8",text="สิ่งที่ยืม")
        self.Scrolledtreeview_transaction.heading("Col8",anchor="center")
        self.Scrolledtreeview_transaction.column("Col8",width="73")
        self.Scrolledtreeview_transaction.column("Col8",minwidth="20")
        self.Scrolledtreeview_transaction.column("Col8",stretch="1")
        self.Scrolledtreeview_transaction.column("Col8",anchor="w")
        
        self.Scrolledtreeview_transaction.heading("Col9",text="ชม. ยืม")
        self.Scrolledtreeview_transaction.heading("Col9",anchor="center")
        self.Scrolledtreeview_transaction.column("Col9",width="84")
        self.Scrolledtreeview_transaction.column("Col9",minwidth="20")
        self.Scrolledtreeview_transaction.column("Col9",stretch="1")
        self.Scrolledtreeview_transaction.column("Col9",anchor="w")
        
        self.Scrolledtreeview_transaction.heading("Col10",text="ชำระ")
        self.Scrolledtreeview_transaction.heading("Col10",anchor="center")
        self.Scrolledtreeview_transaction.column("Col10",width="112")
        self.Scrolledtreeview_transaction.column("Col10",minwidth="20")
        self.Scrolledtreeview_transaction.column("Col10",stretch="1")
        self.Scrolledtreeview_transaction.column("Col10",anchor="w")
        
        self.Scrolledtreeview_transaction.heading("Col11",text="สถานะรายการ")
        self.Scrolledtreeview_transaction.heading("Col11",anchor="center")
        self.Scrolledtreeview_transaction.column("Col11",width="110")
        self.Scrolledtreeview_transaction.column("Col11",minwidth="20")
        self.Scrolledtreeview_transaction.column("Col11",stretch="1")
        self.Scrolledtreeview_transaction.column("Col11",anchor="w")

        self.Button_Edit = tk.Button(self.Frame3)
        self.Button_Edit.place(relx=0.01, rely=0.877, height=34, width=747)
        self.Button_Edit.configure(activebackground="#ececec")
        self.Button_Edit.configure(activeforeground="#000000")
        self.Button_Edit.configure(background="#ffff80")
        self.Button_Edit.configure(command=guicandidate_action.Button_EditClick)
        self.Button_Edit.configure(compound='left')
        self.Button_Edit.configure(disabledforeground="#a3a3a3")
        self.Button_Edit.configure(font="-family {AngsanaUPC} -size 19 -weight bold")
        self.Button_Edit.configure(foreground="#000000")
        self.Button_Edit.configure(highlightbackground="#d9d9d9")
        self.Button_Edit.configure(highlightcolor="black")
        self.Button_Edit.configure(pady="0")
        self.Button_Edit.configure(text='''แก้ไข''')

        self.Entry_tmpborrowtype = tk.Entry(self.Frame3)
        self.Entry_tmpborrowtype.place(relx=0.790, rely=0.832, height=20
                , relwidth=0.60)
        self.Entry_tmpborrowtype.configure(background="#d9d9d9")
        self.Entry_tmpborrowtype.configure(disabledforeground="#d9d9d9")
        self.Entry_tmpborrowtype.configure(font="TkFixedFont")
        self.Entry_tmpborrowtype.configure(foreground="#d9d9d9")
        self.Entry_tmpborrowtype.configure(insertbackground="#d9d9d9")
        self.Entry_tmpborrowtype.configure(relief="flat")
        
        self.Entry_tmpaction = tk.Entry(self.Frame3)
        self.Entry_tmpaction.place(relx=0.890, rely=0.832, height=20
                , relwidth=0.50)
        self.Entry_tmpaction.configure(background="#d9d9d9")
        self.Entry_tmpaction.configure(disabledforeground="#d9d9d9")
        self.Entry_tmpaction.configure(font="TkFixedFont")
        self.Entry_tmpaction.configure(foreground="#d9d9d9")
        self.Entry_tmpaction.configure(insertbackground="#d9d9d9")
        self.Entry_tmpaction.configure(relief="flat")
        
        self.Entry_tmpid = tk.Entry(self.Frame3)
        self.Entry_tmpid.place(relx=0.790, rely=0.932, height=20
                , relwidth=0.50)
        self.Entry_tmpid.configure(background="#d9d9d9")
        self.Entry_tmpid.configure(disabledforeground="#d9d9d9")
        self.Entry_tmpid.configure(font="TkFixedFont")
        self.Entry_tmpid.configure(foreground="#d9d9d9")
        self.Entry_tmpid.configure(insertbackground="#d9d9d9")
        self.Entry_tmpid.configure(relief="flat")

        self.Entry_tmpborrowstatus = tk.Entry(self.Frame3)
        self.Entry_tmpborrowstatus.place(relx=0.890, rely=0.932, height=20
                , relwidth=0.50)
        self.Entry_tmpborrowstatus.configure(background="#d9d9d9")
        self.Entry_tmpborrowstatus.configure(disabledforeground="#d9d9d9")
        self.Entry_tmpborrowstatus.configure(font="TkFixedFont")
        self.Entry_tmpborrowstatus.configure(foreground="#d9d9d9")
        self.Entry_tmpborrowstatus.configure(insertbackground="#d9d9d9")
        self.Entry_tmpborrowstatus.configure(relief="flat")
        
        self.Label_candidateInfo = tk.Label(self.top)
        self.Label_candidateInfo.place(relx=0.017, rely=0.951, height=21
                , width=1163)
        self.Label_candidateInfo.configure(activebackground="#f9f9f9")
        self.Label_candidateInfo.configure(activeforeground="black")
        self.Label_candidateInfo.configure(background="#f8adee")
        self.Label_candidateInfo.configure(compound='center')
        self.Label_candidateInfo.configure(disabledforeground="#a3a3a3")
        self.Label_candidateInfo.configure(font="-family {AngsanaUPC} -size 13 -weight bold")
        self.Label_candidateInfo.configure(foreground="#000000")
        self.Label_candidateInfo.configure(highlightbackground="#d9d9d9")
        self.Label_candidateInfo.configure(highlightcolor="black")
        self.Label_candidateInfo.configure(text='''น้องบาส ส่งเข้าประกวด โครงการ GUI 2022 : UngcleEngineer Bootcamp 2022''')

        self.Label_programname = tk.Label(self.top)
        self.Label_programname.place(relx=0.067, rely=-0.41, height=45
                , width=837)
        self.Label_programname.configure(activebackground="#f9f9f9")
        self.Label_programname.configure(activeforeground="black")
        self.Label_programname.configure(background="#6464ff")
        self.Label_programname.configure(compound='left')
        self.Label_programname.configure(disabledforeground="#a3a3a3")
        self.Label_programname.configure(font="-family {AngsanaUPC} -size 21 -weight bold")
        self.Label_programname.configure(foreground="#ffff00")
        self.Label_programname.configure(highlightbackground="#d9d9d9")
        self.Label_programname.configure(highlightcolor="black")
        self.Label_programname.configure(justify='right')
        self.Label_programname.configure(relief="ridge")
        self.Label_programname.configure(text='''โปรแกรม ยืม-คืน ไอ้โค ไอ้บือ''')

        self.Label_transactionitem_1 = tk.Label(self.top)
        self.Label_transactionitem_1.place(relx=0.158, rely=0.002, height=35
                , width=828)
        self.Label_transactionitem_1.configure(activebackground="#f9f9f9")
        self.Label_transactionitem_1.configure(activeforeground="black")
        self.Label_transactionitem_1.configure(background="#6464ff")
        self.Label_transactionitem_1.configure(compound='left')
        self.Label_transactionitem_1.configure(disabledforeground="#a3a3a3")
        self.Label_transactionitem_1.configure(font="-family {AngsanaUPC} -size 21 -weight bold")
        self.Label_transactionitem_1.configure(foreground="#ffff00")
        self.Label_transactionitem_1.configure(highlightbackground="#d9d9d9")
        self.Label_transactionitem_1.configure(highlightcolor="black")
        self.Label_transactionitem_1.configure(justify='right')
        self.Label_transactionitem_1.configure(relief="ridge")
        self.Label_transactionitem_1.configure(text='''โปรแกรมยืมคืน ไอ้โค ไอ้บือ''')

        
# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''
    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledTreeView(AutoScroll, ttk.Treeview):
    '''A standard ttk Treeview widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        ttk.Treeview.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')
def start_up():
    guicandidate_action.main()

if __name__ == '__main__':
    guicandidate_action.main()





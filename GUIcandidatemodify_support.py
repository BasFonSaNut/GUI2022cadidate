#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 7.3
#  in conjunction with Tcl version 8.6
#    Feb 26, 2022 12:15:32 PM +07  platform: Windows NT
#    Feb 26, 2022 12:29:43 PM +07  platform: Windows NT
#    Feb 26, 2022 04:56:02 PM +07  platform: Windows NT
#    Feb 26, 2022 05:15:04 PM +07  platform: Windows NT
#    Feb 27, 2022 01:42:29 PM +07  platform: Windows NT

from cgitb import text
from math import ceil
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
# for date interval
import pandas as pd
from datetime import datetime,timedelta
from tkinter import messagebox
# end for date interval

import GUIcandidatemodify
import sqlite3

def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = GUIcandidatemodify.Toplevel1(_top1)
    
    
    #set active date to current date
    todaydate = datetime.today()
    _w1.Label_activedatetime.config(text = todaydate.strftime("%d-%b-%Y"))
    _w1.Entry_borrowdate.insert(END,todaydate.strftime("%d-%b-%Y"))
    _w1.Entry_borrowtime.insert(END, todaydate.strftime("%H:%M"))
    
    # _w1.Scrolledtreeview_transaction.config(selectmode="none")
    #end set active date to current date
    
    root.mainloop()
    

def createdbSqlite(*args):
    print('GUIcandidatemodify_support.createdbSqlite')   
    conn = sqlite3.connect('1.db')
    print("เปิดฐานข้อมูลสำเร็จ")
    
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS borrowcowbuff
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        cid           TEXT    NOT NULL,
        fullname      TEXT    NOT NULL,
        borrowdate      CHAR(50)    NOT NULL,
        borrowtime      CHAR(50)    NOT NULL,
        returndate      CHAR(50),
        returntime      CHAR(50),
        borrowtype      CHAR(10),
        borrowhour      INTEGER     DEFAULT 0,
        payment         REAL        DEFAULT 0,
        borrowstatus    CHAR(50));''')
    
    conn.commit()  
    print("สร้างตารางสำเร็จ")     
    conn.close()


def calculatePayment():
    if(_w1.Entry_tmpid.get() ==''):
        tk.messagebox.askquestion(title='Warning', message='เลือกรายการจาก list กดแก้ไข ก่อนทำรายการใดๆ เสมอ \n ยกเว้นสร้างรายการใหม่')
    else:    
        date_1 = _w1.Entry_borrowdate.get()+' '+_w1.Entry_borrowtime.get()
        date_2 = _w1.Entry_returndate.get()+' '+_w1.Entry_returntime.get()
        date_format_str = '%d-%b-%Y %H:%M'
        start = datetime.strptime(date_1, date_format_str)
        end =   datetime.strptime(date_2, date_format_str)

        diff = end - start
        # Get interval between two timstamps in hours
        diff_in_hours = diff.total_seconds() / 3600
        
        
        borrowhour =  ceil(diff_in_hours)
        exactlyround = int((borrowhour / 5))
        extramin = ceil(borrowhour-(5*exactlyround))

        if(exactlyround<1):
            exactlyround:1
        else:
            exactlyround = exactlyround

        price = 0
        price = ((exactlyround * 500)+ (extramin * 100))
        # print(exactlyround,extramin,price)
      
        
        return (borrowhour,price)
    
def doReturn(*args):
    print('GUIcandidatemodify_support.doReturn')
    id = _w1.Entry_tmpid.get()
    borrowstatusTxt ='คืน'
    if(_w1.Entry_tmpid.get() ==''):
        tk.messagebox.askquestion(title='Warning', message='เลือกรายการจาก list กดแก้ไข ก่อนทำรายการใดๆ เสมอ \n ยกเว้นสร้างรายการใหม่')
    else:
        _w1.Entry_tmpborrowstatus.delete(0,END)
        _w1.Entry_tmpborrowstatus.insert(END, 'return')
           
        currentdate = datetime.today()
        returndate =  currentdate.strftime("%d-%b-%Y") 
        returntime = currentdate.strftime("%H:%M")
        
        _w1.Entry_returndate.delete(0,END)
        _w1.Entry_returndate.insert(END, returndate)
        
        _w1.Entry_returntime.delete(0,END)    
        _w1.Entry_returntime.insert(END, returntime)
        
        (borrowHour,Price) = calculatePayment()
        _w1.Entry_borrowhour.delete(0,END)    
        _w1.Entry_borrowhour.insert(END, borrowHour)
        _w1.Entry_payment.delete(0,END)
        _w1.Entry_payment.insert(END, Price) 
        
        MsgBox = tk.messagebox.askquestion ('Confirmation','ถ้าเห็นว่ายอดดังกล่าวถูกต้องแล้ว กด  yes ได้เลย',icon = 'warning')
        if MsgBox == 'yes':
            try:
                conn = sqlite3.connect('1.db')
                print("ติดต่อฐานข้อมูลสำเร็จ")
                c = conn.cursor()
                c.execute("UPDATE borrowcowbuff SET returndate =?, returntime =?, borrowhour=?, payment=?, borrowstatus = ?  \
                    WHERE id = ?",(returndate,returntime,borrowHour,Price,borrowstatusTxt,id,))
                conn.commit()  
                print("บันทึกการคืน สำเร็จ")     
                conn.close()
                
                if _w1.Entry_tmpborrowtype.get() == 'COW':
                    bindingTree(1)
                else:
                    bindingTree(2)        
                
                clearalldata() 
                _w1.Entry_tmpborrowstatus.delete(0,END)    
                _w1.Entry_tmpborrowstatus.insert(END, 'borrow')
                
            except sqlite3.Error as err:
                print(err) 
        else:
            tk.messagebox.showinfo('Return','You will now return to the application screen')
        
        
        
    
def Button_EditClick(*args):
    print('GUIcandidatemodify_support.Button_EditClick')
    _w1.Entry_tmpaction.delete(0,END)
    _w1.Entry_tmpaction.insert(END, 'EDIT')
    
    curItem = _w1.Scrolledtreeview_transaction.focus()
    selectedRow=_w1.Scrolledtreeview_transaction.item(curItem)
    
    # print(type(selectedRow))
    values=selectedRow.get('values')
    # print(values[0],values[1],values[2],values[3],values[4])
    id = values[0]
    cid = str(values[1])
    res = cid.partition('9999')[0]
    cid =  res
    fullname        = values[2]
    borrowdate      = values[3]
    borrowtime      = values[4]
    returndate      = values[5]
    returntime      = values[6]
    borrowtype      = values[7]
    borrowhour      = values[8]
    payment         = values[9]
    borrowstatus    = values[10]
   
    _w1.Entry_tmpid.delete(0,END)
    _w1.Entry_tmpid.insert(END, id)
     
    _w1.Entry_cid.delete(0,END)
    _w1.Entry_cid.insert(END, cid)
    
    _w1.Entry_fullname.delete(0,END)
    _w1.Entry_fullname.insert(END, fullname)
    
    _w1.Entry_borrowdate.delete(0,END)
    _w1.Entry_borrowdate.insert(END, borrowdate)
    
    _w1.Entry_borrowtime.delete(0,END)
    _w1.Entry_borrowtime.insert(END, borrowtime)

    _w1.Entry_returndate.delete(0,END)
    _w1.Entry_returndate.insert(END, returndate)
    
    _w1.Entry_returntime.delete(0,END)
    _w1.Entry_returntime.insert(END, returntime)
    
    _w1.Entry_tmpborrowtype.delete(0,END)
    _w1.Entry_tmpborrowtype.insert(END, borrowtype)
 
    _w1.Entry_borrowhour.delete(0,END)
    _w1.Entry_borrowhour.insert(END, borrowhour)
    
    _w1.Entry_payment.delete(0,END)
    _w1.Entry_payment.insert(END, payment)
    
    if(borrowstatus =='ยืม'):
        borrowstatasTxt ='borrow'
    else:
        borrowstatasTxt ='return' 
               
    _w1.Entry_tmpborrowstatus.delete(0,END)
    _w1.Entry_tmpborrowstatus.insert(END, borrowstatasTxt)
    
    
    # for arg in args:
    #     print ('another arg:', arg)
    # sys.stdout.flush()
     
def doTransaction(*args):
    print('GUIcandidatemodify_support.doTransaction')
    borrowtype = _w1.Entry_tmpborrowtype.get()
    borrowstatus = _w1.Entry_tmpborrowstatus.get()
    borrowstatusTxt = ''
    
    if(borrowstatus =='borrow' or borrowstatus ==''):
        borrowstatusTxt ='ยืม'
    else:
        borrowstatusTxt ='คืน' 
    
    
        
    # print(borrowtype)
    if _w1.Entry_tmpaction.get() == 'EDIT':
        id= _w1.Entry_tmpid.get()
        cid = _w1.Entry_cid.get()+'9999'
        fullname    = _w1.Entry_fullname.get()
        borrowdate  =  _w1.Entry_borrowdate.get()
        borrowtime  = _w1.Entry_borrowtime.get()
        
        returndate  = _w1.Entry_returndate.get()
        returntime  = _w1.Entry_returntime.get()            
        
        borrowhour  = _w1.Entry_borrowhour.get()
        payment     = _w1.Entry_payment.get()
        if(_w1.Entry_tmpid.get() ==''):
            tk.messagebox.askquestion(title='Warning', message='เลือกรายการจาก list กดแก้ไข ก่อนทำรายการใดๆ เสมอ \n ยกเว้นสร้างรายการใหม่')
        else:
            try:
                conn = sqlite3.connect('1.db')
                print("ติดต่อฐานข้อมูลสำเร็จ")
                c = conn.cursor()
                c.execute("UPDATE borrowcowbuff SET cid = ?,fullname =? ,borrowdate =? ,borrowtime =?, \
                    returndate=?,returntime=?,borrowhour=?,payment=?,borrowstatus = ?,borrowtype =?  \
                    WHERE id = ?",(cid,fullname,borrowdate,borrowtime,returndate,returntime,borrowhour,payment,borrowstatusTxt,borrowtype,id,))
                conn.commit()  
                print("แก้ไขข้อมูล สำเร็จ")     
                conn.close()
            except sqlite3.Error as err:
                print(err) 
    else:
        currentdate = datetime.today()
        cid = _w1.Entry_cid.get()+'9999'
        fullname = _w1.Entry_fullname.get()
        borrowdate =  currentdate.strftime("%d-%b-%Y") 
        borrowtime = currentdate.strftime("%H:%M")
        
        if(_w1.Entry_cid.get() =='' and _w1.Entry_fullname.get() == ''):
            tk.messagebox.askquestion(title='Warning', message='เลขที่บัตรประชาชน 9 หลักแรก และชื่อ ต้องมี')
        else:   
            try:
                conn = sqlite3.connect('1.db')
                print("ติดต่อฐานข้อมูลสำเร็จ")
                c = conn.cursor()
                c.execute("INSERT INTO borrowcowbuff (cid,fullname,borrowdate,borrowtime,borrowstatus,borrowtype) \
                    VALUES (?,?,?,?,?,?);", (cid,fullname,borrowdate,borrowtime,'ยืม',borrowtype,))
                conn.commit()  
                print("สร้างเรคคอร์ด สำเร็จ")     
                conn.close()
            except sqlite3.Error as err:
                print(err)    
                
        if _w1.Entry_tmpborrowtype.get() == 'COW':
            bindingTree(1)
        else:
            bindingTree(2)        
        
        clearalldata()        
    # for arg in args:
    #     print ('another arg:', arg)
    # sys.stdout.flush()


    
def clearalldata():
    _w1.Entry_tmpaction.delete(0,END)
    _w1.Entry_tmpaction.insert(END, '')
    
    _w1.Entry_tmpid.delete(0,END)
    _w1.Entry_tmpid.insert(END, '')
     
    _w1.Entry_cid.delete(0,END)
    _w1.Entry_cid.insert(END, '')
    
    _w1.Entry_fullname.delete(0,END)
    _w1.Entry_fullname.insert(END, '')
    
    _w1.Entry_returndate.delete(0,END)
    _w1.Entry_returndate.insert(END, '')
    
    _w1.Entry_returntime.delete(0,END)
    _w1.Entry_returntime.insert(END, '')
    
    _w1.Entry_borrowhour.delete(0,END)
    _w1.Entry_borrowhour.insert(END, '')
    
    _w1.Entry_payment.delete(0,END)
    _w1.Entry_payment.insert(END, '')
        
def deleteTransaction(*args):
    print('GUIcandidatemodify_support.deleteTransaction')
    if(_w1.Entry_tmpid.get() ==''):
        tk.messagebox.askquestion(title='Warning', message='เลือกรายการจาก list กดแก้ไข ก่อนทำรายการใดๆ เสมอ \n ยกเว้นสร้างรายการใหม่')
    else:    
        try:    
            conn = sqlite3.connect('1.db')
            print("เปิดฐานข้อมูลสำเร็จ")
            id = _w1.Entry_tmpid.get()
            c = conn.cursor()
            c.execute("DELETE FROM borrowcowbuff WHERE id = ?",(id,))
            conn.commit()  
            print("ลบเรคคอร์ดสำเร็จ ")   
            conn.close()
            
            if _w1.Entry_tmpborrowtype.get() == 'COW':
                bindingTree(1)
            else:
                bindingTree(2)  
             
        except sqlite3.Error as err:
            print(err) 
               
            
    # for arg in args:
    #     print ('another arg:', arg)
    # sys.stdout.flush()
    
def bindingTree(borrowtype):
    clearalldata()  
    for item in _w1.Scrolledtreeview_transaction.get_children():
        _w1.Scrolledtreeview_transaction.delete(item)  
        
    if(borrowtype==1):
        coworbuff='COW'             
    else:
        coworbuff='BUF' 
                            
    conn = sqlite3.connect("1.db")
    cur = conn.cursor()
    cur.execute("SELECT id,cid,fullname,borrowdate,borrowtime,returndate,returntime,borrowtype,borrowhour,payment,borrowstatus FROM borrowcowbuff WHERE borrowtype = ?",(coworbuff,))
    rows = cur.fetchall()
    
    for row in rows:
        # print(row) # it print all records in the database
        _w1.Scrolledtreeview_transaction.insert("", tk.END, values=row)
    conn.close()

def setCurrentValue():
    todaydate = datetime.today()
    _w1.Entry_borrowdate.delete(0,END)
    _w1.Entry_borrowdate.insert(END,todaydate.strftime("%d-%b-%Y"))
    
    _w1.Entry_borrowtime.delete(0,END)
    _w1.Entry_borrowtime.insert(END, todaydate.strftime("%H:%M"))    
    
def makeCowtransaction(*args):
    print('GUIcandidatemodify_support.makeCowtransaction')
    _w1.Label_transactionitem.config(text = 'รายการ ยืมวัว')
    _w1.Entry_tmpborrowtype.delete(0,END)
    _w1.Entry_tmpborrowtype.insert(END, 'COW')
    
    _w1.Entry_tmpaction.delete(0,END)
    _w1.Entry_tmpaction.insert(END, '')
    
    _w1.Entry_tmpid.delete(0,END)
    _w1.Entry_tmpid.insert(END, '')
    
    _w1.Entry_tmpborrowstatus.delete(0,END)
    _w1.Entry_tmpborrowstatus.insert(END, 'borrow')
    
    bindingTree(1)
    setCurrentValue()
    # for arg in args:
    #     # print ('another arg:', arg)
    # sys.stdout.flush()

def makeBuffalotran(*args):
   
    print('GUIcandidatemodify_support.makeBuffalotran')
    
    _w1.Label_transactionitem.config(text = 'รายการ ยืมควาย')
    _w1.Entry_tmpborrowtype.delete(0,END)
    _w1.Entry_tmpborrowtype.insert(END, 'BUF')
    
    _w1.Entry_tmpaction.delete(0,END)
    _w1.Entry_tmpaction.insert(END, '')
    
    _w1.Entry_tmpid.delete(0,END)
    _w1.Entry_tmpid.insert(END, '')
    
    _w1.Entry_tmpborrowstatus.delete(0,END)
    _w1.Entry_tmpborrowstatus.insert(END, 'borrow')
    
    bindingTree(2)
    setCurrentValue()
    # for arg in args:
    #     print ('another arg:', arg)
    # sys.stdout.flush()
           
def doCancelreturn(*args):
    print('GUIcandidatemodify_support.doCancelreturn')
    if(_w1.Entry_tmpid.get() ==''):
        tk.messagebox.askquestion(title='Warning', message='เลือกรายการจาก list กดแก้ไข ก่อนทำรายการใดๆ เสมอ \n ยกเว้นสร้างรายการใหม่')
    else:    
        try:
            id = _w1.Entry_tmpid.get()
            conn = sqlite3.connect('1.db')
            print("ติดต่อฐานข้อมูลสำเร็จ")
            c = conn.cursor()
            c.execute("UPDATE borrowcowbuff SET returndate=?,returntime=?,borrowhour=?, \
                payment=?,borrowstatus=? WHERE id = ?",('','',0,0.00,'ยืม',id,))
            conn.commit()  
            print("คืนค่าการคืน สำเร็จ")     
            conn.close()
            if(_w1.Entry_tmpborrowtype.get() == 'COW'):
                bindingTree(1)
            else:
                bindingTree(2)    
        except sqlite3.Error as err:
            print(err)    
   
    # for arg in args:
    #     print ('another arg:', arg)
    # sys.stdout.flush()

def searchTransaction(*args):
    print('GUIcandidatemodify_support.searchTransaction')
    searchcid = _w1.Entry_cidsearch.get()
    borrowtype = _w1.Entry_tmpborrowtype.get()
    if(borrowtype == ''):
        tk.messagebox.askquestion(title='Warning', message='โปรดเลือกการทำรายการ วัวหรือควายก่อน ปุ่มด้านขวา')
    else:
        for item in _w1.Scrolledtreeview_transaction.get_children():
            _w1.Scrolledtreeview_transaction.delete(item)  
        
        try:            
            conn = sqlite3.connect("1.db")
            cur = conn.cursor()
            cur.execute("SELECT id,cid,fullname,borrowdate,borrowtime,returndate,returntime,borrowtype,borrowhour,payment,borrowstatus FROM borrowcowbuff WHERE borrowtype = ? and cid like ?",(borrowtype,'%'+searchcid+'%',))
            # cur.execute("SELECT id,cid,fullname,borrowdate,borrowtime,returndate,returntime,borrowtype,borrowhour,payment,borrowstatus FROM borrowcowbuff WHERE borrowtype = '"+borrowtype+"' and cid like '%"+searchcid+"%'")
            rows = cur.fetchall()
            
            for row in rows:
                # print(row) # it print all records in the database
                _w1.Scrolledtreeview_transaction.insert("", tk.END, values=row)
            conn.close()
        except sqlite3.Error as err:
            print(err) 
            
    
    # searchTransaction
    # for arg in args:
    #     print ('another arg:', arg)
    # sys.stdout.flush()

def createDb(*args):
    print('GUIcandidatemodify_support.createDb')
    createdbSqlite()
    # tv.item(selected, values=(temp[0], temp[1], sal_up))
    # for arg in args:
    #     print ('another arg:', arg)
    # sys.stdout.flush()

    
def onClickTransactionRow(*args):
    print('GUIcandidatemodify_support.onClickTransactionRow')
    # print(_w1.Scrolledtreeview_transaction.selection())
    curItem = _w1.Scrolledtreeview_transactiont.focus()
    print(_w1.Scrolledtreeview_transaction.item(curItem))
    
def exitProgram(*args):
    print('GUIcandidatemodify_support.exitProgram')
    root.destroy()
    for arg in args:
        print ('another arg:', arg)
    sys.stdout.flush()

def createCsvFile():
    searchcid = _w1.Entry_cidsearch.get()
    borrowtype = _w1.Entry_tmpborrowtype.get()
    if(borrowtype == ''):
        tk.messagebox.askquestion(title='Warning', message='โปรดเลือกการทำรายการ วัวหรือควายก่อน ปุ่มด้านขวา')
    else:
        for item in _w1.Scrolledtreeview_transaction.get_children():
            _w1.Scrolledtreeview_transaction.delete(item)  
        
        try:            
            conn = sqlite3.connect("1.db")
            cur = conn.cursor()
            cur.execute("SELECT id,cid,fullname,borrowdate,borrowtime,returndate,returntime,borrowtype,borrowhour,payment,borrowstatus FROM borrowcowbuff WHERE borrowtype = ? and cid like ?",(borrowtype,'%'+searchcid+'%',))
            # cur.execute("SELECT id,cid,fullname,borrowdate,borrowtime,returndate,returntime,borrowtype,borrowhour,payment,borrowstatus FROM borrowcowbuff WHERE borrowtype = '"+borrowtype+"' and cid like '%"+searchcid+"%'")
            rows = cur.fetchall()
            
            for row in rows:
                # print(row) # it print all records in the database
                _w1.Scrolledtreeview_transaction.insert("", tk.END, values=row)
            conn.close()
        except sqlite3.Error as err:
            print(err) 
            
def createJsonFile():    
    searchcid = _w1.Entry_cidsearch.get()
    borrowtype = _w1.Entry_tmpborrowtype.get()
    if(borrowtype == ''):
        tk.messagebox.askquestion(title='Warning', message='โปรดเลือกการทำรายการ วัวหรือควายก่อน ปุ่มด้านขวา')
    else:
        for item in _w1.Scrolledtreeview_transaction.get_children():
            _w1.Scrolledtreeview_transaction.delete(item)  
        
        try:            
            conn = sqlite3.connect("1.db")
            cur = conn.cursor()
            cur.execute("SELECT id,cid,fullname,borrowdate,borrowtime,returndate,returntime,borrowtype,borrowhour,payment,borrowstatus FROM borrowcowbuff WHERE borrowtype = ? and cid like ?",(borrowtype,'%'+searchcid+'%',))
            # cur.execute("SELECT id,cid,fullname,borrowdate,borrowtime,returndate,returntime,borrowtype,borrowhour,payment,borrowstatus FROM borrowcowbuff WHERE borrowtype = '"+borrowtype+"' and cid like '%"+searchcid+"%'")
            rows = cur.fetchall()
            
            for row in rows:
                # print(row) # it print all records in the database
                _w1.Scrolledtreeview_transaction.insert("", tk.END, values=row)
            conn.close()
        except sqlite3.Error as err:
            print(err) 
            
def export(*args):
    print('GUIcandidatemodify_support.export')
    
    if(_w1.selectedButton.get()==1):
        createCsvFile()
    else:
        createJsonFile()
                
    for arg in args:
        print ('another arg:', arg)
    sys.stdout.flush()
        
if __name__ == '__main__':
    GUIcandidatemodify.start_up()

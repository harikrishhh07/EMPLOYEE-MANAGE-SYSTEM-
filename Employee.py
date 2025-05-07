from tkinter import * 
from tkinter import ttk
import tkinter as tk
import mysql.connector as m
from tkcalendar import DateEntry
import datetime
from PIL import Image, ImageTk
con=m.connect(host='localhost',user="root",password='root')
cur=con.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS EMPLOYEE")
cur.execute("USE EMPLOYEE")
cur.execute("CREATE TABLE IF NOT EXISTS civil_labour (sno int NOT NULL AUTO_INCREMENT, DAT date DEFAULT NULL, MASEN_NO int DEFAULT 0, MASEN_WAGES int DEFAULT 0,MASEN_TOTAL int DEFAULT (MASEN_NO * MASEN_WAGES), FC_NO int DEFAULT 0,FC_WAGES int DEFAULT 0,FC_TOTAL int DEFAULT ((FC_NO * FC_WAGES)),MC_NO int DEFAULT 0,MC_WAGES int DEFAULT 0,MC_TOTAL int DEFAULT ((MC_NO * MC_WAGES)),PRIMARY KEY (sno))") 
cur.execute("CREATE TABLE IF NOT EXISTS material (sno int NOT NULL AUTO_INCREMENT,DAT date DEFAULT NULL,c_unit int DEFAULT 0,c_rate int DEFAULT 0,c_total int DEFAULT (c_unit * c_rate),s_unit int DEFAULT 0,s_rate int DEFAULT 0,s_total int DEFAULT (s_unit * s_rate),b_no int DEFAULT 0,b_rate int DEFAULT 0,b_total int DEFAULT (b_no * b_rate),j_unit int DEFAULT 0,j_rate int DEFAULT 0,j_total int DEFAULT (j_unit * j_rate),others int DEFAULT 0,total int DEFAULT (((((c_total + s_total) + b_total) + j_total) + others)),PRIMARY KEY (sno))")

window=Tk()
window.configure(bg='BLACK')
window.title ('BUILDING DETAILS')
window.geometry ('1366x725')#735
window.resizable(False,False)
#LOGIN BUTTON FUNCTION
def login():
    if str(e99.get())=="root":    
        global canvas21
        canvas21.destroy()
        can22()
    else:
         messagebox.showinfo("Invalid password!","Enter correct password")
         e99.delete(0,END)
def lg():
    canvas22.destroy()
    can21()
#CANVAS 22    
def can22():
    global canvas22
    canvas22=Canvas(window,bg="#7AA197",height=1366,width=1360,bd=0,relief="raise")
    canvas22.place(x=0,y=0)
    canvas22.create_text(673,127,text="EMPLOYMENT   MANAGEMENT",fill="#232E2B",font=("elephant",30))        
    canvas22.create_text(673,250,text="SELECT  ANY  OPTION",fill="#232E2B",font=("elephant",25))
    b8=Button(canvas22,text='CIVIL_LABOUR',command=goto_cv,width=15,height=1,font=('elephant',11),bd=4,fg='#91CCC0',bg='#2E4F48')
    b8.place(x=465,y=350)
    b8=Button(canvas22,text=' MATERIAL',command=goto_m,width=15,height=1,font=('elephant',11),bd=4,fg='#91CCC0',bg='#2E4F48')
    b8.place(x=690,y=350)
    b8=Button(canvas22,text=' LOG OUT',command=lg,width=10,height=1,font=('elephant',11),bd=5,fg='#7AA197',bg="#1F1212")
    b8.place(x=590,y=450)
#get data from treeview
def get_data(event):
    selected_item=tree.focus()
    if selected_item:
        row=tree.item(selected_item)["values"]
        clear()
        e17.insert(0,row[0])
        e1.insert(0,row[1])
        e2.insert(0,row[2]) 
        e3.insert(0,row[3]) 
        e4.insert(0,row[5]) 
        e5.insert(0,row[6]) 
        e6.insert(0,row[8]) 
        e7.insert(0,row[9]) 
#CIVIL_LABOUR
def goto_cv():
    #global canvas23,canvas24 
    canvas22.destroy()
    canvas23=Canvas(window,bg="#A0B88C",height=1366,width=266,bd=0,highlightthickness=0,relief="raise")
    canvas23.place(x=0,y=0)
    canvas24=Canvas(window,bg="#AABA96",height=1366,width=1100,bd=0,relief="raise")
    canvas24.place(x=266,y=0)
    #clear function to clear values in entry boxes
    def clear():
        e17.delete(0,END)
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
    #save button to save record
    def save_CV():
        try:
            d,masno,maswages,fcno,fcwages,mcno,mcwages=str(e1.get_date()),int(e2.get()),int(e3.get()),int(e4.get()),int(e5.get()),int(e6.get()),int(e7.get())
            cur.execute("insert into CIVIL_LABOUR (Dat,MASEN_NO,MASEN_WAGES,FC_NO,FC_WAGES,MC_NO,MC_WAGES) values ('{}',{},{},{},{},{},{})".format(d,masno,maswages,fcno,fcwages,mcno,mcwages))
            con.commit()
            messagebox.showinfo("message!","details added successfully")
            view_CV()
            clear()
        except ValueError:
            messagebox.showinfo("message!","ENTER CORRECT INPUT")
    #tree view function 
    def view_CV():
            def get_data(event):
                selected_item=tree.focus()
                if selected_item:
                    row=tree.item(selected_item)["values"]
                    clear()
                    e17.insert(0,row[0])
                    e1.insert(0,row[1])
                    e2.insert(0,row[2]) 
                    e3.insert(0,row[3]) 
                    e4.insert(0,row[5]) 
                    e5.insert(0,row[6]) 
                    e6.insert(0,row[8]) 
                    e7.insert(0,row[9]) 
            cur.execute("select SNO,DAT,MASEN_NO,MASEN_WAGES,MASEN_TOTAL,FC_NO,FC_WAGES,FC_TOTAL,MC_NO,MC_WAGES,MC_TOTAL FROM CIVIL_LABOUR")
            recs=cur.fetchall()
            l=[]
            for i in recs:
                l.append(i)
            tree=ttk.Treeview(canvas24)
            tree["show"]="headings"
            s=ttk.Style(canvas24)
            s.theme_use("clam")
            s.configure(".",font=("Bahnschrift SemiBold",12))
            s.configure("Treeview.Heading",fg="red",font=("Bahnschrift SemiBold",12))
            tree["columns"]=("S.NO","DATE","MASEN_NO","MASEN_WAGES","MASEN_TOTAL","FC_NO" ,"FC_WAGES" ,"FC_TOTAL" ,"MC_NO" ,"MC_WAGES", "MC_TOTAL")
            tree.column("S.NO",width=50,minwidth=50,anchor=CENTER)
            tree.column("DATE",width=98,minwidth=98,anchor=CENTER)
            tree.column("MASEN_NO",width=98,minwidth=98,anchor=CENTER)
            tree.column("MASEN_WAGES",width=98,minwidth=98,anchor=CENTER)
            tree.column("MASEN_TOTAL",width=98,minwidth=98,anchor=CENTER)
            tree.column("FC_NO",width=98,minwidth=98,anchor=CENTER)
            tree.column("FC_WAGES",width=98,minwidth=98,anchor=CENTER)
            tree.column("FC_TOTAL",width=98,minwidth=98,anchor=CENTER)
            tree.column("MC_NO",width=98,minwidth=98,anchor=CENTER)
            tree.column("MC_WAGES",width=98,minwidth=98,anchor=CENTER)
            tree.column("MC_TOTAL",width=98,minwidth=98,anchor=CENTER)
            tree.heading("S.NO",text="S.NO",anchor=CENTER)
            tree.heading("DATE",text="DATE",anchor=CENTER)
            tree.heading("MASEN_NO",text="MASEN_NO",anchor=CENTER)
            tree.heading("MASEN_WAGES",text="MASEN_WAGES",anchor=CENTER)
            tree.heading("MASEN_TOTAL",text="MASEN_TOTAL",anchor=CENTER)
            tree.heading("FC_NO",text="FC_NO",anchor=CENTER)
            tree.heading("FC_WAGES",text="FC_WAGES",anchor=CENTER)
            tree.heading("FC_TOTAL",text="FC_TOTAL",anchor=CENTER)
            tree.heading("MC_NO",text="MC_NO",anchor=CENTER)
            tree.heading("MC_WAGES",text="MC_WAGES",anchor=CENTER)
            tree.heading("MC_TOTAL",text="MC_TOTAL",anchor=CENTER)
            try:
                i=0
                for x in l:
                    tree.insert("",i,text="",values=(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10]))
                    i=i+1
            except IndexError:
                messagebox.showinfo("Alert!","Invalid input. Please try again")
            tree.place(x = 5, y = 50,height=380,width=1080)
            tree.bind('<ButtonRelease>',get_data) 
    #update function to update a record        
    def update_cv():
            d,masno,maswages,fcno,fcwages,mcno,mcwages,sno=str(e1.get_date()),int(e2.get()),int(e3.get()),int(e4.get()),int(e5.get()),int(e6.get()),int(e7.get()),int(e17.get())
            cur.execute("update CIVIL_LABOUR set DAT='{}',MASEN_NO={},MASEN_WAGES={},FC_NO={},FC_WAGES={},MC_NO={},MC_WAGES={},MASEN_TOTAL= MASEN_NO*MASEN_WAGES,FC_TOTAL=FC_NO*FC_WAGES,MC_TOTAL=MC_NO*MC_WAGES where SNO={};".format(d,masno,maswages,fcno,fcwages,mcno,mcwages,sno))
            con.commit()
            messagebox.showinfo("message!","details updated successfully")
            view_CV()
    #delete funtion to delete a record        
    def del_cv():
        sno=int(e17.get())
        cur.execute("delete from CIVIL_LABOUR where SNO={};".format(sno))
        con.commit()
        messagebox.showinfo("message!","rec deleted successfully")
        view_CV()
    #search funtion to search the reqired record         
    def ser_cv():
        if e1.get()=="":
            messagebox.showinfo("Alert!","To Search Any Record \nENTER DATE in entry box")
        else:
            d=str(e1.get())
            cur.execute("select SNO,DAT,MASEN_NO,MASEN_WAGES,MASEN_TOTAL,FC_NO,FC_WAGES,FC_TOTAL,MC_NO,MC_WAGES,MC_TOTAL FROM CIVIL_LABOUR  WHERE DAT='{}';".format(d))
            recs=cur.fetchall()
            l=[]
            for i in recs:
                l.append(i)
            tree=ttk.Treeview(canvas24)
            tree["show"]="headings"
            s=ttk.Style(canvas24)
            s.theme_use("clam")
            s.configure(".",font=("Bahnschrift SemiBold",12))
            s.configure("Treeview.Heading",fg="red",font=("Bahnschrift SemiBold",12))
            tree["columns"]=("S.NO","DATE","MASEN_NO","MASEN_WAGES","MASEN_TOTAL","FC_NO" ,"FC_WAGES" ,"FC_TOTAL" ,"MC_NO" ,"MC_WAGES", "MC_TOTAL")
            tree.column("S.NO",width=50,minwidth=50,anchor=CENTER)
            tree.column("DATE",width=98,minwidth=98,anchor=CENTER)
            tree.column("MASEN_NO",width=98,minwidth=98,anchor=CENTER)
            tree.column("MASEN_WAGES",width=98,minwidth=98,anchor=CENTER)
            tree.column("MASEN_TOTAL",width=98,minwidth=98,anchor=CENTER)
            tree.column("FC_NO",width=98,minwidth=98,anchor=CENTER)
            tree.column("FC_WAGES",width=98,minwidth=98,anchor=CENTER)
            tree.column("FC_TOTAL",width=98,minwidth=98,anchor=CENTER)
            tree.column("MC_NO",width=98,minwidth=98,anchor=CENTER)
            tree.column("MC_WAGES",width=98,minwidth=98,anchor=CENTER)
            tree.column("MC_TOTAL",width=98,minwidth=98,anchor=CENTER)
            tree.heading("S.NO",text="S.NO",anchor=CENTER)
            tree.heading("DATE",text="DATE",anchor=CENTER)
            tree.heading("MASEN_NO",text="MASEN_NO",anchor=CENTER)
            tree.heading("MASEN_WAGES",text="MASEN_WAGES",anchor=CENTER)
            tree.heading("MASEN_TOTAL",text="MASEN_TOTAL",anchor=CENTER)
            tree.heading("FC_NO",text="FC_NO",anchor=CENTER)
            tree.heading("FC_WAGES",text="FC_WAGES",anchor=CENTER)
            tree.heading("FC_TOTAL",text="FC_TOTAL",anchor=CENTER)
            tree.heading("MC_NO",text="MC_NO",anchor=CENTER)
            tree.heading("MC_WAGES",text="MC_WAGES",anchor=CENTER)
            tree.heading("MC_TOTAL",text="MC_TOTAL",anchor=CENTER)
            try:
                i=0
                for x in l:
                    tree.insert("",i,text="",values=(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10]))
                    i=i+1
            except IndexError:
                messagebox.showinfo("Alert!","Invalid input. Please try again")
            tree.place(x = 5, y = 50,height=380,width=1080)
            tree.bind('<ButtonRelease>',get_data) 
    #back button function         
    def back():
        canvas23.destroy()
        canvas24.destroy()
        can22()
    #button
    def text_box1(e):e2.delete(0,"end")
    def text_box2(e):e3.delete(0,"end")
    def text_box3(e):e4.delete(0,"end")
    def text_box4(e):e5.delete(0,"end")
    def text_box5(e):e6.delete(0,"end")
    def text_box6(e):e7.delete(0,"end")
    b1=Button(canvas23,text='SAVE_CV',width=8,height=1,font=('elephant',11),bd=3,fg='#151712',bg='#EFFFF0',command=save_CV)
    b1.place(x=20,y=350)
    b8=Button(canvas24,text='BACK',width=8,height=1,font=('elephant',11),bd=4,fg='#151712',bg='#8C780D',command=back)
    b8.place(x=970,y=450)
    b4=Button(canvas23,text='VIEW_CV',width=8,height=1,font=('elephant',11),bd=3,fg='#151712',bg='#E7E8FF',command=view_CV)
    b4.place(x=140,y=349)
    b2=Button(canvas23,text='UPD_CV',width=8,height=1,font=('elephant',11),bd=3,fg='#151712',bg="#FFEFF8",command=update_cv)
    b2.place(x=20,y=400)
    b3=Button(canvas23,text='CLEAR',width=8,height=1,font=('elephant',11),bd=3,fg='#151712',bg='#DBC1C1',command=clear)
    b3.place(x=20,y=450)
    b7=Button(canvas23,text='DEL_CV',width=8,height=1,font=('elephant',11),bd=3,fg='#151712',bg='#E6A4A4',command=del_cv)
    b7.place(x=140,y=399)
    b7=Button(canvas23,text='SEARCH',width=8,height=1,font=('elephant',11),bd=3,fg='#151712',bg='#DEDAA1',command=ser_cv)
    b7.place(x=140,y=450)
    #lable main topics
    canvas23.create_text(40,78,text="DATE:",fill="#272B23",font=("arial black",14))
    canvas23.create_text(120,35,text="ENTRY",fill="#090A08",font=("arial black",14))
    #date ENTRY BOX
    e1=DateEntry(canvas23,selectmade="month",font=("arial black",11))
    e1.place(x=87,y=68, width=110, height=24)
    #sno ENTRY BOX
    e17=Entry(canvas23,font=("Britannic Bold",15),borderwidth=3)
    e17.place(x=170,y=120, width=55, height=24)
    #NO WAGES-lable
    canvas23.create_text(140,170,text="NO",fill="#272B23",font=("arial black",12))
    canvas23.create_text(208,170,text="WAGES",fill="#272B23",font=("arial black",12))
    #CIVIL LABOUR
    canvas23.create_text(80,130,text="CIVIL_LABUOR",fill="#B84A44",font=("arial black",14))
    #MASEN   _LABLE
    canvas23.create_text(45,200,text="MASEN",fill="#272B23",font=("arial black",14))
    #ENTRY BOX
    e2=Entry(canvas23,textvariable=StringVar(),font=("Britannic Bold",15),borderwidth=4)
    e2.insert(10,"0")
    e2.place(x=98,y=185, width=72, height=30)
    e2.bind("<FocusIn>",text_box1)
    e3=Entry(canvas23,textvariable=StringVar(),font=("Britannic Bold",15),borderwidth=4)
    e3.insert(0,"0")
    e3.place(x=175,y=185, width=72, height=30)
    e3.bind("<FocusIn>",text_box2)
    #FC  _LABLE
    canvas23.create_text(25,250,text="FC",fill="#272B23",font=("arial black",14))
    #ENTRY BOX   
    e4=Entry(canvas23,font=("Britannic Bold",15),borderwidth=4)
    e4.insert(10,"0")
    e4.place(x=98,y=235, width=72, height=30)
    e4.bind("<FocusIn>",text_box3)
    e5=Entry(canvas23,font=("Britannic Bold",15),borderwidth=4)
    e5.insert(10,"0")
    e5.place(x=175,y=235, width=72, height=30)
    e5.bind("<FocusIn>",text_box4)
    #MC _LABLE
    canvas23.create_text(25,295,text="MC",fill="#272B23",font=("arial black",14))
    #ENTRY BOX
    e6=Entry(canvas23,font=("Britannic Bold",15),borderwidth=4)
    e6.place(x=98,y=280, width=72, height=30)
    e6.insert(10,"0")
    e6.bind("<FocusIn>",text_box5)
    e7=Entry(canvas23,font=("Britannic Bold",15),borderwidth=4)
    e7.place(x=175,y=280, width=72, height=30)
    e7.insert(10,"0")
    e7.bind("<FocusIn>",text_box6)
#MATERIAL
def goto_m():
    canvas22.destroy()
    canvas23=Canvas(window,bg="#A0B88C",height=1366,width=266,bd=0,highlightthickness=0,relief="raise")
    canvas23.place(x=0,y=0)
    canvas24=Canvas(window,bg="#AABA96",height=1366,width=1100,bd=0,relief="raise")
    canvas24.place(x=266,y=0)
    #clear function
    def clear1():    
        e18.delete(0,END)
        e1.delete(0,END)
        e8.delete(0,END)
        e9.delete(0,END)
        e10.delete(0,END)
        e11.delete(0,END)
        e12.delete(0,END)
        e13.delete(0,END)
        e14.delete(0,END)
        e15.delete(0,END)
        e16.delete(0,END)
    #MATERIAL TREEVIEW
    def save_M():
        try:
            d,C_UNIT,C_RATE,S_UNIT,S_RATE,B_NO,B_RATE,J_UNIT,J_RATE,OTHERS=str(e1.get_date()),int(e8.get()),int(e9.get()),int(e10.get()),int(e11.get()),int(e12.get()),int(e13.get()),int(e14.get()),int(e15.get()),int(e16.get())
            cur.execute("insert into MATERIAL (dat,C_UNIT,C_RATE,S_UNIT,S_RATE,B_NO,B_RATE,J_UNIT,J_RATE,OTHERS) values ('{}',{},{},{},{},{},{},{},{},{})".format(d,C_UNIT,C_RATE,S_UNIT,S_RATE,B_NO,B_RATE,J_UNIT,J_RATE,OTHERS))
            con.commit()
            messagebox.showinfo("message!","details added successfully")
            view_M()
            clear1()
        except ValueError:
            messagebox.showinfo("message!","ENTER CORRECT INPUT")    
    #view tree m
    def view_M():
            def get_data(event):
                selected_item=tree.focus()
                if selected_item:
                    row=tree.item(selected_item)["values"]
                    clear1()
                    e8.insert(0,row[2])
                    e1.insert(0,row[1])
                    e9.insert(0,row[3]) 
                    e10.insert(0,row[5]) 
                    e11.insert(0,row[6]) 
                    e12.insert(0,row[8]) 
                    e13.insert(0,row[9]) 
                    e14.insert(0,row[11]) 
                    e15.insert(0,row[12]) 
                    e16.insert(0,row[14]) 
                    e18.insert(0,row[0])
            cur.execute("select sno,dat,C_UNIT,C_RATE,C_TOTAL,S_UNIT,S_RATE,S_TOTAL,B_NO,B_RATE,B_TOTAL,J_UNIT,J_RATE,J_TOTAL,OTHERS,TOTAL FROM MATERIAL")
            recs=cur.fetchall()
            l=[]
            for i in recs:
                l.append(i)
            tree=ttk.Treeview(canvas24)
            tree["show"]="headings"
            s=ttk.Style(canvas24)
            s.theme_use("clam")
            s.configure(".",font=("Bahnschrift SemiBold",12))
            s.configure("Treeview.Heading",fg="red",font=("Bahnschrift SemiBold",12))
            tree["columns"]=('S.NO','DATE','C_UNIT','C_RATE','C_TOTAL','S_UNIT','S_RATE','S_TOTAL','B_NO','B_RATE','B_TOTAL','J_UNIT','J_RATE','J_TOTAL','OTHERS','TOTAL')
            tree.column("S.NO",width=50,minwidth=50,anchor=CENTER)
            tree.column("DATE",width=95,minwidth=95,anchor=CENTER)
            tree.column("C_UNIT",width=60,minwidth=60,anchor=CENTER)
            tree.column("C_RATE",width=62,minwidth=62,anchor=CENTER)
            tree.column("C_TOTAL",width=70,minwidth=70,anchor=CENTER)
            tree.column("S_UNIT",width=60,minwidth=60,anchor=CENTER)
            tree.column("S_RATE",width=62,minwidth=62,anchor=CENTER)
            tree.column("S_TOTAL",width=70,minwidth=70,anchor=CENTER)
            tree.column("B_NO",width=60,minwidth=60,anchor=CENTER)
            tree.column("B_RATE",width=70,minwidth=70,anchor=CENTER)
            tree.column("B_TOTAL",width=70,minwidth=70,anchor=CENTER)
            tree.column("J_UNIT",width=70,minwidth=70,anchor=CENTER)
            tree.column("J_RATE",width=70,minwidth=70,anchor=CENTER)
            tree.column("J_TOTAL",width=70,minwidth=70,anchor=CENTER)
            tree.column("OTHERS",width=70,minwidth=70,anchor=CENTER)
            tree.column("TOTAL",width=70,minwidth=70,anchor=CENTER)
            tree.heading("S.NO",text="S.NO",anchor=CENTER)
            tree.heading("DATE",text="DATE",anchor=CENTER)
            tree.heading("C_UNIT",text="C_UNIT",anchor=CENTER)
            tree.heading("C_RATE",text="C_RATE",anchor=CENTER)
            tree.heading("C_TOTAL",text="C_TOTAL",anchor=CENTER)
            tree.heading("S_UNIT",text="S_UNIT",anchor=CENTER)
            tree.heading("S_RATE",text="S_RATE",anchor=CENTER)
            tree.heading("S_TOTAL",text="S_TOTAL",anchor=CENTER)
            tree.heading("B_NO",text="B_NO",anchor=CENTER)
            tree.heading("B_RATE",text="B_RATE",anchor=CENTER)
            tree.heading("B_TOTAL",text="B_TOTAL",anchor=CENTER)
            tree.heading("J_UNIT",text="J_UNIT",anchor=CENTER)
            tree.heading("J_RATE",text="J_RATE",anchor=CENTER)
            tree.heading("J_TOTAL",text="J_TOTAL",anchor=CENTER)
            tree.heading("OTHERS",text="OTHERS",anchor=CENTER)
            tree.heading("TOTAL",text="TOTAL",anchor=CENTER)
            try:
                i=0
                for x in l:
                    tree.insert("",i,text="",values=(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10],x[11],x[12],x[13],x[14],x[15]))
                    i=i+1
            except IndexError:
                messagebox.showinfo("Alert!","Invalid input. Please try again")
            tree.place(x = 5, y = 50,height=400,width=1085)
            tree.bind('<ButtonRelease>',get_data) 
    #update material   
    def update_m():
       d,C_UNIT,C_RATE,S_UNIT,S_RATE,B_NO,B_RATE,J_UNIT,J_RATE,OTHERS,SNO=str(e1.get_date()),int(e8.get()),int(e9.get()),int(e10.get()),int(e11.get()),int(e12.get()),int(e13.get()),int(e14.get()),int(e15.get()),int(e16.get()),int(e18.get())
       cur.execute("update material set dat='{}',C_UNIT={},C_RATE={},S_UNIT={},S_RATE={},B_NO={},B_RATE={},J_UNIT={},J_RATE={},OTHERS={},c_total=c_unit*c_rate,s_total=s_unit*s_rate,b_total=b_no*b_rate,j_total=j_unit*j_rate,total=c_total+s_total+b_total+j_total+OTHERS where SNO={};".format(d,C_UNIT,C_RATE,S_UNIT,S_RATE,B_NO,B_RATE,J_UNIT,J_RATE,OTHERS,SNO))
       con.commit()
       messagebox.showinfo("message!","details updated successfully")
       view_M()
    #delete material      
    def del_m():
            sno=int(e18.get())
            cur.execute("delete from material where SNO={};".format(sno))
            con.commit()
            messagebox.showinfo("message!","rec deleted successfully")
            view_M()
    #search material           
    def sea_m():
        if e1.get()=="":
            messagebox.showinfo("Alert!","ENTER DATE in entry box")
        else:
            d=str(e1.get())
            cur.execute("select sno,dat,C_UNIT,C_RATE,C_TOTAL,S_UNIT,S_RATE,S_TOTAL,B_NO,B_RATE,B_TOTAL,J_UNIT,J_RATE,J_TOTAL,OTHERS,TOTAL FROM MATERIAL where dat='{}'".format(d))
            recs=cur.fetchall()
            l=[]
            for i in recs:
                l.append(i)
            tree=ttk.Treeview(canvas24)
            tree["show"]="headings"
            s=ttk.Style(canvas24)
            s.theme_use("clam")
            s.configure(".",font=("Bahnschrift SemiBold",12))
            s.configure("Treeview.Heading",fg="red",font=("Bahnschrift SemiBold",12))
            tree["columns"]=('S.NO','DATE','C_UNIT','C_RATE','C_TOTAL','S_UNIT','S_RATE','S_TOTAL','B_NO','B_RATE','B_TOTAL','J_UNIT','J_RATE','J_TOTAL','OTHERS','TOTAL')
            tree.column("S.NO",width=50,minwidth=50,anchor=CENTER)
            tree.column("DATE",width=95,minwidth=95,anchor=CENTER)
            tree.column("C_UNIT",width=60,minwidth=60,anchor=CENTER)
            tree.column("C_RATE",width=62,minwidth=62,anchor=CENTER)
            tree.column("C_TOTAL",width=70,minwidth=70,anchor=CENTER)
            tree.column("S_UNIT",width=60,minwidth=60,anchor=CENTER)
            tree.column("S_RATE",width=62,minwidth=62,anchor=CENTER)
            tree.column("S_TOTAL",width=70,minwidth=70,anchor=CENTER)   
            tree.column("B_NO",width=60,minwidth=60,anchor=CENTER)
            tree.column("B_RATE",width=70,minwidth=70,anchor=CENTER)
            tree.column("B_TOTAL",width=70,minwidth=70,anchor=CENTER)
            tree.column("J_UNIT",width=70,minwidth=70,anchor=CENTER)
            tree.column("J_RATE",width=70,minwidth=70,anchor=CENTER)
            tree.column("J_TOTAL",width=70,minwidth=70,anchor=CENTER)
            tree.column("OTHERS",width=70,minwidth=70,anchor=CENTER)
            tree.column("TOTAL",width=70,minwidth=70,anchor=CENTER)
            tree.heading("S.NO",text="S.NO",anchor=CENTER)
            tree.heading("DATE",text="DATE",anchor=CENTER)
            tree.heading("C_UNIT",text="C_UNIT",anchor=CENTER)
            tree.heading("C_RATE",text="C_RATE",anchor=CENTER)
            tree.heading("C_TOTAL",text="C_TOTAL",anchor=CENTER)
            tree.heading("S_UNIT",text="S_UNIT",anchor=CENTER)
            tree.heading("S_RATE",text="S_RATE",anchor=CENTER)
            tree.heading("S_TOTAL",text="S_TOTAL",anchor=CENTER)
            tree.heading("B_NO",text="B_NO",anchor=CENTER)
            tree.heading("B_RATE",text="B_RATE",anchor=CENTER)
            tree.heading("B_TOTAL",text="B_TOTAL",anchor=CENTER)
            tree.heading("J_UNIT",text="J_UNIT",anchor=CENTER)
            tree.heading("J_RATE",text="J_RATE",anchor=CENTER)
            tree.heading("J_TOTAL",text="J_TOTAL",anchor=CENTER)
            tree.heading("OTHERS",text="OTHERS",anchor=CENTER)
            tree.heading("TOTAL",text="TOTAL",anchor=CENTER)
            try:
                i=0
                for x in l:
                    tree.insert("",i,text="",values=(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10],x[11],x[12],x[13],x[14],x[15]))
                    i=i+1
            except IndexError:
                messagebox.showinfo("Alert!","Invalid input. Please try again")
            tree.place(x = 5, y = 50,height=400,width=1085)
            tree.bind('<ButtonRelease>',get_data) 
    # back button function
    def back():
        canvas23.destroy()
        canvas24.destroy()
        can22() 
        
    def text_box1(e):e8.delete(0,"end")
    def text_box2(e):e9.delete(0,"end")
    def text_box3(e):e10.delete(0,"end")
    def text_box4(e):e11.delete(0,"end")
    def text_box5(e):e12.delete(0,"end")
    def text_box6(e):e13.delete(0,"end")
    def text_box7(e):e14.delete(0,"end")
    def text_box8(e):e15.delete(0,"end")
    def text_box9(e):e16.delete(0,"end")
    #lable main topics
    canvas23.create_text(47,78,text="DATE:",fill="BLACK",font=("arial black",14))
    #date entry
    e1=DateEntry(canvas23,selectmade="month",font=("arial black",11))
    e1.place(x=94,y=68, width=112, height=24)
    #MATERIAL
    canvas23.create_text(120,35,text="ENTRY",fill="#090A08",font=("arial black",14))
    canvas23.create_text(67,125,text="MATERIAL",fill="#B84A44",font=("arial black",14))
    e18=Entry(canvas23,font=("Britannic Bold",15),borderwidth=3)
    e18.place(x=150,y=113.5, width=55, height=24)
    #NO/UNIT ,RATE
    canvas23.create_text(140,170,text="NO",fill="#272B23",font=("arial black",12))
    canvas23.create_text(208,170,text="UNIT",fill="#272B23",font=("arial black",12))
    #CEMENT
    canvas23.create_text(52,200,text="CEMENT",fill="#272B23",font=("arial black",14))
    e8=Entry(canvas23,font=("Britannic Bold",15),borderwidth=4)
    e8.place(x=105,y=185, width=70, height=30)
    e8.insert(0,"0")
    e8.bind("<FocusIn>",text_box1)
    e9=Entry(canvas23,font=("Britannic Bold",15),borderwidth=4)
    e9.place(x=182,y=185, width=70, height=30)
    e9.insert(0,"0")
    e9.bind("<FocusIn>",text_box2)
    #SAND
    canvas23.create_text(39,250,text="SAND",fill="#272B23",font=("arial black",14))
    e10=Entry(canvas23,font=("Britannic Bold",15),borderwidth=4)
    e10.place(x=105,y=235, width=70, height=30)
    e10.insert(0,"0")
    e10.bind("<FocusIn>",text_box3)
    e11=Entry(canvas23,font=("Britannic Bold",15),borderwidth=4)
    e11.place(x=182,y=235, width=70, height=30)
    e11.insert(0,"0")
    e11.bind("<FocusIn>",text_box4)
    #BRICK
    canvas23.create_text(42,295,text="BRICK",fill="#272B23",font=("arial black",14))
    e12=Entry(canvas23,font=("Britannic Bold",15),borderwidth=4)
    e12.place(x=105,y=280, width=70, height=28)
    e12.insert(0,"0")
    e12.bind("<FocusIn>",text_box5)
    e13=Entry(canvas23,font=("Britannic Bold",15),borderwidth=4)
    e13.place(x=182,y=280, width=70, height=30)
    e13.insert(0,"0")
    e13.bind("<FocusIn>",text_box6)
    #JALLY
    canvas23.create_text(42,339,text="JALLY",fill="#272B23",font=("arial black",14))
    e14=Entry(canvas23,font=("Britannic Bold",15),borderwidth=4)
    e14.place(x=105,y=325, width=70, height=30)
    e14.insert(0,"0")
    e14.bind("<FocusIn>",text_box7)
    e15=Entry(canvas23,font=("Britannic Bold",15),borderwidth=4)
    e15.place(x=182,y=325, width=70, height=30)
    e15.insert(0,"0")
    e15.bind("<FocusIn>",text_box8)
    #OTHERS
    canvas23.create_text(52,395,text="OTHERS",fill="#272B23",font=("arial black",14))
    e16=Entry(canvas23,font=("Britannic Bold",15),borderwidth=4)
    e16.place(x=105,y=380, width=100, height=30)
    e16.insert(0,"0")
    e16.bind("<FocusIn>",text_box9)
    #BUTTONs
    b11=Button(canvas23,text='SAVE_M',width=8,height=1,font=('elephant',11),bd=4,fg='#151712',bg="#EFFFF0",command=save_M)
    b11.place(x=20,y=420)
    b5=Button(canvas23,text='VIEW_M',width=8,height=1,font=('elephant',11),bd=4,fg='#151712',bg='#E7E8FF',command=view_M)
    b5.place(x=130,y=420)
    b7=Button(canvas23,text='SEARCH',width=8,height=1,font=('elephant',11),bd=3,fg='#151712',bg='#DEDAA1',command=sea_m)
    b7.place(x=130,y=520)
    b3=Button(canvas23,text='CLEAR',width=8,height=1,font=('elephant',11),bd=4,fg='#151712',bg='#DBC1C1',command=clear1)
    b3.place(x=20,y=520)
    b6=Button(canvas23,text='UPD_M',width=8,height=1,font=('elephant',11),bd=4,fg='#151712',bg='#FFEFF8',command=update_m)
    b6.place(x=20,y=470)
    b8=Button(canvas23,text='DEL_M',width=8,height=1,font=('elephant',11),bd=4,fg='#151712',bg='#E6A4A4',command=del_m)
    b8.place(x=130,y=470)
    b8=Button(canvas24,text='BACK',width=8,height=1,font=('elephant',11),bd=4,fg='#151712',bg='#8C780D',command=back)
    b8.place(x=970,y=470)

def can21():
        global e99,canvas21,b8
        #canvas 21
        canvas21=Canvas(window,bg="#6B9BA1",height=1366,width=1360,bd=0,relief="raise")
        canvas21.place(x=0,y=0)
        #password
        canvas21.create_text(550,327,text="PASSWORD",fill="#1B3536",font=("elephant",25))
        canvas21.create_text(673,200,text="EMPLOYMENT   MANAGEMENT",fill="#1B3536",font=("elephant",30))
        canvas21.create_text(580,387,text="show password",fill="#97FCFF",font=("elephant",15))
        #pass entry box
        e99=Entry(canvas21,font=("Britannic Bold",13),show=".",borderwidth=3,textvariable=StringVar())
        e99.place(x=680,y=310, width=150, height=30)
        #button
        b8=Button(window,text='LOGIN',command=login,width=12,height=1,font=('elephant',11),bd=5,fg='black',bg='#426E54')
        b8.place(x=550,y=450)
        cv2=IntVar(value=0)
        def tickbox():
            if (cv2.get()==1):
                e99.config(show="")
            elif (cv2.get()==0):
                e99.config(show=".")
        tb=Checkbutton(canvas21,variable=cv2,onvalue=1,offvalue=0,command=tickbox,bg="#6B9BA1")
        tb.place(x=680,y=375)
def key_h(event):
    login()
window.bind("<Return>",key_h)
can21()
window.mainloop()
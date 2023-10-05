import tkinter
from tkinter import messagebox
from tkinter.ttk import*
import mysql.connector
mycon= mysql.connector.connect(host='localhost',user='root',password='Kam@15',database='air')
cur = mycon.cursor()
rootp=tkinter.Tk()
Label(rootp,text="Your Wings Already Exist All You Have To Do Is Fly With Us...",font="Bold 20").pack()
Label(rootp,text="Please Note:Booking for Domestic Trips only",font="Bold 10").pack()
Label(rootp,text="Welcome To INDIAIR",font="Bold 20").pack()
def fun5():
    name=input("Enter your name: ")
    passengers=int(input("Enter the number of passengers travelling: "))
    symptoms=int(input('''Are you or the person you are travelling experiencing any of the following symptoms:
               1.Cough,
               2.Fever, 
               3.Difficulty in Breathing,
               4.Loss of senses of smell and taste or 
               5.None of the above: 
                   '''))
    diseases=int(input('''Have you or the person travelling with you ever had any of the following:
              
               1.Diabetes, 
               2.Hypertension, 
               3.Lung disease, 
               4.Heart disease, 
               5.Kidney Disorder, 
               6.None of the above: 
                   '''))
    travelling=input('''Have you or the person you are travelling with travelled anywhere internationally in the last 28- 45 days? yes/no: ''')
    condition=int(input('''Which of the following apply to you? 
                1.I have recently interacted or lived with someone who has tested positive for COVID-19,  
                2.I am a healthcare worker and i examined a COVID-19 confirmed case without protective gear,
                3.None of the above: 
                    '''))
    if symptoms == 5 and diseases== 6 and (travelling.title()=='NO' or 'no' or 'No') and condition == 3:
        rootp.destroy()
        root=tkinter.Tk()
        root.title('Flight Booking')
        Label(root,text="Enter Boarding").grid(row=1,column=0)
        w=Combobox(root,height=5,width=15,values=["New  Delhi"," Mumbai"  ,"Ahmedabad","Srinagar", "Bangalore" ,"Chennai", "Kolkata","Jaipur"])
        w.grid(row=1,column=1)
        Label(root,text='Enter Destination').grid(row=2,column=0)
        w1=Combobox(root,height=5,width=15,values=["New Delhi","Mumbai", "Ahmedabad","Srinagar","Bangalore","Chennai","Kolkata","Jaipur","Guwahati","Kochi"])
        w1.grid(row=2,column=1)
        w2=Combobox(root,text='BusinessClass',height=5,width=15,values=["Business","Economic"])
        w2.grid(row=3,column=1)
        Label(root,text='Choose Class').grid(row=3,column=0)
        Label(root,text="Name of Passenger").grid(row=4,column=0)
        n=Entry(root,width=30)
        n.grid(row=4,column=1)
        Label(root,text="Choose date of travel").grid(row=5,column=0)
        w3=Combobox(root,text="choose date",height=5,width=15,values=["20-03-2021","21-03-2021","22-03-2021" ,"23-03-2021","24-03-2012","25-03-2021"])
        w3.grid(row=5,column=1)
        Label(root,text="Choose time of your flight").grid(row=6,column=0)
        w4=Combobox(root,height=5,width=15,values=["1:00 AM","7:00 AM","1:00 PM","4:00 PM","9:00 PM"])
        w4.grid(row=6,column=1)
        def fun():
            a=w.get()
            b=w1.get()
            d=w2.get()
            k=n.get()
            f=w3.get()
            g=w4.get()
            x=(k,a,b,f,g)
            cur=mycon.cursor()
            if(a=='' or b=='' or d=='' or f=='' or g==''or k==''):
                messagebox.showerror("OOPS","you can't leave any field empty")
            else:
                if (d=='Economic') :
                    if a!=b:
                        cur.execute("drop table economic2")
                        cur.execute("create table economic2(PNRNO int NOT NULL Auto_Increment,PassengerName varchar(30),boarding char(20),destination char(20),date char(30),time varchar(10), PRIMARY KEY(PNRNO))")
                        cur.execute("alter table economic2 Auto_Increment=100")
                        cur.execute("insert into economic2(PassengerName,boarding,destination,date,time)  values 		                          ('%s','%s','%s','%s','%s')"%x)
                        messagebox.showinfo("congrats","Your seat has been reserved")
                        mycon.commit()
                        cur.execute("select * from economic2 where PassengerName='%s'"%(k,))
                        messagebox.showinfo("records",cur.fetchone())
                        cur.execute("select PNRNO from economic2 where PassengerName = '%s'"%(k,))
                        messagebox.showinfo("Your PNRNO IS ",cur.fetchone())
                        mycon.close()
                    else:
                        print("hyu")
                        messagebox.showerror("Error","you can't choose same city")
                    
                else:
                    if a!=b:
                        cur.execute("drop table common2")
                        cur.execute("create table common2(PNRNO int NOT NULL Auto_Increment ,PassengerName varchar(30),boarding char(20),destination char(20),date char(30),time varchar(10), PRIMARY KEY(PNRNO))")
                        cur.execute("alter table common2 Auto_Increment=200")
                        cur.execute("insert into common2 (PassengerName,boarding,destination,date,time) values ('%s','%s','%s','%s','%s')"%x)
                        messagebox.showinfo("congrats","Your seat has been reserved")
                        mycon.commit()
                        cur.execute("select * from common2 where PassengerName='%s'"%(k,))
                        messagebox.showinfo("records",cur.fetchone())
                        cur.execute("select PNRNO from common2 where PassengerName = '%s'"%(k,))
                        messagebox.showinfo("Your PNRNO IS ",cur.fetchone())
                        mycon.close()
                    else :
                        messagebox.showerror("Error","you can't choose same city")
        Bi=Button(root,text="Insert",command=fun).grid(row=7,column=1)
        root.mainloop()
    else:
        print ("Unfortunately due to safety reasons you cannot be allowed to fly with us.")
def fun9():
    rootp.destroy()
    root4=tkinter.Tk()
    root4.title("Welcome,Search flights")
    Label(root4,text="Enter Boarding").grid(row=0,column=0)
    w1=Combobox(root4,height=5,width=15,values=["New  Delhi", "Mumbai","Ahmedabad","Srinagar","Bangalore" ,"Chennai","Kolkata","Jaipur"])
    w1.grid(row=0,column=1)
    Label(root4,text="select destination").grid(row=1,column=0)
    w2=Combobox(root4,height=5,width=15,values=["New Delhi","Mumbai","Ahmedabad","Srinagar","Bangalore","Chennai","Kolkata","Jaipur"])
    w2.grid(row=1,column=1)
    Label(root4,text="Choose date of travel").grid(row=2,column=0)
  
    w3=Combobox(root4,text="choose date",height=5,width=15,values=["20-03-2021","21-03-2021","22-03-2021","23-03-2021","24-03-2021","25-03-2021"])
    w3.grid(row=2,column=1)
    def fun10():
        a=w1.get()
        b=w2.get()
        c=w3.get()
        u=a.upper()
        v=b.upper()
        cur=mycon.cursor()
        if a=='' or b=='' or c=='':
            messagebox.showerror("Error","Cant leave any field empty")
        else:
            if a!=b:
                cur.execute("drop table display")
                sql5='''create table display(Boarding char(20),Destination char(20),Date char(20),Time varchar(25),Class char(10) ,Fare varchar(30))'''
                cur.execute(sql5)
                insert_stmt = "insert into display(Boarding,Destination,Date ,Time,Class,Fare ) values(%s, %s,%s,%s,%s,%s)"
                data = [("SRINAGAR","MUMBAI","20-03-2021","1:00","Economic","Rs.2500"), ('SRINAGAR','BANGALORE',"21-03-2021","4:00",'Business',"Rs.7500"),('SRINAGAR','NEW DELHI',"22-03-2021","7:00",'Economic',"Rs.5500"), ('SRINAGAR','chennai',"23-03-2021","4:00",'Economic',"Rs.5800") ,('MUMBAI','BANGALORE',"24-03-2021","9:00",' Business ',"Rs.6700"),('MUMBAI','AHMEDABAD',"25-03-2021","9:00",'Economic',"Rs.6000"), ('MUMBAI','KOLKATA',"21-03-2021","1:00",'Economic',"Rs6000") , ("BANGALORE",'CHENNAI',"22-03-2021","7:00",'Economic',"Rs.5790"),  ('BANGALORE','AHEMDABAD', "20-03-2021","4:00",'Business',"Rs.7564") ,('BANGALORE','SRINAGAR',"23-03-2021","1:00",'Economic',"Rs.6590"), ('BANGALORE','KOLKATA',"24-03-2021","1.00",'Economic',"Rs.5570"),('KOLKATA','MUMBAI',"25-03-2021","1:00",'Business',"Rs.4598"), ('KOLKATA','BANGALORE',"21-03-2021","7.00",'Economic',"Rs.4500"), ('KOLKATA','CHENNAI',"22-03-2021","1:00",'Business ',"Rs.5500"), ('NEW DELHI','SHRINAGAR',"23-03-2021" , "9:00",'Economic',"Rs.5040"), ('NEW DELHI','BANGALORE',"24-03-2021","1:00",'Economic',"Rs.5040"),  ('NEW DELHI','CHENNAI',"25-03-2021","1:00",'BUSINESS',"Rs.8040"), ('NEW DELHI','AHMEDABAD',"20-03-2021","7:00",'Economic',"Rs.5040"),('NEW DELHI','KOLKATA',"21-03-2021","4:00",'Economic',"Rs.5040"),('CHENNAI','NEW DELHI',"22-03-2021","1:00",'Business',"Rs.6900"), ('CHENNAI','MUMBAI',"23-03-2021","9:00",'Economic',"Rs.6600"), ('CHENNAI','KOLKATA',"24-03-2021","7:00",'Business',"Rs.7600"),('CHENNAI','SHRINAGAR',"25-03-2021","4:00",'Economic',"Rs.6600"), ('CHENNAI','AHMEDABAD',"20-03-2021","1:00",'Economic',"Rs.6600"), ('Ahmedabad','Chennai',"21-03-2021","7:00",'Economic',"Rs.5570"), ('Ahmedabad','KOLKATA',"22-03-2021","9:00",'Business',"Rs.9570"), ('Ahmedabad','Mumbai',"23-03-2021","1:00",'Economic',"Rs.4000"), ('SRINAGAR','BANGALORE',"25-03-2021","1:00",'Business',"Rs.10000"), ('KOLKATA','Ahmedabad ',"23-03-2021","4:00",'Economic',"Rs.3500"), ('Chennai','Bangalore',"24-03-2021","9:00",'Business',"Rs.2500"), ('Jaipur','Bangalore',"20-03-2021","9:00",'Business',"Rs.2900"), ('Jaipur',"MUMBAI","24-03-2021","1:00","Economic","Rs.2800"),('Jaipur','NEW DELHI',"22-03-2021","7:00",'Economic',"Rs.5500"), ('Jaipur','Kolkata',"22-03-2021","1:00","Economic","Rs.2800")]
                cur.executemany(insert_stmt, data)
                mycon.commit()
                cur.execute("select * from display where Boarding='%s' and Destination='%s' and Date='%s'"%(u,v,c))
                e=cur.fetchone()
                if e!=None:
                        messagebox.showinfo("flights available are",e)
                else:

                   messagebox.showinfo("about flight ","we do not provide services to these destinations ")
            else:
                  messagebox.showerror("Oops","boarding and destination can't be same")
    Bs=Button(root4,text="search",command=fun10).grid(row=5,column=0)
    root4.mainloop()
def fun8():
    rootp.destroy()
    root2=tkinter.Tk()
    root2.title("Welcome,Customer To our Cancellation System")
    Label(root2,text="Enter your PNRNO").grid(row=0,column=0)
    e1=Entry(root2)
    e1.grid(row=0,column=1)
    Label(root2,text="Enter PassengerName").grid(row=1,column=0)
    e2=Entry(root2)
    e2.grid(row=1,column=1)
    Label(root2,text="Choose your class").grid(row=2,column=0)
    w2=Combobox(root2,height=5,width=15,values=["Business","Economic"])
    w2.grid(row=2,column=1)
    Label(root2,text="select boarding").grid(row=3,column=0)
    w3=Combobox(root2,height=5,width=15,values=["New Delhi", "Mumbai", "Ahmedabad", "Srinagar", "Bangalore","Chennai",  "Kolkata","Jaipur"])
    w3.grid(row=3,column=1)
    def fun2():
        d=e1.get()
        t=e2.get()
        b=w2.get()
        c=w3.get()
        cur=mycon.cursor()
        if d=='' or b=='' or c=='' or t=='':
            messagebox.showerror("Oops","You can't Enter and leave any field empty")
        else:
            if b=="Economic":
                cur.execute("select * from economic2 where PNRNO=%s and PassengerName='%s'"%(d,t))
                messagebox.showinfo("Your reservation is cancelled",cur.fetchone())
                cur.execute("DELETE from economic2 where PNRNO=%s and PassengerName='%s'"%(d,t))
                mycon.commit()
                mycon.close()
            else:
                cur.execute("select * from common2 where PNRNO=%s and PassengerName='%s'"%(d,t))
                messagebox.showinfo("your reservation is cancelled",cur.fetchone())
                cur.execute("DELETE from common2 where PNRNO=%s and PassengerName='%s'"%(d,t))
                mycon.commit()
                mycon.close()
    Bc=Button(root2,text="Cancel Reservation",command=fun2).grid(row=5,column=0)
    root2.mainloop()
B1=Button(rootp,text="Cancel Booking",command=fun8).pack()
B2=Button(rootp,text="Search Flight",command=fun9).pack()
B3=Button(rootp,text="Book Flight",command=fun5).pack()
rootp.mainloop()
                                 
cur.execute("UPDATE   patients set stage=0 where Patient_id=%s"%(patient_id,))















                  
              





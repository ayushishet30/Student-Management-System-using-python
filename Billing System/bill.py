from tkinter import *
import math,random,os
from tkinter import messagebox

class BillApp:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color="#074463"
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        #=================Variables=================================
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.shampoo=IntVar()
        self.gel=IntVar()
        self.lotion=IntVar()
        #=================Grocery============================================
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.lentil=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.salt=IntVar()
        #===============Soft Drinks===================================
        self.coke=IntVar()
        self.breezer=IntVar()
        self.jeeru=IntVar()
        self.sprite=IntVar()
        self.fanta=IntVar()
        self.limca=IntVar()
        #==============Total Product Price and Tax Variable===============================================
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.softdrink_price=StringVar()

        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.softdrink_tax=StringVar()

        #==================Customer=========================================
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()
        #================================Customer Details Frame
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphn_lbl=Label(F1,text="Phone Number",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F1,width=15,textvariable=self.c_phon,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        c_bill_lbl=Label(F1,text="Bill Number",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_txt=Entry(F1,width=15,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)

        #============Cosmetic Frame===============
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=180,width=325,height=380)

        bath_lbl=Label(F2,text="Bath Soap", font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Face_cream_lbl=Label(F2,text="Face Cream", font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,pady=10,sticky="w")
        Face_cream_txt=Entry(F2,width=10,textvariable=self.face_cream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        Face_Wash_lbl=Label(F2,text="Face Wash", font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,pady=10,sticky="w")
        Face_Wash_txt=Entry(F2,width=10,textvariable=self.face_wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        Hair_s_lbl=Label(F2,text="Hair Shampoo", font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,pady=10,sticky="w")
        Hair_s_txt=Entry(F2,width=10,textvariable=self.shampoo,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        Hair_g_lbl=Label(F2,text="Hair Gel", font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,pady=10,sticky="w")
        Hair_g_txt=Entry(F2,width=10,textvariable=self.gel,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        bodylotion_lbl=Label(F2,text="Body Lotion", font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,pady=10,sticky="w")
        bodylotion_txt=Entry(F2,width=10,textvariable=self.lotion,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

 #============Grocery Frame===============
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=340,y=180,width=325,height=380)

        g1_lbl=Label(F3,text="Rice", font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,pady=10,sticky="w")
        g1_txt=Entry(F3,width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        g2_lbl=Label(F3,text="Food oil", font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,pady=10,sticky="w")
        g2_txt=Entry(F3,width=10,textvariable=self.food_oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        g3_lbl=Label(F3,text="Lentils", font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,pady=10,sticky="w")
        g3_txt=Entry(F3,width=10,textvariable=self.lentil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        g4_lbl=Label(F3,text="Wheat", font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,pady=10,sticky="w")
        g4_txt=Entry(F3,width=10,textvariable=self.wheat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        g5_lbl=Label(F3,text="Salt", font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,pady=10,sticky="w")
        g5_txt=Entry(F3,width=10,textvariable=self.salt,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        g6_lbl=Label(F3,text="Sugar", font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,pady=10,sticky="w")
        g6_txt=Entry(F3,width=10,textvariable=self.sugar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


#============Soft Drinks Frame===============
        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="SoftDrinks",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=670,y=180,width=325,height=380)

        bath_lbl=Label(F4,text="Coke", font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,pady=10,sticky="w")
        bath_txt=Entry(F4,width=10,textvariable=self.coke,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        c1_lbl=Label(F4,text="Breezer", font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,pady=10,sticky="w")
        c1_txt=Entry(F4,width=10,textvariable=self.breezer,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        c2_lbl=Label(F4,text="Jeeru", font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,pady=10,sticky="w")
        c2_txt=Entry(F4,width=10,textvariable=self.jeeru,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        c3_lbl=Label(F4,text="Sprite", font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,pady=10,sticky="w")
        c3_txt=Entry(F4,width=10,textvariable=self.sprite,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        c4_lbl=Label(F4,text="Fanta", font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,pady=10,sticky="w")
        c4_txt=Entry(F4,width=10,textvariable=self.fanta,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        c5_lbl=Label(F4,text="Limca", font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,pady=10,sticky="w")
        c5_txt=Entry(F4,width=10,textvariable=self.limca,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #============Bill Area Frame===============
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1010,y=180,width=530,height=380)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)


        #================Button Frame==========================
        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=560,relwidth=1,height=140)
        m1_lbl=Label(F6,text="Total Cosmetic Price",bg=bg_color,fg="lightgreen",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7, relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl=Label(F6,text="Total Grocery Price",bg=bg_color,fg="lightgreen",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=18,textvariable=self.grocery_price,font="arial 10 bold",bd=7, relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3_lbl=Label(F6,text="Total Soft Drinks Price",bg=bg_color,fg="lightgreen",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18,textvariable=self.softdrink_price,font="arial 10 bold",bd=7, relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)


        c1_lbl=Label(F6,text="Cosmetic Tax",bg=bg_color,fg="lightgreen",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_txt=Entry(F6,width=18,textvariable=self.cosmetic_tax,font="arial 10 bold",bd=7, relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        c2_lbl=Label(F6,text="Grocery Tax",bg=bg_color,fg="lightgreen",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2_txt=Entry(F6,width=18,textvariable=self.grocery_tax,font="arial 10 bold",bd=7, relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        c3_lbl=Label(F6,text="Soft Drinks Tax",bg=bg_color,fg="lightgreen",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3_txt=Entry(F6,width=18,textvariable=self.softdrink_tax,font="arial 10 bold",bd=7, relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=740,width=580,height=105)

        total_btn=Button(btn_F,command=self.total,text="Total",bg="black",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
        GBill_btn=Button(btn_F,text="Generate Bill",command=self.bill_area, bg="black",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=5)
        Clear_btn=Button(btn_F,text="Clear",command=self.clear_data,bg="black",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=5)
        Exit_btn=Button(btn_F,text="Exit",command=self.Exit_app,bg="black",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()

    def total(self):

        self.c_s_p= self.soap.get() * 40
        self.f_c= self.face_cream.get() * 120
        self.f_w= self.face_wash.get() * 60
        self.h_s= self.shampoo.get() * 180
        self.h_g=self.gel.get() * 140
        self.b_lo= self.lotion.get() * 180
        self.total_cosmetic_price = float(
        self.c_s_p
        +self.f_c
        +self.f_w 
        +self.h_s 
        + self.h_g
        +self.b_lo
    )
        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set("Rs. "+str(self.c_tax))
        


        self.r=self.rice.get() * 80
        self.f_o=self.food_oil.get() * 180
        self.le=self.lentil.get() * 60
        self.w=self.wheat.get() * 240
        self.sal=self.salt.get() * 45
        self.sug=self.sugar.get() * 150
        self.total_grocery_price = float(
        self.r 
        +self.f_o
        +self.le
        +self.w
        + self.sal
        +self.sug  
    )

        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price*0.1),2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))

        
        self.c=self.coke.get() * 75
        self.b=self.breezer.get()* 100
        self.j=self.jeeru.get() * 40
        self.s=self.sprite.get() * 60
        self.f=self.fanta.get() * 65
        self.l=self.limca.get() * 50
        self.total_softdrink_price = float(
        self.c 
        +self.b
        +self.j 
        +self.s
        +self.f
        +self.l
    )

        self.softdrink_price.set("Rs. "+str(self.total_softdrink_price))
        self.s_tax=round((self.total_softdrink_price*0.05),2)
        self.softdrink_tax.set("Rs. "+str(self.s_tax))

        self.Total_bill=float(self.total_cosmetic_price
                              +self.total_grocery_price
                              +self.total_softdrink_price
                              +self.c_tax
                              +self.g_tax
                              +self.s_tax
                              )

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWelcome to the Mart \n")
        self.txtarea.insert(END,f"\n Bill Number : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name: {self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone Number : {self.c_phon.get()}")
        self.txtarea.insert(END,f"\n ========================================")
        self.txtarea.insert(END,f"\n Products\t\tQTY\t Price")
        self.txtarea.insert(END,f"\n ========================================")
        
    def bill_area(self):
            if self.c_name.get()=="" or self.c_phon.get()=="":
                messagebox.showerror("Error","Customer details are mandatory")
            elif self.cosmetic_price.get()=="Rs 0.0" and self.grocery_price.get()=="Rs 0.0" and self.softdrink_price.get()=="Rs 0.0":
                messagebox.showerror("Error","No Product Purchased")
            else: 
                self.welcome_bill()
            
                #===============Cosmetic============================
                if self.soap.get()!=0:
                    self.txtarea.insert(END,f"\n Bath Soap \t\t{self.soap.get()}\t\t{self.c_s_p}")
                if self.face_cream.get()!=0:
                    self.txtarea.insert(END,f"\n Face Creame \t\t{self.face_cream.get()}\t\t{self.f_c}")
                if self.face_wash.get()!=0:
                    self.txtarea.insert(END,f"\n Face Wash \t\t{self.face_wash.get()}\t\t{self.f_w}")
                if self.shampoo.get()!=0:
                    self.txtarea.insert(END,f"\n Hair Shampoo \t\t{self.shampoo.get()}\t\t{self.h_s}")
                if self.gel.get()!=0:
                    self.txtarea.insert(END,f"\n Hair Gel \t\t{self.gel.get()}\t\t{self.h_g}")
                if self.lotion.get()!=0:
                    self.txtarea.insert(END,f"\n Body Lotion \t\t{self.lotion.get()}\t\t{self.b_lo}")            


                #==========Grocery=================================
                if self.rice.get()!=0:
                    self.txtarea.insert(END,f"\n Rice \t\t{self.rice.get()}\t\t{self.r}")
                if self.food_oil.get()!=0:
                    self.txtarea.insert(END,f"\n Food Oil \t\t{self.food_oil.get()}\t\t{self.f_o}")
                if self.lentil.get()!=0:
                    self.txtarea.insert(END,f"\n Lentils \t\t{self.lentil.get()}\t\t{self.le}")
                if self.wheat.get()!=0:
                    self.txtarea.insert(END,f"\n Wheat \t\t{self.wheat.get()}\t\t{self.w}")
                if self.salt.get()!=0:
                    self.txtarea.insert(END,f"\n Salt \t\t{self.salt.get()}\t\t{self.sal}")
                if self.sugar.get()!=0:
                    self.txtarea.insert(END,f"\n Sugar \t\t{self.sugar.get()}\t\t{self.sug}")      


                #==========Soft Drinks=================================
                if self.coke.get()!=0:
                    self.txtarea.insert(END,f"\n Coke \t\t{self.coke.get()}\t\t{self.c}")
                if self.breezer.get()!=0:
                    self.txtarea.insert(END,f"\n Breezer \t\t{self.breezer.get()}\t\t{self.b}")
                if self.jeeru.get()!=0:
                    self.txtarea.insert(END,f"\n Jeeru \t\t{self.jeeru.get()}\t\t{self.j}")
                if self.sprite.get()!=0:
                    self.txtarea.insert(END,f"\n Sprite \t\t{self.sprite.get()}\t\t{self.s}")
                if self.fanta.get()!=0:
                    self.txtarea.insert(END,f"\n Fanta \t\t{self.fanta.get()}\t\t{self.f}")
                if self.limca.get()!=0:
                    self.txtarea.insert(END,f"\n Limca \t\t{self.limca.get()}\t\t{self.l}")    


                self.txtarea.insert(END,f"\n--------------------------------------")
                if self.cosmetic_tax.get()!="Rs. 0.0":
                    self.txtarea.insert(END,f"\n Cosmetic Tax\t\t\t{self.cosmetic_tax.get()}")
                

                if self.grocery_tax.get()!="Rs. 0.0":
                    self.txtarea.insert(END,f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")
            
                if self.softdrink_tax.get()!="Rs. 0.0":
                    self.txtarea.insert(END,f"\n Soft Drinks Tax\t\t\t{self.softdrink_tax.get()}")
            
                self.txtarea.insert(END,f"\n Total Bill : \t\t\t Rs. {self.Total_bill}")
                self.txtarea.insert(END,f"\n--------------------------------------")
                self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no. : {self.bill_no.get()} Bill saved successfully")
        else:
            return
        
    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"): 
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"bills/ {i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid bill number")

    def clear_data(self):
         op=messagebox.askyesno("Clear","Do you really want to clear data?")
         if op>0:
            #=================Variables=================================
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.shampoo.set(0)
            self.gel.set(0)
            self.lotion.set(0)
            #=================Grocery============================================
            self.rice.set(0)
            self.food_oil.set(0)
            self.lentil.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.salt.set(0)
            #===============Soft Drinks===================================
            self.coke.set(0)
            self.breezer.set(0)
            self.jeeru.set(0)
            self.sprite.set(0)
            self.fanta.set(0)
            self.limca.set(0)
            #==============Total Product Price and Tax Variable===============================================
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.softdrink_price.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.softdrink_tax.set("")

            #==================Customer=========================================
            self.c_name.set("")
            self.c_phon.set("")
            self.bill_no.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()

    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.root.destroy()




        

root=Tk()
obj = BillApp(root)
root.mainloop()


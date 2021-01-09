# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 18:49:27 2019

@author: Anshul
"""
import os
import time

class Hospital_Billing():
    facility=['Bandage','Fracture','Cold','Fever','BP']
    charges=[400,8000,700,700,500]
    
    def front(self):
        print("\t\t\t<-------------Welcome To Our Hospitality Services------------->")
        print("\n\n\tServices Available:")
        for i in range(0,len(self.facility)):
            print("[",i+1,"] ",self.facility[i])
        print("\n\nSelect the Service You want:(1 to",len(self.facility),"): ",end="")
        self.selected_service=int(input())
        self.Billing()
    def Billing(self):
        print("\n\nEnter the Following Personal Details ")
        self.name=input("Name: ")
        self.age=int(input("Age(In Numbers): "))
        self.sex=input("Sex(m/f/o): ")
        self.bill_amount=self.charges[self.selected_service-1]
        print("\n\n\t\t:-) Please wait while we're generating your bill...........")
        time.sleep(2)
        bill="Name:"+self.name+"\nAge:"+str(self.age)+"\nSex:"+self.sex+"\nService:"+self.facility[self.selected_service-1]+"\n\nBill Amount:"+str(self.bill_amount)
        print(bill)
        choice=input("Do you Want to download Bill(y or n): ")
        if(choice in 'yes'):
            print("\n\n\t\t\tDownloading......")
            file_name=self.name+".txt"
            file=open(file_name,"w")
            file.write(bill)
            file.close()
            time.sleep(4)
            print("\n\n\t\tDownlaod completed\n\t\tBill has been saved in folder:",os.getcwd())  
        else:
            print("Happy to Serve You:-)   ...Bye")
            exit()

obj=Hospital_Billing()
obj.front()
time.sleep(100)

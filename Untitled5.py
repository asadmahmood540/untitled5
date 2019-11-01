#!/usr/bin/env python
# coding: utf-8

# In[ ]:


name = input("Enter Your Name")
father_name = input("Enter your Father's name")
uni = input("University")


message = """
PIAIC ISLAMABAD BATCH3
Name : {}
Father_Name: {} 
University: {}
"""

message1 = message.format(name, father_name, uni)

print(message1)
Enter Your Nameasad
Enter your Father's nameshahid
Universitybahria

PIAIC ISLAMABAD BATCH3
Name : asad
Father_Name: shahid 
University: bahria

In [1]:
name = input("Enter Your Name")
father_name = input("Enter your Father's name")
math=int(input("your math marks:"))
phy=int(input("your phy marks:"))
eng=int(input("your eng marks"))
chem=int(input("your chem marks:"))
urdu=int(input("your urdu marks"))


total=math+phy+eng+chem+urdu


percenti=total*100
float(percenti)
percenti/=500




message="""
    Board of Intermediate
    name:{}
    father_name:{}
    math marks:{}
    phy marks:{}
    eng marks:{}
    chem marks:{}
    urdu marks:{}
    total gain:{}
    out of:500
    percentage:{}
    

"""
message1=message.format(name,father_name,math,phy,eng,chem,urdu,total,percenti)

print(message1)
Enter Your Nameasad
Enter your Father's nameshahid
your math marks:45
your phy marks:65
your eng marks35
your chem marks:65
your urdu marks89

    Board of Intermediate
    name:asad
    father_name:shahid
    math marks:45
    phy marks:65
    eng marks:35
    chem marks:65
    urdu marks:89
    total gain:299
    out of:500
    percentage:59.8


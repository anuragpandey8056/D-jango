from django.shortcuts import render
from .models import *
# Create your views here.
def home():
    all_data= Student.objects.all()
    my_data=[]
    for i in all_data:
        name = i.Name
        email = i.Email
        contact = i.contact
        address = i.address
        dob = i.dob
        adhar_no = i.adharno
        createddata=i.adharno.CreatedDate
        createdby = i.adharno.createdBY
        data ={
            'name':name,
            'email':email,
            'contact':contact,
            'address':address,
            'dob':dob,
            'adhar_no':adhar_no,
            'createddata':createddata,
            'createdby':createdby,
        }
    my_data.append(data)
    print(my_data)

#!/media/carlos/DATA/anaconda3/envs/py37/bin/python
# @Author: carlos
# @Date:   2019-04-29T19:11:44-05:00
# @Email:  carlos.enciso.o@gmail.com
# @Last modified by:   carlos
# @Last modified time: 2019-05-08T18:09:10-05:00
# @License: Peruvian Geophysical Institute
# @Copyright: MIT
#-----------------------------------
# Importing modules
#-----------------------------------
import datetime
import numpy as np
import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt
import geopandas as gpd

class Areac:
    def __init__(self, area):
        self.area = area

class Perimeterc:
    def __init__(self, csize):
        self.perimeter = csize**2
        color = rgb(13, 120, 107)
#-----------------------------------
# Creating Classes
#-----------------------------------
class Employee:
    num_of_emps = 0
    raise_amt = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_emps += 1

    @property
    def email(self):
        retunr '{}.{}@company.com'.format(first,last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = 'None'
        self.last = 'None'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

class Developer(Employee):
    raise_amt = 1.10
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def  add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())




emp_1 =  Employee('Corey', 'Schafer', 50000)
emp_2 =  Employee('Test', 'User', 60000)
my_date = datetime.date(2016, 7, 11)
# print(Employee.is_workday(my_date))

dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 =  Developer('Test', 'User', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
print(issubclass(Manager, Developer))

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 16:53:25 2019

@author: jasonshu
"""
from datetime import datetime as dt

def convert_to_date(date_str):
    date_obj = dt.strptime(date_str, '%Y-%m-%d')  #YYYY-MM-DD
    return date_obj


class Person:
    def __init__(self, first, last, major, birthdate):
        self.first_name = first
        self.last_name = last
        self.major = major
        self.birthdate = convert_to_date(birthdate)            
        return None
 
    def get_birthyear(self):
        year = self.birthdate.year
        return year

    def store_a_story(self):
        phrase = "{first} was born on {date}, which was a {weekday}. His major is {major}"
        self.phrase = phrase.format(first=self.first_name, date=self.birthdate, weekday=self.birthdate.weekday(), major=self.major)
    
    def tell_me_a_story(self):
        self.store_a_story()
        print(self.phrase)
        
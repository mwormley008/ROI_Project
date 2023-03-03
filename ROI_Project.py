#!/usr/bin/env python3
'''
    File name: ROI_Project.py
    Author: Michael Wormley
    Date created: 3/3/2023
    Date last modified: 3/3/2023
    Python Version: 3.10.9
'''
"""
This program is essentially a calculator used to calculate the return on investment
on things like rental properties, by taking in income, cash flow, expenses, and then 
returning ROI.
"""

class ROI:

    def __init__(self, income, expense):
        self.
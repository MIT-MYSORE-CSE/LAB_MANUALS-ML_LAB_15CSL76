# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 21:43:21 2019

@author: Prasanna Patil
"""
import csv
attributes =[['Sunny','Rainy'],['Warm','Cold'],['Normal','High'],['Strong','Weak'],['Warm','Cool'],['Same','Change']]
num_attributes = len(attributes)
print("\n The most general hypothesis : ['?','?','?','?','?','?'] \n")
print("\n The most specific hypothesis : ['0','0','0','0','0','0'] \n")
print("\n The given training data set \n")
csvFile= open(r"lab1.csv")
reader = csv.reader(csvFile)
a=list(reader)
print(a)
print("\n The initial value of hypothesis :")
hypothesis = ['0']*num_attributes
print(hypothesis)
#comparing with all training examples
for i in range(0,len(a)):# i varies from 0 to 3
    if(a[i][6]=='Yes'):
        for j in range(num_attributes): 
            hypothesis[j] = a[i][j]
        break
    
#comparing with remaining training examples of given data set
print("\n Find S: Finding a maximally specific hypothesis \n")

for i in range(0,len(a)): # i valies from 0 to 3, len(a) is 4, i.e, 4 instances in dataset
    if a[i][num_attributes]=='Yes':  # checking the label/target is "yes" or "no"
        for j in range(0,num_attributes): # j varies from 0 to 5
            if a[i][j]!=hypothesis[j]:  # check 1st instance's 1st attribute value  is same as hypothesis's 1st value or not
                hypothesis[j]='?'       # if no then replace the old hypothesis by "?"
            else:
                hypothesis[j]=a[i][j]   # if yes then copy the attibute value to respective hypothesis
    print("For Training Example No : {0} the hypothesis is".format(i),hypothesis)
print("\n The Maximally Specific Hypothesis for a given Training Examples :\n")
print(hypothesis)

# -*- coding: utf-8 -*-
import math
import sys
from prettytable import PrettyTable

def getgenes():
    age = raw_input("Enter the age in years: ")
    decades = int(age)//10
    ht = raw_input("Enter the height in cm: ")
    height = float(ht)
    wt = raw_input("Enter the weight in kg: ")
    weight = float(wt)
    race = raw_input("What is the race?\nType A for Asian\nType B for Black\nType C for Caucasian\nType U for Unknown or mixed race\n")
    if race.upper() != 'A' and race.upper() != 'B' and race.upper() != 'C' and race.upper() == 'U':
        print("Enter a valid option")
        sys.exit()
    enz = raw_input("Are you on carbamazepine, phenytoin, rifampin, or rifampicin?\nType Y for yes and N for no/don't know\n")
    if enz.upper() != 'Y' and enz.upper() != 'N':
        print("Enter a valid option")
        sys.exit()
    ami = raw_input("Are you on amiodarone?\nType Y for yes and N for no/don't know\n")
    if ami.upper() != 'Y' and ami.upper() != 'N':
        print("Enter a valid option")
        sys.exit()
    dosage = raw_input("What is Warfarin the dosage per week?\n")
    dose = int(dosage)
    computegenes(dose,decades,height,weight,race,enz,ami)
    


def bobgenes():
    age = 56
    decades = age // 10
    height = 177.8
    weight = 72
    dose = 21
    race = 'C'
    enz = 'Y'
    ami = 'Y'
    if race.upper() == 'A':
        r = 'Asian'
    if race.upper() == 'B':
        r = 'Black'
    if race.upper() == 'U':
        r = 'Unknown or mixed race'
    if race.upper() == 'C':
        r = 'Caucasian'
    if enz.upper() == 'Y':
        e = 'takes'
    if enz.upper() == 'N':
        e = 'does not take'
    if ami.upper() == 'Y':
        a = 'takes'
    if ami.upper() == 'N':
        a = 'does not take'
    print('\nBob\'s age is {0} with his height being {0} cm and weight equal to {2} kg. His Warfarin dosage per week is {3} mg. Also, he {4} enzyme-inducers like carbamazepine, phenytoin, rifampin, or rifampicin and {5} amiodarone\n'.format(age,height,weight,dose,e,a))
    computegenes(dose,decades,height,weight,race,enz,ami)


def computegenes(dose,decades,height,weight,race,enz,ami):
    temp = math.sqrt(dose)
    temp = temp - 5.6044 + (0.26145 * decades) - (0.0087 * height) - (0.0128 * weight)
    if race.upper() == 'A':
        temp = temp + 0.1092
    if race.upper() == 'B':
        temp = temp + 0.2760
    if race.upper() == 'U':
        temp = temp + 0.1032
    if enz.upper() == 'Y':
        temp = temp - 1.1816
    if ami.upper() == 'Y':
        temp = temp + 0.5503

    temp = temp * -1
    print('Genetic information is as follows: ')
    t = PrettyTable(['VKORC1', 'CYP2C9','Closeness to actual value'])
    for k1,v1 in VKORC1.items():
        for k2,v2 in CYP2C9.items():
             p = temp - (v1 + v2)
             closeness = p
             if p < 0:
                 p = p * -1
             if p < 0.25:
                 genes['VKORC1'] = k1
                 if k2 != "Unknown":
                     genes['CYP2C9'] = '*' + k2[:2] + '*' + k2[2:]
                 else:
                     genes['CYP2C9'] = k2
                 t.add_row([genes['VKORC1'],genes['CYP2C9'],closeness])

    print(t)



if __name__ == '__main__':
    VKORC1 = {}
    genes = {}
    genes['VKORC1'] = ''
    genes['CYP2C9'] = ''
    VKORC1['A/G'] = 0.8677
    VKORC1['A/A'] = 1.6974
    VKORC1['G/G'] = 0.0
    VKORC1['Unknown'] = 0.4854
    CYP2C9 = {}
    CYP2C9['1/1'] = 0.0
    CYP2C9['1/2'] = 0.5211
    CYP2C9['1/3'] = 0.9357
    CYP2C9['2/2'] = 1.0616
    CYP2C9['2/3'] = 1.9206
    CYP2C9['3/3'] = 2.3312
    CYP2C9['Unknown'] = 0.2188
    getanswer = raw_input("To get Bob's genetic information, type B. To get someone else's genetic information, type X:\n")
    if getanswer.upper() == 'B':
        bobgenes()
    if getanswer.upper() == 'X':
        getgenes()
    if getanswer.upper() != 'X' and getanswer.upper() != 'B':
        print('Not a valid option!')


    


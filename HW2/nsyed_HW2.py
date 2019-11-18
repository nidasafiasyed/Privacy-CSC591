import numpy as np
import re,sys
import csv
from matplotlib import pyplot as plt

#reading the CSV file, and creating a list of salaries
def read_file(filename):
    with open(filename,'r',) as csvfile:
        s=[]
        readcsv=csv.reader(csvfile,delimiter=',')
        next(readcsv)
        for row in readcsv:
            #salary=re.sub("$|,", "", row[2])
            if len(row[2]) > 0:
                salary=row[2].replace(',', "").replace(" ","").replace("$","")
                salary=int(salary)
                s.append(salary)
    get_hist(s,bins)
    get_dphist(s,bins)


#plotting a histogram of number of salaries with salary range buckets
def get_hist(s,bins):
    plt.hist(s,bins,color="skyblue",ec="blue")
    plt.title("Number of employees in different salary brackets")
    plt.xlabel("Salary in USD")
    plt.ylabel("Number of employees")
    plt.show()


#plotting a histogram of salaries with noise
def get_dphist(s,bins):
    lambda1=40 #epsilon=0.05
    lambda2=20 #epsilon=0.1
    lambda3=0.4 #epsilon=5

    noise1=get_noise(s,lambda1)
    noise2=get_noise(s,lambda2)
    noise3=get_noise(s,lambda3)

    legend = ['Actual Salaries', 'With $\epsilon$ = 0.05' , 'With $\epsilon$ = 0.1','With $\epsilon$ = 5.0']
    plt.hist([s,noise1,noise2,noise3],bins,edgecolor='black')
    plt.xlabel('Salary in USD')
    plt.ylabel('Number of Employees')
    plt.title('Number of employees in different salary brackets')
    plt.legend(legend)
    plt.show()

#calculating noise with laplace distribution
def get_noise(s,scale):
    loc=0.
    noise=[]
    for salary in s:
        t=salary + np.random.laplace(loc, scale, 1)
        noise.append(t)
    return noise


if __name__ == "__main__":
    fname="IL_employee_salary.csv"
    bins=[50000,52500,55000,57500,60000,62500,65000,67500,70000,72500,75000,77500,80000,82500,85000,87500,90000,92500,95000,97500,100000]
    read_file(fname)


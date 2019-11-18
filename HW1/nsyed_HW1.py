import re, sys
import math, random
import numpy as np
from collections import defaultdict
from collections import Counter
import operator

#### BEGIN----- functions to read movie files and create db ----- ####

p={}
minp={}

def add_ratings(db, chunks, num):
    if(not (chunks[0] in db)):
        db[chunks[0]] = {}
    db[chunks[0]][num] = int(chunks[2])

def read_files(db, num):
    movie_file = "movies/"+num
    ratings = []
    fo = open(movie_file, "r")
    r = 0
    max = 0
    min = 1
    for line in fo:
        chunks = re.split(",", line)
        chunks[len(chunks)-1] = chunks[len(chunks)-1].strip()

        add_ratings(db, chunks, num)



#### END----- functions to read movie files and create db ----- ####

def score(w, p, aux, r):
    '''
    Inputs: weights of movies, max rating per moive, auxiliary information, and a record, 
    Returns the corresponding score
    '''
    #### ----- your code here ----- ####
    count = 0
    for movie in aux.keys():
        count+=1
    suppaux = count

    s=0
    t=0
    # returns score for each movie
    for movie in aux.keys():
        if movie in r:
            t=1-(abs(aux[movie]-r[movie])/p[movie])
            s+=(w[movie]*(t/suppaux))
    return s


def getscore(w,p,aux,db):
    scores={}
    sc=0
    
    #get score for each user
    for userid in db.keys():
        scores[userid]=score(w,p,aux,db[userid])

    #get maximum 2 scores
    h1,h2=printoutput(scores,db,aux)
    
    return h1,h2 

   
def printoutput(scores,db,aux):

    #get maximum scores and print
    userratings={}

    maxuser=max(scores,key=scores.get)

    maxscore=scores[maxuser]

    maxscore2=0


    for sc in scores.values(): 
        if(sc > maxscore2 and sc < maxscore): 
            maxscore2=sc

    print "\nHighest score: ", maxscore

    print "\nSecond highest score: ", maxscore2

    print "\nUser with maximum score: ", maxuser
    
    #print maximum score's user's ratings
    print "\nRatings done by user", maxuser
    print "----------------"
    print "{:<8} {:<15} ".format('Movie','Rating')
    print "----------------"
    userratings=db[maxuser]
    for movie, rating in sorted(userratings.items()):
        print "{:<8} {:<15} ".format(movie, rating)
    
    #Compare the AUX table and maximum score's user ratings 
    print "\nComparing Aux and user ratings"

    print "-------------------------------------"
    print "{:<8} {:<15} {:<24} ".format('Movie','AUX Rating','User Rating')
    print "-------------------------------------"
    for movie, rating in sorted(aux.items()):
        if movie in userratings:
            print "{:<8} {:<15} {:<24} ".format(movie, rating, userratings[movie])
   
    return maxscore,maxscore2

#compute eccentricity
def eccentricity(g,w,aux):
    count=0
    
    for movie in aux.keys():
        count+=1
    
    suppaux=count

    m=0
    ecc=0
    g=0.1
    for movie in aux.keys():
        m+=(w[movie]/suppaux)

    ecc=g*m
    return ecc

#compute range of ratings of movies
def rating(db, aux):
    minrating={}
    maxrating={}
    p={}
    for userid in db.values():
        for movie,rating in userid.items():
            if movie not in minrating:
                minrating[movie]=rating
            else:
                if rating < minrating[movie]:
                    minrating[movie]=rating
            if movie not in maxrating:
                maxrating[movie]=rating
            else:
                if rating > maxrating[movie]:
                    maxrating[movie]=rating

    for movie in aux.keys():
        if movie in maxrating:
            if aux[movie] > maxrating[movie]:
                #print(aux[movie])
                maxrating[movie]=aux[movie]


    return maxrating
    #print(p)

def compute_weights(db):
    '''
    Input: database of users
    Returns weights of all movies
    '''
    #### ----- your code here ----- ####
    #Dictionary to store movie titles with their frequency
    #movies = [movie for v in db.values() for movie in v.keys()]

    # occurs = Counter(movies)

    # Count each unique element and build a dictionary
    #print occurs
    supp={}
    countuser={}

    for userid in db.values():
        for movie in userid.keys():
            if movie in supp:
                supp[movie]+=1
            else:
                supp[movie]=1
    
    for userid in db.keys():
        if userid not in countuser:
            countuser[userid]=1
        else:
            countuser[userid]+=1
               
    wt={}
    print "Movies with their weights"
    print "----------------"
    print "{:<8} {:<15} ".format('Movie','Weight')
    print "----------------"
    for movie, count in supp.items():
        wt[movie]=1/math.log(count)
    
    for movie, weight in wt.items():
        print "{:<8} {:<15} ".format(movie, weight)

    #print wt

    for userid in db.keys():
        if userid not in countuser:
            countuser[userid]=1
        else:
            countuser[userid]+=1
    print "\nThe number of users are:", len(countuser)

    return wt

#compare difference between highest 2 scores and eccentricity
def isdiff(ecc,diff):
    if diff>ecc:
        print "\nDifference between the highest and second highest score is greater than the eccentricity metric"
    else:
        if diff<ecc:
            print "\nDifference between the highest and second highest score is lesser than the eccentricity metric"
        else:
            print "\nDifference between the highest and second highest score is equal to the eccentricity metric"


#### BEGIN----- additional functions ----- ####



#### END----- additional functions ----- ####

if __name__ == "__main__":
    db = {}
    files = ["03124", "06315", "07242", "16944", "17113",
            "10935", "11977", "03276", "14199", "08191",
            "06004", "01292", "15267", "03768", "02137"]
    for file in files:
        read_files(db, file)

    aux = { '14199': 4.5, '17113': 4.2, '06315': 4.0, '01292': 3.3,
            '11977': 4.2, '15267': 4.2, '08191': 3.8, '16944': 4.2,
            '07242': 3.9, '06004': 3.9, '03768': 3.5, '03124': 3.5}

    #### ----- your code here ----- ###
    w = compute_weights(db)
    p = rating(db,aux)
    h1,h2=getscore(w,p,aux,db)
    diff=h1-h2
    #gamma value
    g=0.1
    ecc=eccentricity(g,w,aux)
    print "\nThe eccentricity with gamma value {} is {}".format(g,ecc)
    print "\nDifference between the highest and second highest score", diff
    isdiff(ecc,diff)

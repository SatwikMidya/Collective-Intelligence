from recommendation import critics
from math import sqrt


# Eucledian Distance Similarity score

# Distance --> the smaller it gets more simillar we want opposite
# our score= 1/(1+distance)  it ensures large value means more simillar and value score=1 is perfectly simillar (Distance can be zero)

# function returns a distance based similarity score between two person

def sim_distance(prefs,person1,person2):
    # get the list of shared items
    si={}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item]=1
    # if they have no ratings in common return zero
    if len(si)==0: return 0

    # Add all sqaure of differences
    sumofSqaures =  sum([pow(prefs[person1][item]-prefs[person2][item],2) 
                        for item in prefs[person1] if item in prefs[person2]])
    return 1/(1+sumofSqaures)


# Pearson Corelation score 
def sim_pearson(prefs,person1,person2):
    si={}
    for item in prefs[person1]:
        if item in prefs[person2]: si[item]=1
    
    n=len(si)
    if n==0 : return 0

    # sum of preferences 
    sum1=sum([prefs[person1][item] for item in si])
    sum2=sum([prefs[person2][item] for item in si])

    # sum of square 
    sumsq1=sum([pow(prefs[person1][item],2) for item in si])
    sumsq2=sum([pow(prefs[person2][item],2) for item in si])

    # sum of products
    psum=sum([prefs[person1][item]*prefs[person2][item] for item in si])

    # calculate pearson score
    num=psum-((sum1*sum2)/n)
    den=sqrt((sumsq1-pow(sum1,2)/n)*(sumsq2-pow(sum2,2)/n))
    if den==0: return 0
    r=num/den

    return r

def topMatches(prefs,person,n=5,similarity=sim_pearson):
    scores=[(similarity(prefs,person,others),others) for others in prefs if others != person]

    scores.sort()
    scores.reverse()
    return scores[0:n]

def getRecommendation(prefs,person,similarity=sim_pearson):
    total={}
    simSums={}
    for other in prefs:
        if other == person: continue
        sim=similarity(prefs,person,other)

        if sim<=0: continue

        for items in prefs[other]:
            if items not in prefs[person] or prefs[person][items]==0:
                total.setdefault(items,0)
                total[items]+=prefs[other][items]*sim
                simSums.setdefault(items,0)
                simSums[items]+=sim
    
    rankings = [(total/simSums[items],items) for items,total in total.items()]

    rankings.sort()
    rankings.reverse()
    return rankings








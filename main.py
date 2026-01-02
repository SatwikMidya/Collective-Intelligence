
# critics['Toby']['Sankes on a Plane']=2.5
# print(critics['Toby'])
from recommendation import critics
from functions import sim_distance
from functions import sim_pearson
from functions import topMatches
from functions import getRecommendation

print(sim_distance(critics,'Lisa Rose','Gene Seymour'))
print(sim_pearson(critics,'Lisa Rose','Gene Seymour'))
print(topMatches(critics,'Toby',n=3))
print(getRecommendation(critics,'Toby'))
print(getRecommendation(critics,'Toby',similarity=sim_distance))


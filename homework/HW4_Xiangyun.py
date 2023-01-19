import json
import requests
import webbrowser
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

import random as random
from matplotlib.path import Path
import numpy as np
from nltk.corpus import stopwords

import re
from collections import Counter

## Step 1: Obtain the json file "RedliningData"
response = requests.get("https://dsl.richmond.edu/panorama/redlining/static/downloads/geojson/MIDetroit1939.geojson")
RedliningData = json.loads(response.text)
# print(RedliningData)
f = open('RedliningData.json', 'w', encoding='UTF-8')
json.dump(RedliningData, f, ensure_ascii=False)
f.close()

## Step 2:
class DetroitDistrict:

     def __init__(self, dict):
        self.Coordinates = dict["geometry"]["coordinates"][0][0]
        self.HolcGrade = dict["properties"]["holc_grade"]
        for i in range(4):
            if ["A", "B", "C", "D"][i] == dict["properties"]["holc_grade"]:
                self.HolcColor = ["darkgreen", "cornflowerblue", "gold", "maroon"][i]
        self.name = dict["properties"]["holc_id"]
        self.Qualitative_Description= dict["properties"]["area_description_data"]["8"]
        self.RandomLat = 0
        self.RandomLong = 0
        self.tract_code = 0
        self.median_household_income = 0

## Step 5:
     def get_tract_code(self, cache = None):
         if cache == None:
            response = requests.get("https://geo.fcc.gov/api/census/area?", {"lat": self.RandomLat, "lon": self.RandomLong,"censusYear": "2010"})
            result = json.loads(response.text)
            self.tract_code = result["results"][0]["block_fips"]
         else:
            self.tract_code = cache["census tract"]
    
## Step 6:
     def get_median_household_income(self, cache = None):
         if cache == None:
            response = requests.get("https://api.census.gov/data/2018/acs/acs5?", {"get":"B19013_001E", "for": "tract:"+self.tract_code[5:11], "in": "state:"+self.tract_code[:2]+"%20county:"+self.tract_code[2:5]})
            result = json.loads(response.text)
            self.median_household_income = result[1][0]
         else:
            self.median_household_income = cache["income info"]
        

Districts = [DetroitDistrict(i) for i in RedliningData['features']]
# print(Districts)
# print(len(Districts))

## Step 3:
fig, ax = plt.subplots()

for i in Districts:
    ax.add_patch(plt.Polygon(i.Coordinates, facecolor = i.HolcColor, edgecolor='Black'))
    ax.autoscale()
plt.rcParams["figure.figsize"] = (15,15)

plt.show()

## Step 4:
try:
    with open("SI507_json_cache.json", "r") as f:
        Cache = json.load(f)
    for i in range(len(Districts)):
        Districts[i].RandomLat = Cache[i]["random lat"]
        Districts[i].RandomLong = Cache[i]["random long"]
except:
    xgrid = np.arange(-83.5,-82.8,.004)
    ygrid = np.arange(42.1, 42.6, .004)
    xmesh, ymesh = np.meshgrid(xgrid,ygrid)
    points = np.vstack((xmesh.flatten(),ymesh.flatten())).T
    for j in Districts:
        p = Path(j.Coordinates)
        grid = p.contains_points(points)
        print(j," : ", points[random.choice(np.where(grid)[0])])
        point = points[random.choice(np.where(grid)[0])]
        j.RandomLong = point[0]
        j.RandomLat = point[1]

# print(Districts[0].RandomLat)
# print(Districts[0].RandomLong)
# Districts[0].get_tract_code() 
# print(Districts[0].tract_code)

## Step 5:
# List = []
try:
    with open("SI507_json_cache.json", "r") as f:
        Cache = json.load(f)
    for i in range(len(Districts)):
        Districts[i].get_tract_code(cache=Cache[i])
except:
    for i in Districts:
        i.get_tract_code() 
#     List.append(i.tract_code)
# print(List)


## Step 6:
try:
    with open("SI507_json_cache.json", "r") as f:
        Cache = json.load(f)
    for i in range(len(Districts)):
        Districts[i].get_median_household_income(cache=Cache[i])
except:
    for i in Districts:
        i.get_median_household_income()

# print(Districts[0].median_household_income)
# print(Districts[100].median_household_income)

## Step 7:
List = []
for i in Districts:
    dict = {"income info": i.median_household_income, "random lat": i.RandomLat, "random long": i.RandomLong, "census tract" : i.tract_code}
    List.append(dict)

# print(List)

with open("SI507_json_cache.json", "w") as f:
    json.dump(List, f)
f.close()


## Step 8:
Grade_A = []
Grade_B = []
Grade_C = []
Grade_D = []
def median(list):
    list.sort()
    list_length = len(list)
    if list_length % 2 == 0:
        return (list[int(list_length / 2) - 1] + list[int(list_length / 2)]) / 2 
    return list[int(list_length / 2)]

for i in Districts:
    if i.HolcGrade == "A":
        Grade_A.append(int(i.median_household_income))
    elif i.HolcGrade == "B":
        Grade_B.append(int(i.median_household_income))
    elif i.HolcGrade == "C":
        Grade_C.append(int(i.median_household_income))
    else:
        Grade_D.append(int(i.median_household_income))

A_mean_income = np.mean(Grade_A)
A_median_income = median(Grade_A)

B_mean_income = np.mean(Grade_B)
B_median_income = median(Grade_B)

C_mean_income = np.mean(Grade_C)
C_median_income = median(Grade_C)

D_mean_income = np.mean(Grade_D)
D_median_income = median(Grade_D)

# print(A_mean_income)
# print(A_median_income)
# print(B_mean_income)
# print(B_median_income)
# print(C_mean_income)
# print(C_median_income)
# print(D_mean_income)
# print(D_median_income)

# Step 9:
str_A = ""
str_B = ""
str_C = ""
str_D = ""
for i in Districts:
    if i.HolcGrade == "A":
        str_A = str_A + i.Qualitative_Description
    elif i.HolcGrade == "B":
        str_B = str_B + i.Qualitative_Description
    elif i.HolcGrade == "C":
        str_C = str_C + i.Qualitative_Description
    else:
        str_D = str_D + i.Qualitative_Description


word_list_A = re.split(r"\s+", str_A)
word_list_B = re.split(r"\s+", str_B)
word_list_C = re.split(r"\s+", str_C)
word_list_D = re.split(r"\s+", str_D)


stop_words = set(stopwords.words('english'))
filtered_A = [w.lower() for w in word_list_A if (not w in stop_words) & (w not in ["area", "area.", "section", "sheet"])]
A_10_Most_Common = Counter(filtered_A).most_common(10)
print(A_10_Most_Common)
# seems A is high quality
filtered_B = [w.lower() for w in word_list_B if (not w in stop_words) & (w not in ["area", "area.", "section", "sheet"])]
B_10_Most_Common = Counter(filtered_B).most_common(10)
print(B_10_Most_Common)

filtered_C = [w.lower() for w in word_list_C if (not w in stop_words) & (w not in ["area", "area.", "section", "sheet"])]
C_10_Most_Common = Counter(filtered_C).most_common(10)
print(C_10_Most_Common)

filtered_D = [w.lower() for w in word_list_D if (not w in stop_words) & (w not in ["area", "area.", "section", "sheet"])]
D_10_Most_Common = Counter(filtered_D).most_common(10)
print(D_10_Most_Common)


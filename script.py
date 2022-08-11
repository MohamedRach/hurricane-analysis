# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def convert(list):
    new_damages_list = []
    for damage in list:
        if damage != "Damages not recorded":
            if damage[-1] == "M":
                convert_float = float(damage[:-1])*1000000
                new_damages_list.append(convert_float)
            else:
                convert_float = float(damage[:-1])*1000000000
                new_damages_list.append(convert_float)
        #else:                                                          # i commented this section so that i can use this function later on
            #new_damages_list.append("Damages not recorded")
    return new_damages_list
#print(convert(damages))

# construct hurricane dictionary:

def create_dict(list1,list2,list3,list4,list5,list6,list7):
    hurricans = {}
    for i in range(0,34):
        hurricans.update({list1[i]: {"Name": list1[i],"Month":list2[i],"Year":list3[i],'Max Sustained Wind':list4[i],"Areas Affected":list5[i],"Damage":list6[i],"Deaths":list7[i]}})
    return hurricans

hurricans = (create_dict(names,months,years,max_sustained_winds,areas_affected,damages,deaths))

# construct hurricane by year dictionary:

def year_dict(hurr):
    dict_by_years = {}
    for value in list(hurr.values()):
        dict_by_years.update({value.get("Year"):value})
    return dict_by_years
hurricans_by_year = year_dict(hurricans)

# count affected areas function:

def areas_affected_count(hurr):
    count_of_areas_affected = {}
    area_count = 0
    for value in list(hurr.values()):
        areas_affected_list = value.get("Areas Affected")
        for area in areas_affected_list:
            if area in count_of_areas_affected:
                count_of_areas_affected[area] += areas_affected_list.count(area)
            else:
                area_count += areas_affected_list.count(area)
                count_of_areas_affected.update({area:area_count})
    return count_of_areas_affected
                
count_of_areas_affected = areas_affected_count(hurricans)



#most affected area function:

def most_affected_area_(dict):
    most_affected_area = max(list(dict.values()))
    for key, val in dict.items():
        if val == most_affected_area:
            affected_area = key
    return "most affected ares is: " + affected_area + " with a count of " + str(most_affected_area)
most_affected_area = most_affected_area_(count_of_areas_affected)

#greatest number of deaths:

def deaths(hurr):
    deaths_list = []
    for value in list(hurr.values()):
        deaths_list.append(value.get("Deaths"))
        max_deaths = max(deaths_list)
        for key , val in value.items():
            if val == max_deaths:
                area_with_biggest_deaths = value.get("Name")
    return "the hurrican with most deaths is " + area_with_biggest_deaths + " number of deaths is: " + str(max_deaths)
hurrican_with_most_deaths = deaths(hurricans)

#catgeorize by mortality:

def hurricans_mortality_rating(hurr):
    hurricans_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}
    for value in list(hurr.values()):
        death = value.get("Deaths")
        if death == 0:
            hurricans_mortality[0].append(value.get("Name"))     #hurricans_mortality[0].append(value)
        elif death > 0 and death <= 100:
            hurricans_mortality[1].append(value.get("Name"))
        elif death > 100 and death <= 500:
            hurricans_mortality[2].append(value.get("Name"))
        elif death > 500 and death <= 1000:
            hurricans_mortality[3].append(value.get("Name"))
        elif death > 1000 and death <= 10000:
            hurricans_mortality[4].append(value.get("Name"))
        elif death > 10000:
            hurricans_mortality[5].append(value.get("Name"))
    return hurricans_mortality
hurricans_mortality = hurricans_mortality_rating(hurricans)

# greatest damage:

def greatest_damage(hurr):
    list_of_damages = []
    list_of_hurricans = []
    for value in list(hurr.values()):
        list_of_damages.append(value.get("Damage"))
        list_of_hurricans.append(value.get("Name"))
    convert_damages_to_floats = convert(list_of_damages)
    biggest_damage = max(convert_damages_to_floats)
    for hurrican in list_of_hurricans:
        if list_of_hurricans.index(hurrican) == convert_damages_to_floats.index(biggest_damage):
            hurrican_with_biggest_damage = hurrican
    return "the hurrican with the biggest damage is: " + hurrican_with_biggest_damage + " it costs " + str(biggest_damage)
hurrican_with_biggest_damage = greatest_damage(hurricans)
#print(hurrican_with_biggest_damage)

# catgeorize by damage:

def damage_rating(hurr):
    damage_ratings = {0:[],1:[],2:[],3:[],4:[],5:[]}
    list_of_damages = []
    list_of_hurricans = []
    for value in list(hurr.values()):
        list_of_damages.append(value.get("Damage"))
        list_of_hurricans.append(value.get("Name"))
    convert_damages_to_floats = convert(list_of_damages)
    for damage in convert_damages_to_floats:
        if damage == 0:
            damage_ratings[0].append(list_of_hurricans[convert_damages_to_floats.index(damage)])     #hurricans_mortality[0].append(value)
        elif damage > 0 and damage <= 100000000:
            damage_ratings[1].append(list_of_hurricans[convert_damages_to_floats.index(damage)])
        elif damage > 100000000 and damage <= 1000000000:
            hurricans_mortality[2].append(list_of_hurricans[convert_damages_to_floats.index(damage)])
        elif damage > 1000000000 and damage <= 10000000000:
            hurricans_mortality[3].append(list_of_hurricans[convert_damages_to_floats.index(damage)])
        elif damage > 10000000000 and damage <= 50000000000:
            damage_ratings[4].append(list_of_hurricans[convert_damages_to_floats.index(damage)])
        elif damage > 50000000000:
            damage_ratings[5].append(list_of_hurricans[convert_damages_to_floats.index(damage)])
    return damage_ratings

damage_ratings = damage_rating(hurricans)
#print(damage_ratings)
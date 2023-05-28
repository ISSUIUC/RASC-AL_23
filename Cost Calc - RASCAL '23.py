#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np

print("This script calculates the price for MORROW.")

#initializes cost catagories
operations_pro = np.zeros(26) #yearly operations cost over the whole project lifecycle
operations_total = 0 #the total cost of operating MITHRIL once its operation - e.g. cost of ground control employees

services_pro = np.zeros(26) #yearly services cost over the whole project lifecycle
services_total = 0 #total cost of services, e.g. launch or use of the DSN antennas

design_pro = np.zeros(26) #yearly design cost over the whole project lifecycle
design_total = 0 #total cost of the design of MITHRIL

fabrication_pro = np.zeros(26) #yearly fabrication cost over the whole project lifecycle
fabrication_total = 0 #total cost of fabricating MITHRIL

total_cost = 0

## NOTES: If the values below are in capital letters it means I got them from research

#fixed price values
STARSHIP_LAUNCH_COST = 11*10**6 #10 launches multiplied by the quotes price of $1,000,000
VULCAN_LAUNCH_COST = 110*10**6

OP_COST_BASELINE = 1.5*10**8 #from Perserverence

DRILL_PRICE = 663000 #from some website, check the MITHRIL tech paper

AMOUNT_METHANE = 400000 #kg
AMOUNT_LOX = 500000 #kg

STORAGE_TANK_SIZE = AMOUNT_LOX/1141 #m^3 NEEDS UPDATES

ATHLETE_PRICE = 3*10**9 #based on the price of the Perserverance Rover
SEV_PRICE = 3*10**9/2
PRECURSOR_PRICE = 3*10**9

DSN_HOURS = 8000 #mostly arbitrary
DSN_BASE_RATE = 1792 #The Rb quoted price from the DSN Mission Support Definition and Commitments Office.
TTC_COST = 300000
NETWORK_ACCESS_FEE = 2700*12
MIM_COST = 290000
RF_TEST_COST = 120000

mars_factor = (((8*10**7)/(2.8*10**4)) + ((6.27*10**8)/(2.9*10**8)) + ((2.46*10**9)/(2.9*10**8)) + ((3.2*10**9)/(2.5*10**5))) / 4
#ah the beautiful and magnificent Mars factor. Basically the cost for a lot of this stuff
# is based on the cost of a terrestrial system and the mars factor scales it up to a reasonable price for Mars.
# Average of four different terrestial and mars equivalents to get something scalable.

#determines price of communications
services_pro[11]+=MIM_COST+RF_TEST_COST+NETWORK_ACCESS_FEE
services_pro[12]+=NETWORK_ACCESS_FEE+TTC_COST
for i in range(11,26): #determines the total yearly cost for DSN usaged based on a 2% inflation rate
    af = DSN_BASE_RATE*(.9+10/10)
    yearly_cost = DSN_HOURS*af+NETWORK_ACCESS_FEE
    services_pro[i]+=yearly_cost

#determines the cost to develope software
CS_LABOR_COST = 110140 + 100000 #average salary from BLS + a bunch for other costs (literally made up these ones)
NUM_CS_WORKERS = 60 #number of engineers on the task (Lembeck randomly said 30 engineers)
total_software_cost = CS_LABOR_COST*NUM_CS_WORKERS*5
total_software_cost_pro = total_software_cost/8 #this number is based on the Gantt chart
for i in range(3,11):
    design_pro[i]+=total_software_cost_pro
    
#determines the cost for operations
op_cost_modifier = 3 #make new something for this possibly????
for i in range(11,26):
    operations_pro[i] = OP_COST_BASELINE*op_cost_modifier
    op_cost_modifier = op_cost_modifier-.1

#determines the launch costs
launch_cost = 0
num_launches_Starships = 3
num_launches_Vulcan = 4
plots_cost = 10*10**9
plots_cost_design = plots_cost*(1105/1739)
plots_cost_fab = plots_cost*(634/1739)
plots_cost_design_pro = plots_cost_design/8
plots_cost_fab_pro = plots_cost_fab/4
for i in range(2,10):
    design_pro[i]+= plots_cost_design_pro
for i in range(8,12):
    fabrication_pro[i]+= plots_cost_fab_pro
services_pro[6] += VULCAN_LAUNCH_COST
services_pro[19] += VULCAN_LAUNCH_COST
services_pro[21] += VULCAN_LAUNCH_COST
services_pro[23] += VULCAN_LAUNCH_COST
services_pro[12] += num_launches_Starships*STARSHIP_LAUNCH_COST

#determines cost of KRUSTY
Pylon_cost = 5500*470
Pylon_cost_fab = Pylon_cost*.75
Pylon_cost_design = Pylon_cost*.25
Pylon_cost_fab_pro = Pylon_cost_fab/8
Pylon_cost_design_pro = Pylon_cost_design/6
for i in range(2,10):
    design_pro[i]+=Pylon_cost_design_pro
for i in range (11,12):
    fabrication_pro[i] += Pylon_cost_fab_pro

#determines SABER cost
# I coined (probably tbh idk if anyone else has said it) the term "Fiscal Gymnastics" after doing this one.
# Full explenation in the paper but honestly there is so much bullshit involved here its insane. 
price_per_barrel_oil = 25000
price_per_gallon_oil = price_per_barrel_oil/42
price_per_kg_oil = price_per_gallon_oil*3.45
price_per_kg_methalox = price_per_kg_oil*(1.55/.82)
saber_price_base = price_per_kg_methalox*(AMOUNT_METHANE+AMOUNT_LOX)/300*mars_factor
saber_cost_design = saber_price_base*(1057/1656)
saber_cost_fab = saber_price_base*(619/1656)
saber_cost_design_pro = saber_cost_design/8
saber_cost_fab_pro = saber_cost_fab/4
for i in range(2,10):
    design_pro[i]+=saber_cost_design_pro
for i in range(8,12):
    fabrication_pro[i]+=saber_cost_fab_pro

#determines storage cost
storage_tank_gallons = 2*STORAGE_TANK_SIZE*8981.85 
tank_cost_per_gallon = 1380000/835958
storage_cost = storage_tank_gallons*tank_cost_per_gallon*mars_factor
storage_cost_design = storage_cost*(1037/1656)
storage_cost_fab = storage_cost*(619/1656)
storage_cost_design_pro = storage_cost_design/8
storage_cost_fab_pro = storage_cost_fab/4
for i in range(2,10):
    design_pro[i]+=storage_cost_design_pro
for i in range(8,12):
    fabrication_pro[i]+=storage_cost_fab_pro

#determines STING cost
sting_cost = DRILL_PRICE*mars_factor
sting_cost_design = sting_cost*(1105/1739)
sting_cost_fab = sting_cost*(634/1739)
sting_cost_design_pro = sting_cost_design/8
sting_cost_fab_pro = sting_cost_fab/4
for i in range(2,10):
    design_pro[i]+=sting_cost_design_pro
for i in range(8,12):
    fabrication_pro[i]+=sting_cost_fab_pro    
    
#determines ATHLETE cost
athlete_cost_design = ATHLETE_PRICE*.5
athlete_cost_fab = ATHLETE_PRICE*.5
athlete_cost_design_pro = athlete_cost_design/8
athlete_cost_fab_pro = athlete_cost_fab/4
for i in range(2,10):
    design_pro[i]+= athlete_cost_design_pro
for i in range(8,12):
    fabrication_pro[i]+=athlete_cost_fab_pro

#Habitat
cost_per_sq_ft_Earth = 225
hab_area_m2 = 8701
hab_cost = cost_per_sq_ft_Earth*hab_area_m2*mars_factor
hab_cost_design = hab_cost*(1037/1656)
hab_cost_fab = hab_cost*(619/1656)
hab_cost_design_pro = hab_cost_design/8
hab_cost_fab_pro = hab_cost_fab/4
for i in range(2,10):
    design_pro[i]+= hab_cost_design_pro
for i in range(8,12):
    fabrication_pro[i]+= hab_cost_fab_pro

#Aquaponics
aquaponics = 300000
aquaponics_cost = aquaponics*mars_factor
aquaponics_cost_design = aquaponics_cost*.3
aquaponics_cost_fab = aquaponics_cost*.7
aquaponics_cost_design_pro = aquaponics_cost_design/8
aquaponics_cost_fab_pro = aquaponics_cost_fab/2
for i in range(2,10):
    design_pro[i]+= aquaponics_cost_design_pro
for i in range(10,12):
    fabrication_pro[i]+= aquaponics_cost_fab_pro

#Medical
med = 500*200
med_cost = med*mars_factor
med_cost_design = med_cost*.3
med_cost_fab = med_cost*.7
med_cost_design_pro = med_cost_design/8
med_cost_fab_pro = med_cost_fab/2
for i in range(2,10):
    design_pro[i]+= med_cost_design_pro
for i in range(10,12):
    fabrication_pro[i]+= med_cost_fab_pro

#ECLSS
ISS_ECLSS_cost = 250*10**6
ECLSS_cost = ISS_ECLSS_cost*3
ECLSS_cost_design = ECLSS_cost*.3
ECLSS_cost_fab = ECLSS_cost*.7
ECLSS_cost_design_pro = ECLSS_cost_design/8
ECLSS_cost_fab_pro = ECLSS_cost_fab/4
for i in range(2,10):
    design_pro[i]+= ECLSS_cost_design_pro
for i in range(8,12):
    fabrication_pro[i]+= ECLSS_cost_fab_pro

#Science/Research
science_cost = 11.75*10**9
science_cost_design = science_cost*.3
science_cost_fab = science_cost*.7
science_cost_design_pro = science_cost_design/8
science_cost_fab_pro = science_cost_fab/2
for i in range(2,10):
    design_pro[i]+= science_cost_design_pro
for i in range(10,12):
    fabrication_pro[i]+= science_cost_fab_pro

#applies a 2% inflation factor
for i in range(26):
    inf_factor = 1.02**i
    design_pro[i] = design_pro[i]*inf_factor
    fabrication_pro[i] = fabrication_pro[i]*inf_factor
    services_pro[i] = services_pro[i]*inf_factor
    operations_pro[i] = operations_pro[i]*inf_factor

#determines total cost in each category
operations_total = sum(operations_pro)
services_total = sum(services_pro)
design_total = sum(design_pro)
fabrication_total = sum(fabrication_pro)
total_cost = operations_total+services_total+design_total+fabrication_total
total_cost_pro = design_pro+fabrication_pro+services_pro+operations_pro



print("The total calculated cost for MORROW is: ", "$","{:,}".format(np.round(total_cost)))
# 

# 

# 

# In[ ]:





# In[ ]:





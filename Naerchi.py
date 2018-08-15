import pandas as pd
import numpy as np
import datetime
import random

# import file
file = 'dataset.csv'
df = pd.read_csv(file)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# Radom Mode: get random restaruant from list
restaruant = df.iloc[1:,0]
print(restaruant)
rand = random.seed(datetime.now())
print(rand)

# procedure to get input
# First get the current time
time = datetime.datetime.now().time()
# take input

def askAlone() {
	alone = input("Do you eat alone? Yes/No")
	if (alone == "Yes")
	    alone = 1
	elif (alone == "No")
	    alone = 0
	else askAlone()
}

def askHungry() {
	alone = input("Are you hungry? Yes/No")
	if (alone == "Yes")
	    alone = 1
	elif (alone == "No")
	    alone = 0
	else askHungry()
}
# print("Do you hungry or do you need a lot food?")
# hungry = input("prompt")
# print("Do you eat alone?" )
# alone = input("prompt")
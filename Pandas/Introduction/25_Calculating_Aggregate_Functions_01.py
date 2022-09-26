import codecademylib3
import pandas as pd

orders = pd.read_csv('orders.csv')

print(orders.head(10))

#Now, they want to know the most expensive shoe for each shoe_type (i.e., the most expensive boot, the most expensive ballet flat, etc.)
#Save your answer to the variable pricey_shoes.
pricey_shoes = orders.groupby('shoe_type').price.max()

#Examine the object that you just created
print(pricey_shoes)

#What type of object is pricey_shoes?
print(type(pricey_shoes))
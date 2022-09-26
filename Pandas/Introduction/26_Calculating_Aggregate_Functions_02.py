import codecademylib3
import pandas as pd

orders = pd.read_csv('orders.csv')

pricey_shoes = orders.groupby('shoe_type').price.max()

#series
print(type(pricey_shoes))
print(pricey_shoes)

#Modify your code from the previous exercise so that it ends with reset_index, which will change pricey_shoes into a DataFrame.
pricey_shoes = orders.groupby('shoe_type').price.max().reset_index()
print(pricey_shoes)
print(type(pricey_shoes))

#Our Marketing team says that it’s important to have some affordably priced shoes available for every color of shoe that we sell.
#Let’s calculate the 25th percentile for shoe price for each shoe_color to help Marketing decide if we have enough cheap shoes on sale. Save the data to the variable cheap_shoes
cheap_shoes = orders.groupby('shoe_color').price.apply(lambda x: np.percentile(x, 25)).reset_index()

#Display cheap_shoes
print(cheap_shoes)

#At ShoeFly.com, our Purchasing team thinks that certain shoe_type/shoe_color combinations are particularly popular this year (for example, blue ballet flats are all the rage in Paris).

#Create a DataFrame with the total number of shoes of each shoe_type/shoe_color combination purchased. Save it to the variable shoe_counts.

shoe_counts = orders.groupby(['shoe_type', 'shoe_color'])['id'].count().reset_index()

#Display shoe_counts
print(shoe_counts)


In the previous example, you created a DataFrame with the total number of shoes of each shoe_type/shoe_color combination purchased for ShoeFly.com.

#The purchasing manager complains that this DataFrame is confusing.

#Make it easier for her to compare purchases of different shoe colors of the same shoe type by creating a pivot table. Save your results to the variable shoe_counts_pivot.

unpivoted = shoe_counts.groupby(['shoe_type', 'shoe_color'])['id'].count().reset_index()

# Now pivot the table
shoe_counts_pivot = unpivoted.pivot(
    columns='shoe_color',
    index='shoe_type',
    values='id').reset_index()

#Display shoe_counts_pivot
print(shoe_counts_pivot)

user_visits = pd.read_csv('page_visits.csv')

#Let’s examine some more data from ShoeFly.com. This time, we’ll be looking at data about user visits to the website (the same dataset that you saw in the introduction to this lesson).
print(user_visits)
print(user_visits.head(5))

#The column utm_source contains information about how users got to ShoeFly’s homepage. For instance, if utm_source = Facebook, then the user came to ShoeFly by clicking on an ad on Facebook.com.

#Use a groupby statement to calculate how many visits came from each of the different sources. Save your answer to the variable click_source.
click_source = user_visits.groupby(['utm_source'])['id'].count().reset_index()

print(click_source)

#Our Marketing department thinks that the traffic to our site has been changing over the past few months. Use groupby to calculate the number of visits to our site from each utm_source for each month. Save your answer to the variable click_source_by_month.
click_source_by_month = user_visits.groupby(['utm_source','month'])['id'].count().reset_index()

#The head of Marketing is complaining that this table is hard to read. Use pivot to create a pivot table where the rows are utm_source and the columns are month. Save your results to the variable click_source_by_month_pivot.
click_source_by_month_pivot = click_source_by_month.pivot(
    columns='month',
    index='utm_source',
    values='id').reset_index()

print(click_source_by_month_pivot)
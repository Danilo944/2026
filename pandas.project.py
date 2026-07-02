import pandas as pd

#defining 1st data frame
spending_data = {
    'Service': ['rent', 'car', 'cellphone', 'groceries', 'gas'],
    'Price': [1400, 450, 190, 600, 150]
}
#convert the dictionary into a DataFrame

df = pd.DataFrame(spending_data)

priority_list = [1, 3, 4, 2, 5]

#Add the priority list using the insert() method

df.insert(2, 'Priority', priority_list)

print(df)

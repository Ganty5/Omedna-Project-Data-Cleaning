import pandas as pd
import statsmodels.api as sm

Thesis = pd.read_csv("C:/Users/Chika/Desktop/MY THESIS/Thesis proper/Thesis python.csv")

Thesis['Y_2021'] = (Thesis['Year'] == 2021).astype(int)
Thesis['Y_2020'] = (Thesis['Year'] == 2020).astype(int)
Thesis['Y_201916'] = ((Thesis['Year'] == 2019) | (Thesis['Year'] == 2016)).astype(int)


print(Thesis.head())

#Creating a dictionary to store results
results = {}

#Loop through round 1 to 10
for rnd in range(1,11):
    
    round_info = Thesis[Thesis['Round'] == rnd]
    
    y = round_info['Response(value)']
    
    x = round_info[['Offers to Responders', 'Y_2021', 'Y_2020', 'Y_201916']]
    x = sm.add_constant(x)
    model = sm.Probit(y,x)
    result = model.fit()
    results[rnd] = result.summary()
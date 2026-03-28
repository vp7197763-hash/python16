import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Company": ["Microsoft", "Google", "Amazon", "IBM", "Deloitte", "Capgemini", "ATOS", "Amdocs"],
    "Recruitments": [120, 150, 180, 90, 110, 130, 70, 95]
})

# a) Bar Chart
plt.figure()
plt.bar(df['Company'], df['Recruitments'])
plt.title("Company Recruitment")
plt.xticks(rotation=45)
plt.show()

# b) Pie Chart
plt.figure()
plt.pie(df['Recruitments'], labels=df['Company'], autopct='%1.1f%%')
plt.title("Recruitment Distribution")
plt.show()

# c) Customized Pie Chart
plt.figure()
plt.pie(df['Recruitments'],
        labels=df['Company'],
        autopct='%1.1f%%',
        explode=[0,0.1,0,0,0,0,0,0],
        shadow=True)
plt.title("Customized Pie Chart")
plt.show()

# d) Doughnut Chart
plt.figure()
plt.pie(df['Recruitments'], labels=df['Company'], autopct='%1.1f%%')
centre_circle = plt.Circle((0,0),0.70)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title("Doughnut Chart")
plt.show()

# e) Compare IBM vs Amdocs
ibm = df[df['Company'] == 'IBM']['Recruitments'].values[0]
amdocs = df[df['Company'] == 'Amdocs']['Recruitments'].values[0]

plt.figure()
plt.bar(['IBM', 'Amdocs'], [ibm, amdocs])
plt.title("IBM vs Amdocs Recruitment Comparison")
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("sales.csv")

# a) Total profit line plot
plt.figure()
plt.plot(df['month'], df['total_profit'], marker='o')
plt.title("Total Profit per Month")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.grid()
plt.show()

# b) Multiline plot for all products
plt.figure()
plt.plot(df['month'], df['facecream'], label='Face Cream')
plt.plot(df['month'], df['facewash'], label='Face Wash')
plt.plot(df['month'], df['toothpaste'], label='Toothpaste')
plt.plot(df['month'], df['bathingsoap'], label='Bath Soap')
plt.plot(df['month'], df['shampoo'], label='Shampoo')
plt.plot(df['month'], df['moisturizer'], label='Moisturizer')

plt.title("Sales Data of All Products")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.show()

# c) Bar chart for facecream & facewash
plt.figure()
width = 0.4
x = range(len(df['month']))

plt.bar(x, df['facecream'], width=width, label='Face Cream')
plt.bar([i + width for i in x], df['facewash'], width=width, label='Face Wash')

plt.xticks([i + width/2 for i in x], df['month'])
plt.title("Face Cream vs Face Wash Sales")
plt.legend()
plt.show()

# d) Pie chart for total yearly sales per product
products = ['facecream','facewash','toothpaste','bathingsoap','shampoo','moisturizer']
total_sales = [df[p].sum() for p in products]

plt.figure()
plt.pie(total_sales, labels=products, autopct='%1.1f%%')
plt.title("Total Sales Distribution")
plt.show()
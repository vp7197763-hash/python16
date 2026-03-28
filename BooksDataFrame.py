import pandas as pd

# Load CSV
df = pd.read_csv("books.csv")

# a) Print complete report
print("\n--- All Books ---")
print(df)

# b) Books by given author
author_name = input("\nEnter author name: ")
print("\nBooks by author:")
print(df[df['author'] == author_name])

# c) Books by given publisher
publisher_name = input("\nEnter publisher name: ")
print("\nBooks by publisher:")
print(df[df['publisher'] == publisher_name])

# d) Cheapest and costliest book
print("\nCheapest Book:")
print(df.loc[df['price'].idxmin()])

print("\nCostliest Book:")
print(df.loc[df['price'].idxmax()])

# e) Sort by year
print("\nBooks sorted by year:")
print(df.sort_values(by='year'))
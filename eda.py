import pandas as pd
import matplotlib.pyplot as plt

# Load data
# df = pd.read_csv("C:/Users/Admin/Desktop/Revenue Leakage DA Project/data/orders.csv")
df = pd.read_csv("C:/Users/Admin/Desktop/Revenue Leakage DA Project/data/orders.csv", encoding='cp1252')


# Check basic structure
print(df.head())
print(df.info())



# Profit by category
category_profit = df.groupby('Category')['Profit'].sum().sort_values()

plt.figure(figsize=(7,5))
category_profit.plot(kind='bar', color=['crimson','seagreen','royalblue'])
plt.title('Total Profit by Category', fontsize=14)
plt.ylabel('Profit', fontsize=12)
plt.xlabel('Category', fontsize=12)
plt.axhline(0, color='black', linewidth=1)
plt.tight_layout()
plt.show()

sub_profit = df.groupby('Sub-Category')['Profit'].sum().sort_values()
leak = df[df['Discount'] > 0.3]
leak.groupby('Category')['Profit'].sum()
df['disc_band'] = pd.cut(df['Discount'],
                         bins=[0,0.2,0.4,1],
                         labels=['Low','Medium','High'])
df.groupby('disc_band')['Profit'].sum()
sub_profit = df.groupby('Sub-Category')['Profit'].sum().sort_values()


plt.figure(figsize=(12,6))
sub_profit.plot(kind='bar'
                )
...


plt.figure(figsize=(7,5))

# Scatter relationship
plt.scatter(
    df['Discount'],   # X: discount percentage
    df['Profit'],     # Y: profit amount
    alpha=0.3         # transparency to show density
)

# Add zero-profit line
plt.axhline(0, color='black', linewidth=1)

# Titles and labels
plt.title('Discount vs Profit Scatter')
plt.xlabel('Discount (%)')
plt.ylabel('Profit')

plt.tight_layout()
plt.show()


df['disc_band'] = pd.cut(
    df['Discount'],
    bins=[0, 0.2, 0.4, 1],
    labels=['Low', 'Medium', 'High']
)

band_profit = df.groupby('disc_band')['Profit'].sum()
print(band_profit)
band_profit.plot(kind='bar')
plt.title('Profit by Discount Band')
plt.show()


# Create discount bands
df['disc_band'] = pd.cut(
    df['Discount'],
    bins=[0, 0.2, 0.4, 1],
    labels=['Low', 'Medium', 'High']
)

# Group profit by discount band
band_profit = df.groupby('disc_band')['Profit'].sum()
print(band_profit)

# Plot
band_profit.plot(kind='bar', color=['seagreen','gold','crimson'])
plt.title('Profit by Discount Band')
plt.xlabel('Discount Band')
plt.ylabel('Total Profit')
plt.axhline(0, color='black')
plt.show()


print(df.columns)


cat_band = df.groupby(['Category', 'disc_band'])['Profit'].sum().unstack()
print(cat_band)

cat_band.plot(kind='bar', figsize=(10,6))
plt.title('Profit by Category and Discount Band')
plt.ylabel('Profit')
plt.axhline(0, color='black')
plt.tight_layout()
plt.show()

#Create discount bands
df['disc_band'] = pd.cut(
    df['Discount'],
    bins=[0, 0.2, 0.4, 1],
    labels=['Low', 'Medium', 'High']
)

# Category vs band analysis
cat_band = df.groupby(['Category', 'disc_band'])['Profit'].sum().unstack()
print(cat_band)

cat_band.plot(kind='bar', figsize=(10,6))
plt.title('Profit by Category and Discount Band')
plt.ylabel('Profit')
plt.axhline(0, color='black')
plt.tight_layout()
# plt.show()


sub_band = df.groupby(['Sub-Category', 'disc_band'])['Profit'].sum().unstack()
print(sub_band)

df['disc_band'] = pd.cut(
    df['Discount'],
    bins=[0, 0.2, 0.4, 1],
    labels=['Low', 'Medium', 'High']
)
df.to_csv('../data/orders_with_bands.csv', index=False)








#%%
import collections
import Expense
import os
import matplotlib.pyplot as plt

dir = os.path.dirname(__file__)
expenses = Expense.Expenses()
expenses.read_expenses(f"{dir}/../data/spending_data.csv")

# %%
spending_categories = []

for expense in expenses.list:
    spending_categories.append(expense.category)

# %%
spending_counter = collections.Counter(spending_categories)
print(spending_counter)
# %%
top5 = spending_counter.most_common(5)

# %%
categories, count = zip(*top5)
# %%
fig, ax = plt.subplots()
ax.bar(categories, count)
ax.set_title('# of Purchases by Category')

#%%
plt.show()

# %%

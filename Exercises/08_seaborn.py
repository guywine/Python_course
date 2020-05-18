# https://seaborn.pydata.org/api.html
# https://seaborn.pydata.org/examples/index.html

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

#### forming tidy data
df = pd.read_csv('extra_material/pew_raw.csv')
tidy_df = (pd.melt(df,
                  ["religion"],
                  var_name="income",
                  value_name="freq")
           .sort_values(by=["religion"])
           .reset_index(drop=True)
           .astype({'income': 'category', 'religion': 'category'})) # category is the type for nominal data

sns.barplot(data=tidy_df, x='income', y='freq', hue='religion')

sns.catplot(data=tidy_df, x="religion", y="freq", hue="income", col="income")

_, ax = plt.subplots(figsize=(25, 8))
sns.stripplot(data=tidy_df, x="religion", y="freq", hue="income", ax=ax)

#####
simple_df = pd.DataFrame(np.random.random((1000, 4)), columns=list('abcd'))

sns.jointplot(data=simple_df, x='a', y='b', kind='kde')
sns.pairplot(data=simple_df)

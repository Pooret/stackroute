import seaborn as sns
import matplotlib.pyplot as plt


# load my dataset
tips = sns.load_dataset("tips")

# plot bill distribution
def plot():
	plt.figure()
	sns.histplot(data=tips, x='total_bill', kde=True, bins=15)
	plt.xlabel("Total Bill")
	plt.ylabel("Frequency")
	plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_path = "/mnt/data/2022 MLB Player Stats - Batting.csv"
data = pd.read_csv(file_path, encoding="latin1", delimiter=";")

# 1. Distribution of Batting Average (BA)
plt.figure(figsize=(8, 5))
sns.histplot(data['BA'], bins=20, kde=True)
plt.title("Distribution of Batting Averages (BA)")
plt.xlabel("Batting Average (BA)")
plt.ylabel("Frequency")
plt.show()

# 2. Home Runs vs. Batting Average
plt.figure(figsize=(8, 5))
sns.scatterplot(data=data, x="BA", y="HR", alpha=0.7)
plt.title("Home Runs vs. Batting Average")
plt.xlabel("Batting Average (BA)")
plt.ylabel("Home Runs (HR)")
plt.show()

# 3. Top 10 Home Run Hitters
top_hr_hitters = data.nlargest(10, 'HR')[['Name', 'HR']]
plt.figure(figsize=(10, 5))
sns.barplot(data=top_hr_hitters, x="HR", y="Name", orient="h")
plt.title("Top 10 Home Run Hitters in 2022")
plt.xlabel("Home Runs (HR)")
plt.ylabel("Player Name")
plt.show()

# 4. Correlation Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(data.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap of Batting Statistics")
plt.show()



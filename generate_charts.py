import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

folder_path = "c:/Users/bisra/Music/Task 2/"
df_clean = pd.read_csv(folder_path + 'cleaned_ravenstack_data.csv')
churn_df = pd.read_csv(folder_path + 'ravenstack_churn_events.csv')

sns.set_theme(style="whitegrid")

# Chart 1: Churn Reasons (Fixed Seaborn syntax)
plt.figure(figsize=(8, 4.5))
reason_counts = churn_df['reason_code'].value_counts()
sns.barplot(x=reason_counts.values, y=reason_counts.index, hue=reason_counts.index, palette="viridis", legend=False)
plt.title('Primary Voice of Customer (VoC) Churn Drivers', fontsize=13, fontweight='bold')
plt.xlabel('Number of Cancelled Accounts')
plt.ylabel('Stated Churn Reason')
plt.tight_layout()
plt.savefig(folder_path + 'churn_reasons_distribution.png')
print("💾 Chart 1 Saved: churn_reasons_distribution.png")

# Chart 2: Industry Breakdown (Fixed Seaborn syntax)
plt.figure(figsize=(8, 4.5))
industry_churn = df_clean.groupby('industry')['is_churned'].mean().sort_values(ascending=False) * 100
sns.barplot(x=industry_churn.values, y=industry_churn.index, hue=industry_churn.index, palette="magma", legend=False)
plt.title('Churn Concentration across Business Vertical Markets', fontsize=13, fontweight='bold')
plt.xlabel('Churn Rate (%)')
plt.ylabel('Industry Sector')
plt.tight_layout()
plt.savefig(folder_path + 'churn_by_industry.png')
print("💾 Chart 2 Saved: churn_by_industry.png")
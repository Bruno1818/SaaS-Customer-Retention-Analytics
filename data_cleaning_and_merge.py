import pandas as pd
import numpy as np

folder_path = "c:/Users/bisra/Music/Task 2/"

accounts = pd.read_csv(folder_path + 'ravenstack_accounts.csv')
subs = pd.read_csv(folder_path + 'ravenstack_subscriptions.csv')
churn = pd.read_csv(folder_path + 'ravenstack_churn_events.csv')

support = pd.read_csv(folder_path + 'ravenstack_support_tickets.csv')
ticket_counts = support.groupby('account_id').size().reset_index(name='total_tickets')

master_df = pd.merge(accounts, ticket_counts, on='account_id', how='left')
master_df['total_tickets'] = master_df['total_tickets'].fillna(0)

master_df['is_churned'] = np.where(master_df['churn_flag'] == True, 1, 0)

output_file = folder_path + 'cleaned_ravenstack_data.csv'
master_df.to_csv(output_file, index=False)

print("\nProcessing complete.")
print(f"File created: {output_file}")
print(f"Total Rows: {master_df.shape[0]} | Total Columns: {master_df.shape[1]}")
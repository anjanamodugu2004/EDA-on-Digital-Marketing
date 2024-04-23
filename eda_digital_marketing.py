import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Set a theme for seaborn to ensure consistent and visually appealing plots
sns.set_theme()

# Read the dataset
df = pd.read_csv(r'C:\Users\Pavan\Downloads\online_advertising_performance_data.csv')

# Replace infinite values with NaN and then check for missing values
df.replace([np.inf, -np.inf], np.nan, inplace=True)

# Print the percentage of missing data per column
missing_percentage = df.isnull().sum() / len(df) * 100
print("Percentage of missing data per column:\n", missing_percentage)

# Handling missing values based on the amount and importance of missing data
# If less critical, fill with median or mean, otherwise consider dropping
df.fillna({
    'user_engagement': df['user_engagement'].median(),
    'clicks': df['clicks'].mean()
}, inplace=True)

# Confirm no more missing values
print("\nMissing values after handling:\n", df.isnull().sum())

# Convert 'day' to datetime
df['day'] = pd.to_datetime(df['day'])

# Convert categorical 'user_engagement' data to numeric
engagement_mapping = {'Low': 0, 'Medium': 1, 'High': 2}
df['user_engagement'] = df['user_engagement'].map(engagement_mapping)

# Data Visualization

# Overall trend in user engagement throughout the campaign period
plt.figure(figsize=(10, 6))
sns.lineplot(x='day', y='user_engagement', data=df)
plt.title('Trend in User Engagement Over Time')
plt.xlabel('Day')
plt.ylabel('User Engagement')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Impact of banner size on clicks
plt.figure(figsize=(10, 6))
sns.boxplot(x='banner', y='clicks', data=df)
plt.title('Impact of Banner Size on Clicks')
plt.xlabel('Banner Size')
plt.ylabel('Clicks')
plt.show()

# Correlation between user engagement levels and revenue generated
correlation_user_engagement_revenue = df['user_engagement'].corr(df['revenue'])
print("Correlation between User Engagement and Revenue:", correlation_user_engagement_revenue)

# Visualization of user engagement impact
plt.figure(figsize=(10, 6))
sns.barplot(x='user_engagement', y='post_click_conversions', data=df)
plt.title('Effectiveness of Campaigns by User Engagement Level')
plt.xlabel('User Engagement Level')
plt.ylabel('Post Click Conversions')
plt.show()

# Highest number of displays and clicks by placement
top_placements_displays = df.groupby('placement')['displays'].sum().nlargest(5)
top_placements_clicks = df.groupby('placement')['clicks'].sum().nlargest(5)
print("Top Placements by Displays:\n", top_placements_displays)
print("Top Placements by Clicks:\n", top_placements_clicks)

# Seasonal patterns in displays and clicks
plt.figure(figsize=(10, 6))
sns.lineplot(x='day', y='displays', data=df, label='Displays')
sns.lineplot(x='day', y='clicks', data=df, label='Clicks')
plt.title('Seasonal Patterns in Displays and Clicks')
plt.xlabel('Day')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.show()

# Outliers in Cost, Clicks, and Revenue
plt.figure(figsize=(10, 6))
sns.boxplot(data=df[['cost', 'clicks', 'revenue']])
plt.title('Outliers in Cost, Clicks, and Revenue')
plt.ylabel('Value')
plt.show()

# Effectiveness of campaigns based on ad size and placement type
plt.figure(figsize=(10, 6))
sns.barplot(x='banner', y='post_click_conversions', hue='placement', data=df)
plt.title('Effectiveness of Campaigns based on Ad Size and Placement Type')
plt.xlabel('Banner Size')
plt.ylabel('Post Click Conversions')
plt.legend(title='Placement')
plt.show()

# Campaigns or banner sizes with consistent high ROI
high_roi_campaigns = df.groupby('campaign_number')['revenue'].sum() / df.groupby('campaign_number')['cost'].sum()
high_roi_banner_sizes = df.groupby('banner')['revenue'].sum() / df.groupby('banner')['cost'].sum()
print("Campaigns with Consistently High ROI:\n", high_roi_campaigns.nlargest(5))
print("Banner Sizes with Consistently High ROI:\n", high_roi_banner_sizes.nlargest(5))

# Distribution of post-click conversions across different placement types
plt.figure(figsize=(10, 6))
sns.boxplot(x='placement', y='post_click_conversions', data=df)
plt.title('Distribution of Post-Click Conversions across Placement Types')
plt.xlabel('Placement Type')
plt.ylabel('Post Click Conversions')
plt.xticks(rotation=45)
plt.show()

# User engagement levels between weekdays and weekends
df['day_of_week'] = df['day'].dt.day_name()
plt.figure(figsize=(10, 6))
sns.boxplot(x='day_of_week', y='user_engagement', data=df)
plt.title('User Engagement Levels between Weekdays and Weekends')
plt.xlabel('Day of the Week')
plt.ylabel('User Engagement')
plt.show()

# Cost per click (CPC) across different campaigns and banner sizes
df['CPC'] = df['cost'] / df['clicks']
plt.figure(figsize=(10, 6))
sns.barplot(x='campaign_number', y='CPC', hue='banner', data=df)
plt.title('Cost per Click (CPC) across Campaigns and Banner Sizes')
plt.xlabel('Campaign')
plt.ylabel('Cost per Click (CPC)')
plt.xticks(rotation=45)
plt.legend(title='Banner Size')
plt.show()

# Cost-effective campaigns or placements in generating post-click conversions
plt.figure(figsize=(10, 6))
sns.barplot(x='placement', y='post_click_conversions', hue='campaign_number', data=df)
plt.title('Cost-effective Placements in Generating Post-Click Conversions')
plt.xlabel('Placement')
plt.ylabel('Post Click Conversions')
plt.xticks(rotation=45)
plt.legend(title='Campaign Number')
plt.show()

# Trends in post-click conversion rates based on the day of the week
plt.figure(figsize=(10, 6))
sns.lineplot(x='day_of_week', y='post_click_conversions', data=df)
plt.title('Trends in Post-Click Conversion Rates based on Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Post Click Conversions')
plt.xticks(range(7), ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
plt.grid(True)
plt.show()

# Effectiveness of campaigns throughout different user engagement types in terms of post-click conversions
plt.figure(figsize=(10, 6))
sns.barplot(x='user_engagement', y='post_click_conversions', hue='campaign_number', data=df)
plt.title('Effectiveness of Campaigns throughout Different User Engagement Types')
plt.xlabel('User Engagement')
plt.ylabel('Post Click Conversions')
plt.xticks(rotation=45)
plt.legend(title='Campaign Number')
plt.show()
import pandas as pd


# Load dataset
df = pd.read_csv('data/winemag-data-130k-v2.csv')

print("Dataset Information:")
print(df.info())

print("\nFirst 5 Rows:")
print(df.head())


# Data Cleaning

# Fill missing prices with the mean price
df['price'] = df['price'].fillna(df['price'].mean())

# Fill missing countries and provinces with the most frequent value
df['country'] = df['country'].fillna(df['country'].mode()[0])
df['province'] = df['province'].fillna(df['province'].mode()[0])

# Remove rows where wine variety is missing
df = df.dropna(subset=['variety'])

# Remove @ from Twitter handles
df['taster_twitter_handle'] = df['taster_twitter_handle'].str.replace(
    '@', '', regex=False
)

# Fill remaining categorical missing values
df['designation'] = df['designation'].fillna('Unknown')
df['region_1'] = df['region_1'].fillna('Unknown')
df['region_2'] = df['region_2'].fillna('Unknown')
df['taster_name'] = df['taster_name'].fillna('Unknown')
df['taster_twitter_handle'] = df['taster_twitter_handle'].fillna('Unknown')


# Check remaining missing values
print("\nRemaining Missing Values:")
print(df.isnull().sum())


# Analysis

# 1. Top 5 countries by average wine rating
top_countries = (
    df.groupby('country')['points']
    .mean()
    .sort_values(ascending=False)
    .head(5)
)

print("\nTop 5 Countries by Average Rating:")
print(top_countries)


# 2. Wines scoring 95+ points and costing $20 or less
great_value_wines = df[
    (df['points'] >= 95) &
    (df['price'] <= 20)
]

print(
    f"\nNumber of Great Value Wines: "
    f"{len(great_value_wines)}"
)


# 3. Top 5 most frequently reviewed wine varieties
top_varieties = df['variety'].value_counts().head(5)

print("\nTop 5 Most Frequently Reviewed Wine Varieties:")
print(top_varieties)


# 4. Average price grouped by score
average_price_by_score = df.groupby('points')['price'].mean()

print("\nAverage Price by Score:")
print(average_price_by_score)


# 5. Top 5 wineries with the most reviews
top_wineries = df['winery'].value_counts().head(5)

print("\nTop 5 Wineries by Number of Reviews:")
print(top_wineries)

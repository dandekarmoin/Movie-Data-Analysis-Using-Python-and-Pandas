import pandas as pd

# Step 1: Load the data
movies = pd.read_csv(r'C:\project of python\movies.csv')

# Step 2: Display first 5 records
print("\nFirst 5 Movies:\n", movies.head())

# Step 3: Top 3 Movies by Rating
top_movies = movies.sort_values(by='Rating', ascending=False).head(3)
print("\nTop 3 Movies:\n", top_movies)

# Step 4: Average Rating per Genre
avg_rating_genre = movies.groupby('Genre')['Rating'].mean().sort_values(ascending=False)
print("\nAverage Rating by Genre:\n", avg_rating_genre)

# Step 5: Most Popular Genre (by number of movies)
popular_genre = movies['Genre'].value_counts()
print("\nMost Popular Genres:\n", popular_genre)

# (Optional) Step 6: Visualize
try:
    import matplotlib.pyplot as plt

    # Plot average rating by genre
    avg_rating_genre.plot(kind='bar', color='skyblue')
    plt.title('Average Rating by Genre')
    plt.xlabel('Genre')
    plt.ylabel('Average Rating')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

except ImportError:
    print("\nInstall matplotlib to see the chart visualization!")

# Sample CSV Templates for Smart Recommender System

This directory should contain three CSV files with the following structures:

## books.csv

Create a CSV file with these columns (example row shown):

```csv
id,book_id,best_book_id,work_id,books_count,isbn,isbn13,authors,original_publication_year,original_title,title,language_code,average_rating,ratings_count,work_ratings_count,work_text_reviews_count,ratings_1,ratings_2,ratings_3,ratings_4,ratings_5,image_url,small_image_url
1,2767052,2767052,2792775,272,439023483,9780439023480,Suzanne Collins,2008,The Hunger Games,The Hunger Games,eng,4.34,4780653,4942365,155254,66715,127936,560092,1481305,2706317,https://images.gr-assets.com/books/1447303603m/2767052.jpg,https://images.gr-assets.com/books/1447303603s/2767052.jpg
```

**Required columns:**
- `title`: Book title (string)
- `authors`: Author name(s) (string)
- `average_rating`: Rating from 0-5 (float)
- `image_url`: URL to book cover image (string)
- `original_title`: Original title if translated (string)
- `language_code`: ISO language code (string)
- `original_publication_year`: Year published (integer)
- `ratings_1` through `ratings_5`: Count of ratings for each star level (integers)

---

## courses.csv

Create a CSV file with these columns (example row shown):

```csv
s.no,course_title,course_organization,course_Certificate_type,course_rating,course_difficulty,course_students_enrolled
1,Python for Everybody Specialization,University of Michigan,SPECIALIZATION,4.8,Beginner,2350000
2,Machine Learning,Stanford University,COURSE,4.9,Intermediate,4500000
3,Deep Learning Specialization,DeepLearning.AI,SPECIALIZATION,4.9,Advanced,850000
```

**Required columns:**
- `course_title`: Course name (string)
- `course_organization`: Provider/university (string)
- `course_Certificate_type`: Certificate type (string)
- `course_rating`: Rating from 0-5 (float)
- `course_difficulty`: Difficulty level (string: Beginner/Intermediate/Advanced/Mixed)
- `course_students_enrolled`: Number of enrolled students (integer)

---

## movies.csv

Create a CSV file with these columns (example row shown):

```csv
imdbId,Imdb Link,Title,IMDB Score,Genre,Poster
tt0111161,https://www.imdb.com/title/tt0111161/,The Shawshank Redemption,9.3,"Drama, Crime",https://m.media-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg
tt0068646,https://www.imdb.com/title/tt0068646/,The Godfather,9.2,"Crime, Drama",https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg
tt0468569,https://www.imdb.com/title/tt0468569/,The Dark Knight,9.0,"Action, Crime, Drama",https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_.jpg
```

**Required columns:**
- `Title`: Movie title (string)
- `IMDB Score`: Rating from 0-10 (float)
- `Genre`: Comma-separated genres (string)
- `Poster`: URL to movie poster image (string)
- `imdbId`: IMDB identifier (string)
- `Imdb Link`: URL to IMDB page (string)

---

## Where to Find Real Datasets

### Books
- **Goodreads Dataset**: Available on Kaggle (search "Goodreads books")
- **Google Books API**: Can be scraped programmatically
- **Open Library**: https://openlibrary.org/developers/dumps

### Courses
- **Coursera/edX Datasets**: Available on Kaggle
- **Class Central**: https://www.classcentral.com (can be scraped)
- **Manual Collection**: Combine data from multiple MOOC platforms

### Movies
- **IMDB Datasets**: https://www.imdb.com/interfaces/ (official datasets)
- **TMDB**: https://www.themoviedb.org/documentation/api
- **OMDb API**: http://www.omdbapi.com/
- **Kaggle**: Search for "IMDB movies" or "movie dataset"

---

## Quick Test Data

If you just want to test the app, create minimal CSV files:

### books.csv (minimal):
```csv
title,authors,average_rating,image_url,original_title,language_code,original_publication_year,ratings_1,ratings_2,ratings_3,ratings_4,ratings_5
Harry Potter,J.K. Rowling,4.5,https://via.placeholder.com/150,Harry Potter,eng,1997,100,200,500,1000,2000
The Hobbit,J.R.R. Tolkien,4.3,https://via.placeholder.com/150,The Hobbit,eng,1937,50,100,300,800,1500
1984,George Orwell,4.2,https://via.placeholder.com/150,1984,eng,1949,80,150,400,900,1700
```

### courses.csv (minimal):
```csv
course_title,course_organization,course_Certificate_type,course_rating,course_difficulty,course_students_enrolled
Python Basics,MIT,COURSE,4.8,Beginner,100000
Machine Learning,Stanford,SPECIALIZATION,4.9,Advanced,250000
Web Development,Harvard,COURSE,4.7,Intermediate,150000
```

### movies.csv (minimal):
```csv
Title,IMDB Score,Genre,Poster,imdbId,Imdb Link
Inception,8.8,"Sci-Fi, Thriller",https://via.placeholder.com/200x300,tt1375666,https://www.imdb.com/title/tt1375666/
The Matrix,8.7,"Action, Sci-Fi",https://via.placeholder.com/200x300,tt0133093,https://www.imdb.com/title/tt0133093/
Interstellar,8.6,"Drama, Sci-Fi",https://via.placeholder.com/200x300,tt0816692,https://www.imdb.com/title/tt0816692/
```

Save each as a separate CSV file and place them in the `ai_project3` directory alongside `app.py`.

---

## Important Notes

1. **Column Names**: Must match exactly (case-sensitive)
2. **Encoding**: Save CSV files as UTF-8
3. **Missing Values**: The app handles missing data gracefully
4. **Image URLs**: Must be valid HTTP/HTTPS URLs or will show placeholders
5. **Commas in Data**: Properly escape fields containing commas (CSV standard)

## Testing the App

1. Create minimal test files using the examples above
2. Run `streamlit run app.py`
3. Verify data loads correctly in the preview section
4. Test search functionality with your sample data
5. Replace with real datasets for production use

---

**Need Help?** Check the main README.md for troubleshooting tips!

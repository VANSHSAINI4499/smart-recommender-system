# Quick Start Guide - Smart Recommender System

## 🚀 Get Up and Running in 5 Minutes

### Step 1: Install Dependencies (1 minute)

Open PowerShell in the `ai_project3` directory and run:

```powershell
pip install -r requirements.txt
```

This installs:
- streamlit (web framework)
- pandas (data processing)
- pillow (image handling)
- rapidfuzz (fuzzy matching)
- numpy (numerical operations)
- xlsxwriter (export functionality)
- requests (image loading)

### Step 2: Prepare Your Data (2 minutes)

**Option A - Use Sample Data (Recommended for testing):**

Create these three minimal CSV files in the `ai_project3` directory:

**books.csv:**
```csv
id,book_id,best_book_id,work_id,books_count,isbn,isbn13,authors,original_publication_year,original_title,title,language_code,average_rating,ratings_count,work_ratings_count,work_text_reviews_count,ratings_1,ratings_2,ratings_3,ratings_4,ratings_5,image_url,small_image_url
1,1,1,1,1,123456789,1234567890123,J.K. Rowling,1997,Harry Potter and the Philosopher's Stone,Harry Potter and the Sorcerer's Stone,eng,4.47,8000000,8500000,120000,100000,200000,800000,2500000,5000000,https://images.gr-assets.com/books/1474154022m/3.jpg,https://images.gr-assets.com/books/1474154022s/3.jpg
2,2,2,2,1,234567890,2345678901234,George Orwell,1949,Nineteen Eighty-Four,1984,eng,4.19,3500000,3800000,95000,80000,150000,600000,1200000,1950000,https://images.gr-assets.com/books/1532714506m/40961427.jpg,https://images.gr-assets.com/books/1532714506s/40961427.jpg
3,3,3,3,1,345678901,3456789012345,Harper Lee,1960,To Kill a Mockingbird,To Kill a Mockingbird,eng,4.27,5000000,5200000,110000,70000,120000,500000,1800000,2810000,https://images.gr-assets.com/books/1553383690m/2657.jpg,https://images.gr-assets.com/books/1553383690s/2657.jpg
```

**courses.csv:**
```csv
s.no,course_title,course_organization,course_Certificate_type,course_rating,course_difficulty,course_students_enrolled
1,Python for Everybody Specialization,University of Michigan,SPECIALIZATION,4.8,Beginner,2350000
2,Machine Learning,Stanford University,COURSE,4.9,Intermediate,4500000
3,Deep Learning Specialization,DeepLearning.AI,SPECIALIZATION,4.9,Advanced,850000
4,Web Development Bootcamp,Udemy,COURSE,4.7,Beginner,580000
5,Data Science Professional Certificate,IBM,PROFESSIONAL CERTIFICATE,4.6,Intermediate,320000
```

**movies.csv:**
```csv
imdbId,Imdb Link,Title,IMDB Score,Genre,Poster
tt0111161,https://www.imdb.com/title/tt0111161/,The Shawshank Redemption,9.3,"Drama",https://m.media-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SX300.jpg
tt0068646,https://www.imdb.com/title/tt0068646/,The Godfather,9.2,"Crime, Drama",https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SX300.jpg
tt0468569,https://www.imdb.com/title/tt0468569/,The Dark Knight,9.0,"Action, Crime, Drama",https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SX300.jpg
tt0108052,https://www.imdb.com/title/tt0108052/,Schindler's List,9.0,"Biography, Drama, History",https://m.media-amazon.com/images/M/MV5BNDE4OTMxMTctNmRhYy00NWE2LTg3YzItYTk3M2UwOTU5Njg4XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SX300.jpg
tt0110912,https://www.imdb.com/title/tt0110912/,Pulp Fiction,8.9,"Crime, Drama",https://m.media-amazon.com/images/M/MV5BNGNhMDIzZTUtNTBlZi00MTRlLWFjM2ItYzViMjE3YzI5MjljXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SX300.jpg
```

**Option B - Use Real Datasets:**

Download from Kaggle or other sources (see DATASET_INFO.md for links).

### Step 3: Run the App (30 seconds)

```powershell
streamlit run app.py
```

The app will automatically open in your default browser at `http://localhost:8501`

If it doesn't open automatically, manually navigate to that URL.

### Step 4: Test the Features (1-2 minutes)

**Test Book Recommender:**
1. Click on "📚 Book Recommender" tab
2. Type "Harry" in the Book Title field
3. Click "🔍 Find Books"
4. View recommendations with ratings and covers

**Test Course Recommender:**
1. Switch to "🎓 Course Recommender" tab
2. Type "Python" in Course Title
3. Select "Beginner" for difficulty
4. Click "🔍 Find Courses"
5. Browse course recommendations

**Test Movie Recommender:**
1. Go to "🎬 Movie Recommender" tab
2. Type "Dark" in Movie Title
3. Type "Action" in Genre
4. Click "🔍 Find Movies"
5. View movie posters and IMDB scores

**Test Auto-Refresh:**
1. Open sidebar (click arrow if collapsed)
2. Set refresh interval to 5 seconds
3. Click "▶️ Start"
4. Watch recommendations update automatically
5. Click "⏸️ Stop" to pause

### Step 5: Explore Advanced Features

- **Export**: Click "💾 Export" buttons to download recommendations as CSV
- **Upload**: Use sidebar file uploaders to load different datasets
- **Preview**: Expand "👀 Preview Loaded Datasets" to verify data
- **Instructions**: Click "📖 How to Use" in sidebar for detailed help

---

## 🎯 Pro Tips

1. **Leave fields empty** to get top-rated items in each category
2. **Use partial names** for better fuzzy matching (e.g., "incep" finds "Inception")
3. **Combine filters** for precise results (e.g., book title + author)
4. **Check the preview** to ensure CSVs loaded correctly
5. **Adjust refresh interval** based on your dataset size (smaller = faster)

---

## ⚠️ Common Issues & Solutions

### Issue: "Module not found" error
**Solution:**
```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

### Issue: CSV file not loading
**Solution:**
- Verify file is in the same directory as `app.py`
- Check column names match exactly (case-sensitive)
- Try using the sidebar file uploader instead

### Issue: Images not displaying
**Solution:**
- Images load from external URLs (requires internet)
- Invalid URLs show placeholder images
- This is normal and doesn't affect functionality

### Issue: App is slow
**Solution:**
- Reduce dataset size for testing
- Data is cached after first load (faster on subsequent runs)
- Lower refresh interval in auto-update mode

### Issue: Auto-refresh not stopping
**Solution:**
- Click "⏸️ Stop" button in sidebar
- Refresh browser page if needed
- Check that "Auto-refresh is INACTIVE" message appears

---

## 🎨 Customization Ideas

Want to personalize the app? Here are some easy modifications:

**Change Colors** (edit app.py, ~line 50-200):
```python
# Find these color codes and replace:
#1f1f1f  -> Your background color
#00d4ff  -> Your primary accent (neon blue)
#00ff9f  -> Your secondary accent (neon green)
#fff200  -> Your highlight color (yellow)
```

**Adjust Number of Recommendations** (edit app.py):
- Books: Change `top_n=5` in `recommend_books()` call
- Courses: Change `top_n=5` in `recommend_courses()` call
- Movies: Change `top_n=8` in `recommend_movies()` call

**Modify Fuzzy Match Threshold** (edit app.py, ~line 300):
```python
# Find: if match[1] > 60
# Change 60 to higher (stricter) or lower (looser) matching
```

---

## 📚 Next Steps

1. **Add More Data**: Expand your CSV files with more books, courses, movies
2. **Implement Semantic Search**: Follow the commented guide in app.py
3. **Add User Ratings**: Extend to track user preferences
4. **Deploy Online**: Use Streamlit Cloud for free hosting
5. **Create API**: Wrap recommendations in FastAPI for other apps

---

## 🆘 Need Help?

- **Documentation**: Check README.md and DATASET_INFO.md
- **Dataset Format**: See DATASET_INFO.md for column requirements
- **Error Messages**: The app shows helpful error messages in the UI
- **Python Version**: Requires Python 3.8 or higher

---

## ✅ Verification Checklist

Before reporting issues, verify:

- [ ] Python 3.8+ installed (`python --version`)
- [ ] Dependencies installed (`pip list | Select-String "streamlit"`)
- [ ] CSV files in correct directory (`ls *.csv`)
- [ ] CSV columns match requirements (see DATASET_INFO.md)
- [ ] Port 8501 not in use by another app
- [ ] Internet connection active (for loading images)

---

**Enjoy your Smart Recommender System! 🎉**

*Built with Streamlit • Powered by AI • Open Source*

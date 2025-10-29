# 🎯 Smart Recommender System

A production-ready Streamlit application featuring three powerful recommendation engines: Books, Courses, and Movies with a modern dark theme and neon accents.

## ✨ Features

- **📚 Book Recommender**: Search by title, genre, or author with fuzzy matching
- **🎓 Course Recommender**: Find courses by title and difficulty level
- **🎬 Movie Recommender**: Discover movies by title and genre with IMDB ratings
- **🔄 Auto-Refresh Mode**: Continuous recommendation updates with user control
- **🎨 Modern UI**: Dark theme with neon blue, green, and yellow accents
- **💾 Export Functionality**: Download recommendations as CSV
- **🔍 Fuzzy Matching**: Smart search using RapidFuzz for better results
- **📊 Rich Metadata**: Ratings, reviews, posters, and detailed information

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Prepare Your Datasets

Place the following CSV files in the same directory as `app.py`:

#### **books.csv** (Required columns):
- id, book_id, best_book_id, work_id, books_count
- isbn, isbn13, authors
- original_publication_year, original_title, title
- language_code, average_rating
- ratings_count, work_ratings_count, work_text_reviews_count
- ratings_1, ratings_2, ratings_3, ratings_4, ratings_5
- image_url, small_image_url

#### **courses.csv** (Required columns):
- s.no, course_title, course_organization
- course_Certificate_type, course_rating
- course_difficulty, course_students_enrolled

#### **movies.csv** (Required columns):
- imdbId, Imdb Link, Title
- IMDB Score, Genre, Poster

### 3. Run the Application

```bash
streamlit run app.py
```

### 4. Open in Browser

Navigate to `http://localhost:8501`

## 📖 How to Use

### Book Recommender
1. Navigate to the "📚 Book Recommender" tab
2. Enter any combination of:
   - Book title (e.g., "Harry Potter")
   - Genre (e.g., "Fantasy")
   - Author/Publisher (e.g., "J.K. Rowling")
3. Click "🔍 Find Books"
4. View 5 top-rated recommendations with covers and ratings
5. Export results using the "💾 Export" button

### Course Recommender
1. Go to the "🎓 Course Recommender" tab
2. Enter:
   - Course title (e.g., "Python Programming")
   - Difficulty level (Beginner/Intermediate/Advanced)
3. Click "🔍 Find Courses"
4. Browse 5 best-rated courses with enrollment stats
5. Export results if needed

### Movie Recommender
1. Switch to the "🎬 Movie Recommender" tab
2. Provide:
   - Movie title (e.g., "Inception")
   - Genre (e.g., "Sci-Fi", "Action")
3. Click "🔍 Find Movies"
4. Explore up to 8 top-rated movies with posters
5. Click IMDB links to view full details
6. Export recommendations

### Auto-Refresh Mode
1. Open the sidebar (⚙️ Control Panel)
2. Adjust "Refresh Interval" (1-30 seconds)
3. Click "▶️ Start" to begin auto-updates
4. Recommendations will refresh automatically
5. Click "⏸️ Stop" to pause
6. **Safe Implementation**: Uses session state + sleep intervals, won't lock up the app

## 🎨 UI Customization

The app features a modern dark theme with:
- **Background**: Dark gray (#1f1f1f)
- **Primary Accent**: Neon blue (#00d4ff)
- **Secondary Accent**: Neon green (#00ff9f)
- **Highlight**: Neon yellow (#fff200)
- **Card Layouts**: Hover effects, shadows, rounded corners
- **Responsive Design**: Adapts to different screen sizes

All styling is embedded in the app via inline CSS injection.

## 📊 Dataset Upload

You can upload CSV files in two ways:

1. **Local Files**: Place CSVs in the app directory
2. **UI Upload**: Use the sidebar file uploaders

The app will:
- Validate column names
- Show preview of first 3 rows
- Display helpful error messages if data is missing

## 🔧 Technical Details

### Recommendation Logic

**Books**:
- Substring matching on title, original_title, and authors
- Fuzzy matching (RapidFuzz) for partial matches
- Filters by genre and publisher/author
- Ranks by average_rating

**Courses**:
- Substring + fuzzy matching on course_title
- Difficulty level filtering
- Ranks by course_rating and enrollment

**Movies**:
- Substring + fuzzy matching on Title
- Genre filtering (supports multi-genre)
- Ranks by IMDB Score

### Caching
- Datasets are cached using `@st.cache_data`
- Faster load times after initial run
- Automatic cache invalidation on file changes

### Error Handling
- Missing image URLs show placeholders
- Graceful fallbacks for invalid data
- User-friendly error messages

## 🚀 Future Enhancements

The code includes commented sections for:

1. **Semantic Vector Search**:
   - Replace substring matching with sentence-transformers
   - Use embeddings for semantic understanding
   - Better handling of synonyms and related concepts

2. **Collaborative Filtering**:
   - User-based recommendations
   - Item-based similarity
   - Matrix factorization

3. **Content-Based Filtering**:
   - TF-IDF vectorization
   - Cosine similarity
   - Feature engineering

To implement semantic search:
```python
pip install sentence-transformers scikit-learn
```

See the commented section at the end of `app.py` for implementation guide.

## 🐛 Troubleshooting

**Issue**: CSV files not loading
- **Solution**: Verify column names match exactly (case-sensitive)
- Use the sidebar file uploader
- Check file encoding (should be UTF-8)

**Issue**: Images not displaying
- **Solution**: Ensure image_url/Poster columns contain valid HTTP URLs
- Placeholder images will show for missing/invalid URLs

**Issue**: Auto-refresh not working
- **Solution**: Check session state in sidebar
- Click Stop then Start to reset
- Refresh the browser page

**Issue**: Slow performance
- **Solution**: Reduce dataset size for testing
- Lower refresh interval
- Cached data loads faster after first run

## 📝 Notes

- **Infinite Loop Safety**: The auto-refresh uses controlled loops with `time.sleep()` and session state checks. It won't hang the Streamlit process.
- **Fuzzy Matching**: RapidFuzz provides fast, high-quality string matching (threshold: 60% similarity)
- **Image Handling**: Posters are loaded directly from URLs; PIL is available for local image processing
- **Export Format**: CSV format for easy import into Excel or other tools

## 📄 License

This project is open-source and available for educational and commercial use.

## 🤝 Contributing

Feel free to:
- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

## 📧 Support

For issues or questions:
1. Check the troubleshooting section
2. Review error messages in the app
3. Verify dataset format matches requirements

---

**Built with ❤️ using Streamlit** | **Powered by AI** | **Data-Driven Recommendations**

🌟 *Don't forget to star this project if you find it useful!*

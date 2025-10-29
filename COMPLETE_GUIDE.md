# 🎯 Complete Setup & Usage Guide

## Welcome to Smart Recommender System!

This guide will walk you through everything from installation to deployment.

---

## 📋 Table of Contents

1. [Quick Start](#quick-start)
2. [Installation Options](#installation-options)
3. [Dataset Setup](#dataset-setup)
4. [Running the App](#running-the-app)
5. [Using the Features](#using-the-features)
6. [Troubleshooting](#troubleshooting)
7. [Deployment](#deployment)
8. [Customization](#customization)

---

## 🚀 Quick Start

### Option 1: One-Click Launch (Windows)

**Double-click one of these files:**
- `launch.bat` (Simple launcher)
- `launch.ps1` (PowerShell launcher with more features)

They will:
- Check Python installation
- Install dependencies if needed
- Verify setup
- Launch the app

### Option 2: Command Line

```powershell
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

### Option 3: Python Script

```powershell
# Automated setup and launch
python run_app.py
```

---

## 💻 Installation Options

### Prerequisites

- **Python 3.8 or higher** ([Download](https://www.python.org/downloads/))
- **Internet connection** (for installing packages and loading images)
- **Web browser** (Chrome, Firefox, Edge, Safari)

### Installing Dependencies

**Method 1: Using pip**
```powershell
pip install -r requirements.txt
```

**Method 2: Using conda**
```powershell
conda create -n recommender python=3.11
conda activate recommender
pip install -r requirements.txt
```

**Method 3: Using poetry**
```powershell
poetry install
```

### Verifying Installation

Run the test script:
```powershell
python test_setup.py
```

This checks:
- ✓ Python version
- ✓ Dependencies installed
- ✓ CSV files present
- ✓ app.py exists
- ✓ CSV structure valid

---

## 📊 Dataset Setup

### Required CSV Files

You need three CSV files in the project directory:

1. **books.csv** - Book data
2. **courses.csv** - Course data  
3. **movies.csv** - Movie data

### Getting Datasets

**Option A: Download Real Data**

- **Books**: [Goodreads Dataset on Kaggle](https://www.kaggle.com/datasets/jealousleopard/goodreadsbooks)
- **Courses**: [Coursera Courses on Kaggle](https://www.kaggle.com/datasets/khusheekapoor/coursera-courses-dataset-2021)
- **Movies**: [IMDB Movies on Kaggle](https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows)

**Option B: Create Test Data**

See `DATASET_INFO.md` for minimal CSV examples. Quick sample:

**books.csv:**
```csv
id,book_id,best_book_id,work_id,books_count,isbn,isbn13,authors,original_publication_year,original_title,title,language_code,average_rating,ratings_count,work_ratings_count,work_text_reviews_count,ratings_1,ratings_2,ratings_3,ratings_4,ratings_5,image_url,small_image_url
1,1,1,1,1,123,123,J.K. Rowling,1997,Harry Potter,Harry Potter,eng,4.5,1000000,1000000,10000,1000,2000,5000,10000,20000,https://via.placeholder.com/150,https://via.placeholder.com/150
```

**courses.csv:**
```csv
s.no,course_title,course_organization,course_Certificate_type,course_rating,course_difficulty,course_students_enrolled
1,Python Basics,MIT,COURSE,4.8,Beginner,100000
```

**movies.csv:**
```csv
imdbId,Imdb Link,Title,IMDB Score,Genre,Poster
tt0111161,https://www.imdb.com/title/tt0111161/,The Shawshank Redemption,9.3,Drama,https://via.placeholder.com/200x300
```

**Option C: Upload via UI**

Don't have files locally? No problem! Use the sidebar file uploader after launching the app.

---

## 🎮 Running the App

### Starting the App

**Windows (Easy):**
```powershell
# Double-click:
launch.bat
# or
launch.ps1
```

**Command Line:**
```powershell
streamlit run app.py
```

**Python Script:**
```powershell
python run_app.py
```

### What Happens Next

1. **Terminal Output**: You'll see Streamlit starting up
2. **Browser Opens**: Default browser opens to http://localhost:8501
3. **App Loads**: Data is loaded and cached
4. **Ready to Use**: Start making recommendations!

### Stopping the App

- **Press** `Ctrl+C` in the terminal
- **Or** close the terminal window
- **Or** close the browser tab and terminal

---

## 🎯 Using the Features

### 📚 Book Recommender

**How to use:**

1. Click the **"📚 Book Recommender"** tab
2. Fill in search criteria:
   - **Book Title**: "Harry Potter", "1984", etc.
   - **Genre**: "Fantasy", "Science Fiction", etc.
   - **Author**: "J.K. Rowling", "George Orwell", etc.
3. Click **"🔍 Find Books"**
4. Browse 5 recommendations with:
   - Book cover images
   - Title and author
   - Average rating (1-5 stars)
   - Publication year
   - Language
   - Ratings breakdown

**Tips:**
- Leave fields empty for top-rated books
- Use partial names ("Harry" finds "Harry Potter")
- Combine filters for precise results
- Export results with the "💾 Export" button

### 🎓 Course Recommender

**How to use:**

1. Click the **"🎓 Course Recommender"** tab
2. Enter search criteria:
   - **Course Title**: "Python", "Machine Learning", etc.
   - **Difficulty**: Beginner, Intermediate, or Advanced
3. Click **"🔍 Find Courses"**
4. View 5 recommendations with:
   - Course title
   - Organization/university
   - Certificate type
   - Rating (1-5 stars)
   - Difficulty badge
   - Student enrollment count

**Tips:**
- Search by topic ("data science") or specific course
- Filter by difficulty for your skill level
- Check enrollment numbers for popularity
- Note certificate types for career goals

### 🎬 Movie Recommender

**How to use:**

1. Click the **"🎬 Movie Recommender"** tab
2. Provide search criteria:
   - **Movie Title**: "Inception", "The Matrix", etc.
   - **Genre**: "Action", "Sci-Fi", "Drama", etc.
3. Click **"🔍 Find Movies"**
4. Explore up to 8 recommendations with:
   - Movie poster
   - Title
   - IMDB score (0-10)
   - Genre tags
   - IMDB link (click to view full details)

**Tips:**
- Search by name or genre only
- Click IMDB links for trailers, cast, reviews
- Combine title + genre for specific results
- Genre search finds all movies in that category

### 🔄 Auto-Refresh Mode

**Continuous recommendations:**

1. Open **sidebar** (click arrow if collapsed)
2. Adjust **"Refresh Interval"** slider (1-30 seconds)
3. Click **"▶️ Start"** to begin auto-updates
4. Recommendations refresh automatically
5. Click **"⏸️ Stop"** to pause

**Use cases:**
- Display on a monitor/TV
- Demo mode for presentations
- Discover new recommendations continuously
- Entertainment mode

**Safety:** Uses controlled loops, won't hang the app!

### 💾 Export Recommendations

**Save your results:**

1. Get recommendations in any module
2. Click **"💾 Export ... Recommendations"** button
3. Click **"⬇️ Download CSV"**
4. Save to your computer
5. Open in Excel, Google Sheets, etc.

**Use cases:**
- Save for later review
- Share with friends
- Create reading/watching lists
- Data analysis

### 📁 Upload Datasets

**Via sidebar:**

1. Open **sidebar** (⚙️ Control Panel)
2. Scroll to **"📁 Dataset Management"**
3. Click **"Upload books.csv"** (or courses/movies)
4. Select your CSV file
5. Data loads instantly

**Use cases:**
- Test different datasets
- Use updated data
- No local files? Upload directly!
- Try different CSV formats

### 👀 Preview Datasets

**Verify your data:**

1. After loading datasets
2. Click **"👀 Preview Loaded Datasets"** expander
3. View first 3 rows of each dataset
4. Confirm columns and data format

**Checks:**
- Column names correct
- Data formatted properly
- Images URLs valid
- Ratings in correct range

---

## 🐛 Troubleshooting

### Common Issues

#### Issue: "Module not found" error

**Solution:**
```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

#### Issue: CSV file not loading

**Symptoms:** Error message about missing columns

**Solutions:**
1. Verify column names match exactly (case-sensitive)
2. Check file encoding (should be UTF-8)
3. Try uploading via sidebar
4. Run test script: `python test_setup.py`
5. See `DATASET_INFO.md` for column requirements

#### Issue: Images not displaying

**Symptoms:** Placeholder images or broken images

**Solutions:**
- Check internet connection (images load from URLs)
- Verify image_url/Poster columns have valid URLs
- Placeholders are normal for missing URLs
- Try different dataset with valid image URLs

#### Issue: App is slow

**Symptoms:** Long load times, lag when searching

**Solutions:**
1. Reduce dataset size (sample 10,000 rows)
2. Data caches after first load (faster next time)
3. Close other browser tabs
4. Lower refresh interval in auto-update mode
5. Use faster computer or smaller datasets

#### Issue: Auto-refresh won't stop

**Symptoms:** Can't stop continuous updates

**Solutions:**
1. Click "⏸️ Stop" button in sidebar
2. Refresh browser page (F5)
3. Check sidebar status (should say "INACTIVE")
4. Restart app if needed

#### Issue: Port already in use

**Symptoms:** Error: "Port 8501 is already in use"

**Solutions:**
```powershell
# Kill existing Streamlit process
taskkill /F /IM streamlit.exe
# Or use a different port
streamlit run app.py --server.port 8502
```

#### Issue: App won't start

**Symptoms:** Error messages when running `streamlit run app.py`

**Solutions:**
1. Check Python version: `python --version` (need 3.8+)
2. Verify Streamlit installed: `pip show streamlit`
3. Run test script: `python test_setup.py`
4. Check for syntax errors in app.py
5. Try reinstalling: `pip install --force-reinstall streamlit`

### Getting Help

1. **Check Documentation**: README.md, QUICKSTART.md, DATASET_INFO.md
2. **Run Test Script**: `python test_setup.py`
3. **Check Console**: Look for error messages in terminal
4. **Check Browser Console**: Press F12, look for JavaScript errors
5. **Verify Data**: Expand preview section in app

### Debug Mode

Enable verbose logging:
```powershell
# Run with debug output
streamlit run app.py --logger.level=debug
```

---

## 🚀 Deployment

### Deploy to Streamlit Cloud (Free!)

**Full guide in:** `DEPLOYMENT.md`

**Quick steps:**

1. **Create GitHub repo:**
   ```powershell
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/yourusername/smart-recommender.git
   git push -u origin main
   ```

2. **Deploy:**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository
   - Click "Deploy!"

3. **Share:**
   - Your app will be live at: `https://yourusername-smart-recommender.streamlit.app`
   - Share the link with anyone!

### Alternative Hosting

- **Heroku**: Dockerfile provided in DEPLOYMENT.md
- **Railway**: One-click deploy
- **AWS/Azure/GCP**: Full control, more complex

---

## 🎨 Customization

### Change Colors

Edit `app.py` (lines ~50-200):

```python
# Find and replace these colors:
#1f1f1f  -> Your background color (dark gray)
#00d4ff  -> Your primary accent (neon blue)
#00ff9f  -> Your secondary accent (neon green)
#fff200  -> Your highlight color (yellow)
```

### Adjust Number of Results

Edit `app.py`:

```python
# Books (around line 750)
recommend_books(..., top_n=5)  # Change to 10, 15, etc.

# Courses (around line 850)
recommend_courses(..., top_n=5)

# Movies (around line 950)
recommend_movies(..., top_n=8)
```

### Modify Fuzzy Matching

Edit `app.py` (around line 300):

```python
# Find: if match[1] > 60
# Change 60 to:
#   - Higher (70-90) for stricter matching
#   - Lower (40-50) for looser matching
```

### Add New Features

See commented sections in `app.py`:
- Semantic search (lines ~850-880)
- Collaborative filtering
- User ratings
- Social features

---

## 📚 Additional Resources

### Documentation Files

- **README.md**: Complete project overview
- **QUICKSTART.md**: 5-minute setup guide
- **DATASET_INFO.md**: CSV format and samples
- **DEPLOYMENT.md**: Cloud deployment guide
- **PROJECT_SUMMARY.md**: What was built and why
- **COMPLETE_GUIDE.md**: This file!

### External Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [RapidFuzz Documentation](https://rapidfuzz.github.io/RapidFuzz/)
- [Streamlit Community Forum](https://discuss.streamlit.io)

### Datasets

- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php)
- [Google Dataset Search](https://datasetsearch.research.google.com/)

---

## ✅ Success Checklist

Before deployment or sharing:

- [ ] All dependencies installed
- [ ] CSV files loaded successfully
- [ ] All three recommenders working
- [ ] Images displaying (or placeholders)
- [ ] Export functionality tested
- [ ] Auto-refresh starts and stops
- [ ] No errors in console
- [ ] Tested on mobile/tablet (responsive)
- [ ] Documentation reviewed
- [ ] Ready to share!

---

## 🎉 You're Ready!

**Your Smart Recommender System is complete and ready to use!**

### Next Steps:

1. **Test locally**: Run `streamlit run app.py`
2. **Add data**: Upload or create CSV files
3. **Explore features**: Try all three recommenders
4. **Customize**: Change colors, add features
5. **Deploy**: Share with the world!
6. **Get feedback**: Improve based on user input
7. **Extend**: Add semantic search, user accounts, etc.

---

## 💬 Need More Help?

- **Quick Setup**: See QUICKSTART.md
- **Dataset Format**: See DATASET_INFO.md
- **Deployment**: See DEPLOYMENT.md
- **Feature Overview**: See README.md
- **What Was Built**: See PROJECT_SUMMARY.md

---

**Built with ❤️ using Streamlit | Powered by AI | Production-Ready**

*Happy Recommending! 🚀*

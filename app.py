"""
======================================================================================
SMART RECOMMENDER SYSTEM - Streamlit App
======================================================================================

A production-ready recommendation engine with three modules:
- Book Recommender (books.csv)
- Course Recommender (courses.csv)  
- Movie Recommender (movies.csv)

HOW TO RUN:
-----------
1. Install dependencies:
   pip install streamlit pandas pillow rapidfuzz

2. Place CSV files in the same directory as this script:
   - books.csv (with columns: id, book_id, best_book_id, work_id, books_count, isbn, 
     isbn13, authors, original_publication_year, original_title, title, language_code, 
     average_rating, ratings_count, work_ratings_count, work_text_reviews_count, 
     ratings_1, ratings_2, ratings_3, ratings_4, ratings_5, image_url, small_image_url)
   - courses.csv (with columns: s.no, course_title, course_organization, 
     course_Certificate_type, course_rating, course_difficulty, course_students_enrolled)
   - movies.csv (with columns: imdbId, Imdb Link, Title, IMDB Score, Genre, Poster)

3. Run the app:
   streamlit run app.py

4. Open your browser to http://localhost:8501

REQUIREMENTS.TXT:
-----------------
streamlit>=1.28.0
pandas>=2.0.0
pillow>=10.0.0
rapidfuzz>=3.0.0
numpy>=1.24.0

NOTES:
------
- The app uses fuzzy matching (RapidFuzz) for better search results
- Auto-refresh mode updates recommendations periodically (user-controlled)
- All images are displayed from URLs in the datasets
- Dark theme with neon accents (blue, green, yellow) for modern look
- Responsive card layouts for all recommendation types

FUTURE ENHANCEMENTS (commented sections in code):
--------------------------------------------------
- Replace substring matching with semantic vector search using sentence-transformers
- Add collaborative filtering for personalized recommendations
- Implement content-based filtering with TF-IDF or embeddings
======================================================================================
"""

import streamlit as st
import pandas as pd
import time
from io import BytesIO
from PIL import Image, ImageOps, ImageDraw, ImageFont
import requests
from rapidfuzz import fuzz, process
import base64

# ============================================================================
# CONFIGURATION & STYLING
# ============================================================================

# Page configuration
st.set_page_config(
    page_title="Smart Recommender System",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for dark theme with neon accents
def inject_custom_css():
    """Inject custom CSS for modern dark theme with neon blue, green, and yellow accents."""
    st.markdown("""
    <style>
    /* Main background and text colors */
    .stApp {
        background-color: #1f1f1f;
        color: #e0e0e0;
    }
    
    /* Headers with neon accents */
    h1, h2, h3 {
        color: #00d4ff !important;
        text-shadow: 0 0 10px rgba(0, 212, 255, 0.5);
        font-weight: 700;
    }
    
    h1 {
        font-size: 3rem !important;
        margin-bottom: 1rem;
    }
    
    /* Card styling */
    .recommendation-card {
        background: linear-gradient(145deg, #2a2a2a, #1a1a1a);
        border: 2px solid #00d4ff;
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 8px 16px rgba(0, 212, 255, 0.2), 0 0 20px rgba(0, 255, 159, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .recommendation-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 24px rgba(0, 212, 255, 0.4), 0 0 30px rgba(0, 255, 159, 0.2);
        border-color: #00ff9f;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #00d4ff, #00ff9f);
        color: #1f1f1f;
        border: none;
        border-radius: 10px;
        padding: 0.75rem 2rem;
        font-weight: 700;
        font-size: 1.1rem;
        box-shadow: 0 4px 12px rgba(0, 212, 255, 0.3);
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #00ff9f, #fff200);
        box-shadow: 0 6px 20px rgba(0, 255, 159, 0.5);
        transform: translateY(-2px);
    }
    
    /* Input fields */
    .stTextInput > div > div > input,
    .stSelectbox > div > div > select {
        background-color: #2a2a2a;
        color: #e0e0e0;
        border: 2px solid #00d4ff;
        border-radius: 8px;
        padding: 0.5rem;
    }
    
    .stTextInput > div > div > input:focus,
    .stSelectbox > div > div > select:focus {
        border-color: #00ff9f;
        box-shadow: 0 0 10px rgba(0, 255, 159, 0.3);
    }
    
    /* Sidebar styling */
    .css-1d391kg, [data-testid="stSidebar"] {
        background-color: #1a1a1a;
        border-right: 2px solid #00d4ff;
    }
    
    /* Metric styling */
    .metric-container {
        background: #2a2a2a;
        border-left: 4px solid #fff200;
        padding: 10px;
        border-radius: 8px;
        margin: 5px 0;
    }
    
    /* Image containers */
    .poster-image {
        border-radius: 10px;
        border: 3px solid #00ff9f;
        box-shadow: 0 4px 12px rgba(0, 255, 159, 0.3);
        transition: transform 0.3s ease;
    }
    
    .poster-image:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 20px rgba(0, 212, 255, 0.5);
    }
    
    /* Warning/Info boxes */
    .stAlert {
        background-color: #2a2a2a;
        border-left: 4px solid #fff200;
        color: #e0e0e0;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #2a2a2a;
        border-radius: 10px;
        padding: 10px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: #1f1f1f;
        border: 2px solid #00d4ff;
        border-radius: 8px;
        color: #00d4ff;
        font-weight: 600;
        padding: 10px 20px;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #00d4ff, #00ff9f);
        color: #1f1f1f;
        border-color: #00ff9f;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background-color: #2a2a2a;
        border: 2px solid #00d4ff;
        border-radius: 8px;
        color: #00d4ff;
        font-weight: 600;
    }
    
    /* Rating stars */
    .rating-stars {
        color: #fff200;
        font-size: 1.2rem;
    }
    
    /* Links */
    a {
        color: #00d4ff;
        text-decoration: none;
        transition: color 0.3s ease;
    }
    
    a:hover {
        color: #00ff9f;
        text-shadow: 0 0 8px rgba(0, 255, 159, 0.5);
    }
    </style>
    """, unsafe_allow_html=True)


# ============================================================================
# DATA LOADING & CACHING
# ============================================================================

# Fixed image sizes (maintain consistent 2:3 ratio for alignment)
BOOK_IMAGE_SIZE = (300, 450)
MOVIE_IMAGE_SIZE = (300, 450)

def _convert_enrollment_to_numeric(value):
    """Convert enrollment strings like '5.3k', '17k', '130k' to numeric values.
    
    Args:
        value: String or numeric value
    
    Returns:
        Numeric value (e.g., '5.3k' -> 5300, '17k' -> 17000)
    """
    if pd.isna(value):
        return 0
    
    if isinstance(value, (int, float)):
        return int(value)
    
    # Convert string like '5.3k' or '17k' to numeric
    value_str = str(value).strip().lower()
    
    if 'k' in value_str:
        try:
            num = float(value_str.replace('k', ''))
            return int(num * 1000)
        except ValueError:
            return 0
    elif 'm' in value_str:
        try:
            num = float(value_str.replace('m', ''))
            return int(num * 1000000)
        except ValueError:
            return 0
    else:
        try:
            return int(float(value_str))
        except ValueError:
            return 0

def _make_placeholder_image(size, text="No Image"):
    """Create a solid placeholder image of the given size with centered text.

    Ensures a consistent aspect ratio across items to preserve grid alignment.
    """
    width, height = size
    bg_color = (42, 42, 42)
    fg_color = (0, 212, 255)  # neon blue accent
    img = Image.new("RGB", size, bg_color)
    draw = ImageDraw.Draw(img)
    # Choose a simple font; fall back to default if truetype not available
    try:
        font = ImageFont.truetype("arial.ttf", size=int(height * 0.08))
    except Exception:
        font = ImageFont.load_default()
    text = text[:20]
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text(((width - tw) / 2, (height - th) / 2), text, fill=fg_color, font=font)
    return img

def _load_image_with_fallback(url: str, size, placeholder_text: str):
    """Try to fetch and resize image; return a consistent-ratio placeholder on failure.

    Uses ImageOps.fit to preserve aspect ratio and crop/letterbox to target size.
    """
    try:
        if url and isinstance(url, str) and url.startswith("http"):
            resp = requests.get(url, timeout=4)
            resp.raise_for_status()
            img = Image.open(BytesIO(resp.content)).convert("RGB")
            # Fit to target while preserving ratio (center crop if needed)
            return ImageOps.fit(img, size, Image.LANCZOS)
    except Exception:
        pass
    return _make_placeholder_image(size, placeholder_text)

@st.cache_data
def load_books_dataset(file_path=None, uploaded_file=None):
    """Load and validate books dataset from CSV file."""
    try:
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file, encoding='latin-1')
        else:
            # Try different encodings
            try:
                df = pd.read_csv(file_path if file_path else 'books.csv', encoding='utf-8')
            except UnicodeDecodeError:
                try:
                    df = pd.read_csv(file_path if file_path else 'books.csv', encoding='latin-1')
                except UnicodeDecodeError:
                    df = pd.read_csv(file_path if file_path else 'books.csv', encoding='ISO-8859-1')
        
        required_cols = ['title', 'authors', 'average_rating', 'image_url']
        missing_cols = [col for col in required_cols if col not in df.columns]
        
        if missing_cols:
            st.error(f"❌ Books dataset missing required columns: {missing_cols}")
            return None
        
        # Preprocess: handle missing values and convert types
        df['title'] = df['title'].fillna('Unknown Title')
        df['authors'] = df['authors'].fillna('Unknown Author')
        df['average_rating'] = pd.to_numeric(df['average_rating'], errors='coerce').fillna(0)
        df['original_publication_year'] = pd.to_numeric(df['original_publication_year'], errors='coerce').fillna(0)
        df['image_url'] = df['image_url'].fillna('')
        df['original_title'] = df['original_title'].fillna(df['title'])
        df['language_code'] = df['language_code'].fillna('en')
        
        # Create lowercase search columns
        df['title_lower'] = df['title'].str.lower()
        df['authors_lower'] = df['authors'].str.lower()
        df['original_title_lower'] = df['original_title'].str.lower()
        
        return df
    except FileNotFoundError:
        st.error("❌ books.csv not found. Please upload the file or place it in the same directory.")
        return None
    except Exception as e:
        st.error(f"❌ Error loading books dataset: {str(e)}")
        return None


@st.cache_data
def load_courses_dataset(file_path=None, uploaded_file=None):
    """Load and validate courses dataset from CSV file."""
    try:
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file, encoding='latin-1')
        else:
            # Try different encodings
            try:
                df = pd.read_csv(file_path if file_path else 'courses.csv', encoding='utf-8')
            except UnicodeDecodeError:
                try:
                    df = pd.read_csv(file_path if file_path else 'courses.csv', encoding='latin-1')
                except UnicodeDecodeError:
                    df = pd.read_csv(file_path if file_path else 'courses.csv', encoding='ISO-8859-1')
        
        required_cols = ['course_title', 'course_rating', 'course_difficulty']
        missing_cols = [col for col in required_cols if col not in df.columns]
        
        if missing_cols:
            st.error(f"❌ Courses dataset missing required columns: {missing_cols}")
            return None
        
        # Preprocess
        df['course_title'] = df['course_title'].fillna('Unknown Course')
        df['course_organization'] = df['course_organization'].fillna('Unknown')
        df['course_rating'] = pd.to_numeric(df['course_rating'], errors='coerce').fillna(0)
        df['course_difficulty'] = df['course_difficulty'].fillna('Unknown')
        # Convert enrollment strings like '5.3k', '17k' to proper numbers
        df['course_students_enrolled'] = df['course_students_enrolled'].apply(_convert_enrollment_to_numeric)
        df['course_Certificate_type'] = df['course_Certificate_type'].fillna('N/A')
        
        # Create lowercase search columns
        df['course_title_lower'] = df['course_title'].str.lower()
        df['course_difficulty_lower'] = df['course_difficulty'].str.lower()
        
        return df
    except FileNotFoundError:
        st.error("❌ courses.csv not found. Please upload the file or place it in the same directory.")
        return None
    except Exception as e:
        st.error(f"❌ Error loading courses dataset: {str(e)}")
        return None


@st.cache_data
def load_movies_dataset(file_path=None, uploaded_file=None):
    """Load and validate movies dataset from CSV file."""
    try:
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file, encoding='latin-1')
        else:
            # Try different encodings
            try:
                df = pd.read_csv(file_path if file_path else 'movies.csv', encoding='utf-8')
            except UnicodeDecodeError:
                try:
                    df = pd.read_csv(file_path if file_path else 'movies.csv', encoding='latin-1')
                except UnicodeDecodeError:
                    df = pd.read_csv(file_path if file_path else 'movies.csv', encoding='ISO-8859-1')
        
        required_cols = ['Title', 'IMDB Score', 'Genre', 'Poster']
        missing_cols = [col for col in required_cols if col not in df.columns]
        
        if missing_cols:
            st.error(f"❌ Movies dataset missing required columns: {missing_cols}")
            return None
        
        # Preprocess
        df['Title'] = df['Title'].fillna('Unknown Movie')
        df['IMDB Score'] = pd.to_numeric(df['IMDB Score'], errors='coerce').fillna(0)
        df['Genre'] = df['Genre'].fillna('Unknown')
        df['Poster'] = df['Poster'].fillna('')
        df['Imdb Link'] = df['Imdb Link'].fillna('')
        
        # Create lowercase search columns
        df['Title_lower'] = df['Title'].str.lower()
        df['Genre_lower'] = df['Genre'].str.lower()
        
        return df
    except FileNotFoundError:
        st.error("❌ movies.csv not found. Please upload the file or place it in the same directory.")
        return None
    except Exception as e:
        st.error(f"❌ Error loading movies dataset: {str(e)}")
        return None


# ============================================================================
# RECOMMENDATION LOGIC - BOOKS
# ============================================================================

def recommend_books(df, book_name='', genre='', publisher='', top_n=5):
    """
    Recommend books based on title, genre, and publisher using substring and fuzzy matching.
    
    Args:
        df: Books DataFrame
        book_name: Book title to search for
        genre: Genre to filter by
        publisher: Publisher/author to filter by
        top_n: Number of recommendations to return
    
    Returns:
        DataFrame of recommended books
    """
    if df is None or df.empty:
        return pd.DataFrame()
    
    # Start with full dataset
    filtered_df = df.copy()
    
    # If no inputs provided, return top-rated books
    if not book_name and not genre and not publisher:
        return filtered_df.nlargest(top_n, 'average_rating')
    
    # Apply filters independently (AND logic: all specified filters must match)
    
    # Filter by book title if provided
    if book_name:
        book_name_lower = book_name.lower()
        
        # Substring matching on title and original_title
        mask = (filtered_df['title_lower'].str.contains(book_name_lower, na=False, regex=False) |
                filtered_df['original_title_lower'].str.contains(book_name_lower, na=False, regex=False))
        
        substring_matches = filtered_df[mask]
        
        # If few results, add fuzzy matching
        if len(substring_matches) < top_n:
            # Use RapidFuzz for fuzzy matching
            titles = filtered_df['title'].tolist()
            fuzzy_matches = process.extract(book_name, titles, scorer=fuzz.ratio, limit=top_n * 2)
            fuzzy_indices = [filtered_df[filtered_df['title'] == match[0]].index[0] 
                           for match in fuzzy_matches if match[1] > 60]
            
            fuzzy_df = filtered_df.loc[fuzzy_indices]
            filtered_df = pd.concat([substring_matches, fuzzy_df]).drop_duplicates()
        else:
            filtered_df = substring_matches
    
    # Filter by genre if provided (search in title as proxy for genre keywords)
    if genre:
        genre_lower = genre.lower()
        filtered_df = filtered_df[
            filtered_df['title_lower'].str.contains(genre_lower, na=False, regex=False) |
            filtered_df['original_title_lower'].str.contains(genre_lower, na=False, regex=False)
        ]
    
    # Filter by publisher/author if provided
    if publisher:
        publisher_lower = publisher.lower()
        filtered_df = filtered_df[
            filtered_df['authors_lower'].str.contains(publisher_lower, na=False, regex=False)
        ]
    
    # Sort by rating and return top N
    if not filtered_df.empty:
        return filtered_df.nlargest(min(top_n, len(filtered_df)), 'average_rating')
    
    return pd.DataFrame()


def display_book_card(book, col):
    """Display a single book recommendation card."""
    with col:
        st.markdown('<div class="recommendation-card">', unsafe_allow_html=True)
        
        # Display book cover with robust same-ratio placeholder fallback (2:3)
        img = _load_image_with_fallback(book.get('image_url', ''), BOOK_IMAGE_SIZE, "No Cover")
        st.image(img, width='stretch', caption=book['title'])
        
        # Book details
        st.markdown(f"### 📚 {book['title']}")
        st.markdown(f"**Author(s):** {book['authors']}")
        
        if book['original_publication_year'] > 0:
            st.markdown(f"**Year:** {int(book['original_publication_year'])}")
        
        st.markdown(f"**Language:** {book['language_code']}")
        
        # Rating display
        rating = float(book['average_rating'])
        stars = "⭐" * int(rating)
        st.markdown(f'<div class="rating-stars">{stars} {rating:.2f}/5.0</div>', unsafe_allow_html=True)
        
        # Ratings breakdown
        if all(col in book.index for col in ['ratings_1', 'ratings_2', 'ratings_3', 'ratings_4', 'ratings_5']):
            with st.expander("📊 Ratings Breakdown"):
                total_ratings = sum([book[f'ratings_{i}'] for i in range(1, 6)])
                if total_ratings > 0:
                    for i in range(5, 0, -1):
                        count = int(book[f'ratings_{i}'])
                        percentage = (count / total_ratings) * 100
                        st.markdown(f"{i}⭐: {count:,} ({percentage:.1f}%)")
        
        st.markdown('</div>', unsafe_allow_html=True)


# ============================================================================
# RECOMMENDATION LOGIC - COURSES
# ============================================================================

def recommend_courses(df, course_title='', difficulty='', top_n=5):
    """
    Recommend courses based on title and difficulty using substring and fuzzy matching.
    
    Args:
        df: Courses DataFrame
        course_title: Course title to search for
        difficulty: Difficulty level to filter by
        top_n: Number of recommendations to return
    
    Returns:
        DataFrame of recommended courses
    """
    if df is None or df.empty:
        return pd.DataFrame()
    
    filtered_df = df.copy()
    
    # If no inputs, return top-rated courses
    if not course_title and not difficulty:
        return filtered_df.nlargest(min(top_n, len(filtered_df)), 'course_rating')
    
    # Filter by course title
    if course_title:
        course_title_lower = course_title.lower()
        
        # Substring matching
        mask = filtered_df['course_title_lower'].str.contains(course_title_lower, na=False, regex=False)
        substring_matches = filtered_df[mask]
        
        # Fuzzy matching if few results
        if len(substring_matches) < top_n:
            titles = filtered_df['course_title'].tolist()
            fuzzy_matches = process.extract(course_title, titles, scorer=fuzz.ratio, limit=top_n * 2)
            fuzzy_indices = [filtered_df[filtered_df['course_title'] == match[0]].index[0] 
                           for match in fuzzy_matches if match[1] > 60]
            
            fuzzy_df = filtered_df.loc[fuzzy_indices]
            filtered_df = pd.concat([substring_matches, fuzzy_df]).drop_duplicates()
        else:
            filtered_df = substring_matches
    
    # Filter by difficulty
    if difficulty:
        difficulty_lower = difficulty.lower()
        filtered_df = filtered_df[
            filtered_df['course_difficulty_lower'].str.contains(difficulty_lower, na=False, regex=False)
        ]
    
    # Sort by rating, then by enrolled students
    if not filtered_df.empty:
        filtered_df = filtered_df.sort_values(
            by=['course_rating', 'course_students_enrolled'],
            ascending=[False, False]
        )
        return filtered_df.head(min(top_n, len(filtered_df)))
    
    return pd.DataFrame()


def display_course_card(course, col):
    """Display a single course recommendation card."""
    with col:
        st.markdown('<div class="recommendation-card">', unsafe_allow_html=True)
        
        st.markdown(f"### 🎓 {course['course_title']}")
        st.markdown(f"**Organization:** {course['course_organization']}")
        st.markdown(f"**Certificate:** {course['course_Certificate_type']}")
        
        # Rating display
        rating = float(course['course_rating'])
        stars = "⭐" * int(rating)
        st.markdown(f'<div class="rating-stars">{stars} {rating:.2f}/5.0</div>', unsafe_allow_html=True)
        
        # Difficulty badge
        difficulty = course['course_difficulty']
        color_map = {
            'beginner': '#00ff9f',
            'intermediate': '#fff200',
            'advanced': '#ff6b6b',
            'mixed': '#00d4ff'
        }
        diff_lower = difficulty.lower()
        badge_color = next((color for key, color in color_map.items() if key in diff_lower), '#00d4ff')
        
        st.markdown(
            f'<div style="background-color: {badge_color}; color: #1f1f1f; '
            f'padding: 5px 15px; border-radius: 20px; display: inline-block; '
            f'font-weight: bold; margin: 10px 0;">{difficulty}</div>',
            unsafe_allow_html=True
        )
        
        # Students enrolled
        students = int(course['course_students_enrolled'])
        st.markdown(f"**👥 Students Enrolled:** {students:,}")
        
        st.markdown('</div>', unsafe_allow_html=True)


# ============================================================================
# RECOMMENDATION LOGIC - MOVIES
# ============================================================================

def recommend_movies(df, movie_name='', genre='', top_n=8):
    """
    Recommend movies based on title and genre using substring and fuzzy matching.
    
    Args:
        df: Movies DataFrame
        movie_name: Movie title to search for
        genre: Genre to filter by
        top_n: Number of recommendations to return
    
    Returns:
        DataFrame of recommended movies
    """
    if df is None or df.empty:
        return pd.DataFrame()
    
    filtered_df = df.copy()
    
    # If no inputs, return top-rated movies
    if not movie_name and not genre:
        return filtered_df.nlargest(min(top_n, len(filtered_df)), 'IMDB Score')
    
    # Filter by movie title
    if movie_name:
        movie_name_lower = movie_name.lower()
        
        # Substring matching
        mask = filtered_df['Title_lower'].str.contains(movie_name_lower, na=False, regex=False)
        substring_matches = filtered_df[mask]
        
        # Fuzzy matching if few results
        if len(substring_matches) < top_n:
            titles = filtered_df['Title'].tolist()
            fuzzy_matches = process.extract(movie_name, titles, scorer=fuzz.ratio, limit=top_n * 2)
            fuzzy_indices = [filtered_df[filtered_df['Title'] == match[0]].index[0] 
                           for match in fuzzy_matches if match[1] > 60]
            
            fuzzy_df = filtered_df.loc[fuzzy_indices]
            filtered_df = pd.concat([substring_matches, fuzzy_df]).drop_duplicates()
        else:
            filtered_df = substring_matches
    
    # Filter by genre
    if genre:
        genre_lower = genre.lower()
        filtered_df = filtered_df[
            filtered_df['Genre_lower'].str.contains(genre_lower, na=False, regex=False)
        ]
    
    # Sort by IMDB score
    if not filtered_df.empty:
        return filtered_df.nlargest(min(top_n, len(filtered_df)), 'IMDB Score')
    
    return pd.DataFrame()


def display_movie_card(movie, col):
    """Display a single movie recommendation card."""
    with col:
        st.markdown('<div class="recommendation-card">', unsafe_allow_html=True)
        
        # Display movie poster with robust same-ratio placeholder fallback (2:3)
        img = _load_image_with_fallback(movie.get('Poster', ''), MOVIE_IMAGE_SIZE, "No Poster")
        st.image(img, width='stretch', caption=movie['Title'])
        
        # Movie details
        st.markdown(f"### 🎬 {movie['Title']}")
        
        # IMDB Score
        score = float(movie['IMDB Score'])
        stars = "⭐" * int(score / 2)  # Convert 10-point scale to 5-star
        st.markdown(f'<div class="rating-stars">{stars} {score:.1f}/10</div>', unsafe_allow_html=True)
        
        # Genre
        st.markdown(f"**Genre:** {movie['Genre']}")
        
        # IMDB Link
        if movie['Imdb Link']:
            st.markdown(f"[🔗 View on IMDB]({movie['Imdb Link']})")
        
        st.markdown('</div>', unsafe_allow_html=True)


# ============================================================================
# AUTO-REFRESH FUNCTIONALITY
# ============================================================================

def initialize_session_state():
    """Initialize session state variables for auto-refresh functionality."""
    if 'running' not in st.session_state:
        st.session_state.running = False
    if 'refresh_interval' not in st.session_state:
        st.session_state.refresh_interval = 5
    if 'last_recommendations' not in st.session_state:
        st.session_state.last_recommendations = None


# ============================================================================
# EXPORT FUNCTIONALITY
# ============================================================================

def export_recommendations_to_csv(recommendations_dict):
    """Export current recommendations to CSV format."""
    output = BytesIO()
    
    # Combine all recommendations into sheets or single file
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        for name, df in recommendations_dict.items():
            if df is not None and not df.empty:
                df.to_excel(writer, sheet_name=name, index=False)
    
    output.seek(0)
    return output


# ============================================================================
# MAIN APPLICATION
# ============================================================================

def main():
    """Main application function."""
    
    # Inject custom CSS
    inject_custom_css()
    
    # Initialize session state
    initialize_session_state()
    
    # Header
    st.markdown("""
    <h1 style="text-align: center;">🎯 SMART RECOMMENDER SYSTEM</h1>
    <p style="text-align: center; font-size: 1.3rem; color: #00ff9f;">
    Your AI-Powered Gateway to Books 📚 | Courses 🎓 | Movies 🎬
    </p>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Sidebar - Dataset Upload & Controls
    with st.sidebar:
        st.markdown("## ⚙️ Control Panel")
        
        st.markdown("### 📁 Dataset Management")
        
        # File uploaders
        books_file = st.file_uploader("Upload books.csv", type=['csv'], key='books_upload')
        courses_file = st.file_uploader("Upload courses.csv", type=['csv'], key='courses_upload')
        movies_file = st.file_uploader("Upload movies.csv", type=['csv'], key='movies_upload')
        
        st.markdown("---")
        
        # Recommendation count settings
        st.markdown("### 🔢 Recommendation Settings")
        
        num_books = st.slider(
            "📚 Number of Books",
            min_value=1,
            max_value=20,
            value=5,
            help="How many book recommendations to show"
        )
        
        num_courses = st.slider(
            "🎓 Number of Courses",
            min_value=1,
            max_value=20,
            value=5,
            help="How many course recommendations to show"
        )
        
        num_movies = st.slider(
            "🎬 Number of Movies",
            min_value=1,
            max_value=20,
            value=8,
            help="How many movie recommendations to show"
        )
        
        st.markdown("---")
        
        # Auto-refresh controls
        st.markdown("### 🔄 Auto-Refresh Settings")
        
        st.session_state.refresh_interval = st.slider(
            "Refresh Interval (seconds)",
            min_value=1,
            max_value=30,
            value=st.session_state.refresh_interval,
            help="How often to refresh recommendations in auto-update mode"
        )
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("▶️ Start", width='stretch'):
                st.session_state.running = True
                st.rerun()
        
        with col2:
            if st.button("⏸️ Stop", width='stretch'):
                st.session_state.running = False
                st.rerun()
        
        if st.session_state.running:
            st.success("🟢 Auto-refresh is ACTIVE")
        else:
            st.info("⚪ Auto-refresh is INACTIVE")
        
        st.markdown("---")
        
        # Instructions
        with st.expander("📖 How to Use"):
            st.markdown("""
            **Getting Started:**
            1. Upload your CSV files or place them in the app directory
            2. Navigate through tabs to access different recommenders
            3. Enter search criteria and get instant recommendations
            4. Enable auto-refresh for continuous updates
            
            **Features:**
            - 🔍 Fuzzy search with substring matching
            - 🎨 Modern dark theme with neon accents
            - 📊 Detailed ratings and metadata
            - 🔄 Auto-refresh mode
            - 💾 Export recommendations to CSV
            
            **Tips:**
            - Leave fields empty for top-rated items
            - Use partial names for better fuzzy matching
            - Combine filters for precise results
            """)
    
    # Load datasets
    books_df = load_books_dataset(uploaded_file=books_file)
    courses_df = load_courses_dataset(uploaded_file=courses_file)
    movies_df = load_movies_dataset(uploaded_file=movies_file)
    
    # Show dataset preview
    if books_df is not None or courses_df is not None or movies_df is not None:
        with st.expander("👀 Preview Loaded Datasets (First 3 Rows)"):
            if books_df is not None:
                st.markdown("**Books Dataset:**")
                st.dataframe(books_df.head(3), width='stretch')
            if courses_df is not None:
                st.markdown("**Courses Dataset:**")
                st.dataframe(courses_df.head(3), width='stretch')
            if movies_df is not None:
                st.markdown("**Movies Dataset:**")
                st.dataframe(movies_df.head(3), width='stretch')
    
    # Tabs for different recommenders
    tab1, tab2, tab3 = st.tabs([
        "📚 Book Recommender",
        "🎓 Course Recommender",
        "🎬 Movie Recommender"
    ])
    
    # ========================================================================
    # BOOK RECOMMENDER TAB
    # ========================================================================
    with tab1:
        st.markdown(f"### 📚 Tell me a book, genre, or author — I'll fetch {num_books} glowing picks ✨")
        
        if books_df is None:
            st.warning("⚠️ Please upload or provide books.csv to use this feature.")
        else:
            col1, col2, col3 = st.columns(3)
            
            with col1:
                book_name = st.text_input(
                    "Book Title",
                    placeholder="e.g., Harry Potter, 1984...",
                    key='book_name_input'
                )
            
            with col2:
                genre = st.text_input(
                    "Genre",
                    placeholder="e.g., Fantasy, Science Fiction...",
                    key='genre_input'
                )
            
            with col3:
                publisher = st.text_input(
                    "Author/Publisher",
                    placeholder="e.g., J.K. Rowling...",
                    key='publisher_input'
                )
            
            if st.button("🔍 Find Books", key='find_books_btn', width='stretch'):
                with st.spinner("Searching for perfect book matches..."):
                    recommendations = recommend_books(
                        books_df,
                        book_name=book_name,
                        genre=genre,
                        publisher=publisher,
                        top_n=num_books
                    )
                    
                    st.session_state.last_recommendations = {
                        'books': recommendations,
                        'params': (book_name, genre, publisher)
                    }
            
            # Display recommendations
            if st.session_state.last_recommendations and 'books' in st.session_state.last_recommendations:
                recommendations = st.session_state.last_recommendations['books']
                
                if not recommendations.empty:
                    st.markdown(f"### 🎉 Found {len(recommendations)} Amazing Books for You!")
                    
                    # Display in grid layout
                    cols = st.columns(min(len(recommendations), 3))
                    for idx, (_, book) in enumerate(recommendations.iterrows()):
                        display_book_card(book, cols[idx % 3])
                    
                    # Export button
                    if st.button("💾 Export Book Recommendations", key='export_books'):
                        csv_data = recommendations.to_csv(index=False)
                        st.download_button(
                            label="⬇️ Download CSV",
                            data=csv_data,
                            file_name=f"book_recommendations_{int(time.time())}.csv",
                            mime="text/csv"
                        )
                else:
                    st.info("🤔 No books found matching your criteria. Try different keywords!")
    
    # ========================================================================
    # COURSE RECOMMENDER TAB
    # ========================================================================
    with tab2:
        st.markdown(f"### 🎓 Discover {num_courses} courses that match your learning goals ✨")
        
        if courses_df is None:
            st.warning("⚠️ Please upload or provide courses.csv to use this feature.")
        else:
            col1, col2 = st.columns(2)
            
            with col1:
                course_title = st.text_input(
                    "Course Title",
                    placeholder="e.g., Python, Machine Learning...",
                    key='course_title_input'
                )
            
            with col2:
                difficulty_options = ['', 'Beginner', 'Intermediate', 'Advanced', 'Mixed']
                difficulty = st.selectbox(
                    "Difficulty Level",
                    options=difficulty_options,
                    key='difficulty_select'
                )
            
            if st.button("🔍 Find Courses", key='find_courses_btn', width='stretch'):
                with st.spinner("Searching for perfect course matches..."):
                    recommendations = recommend_courses(
                        courses_df,
                        course_title=course_title,
                        difficulty=difficulty,
                        top_n=num_courses
                    )
                    
                    st.session_state.last_recommendations = {
                        'courses': recommendations,
                        'params': (course_title, difficulty)
                    }
            
            # Display recommendations
            if st.session_state.last_recommendations and 'courses' in st.session_state.last_recommendations:
                recommendations = st.session_state.last_recommendations['courses']
                
                if not recommendations.empty:
                    st.markdown(f"### 🎉 Found {len(recommendations)} Outstanding Courses for You!")
                    
                    # Display in grid layout
                    cols = st.columns(min(len(recommendations), 2))
                    for idx, (_, course) in enumerate(recommendations.iterrows()):
                        display_course_card(course, cols[idx % 2])
                    
                    # Export button
                    if st.button("💾 Export Course Recommendations", key='export_courses'):
                        csv_data = recommendations.to_csv(index=False)
                        st.download_button(
                            label="⬇️ Download CSV",
                            data=csv_data,
                            file_name=f"course_recommendations_{int(time.time())}.csv",
                            mime="text/csv"
                        )
                else:
                    st.info("🤔 No courses found matching your criteria. Try different keywords!")
    
    # ========================================================================
    # MOVIE RECOMMENDER TAB
    # ========================================================================
    with tab3:
        st.markdown(f"### 🎬 Find your next {num_movies} favorite movies — lights, camera, action! ✨")
        
        if movies_df is None:
            st.warning("⚠️ Please upload or provide movies.csv to use this feature.")
        else:
            col1, col2 = st.columns(2)
            
            with col1:
                movie_name = st.text_input(
                    "Movie Title",
                    placeholder="e.g., Inception, The Matrix...",
                    key='movie_name_input'
                )
            
            with col2:
                genre_movie = st.text_input(
                    "Genre",
                    placeholder="e.g., Action, Drama, Comedy...",
                    key='genre_movie_input'
                )
            
            if st.button("🔍 Find Movies", key='find_movies_btn', width='stretch'):
                with st.spinner("Searching for perfect movie matches..."):
                    recommendations = recommend_movies(
                        movies_df,
                        movie_name=movie_name,
                        genre=genre_movie,
                        top_n=num_movies
                    )
                    
                    st.session_state.last_recommendations = {
                        'movies': recommendations,
                        'params': (movie_name, genre_movie)
                    }
            
            # Display recommendations
            if st.session_state.last_recommendations and 'movies' in st.session_state.last_recommendations:
                recommendations = st.session_state.last_recommendations['movies']
                
                if not recommendations.empty:
                    st.markdown(f"### 🎉 Found {len(recommendations)} Incredible Movies for You!")
                    
                    # Display in grid layout (4 columns for movies)
                    cols = st.columns(min(len(recommendations), 4))
                    for idx, (_, movie) in enumerate(recommendations.iterrows()):
                        display_movie_card(movie, cols[idx % 4])
                    
                    # Export button
                    if st.button("💾 Export Movie Recommendations", key='export_movies'):
                        csv_data = recommendations.to_csv(index=False)
                        st.download_button(
                            label="⬇️ Download CSV",
                            data=csv_data,
                            file_name=f"movie_recommendations_{int(time.time())}.csv",
                            mime="text/csv"
                        )
                else:
                    st.info("🤔 No movies found matching your criteria. Try different keywords!")
    
    # ========================================================================
    # AUTO-REFRESH LOGIC
    # ========================================================================
    if st.session_state.running:
        # Show countdown
        placeholder = st.empty()
        for remaining in range(st.session_state.refresh_interval, 0, -1):
            placeholder.info(f"🔄 Auto-refreshing in {remaining} seconds... (Press Stop to cancel)")
            time.sleep(1)
            if not st.session_state.running:
                break
        
        placeholder.empty()
        
        # Trigger rerun if still running
        if st.session_state.running:
            st.rerun()
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 20px; color: #00d4ff;">
        <p style="font-size: 0.9rem;">
            🌟 Built with Streamlit | Powered by AI | Data-Driven Recommendations
        </p>
        <p style="font-size: 0.8rem; color: #00ff9f;">
            💡 <strong>Future Enhancement:</strong> Replace substring matching with semantic vector search 
            using sentence-transformers for even better recommendations!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    """
    FUTURE ENHANCEMENT - SEMANTIC SEARCH (Commented Implementation Guide):
    -----------------------------------------------------------------------
    To upgrade to semantic vector search:
    
    1. Install sentence-transformers:
       pip install sentence-transformers
    
    2. Load a pre-trained model:
       from sentence_transformers import SentenceTransformer
       model = SentenceTransformer('all-MiniLM-L6-v2')
    
    3. Generate embeddings for all titles in datasets:
       @st.cache_data
       def generate_embeddings(df, text_column):
           texts = df[text_column].tolist()
           embeddings = model.encode(texts)
           return embeddings
    
    4. For search queries, encode the query and compute cosine similarity:
       from sklearn.metrics.pairwise import cosine_similarity
       
       query_embedding = model.encode([query])
       similarities = cosine_similarity(query_embedding, dataset_embeddings)[0]
       top_indices = similarities.argsort()[-10:][::-1]
    
    5. This will provide semantic understanding, capturing meaning beyond exact words.
       Example: "space adventure" would match "interstellar journey" even without shared words.
    """


if __name__ == "__main__":
    main()

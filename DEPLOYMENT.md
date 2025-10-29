# 🚀 Deployment Guide - Streamlit Cloud

Deploy your Smart Recommender System to the cloud for free with Streamlit Cloud!

## Prerequisites

- GitHub account
- Git installed locally
- Your app working locally (test with `streamlit run app.py`)

## Step-by-Step Deployment

### 1. Create a GitHub Repository

```powershell
# Initialize git repository (if not already done)
cd d:\python\ai_project3
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - Smart Recommender System"

# Create repository on GitHub (via web interface)
# Then add remote and push:
git remote add origin https://github.com/YOUR_USERNAME/smart-recommender.git
git branch -M main
git push -u origin main
```

### 2. Prepare for Deployment

Ensure these files are in your repository:
- ✓ `app.py` (main application)
- ✓ `requirements.txt` (dependencies)
- ✓ `.streamlit/config.toml` (optional styling)
- ✓ CSV files (books.csv, courses.csv, movies.csv)
  - **Note**: If CSV files are large (>100MB), use Git LFS or provide upload functionality only

### 3. Deploy on Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub
3. Click "New app"
4. Select:
   - **Repository**: YOUR_USERNAME/smart-recommender
   - **Branch**: main
   - **Main file path**: app.py
5. Click "Deploy!"

Your app will be live at: `https://YOUR_USERNAME-smart-recommender.streamlit.app`

### 4. Configure Secrets (Optional)

If you need API keys or credentials:

1. Click "Advanced settings" before deploying
2. Add secrets in TOML format:
```toml
# .streamlit/secrets.toml
[passwords]
admin_password = "your_secure_password"

[api_keys]
tmdb_api_key = "your_api_key"
```

3. Access in app:
```python
import streamlit as st
password = st.secrets["passwords"]["admin_password"]
```

## Handling Large CSV Files

### Option 1: Git LFS (Large File Storage)

```powershell
# Install Git LFS
git lfs install

# Track CSV files
git lfs track "*.csv"
git add .gitattributes
git add *.csv
git commit -m "Add large CSV files with LFS"
git push
```

### Option 2: External Storage

Upload CSVs to:
- **Google Drive** (public link)
- **Dropbox** (public link)
- **AWS S3** (public bucket)
- **GitHub Releases** (attach as release asset)

Modify `app.py` to download from URL:

```python
import requests
import pandas as pd
from io import StringIO

@st.cache_data
def load_from_url(url):
    response = requests.get(url)
    df = pd.read_csv(StringIO(response.text))
    return df

# Example usage
books_df = load_from_url("https://your-storage/books.csv")
```

### Option 3: Database Integration

For production, use a database:
- **PostgreSQL** (via Supabase - free tier)
- **MongoDB** (Atlas - free tier)
- **Google Sheets** (via gspread)

```python
# Example: Supabase
from supabase import create_client, Client

url = st.secrets["supabase"]["url"]
key = st.secrets["supabase"]["key"]
supabase: Client = create_client(url, key)

response = supabase.table("books").select("*").execute()
books_df = pd.DataFrame(response.data)
```

## Performance Optimization

### 1. Enable Caching

Already implemented in `app.py`:
```python
@st.cache_data
def load_books_dataset(file_path=None, uploaded_file=None):
    # ... loading logic
```

### 2. Reduce Dataset Size

For faster loading:
```python
# Load only necessary columns
df = pd.read_csv('books.csv', usecols=['title', 'authors', 'rating', 'image_url'])

# Sample large datasets
df = df.sample(n=10000)  # Use 10k random rows
```

### 3. Optimize Images

- Use thumbnail URLs instead of full-size images
- Implement lazy loading
- Cache image requests

```python
@st.cache_data
def load_image(url):
    try:
        response = requests.get(url, timeout=5)
        img = Image.open(BytesIO(response.content))
        img.thumbnail((300, 300))  # Resize
        return img
    except:
        return None
```

## Custom Domain (Optional)

1. Deploy to Streamlit Cloud (get default URL)
2. Purchase domain (e.g., from Namecheap, Google Domains)
3. Add CNAME record pointing to your Streamlit Cloud app
4. In Streamlit Cloud settings, add custom domain
5. Wait for DNS propagation (can take 24-48 hours)

Example CNAME record:
```
Host: www
Value: YOUR_USERNAME-smart-recommender.streamlit.app
```

## Monitoring & Analytics

### Built-in Streamlit Metrics

Streamlit Cloud provides:
- App uptime
- Number of viewers
- Resource usage (CPU, memory)

Access via dashboard at [share.streamlit.io](https://share.streamlit.io)

### Google Analytics Integration

Add to `app.py`:

```python
# Add Google Analytics tracking code
st.markdown("""
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
""", unsafe_allow_html=True)
```

## Troubleshooting Deployment Issues

### Issue: App won't start
**Check:**
- `requirements.txt` has all dependencies
- Python version compatibility (add `runtime.txt` if needed)
- No syntax errors in `app.py`

**Create runtime.txt:**
```
python-3.11
```

### Issue: CSV files not loading
**Solutions:**
- Use relative paths: `pd.read_csv('books.csv')`
- Check file is in repository
- Verify file encoding (UTF-8)
- Use file uploader as fallback

### Issue: Out of memory
**Solutions:**
- Reduce dataset size
- Sample large dataframes
- Use more efficient data types:
```python
df = pd.read_csv('books.csv', dtype={'rating': 'float32'})
```

### Issue: Slow performance
**Solutions:**
- Enable caching on all expensive operations
- Lazy load data (load on demand)
- Optimize images (thumbnails, lazy loading)
- Reduce fuzzy match limit

### Issue: Session state not persisting
**Note:** Streamlit Cloud apps reset when idle. For persistent storage:
- Use external database
- Implement cookie-based session management
- Store in Streamlit Cloud secrets

## Security Best Practices

### 1. Environment Variables
Never commit sensitive data. Use secrets:

**.streamlit/secrets.toml** (local only, gitignored):
```toml
[database]
connection_string = "postgresql://user:pass@host:5432/db"

[api_keys]
tmdb_key = "your_api_key"
```

Access in code:
```python
db_string = st.secrets["database"]["connection_string"]
```

Add same secrets in Streamlit Cloud dashboard.

### 2. Input Validation
Sanitize user inputs:
```python
import re

def sanitize_input(text):
    # Remove special characters
    return re.sub(r'[^a-zA-Z0-9\s]', '', text)

book_name = sanitize_input(st.text_input("Book Name"))
```

### 3. Rate Limiting
Prevent abuse:
```python
from datetime import datetime, timedelta

if 'last_search' not in st.session_state:
    st.session_state.last_search = datetime.now() - timedelta(seconds=10)

if st.button("Search"):
    now = datetime.now()
    if (now - st.session_state.last_search).seconds < 2:
        st.warning("Please wait before searching again")
    else:
        # Perform search
        st.session_state.last_search = now
```

## Cost Considerations

**Streamlit Cloud Free Tier:**
- ✓ 1 private app
- ✓ Unlimited public apps
- ✓ Generous resource limits
- ✓ Automatic HTTPS
- ✓ Community support

**When to Upgrade:**
- Need more private apps
- Higher resource requirements
- Priority support
- Custom authentication

**Alternatives:**
- **Heroku** (free tier discontinued)
- **Railway** ($5/month)
- **Render** (free tier available)
- **AWS/Azure/GCP** (variable, more control)

## Maintenance

### Regular Updates

1. **Dependencies**: Update monthly
```powershell
pip install --upgrade streamlit pandas rapidfuzz
pip freeze > requirements.txt
```

2. **Security**: Monitor for CVEs
```powershell
pip audit  # or use safety
```

3. **Data**: Refresh CSV files regularly

### Monitoring

Set up alerts for:
- App downtime
- High resource usage
- Error spikes
- Slow response times

### Backup

Backup strategy:
1. Keep repository up-to-date (git push regularly)
2. Export datasets to external storage
3. Document configuration in README
4. Version control secrets separately

## Success Checklist

Before going live:

- [ ] App runs without errors locally
- [ ] All dependencies in requirements.txt
- [ ] CSV files validated and loaded
- [ ] Images displaying correctly
- [ ] Auto-refresh works safely
- [ ] Export functionality tested
- [ ] Mobile responsive (test on phone)
- [ ] Error messages user-friendly
- [ ] Documentation complete
- [ ] README with usage instructions
- [ ] Privacy policy (if collecting user data)
- [ ] Contact information for support

## Post-Deployment

### Share Your App

1. **Social Media**: Twitter, LinkedIn, Reddit
2. **Product Hunt**: Launch announcement
3. **Hacker News**: Show HN post
4. **Dev.to**: Write a tutorial
5. **GitHub**: Add to awesome-streamlit list

### Gather Feedback

- Add feedback form in app
- Monitor GitHub issues
- Track analytics
- Iterate based on user needs

### Promote

- Write blog post about building process
- Create YouTube demo video
- Share on data science communities
- Submit to app galleries

---

## 📚 Additional Resources

- [Streamlit Docs](https://docs.streamlit.io)
- [Streamlit Cloud Docs](https://docs.streamlit.io/streamlit-community-cloud)
- [Streamlit Forums](https://discuss.streamlit.io)
- [Streamlit Gallery](https://streamlit.io/gallery)

---

**Ready to deploy? Follow the steps above and your app will be live in minutes!**

*Questions? Check the Streamlit Forums or open a GitHub issue.*

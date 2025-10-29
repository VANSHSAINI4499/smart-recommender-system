"""
Test Script for Smart Recommender System
Run this to verify your installation and dataset setup.
"""

import sys
import os

def check_python_version():
    """Check if Python version is 3.8 or higher."""
    version = sys.version_info
    print(f"✓ Python version: {version.major}.{version.minor}.{version.micro}")
    if version.major >= 3 and version.minor >= 8:
        print("  ✓ Python version is compatible (3.8+)")
        return True
    else:
        print("  ✗ Python version too old. Need 3.8 or higher.")
        return False


def check_dependencies():
    """Check if required packages are installed."""
    required_packages = {
        'streamlit': 'streamlit',
        'pandas': 'pandas',
        'PIL': 'pillow',
        'rapidfuzz': 'rapidfuzz',
        'numpy': 'numpy',
        'requests': 'requests'
    }
    
    print("\n📦 Checking dependencies...")
    all_installed = True
    
    for import_name, package_name in required_packages.items():
        try:
            __import__(import_name)
            print(f"  ✓ {package_name} is installed")
        except ImportError:
            print(f"  ✗ {package_name} is NOT installed")
            all_installed = False
    
    return all_installed


def check_csv_files():
    """Check if required CSV files exist."""
    print("\n📁 Checking for CSV files...")
    required_files = ['books.csv', 'courses.csv', 'movies.csv']
    all_exist = True
    
    for filename in required_files:
        if os.path.exists(filename):
            size = os.path.getsize(filename)
            print(f"  ✓ {filename} found ({size:,} bytes)")
        else:
            print(f"  ⚠ {filename} NOT found (you can upload via UI)")
            all_exist = False
    
    return all_exist


def check_csv_structure():
    """Check if CSV files have required columns."""
    print("\n📊 Validating CSV structure...")
    
    try:
        import pandas as pd
        
        # Check books.csv
        if os.path.exists('books.csv'):
            try:
                df = pd.read_csv('books.csv', nrows=1)
                required_cols = ['title', 'authors', 'average_rating', 'image_url']
                missing = [col for col in required_cols if col not in df.columns]
                
                if not missing:
                    print(f"  ✓ books.csv has all required columns")
                    print(f"    Total columns: {len(df.columns)}, Rows: {len(pd.read_csv('books.csv'))}")
                else:
                    print(f"  ✗ books.csv missing columns: {missing}")
            except Exception as e:
                print(f"  ✗ Error reading books.csv: {e}")
        
        # Check courses.csv
        if os.path.exists('courses.csv'):
            try:
                df = pd.read_csv('courses.csv', nrows=1)
                required_cols = ['course_title', 'course_rating', 'course_difficulty']
                missing = [col for col in required_cols if col not in df.columns]
                
                if not missing:
                    print(f"  ✓ courses.csv has all required columns")
                    print(f"    Total columns: {len(df.columns)}, Rows: {len(pd.read_csv('courses.csv'))}")
                else:
                    print(f"  ✗ courses.csv missing columns: {missing}")
            except Exception as e:
                print(f"  ✗ Error reading courses.csv: {e}")
        
        # Check movies.csv
        if os.path.exists('movies.csv'):
            try:
                df = pd.read_csv('movies.csv', nrows=1)
                required_cols = ['Title', 'IMDB Score', 'Genre', 'Poster']
                missing = [col for col in required_cols if col not in df.columns]
                
                if not missing:
                    print(f"  ✓ movies.csv has all required columns")
                    print(f"    Total columns: {len(df.columns)}, Rows: {len(pd.read_csv('movies.csv'))}")
                else:
                    print(f"  ✗ movies.csv missing columns: {missing}")
            except Exception as e:
                print(f"  ✗ Error reading movies.csv: {e}")
                
    except ImportError:
        print("  ⚠ pandas not installed, skipping structure check")


def check_app_file():
    """Check if app.py exists."""
    print("\n📄 Checking for app.py...")
    if os.path.exists('app.py'):
        size = os.path.getsize('app.py')
        print(f"  ✓ app.py found ({size:,} bytes)")
        return True
    else:
        print(f"  ✗ app.py NOT found")
        return False


def main():
    """Run all checks."""
    print("=" * 60)
    print("🎯 Smart Recommender System - Installation Test")
    print("=" * 60)
    
    checks = {
        'Python Version': check_python_version(),
        'Dependencies': check_dependencies(),
        'CSV Files': check_csv_files(),
        'App File': check_app_file()
    }
    
    # Only check CSV structure if pandas is installed
    try:
        import pandas
        check_csv_structure()
    except ImportError:
        pass
    
    # Summary
    print("\n" + "=" * 60)
    print("📋 SUMMARY")
    print("=" * 60)
    
    for check_name, result in checks.items():
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{status}: {check_name}")
    
    all_passed = all(checks.values())
    
    print("\n" + "=" * 60)
    if all_passed:
        print("✅ ALL CHECKS PASSED!")
        print("\nYou're ready to run the app:")
        print("  streamlit run app.py")
    else:
        print("⚠️  SOME CHECKS FAILED")
        print("\nTo fix issues:")
        print("  1. Install dependencies: pip install -r requirements.txt")
        print("  2. Add CSV files or use UI uploader")
        print("  3. See QUICKSTART.md for detailed instructions")
    print("=" * 60)


if __name__ == "__main__":
    main()

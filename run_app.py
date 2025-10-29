"""
Quick Launch Script for Smart Recommender System
Run this script to automatically check setup and launch the app.
"""

import subprocess
import sys
import os

def print_banner():
    """Print welcome banner."""
    banner = """
    ╔════════════════════════════════════════════════════════╗
    ║                                                        ║
    ║        🎯 SMART RECOMMENDER SYSTEM 🎯                 ║
    ║                                                        ║
    ║     Books 📚 | Courses 🎓 | Movies 🎬                 ║
    ║                                                        ║
    ╚════════════════════════════════════════════════════════╝
    """
    print(banner)


def check_streamlit():
    """Check if Streamlit is installed."""
    try:
        import streamlit
        return True
    except ImportError:
        return False


def install_dependencies():
    """Offer to install dependencies."""
    print("\n⚠️  Streamlit not found!")
    response = input("Would you like to install dependencies now? (y/n): ")
    
    if response.lower() == 'y':
        print("\n📦 Installing dependencies...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
            print("✅ Dependencies installed successfully!")
            return True
        except subprocess.CalledProcessError:
            print("❌ Failed to install dependencies.")
            print("Please run manually: pip install -r requirements.txt")
            return False
    else:
        print("\n⚠️  Please install dependencies manually:")
        print("   pip install -r requirements.txt")
        return False


def check_app_file():
    """Check if app.py exists."""
    if not os.path.exists('app.py'):
        print("❌ app.py not found in current directory!")
        print("Please run this script from the ai_project3 directory.")
        return False
    return True


def run_app():
    """Launch the Streamlit app."""
    print("\n🚀 Launching Smart Recommender System...")
    print("━" * 60)
    print("📍 The app will open in your default browser")
    print("🌐 URL: http://localhost:8501")
    print("⏸️  Press Ctrl+C in this terminal to stop the app")
    print("━" * 60)
    print()
    
    try:
        subprocess.run(["streamlit", "run", "app.py"])
    except KeyboardInterrupt:
        print("\n\n👋 App stopped. Thanks for using Smart Recommender System!")
    except FileNotFoundError:
        print("❌ Streamlit command not found.")
        print("Try running directly: python -m streamlit run app.py")


def main():
    """Main launcher function."""
    print_banner()
    
    # Check if app.py exists
    if not check_app_file():
        input("\nPress Enter to exit...")
        sys.exit(1)
    
    # Check Streamlit installation
    if not check_streamlit():
        if not install_dependencies():
            input("\nPress Enter to exit...")
            sys.exit(1)
    
    # Check for CSV files
    csv_files = ['books.csv', 'courses.csv', 'movies.csv']
    missing_files = [f for f in csv_files if not os.path.exists(f)]
    
    if missing_files:
        print(f"\n⚠️  Warning: CSV files not found: {', '.join(missing_files)}")
        print("You can upload them via the app's sidebar once it launches.")
        response = input("\nContinue anyway? (y/n): ")
        if response.lower() != 'y':
            print("Please add CSV files and run again.")
            input("\nPress Enter to exit...")
            sys.exit(0)
    else:
        print("\n✅ All CSV files found!")
    
    # Launch app
    print("\n" + "━" * 60)
    input("Press Enter to launch the app...")
    run_app()


if __name__ == "__main__":
    main()

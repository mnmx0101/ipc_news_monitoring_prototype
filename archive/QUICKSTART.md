# 🚀 Quick Start Guide - Streamlit Dashboard

## TL;DR - Get Running in 3 Steps

```bash
# 1. Run setup script
setup_dashboard.bat

# 2. Edit .env and add your OpenAI API key
# Open .env in a text editor and replace:
# OPENAI_API_KEY=your_openai_key_here
# with your actual key

# 3. Run the dashboard
streamlit run app.py
```

---

## What You Need

✅ **Python 3.8+** installed  
✅ **OpenAI API key** (get one at platform.openai.com)  
✅ **Your processed CSV file** (`all_clean_df.csv`)

---

## Step-by-Step Setup

### Option A: Automated Setup (Recommended)

1. **Run the setup script:**
   ```bash
   setup_dashboard.bat
   ```

2. **Add your OpenAI API key:**
   - Open `.env` in any text editor
   - Find the line: `OPENAI_API_KEY=your_openai_key_here`
   - Replace with: `OPENAI_API_KEY=sk-your-actual-key`
   - Save the file

3. **Place your data file:**
   - Copy `all_clean_df.csv` to `data/processed/`
   - Or update `DATA_PATH` in `.env` to point to your file

4. **Launch the dashboard:**
   ```bash
   streamlit run app.py
   ```

### Option B: Manual Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements-dashboard.txt
   ```

2. **Download NLTK data:**
   ```bash
   python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('punkt_tab')"
   ```

3. **Create .env file:**
   ```bash
   copy .env.example .env
   ```

4. **Edit .env and add your OpenAI key**

5. **Place your CSV file in `data/processed/`**

6. **Run the dashboard:**
   ```bash
   streamlit run app.py
   ```

---

## Where to Put Your OpenAI API Key

### Getting an API Key

1. Go to https://platform.openai.com/api-keys
2. Sign in or create an account
3. Click "Create new secret key"
4. Copy the key (starts with `sk-`)

### Adding the Key to Your Project

**Method 1: Using .env file (Recommended)**

1. Open `.env` in the project root directory
2. Find this line:
   ```
   OPENAI_API_KEY=your_openai_key_here
   ```
3. Replace with your actual key:
   ```
   OPENAI_API_KEY=sk-proj-abc123...
   ```
4. Save the file

**Important:** Never commit your `.env` file to git! It's already in `.gitignore`.

---

## Troubleshooting

### "Data file not found"
- Check that your CSV is at `data/processed/all_clean_df.csv`
- Or update `DATA_PATH` in `.env` to match your file location

### "Missing OPENAI_API_KEY"
- Make sure you created a `.env` file (copy from `.env.example`)
- Check that your API key is correctly added to `.env`
- Restart the Streamlit app after editing `.env`

### "Module not found"
- Run: `pip install -r requirements-dashboard.txt`
- Make sure you're using Python 3.8 or higher

### Dashboard won't start
- Check if port 8501 is already in use
- Try: `streamlit run app.py --server.port 8502`

---

## What's Next?

Once the dashboard is running:

1. **Explore the filters** in the sidebar
2. **Try the time series charts** to see sentiment trends
3. **Use the heatmap** to identify regional anomalies
4. **Generate an LLM summary** for a specific region/timeframe

For detailed documentation, see [README_DASHBOARD.md](README_DASHBOARD.md)

---

## File Structure

```
news-analytics-platform/
├── app.py                      # Main dashboard application
├── .env                        # Your configuration (create this!)
├── .env.example                # Template for .env
├── requirements-dashboard.txt  # Dependencies
├── setup_dashboard.bat         # Automated setup script
├── README_DASHBOARD.md         # Full documentation
├── QUICKSTART.md              # This file
└── data/
    └── processed/
        └── all_clean_df.csv   # Your data file (place here!)
```

---

## Need Help?

1. Check [README_DASHBOARD.md](README_DASHBOARD.md) for detailed documentation
2. Review the troubleshooting section above
3. Verify your `.env` file is configured correctly
4. Ensure your CSV has the required columns (see README_DASHBOARD.md)

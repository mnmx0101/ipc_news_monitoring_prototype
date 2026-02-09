# News Analytics Platform - Setup Guide

This guide will help you set up and run the News Analytics Platform on your local machine.

## 1. Prerequisites

- **Anaconda/Miniconda**: Ensure you have Conda installed.
- **OpenAI API Key**: Required for RAG features.

## 2. Quick Launch (If set up)

If you have already run the setup once, simply double-click the **`launch_crisis_app.bat`** file in this folder. This will open the **Home** page, where you can navigate to different dashboards in the sidebar.

OR run from terminal:
```powershell
launch_crisis_app.bat
```

## 3. First Time Setup

If this is your first time, follow these steps to prepare your environment.

### Step A: Configure Environment Variables
1. Copy `.env.example` to `.env`:
   ```powershell
   copy .env.example .env
   ```
2. Open `.env` with a text editor (Notepad, VS Code).
3. **Important**: Paste your OpenAI API key into the `OPENAI_API_KEY` field.

### Step B: Create Clean Environment
We use a dedicated environment `crisis-dashboard` to avoid conflicts.

Open your Anaconda PowerShell Prompt and run:

```powershell
# 1. Create the environment (only if it doesn't exist)
conda create -n crisis-dashboard python=3.9 streamlit -y

# 2. Activate it
conda activate crisis-dashboard

# 3. Install Python dependencies
pip install pandas altair numpy nltk python-dotenv "openai==0.28.0"

# 4. Download NLTK data (Required for text processing)
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('punkt_tab')"
```

### Step C: Run the App
Once setup is complete, you can run the app:

```powershell
streamlit run Home.py
```
Use the **sidebar** to switch between the General and Crisis dashboards.

## Troubleshooting

- **"OpenAI API Key missing"**: Check your `.env` file.
- **"Protobuf/SSL errors"**: Ensure you are using the `crisis-dashboard` environment we created, not `master` or `base`.

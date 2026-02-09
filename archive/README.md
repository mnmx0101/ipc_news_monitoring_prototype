# News Analytics Platform

A comprehensive platform for scraping, processing, and visualizing news articles from multiple sources. Built for organizational use with deployment capabilities.

## 🎯 Features

- **Multi-Source News Scraping**: Automated scraping from various news sources
- **NLP Processing**: Sentiment analysis, entity extraction, topic modeling
- **Interactive Dashboard**: Real-time visualization of news trends and insights
- **API Backend**: RESTful API for data access
- **Deployment Ready**: Configured for cloud deployment (Docker, CI/CD)

## 📁 Project Structure

```
news-analytics-platform/
├── backend/                 # FastAPI backend
│   ├── api/                # API endpoints
│   ├── scraper/            # News scraping modules
│   ├── processor/          # NLP and data processing
│   ├── models/             # Database models
│   └── utils/              # Utility functions
├── frontend/               # React dashboard
│   ├── src/
│   │   ├── components/    # React components
│   │   ├── pages/         # Dashboard pages
│   │   └── services/      # API services
│   └── public/
├── data/                   # Data storage
│   ├── raw/               # Raw scraped data
│   ├── processed/         # Processed data
│   └── database/          # SQLite/PostgreSQL
├── notebooks/             # Jupyter notebooks for analysis
├── tests/                 # Unit and integration tests
├── docker/                # Docker configurations
├── .github/               # GitHub Actions workflows
└── docs/                  # Documentation

```

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- Node.js 18+
- Docker (optional, for containerized deployment)

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

### Docker Setup

```bash
docker-compose up --build
```

## 🔧 Configuration

Create a `.env` file in the root directory:

```env
# Database
DATABASE_URL=sqlite:///./data/database/news.db

# API Keys (add your sources)
NEWS_API_KEY=your_key_here

# Scraping Configuration
SCRAPE_INTERVAL=3600  # seconds
MAX_ARTICLES_PER_SOURCE=100

# Dashboard
DASHBOARD_PORT=3000
API_PORT=8000
```

## 📊 Data Sources

Currently supported news sources:
- AllAfrica.com
- NewsAPI
- RSS Feeds (configurable)
- Custom scrapers (extensible)

## 🧪 Testing

```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd frontend
npm test
```

## 🌐 Deployment

### Docker Deployment

```bash
docker-compose -f docker-compose.prod.yml up -d
```

### Cloud Deployment

- **AWS**: See `docs/deployment/aws.md`
- **Azure**: See `docs/deployment/azure.md`
- **Google Cloud**: See `docs/deployment/gcp.md`

## 📈 Dashboard Features

- **Real-time News Feed**: Latest articles with filtering
- **Sentiment Analysis**: Track sentiment trends over time
- **Topic Clustering**: Identify trending topics
- **Geographic Distribution**: Map-based visualization
- **Entity Recognition**: Track mentions of people, organizations, locations
- **Custom Alerts**: Set up notifications for specific keywords/topics

## 🛠️ Tech Stack

### Backend
- **FastAPI**: Modern Python web framework
- **SQLAlchemy**: ORM for database management
- **BeautifulSoup4/Scrapy**: Web scraping
- **spaCy/Transformers**: NLP processing
- **Celery**: Task queue for scheduled scraping

### Frontend
- **React + Vite**: Fast, modern UI
- **Recharts/D3.js**: Data visualization
- **TailwindCSS**: Styling
- **React Query**: Data fetching

### Infrastructure
- **Docker**: Containerization
- **PostgreSQL**: Production database
- **Redis**: Caching and task queue
- **Nginx**: Reverse proxy

## 📝 License

MIT License - See LICENSE file for details

## 🤝 Contributing

See CONTRIBUTING.md for guidelines

## 📧 Contact

For organizational support, contact: [your-email@organization.org]

---

**Last Updated**: January 29, 2026

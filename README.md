
PriceTracker
============

PriceTracker is a web-based system for monitoring product prices over time and predicting future price trends using Machine Learning. This project combines web scraping, data storage, machine learning modeling, and a web interface to deliver a full-stack solution for price intelligence.

Project Overview
----------------
The goal of this project is to provide users with historical price tracking and forecast whether a product's price is likely to increase or decrease. It is designed with modern technologies commonly used in the software development and data science industry.

Features
--------
- Automated price scraping from e-commerce websites
- Historical price storage in a PostgreSQL database
- Machine learning model to predict price movement
- RESTful API built with FastAPI to serve data and predictions
- Frontend interface for data visualization (work in progress)
- Containerized with Docker for consistent deployment

Tech Stack
----------
Language        : Python
Scraping        : Selenium / Playwright
Database        : PostgreSQL + SQLAlchemy
API             : FastAPI + Pydantic
ML Framework    : scikit-learn + pandas
Frontend        : HTML, CSS, JavaScript
Visualization   : Chart.js (via JS frontend)
Deployment      : Docker + Railway / Vercel

System Architecture
-------------------
- [ Scraper ] ---> [ PostgreSQL Database ]
-                      ↑
- [ ML Training ] <----┘
-      ↓
- [ FastAPI REST API ]
-      ↓
- [ Frontend (HTML/CSS/JS) ]

Setup Instructions (WIP)
------------------------
Note: This project is under active development. Setup and deployment instructions will be updated accordingly.

Requirements
- Python 3.10+
- Docker & Docker Compose (optional, for deployment)
- PostgreSQL (local or remote)
- Node.js (if using a JS framework in the future)

Quick Start (Backend Only)
1. Clone the repository:
   git clone https://github.com/your-username/pricetracker.git
   cd pricetracker

2. Install dependencies:
   pip install -r requirements.txt

3. Configure environment variables:
   Create a `.env` file and set your PostgreSQL connection and API settings.

4. Run the API:
   uvicorn backend.main:app --reload

Status
------
- [x] Web scraping implemented
- [ ] Data stored in PostgreSQL
- [ ] ML model under development
- [ ] Frontend in progress
- [ ] Full integration and deployment

Future Improvements
-------------------
- Add automated data collection scheduler
- Expand prediction model with external features (e.g., seasonality, demand spikes)
- User authentication and saved product watchlists
- Admin dashboard for monitoring

License
-------
This project is open-source and available under the MIT License.

Author
------
Kauan Barbosa Rezende
GitHub: https://github.com/kauan02
LinkedIn: https://www.linkedin.com/in/kauan-barbosa-5b8133268/

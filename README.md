# NeubAItics Research Hub: AI-Powered Review Sentiment & Insights Dashboard 🚀💡

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Node.js](https://img.shields.io/badge/Node.js-14%2B-green.svg)](https://nodejs.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://github.com/yourusername/neubaitics-research-hub)

---

## Overview
This project is an assignment for the NeubAItics Research Hub evaluation. It is a full-stack AI-powered web application that allows users to:
- **Register & Login:** Secure access via JWT-based authentication.
- **Submit Reviews:** Input product/service reviews.
- **Analyze Sentiment:** Use AI models (NLTK VADER / Hugging Face BERT) to classify reviews as Positive, Neutral, or Negative.
- **Visualize Trends:** Display sentiment distribution and recent reviews on an interactive dashboard.

---

## Environment & File Structure 🌐

### Environment:
- **Backend:** FastAPI (Python)
- **Frontend:** React.js (Vite/Next.js) with Tailwind CSS
- **Database:** PostgreSQL / MongoDB
- **Deployment:** Frontend on Vercel/Netlify, Backend on Render/AWS EC2, Database on MongoDB Atlas/Supabase


---

## Step-by-Step Process & Unique Aspects 🔍

1. **User Registration & Authentication**
   - **What:** Secure user access using JWT.
   - **How:** Users register/login; upon success, a JWT token is generated (see `backend/auth.py`).
   - **Unique:** Ensures secure sessions with token-based authentication.

2. **Review Submission & Sentiment Analysis**
   - **What:** Users submit reviews, and the system analyzes sentiment.
   - **How:** The frontend sends a POST request to the backend (`/reviews` endpoint). The backend pre-processes the review, and then either NLTK VADER (for quick analysis) or a fine-tuned BERT model (for advanced analysis) determines sentiment (see `backend/sentiment.py`).
   - **Unique:** Option to choose between a basic or advanced AI model, returning both sentiment labels and confidence scores.

3. **Data Storage & Dashboard Visualization**
   - **What:** Persist reviews and display sentiment trends.
   - **How:** Reviews and their AI analysis are stored in the database (handled in `backend/database.py`). The dashboard (React component) fetches and visualizes data with interactive charts.
   - **Unique:** Real-time insights via an interactive dashboard, with filtering options and trend visualization.

4. **Integration & Deployment**
   - **What:** Bringing together frontend, backend, and database in a scalable architecture.
   - **How:** Backend APIs are containerized and deployed on cloud platforms (e.g., Render/AWS). The frontend is deployed on Vercel/Netlify.
   - **Unique:** Modern deployment practices ensure scalability, reliability, and ease of maintenance.

---

## How to Set Up & Run 🛠️

### Backend Setup:
1. Navigate to the `backend` directory:
   ```bash
   cd backend

2.Install dependencies:
pip install -r requirements.txt

3.Start the FastAPI server:
uvicorn main:app --reload

### Frontend Setup:

1.Navigate to the  `frontend` directory:
  ```bash
  cd frontend

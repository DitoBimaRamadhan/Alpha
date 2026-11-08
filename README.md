# ALPHA AI - Monetized AI Platform

AI-powered content generation web app. Built with FastAPI (Backend) and React (Frontend).

## Features
- **AI Text Generation**: Create high-quality content instantly.
- **Monetization Ready**: Integrated pricing tiers (Free, Creator, Pro).
- **Usage Tracking**: Database models ready for tracking user requests.

## Tech Stack
- **Frontend**: React, TypeScript, Vite.
- **Backend**: FastAPI, Python, SQLAlchemy.
- **Database**: PostgreSQL (ready).

## Getting Started

### Backend
1. Go to `backend/`.
2. Install dependencies: `pip install -r requirements.txt`.
3. Create `.env` from the root template.
4. Run: `uvicorn app.main:app --reload`.

### Frontend
1. Go to `frontend/`.
2. Install dependencies: `npm install`.
3. Run: `npm run dev`.

## Deployment
This project is structure for easy deployment.
- **GitHub Actions**: Use for CI/CD.
- **Vercel/Netlify**: For frontend.
- **Render/Railway/Heroku**: For backend.

## Roadmap
- [ ] Connect real OpenAI/Anthropic API keys.
- [ ] Implement Stripe for real payments.
- [ ] Add User Authentication (JWT).
- [ ] Image Generation UI.

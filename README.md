# Registration Form (FastAPI + HTML)

A Google Forms-style registration form served by FastAPI. Fields:

- Full Name (text, required)
- Email (email, required)
- Age (number, optional)
- Phone Number (text, required)

Submissions are **not stored** — they're just logged to the server console.

## Run locally

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Open **http://127.0.0.1:8000** in your browser.

## Project structure

```
google-form-app/
├── main.py            # FastAPI app (serves form + handles /submit)
├── static/
│   └── index.html      # The form itself
├── requirements.txt
├── .gitignore
└── README.md
```

## Push to GitHub

```bash
cd google-form-app
git init
git add .
git commit -m "Initial commit: registration form with FastAPI backend"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```

Replace `<your-username>/<your-repo>` with your actual GitHub repo (create an empty one on GitHub first if it doesn't exist yet).

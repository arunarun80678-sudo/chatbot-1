# WebsitePlanner AI
Domain: Plan website structure, pages and features
Theme: Site Planner

Local:
```powershell
python -m venv venv
.\venv\Scripts\python.exe -m pip install -r requirements.txt
.\venv\Scripts\python.exe app.py
```
Open http://127.0.0.1:5000

Render Build: `pip install -r requirements.txt`
Render Start: `gunicorn --bind 0.0.0.0:$PORT app:app`

Configure title, domain, system prompt, behavior, welcome message, colors and PORT in config.py.

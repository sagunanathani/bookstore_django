📚 Bookstore Django Project
A full‑stack Django web application for managing books, sales records, and user authentication.
This project includes login, registration, CRUD operations, data visualization, and a responsive UI.


---

🚀 Features
- User authentication (Login, Logout, Register)
- Books management (list, details, CRUD)
- Sales records with Pandas DataFrame display
- Auto‑generated charts using Matplotlib
- Responsive homepage with image slider
- Modular templates using base.html
- Static files (CSS, JS, images) included
- SQLite for local development
- PostgreSQL for production (Railway)


---

🛠️ Tech Stack
- Python 3
- Django 5
- SQLite (local)
- PostgreSQL (Railway)
- Pandas
- Matplotlib
- Railway.app (Deployment)


---

## ⚙️ Installation (Local Setup)

### 1. Clone the repository
```bash
    git clone https://github.com/yourusername/bookstore_django.git
    cd bookstore_django

2. Create a virtual environment
    python -m venv venv
    source venv/bin/activate   # macOS/Linux
    venv\Scripts\activate      # Windows

3. Install dependencies
    pip install -r requirements.txt

4. Run migrations
    python manage.py migrate

5. Start the development server
    1. go to cmd - windows+r - cd "C:\Users\Saguna Nathani\Desktop\CF_Projects\bookstore_django"
    2. "C:\Users\Saguna Nathani\Envs\achievement2-practice\Scripts\activate.bat" - active 
    (achievement2-practice) C:\Users\Saguna Nathani\Desktop\CF_Projects\bookstore_django>
    python manage.py runserver

🌐 Deployment on Railway
1. Push project to GitHub
    Railway deploys directly from GitHub.

2. Create a new Railway project
    - Go to https://railway.app
    - Click New Project → Deploy from GitHub Repo

3. Add a PostgreSQL database
    Railway automatically generates:
        PGHOST
        PGDATABASE
        PGUSER
        PGPASSWORD
        PGPORT

4. Add environment variables
    In Railway → Variables:
    DJANGO_SECRET_KEY=your-secret-key
    DEBUG=False
    PGHOST=...
    PGDATABASE=...
    PGUSER=...
    PGPASSWORD=...
    PGPORT=...

5. Update Django settings for PostgreSQL
    import os

    if os.environ.get("RAILWAY_ENVIRONMENT"):
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'HOST': os.environ.get('PGHOST'),
                'NAME': os.environ.get('PGDATABASE'),
                'USER': os.environ.get('PGUSER'),
                'PASSWORD': os.environ.get('PGPASSWORD'),
                'PORT': os.environ.get('PGPORT'),
            }
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }

6. Static files for production
    STATIC_URL = '/static/'
    STATIC_ROOT = BASE_DIR / 'staticfiles'
    ALLOWED_HOSTS = ['*']

7. Add Procfile
    web: gunicorn bookstore_django.wsgi

8. Collect static files
    python manage.py collectstatic --noinput

9. Redeploy
    Railway will build and deploy automatically.

🔐 Creating a Superuser on Railway (No Shell Needed)
    Railway Starter plan does not provide a shell.
    So this project includes a custom management command:
    python manage.py createadmin

Add these variables in Railway:
    DJANGO_SUPERUSER_USERNAME=sagunanathani
    DJANGO_SUPERUSER_EMAIL=admin@example.com
    DJANGO_SUPERUSER_PASSWORD=yourpassword

To create a superuser:
- Go to Railway → Web Service → Settings
- Temporarily change Start Command to:
    python manage.py createadmin

- Deploy
- Change Start Command back to:
option 1: python manage.py migrate
option 2: python manage.py migrate && gunicorn bookstore_django.wsgi

📊 Data & Charts
    Sales data is displayed using:
    - Pandas DataFrame → rendered as HTML table
    - Matplotlib → converted to Base64 image and displayed in template

🖼️ Homepage Slider
    The homepage includes a full‑screen image slider using CSS animations.
    Add images in:
    static/sales/images/

🔐 Authentication
    - Django’s built‑in AuthenticationForm
    - Custom RegistrationForm
    - Login/Logout/Register views
    - Dynamic navbar (shows Login/Logout based on user state)

🤝 Contributing
    Pull requests are welcome!
    For major changes, please open an issue first to discuss what you’d like to improve.

📄 License
    This project is open‑source and available under the MIT License.

---









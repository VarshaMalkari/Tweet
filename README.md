TweetHeadQ - Django Twitter Clone
A simple Twitter-like application built with Django.

Features
✅ User authentication (Register, Login, Logout)
✅ Create, edit, and delete tweets
✅ Upload images with tweets
✅ Search tweets by username or keyword
✅ Bootstrap-styled UI

Installation
1️⃣ Clone the repository
    git clone https://github.com/your-username/tweetheadq.git
    cd tweetheadq

2️⃣ Create and activate a virtual environment
    python -m venv venv
    source venv/bin/activate  # Mac/Linux
    venv\Scripts\activate  # Windows

3️⃣ Install dependencies
    pip install -r requirements.txt

4️⃣ Run Migrations
    python manage.py migrate

5️⃣ Create a superuser (optional, for admin access)
    python manage.py createsuperuser

6️⃣ Start the server
    python manage.py runserver
    Now, visit http://127.0.0.1:8000/ in your browser.

Usage
    Register a new account or log in.
    Post tweets with text and images.
    Edit or delete your own tweets.
    Search for tweets using keywords or usernames.

Technologies Used
    Django (Backend)
    SQLite (Database)
    Bootstrap (Frontend)

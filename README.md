🚀 Redis Pub/Sub with Django – Simple Demo
This is a simple Django project that demonstrates how to use Redis Pub/Sub messaging for real-time communication.

🧰 Tech Stack
Backend: Django

Messaging System: Redis (via Docker)

Redis Client: redis-py

Virtual Environment: Python venv

📦 What This Project Does
When you visit a specific Django URL (/publish/), it publishes a message to a Redis channel.

A separate Python script (subscriber.py) listens to that Redis channel and prints messages in real time.

Redis runs in a Docker container on your local system.

🐳 How to Run Redis using Docker
bash
Copy
Edit
docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest
Redis is now accessible at localhost:6379

Redis Insight UI available at: http://localhost:8001

📁 Folder Structure
bash
Copy
Edit
redis_celery_learning/
├── manage.py
├── myproject/         # Django project settings
├── pubapp/            # Django app with pub view
├── subscriber.py      # Redis subscriber script
├── env/               # Python virtual environment (ignored in git)
├── db.sqlite3         # Sample DB (ignored in git)
├── .gitignore
└── README.md
🛠️ How to Run the Project
Create a virtual environment & activate it

bash
Copy
Edit
python -m venv env
env\Scripts\activate  # On Windows
Install dependencies

bash
Copy
Edit
pip install django redis
Run Django server

bash
Copy
Edit
python manage.py runserver
Run the Redis subscriber in a separate terminal

bash
Copy
Edit
python subscriber.py
Visit the publish URL

In your browser, go to:

arduino
Copy
Edit
http://127.0.0.1:8000/publish/
You’ll see the message appear in the terminal running subscriber.py.

📬 What This Demonstrates
Real-time message passing using Redis

Django as a publisher

Redis channel communication

Python script as a live subscriber

🧹 Notes
Redis is running via Docker to avoid local installations.

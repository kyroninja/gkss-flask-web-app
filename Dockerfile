# Start from an official Python base image.
# "slim" is a lightweight version — it has what we need without extra bloat.
FROM python:3.11-slim

# Set the working directory inside the container.
# All commands after this will run from /app, and our files will live here.
WORKDIR /app

# Copy the requirements file first, before copying the rest of the code.
# We do this separately so Docker can cache the pip install step —
# if requirements.txt hasn't changed, Docker skips reinstalling packages
# on the next build, which saves time.
COPY requirements.txt .

# Install dependencies inside the container.
# --no-cache-dir keeps the image size smaller by not storing the pip cache.
RUN pip install --no-cache-dir -r requirements.txt

# Install gunicorn — a production-grade WSGI server.
# We use this instead of Flask's built-in dev server, which isn't meant for real use.
RUN pip install --no-cache-dir gunicorn

# Now copy the rest of the project files into the container.
COPY . .

# Tell Docker that the container will listen on port 5000.
# This doesn't actually publish the port — that happens when you run the container.
EXPOSE 5000

# The command to run when the container starts.
# gunicorn will serve the Flask app defined in app.py as the variable "app".
# --bind 0.0.0.0:5000 makes it accessible from outside the container.
# --workers 2 spins up 2 worker processes to handle requests.
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:app"]

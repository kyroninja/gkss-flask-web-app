# Taskboard

A simple task tracking web app built with Flask. Made this to practice Flask routing and templates — nothing fancy, just a way to keep track of things you need to do.

## What it does

- Add tasks with a title and optional description
- View individual task details
- Mark tasks as complete
- Delete tasks

## Getting started

You'll need Python 3.8+ installed.

1. Clone the repo

2. Create and activate a virtual environment:

   **Mac/Linux:**
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

   **Windows:**
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the app:
   ```
   python app.py
   ```

5. Open your browser and go to `http://localhost:5000`

When you're done, you can deactivate the virtual environment with:
```
deactivate
```

## Running with Docker

If you have Docker installed, you can run the app without setting up Python or a venv locally.

**1. Build the image:**
```
docker build -t taskboard .
```
This reads the `Dockerfile` and packages the app into an image called `taskboard`.

**2. Run the container:**
```
docker run -p 5000:5000 taskboard
```
The `-p 5000:5000` maps port 5000 on your machine to port 5000 inside the container.

**3. Open your browser and go to `http://localhost:5000`**

To stop the container, press `Ctrl+C` in the terminal.

---

## Known issues

There are a few bugs I haven't gotten around to fixing yet — see the [Issues](../../issues) tab. Contributions welcome!

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT — see [LICENSE](LICENSE).

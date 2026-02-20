from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# in-memory task list, probably should move this to a db at some point
tasks = []
next_id = 1


@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add_task():
    global next_id
    title = request.form.get("title")
    description = request.form.get("description")

    # BUG 1: no validation — empty tasks can be added
    new_task = {
        "id": next_id,
        "title": title,
        "description": description,
        "done": False
    }
    tasks.append(new_task)
    next_id += 1

    return redirect(url_for("index"))


@app.route("/task/<int:task_id>")
def view_task(task_id):
    # BUG 2: uses a loop index instead of task id — breaks when tasks are deleted
    task = None
    for t in tasks:
        if t["id"] == task_id:
            task = t
    
    # BUG 3: missing 404 handling — just crashes with a TypeError if task not found
    return render_template("task.html", task=task)


@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = True
    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    global tasks
    # BUG 4: this removes ALL tasks, not just the one matching task_id
    tasks = [t for t in tasks if t["id"] == task_id]
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)

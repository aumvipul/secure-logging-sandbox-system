from flask import Flask, render_template, request
from tamper_log.log_system import TamperEvidentLogger
from tamper_log.verifier import verify_logs
from sandbox.sandbox import run_sandbox

app = Flask(__name__)
logger = TamperEvidentLogger()

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    issues = []

    if request.method == "POST":
        action = request.form.get("action")

        if action == "add_log":
            event = request.form.get("event")
            desc = request.form.get("description")
            logger.add_log(event, desc)
            message = "✅ Log added successfully"

        elif action == "verify":
            issues = verify_logs(logger.get_logs())

        elif action == "run_code":
            code = request.form.get("code")
            output = run_sandbox(code)

            logger.add_log("Sandbox Execution", code)
            message = output

    return render_template(
        "index.html",
        logs=logger.get_logs(),
        message=message,
        issues=issues
    )

if __name__ == "__main__":
    app.run(debug=True)
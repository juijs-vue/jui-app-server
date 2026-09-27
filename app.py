import os

from flask import Flask, abort, request, send_from_directory

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 서버 구현에 속하는 파일/디렉터리는 정적 서빙 대상에서 제외한다.
EXCLUDED_NAMES = {"app.py", "requirements.txt", "venv", ".git", "app.yaml", ".gcloudignore"}

app = Flask(__name__)


@app.route("/export", methods=["POST"])
def export():
    filename = request.form.get("filename")
    filetext = request.form.get("filetext")
    if not filename or filetext is None:
        abort(400, description="filename, filetext 파라미터가 필요합니다.")

    body = filetext.encode("utf-8")
    response = app.response_class(body, mimetype="text/plain")
    response.headers["Pragma"] = "public"
    response.headers["Expires"] = "0"
    response.headers["Cache-Control"] = "must-revalidate, post-check=0, pre-check=0"
    response.headers["Content-Disposition"] = f"attachment; filename={filename}"
    response.headers["Content-Length"] = str(len(body))
    return response


@app.route("/", defaults={"filepath": ""})
@app.route("/<path:filepath>")
def serve_file(filepath):
    if not filepath or filepath.endswith("/"):
        filepath = os.path.join(filepath, "index.html")

    parts = filepath.split("/")
    if any(part in EXCLUDED_NAMES for part in parts):
        abort(404)

    directory, name = os.path.split(filepath)
    full_directory = os.path.join(BASE_DIR, directory)
    return send_from_directory(full_directory, name)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

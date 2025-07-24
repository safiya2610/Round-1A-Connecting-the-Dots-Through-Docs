from flask import Flask, render_template, request, send_from_directory, redirect, url_for
import os
from process import extract_outline

# Folder setup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "input")
OUTPUT_FOLDER = os.path.join(BASE_DIR, "static", "output")

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Flask app setup
app = Flask(__name__, static_folder="static")

@app.route("/", methods=["GET"])
def index():
    pdfs = os.listdir(UPLOAD_FOLDER)
    jsons = os.listdir(OUTPUT_FOLDER)

    file_pairs = []
    for f in pdfs:
        base, _ = os.path.splitext(f)
        json_name = base + ".json"
        if json_name in jsons:
            file_pairs.append((f, json_name))

    return render_template("index.html", file_pairs=file_pairs)

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files['pdf_file']
    if file and file.filename.endswith(".pdf"):
        input_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(input_path)

        output_filename = file.filename.replace(".pdf", ".json")
        output_path = os.path.join(OUTPUT_FOLDER, output_filename)

        extract_outline(input_path, output_path)

    return redirect(url_for("index"))

@app.route("/delete", methods=["POST"])
def delete():
    input_file = request.form["input_file"]
    output_file = request.form["output_file"]

    try:
        os.remove(os.path.join(UPLOAD_FOLDER, input_file))
        os.remove(os.path.join(OUTPUT_FOLDER, output_file))
    except FileNotFoundError:
        pass

    return redirect(url_for("index"))

@app.route("/download/<folder>/<filename>")
def download(folder, filename):
    folder_path = UPLOAD_FOLDER if folder == "input" else OUTPUT_FOLDER
    return send_from_directory(folder_path, filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)  # 👈 Add this for auto-reload and better error messages

# 📄 PDF/Text to JSON Outline Converter (Flask App)

This is a simple web app that allows users to upload `.pdf` or `.txt` files, extracts structured outline information (like title and headings), and generates corresponding `.json` files. All uploaded files and outputs are listed in a table with options to open or delete them.

---

## 🚀 Features

- Upload `.pdf` or `.txt` files
- Automatically extract headings and generate `.json` outline
- Display all uploaded and generated files in a clean table
- Click to open any file in a new tab
- Delete files directly from the interface
- Beautiful UI with custom styled buttons
- Deployable easily on Render or any cloud

---

## 🧰 Tech Stack

- **Frontend**: HTML, CSS (custom styles)
- **Backend**: Python + Flask
- **PDF Handling**: `PyMuPDF (fitz)`
- **Deployment**: Render.com (Free Tier)

---

## 📂 Project Structure

🐳 Run using Docker (Optional)
If you prefer Docker:

bash
Copy
Edit
docker build -t pdf-outliner .
docker run -p 5000:5000 pdf-outliner



---

## ⚙️ Setup Locally (without Docker)

```bash
git clone https://github.com/your-username/pdf-json-outliner.git
cd pdf-json-outliner

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run app
python app.py

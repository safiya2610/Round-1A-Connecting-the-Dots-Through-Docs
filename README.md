# 📄 PDF/Text to JSON Outline Converter (Flask App)

A simple web app to upload `.pdf` or `.txt` files, extract structured outline information (like Title, H1, H2, H3 with page numbers), and generate corresponding `.json` outputs. The app displays all uploaded files and outputs in a clean, interactive table with options to **view** or **delete** files.

---

##  Features

- Upload `.pdf` or `.txt` files
- Extract structured headings and metadata
- Generate `.json` outline files
- Display uploaded/processed files in a responsive table
- Click to open/view any file in a new tab
- Delete uploaded or generated files
- Clean and responsive UI

---

## Tech Stack

- **Frontend**: HTML5, CSS3 (Custom styled)
- **Backend**: Python 3 + Flask
- **PDF Parsing**: `PyMuPDF (fitz)`
- **Deployment**: Render.com (Free tier), Docker (Optional)

---


---

##  Setup Locally (Without Docker)
### 1. Clone the repository
```bash
git clone https://github.com/your-username/pdf-json-outliner.git
cd pdf-json-outliner
```
### 2. Create a virtual environment and activate it
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
python app.py
```
### 4. Run the Flask app
```bash
python app.py
```
## Run using Docker 
```bash
docker build -t pdf-outliner .
docker run -p 5000:5000 pdf-outliner
```


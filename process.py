import fitz  # PyMuPDF
import json
import pytesseract
from PIL import Image
from langdetect import detect
import os

def detect_language(text):
    
    try:
        return detect(text)
    except:
        return "unknown"

def extract_outline(pdf_path, output_path):
    doc = fitz.open(pdf_path)
    headings = []
    max_font = 0
    title = None
    languages = {}

    for page_num, page in enumerate(doc, start=1):
        text = page.get_text()
        
        
        if not text.strip():
            pix = page.get_pixmap(dpi=300)
            img_path = f"page_{page_num}.png"
            pix.save(img_path)

            # OCR with possible Japanese vertical support
            text = pytesseract.image_to_string(Image.open(img_path), lang="jpn+eng", config="--psm 6")
            os.remove(img_path)

      
        lang = detect_language(text)
        languages[page_num] = lang

        blocks = page.get_text("dict", flags=11)["blocks"]
        for b in blocks:
            if "lines" in b:
                for l in b["lines"]:
                    for s in l["spans"]:
                        span_text = s["text"].strip()
                        if not span_text:
                            continue
                        size = s["size"]
                        if size > max_font:
                            max_font = size
                            title = span_text
                        if size > 16:
                            level = "H1"
                        elif size > 14:
                            level = "H2"
                        elif size > 12:
                            level = "H3"
                        else:
                            continue
                        headings.append({
                            "level": level,
                            "text": span_text,
                            "page": page_num
                        })

    result = {
        "title": title or "Unknown",
        "outline": headings,
        "languages": languages
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

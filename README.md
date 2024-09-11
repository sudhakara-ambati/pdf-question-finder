# Past Papers Topic Search

**Past Papers Topic Search** is a script designed to help students and educators find topic-specific questions from a collection of past exam papers. By searching through text-based past papers, this script allows users to quickly locate questions related to specific topics, improving study efficiency and exam preparation.

## Features

- **Topic Search:** Identifies and extracts questions related to specific topics from a collection of past exam papers.
- **Text Extraction:** Processes and extracts text from various file formats, including PDF.

## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/past-papers-topic-search.git
    cd past-papers-topic-search
    ```

2. **Install Dependencies:**

- Python 3.x
- `requests`
- `PyPDF2`
- `fitz`
- `PIL`

## Usage

1. **Prepare Your Past Papers:**
   - Ensure your past papers are in PDF or DOCX format and placed in a directory.

2. **Run the Script:**

    ```bash
    python main.py
    ```


3. **View Results:**
   - The script will output a list of questions related to the specified topic, including their locations in the papers.

# Flask URL Shortener

A simple URL shortener web application built with Python Flask and MongoDB.  
Shorten long URLs to compact, shareable links, and redirect them easily.

---

## Features

- Shorten long URLs to a 6-character unique code
- Redirect shortened URLs to original URLs
- MongoDB backend for URL storage
- Basic form validation and user-friendly UI
- Easily customizable and extendable

---

## Tech Stack

- Backend: Python, Flask
- Database: MongoDB (Atlas or local)
- Frontend: HTML with Tailwind CSS
- Dependencies: pymongo, python-dotenv

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone <repository-url>
cd url-shortener
```

### 2. Create and activate a virtual environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file in the project root with:

```env
MONGO_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/url_db?retryWrites=true&w=majority
BASE_URL=http://localhost:5000
```

Replace `<username>`, `<password>`, and cluster URL with your MongoDB Atlas credentials.

### 5. Run the app

```bash
python app.py
```

Open your browser and visit: `http://localhost:5000`

---

## Usage

- Enter a long URL in the input box.
- Click **Shorten URL**.
- Copy the generated short URL and use it to redirect to the original link.

---

## Troubleshooting

- **DNS errors connecting to MongoDB Atlas?**  
Try using the standard (non-`+srv`) MongoDB connection string from Atlas instead.

- **Activate virtual environment properly on Windows:**  
Use `venv\Scripts\activate` in CMD or PowerShell.

---

## License

- MIT License © 2025 Arghya Dutta <br>
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as per the terms of the license. See [LICENSE](LICENSE) for details.

---

## Contact

For questions or suggestions, contact [arghyadutta2002@gmail.com](mailto:arghyadutta2002@gmail.com)

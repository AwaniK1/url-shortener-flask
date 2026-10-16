# URL Shortener with Click Analytics

A lightweight URL shortening web application built using **Python, Flask, and SQLite**. It converts long URLs into short, shareable links and tracks how many times each link is accessed.

## Features

- **URL Shortening:** Generates unique, six-character alphanumeric short codes.
- **Custom Aliases:** Allows users to create memorable links using custom aliases.
- **Duplicate URL Handling:** Reuses an existing short code when the same URL is submitted without a custom alias.
- **URL Redirection:** Redirects users from a short link to the original destination.
- **Click Analytics:** Tracks the number of times a shortened link is accessed.
- **URL Validation:** Validates URLs before creating short links.
- **Persistent Storage:** Stores URL mappings and click counts in an SQLite database.
- **Automated Testing:** Includes tests using Pytest for key application functionality.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Flask | Web framework and routing |
| SQLite | Database for storing URLs and click counts |
| HTML & CSS | User interface |
| JavaScript | Copy-to-clipboard functionality and click-count updates |
| Pytest | Automated testing |

## Project Structure

```text
url-shortener/
├── app.py
├── database.py
├── test_app.py
├── requirements.txt
├── templates/
│   └── index.html
├── .gitignore
└── README.md
```


## Getting Started

### Prerequisites

- Python 3.10 or later
- pip

### 1. Clone the repository

```bash
git clone https://github.com/AwaniK1/url-shortener-flask.git
cd url-shortener
```

### 2. Create a virtual environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

Open the following address in your browser:

```text
http://127.0.0.1:5000
```

The SQLite database is initialized automatically when the application starts.

## How to Use

1. Enter a long URL, such as `https://www.google.com`.
2. Optionally enter a custom alias, such as `google`.
3. Click **Shorten URL**.
4. Copy the generated short link.
5. Open the short link to be redirected to the original website.
6. View the click count on the result page.

If no custom alias is supplied, the application generates a random short code. Repeated submissions of the same URL reuse the existing code, provided the URL is entered in the same format.

## Database Design

The application uses an SQLite table named `urls`.

| Column | Description |
|---|---|
| `id` | Unique record identifier |
| `original_url` | Original destination URL |
| `short_code` | Generated code or custom alias |
| `clicks` | Number of recorded redirects |

## Running Tests

Run the automated tests with:

```bash
pytest -v
```

The test suite covers key behaviours, including homepage loading, URL validation, and custom alias creation.

## Future Improvements

- User authentication and personal link management
- Expiration dates for shortened URLs
- QR code generation
- Detailed analytics and click history
- Rate limiting and stronger abuse prevention
- Support for a production database such as PostgreSQL

## Limitations

- The application is designed as a learning and portfolio project.
- SQLite is suitable for local development and small-scale usage.
- Custom aliases must be unique.
- URLs with different formats, such as `http://example.com` and `https://example.com`, may be stored separately.
- The local development server is not intended for production deployment.

## Learning Outcomes

This project demonstrates practical experience with:

- Building web applications using Flask
- Designing database operations with SQLite
- Implementing HTTP routing and redirects
- Validating user input
- Tracking application metrics
- Writing automated tests with Pytest



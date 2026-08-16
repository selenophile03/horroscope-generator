# horroscope-generator
# Horoscope Generator

A lightweight, local self-hosted web application that calculates astrological zodiac signs based on birth dates and generates daily personal overview metrics. Built on a split architecture using a FastAPI Python backend service and a native JavaScript/Tailwind CSS frontend dashboard.

## Features

- **Date-to-Zodiac Evaluation Matrix**: Local algorithmic computation of western tropical zodiac boundary ranges without external network dependencies.
- **Categorized Insight Mapping**: Delivers distinct, structured updates covering love, career, and physical wellness parameters.
- **Dynamic Frontend Integration**: An asynchronous user interface utilizing the native Fetch API to query local web services.

## Repository Layout

```text
horoscope-generator/
├── app/
│   ├── __init__.py
│   ├── main.py            # FastAPI Application Entrypoint & Asset Router
│   └── calculator.py      # Zodiac date ranges and prediction engines
├── static/
│   └── index.html         # Tailwind CSS UI dashboard
├── .gitignore             # Standard target build exclusions
├── requirements.txt       # Python environment dependencies
└── README.md              # System deployment documentation
```

## Setup and Installation

### Prerequisites
- Python 3.8 or higher installed on your system.

### Local Development Environment Setup

1. **Clone the repository infrastructure down locally:**
   ```bash
   git clone https://github.com
   cd horoscope-generator
   ```

2. **Initialize and activate an isolated Python virtual environment:**
   ```bash
   python -m venv venv
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows (Command Prompt):
   venv\Scripts\activate
   # On Windows (PowerShell):
   .\venv\Scripts\Activate.ps1
   ```

3. **Install application dependencies via pip:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

Start the local development server using Uvicorn with hot-reload enabled:

```bash
uvicorn app.main:app --reload
```

Once the terminal confirms startup, open your web browser and navigate to:
```text
http://127.0.0.1:8000
```

## API Documentation

### Get Daily Horoscope

Returns computed zodiac classification along with generated prediction details.

- **URL:** `/api/horoscope`
- **Method:** `GET`
- **Query Parameters:**
  - `month` (integer, required): Birth month integer value range `1-12`.
  - `day` (integer, required): Birth day integer value range `1-31`.

#### Sample Request URL
```text
http://127.0.0
```

#### Sample Response Payload (`200 OK`)
```json
{
  "zodiac": "Aries",
  "love": "Clear communication will heal a lingering misunderstanding.",
  "career": "Your focus shifts toward long-term professional stability.",
  "wellness": "Hydration and fresh air will dramatically lift your mood.",
  "lucky_number": 42,
  "lucky_color": "Indigo"
}
```

#### Error States
- `400 Bad Request`: Returned if numerical limits fall out of range (e.g., month = 13).

## Contribution
Submit pull requests against the main branch. Ensure all module paths remain relative to the application workspace core during refactoring phases.

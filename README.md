# 3-Tier Application

A simple 3-tier application with static frontend, Python backend, and MySQL database.

## Architecture

- **Frontend**: Static HTML/CSS/JavaScript
- **Backend**: Python Flask REST API
- **Database**: MySQL (AWS RDS)

## Setup Instructions

### 1. Database Setup (MySQL RDS)

Run the SQL schema in `database/schema.sql` on your RDS MySQL instance:

```bash
mysql -h your-rds-endpoint.region.rds.amazonaws.com -u admin -p < database/schema.sql
```

### 2. Backend Setup

```bash
cd backend
pip install -r requirements.txt

# Copy and configure environment variables
cp .env.example .env
# Edit .env with your RDS credentials

# Run the backend
python app.py
```

The backend will run on `http://localhost:5000`

### 3. Frontend Setup

Simply open `frontend/index.html` in a web browser, or serve it with a simple HTTP server:

```bash
cd frontend
python -m http.server 8000
```

Then visit `http://localhost:8000`

## Configuration

Edit `backend/.env` with your RDS MySQL credentials:

```
DB_HOST=your-rds-endpoint.region.rds.amazonaws.com
DB_USER=admin
DB_PASSWORD=your-password
DB_NAME=app_db
DB_PORT=3306
```

## API Endpoints

- `GET /api/items` - Get all items
- `POST /api/items` - Add new item
- `DELETE /api/items/<id>` - Delete item

## Project Structure

```
.
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── .env.example
├── database/
│   └── schema.sql
└── README.md
```

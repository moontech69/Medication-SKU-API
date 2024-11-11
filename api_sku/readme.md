# Project Title: Medication API
A Django-based backend API that manages medication SKUs, allowing CRUD operations and bulk uploads. This API is designed to simplify managing a catalog of medications with unique constraints.

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Running the Project](#running-the-project)
- [API Documentation](#api-documentation)
- [Running Tests](#running-tests)
- [Deployment](#deployment)

## Features

- CRUD operations for managing individual medication SKUs.
- Bulk upload endpoint for adding multiple medications at once.
- Unique constraints to prevent duplicate medication entries.
- Built with Django REST Framework and includes automated tests.


## Getting Started

These instructions will help you set up and run the project on your local machine for development and testing.

---

## Prerequisites

- **Python** (version 3.6 or above)
- **Django** (version 3.1 or above)
- **SQLite** (included by default with Django, used for local development)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Set up a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## Environment Variables

Create a `.env` file in the root directory to store environment variables.

```plaintext
SECRET_KEY=your_secret_key
DEBUG=True  # Set to False in production
```

---

## Running the Project

1. **Apply database migrations**:
   ```bash
   python manage.py migrate
   ```

2. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

3. Open your browser and navigate to `http://127.0.0.1:8000` to view the project.

---

## API Documentation

Below is a quick overview of the available API endpoints.

| Endpoint                     | Method | Description                     |
|------------------------------|--------|---------------------------------|
| `/api/v1/medications/`          | GET    | Retrieve all medications        |
| `/api/v1/medications/`          | POST   | Create a new medication SKU     |
| `/api/v1/medications/<id>/`     | GET    | Retrieve a specific medication  |
| `/api/v1/medications/<id>/`     | PUT    | Update a specific medication    |
| `/api/v1/medications/<id>/`     | DELETE | Delete a specific medication    |
| `/api/v1/medications/bulk-upload/`     | POST   | Bulk upload medications         |

### Pagination

The API supports pagination, by default responses have a page_size=10 but if you want change that you can pass through params page_size={your_page_size_number}

Pages | HTTP Command
-- | -- 
Page 1 | `/api/v1/medications/?page=1`
Page 3 and Page size 15 | `/api/v1/medications/?page=3&page_size=15`
---

### Filters

The API supports filtering, you can filter by the attributes of a medication like this

Filter | HTTP Command
-- | --
Name filter | `/api/v1/medications/?medication_name=Amox`
Presentation filter | `/api/v1/medications/?presentation=Tablet`
## Running Tests

To run tests and ensure everything is working as expected, use:

```bash
python manage.py test
```

This command will run unit and integration tests for the API.

---

## Deployment

### Option 1: Using Docker

1. **Build the Docker image**:
   ```bash
   docker build -t medication-api .
   ```

2. **Run the Docker container**:
   ```bash
   docker run -p 8000:8000 medication-api
   ```

### Option 2: Deploy to Render

This project has been deployed to [Render](https://render.com), a cloud platform that supports easy deployment for Django projects. You can follow these steps to deploy to Render:

1. **Connect to GitHub**: Link your GitHub repository to Render.
2. **Create a New Web Service**: Select Django as the framework, and configure environment variables as needed.
3. **Set Up Build Commands**: Render will automatically detect Django’s build and start commands, but you may need to adjust them for your specific requirements.

The deployment on Render offers a free hosting tier, which is ideal for testing and development purposes.

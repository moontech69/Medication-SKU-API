
# Axmed SKU Catalogue API

This project is a simplified backend service for Axmed's medication SKU catalogue, enabling CRUD operations and bulk uploads for medication SKUs. It is designed to support frontend applications with robust API endpoints.

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup and Installation](#setup-and-installation)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [Testing](#testing)
- [Additional Notes](#additional-notes)

---

## Overview

Axmed aims to accelerate healthcare and pharmaceutical access in LMICs by allowing buyers to launch tenders for needed pharmaceuticals and enabling sellers to bid. This backend service allows for managing SKUs within a catalogue that supports CRUD operations and bulk uploads.

---

## Features
- Create, Read, Update, and Delete single medication SKUs
- Bulk creation of medication SKUs via JSON
- Data persistence with SQLite
- Automated testing suite

---

## Tech Stack
- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL
- **Containerization**: Docker, Docker Compose

---

## Setup and Installation

### Prerequisites
1. **Docker**: Install [Docker](https://www.docker.com/get-started) if it's not already installed.
2. **Git**: Ensure Git is installed ([Git download link](https://git-scm.com/downloads)).

### 1. Clone the Repository
   ```bash
   git clone https://github.com/moontech69/Medication-SKU-API.git
   cd Medication-SKU-API
   ```
### 2. Running the Application with Docker

#### 2.1 Build and Run Docker Containers
   ```bash
   docker-compose up --build
   ```
   This command will:
   - Build the Django application with SQLite as the database for simplicity in local development and testing.
   - Set up networking between the Django application container and other services (if applicable).

#### 2.2 Run Database Migrations
   ```bash
   docker-compose exec web python manage.py migrate
   ```

#### 3.3 Create a Superuser (Optional)
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

#### 3.4 Access the Application
   - API Base URL: `http://0.0.0.0:8000`
   - Django Admin Panel: `http://0.0.0.0:8000/admin`

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

---

## Testing

To run the test suite, use the following command:
```bash
docker-compose exec web python manage.py test
```

---

## Additional Notes
- **Shutting Down the Application**: To stop and remove containers, run:
  ```bash
  docker-compose down
  ```
- **Environment Configuration**: Adjust `.env` variables as needed for different environments (development, production).


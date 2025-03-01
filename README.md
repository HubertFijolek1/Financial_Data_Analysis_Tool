# Financial Data Analysis Tool

This is an internal financial data analysis tool built using FastAPI, PostgreSQL, Docker, and Linux (Debian/Ubuntu).

## Project Description
The tool collects and processes financial data, performs aggregations and trend analysis, generates reports (JSON/PDF) and dynamic charts, and sends alerts via email. It is intended for internal use by the finance department.

## Technologies
- Python, FastAPI
- PostgreSQL
- Docker, Docker Compose
- Linux (Debian/Ubuntu)

## Project Structure
- `main.py` – FastAPI application entry point
- Modules for data aggregation, reporting, alerts, and external API integration
- Environment configuration (Dockerfile, docker-compose.yml)
- Documentation and tests

## Instructions
1. Clone the repository.
2. Run `docker-compose up` to start the application.
3. Ensure Docker and Docker Compose are installed.

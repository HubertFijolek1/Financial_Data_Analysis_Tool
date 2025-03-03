# Financial Data Analysis Tool API Usage

## Endpoints

### Base Endpoint
- **GET /**  
  Returns a welcome message.

### Financial Reports
- **GET /financials/report**  
  Returns aggregated financial data (JSON).

- **GET /financials/report/pdf**  
  Returns a PDF report of financial records.

- **GET /financials/chart**  
  Returns a PNG image chart showing revenue trends.

### External Data Integration
- **GET /external-data**  
  Fetches external data asynchronously using the provided URL parameter.

For more details, please refer to the Swagger documentation at `/docs`.

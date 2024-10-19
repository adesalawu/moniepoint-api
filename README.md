# moniepoint-api
Here's a structured `README.md` template for your FastAPI project, following an open-source format. This will give contributors or users of your project all the essential information needed to set up and use your API.

```markdown
# FastAPI Push Payment Request API

This project is a Python-based API built using FastAPI. It interacts with Moniepoint's payment gateway to process payments, handle transactions, and retrieve payment statuses.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Running the API](#running-the-api)
- [Environment Variables](#environment-variables)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Authentication**: Authenticate to Moniepoint's API using client credentials.
- **Push Payment Requests**: Create payment requests to process transactions via various methods (e.g., card, POS transfer).
- **Transaction Status**: Retrieve transaction status details.
- **FastAPI Integration**: Built on top of FastAPI, with asynchronous support for high performance.
  
## Requirements
To run the project, ensure you have the following:
- Python 3.10 or higher
- FastAPI
- Uvicorn
- Pydantic Settings
- Python Dotenv
- Requests

## Installation
To set up the project locally, follow these steps:

### 1. Clone the Repository
```bash
git clone https://github.com/adesalaw/moniepoint-api.git
cd moniepoint-fastapi
```

### 2. Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up Environment Variables
Create a `.env` file in the root of your project and add your Moniepoint credentials:

```bash
# .env file
CLIENT_ID=your_moniepoint_client_id
CLIENT_SECRET=your_moniepoint_client_secret
BASE_URL=https://channel.moniepoint.com
```

### 5. Running the API
After setting up the environment variables, you can run the FastAPI application:

```bash
uvicorn app.main:app --reload
```

This will start the server at `http://127.0.0.1:8000`.

## Environment Variables
The following environment variables need to be set in the `.env` file:

| Variable        | Description                         |
|-----------------|-------------------------------------|
| `CLIENT_ID`     | Moniepoint Client ID                |
| `CLIENT_SECRET` | Moniepoint Client Secret            |
| `BASE_URL`      | Moniepoint API base URL             |

## API Endpoints
The following endpoints are available in this API:

### Authentication
**POST** `/v1/auth`

- **Description**: Authenticates and retrieves an access token from Moniepoint.
- **Request**: 
    ```json
    {
      "clientId": "your_moniepoint_client_id",
      "clientSecret": "your_moniepoint_client_secret"
    }
    ```
- **Response**: 
    ```json
    {
      "access_token": "string",
      "expires_in": 3600
    }
    ```

### Push Payment Request
**POST** `/process-payment/`

- **Description**: Initiates a push payment request.
- **Request**: 
    ```json
    {
      "terminalSerial": "your_terminal_serial",
      "amount": 1000,
      "merchantReference": "your_unique_reference",
      "transactionType": "PURCHASE",
      "paymentMethod": "CARD_PURCHASE"
    }
    ```
- **Response**: 
    ```json
    {
      "message": "Payment request received",
      "transactionDetails": {
        // Transaction details here
      }
    }
    ```

### Get Transaction Status
**GET** `/transaction-status/`

- **Description**: Retrieves the status of a given transaction.
- **Response**: 
    ```json
    {
      "transactionReference": "string",
      "status": "PROCESSED",
      "amount": 1000,
      "paymentMethod": "CARD_PURCHASE",
      "responseCode": "00"
    }
    ```

## Testing
You can test the API using Postman, cURL, or FastAPI's interactive documentation available at `http://127.0.0.1:8000/docs`.

### Example cURL Request
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/process-payment/' \
  -H 'Content-Type: application/json' \
  -d '{
  "terminalSerial": "your_terminal_serial",
  "amount": 1000,
  "merchantReference": "your_unique_reference",
  "transactionType": "PURCHASE",
  "paymentMethod": "CARD_PURCHASE"
}'
```

## Contributing
Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes and commit (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a Pull Request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

### Explanation of the `README.md`:
- **Features**: A list of what your API offers.
- **Requirements**: The dependencies needed to run the project.
- **Installation**: Step-by-step instructions to set up the project on a local environment.
- **Running the API**: Details on how to start the FastAPI server.
- **API Endpoints**: Detailed information about available API endpoints, including requests and responses.
- **Testing**: Instructions on how to test the API using cURL or the interactive FastAPI docs.
- **Contributing**: Guidelines for how others can contribute to the project.
- **License**: Information about the project's licensing.

Let me know if you'd like to modify or add anything else!
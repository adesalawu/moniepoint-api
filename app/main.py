"""
Author's Note:
This script serves as the entry point of the FastAPI application. It initializes the app, sets up routes, and launches the server using Uvicorn. The goal is to provide a high-performance API for handling push payment requests and transaction status using Moniepoint's gateway.

Feel free to modify the routes or add additional middleware as needed to extend the functionality.

Author: Adediran
Contact: adesalawu@icloud.com
"""
# app/main.py
from fastapi import FastAPI, HTTPException
from app.config import Settings
from app.models import PaymentRequest
import requests

app = FastAPI()

# Load environment variables
settings = Settings()

@app.post("/process-payment/")
def process_payment(payment: PaymentRequest):
    # Validate incoming payment request
    if not payment:
        raise HTTPException(status_code=400, detail="Request body is required")
    
    # Access clientId, clientSecret, and baseURL from environment variables
    client_id = settings.client_id
    client_secret = settings.client_secret
    base_url = settings.base_url

    # Construct API URL for processing payment
    url = f"{base_url}/v1/auth"  # Adjust this URL as needed based on the Moniepoint API docs

    # Example request payload to send to Moniepoint for processing card payment
    payload = {
        "clientId": client_id,
        "clientSecret": client_secret,
        "terminalSerial": payment.terminalSerial,
        "amount": payment.amount,
        "merchantReference": payment.merchantReference,
        "transactionType": payment.transactionType,
        "paymentMethod": payment.paymentMethod  # Ensure this is set to 'CARD_PURCHASE'
    }

    # Make the request to Moniepoint's API to process the payment
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Error communicating with Moniepoint API")

    # Return the API response
    return {
        "message": "Payment request received",
        "transactionStatus": response.json(),  # Process the response as needed
    }

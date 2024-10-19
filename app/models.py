"""
Author's Note:
This script serves as the entry point of the FastAPI application. It initializes the app, sets up routes, and launches the server using Uvicorn. The goal is to provide a high-performance API for handling push payment requests and transaction status using Moniepoint's gateway.

Feel free to modify the routes or add additional middleware as needed to extend the functionality.

Author: Adediran
Contact: adesalawu@icloud.com
"""
# app/models.py
from pydantic import BaseModel, Field
from typing import Optional

class PaymentRequest(BaseModel):
    clientId: str
    clientSecret: str
    terminalSerial: str
    amount: int
    merchantReference: str
    transactionType: str = "PURCHASE"
    paymentMethod: Optional[str] = "POS"
    cardNumber: str = Field(..., min_length=13, max_length=19)
    cardExpiryMonth: str = Field(..., min_length=2, max_length=2)
    cardExpiryYear: str = Field(..., min_length=2, max_length=2)
    cardCVV: str = Field(..., min_length=3, max_length=4)
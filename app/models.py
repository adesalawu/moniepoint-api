"""
Author's Note:
This script serves as the entry point of the FastAPI application. It initializes the app, sets up routes, and launches the server using Uvicorn. 

The goal is to provide a high-performance API for handling push payment requests and transaction status using Moniepoint's gateway.

Feel free to modify the routes or add additional middleware as needed to extend the functionality.

Author: Adediran
Contact: adesalawu@icloud.com
"""
# app/models.py
# app/models.py
from pydantic import BaseModel, Field

class PaymentRequest(BaseModel):
    clientId: str
    clientSecret: str
    terminalSerial: str
    amount: int
    merchantReference: str
    transactionType: str = Field("PURCHASE", description="The type of transaction, e.g., 'PURCHASE'")
    paymentMethod: str = Field("CARD_PURCHASE", description="Preferred method of payment, e.g., 'CARD_PURCHASE'")
    
    # Card-related fields
    cardNumber: str = Field(..., description="Card number for the transaction")
    cardExpiryMonth: int = Field(..., description="Expiry month of the card")
    cardExpiryYear: int = Field(..., description="Expiry year of the card")
    cardCVV: int = Field(..., description="Card CVV for the transaction")

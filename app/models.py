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
"""
Author's Note:
This script serves as the entry point of the FastAPI application. It initializes the app, sets up routes, and launches the server using Uvicorn. 

The goal is to provide a high-performance API for handling push payment requests and transaction status using Moniepoint's gateway.

Feel free to modify the routes or add additional middleware as needed to extend the functionality.

Author: Adediran
Contact: adesalawu@icloud.com
"""
# app/error_handling.py
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse

async def general_exception_handler(request: Request, exc: Exception):

    return JSONResponse(
        status_code=500,
        content={"message": "An internal server error occurred. Please try again later."},
    )

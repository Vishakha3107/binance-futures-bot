import sys
import logging

logger = logging.getLogger("Validator")

def validate_inputs(symbol: str, side: str, order_type: str, quantity: float, price: float = None):
    """
    Validates user input arguments before placing orders.
    Raises ValueError if validations fail.
    """
    # 1. Validate Symbol format
    if not symbol or not symbol.isalnum() or not symbol.isupper():
        raise ValueError(f"Invalid Symbol: '{symbol}'. Must be alphanumeric and uppercase (e.g., BTCUSDT).")
        
    # 2. Validate Side
    if side.upper() not in ["BUY", "SELL"]:
        raise ValueError(f"Invalid Side: '{side}'. Must be 'BUY' or 'SELL'.")
        
    # 3. Validate Order Type
    if order_type.upper() not in ["MARKET", "LIMIT"]:
        raise ValueError(f"Invalid Order Type: '{order_type}'. Must be 'MARKET' or 'LIMIT'.")
        
    # 4. Validate Quantity
    if quantity <= 0:
        raise ValueError(f"Quantity must be a positive number greater than 0. Provided: {quantity}")
        
    # 5. Validate Price for LIMIT orders
    if order_type.upper() == "LIMIT":
        if price is None or price <= 0:
            raise ValueError("Price is strictly required and must be greater than 0 for LIMIT orders.")
            
    logger.info("Local input validations passed successfully.")

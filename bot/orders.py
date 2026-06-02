import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException

logger = logging.getLogger("OrderManager")

class OrderManager:
    def __init__(self, binance_client: Client):
        self.client = binance_client

    def place_futures_order(self, symbol: str, side: str, order_type: str, quantity: float, price: float = None):
        """Dispatches an order to the Binance USDT-M Futures Testnet."""
        
        # Build standard configuration kwargs for parameters
        params = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "type": order_type.upper(),
            "quantity": quantity
        }
        
        # Inject price dependency if executing a LIMIT structure
        if order_type.upper() == "LIMIT":
            params["price"] = str(price)
            params["timeInForce"] = "GTC"  # Good 'Till Cancelled (Standard for Limit Orders)

        logger.info(f"Sending API payload request summary: {params}")

        try:
            # Call USDT-M futures order endpoint
            response = self.client.futures_create_order(**params)
            logger.info(f"API order placement successful. Order ID: {response.get('orderId')}")
            return response

        except BinanceAPIException as api_err:
            logger.error(f"Binance API validation error occured: Code {api_err.status_code} - {api_err.message}")
            raise api_err
        except BinanceOrderException as order_err:
            logger.error(f"Local parameters order exception: {str(order_err)}")
            raise order_err
        except Exception as net_err:
            logger.error(f"Network error or loss of connection encountered: {str(net_err)}")
            raise net_err

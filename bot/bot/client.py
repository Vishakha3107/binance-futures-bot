import os
import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException

logger = logging.getLogger("BinanceClient")

class BinanceFuturesClient:
    def __init__(self):
        # Fetch configurations from environment variables
        self.api_key = os.getenv("BINANCE_API_KEY")
        self.api_secret = os.getenv("BINANCE_API_SECRET")
        
        if not self.api_key or not self.api_secret:
            logger.error("API Keys missing from environment variables.")
            raise ValueError("Please set BINANCE_API_KEY and BINANCE_API_SECRET in your environment or .env file.")
        
        try:
            # Instantiate client pointing to testnet base URL
            self.client = Client(
                api_key=self.api_key,
                api_secret=self.api_secret,
                testnet=True  # Automatically switches base URL to https://testnet.binancefuture.com
            )
            logger.info("Successfully connected to Binance Futures Testnet client.")
        except Exception as e:
            logger.error(f"Failed to initialize Binance Client: {str(e)}")
            raise e

    def get_client(self) -> Client:
        return self.client

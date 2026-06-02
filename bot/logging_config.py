import logging
import os

def setup_logging():
    """Sets up a dual-handler logger: files for details, console for clean UI."""
    log_format = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    
    # Ensure logs directory exists
    os.makedirs("logs", exist_ok=True)
    
    # Root logger config
    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
        handlers=[
            logging.FileHandler("logs/trading_bot.log"),
            logging.StreamHandler()  # Keeps CLI interactive
        ]
    )
    
    # Suppress verbose third-party logs
    logging.getLogger("urllib3").setLevel(logging.WARNING)

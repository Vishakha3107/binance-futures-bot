import argparse
import sys
from dotenv import load_dotenv

# Load configurations prior to system evaluations
load_dotenv()

from bot.logging_config import setup_logging
from bot.client import BinanceFuturesClient
from bot.orders import OrderManager
from bot.validators import validate_inputs

def main():
    # Setup global Logging configs
    setup_logging()
    
    # Parse CLI input configurations
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Simplified Trading Bot CLI Execution Layer.")
    
    parser.add_argument("--symbol", type=str, required=True, help="Trading symbol ticker (e.g., BTCUSDT)")
    parser.add_argument("--side", type=str, required=True, choices=["BUY", "SELL"], help="Order execution side")
    parser.add_argument("--type", type=str, required=True, choices=["MARKET", "LIMIT"], help="Order execution type")
    parser.add_argument("--quantity", type=float, required=True, help="Order volume transaction quantity")
    parser.add_argument("--price", type=float, default=None, help="Asset target order unit limit price (Required only if type=LIMIT)")
    
    args = parser.parse_args()

    print("\n" + "="*50)
    print("      BINANCE FUTURES TESTNET TRADING BOT EXECUTION")
    print("="*50)
    print(f"Requesting execution: {args.side} {args.quantity} {args.symbol} via {args.type} Order")
    if args.price:
        print(f"Target execution Limit Price: {args.price}")
    print("-"*50)

    try:
        # Step 1: Input Local Validations Validation Layer
        validate_inputs(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )
        
        # Step 2: Initialize connection engine layers
        bot_client = BinanceFuturesClient()
        order_manager = OrderManager(binance_client=bot_client.get_client())
        
        # Step 3: Route transaction dispatch logic layers
        response = order_manager.place_futures_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )
        
        # Step 4: Display Pretty Success Outputs
        print("\n[SUCCESS] Order Placed Successfully!")
        print(f"  - Order ID      : {response.get('orderId')}")
        print(f"  - Current Status: {response.get('status')}")
        print(f"  - Executed Qty  : {response.get('executedQty')}")
        print(f"  - Average Price : {response.get('avgPrice', 'N/A')} USDT")
        print("="*50 + "\n")

    except ValueError as val_err:
        print(f"\n[INPUT ERROR] Local execution validation blocked: {val_err}\n")
        sys.exit(1)
    except Exception as run_err:
        print(f"\n[EXECUTION ERROR] Server failed to process order: {run_err}\n")
        sys.exit(1)

if __name__ == "__main__":
    main()

"""Command-line interface for the Binance Futures Testnet trading bot.

Provides three sub‑commands:
  market  – place a market order
  limit   – place a limit order
  stop    – (optional) place a stop‑limit order

All arguments are validated and any exception is printed to stderr.
"""

import argparse
import sys
from bot.client import get_client
from bot import orders

def main():
    # Create the main parser. This is the "brain" that reads what you type in the terminal.
    parser = argparse.ArgumentParser(description='Binance Futures Testnet Trading Bot')
    
    # We use "subparsers" because we have different commands like 'market', 'limit', etc.
    # It's like having a toolbelt where you pick the specific tool you want to use.
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Market order
    market = subparsers.add_parser('market', help='Place a market order')
    market.add_argument('symbol', type=str, help='Trading pair, e.g. BTCUSDT')
    market.add_argument('quantity', type=float, help='Order quantity')
    market.add_argument('side', type=str, choices=['buy', 'sell'], help='Buy or sell')

    # Limit order
    limit = subparsers.add_parser('limit', help='Place a limit order')
    limit.add_argument('symbol', type=str)
    limit.add_argument('quantity', type=float)
    limit.add_argument('price', type=float, help='Limit price')
    limit.add_argument('side', type=str, choices=['buy', 'sell'])

    # Stop‑limit order (bonus)
    stop = subparsers.add_parser('stop', help='Place a stop‑limit order')
    stop.add_argument('symbol', type=str)
    stop.add_argument('quantity', type=float)
    stop.add_argument('price', type=float, help='Limit price')
    stop.add_argument('stop_price', type=float, help='Trigger price')
    stop.add_argument('side', type=str, choices=['buy', 'sell'])

    # This line actually reads the arguments you typed in the terminal
    args = parser.parse_args()
    
    # Connect to Binance (using the helper function we wrote in bot/client.py)
    client = get_client()

    try:
        # Check which command the user chose and call the right function
        if args.command == 'market':
            order = orders.place_market_order(client, args.symbol, args.quantity, args.side)
        elif args.command == 'limit':
            order = orders.place_limit_order(client, args.symbol, args.quantity, args.price, args.side)
        elif args.command == 'stop':
            order = orders.place_stop_limit_order(client, args.symbol, args.quantity, args.price, args.stop_price, args.side)
        else:
            parser.error('Unknown command')
            
        # If we get here, it worked! Print the receipt.
        print('Order placed successfully:')
        print(order)
    except Exception as e:
        # If anything crashed (like bad API keys or network error), print it nicely here.
        print(f'Error: {e}', file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()

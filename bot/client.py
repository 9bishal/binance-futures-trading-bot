"""Client wrapper for Binance Testnet.
Provides a thin abstraction over `python-binance` so the rest of the code
doesn't need to know about testnet configuration.
"""

import os
import logging
from binance.client import Client

# Configure basic logging – all modules import this logger
logging.basicConfig(
    filename='bot.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s %(message)s'
)
logger = logging.getLogger(__name__)

def get_client():
    """Create and return a Binance `Client` configured for testnet.
    Expects `BINANCE_API_KEY` and `BINANCE_API_SECRET` in env vars.
    """
    api_key = os.getenv('BINANCE_API_KEY')
    api_secret = os.getenv('BINANCE_API_SECRET')
    if not api_key or not api_secret:
        raise EnvironmentError('API credentials not set in environment variables')
    # Create the client using the keys.
    # `testnet=True` is the magic switch! It tells the library to talk to the
    # sandbox (fake money) servers instead of the real Binance exchange.
    client = Client(api_key, api_secret, testnet=True)
    
    logger.info('Initialized Binance testnet client')
    return client

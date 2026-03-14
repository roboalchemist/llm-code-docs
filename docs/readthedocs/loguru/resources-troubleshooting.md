# Frequently Asked Questions and Troubleshooting Tips for Loguru

## How do I create and configure a logger?

Loguru differs from standard logging as you don’t need to create a logger. It is directly provided by Loguru, and you should just import it:

```
from loguru import logger

logger.info("Hello, World!")

```
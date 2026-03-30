# Option 2: CLI for automation
0g-compute-cli setup-network  # Choose testnet/mainnet
0g-compute-cli login           # Connect your wallet
0g-compute-cli deposit --amount 10  # Fund account
0g-compute-cli inference list-providers  # See available services
```

**OpenAI SDK Drop-in Replacement**:
```python
from openai import OpenAI
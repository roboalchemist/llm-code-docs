# Prompt for the OpenAI API key securely
openai_api_key = getpass('Enter your API key: ')
os.environ["OPENAI_API_KEY"] = openai_api_key
```

***

## ⚙️ Initialize Clients

Set up the `OpenAI` and `Dappier` Python SDK clients.

```python Python theme={null}
from openai import OpenAI
from dappier import Dappier
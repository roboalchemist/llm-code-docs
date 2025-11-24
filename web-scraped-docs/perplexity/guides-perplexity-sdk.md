# Source: https://docs.perplexity.ai/guides/perplexity-sdk

## 
[​](https://docs.perplexity.ai/guides/perplexity-sdk#overview)
Overview
The official Perplexity SDKs provide convenient access to the Perplexity APIs from Python 3.8+ and Node.js applications. Both SDKs include type definitions for all request parameters and response fields, with both synchronous and asynchronous clients.
## 
[​](https://docs.perplexity.ai/guides/perplexity-sdk#available-apis)
Available APIs
## [Chat Completions AI responses with web-grounded knowledge, conversation context, and streaming support. ](https://docs.perplexity.ai/guides/chat-completions-sdk)## [Search Ranked web search results with filtering, multi-query support, and domain controls. ](https://docs.perplexity.ai/guides/perplexity-sdk-search)
## 
[​](https://docs.perplexity.ai/guides/perplexity-sdk#installation)
Installation
Install the SDK for your preferred language:
Python
TypeScript/JavaScript
Copy
Ask AI
```
pip install perplexityai

```

## 
[​](https://docs.perplexity.ai/guides/perplexity-sdk#authentication)
Authentication
## [Get your Perplexity API Key Navigate to the **API Keys** tab in the API Portal and generate a new key. Click here ](https://perplexity.ai/account/api) After generating the key, set it as an environment variable in your terminal:
  * Windows
  * MacOS/Linux


Copy
Ask AI
```
setx PERPLEXITY_API_KEY "your_api_key_here"

```

### 
[​](https://docs.perplexity.ai/guides/perplexity-sdk#using-environment-variables)
Using Environment Variables
You can use the environment variable directly:
Python
TypeScript/JavaScript
Copy
Ask AI
```
import os
from perplexity import Perplexity
client = Perplexity() # Automatically uses PERPLEXITY_API_KEY

```

Or use [python-dotenv](https://pypi.org/project/python-dotenv/) (Python) or [dotenv](https://www.npmjs.com/package/dotenv) (Node.js) to load the environment variable from a `.env` file:
Python
TypeScript/JavaScript
Copy
Ask AI
```
import os
from dotenv import load_dotenv
from perplexity import Perplexity
load_dotenv()
client = Perplexity() # Uses PERPLEXITY_API_KEY from .env file

```

Now you’re ready to start using the Perplexity APIs! Choose your API below for step-by-step usage guides.
## [Chat Completions Get started with AI responses ](https://docs.perplexity.ai/guides/chat-completions-sdk)## [Search Get started with web search ](https://docs.perplexity.ai/guides/perplexity-sdk-search)
## 
[​](https://docs.perplexity.ai/guides/perplexity-sdk#resources)
Resources
## [Python Package Install from PyPI with pip ](https://pypi.org/project/perplexityai/)## [Node.js Package Install from npm registry ](https://www.npmjs.com/package/@perplexity-ai/perplexity_ai)

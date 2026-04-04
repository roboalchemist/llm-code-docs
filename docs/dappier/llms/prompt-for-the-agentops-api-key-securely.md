# Prompt for the AgentOps API key securely
agentops_api_key = getpass('Enter your API key: ')
os.environ["AGENTOPS_API_KEY"] = agentops_api_key
```

Set up the OpenAI GPT4o-mini using the CAMEL ModelFactory. You can also configure other models as needed.

```python Python theme={null}
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType
from camel.configs import ChatGPTConfig
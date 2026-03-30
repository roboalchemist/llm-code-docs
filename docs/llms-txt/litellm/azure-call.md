# azure call
response = completion(
  "azure/<your_deployment_name>",
  messages = [{ "content": "Hello, how are you?","role": "user"}]
)

```

```codeBlockLines_e6Vv
from litellm import completion

response = completion(
            model="ollama/llama2",
            messages = [{ "content": "Hello, how are you?","role": "user"}],
            api_base="http://localhost:11434"
)

```

```codeBlockLines_e6Vv
from litellm import completion
import os

## set ENV variables
os.environ["OPENROUTER_API_KEY"] = "openrouter_api_key"

response = completion(
  model="openrouter/google/palm-2-chat-bison",
  messages = [{ "content": "Hello, how are you?","role": "user"}],
)

```

```codeBlockLines_e6Vv
from litellm import completion
import os

## set ENV variables. Visit https://novita.ai/settings/key-management to get your API key
os.environ["NOVITA_API_KEY"] = "novita-api-key"

response = completion(
  model="novita/deepseek/deepseek-r1",
  messages=[{ "content": "Hello, how are you?","role": "user"}]
)

```

### Streaming [​](https://docs.litellm.ai/\#streaming "Direct link to Streaming")

Set `stream=True` in the `completion` args.

- OpenAI
- Anthropic
- VertexAI
- NVIDIA
- HuggingFace
- Azure OpenAI
- Ollama
- Openrouter
- Novita AI

```codeBlockLines_e6Vv
from litellm import completion
import os

## set ENV variables
os.environ["OPENAI_API_KEY"] = "your-api-key"

response = completion(
  model="gpt-3.5-turbo",
  messages=[{ "content": "Hello, how are you?","role": "user"}],
  stream=True,
)

```

```codeBlockLines_e6Vv
from litellm import completion
import os

## set ENV variables
os.environ["ANTHROPIC_API_KEY"] = "your-api-key"

response = completion(
  model="claude-2",
  messages=[{ "content": "Hello, how are you?","role": "user"}],
  stream=True,
)

```

```codeBlockLines_e6Vv
from litellm import completion
import os
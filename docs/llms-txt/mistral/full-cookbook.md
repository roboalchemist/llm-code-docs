# Full Cookbook
You can find a comprehensive cookbook exploring Citations and References leveraging RAG with Wikipedia [here](https://colab.research.google.com/github/mistralai/cookbook/blob/main/mistral/rag/mistral-reference-rag.ipynb).  
This template will help get started with web search and document grounding with citations.


[Coding]
Source: https://docs.mistral.ai/docs/capabilities/coding

LLMs are powerfull tools for text generation, and they also show great performance in code generation for multiple tasks, both for code completion, code generation and agentic tool use for semi-automated software development.

We provide 2 major families of llms for coding:
- **Codestral**: Specifically trained for Code Generation and FIM.
- **Devstral**: Specifically trained for Agentic Tool Use for Software Development.

Note that we also provide **Codestral Embed**, for semantic search and embedding code databases, repositories, and powering coding assistants with state-of-the-art retrieval. Learn more about it [here](https://docs.mistral.ai/capabilities/embeddings/code_embeddings).

## Endpoints & Models
We provide 2 main endpoints:
- `https://api.mistral.ai/v1/fim/completions`: [Fill-in-the-middle](#fim), for code completion and code generation; supporting `codestral-latest`.
- `https://api.mistral.ai/v1/chat/completions`: [Instruction following](#instruct-following), for coding and agentic tool use; supporting `codestral-latest`, `devstral-small-latest` and `devstral-medium-latest`.

## FIM

With this feature, users can define the starting point of the code using a `prompt`, and the ending point of the code using an optional `suffix` and an optional `stop`. The FIM model will then generate the code that fits in between, making it ideal for tasks that require a specific piece of code to be generated.

:::tip[ ]
We also provide the `min_tokens` and `max_tokens` sampling parameters, which are particularly useful for code generation as it allows you to set the minimum and maximum number of tokens that should be produced. This is especially useful when FIM models decide to produce no tokens at all, or are overly verbose, allowing developers to enforce completions within a specific range if they are needed.
:::

### Codestral
Codestral is a cutting-edge generative model that has been specifically designed and optimized for code generation tasks, including fill-in-the-middle and code completion. Codestral was trained on 80+ programming languages, enabling it to perform well on both common and less common languages. 

:::important[ ]
We currently offer two domains for Codestral endpoints, both providing FIM and instruct routes:

| Domain  | Features |
| ------------- | ------------- |
| codestral.mistral.ai | - Monthly subscription based, currently free to use <br/> - Requires a new key for which a phone number is needed |
| api.mistral.ai  | - Allows you to use your existing API key and you can pay to use Codestral <br/> - Ideal for business use |

Wondering which endpoint to use?
- If you're a user, wanting to query Codestral as part of an IDE plugin, codestral.mistral.ai is recommended.
- If you're building a plugin, or anything that exposes these endpoints directly to the user, and expect them to bring their own API keys, you should also target codestral.mistral.ai
- For all other use cases, api.mistral.ai will be better suited

*This guide uses api.mistral.ai for demonstration.*
:::

Below we present three examples:  

#### Example 1: Fill in the middle
Originally, these models are designed to complete code in-between 2 points: a prefix (here called `prompt`) and a `suffix`, generating the code in-between.

<Tabs groupId="code">
  <TabItem value="python" label="python" default>

```python

from mistralai import Mistral

api_key = os.environ["MISTRAL_API_KEY"]
client = Mistral(api_key=api_key)

model = "codestral-latest"
prompt = "def fibonacci(n: int):"
suffix = "n = int(input('Enter a number: '))\nprint(fibonacci(n))"

response = client.fim.complete(
    model=model,
    prompt=prompt,
    suffix=suffix,
    temperature=0,
    # min_tokens=1, # Uncomment to enforce completions to at least 1 token
)

print(
    f"""
{prompt}
{response.choices[0].message.content}
{suffix}
"""
)
```

  </TabItem>

  <TabItem value="curl" label="curl" default>

```bash
curl --location 'https://api.mistral.ai/v1/fim/completions' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header "Authorization: Bearer $MISTRAL_API_KEY" \
--data '{
    "model": "codestral-latest",
    "prompt": "def f(",
    "suffix": "return a + b",
    "max_tokens": 64,
    "temperature": 0
}'
``` 
    </TabItem>
</Tabs>

#### Example 2: Completion
However, you can also use the model for pure code completion, by only providing a `prompt` and no `suffix`.
<Tabs groupId="code">
  <TabItem value="python" label="python" default>

```python

from mistralai import Mistral

api_key = os.environ["MISTRAL_API_KEY"]
client = Mistral(api_key=api_key)

model = "codestral-latest"
prompt = "def is_odd(n): \n return n % 2 == 1 \ndef test_is_odd():"

response = client.fim.complete(model=model, prompt=prompt, temperature=0)

print(
    f"""
{prompt}
{response.choices[0].message.content}
"""
)
```

  </TabItem>

  <TabItem value="curl" label="curl">

```bash
curl --location 'https://api.mistral.ai/v1/fim/completions' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header "Authorization: Bearer $MISTRAL_API_KEY" \
--data '{
    "model": "codestral-latest",
    "prompt": "def is_odd(n): \n return n % 2 == 1 \n def test_is_odd():", 
    "suffix": "",
    "max_tokens": 64,
    "temperature": 0
}'
``` 
    </TabItem>
</Tabs>

#### Example 3: Stop tokens
You can also use stop tokens to control the generation of the model when it generates specific strings.
:::tip[ ]
We recommend adding stop tokens for IDE autocomplete integrations to prevent the model from being too verbose.
:::

<Tabs groupId="code">
  <TabItem value="python" label="python" default>

```python

from mistralai import Mistral

api_key = os.environ["MISTRAL_API_KEY"]
client = Mistral(api_key=api_key)

model = "codestral-latest"
prompt = "def is_odd(n): \n return n % 2 == 1 \ndef test_is_odd():"
suffix = "n = int(input('Enter a number: '))\nprint(fibonacci(n))"

response = client.fim.complete(
    model=model, prompt=prompt, suffix=suffix, temperature=0, stop=["\n\n"]
)

print(
    f"""
{prompt}
{response.choices[0].message.content}
"""
)
```

  </TabItem>

  <TabItem value="curl" label="curl">

```bash
curl --location 'https://api.mistral.ai/v1/fim/completions' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header "Authorization: Bearer $MISTRAL_API_KEY" \
--data '{
    "model": "codestral-latest",
    "prompt": "def is_odd(n): \n return n % 2 == 1 \n def test_is_odd():", 
    "suffix": "test_is_odd()",
    "stop": ["\n\n"],
    "max_tokens": 64,
    "temperature": 0
}'
``` 
    </TabItem>
</Tabs>

## Instruct Following

We also provide the instruct chat endpoint of Codestral with the same model `codestral-latest`.  
The only difference is the endpoint used; so you can leverage powerfull code completion with instruct and chat use cases.

However we also provide `devstral-small-latest` and `devstral-medium-latest` for agentic tool use for software development, this family of models is specifically trained to navigate code bases and leverage tool usage for diverse tasks.

### Codestral

Here is an example of how to use the instruct endpoint of Codestral, it's perfect for specific **code generation** of specific snippets or **code completion** while **following instructions**; so you can better guide generation and exchange with a powerfull coding model.

<Tabs groupId="code">
  <TabItem value="python" label="python" default>

```python

from mistralai import Mistral

api_key = os.environ["MISTRAL_API_KEY"]
client = Mistral(api_key=api_key)

model = "codestral-latest"
message = [{"role": "user", "content": "Write a function for fibonacci"}]
chat_response = client.chat.complete(
    model = model,
    messages = message
)
```

  </TabItem>

  <TabItem value="curl" label="curl">

```bash
curl --location "https://api.mistral.ai/v1/chat/completions" \
     --header 'Content-Type: application/json' \
     --header 'Accept: application/json' \
     --header "Authorization: Bearer $MISTRAL_API_KEY" \
     --data '{
    "model": "codestral-latest",
    "messages": [{"role": "user", "content": "Write a function for fibonacci"}]
  }'
``` 
    </TabItem>
</Tabs>

### Devstral

While Codestral is designed for code generation and FIM, Devstral is a cutting-edge generative model that has been specifically designed and optimized for **agentic tool use for software development**, it can leverage function calling to navigate code bases and call the right tools to perform specific tasks for semi-automated software development.

<Tabs groupId="code">
  <TabItem value="python" label="python" default>

```python

from mistralai import Mistral

api_key = os.environ["MISTRAL_API_KEY"]
client = Mistral(api_key=api_key)

model = "devstral-medium-latest"
message = [{"role": "user", "content": "Create a new file called test.py and write a function for fibonacci"}]

tools = [
    {
        "type": "function",
        "function": {
            "name": "create_file",
            "description": "Create a new file with the given name and content",
            "parameters": {
                "type": "object",
                "properties": {
                    "filename": {
                        "type": "string",
                        "description": "The name of the file to create",
                    },
                    "content": {
                        "type": "string",
                        "description": "The content to write to the file",
                    },
                },
                "required": ["filename", "content"],
            },
        },
    }
]

chat_response = client.chat.complete(
    model = model,
    messages = message,
    tools = tools
)
```

  </TabItem>

  <TabItem value="curl" label="curl">

```bash
curl --location "https://api.mistral.ai/v1/chat/completions" \
     --header 'Content-Type: application/json' \
     --header 'Accept: application/json' \
     --header "Authorization: Bearer $MISTRAL_API_KEY" \
     --data '{
    "model": "devstral-medium-latest",
    "messages": [{"role": "user", "content": "Create a new file called test.py and write a function for fibonacci"}],
    "tools": [
        {
            "type": "function",
            "function": {
                "name": "create_file",
                "description": "Create a new file with the given name and content",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "filename": {
                            "type": "string",
                            "description": "The name of the file to create"
                        },
                        "content": {
                            "type": "string",
                            "description": "The content to write to the file"
                        }
                    },
                    "required": ["filename", "content"]
                }
            }
        }
    ]
  }'
``` 
    </TabItem>
</Tabs>

## Integrations

### Codestral Integrations

<details>
<summary><b>Integration with continue.dev</b></summary>

Continue.dev supports both Codestral base for code generation and Codestral Instruct for chat. 

<iframe width="560" height="315" width="100%" src="https://www.youtube.com/embed/mjltGOJMJZA?si=Tmf0kpPn3hVJ0CaM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

#### How to set up Codestral with Continue

**Here is a step-by-step guide on how to set up Codestral with Continue using the Mistral AI API:**

1. Install the Continue VS Code or JetBrains extension following the instructions [here](https://docs.continue.dev/quickstart). 
Please make sure you install Continue version >v0.8.33.

2. Automatic set up:

- Click on the Continue extension iron on the left menu. Select `Mistral API` as a provider, select `Codestral` as a model. 
- Click "Get API Key" to get Codestral API key. 
- Click "Add model", which will automatically populate the config.json. 

<img src="/img/guides/codestral1.png" alt="drawing" width="300"/>

2. (alternative) Manually edit config.json 
- Click on the gear icon in the bottom right corner of the Continue window to open `~/.continue/config.json` (MacOS) /  `%userprofile%\.continue\config.json` (Windows)
- Log in and request a Codestral API key on Mistral AI's La Plateforme [here](https://console.mistral.ai/codestral)
- To use Codestral as your model for both `autocomplete` and `chat`, replace  `[API_KEY]` with your Mistral API key below and add it to your `config.json` file:

```json title="~/.continue/config.json"
{
  "models": [
    {
      "title": "Codestral",
      "provider": "mistral",
      "model": "codestral-latest",
      "apiKey": "[API_KEY]"
    }
  ],
  "tabAutocompleteModel": {
    "title": "Codestral",
    "provider": "mistral",
    "model": "codestral-latest",
    "apiKey": "[API_KEY]"
  }
}
```

If you run into any issues or have any questions, please join our Discord and post in `#help` channel [here](https://discord.gg/EfJEfdFnDQ)
</details>

<details>
<summary><b>Integration with Tabnine</b></summary>

Tabnine supports Codestral Instruct for chat. 

<iframe width="560" height="315" width="100%" src="https://www.youtube.com/embed/pFa4NLK9Lbw?si=7tsfFUsOyllkwl-M" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

#### How to set up Codestral with Tabnine

##### What is Tabnine Chat? 
Tabnine Chat is a code-centric chat application that runs in the IDE and allows developers
 to interact with Tabnine’s AI models in a flexible, free-form way, using natural language. 
Tabnine Chat also supports dedicated quick actions that use predefined prompts optimized
 for specific use cases.

##### Getting started
To start using Tabnine Chat, first [launch](https://docs.tabnine.com/main/getting-started/getting-the-most-from-tabnine-chat/launch) it in your IDE (VSCode, JetBrains, or Eclipse). 
Then, learn how to [interact](https://docs.tabnine.com/main/getting-started/getting-the-most-from-tabnine-chat/interact) with Tabnine Chat, for example, how to ask questions or give 
instructions. Once you receive your response, you can [read, review, and apply](https://docs.tabnine.com/main/getting-started/getting-the-most-from-tabnine-chat/consume) it within 
your code.

##### Selecting Codestral as Tabnine Chat App model

In the Tabnine Chat App, use the [model selector](https://docs.tabnine.com/main/getting-started/getting-the-most-from-tabnine-chat/switching-between-chat-ai-models) to choose *Codestral*.

</details>

<details>
<summary><b>Integration with LangChain</b></summary>

LangChain provides support for Codestral Instruct. Here is how you can use it in LangChain: 

```py
# Tokenize a list of messages
tokenized = tokenizer.encode_chat_completion(
    ChatCompletionRequest(
        tools=[
            Tool(
                function=Function(
                    name="get_current_weather",
                    description="Get the current weather",
                    parameters={
                        "type": "object",
                        "properties": {
                            "location": {
                                "type": "string",
                                "description": "The city and state, e.g. San Francisco, CA",
                            },
                            "format": {
                                "type": "string",
                                "enum": ["celsius", "fahrenheit"],
                                "description": "The temperature unit to use. Infer this from the users location.",
                            },
                        },
                        "required": ["location", "format"],
                    },
                )
            )
        ],
        messages=[
            UserMessage(content="What's the weather like today in Paris"),
        ],
        model=model_name,
    )
)
tokens, text = tokenized.tokens, tokenized.text

```

Here is the output of “text”, which is a debug representation for you to inspect.

```
<s>[AVAILABLE_TOOLS][{"type": "function", "function": {"name": "get_current_weather", "description": "Get the current weather", "parameters": {"type": "object", "properties": {"location": {"type": "string", "description": "The city and state, e.g. San Francisco, CA"}, "format": {"type": "string", "enum": ["celsius", "fahrenheit"], "description": "The temperature unit to use. Infer this from the users location."}}, "required": ["location", "format"]}}}][/AVAILABLE_TOOLS][INST]What's the weather like today in Paris[/INST]
```

To count the number of tokens, run `len(tokens)` and we get 128 tokens.

## v3 tokenizer 

Our v3 tokenizer uses the Byte-Pair Encoding (BPE) with SentencePiece, which is an open-source tokenization library to build our tokenization vocabulary.

In BPE, the tokenization process starts by treating each byte in a text as a separate token. 
Then, it iteratively adds new tokens to the vocabulary for the most frequent pair of tokens currently appearing in the corpus. For example, if the most frequent pair of tokens is "th" + "e", then a new token "the" will be created and occurrences of "th"+"e" will be replaced with the new token "the". This process continues until no more replacements can be made.

### Our tokenization vocabulary
Our tokenization vocabulary is released in the https://github.com/mistralai/mistral-common/tree/main/tests/data folder. Let’s take a look at the vocabulary of our v3 tokenizer. 

#### Vocabulary size
Our vocabulary consists of 32k vocab + 768 control tokens. The 32k vocab includes 256 bytes and 31,744 characters and merged characters. 

#### Control tokens 
Our vocabulary starts with 10 control tokens, which are special tokens we use in the encoding process to represent specific instructions or indicators:

```
<unk>
<s>
</s>
[INST]
[/INST]
[TOOL_CALLS]
[AVAILABLE_TOOLS]
[/AVAILABLE_TOOLS]
[TOOL_RESULTS]
[/TOOL_RESULTS]
```

#### Bytes
After the control token slots, we have 256 bytes in the vocabulary. A byte is a unit of digital information that consists of 8 bits. Each bit can represent one of two values, either 0 or 1. A byte can therefore represent 256 different values.

```
<0x00>
<0x01>
...
```

Any character, regardless of the language or symbol, can be represented by a sequence of one or more bytes. When a word is not present in the vocabulary, it can still be represented by the bytes that correspond to its individual characters. This is important for handling unknown words and characters. 

#### Characters and merged characters
And finally, we have the characters and merged characters in the vocabulary. The order of the tokens are determined by the frequency of these tokens in the data that was used to train the model, with the most frequent ones in the beginning of the vocabulary. For example, two spaces “▁”, four spaces “▁▁▁▁”, “_t”, “in”, and “er” were found to be the most common tokens we trained on. As we move further down the vocabulary list, the tokens become less frequent. Towards the end of the vocabulary file, you might find less common characters such as Chinese and Korean characters. These characters are less frequent because they were encountered less often in the training data, not because they are less used in general. 

```
▁▁
▁▁▁▁
▁t
in
er
...
벨
ゼ
梦
```

### Run our tokenizer in Python 

To get started, let’s first install our tokenizer via `pip install mistral-common`.  

Once the tokenizer is installed, in a Python environment, we can import the needed modules from `mistral_common`.
```python
from mistral_common.protocol.instruct.messages import (
    AssistantMessage,
    UserMessage,
    ToolMessage
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer
from mistral_common.protocol.instruct.tool_calls import Function, Tool, ToolCall, FunctionCall
from mistral_common.protocol.instruct.request import ChatCompletionRequest
```

We load our tokenizer with `MistralTokenizer` and specify which version of tokenizer we’d like to load. 
```
tokenizer_v3 = MistralTokenizer.v3()
```

Let’s tokenize a series of conversation with different types of messages

```python
tokenized = tokenizer_v3.encode_chat_completion(
    ChatCompletionRequest(
        tools=[
            Tool(
                function=Function(
                    name="get_current_weather",
                    description="Get the current weather",
                    parameters={
                        "type": "object",
                        "properties": {
                            "location": {
                                "type": "string",
                                "description": "The city and state, e.g. San Francisco, CA",
                            },
                            "format": {
                                "type": "string",
                                "enum": ["celsius", "fahrenheit"],
                                "description": "The temperature unit to use. Infer this from the users location.",
                            },
                        },
                        "required": ["location", "format"],
                    },
                )
            )
        ],
        messages=[
            UserMessage(content="What's the weather like today in Paris"),
            AssistantMessage(
                content=None,
                tool_calls=[
                    ToolCall(
                        id="VvvODy9mT",
                        function=FunctionCall(
                            name="get_current_weather",
                            arguments='{"location": "Paris, France", "format": "celsius"}',
                        ),
                    )
                ],
            ),
            ToolMessage(
                tool_call_id="VvvODy9mT", name="get_current_weather", content="22"
            ),
            AssistantMessage(
                content="The current temperature in Paris, France is 22 degrees Celsius.",
            ),
            UserMessage(content="What's the weather like today in San Francisco"),
            AssistantMessage(
                content=None,
                tool_calls=[
                    ToolCall(
                        id="fAnpW3TEV",
                        function=FunctionCall(
                            name="get_current_weather",
                            arguments='{"location": "San Francisco", "format": "celsius"}',
                        ),
                    )
                ],
            ),
            ToolMessage(
                tool_call_id="fAnpW3TEV", name="get_current_weather", content="20"
            ),
        ],
        model="test",
    )
)

tokens, text = tokenized.tokens, tokenized.text
```

Here is the output of “text”, which is a debug representation for you to inspect. 
```
'<s>[INST] What\'s the weather like today in Paris[/INST][TOOL_CALLS] [{"name": "get_current_weather", "arguments": {"location": "Paris, France", "format": "celsius"}, "id": "VvvODy9mT"}]</s>[TOOL_RESULTS] {"call_id": "VvvODy9mT", "content": 22}[/TOOL_RESULTS] The current temperature in Paris, France is 22 degrees Celsius.</s>[AVAILABLE_TOOLS] [{"type": "function", "function": {"name": "get_current_weather", "description": "Get the current weather", "parameters": {"type": "object", "properties": {"location": {"type": "string", "description": "The city and state, e.g. San Francisco, CA"}, "format": {"type": "string", "enum": ["celsius", "fahrenheit"], "description": "The temperature unit to use. Infer this from the users location."}}, "required": ["location", "format"]}}}][/AVAILABLE_TOOLS][INST] What\'s the weather like today in San Francisco[/INST][TOOL_CALLS] [{"name": "get_current_weather", "arguments": {"location": "San Francisco", "format": "celsius"}, "id": "fAnpW3TEV"}]</s>[TOOL_RESULTS] {"call_id": "fAnpW3TEV", "content": 20}[/TOOL_RESULTS]'
```
To count the number of tokens, run `len(tokens)` and we get 302 tokens. 

## Use cases
### NLP tasks

As we mentioned earlier, tokenization is a crucial first step in natural language processing (NLP) tasks. Once we have tokenized our text, we can use those tokens to create text embeddings, which are dense vector representations of the text. These embeddings can then be used for a variety of NLP tasks, such as text classification, sentiment analysis, and machine translation.

Mistral's embedding API simplifies this process by combining the tokenization and embedding steps into one. With this API, we can easily create text embeddings for a given text, without having to separately tokenize the text and create embeddings from the tokens.

If you're interested in learning more about how to use Mistral's embedding API, be sure to check out our [embedding guide](/capabilities/embeddings/overview), which provides detailed instructions and examples.

### Tokens count

Mistral AI's LLM API endpoints charge based on the number of tokens in the input text. 

To help you estimate your costs, our tokenization API makes it easy to count the number of tokens in your text. Simply run `len(tokens)` as shown in the example above to get the total number of tokens in the text, which you can then use to estimate your cost based on our pricing information.


[Mistral AI Crawlers]
Source: https://docs.mistral.ai/docs/robots

## Mistral AI Crawlers

Mistral AI employs web crawlers ("robots") and user agents to execute tasks for its products, either automatically or upon user request. To facilitate webmasters in managing how their sites and content interact with AI, Mistral AI utilizes specific robots.txt tags.

### MistralAI-User

MistralAI-User is for user actions in LeChat. When users ask LeChat a question, it may visit a web page to help answer and include a link to the source in its response. MistralAI-User governs which sites these user requests can be made to. It is not used for crawling the web in any automatic fashion, nor to crawl content for generative AI training.

Full user-agent string: Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; MistralAI-User/1.0; +https://docs.mistral.ai/robots)

Published IP addresses: https://mistral.ai/mistralai-user-ips.json
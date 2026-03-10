# Presence/Frequency Penalty

## Presence Penalty

**Presence Penalty** determines how much the model penalizes the repetition of words or phrases. It encourages the model to use a wider variety of words and phrases, making the output more diverse and creative.

- **Range**: [-2, 2]
- **Default**: 0

A higher presence penalty encourages the model to avoid repeating words or phrases that have already appeared in the output, ensuring a more varied and creative text.

The presence penalty specifically is a **one-time adjustment** applied to all tokens that have been used at least once. It reduces the likelihood of repeating any token that has already appeared. This encourages the model to use a diverse range of tokens, promoting creativity and variety in the output.

## Frequency Penalty

**Frequency Penalty** is a parameter that penalizes the repetition of words based on their frequency in the generated text. It helps to promote diversity and reduce repetition in the output.

- **Range**: [-2, 2]
- **Default**: 0

A higher frequency penalty discourages the model from repeating words that have already appeared frequently in the output. This ensures that the generated text is more varied and less repetitive.

The frequency penalty specifically is a value that increases with the frequency of a token's appearance in the generated text, **an accumulative penalty**, the more the token is sampled the higher the penalty. It reduces the likelihood of repeating any token that has already appeared frequently. This ensures that the generated text is more varied and less repetitive.

### Differences Between Presence Penalty and Frequency Penalty

- **Presence Penalty**: This is a one-off additive contribution that applies to all tokens that have been sampled at least once. It encourages the model to include a diverse range of tokens in the generated text.
- **Frequency Penalty**: This is a contribution that is proportional to how often a particular token has already been sampled. It discourages the model from repeating the same words or phrases too frequently within the generated text.

Both parameters can be tweaked to shape the quality and diversity of the generated text. The best values for these parameters can differ based on the specific task and the desired outcome.

<Tabs>
  <TabItem value="no-penalty" label="No Penalty" default>

### Example Without Presence Penalty

Here's an example of how the output looks without the `Presence Penalty` parameter:

```py

from mistralai import Mistral

api_key = os.environ["MISTRAL_API_KEY"]
model = "ministral-3b-latest"

client = Mistral(api_key=api_key)

chat_response = client.chat.complete(
    model=model,
    messages=[
        {"role": "user",
        "content": "List 10 possible titles for a fantasy book. Give a list only."}
        ],
    temperature=0
)

print(chat_response.choices[0].message.content)
```

### Output Without Presence Penalty

```
1. "The Shattered Crown"
2. "Whispers of the Old Magic"
3. "Echoes of the Forgotten Realm"
4. "The Chronicles of the Silver Moon"
5. "The Enchanted Forest's Secret"
6. "The Last Dragon's Legacy"
7. "The Shadowed Path"
8. "The Song of the Siren's Call"
9. "The Lost City of the Stars"
10. "The Whispering Winds of Destiny"
```
</TabItem>
  <TabItem value="presence-penalty" label="Presence Penalty" default>

### Example With Presence Penalty

Here's an example of how to use the `Presence Penalty` parameter in the API:

```py

from mistralai import Mistral

api_key = os.environ["MISTRAL_API_KEY"]
model = "ministral-3b-latest"

client = Mistral(api_key=api_key)

chat_response = client.chat.complete(
    model=model,
    messages=[
        {"role": "user",
        "content": "List 10 possible titles for a fantasy book. Give a list only."}
        ],
    temperature=0,
    presence_penalty=2
)

print(chat_response.choices[0].message.content)
```

### Output With Presence Penalty

```
1. "The Shattered Crown"
2. "Whispers of the Old Magic"
3. "Echoes of Eternity"
4. "Shadows of the Forgotten Realm"
5. "Chronicles of the Enchanted Forest"
6. "The Last Dragon's Roar"
7. "Mysteries of the Hidden City"
8. "Legends of the Lost Kingdom"
9. "The Whispering Winds"
10. "The Unseen War"
```

> The output list is already slightly different than the first one, being impacted by the presence penalty of present tokens. For instance we have less `The` as a token compared to without presence penalty.

</TabItem>

<TabItem value="frequency-penalty" label="Frequency Penalty">

### Example With Frequency Penalty

Here's an example of how to use the `Frequency Penalty` parameter in the API:

```py

from mistralai import Mistral

api_key = os.environ["MISTRAL_API_KEY"]
model = "ministral-3b-latest"

client = Mistral(api_key=api_key)

chat_response = client.chat.complete(
    model=model,
    messages=[
        {"role": "user",
        "content": "List 10 possible titles for a fantasy book. Give a list only."}
        ],
    temperature=0,
    frequency_penalty=2
)

print(chat_response.choices[0].message.content)
```

### Output With Frequency Penalty

```
1. "The Shattered Crown"
2. "Whispers of the Old Magic"
3. "Echoes of Eternity"
4. "The Forgotten Realm"
5. "Shadows of the Lost City"
6. "Chronicles of the Enchanted Forest"
7. The Last Dragon's Roar
8."The Veil Between Worlds"
9."The Song of the Siren's Call"
10."Legends in Stone"
```

> The output is already more diverse than previously, however notice that after the 7th value of the list tokens such as `_"` and single quotation marks start to also be heavily affected, this shows how stronger the impact of frequency penalty is in the long term as an accumulative penalty.

</TabItem>
</Tabs>

**Penalties are a sensible parameter that can have a significant impact on long context and long output queries. They can also help avoid highly repetitive loops that the model may otherwise fall into, making them a valuable parameter.**

</details>


[Tokenization]
Source: https://docs.mistral.ai/docs/guides/tokenization

<a target="_blank" href="https://colab.research.google.com/github/mistralai/mistral-common/blob/main/examples/tokenizer.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

Tokenization is a fundamental step in LLMs. It is the process of breaking down text into smaller subword units, known as tokens. We recently open-sourced our tokenizer at Mistral AI. This guide will walk you through the fundamentals of tokenization, details about our open-source tokenizers, and how to use our tokenizers in Python.  

## What is tokenization? 

Tokenization is the first step and the last step of text processing and modeling. Texts need to be represented as numbers in our models so that our model can understand. Tokenization breaks down text into tokens, and each token is assigned a numerical representation, or index, which can be used to feed into a model. In a typical LLM workflow: 
- We first encode the input text into tokens using a tokenizer. Each unique token is assigned a specific index number in the tokenizer’s vocabulary. 
- Once the text is tokenized, these tokens are passed through the model, which typically includes an embedding layer and transformer blocks. The embedding layer converts the tokens into dense vectors that capture semantic meanings. Check out our [embedding guide](/capabilities/embeddings/overview) for details. The transformer blocks then process these embedding vectors to understand the context and generate results. 
- The last step is decoding, which detokenize output tokens back to human-readable text. This is done by mapping the tokens back to their corresponding words using the tokenizer’s vocabulary. 

<img src="/img/guides/tokenization1.png" alt="drawing" width="600"/>

Most people only tokenize text. 
Our first release contains tokenization. 
Our tokenizers go beyond the usual text \<-\> tokens, 
adding parsing of tools and structured conversation. 
We also release the validation and normalization code that is used in our API.
Specifically, we use control tokens, which are special tokens to indicate different types of elements. 
These tokens are not treated as strings and are added directly to the code. 
Note that we are still iterating on the tokenizer. Things may change and this is the current state of things. 

We have released three versions of our tokenizers powering different sets of models. 

- v1: `mistral-embed`, `open-mixtral-8x7b`
- v2: `mistral-small-2402` (deprecated), `mistral-large-2402`
- v3: `open-mixtral-8x22b`, `mistral-large-latest`, `mistral-small-latest`, `open-mistral-7b`
- v3 (tekken): `open-mistral-nemo`, `ministral-8b-latest`

This guide will focus on our latest v3 (tekken) tokenizer and v3 tokenizer. 


## v3 (tekken) tokenizer

There are several tokenization methods used in Natural Language Processing (NLP) to convert raw text into tokens such as word-level tokenization, character-level tokenization, and subword-level tokenization including the Byte-Pair Encoding (BPE). 
Our newest tokenizer, tekken, uses the Byte-Pair Encoding (BPE) with [Tiktoken](https://github.com/openai/tiktoken).


Tekken was trained on more than 100 languages and compresses natural language text and 
source code more efficiently than the SentencePiece tokeniser used in previous Mistral models. 
In particular, it is ~30% more efficient at compressing source code in Chinese, Italian, 
French, German, Spanish, and Russian.  It is also 2x and 3x more efficient at compressing 
Korean and Arabic, respectively. Compared to the Llama 3 tokeniser, 
Tekken proved more proficient in compressing text for approximately 85% of all languages.

<img src="/img/guides/tokenization3.png" alt="drawing" width="600"/>


### Our tokenization vocabulary
Our tokenization vocabulary is released in the https://github.com/mistralai/mistral-common/tree/main/tests/data folder. Let’s take a look at the vocabulary of our v3 tekken tokenizer. 

#### Vocabulary size
Our vocabulary consists of 130k vocab + 1k control tokens.  

#### Control tokens 
Our vocabulary starts with 14 control tokens, which are special tokens we use in the encoding process to represent specific instructions or indicators:

```
<unk>
<s>
</s>
[INST]
[/INST]
[AVAILABLE_TOOLS]
[/AVAILABLE_TOOLS]
[TOOL_RESULTS]
[/TOOL_RESULTS]
[TOOL_CALLS]
<pad>
[PREFIX]
[MIDDLE]
[SUFFIX]
```

The tokenizer does not encode control tokens, which help prevent a situation known as prompt injection. For  example, the control token “[INST]” is used to denote user message:
- Without the control tokens, the tokenizer treats “[INST]” as a regular string and encodes the entire sequence “[INST] I love Paris [/INST]”.  This could potentially allow users to include "[INST]" and "[/INST]" tags within their message, causing confusion for the model as it might interpret part of the user's message as an assistant's message.
- With the control tokens, the tokenizer instead concatenates the control tokens with the encoded message: [INST] + encode(“I love Paris”) + [/INST]. This ensures that only the user's message gets encoded, and the encoded messages are guaranteed to have the correct [INST] and [/INST] tags. 

You may have noticed that we have 1000 slots for control tokens. The remaining 1000-14=986 slots for control tokens are actually empty for us to add more control tokens in the future and also ensure our vocabulary size is 131k (2\^17). Computers like powers of 2s! 

#### Bytes, characters, and merged characters

Below are two examples of the vocab. token_str is null when the byte sequence doesn't decode into a full unicode character, e.g., raw bytes.
```
{
    "rank": 0,
    "token_bytes": "AA==",
    "token_str": "\u0000"
},
...
{
    "rank": 7613,
    "token_bytes": "IO2D",
    "token_str": null
},
```

### Run our tokenizer in Python 
To get started, let’s first install our tokenizer and tiktoken via `pip install mistral-common tiktoken`.  

Once the tokenizer is installed, in a Python environment, we can import the needed modules from `mistral_common`.

```py
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer
```

We then can load our tokenizer. 
```py
tokenizer = MistralTokenizer.v3(is_tekken=True)
model_name = "nemostral"
tokenizer = MistralTokenizer.from_model(model_name)
```

Let’s tokenize a series of conversation with different types of messages.
```py
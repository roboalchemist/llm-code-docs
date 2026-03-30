# Source: https://novita.ai/docs/guides/llm-api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Large Language Models

## Model Capabilities

Large Language Models (LLMs) are types of AI model built using deep learning and natural language processing techniques. After being trained on massive amounts of text data, they can understand, generate, and process human language. LLMs have the following main capabilities:

* **Text Generation**

  LLMs can generate logically coherent content based on context and adjust output style as needed.
* **Language Understanding**

  LLMs can accurately understand the meaning of input text and support context-aware conversation.
* **Text Translation**

  LLMs are capable of cross-lingual understanding and generation, enabling translation between different languages.
* **Knowledge-based Q\&A**

  With extensive knowledge basis, LLMs can answer questions across domains such as culture, science, and history.
* **Code Understanding & Generation**

  LLMs can understand and generate code (Python, Java, C++ and so on), detect code errors, and offer suggestions.
* **Text Classification & Summarization**

  LLMs can understand complex sentences, categorize and extract information, and summarize key points.

## Model Selection

On the [LLM Service Page](https://novita.ai/models), you can browse the list of supported models, learn model basics and pricing. Click on a specific model, and you can open its detail page for an online demo. After trying different models with your task, you can compare and choose the most suitable one.

## API Integration

Novita AI provides fast, reliable APIs for open-source models, combining the ease and reliability of top-tier LLM APIs with the flexibility and cost-efficiency of open source LLMs.

* [ChatCompletion](https://platform.openai.com/docs/guides/text-generation/chat-completions-api): Supports both streaming and non-streaming modes.
* [Completion](https://platform.openai.com/docs/guides/text-generation/completions-api): Also supports streaming and non-streaming modes.

If you're already using OpenAI's `ChatCompletion` or `Completion` API, simply set your base URL to: api.novita.ai/openai , get and set your API key, update the model name as needed to start using LLM services.

<Tip>
  For how to get API key, refer to the [API Key Management](/api-reference/basic-authentication).
</Tip>

## Code Examples

### Python

<CodeGroup>
  ```python ChatCompletion theme={"system"}
  from openai import OpenAI

  client = OpenAI(
      base_url="https://api.novita.ai/openai",
      api_key="<Your API Key>",
  )

  model = "deepseek/deepseek-r1"
  stream = True  # or False
  max_tokens = 512

  chat_completion_res = client.chat.completions.create(
      model=model,
      messages=[
          {
              "role": "system",
              "content": "you are a professional AI helper.",
          },
          {
              "role": "user",
              "content": "Where can the example of GPU provided by novita ai be adapted?",
          }
      ],
      stream=stream,
      max_tokens=max_tokens,
  )

  if stream:
      for chunk in chat_completion_res:
          print(chunk.choices[0].delta.content or "", end="")
  else:
      print(chat_completion_res.choices[0].message.content)
  ```

  ```python Completion theme={"system"}
  from openai import OpenAI

  client = OpenAI(
      base_url="https://api.novita.ai/openai",
      api_key="<Your API Key>",
  )

  model = "deepseek/deepseek-r1"
  stream = True  # or False
  max_tokens = 512

  completion_res = client.completions.create(
      model=model,
      prompt="Where can the example of GPU provided by novita ai be adapted?",
      stream=stream,
      max_tokens=max_tokens,
  )

  if stream:
      for chunk in completion_res:
          print(chunk.choices[0].text or "", end="")
  else:
      print(completion_res.choices[0].text)
  ```
</CodeGroup>

### Curl

<CodeGroup>
  ```bash ChatCompletion theme={"system"}
  export API_KEY="<Your API Key>"

  curl "https://api.novita.ai/openai/v1/chat/completions" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer ${API_KEY}" \
    -d '{
      "model": "deepseek/deepseek-r1",
      "messages": [
          {
              "role": "system",
              "content": "you are a professional AI helper."
          },
         {
              "role": "user",
              "content": "Where can the example of GPU provided by novita ai be adapted?"
          }
      ],
      "max_tokens": 512
  }'
  ```

  ```bash Completion theme={"system"}
  export API_KEY="<Your API Key>"

  curl "https://api.novita.ai/openai/v1/completions" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer ${API_KEY}" \
    -d '{
      "model": "deepseek/deepseek-r1",
      "prompt": "Where can the example of GPU provided by novita ai be adapted?",
      "max_tokens": 512
  }'
  ```
</CodeGroup>

## Key Parameters

### Base Parameters

`model`: The target LLM. See the full list on the [LLM Service Page](https://novita.ai/models).

### Messages

> ChatCompletion Only

`messages`: Inputs and outputs when interacting with LLM. Each message belongs to one character. Messages can help you get better outputs, you can try different methods to get better results.

* `content`: message content.
* `role`: Define the speaker:
  * `system`: Set the AI's role, telling model its role or behavior.
  * `user`: The user's input.
  * `assistant`: The AI's response. Users can give examples of output in advance, telling model how to answer current request.
* `name` (optional): separating message writers with same role.

### Prompt

> ChatCompletion Only

`prompt`: Instruction text for generating a completion written by user to LLM to tell the model their task clearly.

### Output Control

Different combination of parameters can help the model to generate more satisfying content.

**Diversity of Text**

> 'temperature' and 'top\_p' can control the diversity of generated text, we advice you to set only one of them. The bigger the value you set, The more diverse the text will be.  The smaller the value you set, The more accurate the text will be.

* `temperature`: Controls randomness. Higher = more creative.
* `top_p`: Nucleus sampling. Controls cumulative probability.
* `top_k`: Limits candidate token count.

**Repetition Penalties**

* `presence_penalty`: Controls repeated tokens of the texts. If one token has already existed in the text, penalty will come, this results in more token in the text.
* `frequency_penalty`: Control token frequency of the texts. Every time the same token exist in the text, penalty will come, which results in less same token in the future in the text.
* `repetition_penalty`: Penalizes or encourages repetition.

### Output Limits

* `max_tokens`: Max tokens in one response. Content after this value in the text will be truncated.
* `stream`: Whether to use streaming. For those with long outputs, we advice you to use streaming mode to prevent timeout error:
  * `true`: Streamed, partial results as they are generated.
  * `false`: Full result after processing.
* `stop`: Strings that will terminate generation when encountered.


Built with [Mintlify](https://mintlify.com).
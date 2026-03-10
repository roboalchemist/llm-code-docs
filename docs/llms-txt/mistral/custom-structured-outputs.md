# Custom Structured Outputs

Custom Structured Outputs allow you to ensure the model provides an answer in a very specific JSON format by supplying a clear JSON schema. This approach allows the model to consistently deliver responses with the correct typing and keywords.

<Tabs>
  <TabItem value="python" label="python" default>

Here is an example of how to achieve this using the Mistral AI client and Pydantic:

### Define the Data Model

First, define the structure of the output using a Pydantic model:

```python
from pydantic import BaseModel

class Book(BaseModel):
    name: str
    authors: list[str]
```

### Start the completion

Next, use the Mistral AI python client to make a request and ensure the response adheres to the defined structure using `response_format` set to the corresponding pydantic model:

```python

from mistralai import Mistral

api_key = os.environ["MISTRAL_API_KEY"]
model = "ministral-8b-latest"

client = Mistral(api_key=api_key)

chat_response = client.chat.parse(
    model=model,
    messages=[
        {
            "role": "system", 
            "content": "Extract the books information."
        },
        {
            "role": "user", 
            "content": "I recently read 'To Kill a Mockingbird' by Harper Lee."
        },
    ],
    response_format=Book,
    max_tokens=256,
    temperature=0
)
```

In this example, the `Book` class defines the structure of the output, ensuring that the model's response adheres to the specified format.

There are two types of possible outputs that are easily accessible via our SDK:

1. The raw JSON output, accessed with `chat_response.choices[0].message.content`:
```json
{
  "authors": ["Harper Lee"],
  "name": "To Kill a Mockingbird"
}
```

2. The parsed output, converted into a Pydantic object with `chat_response.choices[0].message.parsed`. In this case, it is a `Book` instance:
```python
name='To Kill a Mockingbird' authors=['Harper Lee']
```

  </TabItem>

  <TabItem value="typescript" label="typescript">

Here is an example of how to achieve this using the Mistral AI client and Zod:

### Define the Data Model

First, define the structure of the output using Zod:

```typescript


const Book = z.object({
  name: z.string(),
  authors: z.array(z.string()),
});
```

### Start the completion

Next, use the Mistral AI TypeScript client to make a request and ensure the response adheres to the defined structure using `responseFormat` set to the corresponding Zod schema:

```typescript


const apiKey = process.env.MISTRAL_API_KEY;

const client = new Mistral({apiKey: apiKey});

const chatResponse = await client.chat.parse({
  model: "ministral-8b-latest",
  messages: [
    {
      role: "system",
      content: "Extract the books information.",
    },
    {
      role: "user",
      content: "I recently read 'To Kill a Mockingbird' by Harper Lee.",
    },
  ],
  responseFormat: Book,
  maxTokens: 256,
  temperature: 0,
});
```

In this example, the `Book` schema defines the structure of the output, ensuring that the model's response adheres to the specified format.

There are two types of possible outputs that are easily accessible via our SDK:

1. The raw JSON output, accessed with `chatResponse.choices[0].message.content`:
```json
{
  "authors": ["Harper Lee"],
  "name": "To Kill a Mockingbird"
}
```

2. The parsed output, converted into a TypeScript object with `chatResponse.choices[0].message.parsed`. In this case, it is a `Book` object:
```typescript
{ name: 'To Kill a Mockingbird', authors: [ 'Harper Lee' ] }
```

  </TabItem>
  <TabItem value="curl" label="curl">

The request is structured to ensure that the response adheres to the specified custom JSON schema. The `schema` defines the structure of a Book object with name and authors properties.

```bash
curl --location "https://api.mistral.ai/v1/chat/completions" \
     --header 'Content-Type: application/json' \
     --header 'Accept: application/json' \
     --header "Authorization: Bearer $MISTRAL_API_KEY" \
     --data '{
    "model": "ministral-8b-latest",
    "messages": [
     {
        "role": "system",
        "content": "Extract the books information."
      },
     {
        "role": "user",
        "content": "I recently read To Kill a Mockingbird by Harper Lee."
      }
    ],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "schema": {
          "properties": {
            "name": {
              "title": "Name",
              "type": "string"
            },
            "authors": {
              "items": {
                "type": "string"
              },
              "title": "Authors",
              "type": "array"
            }
          },
          "required": ["name", "authors"],
          "title": "Book",
          "type": "object",
          "additionalProperties": false
        },
        "name": "book",
        "strict": true
      }
    },
    "max_tokens": 256,
    "temperature": 0
  }'
```
  </TabItem>
</Tabs>

:::note
To better guide the model, the following is being always prepended by default to the System Prompt when using this method:
```
Your output should be an instance of a JSON object following this schema: {{ json_schema }}
```

However, it is recommended to add more explanations and iterate on your system prompt to better clarify the expected schema and behavior.
:::

### FAQ
**Q: Which models support custom Structured Outputs?**  
**A:** All currently available models except for `codestral-mamba` are supported.


[JSON mode]
Source: https://docs.mistral.ai/docs/capabilities/structured-output/json-mode

Users have the option to set `response_format` to `{"type": "json_object"}` to enable JSON mode.
Currently, JSON mode is available for all of our models through API. 

<Tabs>
  <TabItem value="python" label="python" default>

```python

from mistralai import Mistral

api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-large-latest"

client = Mistral(api_key=api_key)
messages = [
    {
        "role": "user",
        "content": "What is the best French meal? Return the name and the ingredients in short JSON object.",
    }
]
chat_response = client.chat.complete(
      model = model,
      messages = messages,
      response_format = {
          "type": "json_object",
      }
)

print(chat_response.choices[0].message.content)


```
Example output: 
```
{"name": "Coq au Vin", "ingredients": ["chicken", "red wine", "bacon", "mushrooms", "onions", "garlic", "chicken broth", "thyme", "bay leaf", "flour", "butter", "olive oil", "salt", "pepper"]}
```


  </TabItem>
  <TabItem value="typescript" label="typescript">
```typescript


const apiKey = process.env.MISTRAL_API_KEY;

const mistral = new Mistral({apiKey: apiKey});

const chatResponse = await mistral.chat.complete({
    model: "mistral-large-latest",
    messages: [{role: 'user', content: 'What is the best French meal? Return the name and the ingredients in JSON format.'}],
    responseFormat: {type: 'json_object'},
    }
);

console.log('JSON:', chatResponse.choices[0].message.content)
```
  </TabItem>
  <TabItem value="curl" label="curl">
```bash
curl --location "https://api.mistral.ai/v1/chat/completions" \
     --header 'Content-Type: application/json' \
     --header 'Accept: application/json' \
     --header "Authorization: Bearer $MISTRAL_API_KEY" \
     --data '{
    "model": "mistral-large-latest",
    "messages": [
     {
        "role": "user",
        "content": "What is the best French cheese? Return the product and produce location in JSON format"
      }
    ],
    "response_format": {"type": "json_object"}
  }'
```
  </TabItem>
</Tabs>


[Structured Output]
Source: https://docs.mistral.ai/docs/capabilities/structured-output/overview
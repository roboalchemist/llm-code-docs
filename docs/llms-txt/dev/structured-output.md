# Source: https://dev.writer.com/home/structured-output.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Receive structured outputs

## Overview

The [`chat` endpoint](/api-reference/completion-api/chat-completion) supports structured outputs for chat completions with `palmyra-x5` and `palmyra-x4` models.

Structured outputs allow you to specify the response schema that the model should follow.

You can use structured outputs in one of two ways:

1. [Pass in a `json_schema` object](/home/structured-output#sample-request-and-response) in the `response_format` parameter when making a request to the `chat` endpoint.
2. [Use the `parse` method](/home/structured-output#sdk-parse-methods) in the Python and JavaScript SDKs and pass in a [`Pydantic`](https://docs.pydantic.dev/) or [`Zod`](https://zod.dev/) object.

## Sample request and response

The sample request and response below shows how to use structured outputs with the `chat` endpoint and the `response_format` parameter.

The `json_schema` object must be in [JSON Schema format](https://json-schema.org/understanding-json-schema/).

To guarantee that the model includes all the fields in the response, include the [`required` field](https://json-schema.org/understanding-json-schema/reference/object.html#required) in the `json_schema` object.

<CodeGroup>
  ```bash cURL theme={null}
  curl -X POST https://api.writer.com/v1/chat \
    --header "Content-Type: application/json" \
    --header "Authorization: Bearer $WRITER_API_KEY" \
    --data '{
      "model": "palmyra-x5",
      "messages": [
        { "role": "system", "content": "You are a helpful cooking assistant." },
        { "role": "user", "content": "Give me a recipe for a simple pasta dish." }
      ],
      "response_format": {
        "type": "json_schema",
        "json_schema": {
          "schema": {
            "type": "object",
            "properties": {
              "recipe_name": {"type": "string"},
              "ingredients": {"type": "array", "items": {"type": "string"}},
              "steps": {"type": "array", "items": {"type": "string"}},
              "preparation_time": {"type": "string"},
              "servings": {"type": "number"}
            },
            "required": ["recipe_name", "ingredients", "steps", "preparation_time", "servings"]
          }
        }
      }
    }'
  ```

  ```python Python theme={null}
  import json
  from writerai import Writer

  # Initialize the client. If you don't pass the `api_key` parameter,
  # the client looks for the `WRITER_API_KEY` environment variable.
  client = Writer()

  response = client.chat.chat(
    model="palmyra-x5",
    messages=[
      {"role": "system", "content": "You are a helpful cooking assistant."},
      {"role": "user", "content": "Give me a recipe for a simple pasta dish."}
    ],
    response_format={
      "type": "json_schema",
      "json_schema": {
        "schema": {
          "type": "object",
          "properties": {"recipe_name": {"type": "string"}, "ingredients": {"type": "array", "items": {"type": "string"}}, "steps": {"type": "array", "items": {"type": "string"}}, "preparation_time": {"type": "string"}, "servings": {"type": "number"}},
          "required": ["recipe_name", "ingredients", "steps", "preparation_time", "servings"]
        }
      }
    }
  )

  print(json.loads(response.choices[0].message.content))
  ```

  ```javascript JavaScript theme={null}
  import { Writer } from 'writer-sdk';

  // Initialize the client. If you don't pass the `apiKey` parameter,
  // the client looks for the `WRITER_API_KEY` environment variable.
  const client = new Writer();

  const response = await client.chat.chat({
    model: 'palmyra-x5',
    messages: [
      { role: 'system', content: 'You are a helpful cooking assistant.' },
      { role: 'user', content: 'Give me a recipe for a simple pasta dish.' }
    ],
    response_format: { 
      type: 'json_schema',
      json_schema: {
        schema: {
          type: 'object',
          properties: { recipe_name: { type: 'string' }, ingredients: { type: 'array', items: { type: 'string' } }, steps: { type: 'array', items: { type: 'string' } }, preparation_time: { type: 'string' }, servings: { type: 'number' } },
          required: ['recipe_name', 'ingredients', 'steps', 'preparation_time', 'servings']
        }
      }
    },
  });

  console.log(JSON.parse(response.choices[0].message.content));
  ```
</CodeGroup>

The response from the `chat` endpoint includes a `message` object with the `content` field set to the raw response from the model.

<CodeGroup>
  ```json response theme={null}
  {
  "id": "1234",
  "object": "chat.completion",
  "choices": [
      {
      "index": 0,
      "finish_reason": "stop",
      "message": {
          "content": "{ \"recipe_name\": \"Spaghetti Aglio e Olio\", \"ingredients\": [\"12 oz spaghetti\", \"3-4 garlic cloves\", \"1/3 cup extra virgin olive oil\", \"4-6 dried red chili flakes (optional)\", \"Salt\", \"Freshly ground black pepper\", \"Grated Parmesan cheese (optional)\", \"Fresh parsley, chopped (optional)\"], \"steps\": [\"Bring a large pot of salted water to a boil. Cook the spaghetti according to the package instructions until al dente. Reserve 1 cup of pasta water before draining.\", \"In a large skillet, heat the olive oil over medium-low heat. Add the thinly sliced garlic and cook, stirring occasionally, until golden brown (about 4-5 minutes). Be careful not to burn the garlic.\", \"If using red chili flakes, add them to the skillet and cook for another minute.\", \"Add the reserved pasta water to the skillet and stir to combine.\", \"Add the cooked spaghetti to the skillet, tossing to coat the pasta in the garlic and oil mixture. Season with salt and black pepper to taste.\", \"Serve hot, topped with grated Parmesan cheese and chopped fresh parsley if desired.\"] }",
          "role": "assistant",
          "tool_calls": null,
          "graph_data": {
          "sources": null,
          "status": null,
          "subqueries": null
          },
          "llm_data": null,
          "image_data": null,
          "translation_data": null,
          "refusal": null
      },
      "logprobs": null
      }
  ],
  "created": 1745948916,
  "model": "palmyra-x5",
  "usage": {
      "prompt_tokens": 2550,
      "total_tokens": 2797,
      "completion_tokens": 247,
      "prompt_token_details": null,
      "completion_tokens_details": null
  },
  "system_fingerprint": "v1",
  "service_tier": null
  }
  ```
</CodeGroup>

## SDK parse methods

The Python and JavaScript SDKs provide helper `parse` methods for working with structured outputs.

You can define a `Pydantic` or `Zod` model for the response schema, and pass it as the `response_format` parameter to the `parse` method.

The result from the `parse` method includes a `message` object with the `parsed` field. This field's value is an instance of the `Pydantic` or `Zod` model you passed for the `response_format` parameter.

<Warning>
  If you include tool calls in your request, the `parse` method only works with [custom functions](/home/tool-calling) where the tool calls are of type `function`. It does not work with built-in tools with other types such as `web_search`, `vision`, or `translate`. For those cases, you can pass a `json_schema` object in the `response_format` parameter for the `chat` endpoint.
</Warning>

<CodeGroup>
  ```python Python theme={null}
  from typing import List
  from pydantic import Field, BaseModel
  from writerai import Writer

  # Initialize the client. If you don't pass the `api_key` parameter,
  # the client looks for the `WRITER_API_KEY` environment variable.
  client = Writer()

  # Define a Pydantic model for structured output
  class Recipe(BaseModel):
      recipe_name: str = Field(description="The name of the recipe")
      ingredients: List[str] = Field(description="A list of ingredients for the recipe")
      steps: List[str] = Field(description="A list of steps for the recipe")
      preparation_time: str = Field(description="The preparation time for the recipe")
      servings: int = Field(description="The number of servings for the recipe")

  parsed_response = client.chat.parse(
      model="palmyra-x5",
      messages=[
          {"role": "system", "content": "You are a helpful cooking assistant."},
          {
              "role": "user",
              "content": "Give me a recipe for a simple pasta dish.",
          },
      ],
      response_format=Recipe,
  )
  parsed = parsed_response.choices[0].message.parsed

  # Print the parsed response
  print(f"Recipe name: {parsed.recipe_name}")
  print(f"Ingredients:")
  for item in parsed.ingredients:
      print(f"- {item}")
  print(f"Steps:")
  for item in parsed.steps:
      print(f"- {item}")
  print(f"Preparation time: {parsed.preparation_time}")
  print(f"Servings: {parsed.servings}")
  ```

  ```javascript JavaScript theme={null}
  import { Writer } from 'writer-sdk';
  import { z } from 'zod';
  import { zodResponseFormat } from 'writer-sdk/helpers/zod';

  // Initialize the client. If you don't pass the `apiKey` parameter,
  // the client looks for the `WRITER_API_KEY` environment variable.
  const client = new Writer();

  async function main() {
    // Define a schema for structured output
    const recipeSchema = z.object({
      recipeName: z.string(),
      ingredients: z.array(
        z.object({
          name: z.string(),
          amount: z.string(),
        }),
      ),
      steps: z.array(z.string()),
      preparationTime: z.string(),
      servings: z.number(),
    });

    const completion = await client.chat.parse({
      model: 'palmyra-x5',
      messages: [
        { role: 'system', content: 'You are a helpful cooking assistant.' },
        { role: 'user', content: 'Give me a recipe for a simple pasta dish.' },
      ],
      response_format: zodResponseFormat(recipeSchema, 'recipe'),
      temperature: 0.7,
    });

    // Access the parsed structured data
    const message = completion.choices[0]?.message;
    if (message?.parsed) {
      console.log('Recipe name:', message.parsed.recipeName);
      console.log('Ingredients:');
      message.parsed.ingredients.forEach((ing) => {
        console.log(`- ${ing.amount} ${ing.name}`);
      });
      console.log('\nSteps:');
      message.parsed.steps.forEach((step, index) => {
        console.log(`${index + 1}. ${step}`);
      });
      console.log(`\nPreparation time: ${message.parsed.preparationTime}`);
      console.log(`Servings: ${message.parsed.servings}`);
    } else {
      console.log('Raw content:', message?.content);
    }
  }

  main()
  ```
</CodeGroup>

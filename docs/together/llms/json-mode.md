# Source: https://docs.together.ai/docs/json-mode.md

> Learn how to use JSON mode to get structured outputs from LLMs like DeepSeek V3 & Llama 3.3.

# Structured Outputs

## Introduction

Standard large language models respond to user queries by generating plain text. This is great for many applications like chatbots, but if you want to programmatically access details in the response, plain text is hard to work with.

Some models have the ability to respond with structured JSON instead, making it easy to work with data from the LLM's output directly in your application code.

If you're using a supported model, you can enable structured responses by providing your desired schema details to the `response_format` key of the Chat Completions API.

## Supported models

The following newly released top models support JSON mode:

* `openai/gpt-oss-120b`
* `openai/gpt-oss-20b`
* `moonshotai/Kimi-K2-Instruct`
* `zai-org/GLM-4.5-Air-FP8`
* `Qwen/Qwen3-Next-80B-A3B-Instruct`
* `Qwen/Qwen3-Next-80B-A3B-Thinking`
* `Qwen/Qwen3-235B-A22B-Thinking-2507`
* `Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8`
* `Qwen/Qwen3-235B-A22B-Instruct-2507-tput`
* `deepseek-ai/DeepSeek-R1`
* `deepseek-ai/DeepSeek-R1-0528-tput`
* `deepseek-ai/DeepSeek-V3`
* `meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8`
* `Qwen/Qwen2.5-72B-Instruct-Turbo`
* `Qwen/Qwen2.5-VL-72B-Instruct`

The rest of the models that support JSON mode include:

* `meta-llama/Llama-4-Scout-17B-16E-Instruct`
* `meta-llama/Llama-3.3-70B-Instruct-Turbo`
* `deepcogito/cogito-v2-preview-llama-70B`
* `deepcogito/cogito-v2-preview-llama-109B-MoE`
* `deepcogito/cogito-v2-preview-llama-405B`
* `deepcogito/cogito-v2-preview-deepseek-671b`
* `deepseek-ai/DeepSeek-R1-Distill-Llama-70B`
* `deepseek-ai/DeepSeek-R1-Distill-Qwen-14B`
* `marin-community/marin-8b-instruct`
* `meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo`
* `meta-llama/Llama-3.3-70B-Instruct-Turbo-Free`
* `Qwen/Qwen2.5-7B-Instruct-Turbo`
* `Qwen/Qwen2.5-Coder-32B-Instruct`
* `Qwen/QwQ-32B`
* `Qwen/Qwen3-235B-A22B-fp8-tput`
* `arcee-ai/coder-large`
* `meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo`
* `meta-llama/Llama-3.2-3B-Instruct-Turbo`
* `meta-llama/Meta-Llama-3-8B-Instruct-Lite`
* `meta-llama/Llama-3-70b-chat-hf`
* `google/gemma-3n-E4B-it`
* `mistralai/Mistral-7B-Instruct-v0.1`
* `mistralai/Mistral-7B-Instruct-v0.2`
* `mistralai/Mistral-7B-Instruct-v0.3`
* `arcee_ai/arcee-spotlight`

## Basic example

Let's look at a simple example, where we pass a transcript of a voice note to a model and ask it to summarize it.

We want the summary to have the following structure:

```json JSON theme={null}
{
  "title": "A title for the voice note",
  "summary": "A short one-sentence summary of the voice note",
  "actionItems": ["Action item 1", "Action item 2"]
}
```

We can tell our model to use this structure by giving it a [JSON Schema](https://json-schema.org/) definition. Since writing JSON Schema by hand is a bit tedious, we'll use a library to help – Pydantic in Python, and Zod in TypeScript.

Once we have the schema, we can include it in the system prompt and give it to our model using the `response_format` key.

Let's see what this looks like:

<CodeGroup>
  ```py Python theme={null}
  import json
  import together
  from pydantic import BaseModel, Field

  client = together.Together()


  ## Define the schema for the output
  class VoiceNote(BaseModel):
      title: str = Field(description="A title for the voice note")
      summary: str = Field(
          description="A short one sentence summary of the voice note."
      )
      actionItems: list[str] = Field(
          description="A list of action items from the voice note"
      )


  def main():
      transcript = (
          "Good morning! It's 7:00 AM, and I'm just waking up. Today is going to be a busy day, "
          "so let's get started. First, I need to make a quick breakfast. I think I'll have some "
          "scrambled eggs and toast with a cup of coffee. While I'm cooking, I'll also check my "
          "emails to see if there's anything urgent."
      )

      # Call the LLM with the JSON schema
      extract = client.chat.completions.create(
          messages=[
              {
                  "role": "system",
                  "content": f"The following is a voice message transcript. Only answer in JSON and follow this schema {json.dumps(VoiceNote.model_json_schema())}.",
              },
              {
                  "role": "user",
                  "content": transcript,
              },
          ],
          model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
          response_format={
              "type": "json_schema",
              "schema": VoiceNote.model_json_schema(),
          },
      )

      output = json.loads(extract.choices[0].message.content)
      print(json.dumps(output, indent=2))
      return output


  main()
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";
  import { z } from "zod";
  import { zodToJsonSchema } from "zod-to-json-schema";

  const together = new Together();

  // Defining the schema we want our data in
  const voiceNoteSchema = z.object({
    title: z.string().describe("A title for the voice note"),
    summary: z
      .string()
      .describe("A short one sentence summary of the voice note."),
    actionItems: z
      .array(z.string())
      .describe("A list of action items from the voice note"),
  });
  const jsonSchema = zodToJsonSchema(voiceNoteSchema, { target: "openAi" });

  async function main() {
    const transcript =
      "Good morning! It's 7:00 AM, and I'm just waking up. Today is going to be a busy day, so let's get started. First, I need to make a quick breakfast. I think I'll have some scrambled eggs and toast with a cup of coffee. While I'm cooking, I'll also check my emails to see if there's anything urgent.";
    const extract = await together.chat.completions.create({
      messages: [
        {
          role: "system",
          content: `The following is a voice message transcript. Only answer in JSON and follow this schema ${JSON.stringify(jsonSchema)}.`,
        },
        {
          role: "user",
          content: transcript,
        },
      ],
      model: "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
      response_format: { type: "json_object", schema: jsonSchema },
    });

    if (extract?.choices?.[0]?.message?.content) {
      const output = JSON.parse(extract?.choices?.[0]?.message?.content);
      console.log(output);
      return output;
    }
    return "No output.";
  }

  main();
  ```

  ```Text curl theme={null}
  curl -X POST https://api.together.xyz/v1/chat/completions \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -d '{
    "messages": [
      {
        "role": "system",
        "content": "The following is a voice message transcript. Only answer in JSON."
      },
      {
        "role": "user",
        "content": "Good morning! It'"'"'s 7:00 AM, and I'"'"'m just waking up. Today is going to be a busy day, so let'"'"'s get started. First, I need to make a quick breakfast. I think I'"'"'ll have some scrambled eggs and toast with a cup of coffee. While I'"'"'m cooking, I'"'"'ll also check my emails to see if there'"'"'s anything urgent."
      }
    ],
    "model": "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
    "response_format": {
      "type": "json_object",
      "schema": {
        "properties": {
          "title": {
            "description": "A title for the voice note",
            "title": "Title",
            "type": "string"
          },
          "summary": {
            "description": "A short one sentence summary of the voice note.",
            "title": "Summary",
            "type": "string"
          },
          "actionItems": {
            "description": "A list of action items from the voice note",
            "items": { "type": "string" },
            "title": "Actionitems",
            "type": "array"
          }
        },
        "required": ["title", "summary", "actionItems"],
        "title": "VoiceNote",
        "type": "object"
      }
    }
  }'
  ```
</CodeGroup>

If we try it out, our model responds with the following:

```json JSON theme={null}
{
  "title": "Morning Routine",
  "summary": "Starting the day with a quick breakfast and checking emails",
  "actionItems": [
    "Cook scrambled eggs and toast",
    "Brew a cup of coffee",
    "Check emails for urgent messages"
  ]
}
```

Pretty neat!

Our model has generated a summary of the user's transcript using the schema we gave it.

### Prompting the model

It's important to always tell the model to respond **only in JSON** and include a plain‑text copy of the schema in the prompt (either as a system prompt or a user message). This instruction must be given *in addition* to passing the schema via the `response_format` parameter.

By giving an explicit "respond in JSON" direction and showing the schema text, the model will generate output that matches the structure you defined. This combination of a textual schema and the `response_format` setting ensures consistent, valid JSON responses every time.

## Regex example

All the models supported for JSON mode also support regex mode. Here's an example using it to constrain the classification.

<CodeGroup>
  ```py Python theme={null}
  import together

  client = together.Together()

  completion = client.chat.completions.create(
      model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
      messages=[
          {
              "role": "system",
              "content": "You are an AI-powered expert specializing in classifying sentiment. You will be provided with a text, and your task is to classify its sentiment as positive, neutral, or negative.",
          },
          {"role": "user", "content": "Wow. I loved the movie!"},
      ],
      response_format={
          "type": "regex",
          "pattern": "(positive|neutral|negative)",
      },
  )

  print(completion.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";
  const together = new Together();

  async function main() {
    const completion = await together.chat.completions.create({
      model: "meta-llama/Llama-3.3-70B-Instruct-Turbo",
      temperature: 0.2,
      max_tokens: 10,
      messages: [
        {
          role: "system",
          content:
            "You are an AI-powered expert specializing in classifying sentiment. You will be provided with a text, and your task is to classify its sentiment as positive, neutral, or negative.",
        },
        {
          role: "user",
          content: "Wow. I loved the movie!",
        },
      ],
      response_format: {
        type: "regex",
        // @ts-ignore
        pattern: "(positive|neutral|negative)",
      },
    });

    console.log(completion?.choices[0]?.message?.content);
  }

  main();
  ```

  ```curl cURL theme={null}
  curl https://api.together.xyz/v1/chat/completions \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo",
      "messages": [
        {
          "role": "user",
          "content": "Return only an email address for Alan Turing at Enigma. End with .com and newline."
        }
      ],
      "stop": ["\n"],
      "response_format": {
        "type": "regex",
        "pattern": "\\w+@\\w+\\.com\\n"
      },
      "temperature": 0.0,
      "max_tokens": 50
    }'
  ```
</CodeGroup>

## Reasoning model example

You can also extract structured outputs from some reasoning models such as `DeepSeek-R1-0528`.

Below we ask the model to solve a math problem step-by-step showing its work:

```py Python theme={null}
import json
import together
from pydantic import BaseModel, Field

client = together.Together()


class Step(BaseModel):
    explanation: str
    output: str


class MathReasoning(BaseModel):
    steps: list[Step]
    final_answer: str


completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-R1",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful math tutor. Guide the user through the solution step by step.",
        },
        {"role": "user", "content": "how can I solve 8x + 7 = -23"},
    ],
    response_format={
        "type": "json_schema",
        "schema": MathReasoning.model_json_schema(),
    },
)

math_reasoning = json.loads(completion.choices[0].message.content)

print(json.dumps(math_reasoning, indent=2))
```

Example output:

```json JSON theme={null}
{
  "steps": [
    {
      "explanation": "To solve the equation 8x + 7 = -23, I need to isolate the variable x on one side of the equation. That means I'll have to get rid of the constant term and the coefficient of x.",
      "output": ""
    },
    {
      "explanation": "First, I'll eliminate the constant term on the left side. Since it's +7, I can subtract 7 from both sides of the equation. This keeps the equation balanced.",
      "output": "8x + 7 - 7 = -23 - 7"
    },
    {
      "explanation": "Now, simplifying both sides: on the left, 7 - 7 is 0, so I'm left with 8x. On the right, -23 - 7 is -30.",
      "output": "8x = -30"
    },
    {
      "explanation": "Next, I need to solve for x. Since x is multiplied by 8, I should divide both sides by 8 to isolate x.",
      "output": "8x / 8 = -30 / 8"
    },
    {
      "explanation": "Simplifying that, 8x divided by 8 is just x. And -30 divided by 8 is -30/8.",
      "output": "x = -30/8"
    },
    {
      "explanation": "I can simplify this fraction. Both 30 and 8 are divisible by 2. So, -30 divided by 2 is -15, and 8 divided by 2 is 4.",
      "output": "x = -15/4"
    },
    {
      "explanation": "I can also write this as a mixed number or decimal, but the fraction is already simplified. -15/4 is -3.75, but I'll keep it as a fraction since it's exact.",
      "output": "x = -15/4"
    }
  ],
  "final_answer": "x = -\\frac{15}{4}"
}
```

## Vision model example

Let's look at another example, this time using a vision model.

We want our LLM to extract text from the following screenshot of a Trello board:

![Trello board](https://files.readme.io/4512824ce58b18d946c8a8c786a21a5346e18e8b1860fc03de07d69a0145450e-image.png)

In particular, we want to know the name of the project (Project A), and the number of columns in the board (4).

Let's try it out:

<CodeGroup>
  ```py Python theme={null}
  import json
  import together
  from pydantic import BaseModel, Field

  client = together.Together()


  ## Define the schema for the output
  class ImageDescription(BaseModel):
      project_name: str = Field(
          description="The name of the project shown in the image"
      )
      col_num: int = Field(description="The number of columns in the board")


  def main():
      imageUrl = "https://napkinsdev.s3.us-east-1.amazonaws.com/next-s3-uploads/d96a3145-472d-423a-8b79-bca3ad7978dd/trello-board.png"

      # Call the LLM with the JSON schema
      extract = client.chat.completions.create(
          messages=[
              {
                  "role": "user",
                  "content": [
                      {
                          "type": "text",
                          "text": "Extract a JSON object from the image.",
                      },
                      {
                          "type": "image_url",
                          "image_url": {
                              "url": imageUrl,
                          },
                      },
                  ],
              },
          ],
          model="Qwen/Qwen2.5-VL-72B-Instruct",
          response_format={
              "type": "json_schema",
              "schema": ImageDescription.model_json_schema(),
          },
      )

      output = json.loads(extract.choices[0].message.content)
      print(json.dumps(output, indent=2))
      return output


  main()
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";
  import { z } from "zod";
  import { zodToJsonSchema } from "zod-to-json-schema";

  const together = new Together();

  // Define the shape of our data
  const schema = z.object({
    projectName: z
      .string()
      .describe("The name of the project shown in the image"),
    columnCount: z.number().describe("The number of columns in the board"),
  });
  const jsonSchema = zodToJsonSchema(schema, { target: "openAi" });

  const imageUrl =
    "https://napkinsdev.s3.us-east-1.amazonaws.com/next-s3-uploads/d96a3145-472d-423a-8b79-bca3ad7978dd/trello-board.png";

  async function main() {
    const extract = await together.chat.completions.create({
      messages: [
        {
          role: "user",
          content: [
            { type: "text", text: "Extract a JSON object from the image." },
            {
              type: "image_url",
              image_url: { url: imageUrl },
            },
          ],
        },
      ],
      model: "Qwen/Qwen2.5-VL-72B-Instruct",
      response_format: {
        type: "json_object",
        schema: jsonSchema,
      },
    });

    if (extract?.choices?.[0]?.message?.content) {
      const output = JSON.parse(extract?.choices?.[0]?.message?.content);
      console.log(output);
      return output;
    }
    return "No output.";
  }

  main();
  ```
</CodeGroup>

If we run it, we get the following output:

```json JSON theme={null}
{
  "projectName": "Project A",
  "columnCount": 4
}
```

JSON mode has worked perfectly alongside Qwen's vision model to help us extract structured text from an image!

## Try out your code in the Together Playground

You can try out JSON Mode in the [Together Playground](https://api.together.ai/playground/v2/chat/Qwen/Qwen2.5-VL-72B-Instruct?) to test out variations on your schema and prompt:

![Playground](https://files.readme.io/464405525305919beed6d35a6e85b48cf5a3149891c4eefcee4d17b79773940c-Screenshot_2025-04-24_at_5.07.55_PM.png)

Just click the RESPONSE FORMAT dropdown in the right-hand sidebar, choose JSON, and upload your schema!


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt
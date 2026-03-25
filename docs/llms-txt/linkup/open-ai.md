# Source: https://docs.linkup.so/pages/sdk/open-ai/open-ai.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.linkup.so/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenAI SDK

> How to use OpenAI SDK natively in your apps.

## Introduction

The OpenAI SDK can be used to interact with the Linkup API, to generate responses.

<Info>
  We are only compatible with [Responses API](https://platform.openai.com/docs/api-reference/responses).<br />
  Chat Completions API is **NOT** supported at the moment.
</Info>

## Quickstart

Get started with the OpenAI SDK in less than 5 minutes!

<Tabs>
  <Tab title="Python">
    <Steps>
      <Step title="Get your API Keys">
        <Card title="Get your API key" icon="key" href="https://app.linkup.so" horizontal="True">
          Create a Linkup account for free to get your API key.
        </Card>
      </Step>

      <Step title="Installation">
        You can install the OpenAI SDK using the following:

        ```shell  theme={null}
        pip install openai
        ```
      </Step>

      <Step title="Usage">
        Here is a basic usage showing how to use the OpenAI SDK:

        ```python  theme={null}
        from openai import OpenAI

        client = OpenAI(
          base_url='https://api.linkup.so/v1',
          api_key="<YOUR API KEY>"
        )

        response = client.responses.create(
          model="linkup-standard",
          input="Can you tell me which women were awarded the Physics Nobel Prize",
        )

        print(response.output_text)
        ```
      </Step>
    </Steps>
  </Tab>

  <Tab title="TypeScript">
    <Steps>
      <Step title="Get your API Keys">
        <Card title="Get your API key" icon="key" href="https://app.linkup.so" horizontal="True">
          Create a Linkup account for free to get your API key.
        </Card>
      </Step>

      <Step title="Installation">
        You can install the OpenAI SDK using the following:

        ```shell  theme={null}
        npm i openai
        ```
      </Step>

      <Step title="Usage">
        Here is a basic usage showing how to use the OpenAI SDK:

        ```typescript  theme={null}
        import OpenAI from 'openai';

        const client = new OpenAI({
          baseURL: 'https://api.linkup.so/v1',
          apiKey: "<YOUR API KEY>"
        });

        const response = await client.responses.create({
          model: "linkup-standard",
          input: "Can you tell me which women were awarded the Physics Nobel Prize",
        });

        console.log(response.output_text);
        ```
      </Step>
    </Steps>
  </Tab>
</Tabs>

## Input Parameters

| Parameter | Type   | Description                                                  | Default  |
| --------- | ------ | ------------------------------------------------------------ | -------- |
| model     | string | Type of search to perform "linkup-standard" or "linkup-deep" | Required |

For others parameters, please refer to the [Responses API](https://platform.openai.com/docs/api-reference/responses).

### Model

The `model` field is used to select the type of search you want to perform:

* **linkup-standard**: the search will be straightforward and fast, suited for relatively simple queries (e.g. "What's the weather in Paris today?")
* **linkup-deep**: the search will use an agentic workflow, which makes it in general slower, but it will be able to solve more complex queries (e.g. "What is the company profile of LangChain accross the last few years, and how does it compare to its concurrents?")

## Using structured output (advanced)

<Tabs>
  <Tab title="Python">
    <Steps>
      <Step title="Get your API Keys">
        <Card title="Get your API key" icon="key" href="https://app.linkup.so" horizontal="True">
          Create a Linkup account for free to get your API key.
        </Card>
      </Step>

      <Step title="Installation">
        You need to install the OpenAI SDK and Pydantic using the following:

        ```shell  theme={null}
        pip install openai pydantic
        ```
      </Step>

      <Step title="Usage">
        Here is a example of how to use the structured output with the OpenAI SDK:

        ```python  theme={null}
        from openai import OpenAI
        from pydantic import BaseModel

        class Winner(BaseModel):
          name: str
          year: str

        class Response(BaseModel):
          winners: list[Winner]

        client = OpenAI(
          base_url='https://api.linkup.so/v1',
          api_key="<YOUR API KEY>"
        )

        response = client.responses.parse(
          model="linkup-standard",
          input="Can you tell me which women were awarded the Physics Nobel Prize",
          text_format=Response,
        )

        print(response.output_parsed)
        ```
      </Step>
    </Steps>
  </Tab>

  <Tab title="TypeScript">
    <Steps>
      <Step title="Get your API Keys">
        <Card title="Get your API key" icon="key" href="https://app.linkup.so" horizontal="True">
          Create a Linkup account for free to get your API key.
        </Card>
      </Step>

      <Step title="Installation">
        You need to install the OpenAI SDK and Zod using the following:

        ```shell  theme={null}
        npm i openai zod
        ```
      </Step>

      <Step title="Usage">
        Here is a example of how to use the structured output with the OpenAI SDK:

        ```typescript  theme={null}
        import OpenAI from 'openai';
        import { zodTextFormat } from 'openai/helpers/zod.mjs';
        import { z } from "zod";

        const client = new OpenAI({
          baseURL: 'https://api.linkup.so/v1',
          apiKey: "<YOUR API KEY>"
        });

        const NobelWinners = z.object({
          winners: z.array(
            z.object({
              name: z.string(),
              year: z.string(),
            })
          )
        });

        const response = await client.responses.create({
          model: "linkup-standard",
          input: "Can you tell me which women were awarded the Physics Nobel Prize",
          text: {
            format: zodTextFormat(NobelWinners, "winners"),
          }
        });

        console.log(response.output_text);
        ```
      </Step>
    </Steps>
  </Tab>
</Tabs>

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


Built with [Mintlify](https://mintlify.com).
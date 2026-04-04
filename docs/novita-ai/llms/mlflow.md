# Source: https://novita.ai/docs/guides/mlflow.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# MLflow

> Trace Novita AI calls in MLflow with OpenAI-compatible SDK instrumentation for Python and JavaScript.

This guide shows how to integrate **Novita AI** with MLflow Tracing. By using Novita AI's OpenAI-compatible endpoint (`https://api.novita.ai/openai`), you can capture prompts, responses, latency, token usage, and model metadata in MLflow.

<Frame>
    <img src="https://mintcdn.com/novitaai/TDkIugxCqQKXM7rz/images/third-party/mlflow-trace-details-timeline.png?fit=max&auto=format&n=TDkIugxCqQKXM7rz&q=85&s=e91bc43cf88dc473905c4001015b8cfa" alt="MLflow trace details and timeline" width="3076" height="1422" data-path="images/third-party/mlflow-trace-details-timeline.png" />
</Frame>

# Prerequisites

Before you start, make sure you have:

* Novita AI API key: create one in [Key Management](https://novita.ai/settings/key-management).
* A running MLflow tracking server. You can use local default `http://localhost:5000`.
* Python or JavaScript runtime.

# Integration Steps

## Step 1: Install Dependencies

<CodeGroup>
  ```bash Python icon="python" theme={"system"}
  pip install 'mlflow[genai]' openai
  ```

  ```bash JavaScript / TypeScript icon="js" theme={"system"}
  npm install @mlflow/openai openai
  ```
</CodeGroup>

## Step 2: Start MLflow Server

If you have a local Python environment >= 3.10, you can start MLflow with:

```bash  theme={"system"}
mlflow server
```

MLflow also provides a Docker Compose setup:

```bash  theme={"system"}
git clone --depth 1 --filter=blob:none --sparse https://github.com/mlflow/mlflow.git
cd mlflow
git sparse-checkout set docker-compose
cd docker-compose
cp .env.dev.example .env
docker compose up -d
```

Then open `http://localhost:5000` to confirm the MLflow UI is accessible.

## Step 3: Enable Tracing and Call Novita AI

<CodeGroup>
  ```python Python icon="python" theme={"system"}
  import openai
  import mlflow

  # Enable auto-tracing for OpenAI-compatible calls
  mlflow.openai.autolog()

  # Optional: set tracking target and experiment
  mlflow.set_tracking_uri("http://localhost:5000")
  mlflow.set_experiment("Novita AI")

  client = openai.OpenAI(
      base_url="https://api.novita.ai/openai",
      api_key="<your_novita_api_key>",
  )

  response = client.chat.completions.create(
      model="deepseek/deepseek-r1",
      messages=[
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": "What is the capital of France?"},
      ],
  )

  print(response.choices[0].message.content)
  ```

  ```ts JavaScript / TypeScript icon="js" theme={"system"}
  import { OpenAI } from "openai";
  import { tracedOpenAI } from "@mlflow/openai";

  const client = tracedOpenAI(
    new OpenAI({
      baseURL: "https://api.novita.ai/openai",
      apiKey: "<your_novita_api_key>",
    })
  );

  const response = await client.chat.completions.create({
    model: "deepseek/deepseek-r1",
    messages: [
      { role: "system", content: "You are a helpful assistant." },
      { role: "user", content: "What is the capital of France?" },
    ],
    temperature: 0.1,
    max_tokens: 100,
  });

  console.log(response.choices[0].message?.content);
  ```
</CodeGroup>

## Step 4: View Traces in MLflow UI

Open your MLflow UI (for example `http://localhost:5000`) and go to your configured experiment to inspect traces.

You should see:

* Prompt and completion content
* Latency and token usage
* Model and request metadata
* Errors/exceptions (if any)

## Step 5: Advanced Tracing References

### Streaming and Async

MLflow supports tracing for streaming and async Novita AI APIs. See:

* [OpenAI Tracing](https://mlflow.org/docs/latest/genai/tracing/integrations/listing/openai/)

### Combine with frameworks or manual tracing

<CodeGroup>
  ```python Python icon="python" theme={"system"}
  import json
  from openai import OpenAI
  import mlflow
  from mlflow.entities import SpanType

  # Initialize the OpenAI client with Novita AI API endpoint
  client = OpenAI(
      base_url="https://api.novita.ai/openai",
      api_key="<your_novita_api_key>",
  )


  # Create a parent span for the Novita AI call
  @mlflow.trace(span_type=SpanType.CHAIN)
  def answer_question(question: str):
      messages = [{"role": "user", "content": question}]
      response = client.chat.completions.create(
          model="deepseek/deepseek-r1",
          messages=messages,
      )

      # Attach session/user metadata to the trace
      mlflow.update_current_trace(
          metadata={
              "mlflow.trace.session": "session-12345",
              "mlflow.trace.user": "user-a",
          }
      )
      return response.choices[0].message.content


  answer = answer_question("What is the capital of France?")
  ```

  ```ts JavaScript / TypeScript icon="js" theme={"system"}
  import * as mlflow from "@mlflow/core";
  import { OpenAI } from "openai";
  import { tracedOpenAI } from "@mlflow/openai";

  mlflow.init({
    trackingUri: "http://localhost:5000",
    experimentId: "<your_experiment_id>",
  });

  // Wrap the OpenAI client and point to Novita AI endpoint
  const client = tracedOpenAI(
    new OpenAI({
      baseURL: "https://api.novita.ai/openai",
      apiKey: "<your_novita_api_key>",
    })
  );

  // Create a traced function that wraps the Novita AI call
  const answerQuestion = mlflow.trace(
    async (question: string) => {
      const resp = await client.chat.completions.create({
        model: "deepseek/deepseek-r1",
        messages: [{ role: "user", content: question }],
      });
      return resp.choices[0].message?.content;
    },
    { name: "answer-question" }
  );

  await answerQuestion("What is the capital of France?");
  ```
</CodeGroup>

For full upstream reference:

* MLflow Novita AI integration page: [Tracing Novita AI](https://mlflow.org/docs/latest/genai/tracing/integrations/listing/novitaai/)
* MLflow OpenAI tracing docs: [OpenAI Tracing](https://mlflow.org/docs/latest/genai/tracing/integrations/listing/openai/)

For Novita model details and endpoint usage, see:

* Novita LLM API guide: [LLM API](/guides/llm-api)


Built with [Mintlify](https://mintlify.com).
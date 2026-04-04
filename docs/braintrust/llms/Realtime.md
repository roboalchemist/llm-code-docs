# Source: https://braintrust.dev/docs/cookbook/recipes/Realtime.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Evaluating audio with the OpenAI Realtime API

<div className="text-sm">[Contributed](https://github.com/braintrustdata/braintrust-cookbook/blob/main/examples/Realtime/Realtime.mdx) by [Ornella Altunyan](https://twitter.com/ornelladotcom) on 2024-12-14</div>

The OpenAI [Realtime API](https://platform.openai.com/docs/guides/realtime), designed for building advanced multimodal conversational experiences, unlocks even more use cases in AI applications. However, evaluating this and other audio models' outputs in practice is an unsolved problem. In this cookbook, we'll build a robust application with the Realtime API, incorporating tool-calling and user input. Then, we'll evaluate the results. Let's get started!

## Getting started

In this cookbook, we're going to build a speech-to-speech RAG agent that answers questions about the Braintrust documentation.

To get started, you'll need a few accounts:

* [Braintrust](https://www.braintrust.dev/signup)
* [Pinecone](https://app.pinecone.io/?sessionType=signup)
* [OpenAI](https://platform.openai.com/signup)

and `node`, `npm`, and `typescript` installed locally. If you'd like to follow along in code,
the [realtime-rag](https://github.com/braintrustdata/braintrust-cookbook/tree/main/examples/Realtime/realtime-rag)
project contains a working example with all of the documents and code snippets we'll use.

## Clone the repo

To start, clone the repo and install the dependencies:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
git clone https://github.com/braintrustdata/braintrust-cookbook.git
cd braintrust-cookbook/examples/Realtime/realtime-rag
npm install
```

Next, create a `.env.local` file with your API keys:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
BRAINTRUST_API_KEY=<your-api-key>
PINECONE_API_KEY=<your-pinecone-api-key>
```

Finally, make sure to set your `OPENAI_API_KEY` environment variable in the [AI providers](https://www.braintrust.dev/app/braintrustdata.com/settings/secrets) section
of your account, and set the `PINECONE_API_KEY` environment variable in the [Environment variables](https://www.braintrust.dev/app/settings?subroute=env-vars) section.

<Callout type="info">
  We'll use the local environment variables to embed and upload the vectors, and
  the Braintrust variables to run the RAG tool and LLM calls remotely.
</Callout>

## Upload the vectors

To upload the vectors, run the `upload-vectors.ts` script:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
npx tsx upload-vectors.ts
```

This script reads all the files from the `docs-sample` directory, breaks them into sections based on headings, and creates vector embeddings for each section using OpenAI's API. It then stores those embeddings along with the section's title and content in Pinecone.

That's it for setup! Now let's dig into the code.

## Accessing the Realtime API

Building with the OpenAI Realtime API is complex because it is built on WebSockets, and it lacks client-side authentication. However, the Braintrust [AI Proxy](/deploy/ai-proxy) makes it easy to connect to the API in a secure and scalable way. The proxy securely manages your OpenAI API key, issuing [**temporary credentials**](/deploy/ai-proxy#temporary-credentials-for-end-user-access) to your backend and frontend. The frontend sends any voice data from your app to the proxy, which handles secure communication with OpenAI’s Realtime API.

To access the Realtime API through the Braintrust proxy, we changed the proxy URL when instantiating the `RealtimeClient` to `https://braintrustproxy.com/v1/realtime`. In our app, the `RealtimeClient` is initialized when the `ConsolePage` component is rendered.

We set up this logic in `page.tsx`:

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import { ConsolePage } from '@/components/ConsolePage';
import './App.scss';

const PROXY_URL =
  process.env.BRAINTRUST_PROXY_URL ?? 'https://braintrustproxy.com/v1';

// You can swap this out to your OPENAI_API_KEY if you do not have a Braintrust account, but
// you will not have access to logging features.
const API_KEY = process.env.BRAINTRUST_API_KEY;

// Set this to your project name if you have one, otherwise it will default to "Realtime voice console"
const BRAINTRUST_PROJECT_NAME = process.env.BRAINTRUST_PROJECT_NAME;

export default async function Home() {
  if (!API_KEY) {
    return (
      <div>
        Missing BRAINTRUST_API_KEY
      </div>
    );
  }

  const model = 'gpt-4o-realtime-preview-2024-10-01';
  const response = await fetch(`${PROXY_URL}/credentials`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${API_KEY}`,
    },
    body: JSON.stringify({
      model,
      logging: {
        project_name: BRAINTRUST_PROJECT_NAME || "Realtime RAG bot",
      },
      // This is the TTL for starting the conversation, but it can continue as long as needed
      // once the conversation is started.
      ttl_seconds: 60 * 10 /* 10 minutes */,
    }),
    cache: 'no-store',
  });

  if (!response.ok) {
    const text = await response.text();
    return <div><p>Failed to get credentials</p><pre>{text}</pre></div>;
  }

  const { key } = await response.json();

  return <ConsolePage apiKey={key} url={`${PROXY_URL}/realtime`} />;
}
```

<Callout>
  You can also use our proxy with an AI provider’s API key, but you will not
  have access to other Braintrust features, like logging.
</Callout>

## Creating a RAG tool

The retrieval logic also happens on the server side. We set up the helper function and route handler that queries Pinecone in `route.ts` so that we can call the retrieval tool on the client side like this:

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
client.addTool(
  {
    name: "pinecone_retrieval",
    description:
      "Retrieves relevant information from Braintrust documentation.",
    parameters: {
      type: "object",
      properties: {
        query: {
          type: "string",
          description: "The search query to find relevant documentation.",
        },
      },
      required: ["query"],
    },
  },
  async ({ query }: { query: string }) => {
    try {
      setLastQuery(query);
      const results = await fetchFromPinecone(query);
      setRetrievalResults(results);
      return results
        .map(
          (result) =>
            `[Score: ${result.score.toFixed(2)}] ${result.metadata.title}\n${
              result.metadata.content
            }`,
        )
        .join("\n\n");
    } catch (error) {
      throw error;
    }
  },
);
```

<Callout type="info">
  Currently, because of the way the Realtime API works, we have to use OpenAI
  tool calling here instead of Braintrust tool functions.
</Callout>

## Setting up the system prompt

When we call the Realtime API, we pass it a set of instructions that are configured in `conversation_config.js`:

```javascript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
export const instructions = `System settings:
Tool use: enabled.

Instructions:
- You are an AI agent responsible for helping users with questions about Braintrust
- Always use the pinecone_retrieval tool to get additional context for your responses
- You should only answer questions about Braintrust
- If you are asked a question that is irrelevant to Braintrust, give a simple and polite refusal
- Make sure there is no code in your responses, responses should be text information-based only giving as much detail as possible
- Please make sure to respond with a helpful voice via audio
- Be kind, helpful, and curteous
- It is okay to ask the user questions
- Use tools and functions you have available liberally, it is part of the training apparatus
- Be open to exploration and conversation
- Someone is relying on you - help them be as successful as possible!

Personality:
- Be upbeat and genuine
- Try speaking quickly as if excited
`;
```

Feel free to play around with the system prompt at any point, and see how it impacts the LLM's responses in the app.

## Running the app

To run the app, navigate to `/web` and run `npm run dev`. You should have the app load on `localhost:3000`.

Start a new conversation, and ask a few questions about Braintrust. Feel free to interrupt the bot, or ask unrelated questions, and see what happens. When you're finished, end the conversation. Have a couple of conversations to get a feel for some of the limitations and nuances of the bot - each conversation will come in handy in the next step.

## Logging in Braintrust

In addition to client-side authentication, you’ll also get the other benefits of building with Braintrust, like logging, built in. When you ran the app and connected to the Realtime API, logs were generated for each conversation. When you closed the session, the log was complete and ready to view in Braintrust. Each LLM and tool call is contained in its own span inside of the trace. In addition, the audio files were uploaded as [attachments](https://braintrust.dev/blog/attachments) in your trace. This means that you don’t have to exit the UI to listen to each of the inputs and outputs for the LLM calls.

<img src="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/Realtime/realtime-log.png?fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=cba2a3d51242c098198dbb0af9d68526" alt="Realtime log with attachment" data-og-width="2802" width="2802" data-og-height="1988" height="1988" data-path="cookbook/assets/Realtime/realtime-log.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/Realtime/realtime-log.png?w=280&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=1c69e8ad7528b81e6cc90647102ab04b 280w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/Realtime/realtime-log.png?w=560&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=4aeae2989b16642d4d21cb0770a7a5c7 560w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/Realtime/realtime-log.png?w=840&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=63db8dc06c588bfe594a2f0ac049e5e8 840w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/Realtime/realtime-log.png?w=1100&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=017f12ba06da97351a919ae8cc96e949 1100w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/Realtime/realtime-log.png?w=1650&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=5d8d01c40d4bdf0ef5291b115b13b860 1650w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/Realtime/realtime-log.png?w=2500&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=ab121ac647e5116f514cb7f4a9a6713e 2500w" />

## Online evaluations

In Braintrust, you can run server-side online evaluations that are automatically run asynchronously as you upload logs. This makes it easier to evaluate your app in situations like this, where the prompt and tool might not be synced to Braintrust.

Audio evals are complex, because there are multiple aspects of your application you can focus on. In this cookbook, we'll use the vector search query as a proxy for the quality of the Realtime API's interpretation of the user's input.

### Setting up your scorer

We'll need to create a scorer that captures the criteria we want to evaluate. Since we're dealing with complex RAG outputs, we'll use a custom LLM-as-a-judge scorer.
For an LLM-as-a-judge scorer, you define a prompt that evaluates the output and maps its choices to specific scores.

Navigate to **Scorers** and create a new scorer. Call your scorer **BraintrustRAG** and add the following prompt:

```javascript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
Consider the following question:

{{input.arguments.query}}

and answer:

{{output}}

How well does the answer answer the question?
a) Very well
b) Reasonably well
c) Not well
```

The prompt uses mustache syntax to map the input to the query that gets sent to Pinecone, and get the output. We'll also assign choice score to the options we included in the prompt.

<img src="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/Realtime/rag-scorer.png?fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=9c530837a968c76de7719d409f5ee0cb" alt="RAG scorer" data-og-width="1524" width="1524" data-og-height="1816" height="1816" data-path="cookbook/assets/Realtime/rag-scorer.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/Realtime/rag-scorer.png?w=280&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=7a89406a41742e6cd6d0e4208f891b3f 280w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/Realtime/rag-scorer.png?w=560&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=6cc72a537fcc28557a260c9483b4654f 560w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/Realtime/rag-scorer.png?w=840&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=845ce12fc35cf96fb2aa35d14ad6a5b3 840w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/Realtime/rag-scorer.png?w=1100&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=df497cd1e7e9f2be6d5608bcddc81ad1 1100w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/Realtime/rag-scorer.png?w=1650&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=77b92503a83137f143c1d96f28146b4d 1650w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/Realtime/rag-scorer.png?w=2500&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=030fb85d0df9ef7458a17a59f58d4a1c 2500w" />

### Configuring your online eval

Navigate to **Configuration** and scroll down to **Online scoring**. Select **Add rule** to configure your online scoring rule. Select the scorer we just created from the menu, and deselect **Apply to root span**. We'll filter to the **function** span since that's where our tool is called.

<img src="https://mintcdn.com/braintrust/f0JS3zbOyRi_8sGi/cookbook/assets/Realtime/configure-score.png?fit=max&auto=format&n=f0JS3zbOyRi_8sGi&q=85&s=28276b6471813abe4edae034a4bf9572" alt="Configure score" data-og-width="1010" width="1010" data-og-height="1386" height="1386" data-path="cookbook/assets/Realtime/configure-score.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/f0JS3zbOyRi_8sGi/cookbook/assets/Realtime/configure-score.png?w=280&fit=max&auto=format&n=f0JS3zbOyRi_8sGi&q=85&s=3d2b9bb903929885f1445293d85a03d9 280w, https://mintcdn.com/braintrust/f0JS3zbOyRi_8sGi/cookbook/assets/Realtime/configure-score.png?w=560&fit=max&auto=format&n=f0JS3zbOyRi_8sGi&q=85&s=7ae41bd889f2f80e9640a71b80a43b90 560w, https://mintcdn.com/braintrust/f0JS3zbOyRi_8sGi/cookbook/assets/Realtime/configure-score.png?w=840&fit=max&auto=format&n=f0JS3zbOyRi_8sGi&q=85&s=2c4168dec6f303a1e304547086f4e43d 840w, https://mintcdn.com/braintrust/f0JS3zbOyRi_8sGi/cookbook/assets/Realtime/configure-score.png?w=1100&fit=max&auto=format&n=f0JS3zbOyRi_8sGi&q=85&s=6e22378b9f1e5015e810194b04428d21 1100w, https://mintcdn.com/braintrust/f0JS3zbOyRi_8sGi/cookbook/assets/Realtime/configure-score.png?w=1650&fit=max&auto=format&n=f0JS3zbOyRi_8sGi&q=85&s=b7813edc46f701171f319d844cf14982 1650w, https://mintcdn.com/braintrust/f0JS3zbOyRi_8sGi/cookbook/assets/Realtime/configure-score.png?w=2500&fit=max&auto=format&n=f0JS3zbOyRi_8sGi&q=85&s=fe4d9534f1fc02a2d1ad7a23e8bd1b80 2500w" />

The score will now automatically run at the specified sampling rate for all logs in the project.

### Viewing your evaluations

Now that you've set up your online evaluations, you can view the scores from within your logs. Underneath each function span that was included in the sampling rate, you'll have an additional span with the score.

<img src="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/Realtime/scoring-span.png?fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=5a072512cb2c32f9e069c97f737cba86" alt="Scoring span" data-og-width="2792" width="2792" data-og-height="2010" height="2010" data-path="cookbook/assets/Realtime/scoring-span.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/Realtime/scoring-span.png?w=280&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=b548742c37a8aa972c265e4e34d9e31d 280w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/Realtime/scoring-span.png?w=560&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=ba3aa613a8e2f5ac7be2b5707cc22c90 560w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/Realtime/scoring-span.png?w=840&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=6360e34287de17513dfe9f4a43bbd55b 840w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/Realtime/scoring-span.png?w=1100&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=e7e059759a7984f89ac856246bb86cf8 1100w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/Realtime/scoring-span.png?w=1650&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=1d5351445a5915960dc17e06f15fa7a5 1650w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/Realtime/scoring-span.png?w=2500&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=66c54aa9824678d8c082538e78739b06 2500w" />

This particular function call was scored a 0. But if we take a closer look at the logs, we can see that the question was actually answered pretty well.
You may notice this pattern for other logs as well - so is our function actually not performing well?

## Improving your evals

There are three main ways to improve your evals:

* Refine the scoring function to ensure it accurately reflects the success criteria.
* Add new scoring functions to capture different performance aspects (for example, correctness or efficiency).
* Expand your dataset with more diverse or challenging test cases.

In this case, we need to be more precise about what we're testing for in our scoring function. In our application, we're asking for answers within the specific context of Braintrust, but our current scoring function is attempting to judge the responses to our questions objectively.

Let's edit our scoring function to test for that as precisely as possible.

### Improving our existing scorer

Let's change the prompt for our scoring function to:

```javascript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
Consider the following question from an existing Braintrust user:

{{input.arguments.query}}

and answer:

{{output}}

How helpful is the answer, assuming the question is always in the context of Braintrust?
a) Very helpful
b) Reasonably helpful
c) Not helpful
```

As you continue to iterate on your scoring function and generate more logs, you should aim to see your scores go up.

<img src="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/Realtime/logs-over-time.png?fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=b1170633c65b5a4b35f1ed44c365c62f" alt="Logs over time" data-og-width="2808" width="2808" data-og-height="2016" height="2016" data-path="cookbook/assets/Realtime/logs-over-time.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/Realtime/logs-over-time.png?w=280&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=fd5792d7b48dc392afbc6fff49742d81 280w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/Realtime/logs-over-time.png?w=560&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=b5b60d6684eaa96d632a79263d8fd13f 560w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/Realtime/logs-over-time.png?w=840&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=1819eb61edc33642a5ae305ce9b4cc0f 840w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/Realtime/logs-over-time.png?w=1100&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=744fe19312f4a16de2077ba926fbd02c 1100w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/Realtime/logs-over-time.png?w=1650&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=23b99b9fa7d0563f77686615bdcaf092 1650w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/Realtime/logs-over-time.png?w=2500&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=dc971a084c0fe7e58e6f9a2ba930de14 2500w" />

## What's next

As you continue to build more AI applications with complex function calls and new APIs, it's important to continuously improve both your AI application and your evaluation process. Here are some resources to help you do just that:

* [I ran an eval. Now what?](https://braintrust.dev/blog/after-evals)
* [What to do when a new AI model comes out](https://braintrust.dev/blog/new-model)

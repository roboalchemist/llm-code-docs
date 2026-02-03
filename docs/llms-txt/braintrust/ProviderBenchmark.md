# Source: https://braintrust.dev/docs/cookbook/recipes/ProviderBenchmark.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Benchmarking inference providers

<div className="text-sm">[Contributed](https://github.com/braintrustdata/braintrust-cookbook/blob/main/examples/ProviderBenchmark/ProviderBenchmark.ipynb) by [Ankur Goyal](https://twitter.com/ankrgyl) on 2024-07-29</div>

Although there are a small handful of open-source LLMs, there are a variety of inference providers that can host them for you, each with different cost,
speed, and as we'll see below, accuracy trade-offs. And even if one provider excels at a certain model size, it may not be the best choice for another.

## Key takeaways

It's very important to evaluate your specific use case against a variety of both models and providers to make an informed decision about which to use.
What I learned is that the results are pretty unpredictable and vary across both provider and model size. Just because one provider has a good 8b model,
doesn't mean that its 405b is fast or accurate.

Here are some things that surprised me:

* **8b models are consistently fast, but have high variance in accuracy**
* **One provider is fastest for 8b and 70b, yet slowest for 405b**
* **The best provider is different across the two benchmarks we ran**

Hopefully this analysis will help you create your own benchmarks and make an informed decision about which provider to use.

## Setup

Before you get started, make sure you have a [Braintrust account](https://www.braintrust.dev/signup) and API keys for all the providers you want to test. Here, we're testing [Together](https://www.together.ai), [Fireworks](https://fireworks.ai/), and [Lepton](https://www.lepton.ai/), although Braintrust supports several others (including Azure, Bedrock, Groq, and more).

Make sure to plug each provider's API key into your Braintrust account's [AI secrets](https://www.braintrust.dev/app/settings?subroute=secrets) configuration and acquire a [`BRAINTRUST_API_KEY`](https://www.braintrust.dev/app/settings?subroute=api-keys).

Put your `BRAINTRUST_API_KEY` in a `.env.local` file next to this notebook, or just hardcode it into the code below.

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import dotenv from "dotenv";
import * as fs from "fs";

if (fs.existsSync(".env.local")) {
  dotenv.config({ path: ".env.local", override: true });
}
```

### Task code

We are going to reuse the task function from [Tool calls in LLaMa 3.1](https://www.braintrust.dev/docs/cookbook/recipes/LLaMa-3_1-Tools), which is below. For a detailed explanation of the task, see that recipe.

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import { OpenAI } from "openai";
import { wrapOpenAI } from "braintrust";

import { templates } from "autoevals";
import * as yaml from "js-yaml";
import mustache from "mustache";

const client = wrapOpenAI(
  new OpenAI({
    apiKey: process.env.BRAINTRUST_API_KEY,
    baseURL: "https://api.braintrust.dev/v1/proxy",
    defaultHeaders: { "x-bt-use-cache": "never" },
  })
);

function parseToolResponse(response: string) {
  const functionRegex = /<function=(\w+)>(.*?)(?:<\/function>|$)/;
  const match = response.match(functionRegex);

  if (match) {
    const [, functionName, argsString] = match;
    try {
      const args = JSON.parse(argsString);
      return {
        functionName,
        args,
      };
    } catch (error) {
      console.error("Error parsing function arguments:", error);
      return null;
    }
  }

  return null;
}

const template = yaml.load(templates["factuality"]);

const selectTool = {
  name: "select_choice",
  description: "Call this function to select a choice.",
  parameters: {
    properties: {
      reasons: {
        description:
          "Write out in a step by step manner your reasoning to be sure that your conclusion is correct. Avoid simply stating the correct answer at the outset.",
        title: "Reasoning",
        type: "string",
      },
      choice: {
        description: "The choice",
        title: "Choice",
        type: "string",
        enum: Object.keys(template.choice_scores),
      },
    },
    required: ["reasons", "choice"],
    title: "CoTResponse",
    type: "object",
  },
};

async function LLaMaFactuality({
  model,
  input,
  output,
  expected,
}: {
  model: string;
  input: string;
  output: string;
  expected: string;
}) {
  const toolPrompt = `You have access to the following functions:

Use the function '${selectTool.name}' to '${selectTool.description}':
${JSON.stringify(selectTool)}

If you choose to call a function ONLY reply in the following format with no prefix or suffix:

<function=example_function_name>{"example_name": "example_value"}</function>

Reminder:
- If looking for real time information use relevant functions before falling back to brave_search
- Function calls MUST follow the specified format, start with <function= and end with </function>
- Required parameters MUST be specified
- Only call one function at a time
- Put the entire function call reply on one line

Here are a few examples:

`;

  const response = await client.chat.completions.create({
    model,
    messages: [
      {
        role: "system",
        content: toolPrompt,
      },
      {
        role: "user",
        content: mustache.render(template.prompt, {
          input,
          output,
          expected,
        }),
      },
    ],
    temperature: 0,
    max_tokens: 2048,
  });

  try {
    const parsed = parseToolResponse(response.choices[0].message.content);
    return {
      name: "Factuality",
      score: template.choice_scores[parsed?.args.choice],
      metadata: {
        rationale: parsed?.args.reasons,
        choice: parsed?.args.choice,
      },
    };
  } catch (e) {
    return {
      name: "Factuality",
      score: -1,
      metadata: {
        error: `${e}`,
      },
    };
  }
}

console.log(
  await LLaMaFactuality({
    model: "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
    input: "What is the weather in Tokyo?",
    output: "The weather in Tokyo is scorching.",
    expected: "The weather in Tokyo is extremely hot.",
  })
);
```

```
(node:12633) [DEP0040] DeprecationWarning: The \`punycode\` module is deprecated. Please use a userland alternative instead.
(Use \`node --trace-deprecation ...\` to show where the warning was created)
```

```
{
  name: 'Factuality',
  score: 0.6,
  metadata: {
    rationale: "The submitted answer 'The weather in Tokyo is scorching' is a superset of the expert answer 'The weather in Tokyo is extremely hot' because it includes the same information and adds more detail. The word 'scorching' is a synonym for 'extremely hot', so the submitted answer is fully consistent with the expert answer.",
    choice: 'B'
  }
}
```

### Dataset

We'll use the same data as well: a subset of the [CoQA](https://stanfordnlp.github.io/coqa/) dataset.

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
interface CoqaCase {
  input: {
    input: string;
    output: string;
    expected: string;
  };
  expected: number;
}

const data: CoqaCase[] = JSON.parse(
  fs.readFileSync("../LLaMa-3_1-Tools/coqa-factuality.json", "utf-8")
);

console.log("LLaMa-3.1-8B Factuality");
console.log(
  await LLaMaFactuality({
    model: "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
    ...data[1].input,
  })
);
```

```
LLaMa-3.1-8B Factuality
{
  name: 'Factuality',
  score: 0,
  metadata: {
    rationale: "The submitted answer 'in a barn' does not contain the word 'white' which is present in the expert answer. Therefore, it is not a subset or superset of the expert answer. The submitted answer also does not contain all the same details as the expert answer. There is a disagreement between the submitted answer and the expert answer.",
    choice: 'D'
  }
}
```

## Running evals

Let's create a list of the providers we want to evaluate. Each provider conveniently names its flavor of each model slightly differently, so we can use these as a unique identifier.

To facilitate this test, we also self-hosted an official Meta-LLaMa-3.1-405B-Instruct-FP8 model, which is available on [Hugging Face](https://huggingface.co/meta-llama/Meta-Llama-3.1-405B-Instruct-FP8) using [vLLM](https://vllm.readthedocs.io/en/latest/). You can configure this model as a custom endpoint in Braintrust to use it alongside other providers.

### Provider map

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
const providers = [
  {
    provider: "Provider 1",
    models: [
      "accounts/fireworks/models/llama-v3p1-8b-instruct",
      "accounts/fireworks/models/llama-v3p1-70b-instruct",
      "accounts/fireworks/models/llama-v3p1-405b-instruct",
    ],
  },
  {
    provider: "Provider 2",
    models: [
      "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
      "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
      "meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo",
    ],
  },
  {
    provider: "Provider 3",
    models: ["llama3-1-8b", "llama3-1-70b", "llama3-1-405b"],
  },
  {
    provider: "Self-hosted vLLM",
    models: ["meta-llama/Meta-Llama-3.1-405B-Instruct-FP8"],
  },
];
```

### Eval code

We'll run each provider in parallel, and within the provider, we'll run each model in parallel. This roughly assumes that rate limits are per model, not per provider.

We're also running with a low concurrency level (3) to avoid overwhelming a provider and hitting rate limits. The [Braintrust proxy](/deploy/ai-proxy) handles rate limits for us, but they are reflected in the final task duration.

You'll also notice that we parse and track the provider as well as the model in each experiment's metadata. This allows us to do some rich analysis on the results.

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import { Eval } from "braintrust";
import { Score, NumericDiff } from "autoevals";

function NonNull({ output }: { output: number | null }) {
  return output !== null && output !== undefined ? 1 : 0;
}

async function CorrectScore({
  output,
  expected,
}: {
  output: number | null;
  expected: number | null;
}): Promise<Score> {
  if (output === null || expected === null) {
    return {
      name: "CorrectScore",
      score: 0,
      metadata: {
        error: output === null ? "output is null" : "expected is null",
      },
    };
  }
  return {
    ...(await NumericDiff({ output, expected })),
    name: "CorrectScore",
  };
}

async function runProviderBenchmark(provider: (typeof providers)[number]) {
  const evals = [];
  for (const model of provider.models) {
    const size = model.toLowerCase().includes("8b")
      ? "8b"
      : model.toLowerCase().includes("70b")
        ? "70b"
        : "405b";

    evals.push(
      Eval("LLaMa-3.1-Multi-Provider-Benchmark", {
        data: data,
        task: async (input) =>
          (await LLaMaFactuality({ model, ...input }))?.score,
        scores: [CorrectScore, NonNull],
        metadata: {
          size,
          provider: provider.provider,
          model,
        },
        experimentName: `${provider.provider} (${size})`,
        maxConcurrency: 3,
        trialCount: 3,
      })
    );
  }
  await Promise.all(evals);
}

await Promise.all(providers.map(runProviderBenchmark));
```

## Results

Let's start by looking at the project view. Braintrust makes it easy to morph this into a multi-level grouped analysis where we can see the score vs. duration in a scatter plot, and how each provider stacks up in the table.

<img src="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ProviderBenchmark/configuring-graph.gif?s=f64e21acab41fb75f49105cc62750853" alt="Setting up the table" data-og-width="800" width="800" data-og-height="713" height="713" data-path="cookbook/assets/ProviderBenchmark/configuring-graph.gif" data-optimize="true" data-opv="3" />

### Insights

Now let's dig into this chart and see what we can learn.

1. **70b hits a nice sweet spot**

It looks like on average, each weight class costs you an extra second on average. However, the jump in average accuracy from 8b to 70b is 16%+ while
70b to 405b is only 2.87%.

<img src="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ProviderBenchmark/aggregate-tradeoff.png?fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=71ca1e4b2b66985e69ef2c6dcaab9ef3" alt="Pivot table" data-og-width="714" width="714" data-og-height="215" height="215" data-path="cookbook/assets/ProviderBenchmark/aggregate-tradeoff.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ProviderBenchmark/aggregate-tradeoff.png?w=280&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=3f302b63fad6db5526d284936dfa35fb 280w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ProviderBenchmark/aggregate-tradeoff.png?w=560&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=75a406b2a613a712ba56867599f4f65c 560w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ProviderBenchmark/aggregate-tradeoff.png?w=840&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=373e2093a7c1fb92957f5a0edb86cbe3 840w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ProviderBenchmark/aggregate-tradeoff.png?w=1100&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=d87f48b31e5c881a4fa8eb014b33da8b 1100w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ProviderBenchmark/aggregate-tradeoff.png?w=1650&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=a94e04a09cde70860a89b0be91a0a57b 1650w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ProviderBenchmark/aggregate-tradeoff.png?w=2500&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=e15865a6c7229e6f8a8f836309abda72 2500w" />

2. **8b models are consistently really fast, but some providers' 70b models are slower than others'**

The distribution among providers for 8b latency is very tight, but that starts to change with 70b and even more so with 405b models.

<img src="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ProviderBenchmark/speed-variance.png?fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=e1f279507610f8cfbb3b23634d02583a" alt="Speed distribution" data-og-width="1039" width="1039" data-og-height="287" height="287" data-path="cookbook/assets/ProviderBenchmark/speed-variance.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ProviderBenchmark/speed-variance.png?w=280&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=3a1f59a220113aada07cef1881f56ce0 280w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ProviderBenchmark/speed-variance.png?w=560&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=44e8b0a73df93b0bf7ca258aa9082f8d 560w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ProviderBenchmark/speed-variance.png?w=840&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=c0db4dead98270eb654582f6f6e97591 840w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ProviderBenchmark/speed-variance.png?w=1100&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=4961712cae32753f0a11ba8593fbf1d7 1100w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ProviderBenchmark/speed-variance.png?w=1650&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=7823e3395e3382c7f94b08ba49693e81 1650w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ProviderBenchmark/speed-variance.png?w=2500&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=215db8c469477ef69d41b00fcd638a4c 2500w" />

3. **High accuracy variance in 8b models**

Within 8b models in particular, there is a pretty significant difference in accuracy

<img src="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ProviderBenchmark/performance-variance-8b.png?fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=70c6b142cf3bc3abfe97b7fba2428a30" alt="Accuracy distribution" data-og-width="705" width="705" data-og-height="166" height="166" data-path="cookbook/assets/ProviderBenchmark/performance-variance-8b.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ProviderBenchmark/performance-variance-8b.png?w=280&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=d6cea42f99c12e518b0125b8c42ba081 280w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ProviderBenchmark/performance-variance-8b.png?w=560&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=a2387054ce31998e904883750818f41c 560w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ProviderBenchmark/performance-variance-8b.png?w=840&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=b6e3b9791fd67408bfebf0ac5f01b717 840w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ProviderBenchmark/performance-variance-8b.png?w=1100&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=e38e5635b7db263877e3a235ed9ea95b 1100w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ProviderBenchmark/performance-variance-8b.png?w=1650&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=379698008d4bca3565209017f9cf0d44 1650w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ProviderBenchmark/performance-variance-8b.png?w=2500&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=c11f36ddcb6879badd36713dcb3a3308 2500w" />

4. **Provider 1 is the fastest except for 405b**

<img src="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ProviderBenchmark/provider-1-insight.png?fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=43543238c4af2028db3947db8884cfbe" alt="Provider 1" data-og-width="931" width="931" data-og-height="242" height="242" data-path="cookbook/assets/ProviderBenchmark/provider-1-insight.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ProviderBenchmark/provider-1-insight.png?w=280&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=5049897185c264d40d2078a73f3fa1d9 280w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ProviderBenchmark/provider-1-insight.png?w=560&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=da3d791c4ba72601e48f2e6c779a2467 560w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ProviderBenchmark/provider-1-insight.png?w=840&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=28e5f647b6966a764d5479facef4f396 840w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ProviderBenchmark/provider-1-insight.png?w=1100&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=ec0c4a42736d47973b861ed374b14e2d 1100w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ProviderBenchmark/provider-1-insight.png?w=1650&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=e985142efbe5d37e0c535ffd434207b3 1650w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ProviderBenchmark/provider-1-insight.png?w=2500&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=3196db7418a29fc24696488d2555b567 2500w" />

Interestingly, provider 1's 8b model is both the fastest and most accurate. However, its 405b model, while accurate, is the slowest by far. This is likely due to
rate limits, or perhaps they have optimized it using a different method.

5. **Self-hosting strikes a nice balance**

Self-hosting strikes a nice balance between latency and quality (note: we only tested self-hosted 405b). Of course, this comes at a price -- around \$27/hour using [Lambda Labs](https://lambdalabs.com/)

<img src="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ProviderBenchmark/self-hosted.png?fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=1d176d5a554899a76b0679e518fce1c0" alt="Self-hosted" data-og-width="1052" width="1052" data-og-height="243" height="243" data-path="cookbook/assets/ProviderBenchmark/self-hosted.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ProviderBenchmark/self-hosted.png?w=280&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=21f5574e3e864ce74a9b096f0aa9fe2b 280w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ProviderBenchmark/self-hosted.png?w=560&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=287fbc8cf9e748bf257ac99798e6bd58 560w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ProviderBenchmark/self-hosted.png?w=840&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=80fc6037565b8cfccdc50b90c38cfe04 840w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ProviderBenchmark/self-hosted.png?w=1100&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=af46ea264399ffd50578b8bf71cdd169 1100w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ProviderBenchmark/self-hosted.png?w=1650&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=1a14b7cb27d3e5e25b8389dcb775d105 1650w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ProviderBenchmark/self-hosted.png?w=2500&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=4782140b13512bdf2dbcc9ddfae70faa 2500w" />

### Another benchmark

We also used roughly the same code on a different, more-realistic, internal benchmark which measures how well our [AI search](https://www.braintrust.dev/docs/cookbook/recipes/AISearch) bar works. Here is the same
visualization for that benchmark:

<img src="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ProviderBenchmark/ai-search.png?fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=be53a3583d797600182a0bdcdfe18a21" alt="AISearch" data-og-width="1500" width="1500" data-og-height="950" height="950" data-path="cookbook/assets/ProviderBenchmark/ai-search.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ProviderBenchmark/ai-search.png?w=280&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=ee2f52c39f234194c414bb8b8e03c89e 280w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ProviderBenchmark/ai-search.png?w=560&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=cc75109b5787ac99b281e1ec94ff40d0 560w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ProviderBenchmark/ai-search.png?w=840&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=29e6aab707de356f75b8e086c5e05fbb 840w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ProviderBenchmark/ai-search.png?w=1100&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=c90c90ef6c557bb5b52cdf71dc100769 1100w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ProviderBenchmark/ai-search.png?w=1650&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=5ff306364cf92bd56605c6662dfb89b1 1650w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ProviderBenchmark/ai-search.png?w=2500&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=90bcadcebaf74c1035e3f7c5ac1243e3 2500w" />

As you can see, certain things are consistent, but others are not. Again, this highlights how important it is to run this analysis on your own use case.

* **Provider 1 is less differentiated**. Although Provider 1 is still the fastest, it comes at the cost of accuracy in the 70b and 405b classes, where Provider 2 wins on accuracy. Provider 2 also wins on speed for 405b.
* **Provider 3 has a hard time in the 70b class**. This workload is heavy on prompt tokens (\~3500 per test case). Maybe that has something to do with it?
* **More latency variance across the board**. Again, this may have to do with the significant jump in prompt tokens.
* **Self-hosted seems to be about the same**. Interestingly, the self-hosted model appears at about the same spot in the graph!

## Where to go from here

This is just one benchmark, but as you can see, there is a pretty significant difference in speed and accuracy between providers. I'd highly encourage testing
on your own workload and using a tool like [Braintrust](https://www.braintrust.dev) to help you construct a good eval and understand the trade-offs across providers
in depth.

Feel free to [reach out](mailto:support@braintrust.dev) if we can help, or feel free to [sign up](https://www.braintrust.dev/signup) to try out Braintrust for yourself.
If you enjoy performing this kind of analysis, we are [hiring](https://www.braintrust.dev/careers).

Happy evaluating!

*Thanks to [Hamel](https://x.com/HamelHusain) for hosting the self-hosted model and feedback on drafts.*

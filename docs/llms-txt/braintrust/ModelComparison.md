# Source: https://braintrust.dev/docs/cookbook/recipes/ModelComparison.md

# Comparing evals across multiple AI models

<div className="text-sm">[Contributed](https://github.com/braintrustdata/braintrust-cookbook/blob/main/examples/ModelComparison/ModelComparison.ipynb) by [John Huang](https://www.linkedin.com/in/j13huang/) on 2024-05-22</div>

This tutorial will teach you how to use Braintrust to compare the same prompts across different AI models and parameters to help decide on choosing a model to run your AI apps.

Before starting, please make sure that you have a Braintrust account. If you do not, please [sign up](https://www.braintrustdata.com). After this tutorial, feel free to dig deeper by visiting [the docs](http://www.braintrustdata.com/docs).

## Installing dependencies

To see a list of dependencies, you can view the accompanying [package.json](https://github.com/braintrustdata/braintrust-cookbook/tree/main/examples/ModelComparison/package.json) file. Feel free to copy/paste snippets of this code to run in your environment, or use [tslab](https://github.com/yunabe/tslab) to run the tutorial in a Jupyter notebook.

## Setting up the data

For this example, we will use a small subset of data taken from the [google/boolq](https://huggingface.co/datasets/google/boolq) dataset. If you'd like, you can try datasets and prompts from any of the other [cookbooks](https://www.braintrustdata.com/docs/cookbook/) at Braintrust.

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
// curl -X GET "https://datasets-server.huggingface.co/rows?dataset=google%2Fboolq&config=default&split=train&offset=500&length=5" > ./assets/dataset.json
import dataset from "./assets/dataset.json";

// labels these 1-3 so that they will be easier to recognize in the app
const prompts = [
  "(1) - true or false",
  "(2) - Answer using true or false only",
  "(3) - Answer the following question as accurately as possible with the words 'true' or 'false' in lowercase only. Do not include any other words in the response",
];

// extract question/answers from rows into input/expected
const evalData = dataset.rows.map(({ row: { question, answer } }) => ({
  input: question,
  expected: `${answer}`,
}));
console.log(evalData);
```

```
[
  {
    input: 'do you have to have two license plates in ontario',
    expected: 'true'
  },
  {
    input: 'are black beans the same as turtle beans',
    expected: 'true'
  },
  {
    input: 'is a wooly mammoth the same as a mastodon',
    expected: 'false'
  },
  {
    input: 'is carling black label a south african beer',
    expected: 'false'
  },
  {
    input: 'were the world trade centers the tallest buildings in america',
    expected: 'true'
  }
]
```

## Running comparison evals across multiple models

Let's set up some code to compare these prompts and inputs across 3 different models and different temperature values. For this cookbook we will be using [Braintrust's LLM proxy](https://www.braintrustdata.com/docs/guides/proxy) to access the API for different models.

All we need to do is provide a `baseURL` to the proxy with the relevant API key that we want to access, and the use the `wrapOpenAI` function from braintrust which will help us capture helpful debugging information about each model's performance while keeping the same SDK interface across all models.

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import { wrapOpenAI } from "braintrust";
import { OpenAI } from "openai";

async function callModel(
  input: string,
  {
    model,
    apiKey,
    temperature,
    systemPrompt,
  }: {
    model: string;
    apiKey: string;
    temperature: number;
    systemPrompt: string;
  }
) {
  const client = wrapOpenAI(
    new OpenAI({
      baseURL: "https://api.braintrust.dev/v1/proxy",
      apiKey, // Can use OpenAI, Anthropic, Mistral etc. API keys here
    })
  );

  const response = await client.chat.completions.create({
    model: model,
    messages: [
      {
        role: "system",
        content: systemPrompt,
      },
      {
        role: "user",
        content: input,
      },
    ],
    temperature,
    seed: 123,
  });
  return response.choices[0].message.content || "";
}
```

Then we will set up our eval data for each combination of model, prompt and temperature.

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
const combinations: {
  model: { name: string; apiKey: string };
  temperature: number;
  prompt: string;
}[] = [];
for (const model of [
  {
    name: "claude-3-opus-20240229",
    apiKey: process.env.ANTHROPIC_API_KEY ?? "",
  },
  {
    name: "claude-3-haiku-20240307",
    apiKey: process.env.ANTHROPIC_API_KEY ?? "",
  },
  { name: "gpt-4", apiKey: process.env.OPENAI_API_KEY ?? "" },
  { name: "gpt-4o", apiKey: process.env.OPENAI_API_KEY ?? "" },
]) {
  for (const temperature of [0, 0.25, 0.5, 0.75, 1]) {
    for (const prompt of prompts) {
      combinations.push({
        model,
        temperature,
        prompt,
      });
    }
  }
}

[process.env.ANTHROPIC_API_KEY, process.env.OPENAI_API_KEY].forEach(
  (v, i) => !v && console.warn(i, "API key not set")
);
// don't log API keys
console.log(
  combinations.slice(0, 5).map(({ model: { name }, temperature, prompt }) => ({
    model: name,
    temperature,
    prompt,
  }))
);
```

```
[
  {
    model: 'claude-3-opus-20240229',
    temperature: 0,
    prompt: '(1) - true or false'
  },
  {
    model: 'claude-3-opus-20240229',
    temperature: 0,
    prompt: '(2) - Answer using true or false only'
  },
  {
    model: 'claude-3-opus-20240229',
    temperature: 0,
    prompt: "(3) - Answer the following question as accurately as possible with the words 'true' or 'false' in lowercase only. Do not include any other words in the response"
  },
  {
    model: 'claude-3-opus-20240229',
    temperature: 0.25,
    prompt: '(1) - true or false'
  },
  {
    model: 'claude-3-opus-20240229',
    temperature: 0.25,
    prompt: '(2) - Answer using true or false only'
  }
]
```

Let's use the functions and data that we have set up to run some evals on Braintrust! We will be using two scorers for this eval:

1. A simple exact match scorer that will compare the output from the LLM exactly with the expected value
2. A Levenshtein scorer which will calculate the Levenshtein distance between the LLM output and our expected value

We are also adding the model, temperature, and prompt into the metadata so that we can use those fields to help our visualization inside the braintrust app after the evals are finished running.

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import { Eval } from "braintrust";
import { Levenshtein } from "autoevals";

const exactMatch = (args: { input; output; expected? }) => {
  return {
    name: "ExactMatch",
    score: args.output === args.expected ? 1 : 0,
  };
};

await Promise.all(
  combinations.map(async ({ model, temperature, prompt }) => {
    Eval("Model comparison", {
      data: () =>
        evalData.map(({ input, expected }) => ({
          input,
          expected,
        })),
      task: async (input) => {
        return await callModel(input, {
          model: model.name,
          apiKey: model.apiKey,
          temperature,
          systemPrompt: prompt,
        });
      },
      scores: [exactMatch, Levenshtein],
      metadata: {
        model: model.name,
        temperature,
        prompt,
      },
    });
  })
);
```

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
 ████████████████████████████████████████ | Model comparison                         | 100% | 5/5 datapoints

=========================SUMMARY=========================
main-1716504446-539a4a27 compared to main-1716504446-c81946d8:
52.00% ''Levenshtein'' score    (0 improvements, 0 regressions)
40.00% ''ExactMatch' ' score    (0 improvements, 0 regressions)

5.06s 'duration'        (0 improvements, 0 regressions)

See results for main-1716504446-539a4a27 at https://www.braintrust.dev/app/braintrustdata.com/p/Model%20comparison/experiments/main-1716504446-539a4a27


=========================SUMMARY=========================
main-1716504446-44ef0250 compared to main-1716504446-75fa02ea:
0.00% ''ExactMatch' ' score     (0 improvements, 0 regressions)
1.43% ''Levenshtein'' score     (0 improvements, 0 regressions)

1.05s 'duration'        (0 improvements, 0 regressions)

See results for main-1716504446-44ef0250 at https://www.braintrust.dev/app/braintrustdata.com/p/Model%20comparison/experiments/main-1716504446-44ef0250
```

## Visualizing

Now we have successfully run our evals! Let's log onto [braintrust.dev](https://braintrust.dev) and take a look at the results.

Click into the newly generated project called `Model comparison`, and check it out! You should notice a few things:

<img src="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ModelComparison/initial-chart.png?fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=7ee79669e207e83df39950e490ef6def" alt="initial-chart" data-og-width="1490" width="1490" data-og-height="445" height="445" data-path="cookbook/assets/ModelComparison/initial-chart.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ModelComparison/initial-chart.png?w=280&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=569adb66408b0916753ef9137e32e99f 280w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ModelComparison/initial-chart.png?w=560&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=ffe364b6591574cf7fe2639eb77bf7b1 560w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ModelComparison/initial-chart.png?w=840&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=0880fbc7e77f03f7c09f924f129e5137 840w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ModelComparison/initial-chart.png?w=1100&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=cdde7c46d60221dca730f449faaebb04 1100w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ModelComparison/initial-chart.png?w=1650&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=1873b46ad2796033931ef5956d0a7efa 1650w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ModelComparison/initial-chart.png?w=2500&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=7fd3b7915fa22802d8360bc5ca4e0a37 2500w" />

* Each line represents a score over time, and each data point represents an experiment that was run.
  * From the code, we ran 60 experiments (5 temperature values x 4 models x 3 prompts) so one line should consist of 60 dots, each with a different combination of temperature, model, and prompt.
* Metadata fields are automatically populated as viable X axis values.
* Metadata fields with numeric values are automatically populated as viable Y axis values.

<img src="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ModelComparison/initial-chart-x-axis.png?fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=1e63c4bffa0b1ee4e57f13336e982b54" alt="initial-chart-temperature" data-og-width="1477" width="1477" data-og-height="553" height="553" data-path="cookbook/assets/ModelComparison/initial-chart-x-axis.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ModelComparison/initial-chart-x-axis.png?w=280&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=78ec0cf58ff5e3079b550c314e1acc80 280w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ModelComparison/initial-chart-x-axis.png?w=560&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=97eea0811c7966db1e696912b909d9fd 560w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ModelComparison/initial-chart-x-axis.png?w=840&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=621c61e562d0761354707c893306923f 840w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ModelComparison/initial-chart-x-axis.png?w=1100&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=141dc8916f20a3c4aebd516f686eeea9 1100w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ModelComparison/initial-chart-x-axis.png?w=1650&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=dcf733a00708609f80b1f29b45aa1bb6 1650w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ModelComparison/initial-chart-x-axis.png?w=2500&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=5f5e6a5c1de49a1340a18eb2a42b4685 2500w" />

## Diving in

This chart allows us to also group data to allow us to compare experiment runs by model, prompt, and temperature.

By selecting `X Axis prompt`, we can see pretty clearly that the longer prompt performed better than the shorter ones.

<img src="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ModelComparison/group-by-prompt.png?fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=58dcb3becef2752414ac9965d5bc13da" alt="grouped-chart" data-og-width="1478" width="1478" data-og-height="456" height="456" data-path="cookbook/assets/ModelComparison/group-by-prompt.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ModelComparison/group-by-prompt.png?w=280&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=b0fcea000688a4d100f58ea3eb03fdb4 280w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ModelComparison/group-by-prompt.png?w=560&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=1b69b7b5977f924b415bf0b01d427027 560w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ModelComparison/group-by-prompt.png?w=840&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=b194c21a18ba87611154bb0bc34678df 840w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ModelComparison/group-by-prompt.png?w=1100&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=b4ad5818051025cc976ac76a5afd4657 1100w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ModelComparison/group-by-prompt.png?w=1650&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=03f86059908a40588196d7b33ababf79 1650w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ModelComparison/group-by-prompt.png?w=2500&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=ec01cc3401399f867b747077e82d9b47 2500w" />

By selecting the `one color per model` and `X Axis model`, we can also visualize performance between different models. From this view we can see that the OpenAI models outperformed the Anthropic models.

<img src="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ModelComparison/group-by-model.png?fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=e7699229705e6eb8e3cb37a92b2aeeae" alt="grouped-chart" data-og-width="1480" width="1480" data-og-height="458" height="458" data-path="cookbook/assets/ModelComparison/group-by-model.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ModelComparison/group-by-model.png?w=280&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=3607567ab6a1067b950750b90b036d48 280w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ModelComparison/group-by-model.png?w=560&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=02c4936a73b3e4474826c8f590078c68 560w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ModelComparison/group-by-model.png?w=840&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=f48a1ce4b5d89e35e2e24afd4940e9bd 840w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ModelComparison/group-by-model.png?w=1100&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=0ebf16799c1a814db718cd2608eb7b73 1100w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ModelComparison/group-by-model.png?w=1650&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=2274ae64ead5420978c2d8311ad002e2 1650w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ModelComparison/group-by-model.png?w=2500&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=a82599804a75ba43d58e0ff033113664 2500w" />

Let's see if we can find any differences between the OpenAI models by selecting the `one color per model`, `one symbol per prompt`, and `X Axis temperature`.

<img src="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ModelComparison/grouped-chart.png?fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=0ca1226708aa4e8dec34a99e4806ef46" alt="grouped-chart" data-og-width="1473" width="1473" data-og-height="448" height="448" data-path="cookbook/assets/ModelComparison/grouped-chart.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ModelComparison/grouped-chart.png?w=280&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=2223a67fdfb6bd7bcb6560ce108db1c4 280w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ModelComparison/grouped-chart.png?w=560&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=af95d61c71236eeabd23f015c391410b 560w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ModelComparison/grouped-chart.png?w=840&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=88872b49cf26165d24ce94efd5dd6f56 840w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ModelComparison/grouped-chart.png?w=1100&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=e7e24d5c762faedb228490847024048c 1100w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ModelComparison/grouped-chart.png?w=1650&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=55f83a83974510c6c6b2071709e1feb1 1650w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/ModelComparison/grouped-chart.png?w=2500&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=bc2842c1fe89e0b6170bfe49e7860793 2500w" />

In this view, we can see that `gpt-4` performed better than `gpt-4o` at higher temperatures!

## Parting thoughts

This is just the start of evaluating and improving your AI applications. From here, you should run more experiments with larger datasets, and also try out different prompts! Once you have run another set of experiments, come back to the chart and play with the different views and groupings. You can also add filtering to filter for experiments with specific scores and metadata to find even more insights.

Happy evaluating!


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt
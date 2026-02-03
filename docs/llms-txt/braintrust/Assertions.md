# Source: https://braintrust.dev/docs/cookbook/recipes/Assertions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How Zapier uses assertions to evaluate tool usage in chatbots

<div className="text-sm">[Contributed](https://github.com/braintrustdata/braintrust-cookbook/blob/main/examples/Assertions/Assertions.ipynb) by [Vítor Balocco](https://twitter.com/vitorbal) on 2024-02-13</div>

[Zapier](https://zapier.com/) is the #1 workflow automation platform for small and midsize businesses, connecting to more than 6000 of the most popular work apps. We were also one of the first companies to build and ship AI features into our core products. We've had the opportunity to work with Braintrust since the early days of the product, which now powers the evaluation and observability infrastructure across our AI features.

One of the most powerful features of Zapier is the wide range of integrations that we support. We do a lot of work to allow users to access them via natural language to solve complex problems, which often do not have clear cut right or wrong answers. Instead, we define a set of criteria that need to be met (assertions). Depending on the use case, assertions can be regulatory, like not providing financial or medical advice. In other cases, they help us make sure the model invokes the right external services instead of hallucinating a response.

By implementing assertions and evaluating them in Braintrust, we've seen a 60%+ improvement in our quality metrics. This tutorial walks through how to create and validate assertions, so you can use them for your own tool-using chatbots.

## Initial setup

We're going to create a chatbot that has access to a single tool, *weather lookup*, and throw a series of questions at it. Some questions will involve the weather and others won't. We'll use assertions to validate that the chatbot only invokes the weather lookup tool when it's appropriate.

Let's create a simple request handler and hook up a weather tool to it.

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import { wrapOpenAI } from "braintrust";
import pick from "lodash/pick";
import { ChatCompletionTool } from "openai/resources/chat/completions";
import OpenAI from "openai";
import { z } from "zod";
import zodToJsonSchema from "zod-to-json-schema";

// This wrap function adds some useful tracing in Braintrust
const openai = wrapOpenAI(new OpenAI());

// Convenience function for defining an OpenAI function call
const makeFunctionDefinition = (
  name: string,
  description: string,
  schema: z.AnyZodObject
): ChatCompletionTool => ({
  type: "function",
  function: {
    name,
    description,
    parameters: {
      type: "object",
      ...pick(
        zodToJsonSchema(schema, {
          name: "root",
          $refStrategy: "none",
        }).definitions?.root,
        ["type", "properties", "required"]
      ),
    },
  },
});

const weatherTool = makeFunctionDefinition(
  "weather",
  "Look up the current weather for a city",
  z.object({
    city: z.string().describe("The city to look up the weather for"),
    date: z.string().optional().describe("The date to look up the weather for"),
  })
);

// This is the core "workhorse" function that accepts an input and returns a response
// which optionally includes a tool call (to the weather API).
async function task(input: string) {
  const completion = await openai.chat.completions.create({
    model: "gpt-3.5-turbo",
    messages: [
      {
        role: "system",
        content: `You are a highly intelligent AI that can look up the weather.`,
      },
      { role: "user", content: input },
    ],
    tools: [weatherTool],
    max_tokens: 1000,
  });

  return {
    responseChatCompletions: [completion.choices[0].message],
  };
}
```

Now let's try it out on a few examples!

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
JSON.stringify(await task("What's the weather in San Francisco?"), null, 2);
```

```
{
  "responseChatCompletions": [
    {
      "role": "assistant",
      "content": null,
      "tool_calls": [
        {
          "id": "call_vlOuDTdxGXurjMzy4VDFHGBS",
          "type": "function",
          "function": {
            "name": "weather",
            "arguments": "{\n  \"city\": \"San Francisco\"\n}"
          }
        }
      ]
    }
  ]
}
```

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
JSON.stringify(await task("What is my bank balance?"), null, 2);
```

```
{
  "responseChatCompletions": [
    {
      "role": "assistant",
      "content": "I'm sorry, but I can't provide you with your bank balance. You will need to check with your bank directly for that information."
    }
  ]
}
```

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
JSON.stringify(await task("What is the weather?"), null, 2);
```

```
{
  "responseChatCompletions": [
    {
      "role": "assistant",
      "content": "I need more information to provide you with the weather. Could you please specify the city and the date for which you would like to know the weather?"
    }
  ]
}
```

## Scoring outputs

Validating these cases is subtle. For example, if someone asks "What is the weather?", the correct answer is to ask for clarification. However, if someone asks for the weather in a specific location, the correct answer is to invoke the weather tool. How do we validate these different types of responses?

### Using assertions

Instead of trying to score a specific response, we'll use a technique called *assertions* to validate certain criteria about a response. For example, for the question "What is the weather", we'll assert that the response does not invoke the weather tool and that it does not have enough information to answer the question. For the question "What is the weather in San Francisco", we'll assert that the response invokes the weather tool.

### Assertion types

Let's start by defining a few assertion types that we'll use to validate the chatbot's responses.

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
type AssertionTypes =
  | "equals"
  | "exists"
  | "not_exists"
  | "llm_criteria_met"
  | "semantic_contains";

type Assertion = {
  path: string;
  assertion_type: AssertionTypes;
  value: string;
};
```

`equals`, `exists`, and `not_exists` are heuristics. `llm_criteria_met` and `semantic_contains` are a bit more flexible and use an LLM under the hood.

Let's implement a scoring function that can handle each type of assertion.

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import { ClosedQA } from "autoevals";
import get from "lodash/get";
import every from "lodash/every";

/**
 * Uses an LLM call to classify if a substring is semantically contained in a text.
 * @param text The full text you want to check against
 * @param needle The string you want to check if it is contained in the text
 */
async function semanticContains({
  text1,
  text2,
}: {
  text1: string;
  text2: string;
}): Promise<boolean> {
  const system = `
  You are a highly intelligent AI. You will be given two texts, TEXT_1 and TEXT_2. Your job is to tell me if TEXT_2 is semantically present in TEXT_1.
  Examples:
  \`\`\`
  TEXT_1: "I've just sent “hello world” to the #testing channel on Slack as you requested. Can I assist you with anything else?"
  TEXT_2: "Can I help you with something else?"
  Result: YES
  \`\`\`

  \`\`\`
  TEXT_1: "I've just sent “hello world” to the #testing channel on Slack as you requested. Can I assist you with anything else?"
  TEXT_2: "Sorry, something went wrong."
  Result: NO
  \`\`\`

  \`\`\`
  TEXT_1: "I've just sent “hello world” to the #testing channel on Slack as you requested. Can I assist you with anything else?"
  TEXT_2: "#testing channel Slack"
  Result: YES
  \`\`\`

  \`\`\`
  TEXT_1: "I've just sent “hello world” to the #testing channel on Slack as you requested. Can I assist you with anything else?"
  TEXT_2: "#general channel Slack"
  Result: NO
  \`\`\`
  `;

  const toolSchema = z.object({
    rationale: z
      .string()
      .describe(
        "A string that explains the reasoning behind your answer. It's a step-by-step explanation of how you determined that TEXT_2 is or isn't semantically present in TEXT_1."
      ),
    answer: z.boolean().describe("Your answer"),
  });

  const completion = await openai.chat.completions.create({
    model: "gpt-3.5-turbo",
    messages: [
      {
        role: "system",
        content: system,
      },
      {
        role: "user",
        content: `TEXT_1: "${text1}"\nTEXT_2: "${text2}"`,
      },
    ],
    tools: [
      makeFunctionDefinition(
        "semantic_contains",
        "The result of the semantic presence check",
        toolSchema
      ),
    ],
    tool_choice: {
      function: { name: "semantic_contains" },
      type: "function",
    },
    max_tokens: 1000,
  });

  try {
    const { answer } = toolSchema.parse(
      JSON.parse(
        completion.choices[0].message.tool_calls![0].function.arguments
      )
    );
    return answer;
  } catch (e) {
    console.error(e, "Error parsing semanticContains response");
    return false;
  }
}

const AssertionScorer = async ({
  input,
  output,
  expected: assertions,
}: {
  input: string;
  output: any;
  expected: Assertion[];
}) => {
  // for each assertion, perform the comparison
  const assertionResults: {
    status: string;
    path: string;
    assertion_type: string;
    value: string;
    actualValue: string;
  }[] = [];
  for (const assertion of assertions) {
    const { assertion_type, path, value } = assertion;
    const actualValue = get(output, path);
    let passedTest = false;

    try {
      switch (assertion_type) {
        case "equals":
          passedTest = actualValue === value;
          break;
        case "exists":
          passedTest = actualValue !== undefined;
          break;
        case "not_exists":
          passedTest = actualValue === undefined;
          break;
        case "llm_criteria_met":
          const closedQA = await ClosedQA({
            input:
              "According to the provided criterion is the submission correct?",
            criteria: value,
            output: actualValue,
          });
          passedTest = !!closedQA.score && closedQA.score > 0.5;
          break;
        case "semantic_contains":
          passedTest = await semanticContains({
            text1: actualValue,
            text2: value,
          });
          break;
        default:
          assertion_type satisfies never; // if you see a ts error here, its because your switch is not exhaustive
          throw new Error(`unknown assertion type ${assertion_type}`);
      }
    } catch (e) {
      passedTest = false;
    }
    assertionResults.push({
      status: passedTest ? "passed" : "failed",
      path,
      assertion_type,
      value,
      actualValue,
    });
  }

  const allPassed = every(assertionResults, (r) => r.status === "passed");

  return {
    name: "Assertions Score",
    score: allPassed ? 1 : 0,
    metadata: {
      assertionResults,
    },
  };
};
```

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
const data = [
  {
    input: "What's the weather like in San Francisco?",
    expected: [
      {
        path: "responseChatCompletions[0].tool_calls[0].function.name",
        assertion_type: "equals",
        value: "weather",
      },
    ],
  },
  {
    input: "What's the weather like?",
    expected: [
      {
        path: "responseChatCompletions[0].tool_calls[0].function.name",
        assertion_type: "not_exists",
        value: "",
      },
      {
        path: "responseChatCompletions[0].content",
        assertion_type: "llm_criteria_met",
        value:
          "Response reflecting the bot does not have enough information to look up the weather",
      },
    ],
  },
  {
    input: "How much is AAPL stock today?",
    expected: [
      {
        path: "responseChatCompletions[0].tool_calls[0].function.name",
        assertion_type: "not_exists",
        value: "",
      },
      {
        path: "responseChatCompletions[0].content",
        assertion_type: "llm_criteria_met",
        value:
          "Response reflecting the bot does not have access to the ability or tool to look up stock prices.",
      },
    ],
  },
  {
    input: "What can you do?",
    expected: [
      {
        path: "responseChatCompletions[0].content",
        assertion_type: "semantic_contains",
        value: "look up the weather",
      },
    ],
  },
];
```

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import { Eval } from "braintrust";

await Eval("Weather Bot", {
  data,
  task: async (input) => {
    const result = await task(input);
    return result;
  },
  scores: [AssertionScorer],
});
```

```
{
  projectName: 'Weather Bot',
  experimentName: 'HEAD-1707465445',
  projectUrl: 'https://www.braintrust.dev/app/braintrust.dev/p/Weather%20Bot',
  experimentUrl: 'https://www.braintrust.dev/app/braintrust.dev/p/Weather%20Bot/HEAD-1707465445',
  comparisonExperimentName: undefined,
  scores: undefined,
  metrics: undefined
}
```

```
 ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ | Weather Bot                              |   4% | 4/100 datapoints
```

```
{
  projectName: 'Weather Bot',
  experimentName: 'HEAD-1707465445',
  projectUrl: 'https://www.braintrust.dev/app/braintrust.dev/p/Weather%20Bot',
  experimentUrl: 'https://www.braintrust.dev/app/braintrust.dev/p/Weather%20Bot/HEAD-1707465445',
  comparisonExperimentName: undefined,
  scores: undefined,
  metrics: undefined
}
```

### Analyzing results

It looks like half the cases passed.

<img src="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/Assertions/initial-experiment.png?fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=fb9fefe255908078be31ef88ab9d76aa" alt="Initial experiment" data-og-width="2768" width="2768" data-og-height="2374" height="2374" data-path="cookbook/assets/Assertions/initial-experiment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/Assertions/initial-experiment.png?w=280&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=7ebec24e95dca35abe66e0ade33f7327 280w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/Assertions/initial-experiment.png?w=560&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=b98f1fabcbf243e31a43febdb6ced6b8 560w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/Assertions/initial-experiment.png?w=840&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=30ef2e268442f929e9bd5ff50ed5b126 840w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/Assertions/initial-experiment.png?w=1100&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=80609873b09d9c2d6dd51c231ed4c723 1100w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/Assertions/initial-experiment.png?w=1650&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=fc505c205a9262380166b960d374942e 1650w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/Assertions/initial-experiment.png?w=2500&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=c3c2996a4d536e3c9a6cca05b2be49f2 2500w" />

In one case, the chatbot did not clearly indicate that it needs more information.

<img src="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/Assertions/reason-1.png?fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=e95b4db5449c6e51d40e751dd024ecc7" alt="result-1" data-og-width="876" width="876" data-og-height="1112" height="1112" data-path="cookbook/assets/Assertions/reason-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/Assertions/reason-1.png?w=280&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=dc7366c3441dcb0a9115c6f68507603f 280w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/Assertions/reason-1.png?w=560&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=1c6cd102d419af302bc86642d3148102 560w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/Assertions/reason-1.png?w=840&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=1117ee86e9f1a3dd93b01f73178eba8c 840w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/Assertions/reason-1.png?w=1100&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=163f61809ff8a179abb605662db962d9 1100w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/Assertions/reason-1.png?w=1650&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=165583965b9c1142fd2c7d32abfb92de 1650w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/Assertions/reason-1.png?w=2500&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=fce5ab7e92c4cdad1771a6901bce1e6d 2500w" />

In the other case, the chatbot halucinated a stock tool.

<img src="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/Assertions/reason-2.png?fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=87eb29f6accd78557fad54aa64ed112c" alt="result-2" data-og-width="864" width="864" data-og-height="986" height="986" data-path="cookbook/assets/Assertions/reason-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/Assertions/reason-2.png?w=280&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=acddf036f15d68bcfdefa37be8b8a71e 280w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/Assertions/reason-2.png?w=560&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=b303e36a78a60deabbc494dc063e7459 560w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/Assertions/reason-2.png?w=840&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=c08397a6bcb00bb4482123e2b85879d0 840w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/Assertions/reason-2.png?w=1100&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=cc55c353d684f6be308989a1a68d1289 1100w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/Assertions/reason-2.png?w=1650&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=b96c2ce63291a295ab8c41ec154d3261 1650w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/Assertions/reason-2.png?w=2500&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=910c824db0a3888f4b368698af72d046 2500w" />

## Improving the prompt

Let's try to update the prompt to be more specific about asking for more information and not hallucinating a stock tool.

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
async function task(input: string) {
  const completion = await openai.chat.completions.create({
    model: "gpt-3.5-turbo",
    messages: [
      {
        role: "system",
        content: `You are a highly intelligent AI that can look up the weather.

Do not try to use tools other than those provided to you. If you do not have the tools needed to solve a problem, just say so.

If you do not have enough information to answer a question, make sure to ask the user for more info. Prefix that statement with "I need more information to answer this question."
        `,
      },
      { role: "user", content: input },
    ],
    tools: [weatherTool],
    max_tokens: 1000,
  });

  return {
    responseChatCompletions: [completion.choices[0].message],
  };
}
```

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
JSON.stringify(await task("How much is AAPL stock today?"), null, 2);
```

```
{
  "responseChatCompletions": [
    {
      "role": "assistant",
      "content": "I'm sorry, but I don't have the tools to look up stock prices."
    }
  ]
}
```

### Re-running eval

Let's re-run the eval and see if our changes helped.

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
await Eval("Weather Bot", {
  data: data,
  task: async (input) => {
    const result = await task(input);
    return result;
  },
  scores: [AssertionScorer],
});
```

```
{
  projectName: 'Weather Bot',
  experimentName: 'HEAD-1707465778',
  projectUrl: 'https://www.braintrust.dev/app/braintrust.dev/p/Weather%20Bot',
  experimentUrl: 'https://www.braintrust.dev/app/braintrust.dev/p/Weather%20Bot/HEAD-1707465778',
  comparisonExperimentName: 'HEAD-1707465445',
  scores: {
    'Assertions Score': {
      name: 'Assertions Score',
      score: 0.75,
      diff: 0.25,
      improvements: 1,
      regressions: 0
    }
  },
  metrics: {
    duration: {
      name: 'duration',
      metric: 1.5197500586509705,
      unit: 's',
      diff: -0.10424983501434326,
      improvements: 2,
      regressions: 2
    }
  }
}
```

```
 ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ | Weather Bot                              |   4% | 4/100 datapoints
```

```
{
  projectName: 'Weather Bot',
  experimentName: 'HEAD-1707465778',
  projectUrl: 'https://www.braintrust.dev/app/braintrust.dev/p/Weather%20Bot',
  experimentUrl: 'https://www.braintrust.dev/app/braintrust.dev/p/Weather%20Bot/HEAD-1707465778',
  comparisonExperimentName: 'HEAD-1707465445',
  scores: {
    'Assertions Score': {
      name: 'Assertions Score',
      score: 0.75,
      diff: 0.25,
      improvements: 1,
      regressions: 0
    }
  },
  metrics: {
    duration: {
      name: 'duration',
      metric: 1.5197500586509705,
      unit: 's',
      diff: -0.10424983501434326,
      improvements: 2,
      regressions: 2
    }
  }
}
```

Nice! We were able to improve the "needs more information" case.

<img src="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/Assertions/second-experiment.png?fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=9b059c15e8009ef18902dfd8530db24d" alt="second experiment" data-og-width="2732" width="2732" data-og-height="2348" height="2348" data-path="cookbook/assets/Assertions/second-experiment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/Assertions/second-experiment.png?w=280&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=e9f1ff2b09d3d575e68d6cb9d8ed5a72 280w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/Assertions/second-experiment.png?w=560&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=ec7f5f6765ba8ec97117c98b17886587 560w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/Assertions/second-experiment.png?w=840&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=f408bfe20e915c92ef9bcbef1a69503f 840w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/Assertions/second-experiment.png?w=1100&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=0b8b1683de5648e11d3c2223bbc9ab98 1100w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/Assertions/second-experiment.png?w=1650&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=868cc0225b742d383dded611dd32db6c 1650w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/Assertions/second-experiment.png?w=2500&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=5c19600a9ae39f5920816ce3e3061d6f 2500w" />

However, we now halucinate and ask for the weather in NYC. Getting to 100% will take a bit more iteration!

<img src="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/Assertions/bad-tool-call.png?fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=9ae8487c4ede3327623d92200ce1107e" alt="bad tool call" data-og-width="892" width="892" data-og-height="1078" height="1078" data-path="cookbook/assets/Assertions/bad-tool-call.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/Assertions/bad-tool-call.png?w=280&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=ce96307c44464ddf64452f894a548a11 280w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/Assertions/bad-tool-call.png?w=560&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=dedd36597ba8972ae36c6628672da9ac 560w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/Assertions/bad-tool-call.png?w=840&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=93a409acae650d8bbd16e932eb08c793 840w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/Assertions/bad-tool-call.png?w=1100&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=0cb6b09aef74e89428df46394e1f0667 1100w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/Assertions/bad-tool-call.png?w=1650&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=10fe66a804a6c0d8b2fdd75ec12df845 1650w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/Assertions/bad-tool-call.png?w=2500&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=c14632152eb1d30c34aa3cfd2d149a0b 2500w" />

Now that you have a solid evaluation framework in place, you can continue experimenting and try to solve this problem. Happy evaling!

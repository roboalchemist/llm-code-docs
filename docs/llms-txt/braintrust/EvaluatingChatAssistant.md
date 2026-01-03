# Source: https://braintrust.dev/docs/cookbook/recipes/EvaluatingChatAssistant.md

# Evaluating a chat assistant

<div className="text-sm">[Contributed](https://github.com/braintrustdata/braintrust-cookbook/blob/main/examples/EvaluatingChatAssistant/EvaluatingChatAssistant.ipynb) by [Tara Nagar](https://www.linkedin.com/in/taranagar/) on 2024-07-16</div>

## Evaluating a multi-turn chat assistant

This tutorial will walk through using Braintrust to evaluate a conversational, multi-turn chat assistant.

These types of chat bots have become important parts of applications, acting as customer service agents, sales representatives, or travel agents, to name a few. As an owner of such an application, it's important to be sure the bot provides value to the user.

We will expand on this below, but the history and context of a conversation is crucial in being able to produce a good response. If you received a request to "Make a dinner reservation at 7pm" and you knew where, on what date, and for how many people, you could provide some assistance; otherwise, you'd need to ask for more information.

Before starting, please make sure you have a Braintrust account. If you do not have one, you can [sign up here](https://www.braintrust.dev).

## Installing dependencies

Begin by installing the necessary dependencies if you have not done so already.

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
pnpm install autoevals braintrust openai
```

## Inspecting the data

Let's take a look at the small dataset prepared for this cookbook. You can find the full dataset in the accompanying [dataset.ts file](https://github.com/braintrustdata/braintrust-cookbook/tree/main/examples/EvaluatingChatAssistant/dataset.ts). The `assistant` turns were generated using `claude-3-5-sonnet-20240620`.

Below is an example of a data point.

* `chat_history` contains the history of the conversation between the user and the assistant
* `input` is the last `user` turn that will be sent in the `messages` argument to the chat completion
* `expected` is the output expected from the chat completion given the input

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import dataset, { ChatTurn } from "./assets/dataset";

console.log(dataset[0]);
```

```
{
  chat_history: [
    {
      role: 'user',
      content: "when was the ballon d'or first awarded for female players?"
    },
    {
      role: 'assistant',
      content: "The Ballon d'Or for female players was first awarded in 2018. The inaugural winner was Ada Hegerberg, a Norwegian striker who plays for Olympique Lyonnais."
    }
  ],
  input: "who won the men's trophy that year?",
  expected: "In 2018, the men's Ballon d'Or was awarded to Luka Modrić."
}
```

From looking at this one example, we can see why the history is necessary to provide a helpful response.

If you were asked "Who won the men's trophy that year?" you would wonder *What trophy? Which year?* But if you were also given the `chat_history`, you would be able to answer the question (maybe after some quick research).

## Running experiments

The key to running evals on a multi-turn conversation is to include the history of the chat in the chat completion request.

### Assistant with no chat history

To start, let's see how the prompt performs when no chat history is provided. We'll create a simple task function that returns the output from a chat completion.

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import { wrapOpenAI } from "braintrust";
import { OpenAI } from "openai";

const experimentData = dataset.map((data) => ({
  input: data.input,
  expected: data.expected,
}));
console.log(experimentData[0]);

async function runTask(input: string) {
  const client = wrapOpenAI(
    new OpenAI({
      baseURL: "https://api.braintrust.dev/v1/proxy",
      apiKey: process.env.OPENAI_API_KEY ?? "", // Can use OpenAI, Anthropic, Mistral, etc. API keys here
    }),
  );

  const response = await client.chat.completions.create({
    model: "gpt-4o",
    messages: [
      {
        role: "system",
        content:
          "You are a helpful and polite assistant who knows about sports.",
      },
      {
        role: "user",
        content: input,
      },
    ],
  });
  return response.choices[0].message.content || "";
}
```

```
{
  input: "who won the men's trophy that year?",
  expected: "In 2018, the men's Ballon d'Or was awarded to Luka Modrić."
}
```

#### Scoring and running the eval

We'll use the `Factuality` scoring function from the [autoevals library](https://www.braintrust.dev/docs/reference/autoevals) to check how the output of the chat completion compares factually to the expected value.

We will also utilize [trials](https://www.braintrust.dev/docs/guides/evals/write#trials) by including the `trialCount` parameter in the `Eval` call. We expect the output of the chat completion to be non-deterministic, so running each input multiple times will give us a better sense of the "average" output.

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import { Eval } from "braintrust";
import Factuality from "autoevals";

Eval("Chat assistant", {
  experimentName: "gpt-4o assistant - no history",
  data: () => experimentData,
  task: runTask,
  scores: [Factuality],
  trialCount: 3,
  metadata: {
    model: "gpt-4o",
    prompt: "You are a helpful and polite assistant who knows about sports.",
  },
});
```

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
Experiment gpt - 4o assistant - no history is running at https://www.braintrust.dev/app/braintrustdata.com/p/Chat%20assistant/experiments/gpt-4o%20assistant%20-%20no%20history
 ████████████████████████████████████████ | Chat assistant[experimentName = gpt - 4o... | 100 % | 15 / 15 datapoints


=========================SUMMARY=========================
61.33% 'Factuality' score       (0 improvements, 0 regressions)

4.12s 'duration'        (0 improvements, 0 regressions)
0.01$ 'estimated_cost'  (0 improvements, 0 regressions)

See results for gpt-4o assistant - no history at https://www.braintrust.dev/app/braintrustdata.com/p/Chat%20assistant/experiments/gpt-4o%20assistant%20-%20no%20history
```

61.33% Factuality score? Given what we discussed earlier about chat history being important in producing a good response, that's surprisingly high. Let's log onto [braintrust.dev](https://www.braintrust.dev) and take a look at how we got that score.

#### Interpreting the results

<img src="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/no-history-trace.png?fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=3c6badae27adb13b7bd09527b0972f9f" alt="no-history-trace" data-og-width="2972" width="2972" data-og-height="1798" height="1798" data-path="cookbook/assets/EvaluatingChatAssistant/no-history-trace.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/no-history-trace.png?w=280&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=548f17d092fc3afb063c0aa97ce8620e 280w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/no-history-trace.png?w=560&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=611809fa190f7b675feaa0c9045bfb41 560w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/no-history-trace.png?w=840&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=54089250688b27387701cdc72ebdb675 840w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/no-history-trace.png?w=1100&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=9e97b94a6ba9acf9341de5fcd3c8fc04 1100w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/no-history-trace.png?w=1650&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=0d4f246bee18adf3a7217d6ec3b6c257 1650w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/no-history-trace.png?w=2500&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=4d4e7994d9a718223c2be41de5b5a37e 2500w" />

If we look at the score distribution chart, we can see ten of the fifteen examples scored at least 60%, with over half even scoring 100%. If we look into one of the examples with 100% score, we see the output of the chat completion request is asking for more context as we would expect:

`Could you please specify which athlete or player you're referring to? There are many professional athletes, and I'll need a bit more information to provide an accurate answer.`

This aligns with our expectation, so let's now look at how the score was determined.

<img src="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/no-history-score.png?fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=e31c53dbd2ffa84fab5505150e5e9369" alt="no-history-score" data-og-width="2972" width="2972" data-og-height="1794" height="1794" data-path="cookbook/assets/EvaluatingChatAssistant/no-history-score.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/no-history-score.png?w=280&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=3a9447057dac151a462aab84acdcc0d1 280w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/no-history-score.png?w=560&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=5e134d19868f13abc618a7c6c4b1ff5a 560w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/no-history-score.png?w=840&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=544bd03384fbbc4dc9bbb5b43afcdb04 840w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/no-history-score.png?w=1100&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=21b8a1c21f5193fb51a7b765ce76b86f 1100w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/no-history-score.png?w=1650&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=43f1988aaa430915bb310d90f2ed2a99 1650w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/no-history-score.png?w=2500&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=9ebf2739c78f5f9743c8de39e3f09b42 2500w" />

Click into the scoring trace, we see the chain of thought reasoning used to settle on the score. The model chose `(E) The answers differ, but these differences don't matter from the perspective of factuality.` which is *technically* correct, but we want to penalize the chat completion for not being able to produce a good response.

#### Improve scoring with a custom scorer

While Factuality is a good general purpose scorer, for our use case option (E) is not well aligned with our expectations. The best way to work around this is to customize the scoring function so that it produces a lower score for asking for more context or specificity.

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import { LLMClassifierFromSpec, Score } from "autoevals";

function Factual(args: {
  input: string;
  output: string;
  expected: string;
}): Score | Promise<Score> {
  const factualityScorer = LLMClassifierFromSpec("Factuality", {
    prompt: `You are comparing a submitted answer to an expert answer on a given question. Here is the data:
              [BEGIN DATA]
              ************
              [Question]: {{{input}}}
              ************
              [Expert]: {{{expected}}}
              ************
              [Submission]: {{{output}}}
              ************
              [END DATA]

              Compare the factual content of the submitted answer with the expert answer. Ignore any differences in style, grammar, or punctuation.
              The submitted answer may either be a subset or superset of the expert answer, or it may conflict with it. Determine which case applies. Answer the question by selecting one of the following options:
              (A) The submitted answer is a subset of the expert answer and is fully consistent with it.
              (B) The submitted answer is a superset of the expert answer and is fully consistent with it.
              (C) The submitted answer contains all the same details as the expert answer.
              (D) There is a disagreement between the submitted answer and the expert answer.
              (E) The answers differ, but these differences don't matter from the perspective of factuality.
              (F) The submitted answer asks for more context, specifics or clarification but provides factual information consistent with the expert answer.
              (G) The submitted answer asks for more context, specifics or clarification but does not provide factual information consistent with the expert answer.`,
    choice_scores: {
      A: 0.4,
      B: 0.6,
      C: 1,
      D: 0,
      E: 1,
      F: 0.2,
      G: 0,
    },
  });
  return factualityScorer(args);
}
```

You can see the built-in Factuality prompt [here](https://github.com/braintrustdata/autoevals/blob/main/templates/factuality.yaml). For our customized scorer, we've added two score choices to that prompt:

```
- (F) The submitted answer asks for more context, specifics or clarification but provides factual information consistent with the expert answer.
- (G) The submitted answer asks for more context, specifics or clarification but does not provide factual information consistent with the expert answer.
```

These will score (F) = 0.2 and (G) = 0 so the model gets some credit if there was any context it was able to gather from the user's input.

We can then use this spec and the `LLMClassifierFromSpec` function to create our customer scorer to use in the eval function.

Read more about [defining your own scorers](https://www.braintrust.dev/docs/guides/evals/write#define-your-own-scorers) in the documentation.

#### Re-running the eval

Let's now use this updated scorer and run the experiment again.

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
Eval("Chat assistant", {
  experimentName: "gpt-4o assistant - no history",
  data: () =>
    dataset.map((data) => ({ input: data.input, expected: data.expected })),
  task: runTask,
  scores: [Factual],
  trialCount: 3,
  metadata: {
    model: "gpt-4o",
    prompt: "You are a helpful and polite assistant who knows about sports.",
  },
});
```

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
Experiment gpt - 4o assistant - no history - 934e5ca2 is running at https://www.braintrust.dev/app/braintrustdata.com/p/Chat%20assistant/experiments/gpt-4o%20assistant%20-%20no%20history-934e5ca2
 ████████████████████████████████████████ | Chat assistant[experimentName = gpt - 4o... | 100 % | 15 / 15 datapoints


=========================SUMMARY=========================
gpt-4o assistant - no history-934e5ca2 compared to gpt-4o assistant - no history:
6.67% (-54.67%) 'Factuality' score      (0 improvements, 5 regressions)

4.77s 'duration'        (2 improvements, 3 regressions)
0.01$ 'estimated_cost'  (2 improvements, 3 regressions)

See results for gpt-4o assistant - no history-934e5ca2 at https://www.braintrust.dev/app/braintrustdata.com/p/Chat%20assistant/experiments/gpt-4o%20assistant%20-%20no%20history-934e5ca2
```

6.67% as a score aligns much better with what we expected. Let's look again into the results of this experiment.

#### Interpreting the results

<img src="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/no-history-custom-score.png?fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=9d06889a5721d1826c13d8044925196a" alt="no-history-custom-score" data-og-width="2976" width="2976" data-og-height="1800" height="1800" data-path="cookbook/assets/EvaluatingChatAssistant/no-history-custom-score.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/no-history-custom-score.png?w=280&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=5eeb32a5c09d582f7e790b190f66a759 280w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/no-history-custom-score.png?w=560&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=18fa6537a5e194c2b7de493edd5e0cfe 560w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/no-history-custom-score.png?w=840&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=5f7ca3991e618424121da2ee3e6b08d2 840w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/no-history-custom-score.png?w=1100&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=b55ccac96522e5985284352ba813d1ae 1100w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/no-history-custom-score.png?w=1650&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=a9faf38d9867e5495823a794fe63f128 1650w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/no-history-custom-score.png?w=2500&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=6a50e801acf3686811e9ceadca287173 2500w" />

In the table we can see the `output` fields in which the chat completion responses are requesting more context. In one of the experiment that had a non-zero score, we can see that the model asked for some clarification, but was able to understand from the question that the user was inquiring about a controversial World Series. Nice!

<img src="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/no-history-custom-score-cot.png?fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=36e52d1de3e15b2ce7a8e6656cc02fd5" alt="no-history-custom-score-cot" data-og-width="2974" width="2974" data-og-height="1800" height="1800" data-path="cookbook/assets/EvaluatingChatAssistant/no-history-custom-score-cot.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/no-history-custom-score-cot.png?w=280&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=a2ddd2bee07ce31e6913ed23e4ce940d 280w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/no-history-custom-score-cot.png?w=560&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=68d7cc909efd1d6d127c350737be7862 560w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/no-history-custom-score-cot.png?w=840&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=caca0e3303a2f47c14d36395e2f1be18 840w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/no-history-custom-score-cot.png?w=1100&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=5f0b46dc59060ec7276d35006084e38c 1100w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/no-history-custom-score-cot.png?w=1650&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=0b21b8ea2c5ac401b3331a7939fe0259 1650w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/no-history-custom-score-cot.png?w=2500&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=dd1ee59bec7a7cef05afbaba513cb93b 2500w" />

Looking into how the score was determined, we can see that the factual information aligned with the expert answer but the submitted answer still asks for more context, resulting in a score of 20% which is what we expect.

### Assistant with chat history

Now let's shift and see how providing the chat history improves the experiment.

#### Update the data, task function and scorer function

We need to edit the inputs to the `Eval` function so we can pass the chat history to the chat completion request.

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
const experimentData = dataset.map((data) => ({
  input: { input: data.input, chat_history: data.chat_history },
  expected: data.expected,
}));
console.log(experimentData[0]);

async function runTask({
  input,
  chat_history,
}: {
  input: string;
  chat_history: ChatTurn[];
}) {
  const client = wrapOpenAI(
    new OpenAI({
      baseURL: "https://api.braintrust.dev/v1/proxy",
      apiKey: process.env.OPENAI_API_KEY ?? "", // Can use OpenAI, Anthropic, Mistral, etc. API keys here
    }),
  );

  const response = await client.chat.completions.create({
    model: "gpt-4o",
    messages: [
      {
        role: "system",
        content:
          "You are a helpful and polite assistant who knows about sports.",
      },
      ...chat_history,
      {
        role: "user",
        content: input,
      },
    ],
  });
  return response.choices[0].message.content || "";
}

function Factual(args: {
  input: {
    input: string;
    chat_history: ChatTurn[];
  };
  output: string;
  expected: string;
}): Score | Promise<Score> {
  const factualityScorer = LLMClassifierFromSpec("Factuality", {
    prompt: `You are comparing a submitted answer to an expert answer on a given question. Here is the data:
              [BEGIN DATA]
              ************
              [Question]: {{{input}}}
              ************
              [Expert]: {{{expected}}}
              ************
              [Submission]: {{{output}}}
              ************
              [END DATA]

              Compare the factual content of the submitted answer with the expert answer. Ignore any differences in style, grammar, or punctuation.
              The submitted answer may either be a subset or superset of the expert answer, or it may conflict with it. Determine which case applies. Answer the question by selecting one of the following options:
              (A) The submitted answer is a subset of the expert answer and is fully consistent with it.
              (B) The submitted answer is a superset of the expert answer and is fully consistent with it.
              (C) The submitted answer contains all the same details as the expert answer.
              (D) There is a disagreement between the submitted answer and the expert answer.
              (E) The answers differ, but these differences don't matter from the perspective of factuality.
              (F) The submitted answer asks for more context, specifics or clarification but provides factual information consistent with the expert answer.
              (G) The submitted answer asks for more context, specifics or clarification but does not provide factual information consistent with the expert answer.`,
    choice_scores: {
      A: 0.4,
      B: 0.6,
      C: 1,
      D: 0,
      E: 1,
      F: 0.2,
      G: 0,
    },
  });
  return factualityScorer(args);
}
```

```
{
  input: {
    input: "who won the men's trophy that year?",
    chat_history: [ [Object], [Object] ]
  },
  expected: "In 2018, the men's Ballon d'Or was awarded to Luka Modrić."
}
```

We update the parameter to the task function to accept both the `input` string and the `chat_history` array and add the `chat_history` into the messages array in the chat completion request, done here using the spread `...` syntax.

We also need to update the `experimentData` and `Factual` function parameters to align with these changes.

#### Running the eval

Use the updated variables and functions to run a new eval.

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
Eval("Chat assistant", {
  experimentName: "gpt-4o assistant",
  data: () => experimentData,
  task: runTask,
  scores: [Factual],
  trialCount: 3,
  metadata: {
    model: "gpt-4o",
    prompt: "You are a helpful and polite assistant who knows about sports.",
  },
});
```

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
Experiment gpt - 4o assistant is running at https://www.braintrust.dev/app/braintrustdata.com/p/Chat%20assistant/experiments/gpt-4o%20assistant
 ████████████████████████████████████████ | Chat assistant[experimentName = gpt - 4o... | 100 % | 15 / 15 datapoints


=========================SUMMARY=========================
gpt-4o assistant compared to gpt-4o assistant - no history-934e5ca2:
60.00% 'Factuality' score       (0 improvements, 0 regressions)

4.34s 'duration'        (0 improvements, 0 regressions)
0.01$ 'estimated_cost'  (0 improvements, 0 regressions)

See results for gpt-4o assistant at https://www.braintrust.dev/app/braintrustdata.com/p/Chat%20assistant/experiments/gpt-4o%20assistant
```

60% score is a definite improvement from 4%.

You'll notice that it says there were 0 improvements and 0 regressions compared to the last experiment `gpt-4o assistant - no history-934e5ca2` we ran. This is because by default, Braintrust uses the `input` field to match rows across experiments. From the dashboard, we can customize the comparison key ([see docs](https://www.braintrust.dev/docs/guides/evals/interpret#customizing-the-comparison-key)) by going to the [project configuration page](https://www.braintrust.dev/app/braintrustdata.com/p/Chat%20assistant/configuration).

#### Update experiment comparison for diff mode

Let's go back to the dashboard.

For this cookbook, we can use the `expected` field as the comparison key because this field is unique in our small dataset.

In the Configuration tab, go to the bottom of the page to update the comparison key:

<img src="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/comparison-key.png?fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=4d326d0639fb7999a1706dad40fd606f" alt="comparison-key" data-og-width="765" width="765" data-og-height="333" height="333" data-path="cookbook/assets/EvaluatingChatAssistant/comparison-key.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/comparison-key.png?w=280&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=2429e723c272a7cf696b71f2f0232809 280w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/comparison-key.png?w=560&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=edacde6209cd292ffa3bd253ccde8555 560w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/comparison-key.png?w=840&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=99fc50f10af17cfcdf451313128ce6b9 840w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/comparison-key.png?w=1100&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=c8d62416e295874d6f5375094f0527b9 1100w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/comparison-key.png?w=1650&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=d93034b2dde1811efea62af19d6daaef 1650w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/comparison-key.png?w=2500&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=c236879d39440f2372497132c78db9a0 2500w" />

#### Interpreting the results

Turn on diff mode using the toggle on the upper right of the table.

<img src="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/experiment-diff.png?fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=06c2cec39ea5b7e2751089bca1b65a64" alt="experiment-diff" data-og-width="2974" width="2974" data-og-height="1800" height="1800" data-path="cookbook/assets/EvaluatingChatAssistant/experiment-diff.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/experiment-diff.png?w=280&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=254737d7cca6a4308c01f533bd565145 280w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/experiment-diff.png?w=560&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=915646fc04d7b9b6ba6b0de7673aadc0 560w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/experiment-diff.png?w=840&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=6bca58d84831783e087fa0e87f922169 840w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/experiment-diff.png?w=1100&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=1e812d613f1e195786641ba430d4ba7a 1100w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/experiment-diff.png?w=1650&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=4cb0e2bba7b4965c6a8ea0654d61b05f 1650w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/experiment-diff.png?w=2500&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=2e38cd3e1409ed59ac35fc5f9eccd0f2 2500w" />

Since we updated the comparison key, we can now see the improvements in the Factuality score between the experiment run with chat history and the most recent one run without for each of the examples. If we also click into a trace, we can see the change in input parameters that we made above where it went from a `string` to an object with `input` and `chat_history` fields.

All of our rows scored 60% in this experiment. If we look into each trace, this means the submitted answer includes all the details from the expert answer with some additional information.

60% is an improvement from the previous run, but we can do better. Since it seems like the chat completion is always returning more than necessary, let's see if we can tweak our prompt to have the output be more concise.

#### Improving the result

Let's update the system prompt used in the chat completion request.

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
async function runTask({
  input,
  chat_history,
}: {
  input: string;
  chat_history: ChatTurn[];
}) {
  const client = wrapOpenAI(
    new OpenAI({
      baseURL: "https://api.braintrust.dev/v1/proxy",
      apiKey: process.env.OPENAI_API_KEY ?? "", // Can use OpenAI, Anthropic, Mistral etc. API keys here
    }),
  );

  const response = await client.chat.completions.create({
    model: "gpt-4o",
    messages: [
      {
        role: "system",
        content:
          "You are a helpful, polite assistant who knows about sports. Only answer the question; don't add additional information outside of what was asked.",
      },
      ...chat_history,
      {
        role: "user",
        content: input,
      },
    ],
  });
  return response.choices[0].message.content || "";
}
```

In the task function, we'll update the `system` message to specify the output should be precise and then run the eval again.

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
Eval("Chat assistant", {
  experimentName: "gpt-4o assistant - concise",
  data: () => experimentData,
  task: runTask,
  scores: [Factual],
  trialCount: 3,
  metadata: {
    model: "gpt-4o",
    prompt:
      "You are a helpful, polite assistant who knows about sports. Only answer the question; don't add additional information outside of what was asked.",
  },
});
```

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
Experiment gpt - 4o assistant - concise is running at https://www.braintrust.dev/app/braintrustdata.com/p/Chat%20assistant/experiments/gpt-4o%20assistant%20-%20concise
 ████████████████████████████████████████ | Chat assistant[experimentName = gpt - 4o... | 100 % | 15 / 15 datapoints


=========================SUMMARY=========================
gpt-4o assistant - concise compared to gpt-4o assistant:
86.67% (+26.67%) 'Factuality' score     (4 improvements, 0 regressions)

1.89s 'duration'        (5 improvements, 0 regressions)
0.01$ 'estimated_cost'  (4 improvements, 1 regressions)

See results for gpt-4o assistant - concise at https://www.braintrust.dev/app/braintrustdata.com/p/Chat%20assistant/experiments/gpt-4o%20assistant%20-%20concise
```

Let's go into the dashboard and see the new experiment.

<img src="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/concise-diff.png?fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=233ca2b1c2b351375e37a2211cb710de" alt="concise-diff" data-og-width="2976" width="2976" data-og-height="1802" height="1802" data-path="cookbook/assets/EvaluatingChatAssistant/concise-diff.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/concise-diff.png?w=280&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=699ababccea681a0b34ff3e625e298af 280w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/concise-diff.png?w=560&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=7ac78f0ccb31f507e412bbe17442af21 560w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/concise-diff.png?w=840&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=aeda89664a9742ee507a330661063f13 840w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/concise-diff.png?w=1100&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=7bb123e464a274f57e918a3ccefbeff2 1100w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/concise-diff.png?w=1650&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=119b44f1ae3b399918253fc7645f81bc 1650w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/EvaluatingChatAssistant/concise-diff.png?w=2500&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=d767a0fb9fda0b3a924d7abc3339f801 2500w" />

Success! We got a 27 percentage point increase in factuality, up to an average score of 87% for this experiment with our updated prompt.

### Conclusion

We've seen in this cookbook how to evaluate a chat assistant and visualized how the chat history effects the output of the chat completion. Along the way, we also utilized some other functionality such as updating the comparison key in the diff view and creating a custom scoring function.

Try seeing how you can improve the outputs and scores even further!


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt
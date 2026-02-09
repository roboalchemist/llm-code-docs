# Source: https://braintrust.dev/docs/cookbook/recipes/Loop.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Using Loop in AI product development

<div className="text-sm">[Contributed](https://github.com/braintrustdata/braintrust-cookbook/blob/main/examples/Loop/loop.mdx) by [Alex Zelenskiy](https://www.linkedin.com/in/alexzelenskiy/) on 2025-11-21</div>

[Loop](/observe/loop) is a built-in AI assistant that helps you throughout the AI product development process in Braintrust. From creating scorers and generating datasets to analyzing logs and improving prompts, Loop is available throughout the product to help with your workflows. This guide shows how you can use Loop to build, evaluate, and improve a weather agent, demonstrating how Loop can make common AI development tasks easier and more accessible.

By the end of this guide, you'll learn how to:

* Use Loop to create custom scorers for your specific use case
* Analyze logs with Loop to understand quality issues
* Clean and prepare datasets with Loop's help
* Iterate on prompts using Loop's experiment analysis

In this cookbook, we'll represent messages you send to Loop with 💬.

## Getting started

This example uses the OpenAI Agents SDK to build a simple weather agent. You'll need:

* A [Braintrust](https://www.braintrust.dev/signup) account
* An [OpenAI](https://platform.openai.com/) API key
* Node.js and npm installed

First, install the required dependencies:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
npm install @openai/agents braintrust @braintrust/openai-agents
```

Set up your environment variables in a `.env` file:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
BRAINTRUST_API_KEY=<your-api-key>
OPENAI_API_KEY=<your-openai-key>
```

## Building the weather agent

Let's start with a basic agent that can fetch current weather information. This agent uses the OpenAI Agents SDK and has one tool that returns realtime weather data for a given location.

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import { Agent, run, addTraceProcessor } from "@openai/agents";
import { getWeatherByPlace } from "./weather-tool.js";
import { initLogger } from "braintrust";
import { OpenAIAgentsTraceProcessor } from "@braintrust/openai-agents";

// Initialize Braintrust logger
const logger = initLogger({
  projectName: "Weather-Agent",
  apiKey: process.env.BRAINTRUST_API_KEY,
});

// Create the tracing processor
const processor = new OpenAIAgentsTraceProcessor({ logger });

// Add the processor to OpenAI Agents
addTraceProcessor(processor);

// Create the agent with a simple instruction
const agent = new Agent({
  name: "WeatherAgent",
  instructions: "You are a friendly assistant",
  model: "gpt-4o-mini",
  tools: [getWeatherByPlace],
});

// Test the agent
const result = await run(agent, "What's the weather in London?");
```

The agent works, but there's an important limitation: it can only fetch current weather data, not forecasts or historical information. We need to ensure the agent doesn't promise capabilities it doesn't have.

## Creating a scorer with Loop

Instead of manually writing a scorer from scratch, we can ask Loop to create one for us. This is especially useful when you need domain-specific evaluation logic.

Send this message to Loop:

<Callout>
  💬 *Create an LLM scorer that checks output to make sure it provides realtime
  weather information when asked, but doesn't offer to provide forecasts or
  historical data. We will be running this on an agent that can ONLY get
  realtime data.*
</Callout>

<img src="https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/create-scorer-with-loop.png?fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=2e820f1ec9ad2a731256db70273538c9" alt="Creating a scorer with Loop" data-og-width="1976" width="1976" data-og-height="1079" height="1079" data-path="cookbook/assets/Loop/create-scorer-with-loop.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/create-scorer-with-loop.png?w=280&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=107df5bf99151220726ffbb7ad577f0d 280w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/create-scorer-with-loop.png?w=560&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=b91f07d343905c938b064ff3367f073f 560w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/create-scorer-with-loop.png?w=840&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=5cc1eccb62000e141e46e38e3615fd05 840w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/create-scorer-with-loop.png?w=1100&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=636aab482063451adb90e924c4efe97d 1100w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/create-scorer-with-loop.png?w=1650&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=08212afca6c38e53851bf96a882e7261 1650w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/create-scorer-with-loop.png?w=2500&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=feed702131065eead2fd0b1db9f7e102 2500w" />

Loop will generate a scorer that checks whether the agent stays within its capabilities. Once created, you can add it to your online scoring configuration to automatically evaluate incoming logs.

<img src="https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/configure-online-scoring.png?fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=4163c76dbf635cee83b8e2e00798bc61" alt="Configuring online scoring" data-og-width="1976" width="1976" data-og-height="677" height="677" data-path="cookbook/assets/Loop/configure-online-scoring.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/configure-online-scoring.png?w=280&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=fd1d229e691090136247d9042e2cbd9f 280w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/configure-online-scoring.png?w=560&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=8fe828aae9a9b2c36cc6e4d87aefd376 560w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/configure-online-scoring.png?w=840&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=b7c7e5a1a59569f877e663dd856013bb 840w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/configure-online-scoring.png?w=1100&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=f8b706cb93495e6ad8ef1ace94940425 1100w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/configure-online-scoring.png?w=1650&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=2bda8fb8f88c4408c30a863190be4a4c 1650w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/configure-online-scoring.png?w=2500&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=27fca71a295103763b3367e901bac220 2500w" />

## Analyzing logs with Loop

After running your agent for a while, you'll accumulate logs that you can analyze. Looking at the Logs view, you might notice some responses are getting poor scores.

<img src="https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/logs-view-with-scores.png?fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=d2c4e16edb3acb8456ccd8ab9df783e4" alt="Logs view showing scores" data-og-width="1976" width="1976" data-og-height="903" height="903" data-path="cookbook/assets/Loop/logs-view-with-scores.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/logs-view-with-scores.png?w=280&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=86f716b5cae04c5e70896689a8a91618 280w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/logs-view-with-scores.png?w=560&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=6d71beb5960ae8e4b698cc406844c58e 560w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/logs-view-with-scores.png?w=840&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=d85e317094ce18595ad22d8205a25965 840w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/logs-view-with-scores.png?w=1100&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=c90d8b470c06074f39b8927f7dbacb5a 1100w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/logs-view-with-scores.png?w=1650&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=293e20bb48fd899afa9d25370cd4c463 1650w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/logs-view-with-scores.png?w=2500&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=b2bcd3a66ef599875cf813e4f42f523e 2500w" />

Rather than manually reviewing each log, ask Loop to identify patterns:

<Callout>
  💬 *Can you look at the last 3 days of logs and explain why some of them got
  poor scores?*
</Callout>

<img src="https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/loop-analyzing-logs.png?fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=f00b42068f6fa0f509d2dd0509274f90" alt="Loop analyzing logs" data-og-width="1976" width="1976" data-og-height="1014" height="1014" data-path="cookbook/assets/Loop/loop-analyzing-logs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/loop-analyzing-logs.png?w=280&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=0583a424bdd25f26a017547fea4f2b80 280w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/loop-analyzing-logs.png?w=560&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=36885f5589d6b83616c2e7ff0ad6812a 560w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/loop-analyzing-logs.png?w=840&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=979430b7ed60a54e47c49804057325ec 840w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/loop-analyzing-logs.png?w=1100&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=56e2631aab1486a5d0c84fb8f422c1d3 1100w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/loop-analyzing-logs.png?w=1650&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=509ca424729829f40fa2cd42a86c4774 1650w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/loop-analyzing-logs.png?w=2500&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=4a94cba1e159e4aa780023fd651f2c79 2500w" />

Loop analyzes the logs and provides insights like:

```markdown  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
# Key patterns in poor scores:

Over-helpful follow-ups hurt scores: When the agent offers forecasts,
hourly predictions, or future weather after correctly providing current weather,
it gets penalized.

Missing weather data: When the agent asks for clarification
without providing any weather information (even when it could make a reasonable
assumption), it fails the quality check.

The agent seems too eager to offer additional services that are outside
its allowed scope (current weather only).

# Recommendations:

Configure the agent to ONLY provide current weather without suggesting
forecasts or additional features.

For ambiguous locations, provide weather for the most common interpretation
while noting the assumption, rather than just asking for clarification.

Remove any prompts or behaviors that cause the agent to offer
forecast-related capabilities.
```

### Refining the scorer

Sometimes you'll notice edge cases where the scorer doesn't catch problematic behavior. For example, if an agent response asks "Would you like me to monitor it and alert you if anything changes?" - the agent can't actually do that, but the scorer might miss it.

You can ask Loop to update the scorer:

<Callout>
  💬 *The scorer "Realtime weather only" rated this response as good but it
  contains the phrase "Would you like me to monitor it and alert you if anything
  changes?" which is not in the capability of the agent. It can't do anything
  independently. Please update the scorer so it catches this in the future.*
</Callout>

<img src="https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/update-scorer.png?fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=3d33d16d2181d23311d7cbd2bf6ecd86" alt="Updating the scorer" data-og-width="1976" width="1976" data-og-height="1014" height="1014" data-path="cookbook/assets/Loop/update-scorer.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/update-scorer.png?w=280&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=000f7fbb231de44557a723577b996a57 280w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/update-scorer.png?w=560&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=2536fe99c362641eecc313495c1318c3 560w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/update-scorer.png?w=840&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=b4f374f3aba45913dfe6c313e14e6865 840w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/update-scorer.png?w=1100&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=adb67bacd729cb1c5d18513f7c3fc4b3 1100w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/update-scorer.png?w=1650&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=5a141e7ff827a156c7163caf50db7708 1650w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/update-scorer.png?w=2500&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=c7fcf8127297d8f195f0f3b3886b398e 2500w" />

Loop will modify the scorer to catch these cases going forward.

## Building a dataset with Loop

To systematically improve the agent, you'll want to create a dataset of problematic cases. Start by adding poorly-rated responses to a dataset:

<img src="https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/add-logs-to-dataset.png?fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=fc9727cc5083f48801d0ac6434e63999" alt="Adding logs to dataset" data-og-width="1976" width="1976" data-og-height="870" height="870" data-path="cookbook/assets/Loop/add-logs-to-dataset.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/add-logs-to-dataset.png?w=280&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=ba8b77f1e2b272e1acaad21679982fa9 280w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/add-logs-to-dataset.png?w=560&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=a87968aa5b02ef6386bc1fc3dd43271f 560w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/add-logs-to-dataset.png?w=840&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=204f6eb1bc8fc70f7902c28230311b8b 840w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/add-logs-to-dataset.png?w=1100&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=04dcb2e34c1275f09e84ab21d6b6e3be 1100w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/add-logs-to-dataset.png?w=1650&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=f8ede5791696c8dcdbaf34acb8ef2759 1650w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/add-logs-to-dataset.png?w=2500&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=d71f3463c16f0e81956a8e535c4c723d 2500w" />

You might notice the dataset has extra columns you don't need:

<img src="https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/dataset-extra-columns.png?fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=34adae474b47539caa737062211d7387" alt="Dataset with extra columns" data-og-width="1976" width="1976" data-og-height="1071" height="1071" data-path="cookbook/assets/Loop/dataset-extra-columns.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/dataset-extra-columns.png?w=280&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=47a04dac86133a68f262e1cc7f936c13 280w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/dataset-extra-columns.png?w=560&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=a2a1d3786cbb6b02376277ba3204a49e 560w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/dataset-extra-columns.png?w=840&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=24ad9f2ac408c45ec14692918543f40b 840w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/dataset-extra-columns.png?w=1100&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=54c7753b4f47eb957295f0456f1248e5 1100w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/dataset-extra-columns.png?w=1650&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=0a267212bde78459e2e1bcf3e7918c99 1650w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/dataset-extra-columns.png?w=2500&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=40bf60b3b7ab85e762e98c20990397e9 2500w" />

Instead of manually editing each row, ask Loop to clean it up:

<Callout>
  💬 *Remove the expected column/cell from all the rows in this dataset*
</Callout>

The input format might also need adjustment. If your inputs are JSON objects but you only need the content field:

<Callout>
  💬 *The inputs are in JSON format right now, but I want them to be just
  whatever is in the "content" field of the JSON object in input.*
</Callout>

Now your dataset is clean and ready to use:

<img src="https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/clean-dataset.png?fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=58761181ab3191bd642f060e73dc1749" alt="Clean dataset" data-og-width="1976" width="1976" data-og-height="700" height="700" data-path="cookbook/assets/Loop/clean-dataset.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/clean-dataset.png?w=280&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=c076e7e91468dbd4a96bc8e574d75b58 280w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/clean-dataset.png?w=560&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=a66354b425de7e1a0133e1defacad26d 560w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/clean-dataset.png?w=840&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=f3d597c3c7a1d39ec83bf0e1ae225639 840w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/clean-dataset.png?w=1100&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=5967d672c4745a070780309b0c23b35a 1100w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/clean-dataset.png?w=1650&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=55cafef96359df9354fc6bf10fd24616 1650w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/clean-dataset.png?w=2500&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=61ca0146d43a80f2ecb75596afe1d62c 2500w" />

You can also ask Loop to generate additional test cases:

<Callout>
  💬 *Add 5 more rows to this dataset that are like the other ones in here where
  the input is asking for the current weather in a specific city.*
</Callout>

<img src="https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/dataset-generated-rows.png?fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=80b9471ec2a2280ac292f2ebfbecb8b2" alt="Dataset with generated rows" data-og-width="1976" width="1976" data-og-height="1079" height="1079" data-path="cookbook/assets/Loop/dataset-generated-rows.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/dataset-generated-rows.png?w=280&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=48238fc4d49fc6c1de643123bdfd0ed1 280w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/dataset-generated-rows.png?w=560&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=946be62aa5415901ff55bc77d95f36be 560w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/dataset-generated-rows.png?w=840&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=95cb71b0f163bf042b50627bd2c1820c 840w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/dataset-generated-rows.png?w=1100&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=f0b7f77ccaccaff1da58f98315d96afa 1100w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/dataset-generated-rows.png?w=1650&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=ea58a2740f145018253d28ea912b5a08 1650w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/dataset-generated-rows.png?w=2500&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=443f3523b3f7f4acf08b35ac259e797a 2500w" />

## Running evaluations

With a scorer and dataset ready, you can run evaluations to measure your agent's performance. This example pulls the dataset and scorer from Braintrust and runs the evaluation with the SDK:

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import { Agent, run } from "@openai/agents";
import { getWeatherByPlace } from "./weather-tool.js";
import { initDataset, Eval, initFunction } from "braintrust";

// Create the agent (same as before)
const agent = new Agent({
  name: "WeatherAgent",
  instructions: "You are a friendly assistant",
  model: "gpt-4o-mini",
  tools: [getWeatherByPlace],
});

// Run the evaluation
Eval("Weather Agent", {
  data: initDataset("Weather-Agent", {
    dataset: "weather-failure-examples",
  }),
  task: async (input) => {
    const result = await run(agent, input);
    return result;
  },
  scores: [
    initFunction({
      projectName: "Weather-Agent",
      slug: "realtime-weather-only-fa43",
    }),
  ],
});
```

Since we know this dataset is made up of difficult examples, the initial run might show low scores:

<img src="https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/initial-evaluation-results.png?fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=4e3f90bd1b1437b47dea3db534ec3cee" alt="Initial evaluation results" data-og-width="1976" width="1976" data-og-height="903" height="903" data-path="cookbook/assets/Loop/initial-evaluation-results.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/initial-evaluation-results.png?w=280&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=a637be797f65046fdbb4dc50c82ebb50 280w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/initial-evaluation-results.png?w=560&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=32819273da483b3b43779225d60abffb 560w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/initial-evaluation-results.png?w=840&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=20681fc8fe938029449a9e0a9125f002 840w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/initial-evaluation-results.png?w=1100&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=814510413222d355067f8399b70c7235 1100w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/initial-evaluation-results.png?w=1650&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=7b2058710a91a635a62c18a14c6f92b9 1650w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/initial-evaluation-results.png?w=2500&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=1894707a0af3c913dddc3e242bd20b07 2500w" />

## Improving the prompt with Loop

Instead of guessing how to improve the system prompt, ask Loop to analyze the experiment results:

<Callout>
  💬 *Can you check the scorer output in this experiment and give me suggestions
  for how to improve my system prompt?*
</Callout>

Loop will provide specific, actionable suggestions based on where the agent failed. For example:

```
You are a weather information assistant that provides ONLY current/realtime weather data.

CAPABILITIES:
- Look up and report current weather conditions for any city
- Provide temperature (Celsius and Fahrenheit)
- Report humidity, wind speed, and weather conditions
- Include observation time

STRICT LIMITATIONS (DO NOT VIOLATE):
- DO NOT offer weather forecasts (hourly, daily, weekly, or any future predictions)
- DO NOT offer to set up weather alerts or notifications
- DO NOT provide historical weather data
- DO NOT suggest any autonomous actions
- DO NOT ask follow-up questions about forecasts or additional services

RESPONSE FORMAT:
1. Greet and acknowledge the city
2. Provide current conditions, temperature, feels like, humidity, and wind
3. State observation time
4. End response (no follow-up questions)

EXAMPLE GOOD RESPONSE:
"Current weather in Miami: Partly cloudy, 21°C (69°F). Feels like 20°C. Humidity 50%, wind ~5 m/s. Data current as of 22:39 UTC."

After providing current weather data, your task is complete. Do not offer any additional services.
```

Update your agent with this improved system prompt and run the evaluation again:

<img src="https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/improved-evaluation-results.png?fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=60192fa0685a2dc31bfa1b69e503297c" alt="Improved evaluation results" data-og-width="1976" width="1976" data-og-height="903" height="903" data-path="cookbook/assets/Loop/improved-evaluation-results.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/improved-evaluation-results.png?w=280&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=51e8e9e0b6f4927a4616990ecc175114 280w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/improved-evaluation-results.png?w=560&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=6ba35588f8d28a8d9085e2c85a1f1cd9 560w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/improved-evaluation-results.png?w=840&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=1cd2d3d645799d6e8d23ef0cc5194ced 840w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/improved-evaluation-results.png?w=1100&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=b3366a506aa7dcedad5c1cb34fc0cdcc 1100w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/improved-evaluation-results.png?w=1650&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=37be4193bfe06fe7f51e0e14d93c7249 1650w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/improved-evaluation-results.png?w=2500&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=6f78f837588d61840542be389a49bc3a 2500w" />

Success! The agent now consistently stays within its capabilities.

## Other Loop use cases

Beyond the core workflow shown above, Loop can help with other common tasks.

### Generating charts

You can ask Loop to create visualizations of your data:

<Callout>
  💬 *Can you make me a chart that shows the number of times a tool called
  "get\_weather\_by\_city" was called over time?*
</Callout>

<img src="https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/loop-generated-chart.png?fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=432cde7bb4b77bd395dd71be4b19c60a" alt="Loop-generated chart" data-og-width="1976" width="1976" data-og-height="1014" height="1014" data-path="cookbook/assets/Loop/loop-generated-chart.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/loop-generated-chart.png?w=280&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=44d74cbb42898a200424494da28ea819 280w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/loop-generated-chart.png?w=560&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=bd155cf131869341695c77d445c6fa51 560w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/loop-generated-chart.png?w=840&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=7ef4699e8f80c1b164088c62f091242a 840w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/loop-generated-chart.png?w=1100&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=aa3634469a7a7465e45a1245076b8b51 1100w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/loop-generated-chart.png?w=1650&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=973bf506164d30b1a284dc4a76b2c72d 1650w, https://mintcdn.com/braintrust/2Wq10qnTltNexB72/cookbook/assets/Loop/loop-generated-chart.png?w=2500&fit=max&auto=format&n=2Wq10qnTltNexB72&q=85&s=cf00a2bf889b688307213a1b68ead06c 2500w" />

Loop will generate the chart definition and display it for you, making it easy to understand usage patterns and share data with stakeholders without writing any charting code.

## Next steps

Now that you've seen how Loop can accelerate your AI development workflow, try applying it to your own projects:

* Use Loop to create scorers for your specific evaluation criteria
* Ask Loop to analyze your logs and identify quality issues
* Let Loop help you clean and augment your datasets
* Get Loop's suggestions for improving your prompts based on experiment results

For more information on Loop and other Braintrust features:

* Learn more about [Loop](/observe/loop)
* Explore [logging](/observe/view-logs) and [experiments](/evaluate/run-evaluations)
* Check out other [cookbook recipes](/cookbook)

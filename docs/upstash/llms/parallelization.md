# Source: https://upstash.com/docs/workflow/agents/patterns/parallelization.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Parallelization

<img src="https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/diagram/parallel-diagram.png?fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=e2a0c9d6b9087aa110a5552a0343a616" data-og-width="1856" width="1856" data-og-height="880" height="880" data-path="img/workflow/agents/diagram/parallel-diagram.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/diagram/parallel-diagram.png?w=280&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=b377332ee8b667f81791816d635edd91 280w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/diagram/parallel-diagram.png?w=560&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=b27d5a7c75ba10432b239ab0ac9e39d3 560w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/diagram/parallel-diagram.png?w=840&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=ac6a7bdc1da4f5b155826bcc9f996a79 840w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/diagram/parallel-diagram.png?w=1100&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=dc1ac647c5d2cf7ad062e7753cc305cd 1100w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/diagram/parallel-diagram.png?w=1650&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=970752cda6b5a12bab4ec923f7f0ccbd 1650w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/diagram/parallel-diagram.png?w=2500&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=8214652e3e4c8dca441346c945518675 2500w" />

This workflow calls multiple agents simultaneously to handle tasks, and then aggregates their results.

```ts  theme={"system"}
import { serve } from "@upstash/workflow/nextjs";
import { agentWorkflow } from "@upstash/workflow-agents";

export const { POST } = serve(async (context) => {
  const agents = agentWorkflow(context);
  const model = agents.openai('gpt-3.5-turbo');

  // Define worker agents
  const worker1 = agents.agent({
    model,
    name: 'worker1',
    maxSteps: 1,
    background: 'You are an agent that explains quantum physics.',
    tools: {}
  });

  const worker2 = agents.agent({
    model,
    name: 'worker2',
    maxSteps: 1,
    background: 'You are an agent that explains relativity.',
    tools: {}
  });

  const worker3 = agents.agent({
    model,
    name: 'worker3',
    maxSteps: 1,
    background: 'You are an agent that explains string theory.',
    tools: {}
  });

  // Await results
  const [result1, result2, result3] = await Promise.all([
    agents.task({ agent: worker1, prompt: "Explain quantum physics." }).run(),
    agents.task({ agent: worker2, prompt: "Explain relativity." }).run(),
    agents.task({ agent: worker3, prompt: "Explain string theory." }).run(),
  ]);

  // Aggregating results
  const aggregator = agents.agent({
    model,
    name: 'aggregator',
    maxSteps: 1,
    background: 'You are an agent that summarizes multiple answers.',
    tools: {}
  });

  const task = await agents.task({
    agent: aggregator,
    prompt: `Summarize these three explanations: ${result1.text}, ${result2.text}, ${result3.text}`
  })
  const finalSummary = await task.run();

  console.log(finalSummary.text);
});

```

You can also see how the same thing can be achieved using an manager agent in [orchestrator-workers example](/workflow/agents/patterns/orchestrator-workers).

<img src="https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/logs/logs-parallel.png?fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=d77a76d3ecd3e82cda89da7e2115f4b1" data-og-width="1434" width="1434" data-og-height="622" height="622" data-path="img/workflow/agents/logs/logs-parallel.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/logs/logs-parallel.png?w=280&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=7abb49e99f1add232802f0f7274df800 280w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/logs/logs-parallel.png?w=560&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=8ec77a3ee56aba8e6f6dfbf45fb87b1c 560w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/logs/logs-parallel.png?w=840&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=646834d1ee837f7a3e6872234632f461 840w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/logs/logs-parallel.png?w=1100&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=cfd16d98af9a309c2b17d9a03a88644c 1100w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/logs/logs-parallel.png?w=1650&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=deb1ae1f7cea02570dbbed29d8acdfec 1650w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/logs/logs-parallel.png?w=2500&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=c6eb085d5559d66eca4dcf931d1c357b 2500w" />

In response to the prompt, our agents generate this response:

```
Quantum physics explores the behavior of very small particles, such as atoms and subatomic particles, in the strange world of quantum mechanics, where particles can exist in multiple states simultaneously. Key principles include superposition and entanglement, leading to technological advancements like quantum computers. Relativity, developed by Albert Einstein, consists of special relativity and general relativity, explaining the behavior of objects moving at high speeds and the warping of spacetime by massive objects. String theory proposes that the universe's fundamental building blocks are tiny vibrating strings, aiming to unify the four fundamental forces of nature and suggest extra dimensions beyond the familiar ones.
```

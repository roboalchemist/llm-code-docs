# Source: https://upstash.com/docs/workflow/agents/patterns/prompt-chaining.md

# Prompt Chaining

<img src="https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/diagram/prompt-chain-diagram.png?fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=9da3927de6a1ad5fb0f98f72cac0cf3e" data-og-width="2420" width="2420" data-og-height="558" height="558" data-path="img/workflow/agents/diagram/prompt-chain-diagram.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/diagram/prompt-chain-diagram.png?w=280&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=e9a735fdeb2b78dbf59354c452ac66a9 280w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/diagram/prompt-chain-diagram.png?w=560&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=f416bdab7c162b795d2f75d9cc1e6dcb 560w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/diagram/prompt-chain-diagram.png?w=840&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=540400910092635e06e56bdd43e2a1c6 840w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/diagram/prompt-chain-diagram.png?w=1100&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=58e8a04126d3d1cfa331b42c0773f93d 1100w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/diagram/prompt-chain-diagram.png?w=1650&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=fa20136d6c7b9505b6b4f475b5bf085c 1650w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/diagram/prompt-chain-diagram.png?w=2500&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=9dc6a4d288b55c9b854efb6b895f7ddc 2500w" />

This workflow involves chaining multiple LLM calls, where the output of one agent becomes the input for the next agent.

```ts  theme={"system"}
import { serve } from "@upstash/workflow/nextjs";
import { WikipediaQueryRun } from "@langchain/community/tools/wikipedia_query_run";

export const { POST } = serve(async (context) => {
  const model = context.agents.openai('gpt-3.5-turbo');

  const agent1 = context.agents.agent({
    model,
    name: 'firstAgent',
    maxSteps: 1,
    background: 'You are an agent that lists famous physicists.',
    tools: {}
  });

  const agent2 = context.agents.agent({
    model,
    name: 'secondAgent',
    // set to 2 as this agent will first request tools
    // and then summarize them:
    maxSteps: 2,
    background:
      'You are an agent that describes the work of' +
      ' the physicists listed in the previous prompt.',
    tools: {
      wikiTool: new WikipediaQueryRun({
        topKResults: 1,
        maxDocContentLength: 500,
      })
    }
  });

  const agent3 = context.agents.agent({
    model,
    name: 'thirdAgent',
    maxSteps: 1,
    background:
      'You are an agent that summarizes the ' +
      'works of the physicists mentioned previously.',
    tools: {}
  });

  // Chaining agents
  const firstOutput = await context.agents.task({
    agent: agent1,
    prompt: "List 3 famous physicists."
  }).run();

  const secondOutput = await context.agents.task({
    agent: agent2,
    prompt: `Describe the work of: ${firstOutput.text}`
  }).run();
  

  const { text } = await context.agents.task({
    agent: agent3,
    prompt: `Summarize: ${secondOutput.text}`
  }).run();

  console.log(text);
});
```

<img src="https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/logs/logs-chain.png?fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=3993f6d3eb9278bc17d2e6bbdab8e74f" data-og-width="1430" width="1430" data-og-height="852" height="852" data-path="img/workflow/agents/logs/logs-chain.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/logs/logs-chain.png?w=280&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=fee5c241e9288fc6379f7f42842f1e54 280w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/logs/logs-chain.png?w=560&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=98bd6c7e38a7692126c8c145e5bfa072 560w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/logs/logs-chain.png?w=840&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=c7556e42ee5f501d7a09de14a10699b5 840w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/logs/logs-chain.png?w=1100&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=f690b9860bb163f8f8f68bf4de3d034d 1100w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/logs/logs-chain.png?w=1650&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=ea4ee9de9daafb71ad2c679e108db74c 1650w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/logs/logs-chain.png?w=2500&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=3aca877adf2e30f1b95523f9d4657027 2500w" />

In response to the prompt, our agents generate this response:

```
Albert Einstein was a German physicist known for his theory of relativity and the famous equation E=mc^2. He made significant contributions to quantum mechanics and was awarded the Nobel Prize in Physics in 1921. 

Isaac Newton, an English polymath, was a key figure in the Scientific Revolution and the Enlightenment. He is famous for his laws of motion and universal gravitation, as outlined in his book "PhilosophiÃ¦ Naturalis Principia Mathematica."

Marie Curie, a Polish-French physicist and chemist, conducted pioneering research on radioactivity and was the first woman to win a Nobel Prize. She is the only person to win Nobel Prizes in two scientific fields and her work has had a lasting impact on physics and chemistry.
```

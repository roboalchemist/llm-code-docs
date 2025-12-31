# Source: https://upstash.com/docs/workflow/agents/patterns/orchestrator-workers.md

# Orchestrator-Workers

<img src="https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/diagram/orchestrator-diagram.png?fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=7c8aebde675a468301b2f3c136ab1ecd" data-og-width="2234" width="2234" data-og-height="842" height="842" data-path="img/workflow/agents/diagram/orchestrator-diagram.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/diagram/orchestrator-diagram.png?w=280&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=8fc7ae85a5d783ac46a41acc819ccb11 280w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/diagram/orchestrator-diagram.png?w=560&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=567d98e7e97f1ecd5de8c759288e6c65 560w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/diagram/orchestrator-diagram.png?w=840&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=d3176e7e279faac3cc5135333d2c57ca 840w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/diagram/orchestrator-diagram.png?w=1100&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=e97f8ea8a2f72f1bb43cd1554d4641ef 1100w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/diagram/orchestrator-diagram.png?w=1650&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=9527a8bfacd689c6925e7c5c19dec159 1650w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/diagram/orchestrator-diagram.png?w=2500&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=bbdc8e82d3fa5e902253ece140434df7 2500w" />

This workflow uses an orchestrator to direct multiple worker agents to handle different subtasks, then synthesizes their outputs.

```ts  theme={"system"}
import { serve } from "@upstash/workflow/nextjs";
import { WikipediaQueryRun } from "@langchain/community/tools/wikipedia_query_run";

const wikiTool = new WikipediaQueryRun({
  topKResults: 1,
  maxDocContentLength: 500,
})

export const { POST } = serve(async (context) => {
  const model = context.agents.openai('gpt-4o');

  // Worker agents
  const worker1 = context.agents.agent({
    model,
    name: 'worker1',
    tools: { wikiTool },
    maxSteps: 3,
    background: 'You are a worker agent that answers general questions about advanced physics.'
  });

  const worker2 = context.agents.agent({
    model,
    name: 'worker2',
    tools: { wikiTool },
    maxSteps: 3,
    background: 'You are a worker agent that answers questions about quantum mechanics.'
  });

  const worker3 = context.agents.agent({
    model,
    name: 'worker3',
    tools: { wikiTool },
    maxSteps: 3,
    background: 'You are a worker agent that answers questions about relativity.'
  });

  // Synthesizing results
  const task = context.agents.task({
    model,
    prompt: `Create a Q&A for advanced topics in physics`,
    agents: [worker1, worker2, worker3],
    maxSteps: 3,
  })
  const { text } = await task.run();

  console.log(text);
});
```

If you wish to manually use the model results instead of utilizing a [manager LLM](/workflow/agents/overview#multi-agents) as we did in this example, see the [parallelization example](/workflow/agents/patterns/parallelization)

<img src="https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/logs/logs-manager.png?fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=ee2002c8832b16d0c94dd4807bfbc58d" data-og-width="1290" width="1290" data-og-height="1386" height="1386" data-path="img/workflow/agents/logs/logs-manager.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/logs/logs-manager.png?w=280&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=973c6e8c45b96926995784ef35bfdf6c 280w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/logs/logs-manager.png?w=560&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=8ab23efb24eee13e5cf3145809d0db83 560w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/logs/logs-manager.png?w=840&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=62bc7677694fb9780b31059c51412d7f 840w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/logs/logs-manager.png?w=1100&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=0109884fcffd9941d8f7e494d5825b80 1100w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/logs/logs-manager.png?w=1650&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=71cbe64f7bf0cd0117fa9ce1592e7697 1650w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/logs/logs-manager.png?w=2500&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=a0e78ea6de5beabf3e6f2232c39a507a 2500w" />

In response to the prompt, the agents create the following response:

```
### Quantum Mechanics

**Q: What is quantum mechanics?**
A: Quantum mechanics is a fundamental theory in physics that describes the behavior of nature at the atomic and subatomic levels. It serves as the foundation for all quantum physics, including quantum chemistry, quantum field theory, quantum technology, and quantum information science.

**Q: What are some key principles of quantum mechanics?**
A: 
1. **Wave-Particle Duality**: Particles exhibit both wave-like and particle-like properties.
2. **Uncertainty Principle**: Certain pairs of physical properties, like position and momentum, cannot be simultaneously measured with arbitrary precision.
3. **Quantum Superposition**: A quantum system can exist in multiple states at once until it is measured.
4. **Quantum Entanglement**: Particles become interconnected such that the state of one influences the state of another, regardless of distance.
5. **Quantization**: Energy levels in quantum systems are discrete.
6. **Probability and Wave Functions**: Quantum systems are described by wave functions, which provide probabilities of finding a system in a particular state.
7. **Observer Effect**: Measurement affects the system being observed.

### Relativity

**Q: What is the theory of relativity?**
A: Developed by Albert Einstein, the theory of relativity encompasses two interrelated theories: special relativity and general relativity.

**Q: What is special relativity?**
A: Proposed by Einstein in 1905, special relativity addresses the relationship between space and time in the absence of gravity. It is based on two key postulates: the invariance of physical laws in all inertial frames and the constancy of the speed of light in a vacuum.

**Q: What is general relativity?**
A: Published by Einstein in 1915, general relativity is a geometric theory of gravitation. It describes gravity as a geometric property of space and time, or four-dimensional spacetime, and explains how massive objects cause a distortion in spacetime.

These topics challenge classical intuitions and have led to significant advancements in our understanding of the universe and the development of new technologies.
```

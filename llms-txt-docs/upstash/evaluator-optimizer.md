# Source: https://upstash.com/docs/workflow/agents/patterns/evaluator-optimizer.md

# Evaluator-Optimizer

<img src="https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/diagram/evaluator-diagram.png?fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=397ca67e5abd9c7a2a2adc010c53889d" data-og-width="1654" width="1654" data-og-height="740" height="740" data-path="img/workflow/agents/diagram/evaluator-diagram.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/diagram/evaluator-diagram.png?w=280&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=bc93c85c311f4cba37fc0176535284b0 280w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/diagram/evaluator-diagram.png?w=560&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=95a68c5e03c1b5ef8d4223eda31c0581 560w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/diagram/evaluator-diagram.png?w=840&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=8af28e72146c82aacc173da479c17a67 840w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/diagram/evaluator-diagram.png?w=1100&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=14a51520d0b8b163f790e2f2763eb389 1100w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/diagram/evaluator-diagram.png?w=1650&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=212f123c10cad13a8e607f4ef9d326b5 1650w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/diagram/evaluator-diagram.png?w=2500&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=60b59c783ea112d1c3df2cd731c2d6a3 2500w" />

In this example, the generator creates output and passes it to the evaluator, which evaluates the response. If the evaluation fails, the evaluator returns corrections, and the generator is called again using the corrected output.

```ts  theme={"system"}
import { serve } from "@upstash/workflow/nextjs";

export const { POST } = serve(async (context) => {
  const model = context.agents.openai('gpt-3.5-turbo');

  // Generator agent that generates content
  const generator = context.agents.agent({
    model,
    name: 'generator',
    maxSteps: 1,
    background: 'You are an agent that generates text based on a prompt.',
    tools: {}
  });

  // Evaluator agent that evaluates the text and gives corrections
  const evaluator = context.agents.agent({
    model,
    name: 'evaluator',
    maxSteps: 1,
    background: 'You are an agent that evaluates the generated text and provides corrections if needed.',
    tools: {}
  });

  let generatedText = '';
  let evaluationResult = '';

  const prompt = "Generate a short explanation of quantum mechanics.";
  let nextPrompt = prompt;
  for (let i = 0; i < 3; i++) {
    // Construct prompt for generator: 
    // - If there's no evaluation, use the original prompt
    // - If there's an evaluation, provide the prompt, the last generated text, and the evaluator's feedback
    if (evaluationResult && evaluationResult !== "PASS") {
      nextPrompt = `Please revise the answer to the question "${prompt}". Previous answer was: "${generatedText}", which received this feedback: "${evaluationResult}".`;
    }

    // Generate content
    const generatedResponse = await context.agents.task({ agent: generator, prompt: nextPrompt }).run();
    generatedText = generatedResponse.text

    // Evaluate the generated content
    const evaluationResponse = await context.agents.task({ agent: evaluator, prompt: `Evaluate and provide feedback for the following text: ${generatedText}` }).run();
    evaluationResult = evaluationResponse.text

    // If the evaluator accepts the content (i.e., "PASS"), stop
    if (evaluationResult.includes("PASS")) {
      break;
    }
  }

  console.log(generatedText);
});
```

<img src="https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/logs/logs-evaluator.png?fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=a4233550ccd453181bf070f154f0eb52" data-og-width="1418" width="1418" data-og-height="704" height="704" data-path="img/workflow/agents/logs/logs-evaluator.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/logs/logs-evaluator.png?w=280&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=07ae6cc3eb68aae8f842c76bdbbe183d 280w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/logs/logs-evaluator.png?w=560&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=6233eca76ffa2ed033845fdf43505f5d 560w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/logs/logs-evaluator.png?w=840&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=83df7e9e7ae90ee6dc28161a55e488e1 840w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/logs/logs-evaluator.png?w=1100&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=f692b301051ab223c07a884bb6169268 1100w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/logs/logs-evaluator.png?w=1650&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=c1e97fa08c6cbbf404cbc3ed6c6e9031 1650w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/agents/logs/logs-evaluator.png?w=2500&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=876e3b25c1de8b0f8bc1ff79c85505bd 2500w" />

In response to the prompt, our agents generate this response:

```
Quantum mechanics is a branch of physics that describes the behavior of particles at the smallest scales, such as atoms and subatomic particles. It introduces the concept of quantized energy levels, wave-particle duality, and probabilistic nature of particles. In quantum mechanics, particles can exist in multiple states simultaneously until measured, and their behavior is governed by mathematical equations known as wave functions. This theory has revolutionized our understanding of the fundamental building blocks of the universe and has led to the development of technologies like quantum computing and quantum cryptography.
```

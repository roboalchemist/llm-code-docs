# Source: https://www.traceloop.com/docs/evaluators/made-by-traceloop.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Made by Traceloop

> Pre-configured evaluators by Traceloop for common assessment tasks

The Evaluator Library provides a comprehensive collection of pre-built quality checks designed to systematically assess AI outputs.

Each evaluator comes with a predefined input and output schema. When using an evaluator, you’ll need to map your data to its input schema.

<Frame>
  <img className="block dark:hidden" src="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-made-by-traceloop-light.png?fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=99441f9ee05624cc1167e7a16600984d" data-og-width="2384" width="2384" data-og-height="1392" height="1392" data-path="img/evaluator/eval-made-by-traceloop-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-made-by-traceloop-light.png?w=280&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=863a4cbc9f32a775330a81753846313f 280w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-made-by-traceloop-light.png?w=560&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=90493bcf908dccfe98033df5489b229b 560w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-made-by-traceloop-light.png?w=840&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=72786af4c0b9cb5f780c6d4139778331 840w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-made-by-traceloop-light.png?w=1100&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=e5a988662851764167696fd4f2fc6d0b 1100w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-made-by-traceloop-light.png?w=1650&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=219cef3045bdbde62af03b1236858644 1650w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-made-by-traceloop-light.png?w=2500&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=d7aef7cacb08ee41d95fa53209e99140 2500w" />

  <img className="hidden dark:block" src="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-made-by-traceloop-dark.png?fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=dfc7496c9b2afb1128a3af59bf90a68f" data-og-width="2378" width="2378" data-og-height="1374" height="1374" data-path="img/evaluator/eval-made-by-traceloop-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-made-by-traceloop-dark.png?w=280&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=1020f0b2e654def7f388cc45c153948b 280w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-made-by-traceloop-dark.png?w=560&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=bd3ad3305814b1ef2a85cd60687f35b2 560w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-made-by-traceloop-dark.png?w=840&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=f775454161783c264fc19afc62c7959e 840w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-made-by-traceloop-dark.png?w=1100&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=20b4100bfeb4b2a2bcea871be7aefd3b 1100w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-made-by-traceloop-dark.png?w=1650&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=f6c63389550d078e4874fa2c168dec42 1650w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-made-by-traceloop-dark.png?w=2500&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=af33b371245f886a5bfc80bd55252475 2500w" />
</Frame>

## Evaluator Types

### Style

<CardGroup cols={3}>
  <Card title="Character Count" icon="text">
    Analyze response length and verbosity to ensure outputs meet specific length requirements.
  </Card>

  <Card title="Character Count Ratio" icon="hashtag">
    Measure the ratio of characters to the input to assess response proportionality and expansion.
  </Card>

  <Card title="Word Count" icon="align-left">
    Ensure appropriate response detail level by tracking the total number of words in outputs.
  </Card>

  <Card title="Word Count Ratio" icon="hashtag">
    Measure the ratio of words to the input to compare input/output verbosity and expansion patterns.
  </Card>
</CardGroup>

### Quality & Correctness

<CardGroup cols={3}>
  <Card title="Answer Relevancy" icon="bullseye">
    Verify responses address the query to ensure AI outputs stay on topic and remain relevant.
  </Card>

  <Card title="Faithfulness" icon="circle-check">
    Detect hallucinations and verify facts to maintain accuracy and truthfulness in AI responses.
  </Card>

  <Card title="Answer Correctness" icon="circle-check">
    Evaluate factual accuracy by comparing answers against ground truth.
  </Card>

  <Card title="Answer Completeness" icon="circle-check">
    Measure how completely responses use relevant context to ensure all relevant information is addressed.
  </Card>

  <Card title="Topic Adherence" icon="hashtag">
    Validate topic adherence to ensure responses stay focused on the specified subject matter.
  </Card>

  <Card title="Semantic Similarity" icon="hashtag">
    Validate semantic similarity between expected and actual responses to measure content alignment.
  </Card>

  <Card title="Instruction Adherence" icon="clipboard-check">
    Measure how well the LLM response follows given instructions to ensure compliance with specified requirements.
  </Card>

  <Card title="Measure Perplexity" icon="hashtag">
    Measure text perplexity from logprobs to assess the predictability and coherence of generated text.
  </Card>

  <Card title="Uncertainty Detector" icon="gauge">
    Generate responses and measure model uncertainty from logprobs to identify when the model is less confident in its outputs.
  </Card>

  <Card title="Conversation Quality" icon="comments">
    Evaluate conversation quality based on tone, clarity, flow, responsiveness, and transparency.
  </Card>

  <Card title="Context Relevance" icon="hashtag">
    Validate context relevance to ensure retrieved context is pertinent to the query.
  </Card>
</CardGroup>

### Security & Compliance

<CardGroup cols={3}>
  <Card title="PII Detection" icon="shield">
    Identify personal information exposure to protect user privacy and ensure data security compliance.
  </Card>

  <Card title="Profanity Detection" icon="triangle-exclamation">
    Flag inappropriate language use to maintain content quality standards and professional communication.
  </Card>

  <Card title="Sexism Detection" icon="triangle-exclamation">
    Detect sexist and discriminatory content.
  </Card>

  <Card title="Prompt Injection" icon="shield-exclamation">
    Detect prompt injection attacks in user inputs.
  </Card>

  <Card title="Toxicity Detector" icon="skull">
    Detect toxic content including personal attacks, mockery, hate, and threats.
  </Card>

  <Card title="Secrets Detection" icon="lock">
    Monitor for credential and key leaks to prevent accidental exposure of sensitive information.
  </Card>
</CardGroup>

### Formatting

<CardGroup cols={3}>
  <Card title="SQL Validation" icon="database">
    Validate SQL queries to ensure proper syntax and structure in database-related AI outputs.
  </Card>

  <Card title="JSON Validation" icon="code">
    Validate JSON responses to ensure proper formatting and structure in API-related outputs.
  </Card>

  <Card title="Regex Validation" icon="asterisk">
    Validate regex patterns to ensure correct regular expression syntax and functionality.
  </Card>

  <Card title="Placeholder Regex" icon="asterisk">
    Validate placeholder regex patterns to ensure proper template and variable replacement structures.
  </Card>
</CardGroup>

### Agents

<CardGroup cols={3}>
  <Card title="Agent Goal Accuracy" icon="bullseye">
    Validate agent goal accuracy to ensure AI systems achieve their intended objectives effectively.
  </Card>

  <Card title="Agent Tool Error Detector" icon="wrench">
    Detect errors or failures during tool execution to monitor agent tool performance.
  </Card>

  <Card title="Agent Flow Quality" icon="route">
    Validate agent trajectories against user-defined natural language tests to assess agent decision-making paths.
  </Card>

  <Card title="Agent Efficiency" icon="zap">
    Evaluate agent efficiency by checking for redundant calls and optimal paths to optimize agent performance.
  </Card>

  <Card title="Agent Goal Completeness" icon="circle-check">
    Measure whether the agent successfully accomplished all user goals to verify comprehensive goal achievement.
  </Card>

  <Card title="Intent Change" icon="repeat">
    Detect whether the user's primary intent or workflow changed significantly during a conversation.
  </Card>
</CardGroup>

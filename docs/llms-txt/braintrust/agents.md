# Source: https://braintrust.dev/docs/core/functions/agents.md

# Source: https://braintrust.dev/docs/best-practices/agents.md

# Evaluating agents

Agent-based systems are inherently complex because they often break down tasks into multiple steps to reach a final result. Some agents operate almost entirely autonomously,
repeatedly leveraging available tools to find a satisfactory answer, while others follow more predefined, static workflows. Regardless of the approach, it’s important to
evaluate these systems both as a whole (*for example, did the agent’s plan make sense, and was the final answer correct?*) and at each individual step (*for example, did the
agent choose the right tool, did the retrieval component provide relevant information, and in multi-agent setups, did it direct the request to the correct model or sub-agent?*).

Evaluating agents can range from targeted unit-like tests to comprehensive end-to-end scenarios. Here’s how to structure those evaluations specifically tailored to agent-based
AI systems, ranging from simple to complex.

## Key questions for evaluating agents

When evaluating sophisticated agent behaviors, ask questions like:

* If the agent starts by providing a plan of actions to take in answering the user's query, does that plan make sense given the user's objective?
* If the agent provides reasoning steps, are those intermediate thoughts expected?
* Did the agent choose the correct next step or defer to a human as expected?
* Did the agent invoke the correct tools?
* When invoking a tool, did the agent properly build up the arguments to invoke it?
* When examining a tool's output, did the agent properly utilize it to provide an answer or move to the next expected step?

<Note>
  Errors can surface at any point in an agentic system. To debug and understand these errors it's important to capture the inputs at each step as well as the outputs.
</Note>

## Types of evaluations

### Offline evaluations

Offline evaluations proactively identify issues in agent behavior before deployment. These function similarly to unit tests or integration tests, emphasizing reproducibility and stability.
You can use datasets to test both the end-to-end performance of your agent and its intermediate steps. For instance, you might create a specific dataset to test a retrieval step in a RAG pipeline, or one that checks whether generated SQL adheres to security constraints.
Once you’ve created a “golden dataset” with ground truth examples, you can apply either code-based scorers or LLM-as-a-judge scorers to evaluate outputs systematically.

**Recommended approach:**

* **Stub external dependencies**: Snapshot sufficient state from production or staging environments to simulate databases, APIs, and infrastructure.
* **Isolate specific agent actions**: Create deterministic scenarios to evaluate critical behaviors reliably.
* **Assess incremental behavior**: Evaluate individual agent steps, including tool calls, parameter accuracy, and responses.

### Online evaluations

Online evaluations continuously monitor real-time performance, capturing live user interactions, and diagnosing issues as they arise. Here, there is no ground truth to evaluate the overall
performance of the agent or any of its steps, so in general, we rely on LLM-as-a-judge scorers for evaluation.

**Recommended approach:**

* **Real environment usage**: Always evaluate in your actual production environment for accurate user experience insights.

* **Incorporate user feedback**: Allow users to like or dislike agent responses and provide comments. This can be invaluable for error analysis and informed sampling traces for evaluation.
  Refer to the [user feedback](/core/logs/write#user-feedback) docs for implementation details.

* **Real-time scoring**: Implement continuous monitoring for key behaviors like hallucinations, tool accuracy, and goal completion.
  More information is available in the [online scoring](/core/experiments/write#online-evaluation) documentation.

* **Adaptive sampling**: Start by scoring all requests, then adjust sample rates based on agent stability and usage volume.
  For details on how to control sampling from your logs, check out the [online scoring](/core/experiments/write#online-evaluation) docs.

* **Feedback integration**: Use both low-scoring and anomalously high-scoring examples to feed new test scenarios into offline evaluations.

## Structuring agent evaluations

**End-to-end**:

* Use real or simulated environments to evaluate complete task flows.
* Focus on goal success, coherence, and robustness.

If you need to incorporate intermediate results in your agents to evaluate the final result, you can use the [`hooks` argument](/core/experiments/write#additional-metadata) in your eval's task function to add the results to your
trace's metadata, which can then be used in any of your eval's scorers to evaluate the final output, like this:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  export async function taskFunc(input, hooks) {
    // ..
    if (rsp.choices[0].finish_reason === "tool_calls") {
      const toolCalls = rsp.choices[0].message.tool_calls;
      hooks.metadata.tool_calls = toolCalls;
    }
    // ...
  }
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  async def task_func(input: str, hooks=None) -> str:
      # ...
      if rsp.choices[0].finish_reason == "tool_calls":
          tool_calls = rsp.choices[0].message.tool_calls
          hooks.metadata["tool_calls"] = tool_calls

  # ...
  ```
</CodeGroup>

**Single-step**:

* Use snapshotted scenarios with stubbed infrastructure to test specific decisions in isolation.
* Make sure you include the inputs from the preceding step as sometimes a "step failure" may really be due to a problem with the previous step's output.
* Target precise behaviors, ensuring reproducibility and reliability.

You can accomplish this by including "inline scorers" into your code. For example, you can run an inline scorer only if the agent
chooses to initiate a `tool call`:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  if (!res.choices[0].message.tool_calls?.length) {
    // Start hallucination scoring in the background (fire-and-forget)
    runHallucinationScore({
      question: message,
      answer: res.choices[0].message.content,
      context: documents,
    });
    break;
  }
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  # ...
  if not res.choices[0].message.tool_calls:
      run_hallucination_score(question=message, answer=res.choices[0].message.content, context=documents)
      break
  # ...
  ```
</CodeGroup>

<Tip>
  To see the full example, check out the [API Agent cookbook](/cookbook/recipes/APIAgent-Py).
</Tip>

For more complex and interrelated tool calling scenarios, this idea can be extended. For example, imagine one tool first generates SQL, a second tool executes that SQL, and a third tool translates the results into plain language. By attaching a separate inline scorer to each stage, you'll have the granular feedback needed to pinpoint and analyze errors in every part of your agent pipeline.

### Additional resources

* [An agent that runs OpenAPI commands](/cookbook/recipes/APIAgent-Py)
* [Using functions to build a RAG agent](/cookbook/recipes/ToolRAG)
* [A field guide to rapidly improving AI products](https://hamel.dev/blog/posts/field-guide/)

## Designing comprehensive agent evaluations

For agents managing complex, multi-step interactions, make sure evaluations account for variability and context-dependence:

* **Snapshotting state**: Capture tool calls and responses from live environments for accurate offline evaluation scenarios.
* **Incremental assessment**: Evaluate each step individually to manage non-deterministic agent interactions effectively.
* **Goal-oriented evaluation**: For complex sequences, prioritize evaluations based on the agent's ultimate success or failure in achieving its intended outcome.

## Evolving your evaluation suite

Evaluations should evolve alongside your agent’s behavior and product goals.

<Steps>
  <Step title="Start with simple scenarios">
    Start with simple scenarios, using stubbed environments to isolate key decisions.
  </Step>

  <Step title="Add complex flows">
    Add complex flows using simulated or real data to test agents under realistic conditions.
  </Step>

  <Step title="Define custom success criteria">
    For data-intensive agents (for example, manipulating and loading data into databases), define custom success criteria, like:

    * Schema compliance
    * Data transformation correctness
    * Deterministic output formats
  </Step>

  <Step title="Use continuous feedback loops">
    * Iterate on scorers
    * Expand your dataset coverage
    * Adapt to new agent workflows
  </Step>
</Steps>

By combining offline and online evaluations, and balancing end-to-end testing with single-step checks, you’ll build a solid evaluation architecture. You'll be able to catch issues early, debug faster, and continuously improve your agent based on real-world user expectations.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt
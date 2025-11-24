# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/how-to/evaluate-and-optimize-agents--chains-or-multi-step-workflows.md

# Evaluate and Optimize Agents

> How to use Galileo Evaluate with Agents

Galileo Evaluate helps you evaluate and optimize Agents with out-of-the-box Tracing and Analytics. Galileo allows you to run and log experiments, trace all the steps taken by your Agent, and use [Galileo Preset](/galileo/gen-ai-studio-products/galileo-guardrail-metrics) or [Custom Metrics](/galileo/gen-ai-studio-products/galileo-evaluate/how-to/choose-your-guardrail-metrics) to evaluate and debug your end-to-end system .

## Getting Started

The first step in evaluating your application is creating an evaluation run. To do this, run your evaluation set (e.g. a set of inputs that mimic the inputs you expect to get from users) through your Agent create a run.

Follow our instructions on how to [Integrate Evaluate into your existing application](/galileo/gen-ai-studio-products/galileo-evaluate/integrations).

## Tracing and Visualizing your Agent

Once you log your evaluation runs, you can go to the Galileo Console to analyze your Agent executions. For each execution, you'll be able to see what the input into the workflow was and what the final response was, as well as any steps of decisions taken to get to the final result.

![](https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/e-op.png)

Clicking on any row on the table will open the Expanded View for that workflow or step. You can dig through the steps that your Agent took to understand how it got to the final response, and trace any mistakes back to an incorrect step.

![](https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/ev-op-2.png)

## Metrics

Galileo has [Galileo Preset Metrics](/galileo/gen-ai-studio-products/galileo-guardrail-metrics) to help you evaluate and debug application. In addition, Galileo supports user-defined [custom metrics](/galileo/gen-ai-studio-products/galileo-evaluate/how-to/choose-your-guardrail-metrics). When logging your evaluation run, make sure to include the metrics you want computed for your run.

More information on how to [evaluate and debug them on the console](/galileo/gen-ai-studio-products/galileo-observe/how-to/identifying-and-debugging-issues).

For Agents, the metrics we recommend to use are:

* [Action Completion](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/action-completion): A metric at the session level detecting whether the agent successfully accomplished all user's goals. This metric will show use-cases where the Agent is not able to fully help the user in all of its tasks.

* [Action Advancement](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/action-advancement): A metric at the workflow level detecting whether the agent successfully accomplished or advanced towards at least one user goal. This metric will show use-cases where the Agent is not able to help the user in any of its tasks.

* [Tool Selection Quality](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/tool-selection-quality): A metric on your LLM steps that detects whether the correct Tool and Parameters were chosen by the LLM. When you use LLMs to determine the sequence of steps that happen in your Agent, this metric will help you find 'planning' errors in your Agent.

* [Tool Errors](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/tool-error): A metric on your Tool steps that detects whether they executed correctly. Tools are a common building block for Agents. Detecting errors and patterns in those errors is an important step in your debugging journey.

* [Instruction Adherence](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/instruction-adherence): A metric on your LLM steps that measures whether the LLM followed its instructions.

* [Context Adherence](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/context-adherence): If your Agent uses a Retriever or has summarization steps, this metric can help detect hallucinations or ungrounded facts in the response.

You can always create or generate your own Metric for your use case, or tailor any of these metrics via Continuous Learning via Human Feedback (CLHF).

## Iterative Experimentation

Now that you've identified something wrong with your Chain or Agent, try to change your chain or agent configuration, prompt template, or model settings and re-run your evaluation under the same project. Your project view will allow you to quickly compare evaluation runs and see which [configuration](/galileo/gen-ai-studio-products/galileo-evaluate/how-to/evaluate-and-optimize-agents--chains-or-multi-step-workflows#keeping-track-of-what-changed-in-your-experiment) of your system worked best.

#### Keeping track of what changed in your experiment

As you start experimenting, you're going to want to keep track of what you're attempting with each experiment. To do so, use Prompt Tags. Prompt Tags are tags you can add to the run (e.g. "agent\_architecture" = "voyage-2", "agent\_architecture" = "reflexion").

Prompt Tags will help you remember what you tried with each experiment. Read more about [how to add Prompt Tags here](/galileo/gen-ai-studio-products/galileo-evaluate/how-to/add-tags-and-metadata-to-prompt-runs).

# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/how-to/evaluate-and-optimize-agents--chains-or-multi-step-workflows.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Evaluate and Optimize Agents

> How to use Galileo Evaluate with Agents

Galileo Evaluate helps you evaluate and optimize Agents with out-of-the-box Tracing and Analytics. Galileo allows you to run and log experiments, trace all the steps taken by your Agent, and use [Galileo Preset](/galileo/gen-ai-studio-products/galileo-guardrail-metrics) or [Custom Metrics](/galileo/gen-ai-studio-products/galileo-evaluate/how-to/choose-your-guardrail-metrics) to evaluate and debug your end-to-end system .

## Getting Started

The first step in evaluating your application is creating an evaluation run. To do this, run your evaluation set (e.g. a set of inputs that mimic the inputs you expect to get from users) through your Agent create a run.

Follow our instructions on how to [Integrate Evaluate into your existing application](/galileo/gen-ai-studio-products/galileo-evaluate/integrations).

## Tracing and Visualizing your Agent

Once you log your evaluation runs, you can go to the Galileo Console to analyze your Agent executions. For each execution, you'll be able to see what the input into the workflow was and what the final response was, as well as any steps of decisions taken to get to the final result.

<img src="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/e-op.png?fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=c141d71ab86c31a35c1c721c4f3f96c6" alt="" data-og-width="3022" width="3022" data-og-height="1040" height="1040" data-path="images/e-op.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/e-op.png?w=280&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=ec63ead06aa46e8ee779552623c043d9 280w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/e-op.png?w=560&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=ee52d7336acffc6996caaaa10852fdba 560w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/e-op.png?w=840&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=f06ceeba565e45f60d50a70ce880699a 840w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/e-op.png?w=1100&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=011188465798002f3fb70a37556aded9 1100w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/e-op.png?w=1650&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=9b0684d6cdd8f9d2ead2e44ad918e2ee 1650w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/e-op.png?w=2500&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=1ca5dea6fff46789b179e8cec0dda05a 2500w" />

Clicking on any row on the table will open the Expanded View for that workflow or step. You can dig through the steps that your Agent took to understand how it got to the final response, and trace any mistakes back to an incorrect step.

<img src="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/ev-op-2.png?fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=0d02d297206c20cf67a72081dee501f4" alt="" data-og-width="3022" width="3022" data-og-height="1196" height="1196" data-path="images/ev-op-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/ev-op-2.png?w=280&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=57e7bb002ff5f1a6d6b3d9f9de02a519 280w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/ev-op-2.png?w=560&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=e56db4e755baeaf2b448ecc29e06ab62 560w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/ev-op-2.png?w=840&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=ec7d807ccbba9e4b7cb10c6111dcd58d 840w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/ev-op-2.png?w=1100&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=b33f7c0ad69500ae6162e56df8cf4fe1 1100w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/ev-op-2.png?w=1650&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=52a109b6541c1c0f6598b66b71eddfe8 1650w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/ev-op-2.png?w=2500&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=6402a4554c7961ddf227b6cc7c38765e 2500w" />

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

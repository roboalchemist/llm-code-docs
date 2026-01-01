# Source: https://www.traceloop.com/docs/evaluators/intro.md

# Introduction

> Evaluating workflows and LLM outputs

The evaluation library is a core feature of Traceloop, providing comprehensive tools to assess LLM outputs, data quality, and performance across various dimensions. Whether you need automated scoring or human judgment, the evaluation system has you covered.

## Why Do We Need Evaluators?

LLM agents are more complex than single-turn completions.
They operate across multiple steps, use tools, and depend on context and external systems like memory or APIs. This complexity introduces new failure modes: agents may hallucinate tools, get stuck in loops, or produce final answers that hide earlier mistakes.

Evaluators make these issues visible by checking correctness, relevance, task completion, tool usage, memory retention, safety, and style. They ensure outputs remain consistent even when dependencies shift and provide a structured way to measure reliability. Evaluation is continuous, extending into production through automated tests, drift detection, quality gates, and online monitoring.
In short, evaluators turn outputs into trustworthy systems by providing measurable and repeatable checks that give teams confidence to deploy at scale.

## Evaluators types

The system supports:

* **Custom evaluators** - Create your own evaluation logic tailored to specific needs
* **Built-in evaluators** - pre-configured evaluators by Traceloop for common assessment tasks

In the Evaluator Library, select the evaluator you want to define.
You can either create a custom evaluator by clicking **New Evaluator** or choose one of the prebuilt **Made by Traceloop** evaluators.

<Frame>
  <img className="block dark:hidden" src="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-library-light.png?fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=7d69270c64122e6a882daf930897f366" data-og-width="2370" width="2370" data-og-height="1376" height="1376" data-path="img/evaluator/eval-library-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-library-light.png?w=280&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=ef654f37807e63377669e10984393ca5 280w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-library-light.png?w=560&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=c7ca9fab7c0efb3644a7274bd4a2ce2c 560w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-library-light.png?w=840&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=1ebe5ab46ad2c7c6f9ac9b25bbe658c8 840w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-library-light.png?w=1100&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=2dc1fe885e05646d2912579a094f0e76 1100w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-library-light.png?w=1650&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=7820d08b52f57a5216b2b69001ba8818 1650w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-library-light.png?w=2500&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=9c025d919d874f1b57fa39990aa8df32 2500w" />

  <img className="hidden dark:block" src="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-library-dark.png?fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=fd362fa828c219fe2647f2d9594bd039" data-og-width="2378" width="2378" data-og-height="1376" height="1376" data-path="img/evaluator/eval-library-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-library-dark.png?w=280&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=fe221ba4669f635f43bf6df7c132b202 280w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-library-dark.png?w=560&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=90972a83cde649c3b60598ea0ca63e3b 560w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-library-dark.png?w=840&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=2bc3fdfe6ed6107b6b9a2d3fe0107e67 840w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-library-dark.png?w=1100&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=88d2ebf74a717077350d553d191fa679 1100w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-library-dark.png?w=1650&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=283084a4f50c8136336fce23a8f42ab3 1650w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/evaluator/eval-library-dark.png?w=2500&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=93db1be0b94703920a1c6c17e57753c9 2500w" />
</Frame>

Clicking on existing evaluators will present their input and output schema. This is valuable information in order to execute the evaluator [through the SDK](../experiments/running-from-code).

## Where to Use Evaluators

Evaluators can be used in multiple contexts within Traceloop:

* **[Guardrails](./guardrails)** - Apply evaluators in real-time as inline safety checks and quality gates that run synchronously with your application code to prevent issues before they reach users
* **[Playgrounds](../playgrounds/quick-start)** - Test and iterate on your evaluators interactively, compare different configurations, and validate evaluation logic before deployment
* **[Experiments](../experiments/introduction)** - Run systematic evaluations across datasets programmatically using the SDK, track performance metrics over time, and easily compare experiment results
* **[Monitors](../monitoring/introduction)** - Continuously evaluate your LLM applications in production with real-time monitoring and alerting on quality degradation


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://www.traceloop.com/docs/llms.txt
# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/how-to/enabling-scorers-in-runs.md

# Enabling Scorers in Runs

> Learn how to turn on metrics when creating runs in your Python environment.

Galileo provides users the ability to tune which metrics to use for their evaluation.

<Info>Check out [Choose your Guardrail Metrics](/galileo/gen-ai-studio-products/galileo-evaluate/how-to/choose-your-guardrail-metrics) to understand which metrics or scorers apply to your use case.</Info>

## Using scorers

To use scorers during a prompt run, sweep, or even a more complex workflow, simply pass them in through the scorers argument:

```py

import promptquality as pq

pq.run(..., scorers=[pq.Scorers.correctness, pq.Scorers.context_adherence])
```

## Disabling default scorers

By default, we turn on a few scorers for you (PII, Toxicity, BLEU, ROUGE). If you want to disable a default scorer you can pass in a ScorersConfiguration object.

```py

pq.run(...,
  scorers=[pq.Scorers.correctness,pq.Scorers.context_adherence],
  scorers_config=pq.ScorersConfiguration(latency=False)
  )
```

You can even use the ScorersConfiguration to turn on other scorers, rather than using the scorers argument.

```py
  pq.run(..., scorers_config=pq.ScorersConfiguration(latency=False, groundedness=True))
```

## Logging Workflows

If you're logging workflows using [EvaluateRun](https://promptquality.docs.rungalileo.io/#promptquality.EvaluateRun), you can add your scorers similarly:

```py
evaluate_run = pq.EvaluateRun(run_name="my_run", project_name="my_project", scorers=[pq.Scorers.correctness, pq.Scorers.context_adherence])
```

## Customizing Plus Scorers

We allow customizing execution parameters for the [Chainpoll](/galileo/gen-ai-studio-products/galileo-ai-research/chainpoll)-powered metrics from our Guardrail Store. Check out [Customizing Chainpoll-powered Metrics](/galileo/gen-ai-studio-products/galileo-evaluate/how-to/customize-chainpoll-powered-metrics).

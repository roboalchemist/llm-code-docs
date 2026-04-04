# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-protect/concepts/rule.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Rule

> A condition or rule you never want your application to break. It's composed of three ingredients

* A metric

* An operator

* A target value

Your Rules should evaluate to False for the base case, and to True for unwanted scenarios.

In the example above, the "*input/output shall never contain PII*" is encoded into a Rule like below:

```
{
  "metric": "pii",
  "operator": "contains",
  "target_value": "ssn",
},
```

Or:

```py  theme={null}
gp.Rule(
    metric=gp.RuleMetrics.pii,
    operator=gp.RuleOperator.contains,
    target_value="ssn"
)
```

## Rules and Metrics

Each metric requires a specific operator and target value to be compared against. An exhaustive list of metrics supported along with the operators and target values can be found [here](/galileo/gen-ai-studio-products/galileo-protect/how-to/supported-metrics-and-operators).

At runtime, the rule is compared with the provided payload, and the metric is computed. If all of the rules are triggered, the ruleset is triggered and the action is applied.

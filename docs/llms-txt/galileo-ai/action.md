# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-protect/concepts/action.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Action

> Galileo will provide a set of action types (override, passthrough), that the user can use, along with a configuration for each action type.

Actions are user-defined actions that are taken as a result of the [ruleset](/galileo/gen-ai-studio-products/galileo-protect/concepts/ruleset) being triggered.

An Action can be defined as:

```python  theme={null}
gp.OverrideAction(
    choices=["Sorry, I cannot answer that question."]
)
```

The action would be included in the ruleset definition as:

```py  theme={null}
gp.Ruleset(
    rules=[
        gp.Rule(
            metric=gp.RuleMetrics.pii,
            operator=gp.RuleOperator.contains,
            target_value="ssn"
        ),
        gp.Rule(
            metric=gp.RuleMetrics.toxicity,
            operator=gp.RuleOperator.gt,
            target_value=0.8
        )
    ],
    action=gp.OverrideAction(
        choices=["Sorry, I cannot answer that question."]
    )
)
```

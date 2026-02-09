# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-protect/concepts/ruleset.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Ruleset

> All of the Rules within a Ruleset are executed in parallel, and the final resolution depends on all of the rules being completed.

A Ruleset is a collection of one or more [Rules](/galileo/gen-ai-studio-products/galileo-protect/concepts/rule) combined with an Action. The Ruleset gets triggered when all of the rules are broken (i.e. all their condition evaluate to True). Rules are AND-ed together, not OR-ed, so all of them have to be True for the Ruleset to *Trigger*.

For example, a ruleset can be defined as "PII metric contains SSN AND toxicity greater than 0.8". This ruleset would be triggered if the output text was detected to contain an SSN and the toxicity of the output text was greater than 0.8.

The order in which Rulesets appear in the list matters. Only one Action gets taken In the example above, the ruleset is the list of Guardrail metrics stored in `prioritized_rulesets`.

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
)
```

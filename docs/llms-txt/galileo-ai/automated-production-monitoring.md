# Source: https://docs.galileo.ai/galileo/galileo-nlp-studio/text-classification/automated-production-monitoring.md

# Automated Production Monitoring

> Monitor text classification models in production with automated tools from Galileo NLP Studio to detect data drift and maintain performance.

![](https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/nlp-predicate.png)

Leverage all the Galileo 'building blocks' that are logged and stored for you to create Tests using Galileo Conditions -- a class for building custom data quality checks.

Conditions are simple and flexible, allowing you to author powerful data/model tests.

## Run Report

Integrate with email or slack to automatically receive a report of Condition outcomes after a run finishes processing.

![](https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/nlp-monitoring-report.png)

## Examples

```py

    Example 1: Alert if over 50% of high DEP (>=0.7) data contains PII

        >>> c = Condition(
        ...     operator=Operator.gt,
        ...     threshold=0.5,
        ...     agg=AggregateFunction.pct,
        ...     filters=[
        ...         ConditionFilter(
        ...             metric="data_error_potential", operator=Operator.gte, value=0.7
        ...         ),
        ...         ConditionFilter(
        ...             metric="galileo_pii", operator=Operator.neq, value="None"
        ...         ),
        ...     ],
        ... )
        >>> dq.register_run_report(conditions=[c])
```

```py

    Example 2: Alert if at least 20% of the dataset has drifted (Inference DataFrames only)

        >>> c = Condition(
        ...     operator=Operator.gte,
        ...     threshold=0.2,
        ...     agg=AggregateFunction.pct,
        ...     filters=[
        ...         ConditionFilter(
        ...             metric="is_drifted", operator=Operator.eq, value=True
        ...         ),
        ...     ],
        ... )
        >>> dq.register_run_report(conditions=[c])
```

{" "}

<Icon icon="bolt" />

[Get started](/galileo/galileo-nlp-studio/text-classification/build-your-own-conditions) building your own Reports with Galileo Conditions

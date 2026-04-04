# Source: https://docs.galileo.ai/galileo/galileo-nlp-studio/text-classification/automated-production-monitoring.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Automated Production Monitoring

> Monitor text classification models in production with automated tools from Galileo NLP Studio to detect data drift and maintain performance.

<img src="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/nlp-predicate.png?fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=4bfe9027920bcaf5acd83363a0a9d9cf" alt="" data-og-width="1766" width="1766" data-og-height="866" height="866" data-path="images/nlp-predicate.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/nlp-predicate.png?w=280&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=6e5b3b5f9e89ae4ae761af717eb82d9f 280w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/nlp-predicate.png?w=560&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=19de2f99b20f6a4fa419ec60372087f6 560w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/nlp-predicate.png?w=840&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=8ffc2690271225d55ba8d337c331423c 840w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/nlp-predicate.png?w=1100&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=07a82f63754fbd6f1375c239bbb7d302 1100w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/nlp-predicate.png?w=1650&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=bfc9e5cba01e5da9f175711507cffd61 1650w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/nlp-predicate.png?w=2500&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=822cac2627a642a32f737ff114819df6 2500w" />

Leverage all the Galileo 'building blocks' that are logged and stored for you to create Tests using Galileo Conditions -- a class for building custom data quality checks.

Conditions are simple and flexible, allowing you to author powerful data/model tests.

## Run Report

Integrate with email or slack to automatically receive a report of Condition outcomes after a run finishes processing.

<img src="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/nlp-monitoring-report.png?fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=4ee767d4eae2e48c1da87515dbe22e6f" alt="" data-og-width="757" width="757" data-og-height="699" height="699" data-path="images/nlp-monitoring-report.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/nlp-monitoring-report.png?w=280&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=128c92b2161df176a0657cd0ebe8fc73 280w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/nlp-monitoring-report.png?w=560&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=a48620a07a87e5574defbd855b06593f 560w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/nlp-monitoring-report.png?w=840&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=d699e6d863d2dfefdbf3f1f5e97ba340 840w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/nlp-monitoring-report.png?w=1100&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=928e83197dc2c5a7f89caa9df88dc611 1100w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/nlp-monitoring-report.png?w=1650&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=1ac3472aa31cdcfe79ad359eecac9a05 1650w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/nlp-monitoring-report.png?w=2500&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=9fa697fd0763e9cf8dd2c54a3c603f4e 2500w" />

## Examples

```py  theme={null}

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

```py  theme={null}

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

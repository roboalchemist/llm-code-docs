# Source: https://docs.snowflake.com/en/user-guide/ml-functions/top-insights.md

# Source: https://docs.snowflake.com/en/sql-reference/classes/top-insights.md

# TOP_INSIGHTS (SNOWFLAKE.ML)

The GET_DRIVERS method of the TOP_INSIGHTS class determines the dimensions in your data that have the most influence on
a specified metric. You use [CREATE SNOWFLAKE.ML.TOP_INSIGHTS](top-insights/commands/create-top-insights.md) to create an instance of the class, then use the
[<instance_name>!GET_DRIVERS](top-insights/methods/get_drivers.md) method to get the insights.

> **Important:**
>
> **Legal notice.** This Snowflake ML function is powered by machine learning technology, which you, not Snowflake, determine when and how to use. Machine
> learning technology and results provided may be inaccurate, inappropriate, or biased.
> Snowflake provides you with the machine learning models that you can use within your own workflows. Decisions based on machine
> learning outputs, including those built into automatic pipelines, should have human oversight and review processes
> to ensure model-generated content is accurate.
> Snowflake provides algorithms (without any pretraining) and you’re responsible for the data that you provide the algorithm (for example, for training and inference) and the decisions you make using the resulting model’s output.
> Queries for this feature or function are treated as any
> other SQL query and may be considered [metadata](../metadata.md).
>
> **Metadata.** When you use Snowflake ML functions, Snowflake logs generic error messages returned by an ML
> function. These error logs help us troubleshoot issues that arise and improve these functions to serve you better.
>
> For further information, see [Snowflake AI Trust and Safety FAQ](https://www.snowflake.com/en/legal/snowflake-ai-trust-and-safety/).

## TOP_INSIGHTS commands

* [CREATE SNOWFLAKE.ML.TOP_INSIGHTS](top-insights/commands/create-top-insights.md)
* [DROP SNOWFLAKE.ML.TOP_INSIGHTS](top-insights/commands/drop-top-insights.md)
* [SHOW SNOWFLAKE.ML.TOP_INSIGHTS](top-insights/commands/show-top-insights.md)

## TOP_INSIGHTS methods

* [<instance_name>!GET_DRIVERS](top-insights/methods/get_drivers.md)

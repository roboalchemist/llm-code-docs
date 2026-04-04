# Source: https://docs.snowflake.com/en/migrations/sma-docs/use-cases/assessment-walkthrough/interpreting-the-assessment-output/assessment-output-in-application.md

# Snowpark Migration Accelerator: Assessment Output - In Application

When the Snowpark Migration Accelerator (SMA) finishes analyzing your code, it generates assessment artifacts and automatically takes you to the Assessment Results page.

## Readiness Scores

The Assessment Results page provides a concise overview, displaying only the available [readiness scores](../../../user-guide/assessment/readiness-scores.md) from the current tool execution.

### Snowpark Connect Readiness Score

The initial readiness score shown will be the [Snowpark Connect Readiness Score](../../../user-guide/assessment/readiness-scores.md). This is a measure of the found references to the Spark API and what percentage of them are supported by Snowpark Connect. This section will show:

* **Snowpark Connect Readiness Score**: the percentage of references to the Spark API that are supported by Snowpark Connect.
* **What to do next**: recommendations on what actions to take before continuing to the next step.
* **Understanding the Snowpark Connect Readiness Score**: description of the readiness score and how to interpret it.
* **All Identified Spark API Usages**: the total count of references to the Spark API found in this codebase
* **Spark API Usages Compatible with Snowpark Connect**: the count of references that are supported by Snowpark Connect.

> **Note:**
>
> Important Information:
>
> * A high readiness score, even 100%, doesn’t guarantee immediate migration success. It indicates that the Spark API references are compatible with Snowflake, suggesting good potential for migration to Snowpark Connect.
> * The readiness score you see may be different from this example because you might be using a different version of the tool, and the source code in these public repositories can change at any time since they’re not controlled by Snowflake.
> * Depending on your tool version, you may see additional readiness scores. For details on understanding these scores, please refer to [the current list of readiness scores](../../../user-guide/assessment/readiness-scores.md).
>
> The readiness scores are the most important information to review in the application. While other summaries are briefly covered, you can find detailed information about what the readiness scores mean in the conclusions from the assessment summary section below.
>
> ## Other Summaries
>
> ### Execution Summary
>
> Below the readiness score section, you will find the execution summary.
>
>
>
> The execution summary provides details about the current process. While this information can be helpful when troubleshooting issues with the SMA team, you don’t need to review it at this time.
>
> ## Conclusions from the Assessment Summary in the Application
>
> Before proceeding, we need to evaluate several key aspects:
>
> * *Readiness Level (Compatibility with Snowpark Connect)*
>   The assessment shows a Readiness Score of **93.37%** (your result may vary based on your tool version). Scores above 80% indicate high Snowpark Connect compatibility, suggesting that migration is recommended for this codebase. To understand the full compatibility picture, we need to examine the complete assessment results in the output folder.
> * *Size of the Spark footprint/impact on this codebase*
>   The analysis found 3,742 total Spark API references, with 3,494 automatically supported for conversion. This leaves only 248 references requiring manual conversion. While the total codebase size is unknown, the small number of unsupported references suggests a manageable evaluation effort. These 248 references likely follow a few common patterns, making them easier to assess. The actual conversion effort will be determined during the migration phase.
>
> Based on the analysis, this codebase appears to be well-suited for migration from Spark to Snowpark Connect, with minimal effort required to complete the conversion. Let’s examine the remaining output to confirm this assessment.

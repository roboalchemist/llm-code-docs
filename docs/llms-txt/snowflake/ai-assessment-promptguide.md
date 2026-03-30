# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/ai-assessment-promptguide.md

# Prompt guide for AI assessment

Use the suggested prompts on this page to use the `snowconvert-assessment` skill of the Cortex Code CLI agent.
These prompts can be used to direct the Cortex Code CLI agent to customize the assessment of specific sections of the source database code.

You can use the prompts to customize the suggested migration plan in the generated unified report.
Refer to [AI assessment report](ai-assessment.md) for more information on the unified report.

> **Note:**
>
> Snowflake strongly recommends installing Python (3.11 or later) and the [uv package manager](https://docs.astral.sh/uv/) to avoid issues related to environment dependencies.

## Invoke the skill

When you invoke the `snowconvert-assessment` skill, the Cortex Code CLI agent responds by:

1. Showing a welcome message explaining the functionality.
2. Confirming your request before running any analysis.
3. Asking for more details on path, goals, preferences, if needed.

## Example prompt scenarios

1. Start by invoking the `snowconvert-assessment` skill as shown below:

   ```none
   Use skill snowconvert-assessment
   ```

   The Cortex Code CLI agent will ask for the following:

   1. Path to your SnowConvert AI reports.
   2. Path to the file location for the assessment report that will be generated as output.
   3. Any specific goals or preferences for the assessment.
2. Start the assessment with the following prompt:

   ```none
   Run a comprehensive assessment with all the analyses.

   Analyze my SnowConvert AI reports at /path/to/Reports.

   Start fresh analysis (do not reuse previous results).
   ```

3. Set specific goals for the Cortex Code CLI agent. You can limit the number of deployment waves with the following prompt:

   ```none
   I want a maximum of five deployment waves.
   ```

   You can also specify the range of deployment waves as shown below:

   ```none
   Create 3-4 deployment waves.
   ```

4. To change the size of the deployment waves, use the following prompt as shown below:

   ```none
   Waves should have 20-30 objects each.
   ```

5. To force the wave to contain a fixed number of objects as shown below:

   ```none
   I need smaller batches with a maximum of 15 objects per wave.
   ```

6. You can prioritize objects in the deployment waves based on the business functions. For example, to prioritize all payroll-related objects in a specific deployment wave, use the following prompt:

   ```none
   Prioritize all Payroll-related objects in Wave 1.

   Put all customer* objects in the earliest waves.

   I need PKG_PAYROLL, PKG_HR, and PKG_FINANCE deployed first.
   ```

7. Once you have initial results, you can refine the AI assessment report.

   * To reorganize the objects in the suggested deployment waves, use the following prompt:

     ```none
     Move dbo.CriticalTable to Wave 1.

     Relocate all reporting procedures to Wave 5.
     ```

   * To investigate dependencies, use the following prompt:

     ```none
     Show me which objects have circular dependencies

     What objects are blocking the migration?

     Which objects depend on dbo.LegacyTable?
     ```

8. After investigations, you can regenerate the assessment report with the following prompts:

   ```none
   Generate a new HTML report.

   Regenerate with smaller batch sizes.

   Redo the analysis excluding the Staging schema.
   ```

   The Cortex Code CLI agent maintains the context. There is no need to start over.
9. To analyze the results of the assessment report, you can ask targeted questions using the following prompts:

   ```none
   How many objects are flagged for exclusion?

   What is the breakdown by schema?

   Show me a summary of the assessment.
   ```

10. You can drill down into the generated assessment report with the following prompts:

> * For objects categorized under the Exclusion Report:
>
>   ```none
>   Identify temporary and staging objects.
>
>   Find deprecated objects that can be excluded.
>   ```
>
> * For Dynamic SQL Report review, use the following prompt:
>
>   ```none
>   Analyze Dynamic SQL patterns in my codebase.
>   ```
>
> * For SSIS/ETL package analysis, use the following prompt:
>
>   ```none
>   Assess my SSIS packages for classification and migration complexity.
>   ```

## Tips for running AI assessments

The `snowconvert-assessment` skill is a powerful tool that can be used to generate actionable migration plans for complex workloads.
This section contains helpful tips that optimize the skill for best results.

1. Use a structured approach with target goals for maximum efficiency.

   **Example of an inefficient prompt sequence:**

   Prompt 1:

   ```none
   Generate waves
   ```

   Prompt 2:

   ```none
   Make the waves smaller
   ```

   Prompt 3:

   ```none
   Prioritize Payroll objects
   ```

   **Example of an efficient prompt:**

   ```none
   Generate waves with 20-30 objects each, prioritizing all Payroll-related objects
   ```

2. Use wildcards to expand the object selection to include all related objects.

   **Example of supported wildcard patterns:**

   > * `*payroll*` matches all objects containing the term “payroll” in the object name.
   > * `PKG_*` matches all objects starting with `PKG_` in the object name.
   > * `dbo.Customer*` matches all objects in the dbo schema starting with “Customer”.
   > * `*_Archive` matches all objects ending with “_Archive”.
3. Select dependency-based ordering or category-based ordering for deployment waves. By default, the Cortex Code CLI agent organizes the objects in the deployment waves based on their category, in the following order:

   > 1. Tables
   > 2. Views
   > 3. Procedures and functions
   > 4. ETL/SSIS packages

> If you prefer a dependency-based ordering:
>
> ```none
> Use dependency-based ordering instead of category-based
> ```

## Troubleshooting

**I want different wave sizes**

Use the following prompt to specify the minimum and maximum number of objects per wave:

```none
Regenerate waves with a minimum of 15 and maximum of 30 objects per wave
```

**Important objects are late in the waves**

Use the following prompt to move important objects to the earlier waves:

```none
Prioritize *CriticalProcess* objects to appear in Wave 1.
```

or reorganize after generation:

```none
Move dbo.CriticalTable to Wave 1.
```

**I have too many waves**

Use the following prompt to reduce the number of waves by increasing the number of objects per wave:

```none
Regenerate with larger waves - 60-100 objects each
```

**There are objects with circular dependencies**

Review the `cycles.txt` file from the SnowConvert AI reports and consider schema refactoring, or deploying circular dependency groups together, or manual intervention for complex cases.

## Frequently asked questions

1. Can I run just one type of analysis/assessment (for example, waves only)?

   Yes, you can run just one type of analysis/assessment by specifying the name of the report in the prompt (for example, deployment waves only).
2. How do I update the analysis/assessment after code changes?

   Re-run the assessment with updated SnowConvert AI reports, or specify “Start fresh analysis” in the prompt.
3. Can I export the data from the assessment report?

   Yes, the interactive `multi_report.html` report allows you to export the data from the assessment report into `csv` files.
4. What if I disagree with the object exclusion recommendations?

   The object exclusions are recommendations only. You can decide what to exclude.
5. How do I handle the objects that the Cortex Code CLI agent cannot categorize?

   Review the objects in the report manually. Such objects are flagged as “Uncertain items” in the report.

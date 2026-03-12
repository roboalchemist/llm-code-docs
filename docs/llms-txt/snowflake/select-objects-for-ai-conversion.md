# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/ai-verification/select-objects-for-ai-conversion.md

# Selecting objects for AI code conversion

This topic describes the functions available on the **Select Objects** page, when running AI code conversion.

## Tree view

The tree view as shown above displays the structure of databases and schemas in the converted workload, along with the conversion status of each code unit. You can perform the following actions on the database objects shown in a tree view under the **Name** column:

* Select the database objects to run AI code conversion on.
* Mark objects as **Verified by user** to exclude them from subsequent runs of the AI code conversion process. This status indicates that the user has reviewed the code and considers it valid for deployment. It represents the highest level of trust.
* Filter the database objects by type, database, schema and status.

## Selection Summary

The **Selection Summary** indicates the number of selected objects, the associated dependencies, and the estimated time and cost for AI code conversion. Note that the total number of objects includes the object selected and its dependencies. The estimated time and costs depend upon the size of the selected objects and token usage based on historical benchmark data.

**Total objects**: Shows the total number of objects to be processed, including both the user’s selection and any dependent objects.

**Estimated cost in Snowflake credits**: Shows the estimate based on object size and historical benchmark data. It calculates total token usage converted into standard Snowflake credit costs.

## Breakdown

The **Breakdown** section shows all objects grouped by their conversion status as below:

* **Converted successfully**: The object was successfully converted with deterministic conversion (non AI code conversion) and is ready to be deployed to Snowflake.
* **Has issues**: The object has issues from either deterministic or AI code conversion and cannot be deployed without fixes.Try running AI code conversion again or fixing it manually.
* **Suggested fixes**: The AI code conversion process has generated suggested fixes and requires user review.
* **Verified by AI/AI converted**: The AI code conversion process verified that the source code and converted code produced equivalent results. User review is required, additionally.
* **Verified by User**: These objects were reviewed by the user in a previous AI code conversion and are valid for deployment. This status represents the highest level of trust. All objects should be marked as “Verified by User” after the user review and manual fixes.

## Footer actions

After selecting objects and reviewing the **Selection Summary**, the AI code conversion process can be initiated by selecting **AI convert**

The process of running AI code conversion is meant to be iterative. Multiple execution runs can be performed on the same code base until the expected conversion accuracy is achieved. Select **Go to latest conversion** at the bottom of the page to view the results of the last iteration of AI code conversion.

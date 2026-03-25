# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/snowconvert-ai-verification.md

# AI code conversion

AI code conversion strengthens the migration process by using AI agents to convert more objects through automated functional validation of converted database code. It uses synthetic data generation, AI-driven unit testing, and AI-driven resolution of errors identified in the deterministic code conversion step, where error warnings and issues (EWIs) and functional difference messages (FDMs) flag conversion issues—along with an intelligent layer in the Snowflake Service that proactively converts code, verifies correctness, resolves errors, and accelerates confidence.

During migration, deterministic logic is first used to translate the source code, surfacing EWIs and FDMs when it cannot automatically resolve certain patterns. Following this, AI code conversion is then used to reduce the manual remediation effort by identifying and resolve issues earlier in the process, and provide assurance to users that the converted objects behave as expected. Users must review and confirm AI suggestions to ensure they align with the functionality and standards.

| AI code conversion is currently available for SQL Server, Redshift, BigQuery, and PostgreSQL databases. |
| --- |

## Key features of AI code conversion

* **Accelerated AI validation**: Reduces the time and resources spent on manual testing.
* **Automated test generation**: Automatically generates test cases with test data based on your existing queries and business logic.
* **Repair suggestions**: Generates suggestions to produce consistent results between the source database system and Snowflake.

## Prerequisites for AI code conversion

Before you get started with AI code conversion, complete the following steps:

1. Download and install [SnowConvert AI](https://docs.snowflake.com/en/migrations/snowconvert-docs/general/getting-started/download-and-access).
2. [Recommended] Convert your legacy SQL Server code by using [SnowConvert AI](https://docs.snowflake.com/en/migrations/snowconvert-docs/general/getting-started/download-and-access).
3. Connect an account specifically designated for testing and development and avoid using a production account.

   Some objects will be created as part of the AI code conversion process.
4. Ensure the PUBLIC role in the account you connect doesn’t have access to any production data and doesn’t have privileges to execute any sensitive operations, such as CREATE USER commands.
5. Ensure that the role used for AI code conversion has the following privileges on the account:

   * CREATE DATABASE
   * CREATE MIGRATION
6. Enable Cortex AI SQL functions in the account, specifically for model `claude-4-sonnet`.

   * To enable the model if it’s not available in your region, see [Cross-region inference](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cross-region-inference#any-region).

## Getting started with AI code conversion

To begin a migration validation project, complete the following steps:

1. Execute the [code conversion of SnowConvert AI](https://docs.snowflake.com/en/migrations/snowconvert-docs/general/getting-started/running-snowconvert/conversion/README) on your SQL Server database.
2. After the code conversion is complete, select **Go to AI code conversion** from the **Results** page.

   | All AI processing happens in the Snowflake account you connect to and consumes Snowflake charges. |
   | --- |

3. You will be redirected to the **Connect to Snowflake** page to enter the connection parameters of a testing account. This is necessary to ensure that the AI code conversion process creates objects and executes queries in the test database and avoids unintended changes to the production database. Select **Continue**.
4. Acknowledge and confirm the **AI disclaimers** and select **Continue**.
5. The **Select objects** page displays the current conversion status of each database object under the **Conversion** column. Select the required objects for AI code conversion. You can also run an [AI code conversion process with source-system verification](https://docs.snowflake.com/en/migrations/snowconvert-docs/ai-verification/snowconvert-ai-twosided-verification) by selecting **Upload custom instructions**.

   SnowConvert automatically performs the following actions:

   1. Automatically selects and validates dependent objects when they are associated with your chosen objects.
   2. Reviews a summary of the selected objects, their dependencies, and the estimated time and Snowflake credit cost.
   3. Confirms the selection to proceed with code conversion.
6. Select **AI Convert**. SnowConvert AI connects to your Snowflake account, where it relies on [Cortex AI Functions](https://docs.snowflake.com/en/user-guide/snowflake-cortex/aisql) to review your code and suggest resolutions to any problems. AI code conversion might take a few minutes to start, and it might run for several minutes or hours depending on the complexity of the code being verified.
7. The **AI Results** page shows the status for the AI code conversion of selected objects. The **Status** column indicates the AI code conversion outcomes. Select **Details** to review the test code and test results, source code, and converted code.

   | Review the code generated by AI before deploying it. Code generated by AI might not be correct. |
   | --- |

   * Status of the AI code conversion:

     * **Converted successfully**: Indicates that the object was successfully converted by deterministic conversion (not by AI code conversion). It is ready to be deployed to Snowflake.
     * **Has issues**: Indicates that the object conversion was not successful and still has issues from either deterministic or AI conversion. It needs manual fixes or another AI code conversion run.
     * **Suggested fixes**: Indicates that AI code conversion proposed code fixes for the object. The fixes need user review before being considered ready for deployment to Snowflake.
     * **Verified by AI**: Indicates that AI code conversion successfully converted the object. It can be considered ready for deployment to Snowflake after review.
     * **Verified by User**: Indicates that a user explicity reviewed the object and marked it as valid for deployment. This is the highest trust level and objects in this state are excluded from subsequent AI code conversion runs.
   * **Open Code**:

     * By default, this option opens and compares your original source code and the code generated by the AI code conversion process in VS Code.
     * If you click the arrow next to **Open Code**, you also have the option to open and compare in VS Code:

       * The converted code from SnowConvert and the code converted by AI.
8. Select **Verified by user** for all objects for which you have accepted the AI code conversion. Only objects that are verified by the user can be deployed.

## Billing and cost considerations with SnowConvert AI code conversion

AI code conversion consumes Snowflake credits based on the compute resources it uses in your Snowflake account. The following features contribute to the cost:

* AI SQL - AI code conversion uses Cortex AI SQL.
* Warehouse - Test queries are executed in a warehouse.
* Snowflake stages - Input and outputs for AI code conversion are stored in a stage, which incurs storage costs.
* SPCS - AI code conversion might consume a small amount of credits to use Snowpark Container
  Services. To find the costs associated with AI code conversion, look for compute pools with names that start with
  `AI_MIGRATOR`. For more information, see [Snowpark Container Services costs](https://docs.snowflake.com/en//developer-guide/snowpark-container-services/accounts-orgs-usage-views).

For more information, see [Snowflake Service Consumption Table](https://www.snowflake.com/legal-files/CreditConsumptionTable.pdf).

## Limitations of AI powered code conversion

The initial version is optimized for standard SQL Server migrations. While migration process can handle many query types, all the changes generated by SnowConvert AI code conversion must be reviewed by the customer before they can be deployed to any account.

## Legal notices for AI features

Your use of Snowflake AI features is subject to all agreements, terms or policies that apply to such usage, including but not limited to those documented in the [Snowflake AI & ML Documentation](https://docs.snowflake.com/en/guides-overview-ai-features).

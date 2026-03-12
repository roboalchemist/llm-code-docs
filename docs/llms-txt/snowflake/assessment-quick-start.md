# Source: https://docs.snowflake.com/en/migrations/sma-docs/user-guide/assessment/assessment-quick-start.md

# Snowpark Migration Accelerator: Assessment Quick Start

The Snowpark Migration Accelerator (SMA) helps you analyze your source code by generating detailed reports and inventories. This guide will show you how to begin the assessment process.

## How to Execute an Assessment

To begin assessing your code, create a new project in the Snowpark Migration Accelerator (SMA) tool.

1. Begin by selecting the **New Project** button.

Complete the required fields in the New Project dialog, including project name, email address, company name, input folder, and output folder. Once all required information is provided, click the **Save** button to create your project.

The project home page displays with a **Code Process** card. This card provides access to a guided flow for running assessment and conversion on your code.

Select the **Start Assessment** card to run an assessment on your code and analyze migration complexity. Click the **Continue** button to proceed.

The assessment execution screen displays, showing the progress of three stages: Loading Source Code, Analyzing Source Code, and Writing Results. Processing time varies depending on your project size.

Once the assessment is complete, the results screen will display. This screen provides detailed information to help you understand your current code and its potential migration to Snowpark Connect. For a complete walkthrough of this output, please refer to the [Understanding the Assessment Summary](understanding-the-assessment-summary.md) section.

Note that while you can find basic information in the [assessment summary](understanding-the-assessment-summary.md) page above, the complete [output folder](output-reports/README.md) contains much more detailed information, including a comprehensive multi-page report.

## Next Steps

After the tool completes its analysis, you’ll need to review the results and determine your next steps. Here are some helpful tips to guide you:

* Consider the Readiness Score as an Initial Guide: While the readiness score evaluates Snowpark Connect compatibility, it’s important to understand that successful migration depends on multiple factors. These include compatibility with third-party libraries and whether Snowpark Connect is the optimal solution for your specific workload.
* Take Time to Analyze the Assessment Results: The assessment provides valuable insights that can help you create an effective migration strategy. Carefully review the assessment data before starting the conversion process to avoid unnecessary rework and ensure a more efficient migration.

Additional options are available in the application menu, as shown in the image below:

* **Retry Assessment** - You can run the assessment again by clicking the **Retry Assessment** button on the Assessment Results page. This is useful when you’ve made changes to your source code and want to see updated results.
* **Convert to the Snowpark API** - While this is the next step in the process, we recommend reviewing the assessment results thoroughly before proceeding. For more details, see the [conversion section of this documentation](../conversion/README.md).
* **View Reports** - Opens the folder containing assessment output reports. These include the detailed assessment report, Spark reference inventory, and other analyses of your source codebase. Each report type is explained in detail in this documentation.

For a detailed review of the assessment summary information, continue reading. However, if you’re ready to begin the conversion process, you can proceed directly to the conversion quick start guide.

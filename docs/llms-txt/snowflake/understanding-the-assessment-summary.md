# Source: https://docs.snowflake.com/en/migrations/sma-docs/user-guide/assessment/understanding-the-assessment-summary.md

# Snowpark Migration Accelerator: Understanding the Assessment Summary

After running an assessment, you can view the initial results and summary in the Assessment Summary Report.

Keep in mind that this report summarizes the information from the inventory files created in the [Output Reports](output-reports/README.md) folder during the SMA execution. For a comprehensive analysis, please review the [Detailed Report](output-reports/README.md) in the output directory.

The Assessment Results section of the application contains several components, which are explained in detail below.

## Standard Assessment Summary

The summary will appear as shown below:

In the top-right corner of the report, the **Execution date** indicates when the analysis was run.

### Snowpark Connect Readiness Score

The Snowpark Connect Readiness Score will look something like this:

1. **Readiness Score** - It will show you the readiness score you obtained. The Snowpark Connect readiness score indicates the proportion of Spark API references that are supported by Snowpark Connect. This score is calculated by dividing the number of supported Spark API references by the total Spark API references. You can learn more about this score in the [Snowpark Connect Readiness Score](readiness-scores.md) section.
2. **Score Explanation** - An explanation of what the Snowpark Connect Readiness score is and how to interpret it.
3. **Next Steps** - Depending on the readiness score obtained, the SMA will advise you on what actions you should take before proceeding to the next step.
4. **Score Breakdown** - A detailed explanation of how the Snowpark Connect Readiness Score was calculated. In this case, it will show you the number of Spark API references supported by Snowpark Connect divided by the total number of Spark API references.

**Supported Usages** refers to the number of Spark API references in a workload that are supported by Snowpark Connect. In contrast, **identified usages** represents the total count of Spark API references found within that workload.

### Spark API Usages

> **Danger:**
>
> The **Spark API Usages** section has been deprecated since version **2.0.2**. You can now find:
>
> * A summary of Spark API usage in [the Detailed Report](output-reports/curated-reports.md)
> * A complete list of all Spark API usage instances in [the Spark API Usages Inventory](output-reports/sma-inventories.md)

The report contains three main sections displayed as tabs:

1. Overall Usage Classification
2. Spark API Usage Categorization
3. Spark API Usages By Status

We will examine each section in detail below.

#### Overall Usage Classification

This tab displays a table containing three rows that show:

* Supported operations
* Unsupported operations
* Total usage statistics

Additional details are provided in the following section:

1. **Usages Count** - The total number of times Spark API functions are referenced in your code. Each reference is classified as either supported or unsupported, with totals shown at the bottom.
2. **Files with at least 1 usage** - The number of files that contain at least one Spark API reference. If this number is less than your total file count, it means some files don’t use Spark API at all.
3. **Percentage of All Files** - Shows what portion of your files use Spark API. This is calculated by dividing the number of files with Spark API usage by the total number of code files, expressed as a percentage.

#### Spark API Usage Categorization

This tab displays the different types of Spark references detected in your codebase. It shows the overall Readiness Score (which is the same score shown at the top of the page) and provides a detailed breakdown of this score by category.

You can find all available categorizations in the [Spark Reference Categories](spark-reference-categories.md) section.

#### Spark API Usages By Status

The final tab displays a categorical breakdown organized by mapping status.

The SMA tool uses seven main mapping statuses, which indicate how well Spark code can be converted to Snowpark. For detailed information about these statuses, refer to the [Spark Reference Categories](spark-reference-categories.md) section.

### Import Calls

> **Danger:**
>
> The **Import Calls** section has been removed since version **2.0.2**. You can now find:
>
> * A summary of import statements in [the Detailed Report](output-reports/curated-reports.md)
> * A complete list of all import calls in [the Import Usages Inventory](output-reports/sma-inventories.md)

The “Import Calls” section displays frequently used external library imports found in your codebase. Note that Spark API imports are excluded from this section, as they are covered separately in the “Spark API” section.

This table contains the following information:

The report displays the following information:

1. A table with 5 rows showing:

   * The 3 most frequently imported Python libraries
   * An “Other” row summarizing all remaining packages
   * A “Total” row showing the sum of all imports
2. A “Supported in Snowpark” column indicating whether each library is included in Snowflake’s [list of supported packages in Snowpark](https://repo.anaconda.com/pkgs/snowflake/).
3. An “Import Count” column showing how many times each library was imported across all files.
4. A “File Coverage” column showing the percentage of files that contain at least one import of each library. For example:

   * If ‘sys’ appears 29 times in the import statements but is only used in 28.16% of files, this suggests it’s typically imported once per file where it’s used.
   * The “Other” category might show 56 imports occurring across 100% of files.

For detailed import information per file, refer to the ImportUsagesInventory.csv file in the [Output Reports](output-reports/README.md).

### File Summary

> **Danger:**
>
> The **File Summary** section has been removed since version **2.0.2**. You can now find:
>
> * A summary of files and file types in [the Detailed Report](output-reports/curated-reports.md)
> * A complete list of all files (both analyzed and not analyzed) in [the File Inventory](output-reports/sma-inventories.md)

The summary report contains multiple tables displaying metrics organized by file type and size. These metrics provide insights into the codebase’s volume and help estimate the required effort for the migration project.

The Snowpark Migration Accelerator analyzes all files in your source codebase, including both code and non-code files. You can find detailed information about the scanned files in the [files.csv](output-reports/README.md) report.

The File Summary contains multiple sections. Let’s examine each section in detail.

#### File Type Summary

The File Type Summary displays a list of all file extensions found in your scanned code repository.

The file extensions listed indicate which types of code files SMA can analyze. For each file extension, you will find the following information:

* **Lines of Code** - The total number of executable code lines across all files with this extension. This count excludes comments and empty lines.
* **File Count** - The total number of files found with this extension.
* **Percentage of Total Files** - The percentage that files with this extension represent out of all files in the project.

To analyze your workload, you can easily identify whether it primarily consists of script files (such as Python or R), notebook files (like Jupyter notebooks), or SQL files. This information helps determine the main types of code files in your project.

#### Notebook Sizing by Language

The tool evaluates notebooks in your codebase and assigns them a “t-shirt” size (S, M, L, XL) based on the number of code lines they contain. This sizing helps estimate the complexity and scope of each notebook.

The notebook sizes are categorized according to the main programming language used within each notebook.

#### Notebook Stats By Language

This table displays the total number of code lines and cells in all notebooks, organized by programming language.

These notebooks are organized by the primary programming language used within them.

#### Code File Content

When running SMA, the tab name will change based on your source language:

* For Python source files, the tab will display “Python File Content”
* For Scala source files, the tab will display “Scala File Content”

This row shows how many files contain Spark API references. The “Spark Usages” row displays:

1. The number of files that use Spark APIs
2. What percentage these files represent of the total codebase files analyzed

This metric helps identify what percentage of files do not contain Spark API references. A low percentage suggests that many code files lack Spark dependencies, which could mean the migration effort might be smaller than initially estimated.

#### Code File Sizing

The File Sizing tab name changes based on your source language:

* For Python source files, it displays as “Python File Sizing”
* For Scala source files, it displays as “Scala File Sizing”

The codebase files are categorized using “t-shirt” sizes (S, M, L, XL). Each size has specific criteria described in the “Size” column. The table also shows what percentage of all Python files falls into each size category.

Understanding the file size distribution in your codebase can help assess workload complexity. A high percentage of small files typically suggests simpler, less complex workloads.

### Issues Summary

The Issues Summary provides critical information about potential problems found during code scanning. When transitioning from assessment to conversion, you’ll see a list of EWIs (Errors, Warnings, and Issues) detected in your codebase. For a detailed explanation of these issues, please refer to the Issue Analysis section in the documentation.

At the top of the issue summary, you will find a table that provides an overview of all identified issues.

The table contains two rows.

* The “Number of issues” represents the total count of all issue codes found in each category.
* The “Number of unique issues” represents the count of distinct error codes found in each category.

The problems are divided into three main categories:

* **Warnings** indicate potential differences between source and target platforms that may not require immediate action but should be considered during testing. These could include slight variations in behavior for edge cases or notifications about changes in appearance compared to the source platform.
* **Conversion issues** highlight elements that either failed to convert or need additional configuration to work properly in the target platform.
* **Parsing issues** occur when the tool cannot interpret specific code elements. These are critical issues requiring immediate attention, typically caused by non-compiling source code or incorrect code extraction. If you believe your source code is correct but still receive parsing errors, it may be due to an unrecognized pattern in SMA. In such cases, please [report an issue](../project-overview/configuration-and-settings.md) and include the problematic source code section.

The table summarizes the total count for each item.

Below this table, you will find a list of unique issue codes and their descriptions.

Each issue code entry provides:

* The unique issue identifier
* A description of the issue
* The number of occurrences
* The severity level (Warning, Conversion Error, or Parsing Error)

You can click any issue code to view detailed documentation that includes:

* A full description of the issue
* Example code
* Recommended solutions

For instance, clicking the first issue code shown above (SPRKPY1002) will take you to its dedicated documentation page.

By default, the table displays only the top 5 issues. To view all issues, click the SHOW ALL ISSUES button located below the table. You can also use the search bar above the table to find specific issues.

Understanding the remaining conversion work is crucial during assessment mode. You can find detailed information about each issue and its location in the issue inventory within the [Reports folder](output-reports/README.md).

### Execution Summary

The execution summary provides a comprehensive overview of the tool’s recent analysis. It includes:

* The code analysis score
* User details
* The unique execution ID
* Version information for both SMA and Snowpark API
* Project folder locations that were specified during [Project Creation](../project-overview/project-setup.md)

### Appendixes

The appendixes contain additional reference information that can help you better understand the output generated by the SMA tool.

This guide contains general reference information about using the Snowpark Migration Accelerator (SMA). While the content may be updated periodically, it focuses on universal SMA usage rather than details about specific codebases.

---

This is what most users will see when they run the Snowpark Migration Accelerator (SMA). If you are using an older version, you might see the Abbreviated Assessment Summary instead, which is shown below.

## Abbreviated Assessment Summary [Deprecated]

If your readiness score is low, your migration summary might appear as follows:

This summary contains the following information:

* **Execution Date**: Shows when your analysis was performed. You can view results from any previous execution for this project.
* **Result**: Indicates if your workload is suitable for migration based on the [readiness score](../../support/glossary.md). The readiness score is a preliminary assessment tool and does not guarantee migration success.
* **Input Folder**: Location of the source files that were analyzed.
* **Output Folder**: Location where analysis reports and converted code files are stored.
* **Total Files**: Number of files analyzed.
* **Execution Time**: Duration of the analysis process.
* **Identified Spark References**: Number of Spark API calls found in your code.
* **Count of Python (or Scala) Files**: Number of source code files in the specified programming language.

---

## Next Steps

The application provides several additional features, which can be accessed through the interface shown in the image below.

* **Retry Assessment** - You can run the assessment again by clicking the **Retry Assessment** button on the Assessment Results page. This is useful when you make changes to the source code and want to see updated results.
* **Convert to the Snowpark API** - While this may seem like the next logical step, it’s important to review the assessment results thoroughly before proceeding. For more information, see the [conversion section of this documentation](../conversion/README.md).
* **View Reports** - Opens the folder containing assessment output reports. These include the detailed assessment report, Spark reference inventory, and other analyses of your source codebase. Each report type is explained in detail in this documentation.

The following pages provide detailed information about the reports generated each time the tool runs.

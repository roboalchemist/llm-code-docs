# Source: https://docs.snowflake.com/en/migrations/sma-docs/user-guide/project-overview/tool-execution.md

# Snowpark Migration Accelerator: Tool Execution

After setting up your project, you can run the Snowpark Migration Accelerator (SMA). This is the most straightforward step in the process.

On the Assessment Settings page, select **Start Assessment** and then click **Continue** in the bottom right corner to begin running the Snowpark Migration Accelerator (SMA).

The tool will now begin scanning all files in the input directory. During execution, you will see a progress screen similar to the following:

The migration process consists of three distinct phases:

* **Loading Source Code**: SMA scans all files in the input directory to create a file inventory. From this inventory, it builds a semantic model using code from the specified file extensions.
* **Analyzing Source Code**: During this main phase, SMA creates an Abstract Syntax Tree (AST) to represent your source code’s functionality. While building the AST, it also creates a symbol table to track elements and functions throughout the conversion process. This symbol table helps generate all output reports. In conversion mode, SMA identifies elements in the AST that have Snowflake equivalents and maps them to their corresponding Snowflake functions.
* **Writing Results**: In the final step, SMA generates output files. In Assessment mode, it creates reports. In conversion mode, it produces both reports and converted code in your specified output folder.

After all three phases are complete, the Assessment Results page is automatically displayed.

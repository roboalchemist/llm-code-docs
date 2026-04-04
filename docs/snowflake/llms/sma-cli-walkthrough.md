# Source: https://docs.snowflake.com/en/migrations/sma-docs/use-cases/sma-cli-walkthrough.md

# Snowpark Migration Accelerator: SMA CLI Walkthrough

The [Snowpark Migration Accelerator (SMA)](https://www.snowflake.com/en/data-cloud/snowpark/migration-accelerator/) helps developers migrate their Python or Scala Spark code to Snowpark. It analyzes your code and:

1. Evaluates compatibility with Snowpark
2. Automatically converts compatible Spark API calls to Snowpark API
3. Identifies code that cannot be automatically converted
4. Creates an inventory of third-party library imports from scripts and notebooks
5. Generates an editable compatibility report comparing Spark and Snowpark code

Snowflake has released a Command Line Interface (CLI) for the Snowpark Migration Accelerator (SMA). This guide will demonstrate how to use the CLI both as a standalone tool and within a script.

## Using the CLI

You can download the Command Line Interface (CLI) from [the Download and Access section](../general/getting-started/download-and-access.md). Select the version that matches your operating system. You can store the CLI in any accessible location on your machine or container.

> **Note:**
>
> **NOTE**: While this walkthrough uses screenshots from a Mac computer, the process is similar for Windows and Linux users.

After downloading the package file (.zip or .tar format), extract its contents. The Command Line Interface (CLI) tool is located in the “orchestrator” folder within the extracted files.

Open a terminal or command prompt in the installation folder and verify the CLI installation by running the following command to check its version:

./sma –version

You will see results that look like this:

The SMA Command Line Interface (CLI) is a local application that runs on your computer, similar to the SMA desktop application. To analyze your code files using the SMA CLI, these files must be stored on your local machine where the CLI can access them. The CLI supports the same file types as the regular SMA application. For a complete list of supported file types, please refer to [the supported filetypes in the SMA documentation](../user-guide/before-using-the-sma/supported-filetypes.md).

> **Note:**
>
> **NOTE**: To test the CLI functionality, you can use the sample codebase provided in [the Assessment](assessment-walkthrough/walkthrough-setup/README.md) section or refer to the Conversion walkthroughs in the SMA documentation.

The SMA documentation contains a complete list of CLI arguments. Let’s explore the most important ones in this section.

The SMA CLI runs in [Conversion mode](../user-guide/conversion/README.md) by default, rather than [Assessment mode](../user-guide/assessment/README.md). To run the CLI in assessment mode, use [the -a argument](assessment-walkthrough/README.md). For conversion operations, you’ll need a valid access code. To verify if you have a valid access code, use the following command:

```bash
./sma show-ac
```

To run a conversion, you need to provide:

1. Input directory (required)
2. Output directory (required)

If you haven’t created a project file before, you’ll also need to provide:

* User email
* Organization name
* Project name

Once you’ve set up these parameters for the first time, you only need to specify the input and output directories for future conversions.

```bash
./sma -i '/your/INput/directory/path/here' -o '/your/OUTput/directory/path/here' -e your@email.com -c Your-Organization -p Your-Project-Name
```

This screen displays a summary of your execution settings and prompts you to confirm whether you want to proceed.

To skip the confirmation prompt, add the –yes or -y parameter. This is particularly important when running the CLI from automated scripts.

The tool provides detailed progress information during its execution.

While the tool is running, it will continuously print output to the screen. When the process is complete, you will see the prompt again. The tool generates detailed output that includes all processes, issues, and completed or failed steps. You don’t need to read through all of this information while it’s running, as you can review it later in [the Logs output folder](../user-guide/assessment/output-logs.md).

## Viewing the Output

The SMA CLI produces the same output as the SMA application. When you run the tool, it creates three folders in your specified output directory:

* [Reports](../user-guide/assessment/output-reports/README.md)
* [Logs](../user-guide/assessment/output-logs.md)
* Output (contains the converted code)

For detailed guidance on working with code that has been converted by the Snowpark Migration Accelerator (SMA), please refer to [the conversion walkthrough](conversion-walkthrough.md).

## Running the CLI Programmatically

Coming soon! The SMA team will provide a script that enables you to run the SMA Command Line Interface (CLI) automatically across multiple directories.

---

Try out the Command Line Interface (CLI) today. If you need help or have questions, contact the Snowpark Migration Accelerator team at [sma-support@snowflake.com](mailto:sma-support%40snowflake.com).

# Source: https://docs.safetycli.com/safety-docs/safety-cli/scanning-for-vulnerable-and-malicious-packages/license-scanning.md

# License Scanning

Safety provides a clear overview of the licenses used across all your dependencies.

To display the licenses in use, run the **`safety license`** command instead of the usual **`safety scan`** command used to perform vulnerability scans.

You can run the **`safety license --help`** to see a full list of available options.&#x20;

Running **`safety license`** will scan the current Python environment for all installed dependencies and report on their licenses.

Running **`safety license -r requirements.txt`** will report on the packages in the named requirements file.

## Output Options <a href="#output-options" id="output-options"></a>

The default output option is to the screen.

If you wish to ingest or analyze the resulting license report data you can generate a JSON file from the report by adding the **`--output json`** argument, as in the example below:

**`safety license -r requirements.txt --output json`**

Another output option is **`--output bare`** which will print the unique set of licenses that were present in the packages that were analyzed, as in the example below:

**`safety license -r requirements.txt --output bare`**

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/hadoop-file-input-cp-main-page/select-an-engine-hadoop-file-input/using-the-hadoop-file-input-step-on-the-pentaho-engine-cp/options-hadoop-file-input-reuse/file-tab-hadoop-file-input-kettle/selecting-a-file-using-regular-expressions-kettle.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/hadoop-file-input-cp-main-page/options-hadoop-file-input-reuse/file-tab-hadoop-file-input-kettle/selecting-a-file-using-regular-expressions-kettle.md

# Selecting a file using regular expressions

Use the **Wildcard (RegExp)** field in the **File** tab to search for files by wildcard in the form of a regular expression. Regular expressions are more sophisticated than using `*` and `?` wildcards. This table describes several examples of regular expressions.

| File Name | Regular Expression          | Files Selected                                                                                  |
| --------- | --------------------------- | ----------------------------------------------------------------------------------------------- |
| `/dirA/`  | `.userdata.\.txt`           | Find all files in `/dirA/` with names containing userdata and ending with `.txt`                |
| `/dirB/`  | `AAA.\*`                    | Find all files in `/dirB/` with names that start with `AAA`                                     |
| `/dirC/`  | `\[ENG:A-Z\]\[ENG:0-9\].\*` | Find all files in `/dirC/` with names that start with a capital and followed by a digit (A0-Z9) |

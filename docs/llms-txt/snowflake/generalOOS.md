# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/general/technical-documentation/issues-and-troubleshooting/out-of-scope/generalOOS.md

# SnowConvert AI - Out of Scope

## SSC-OOS-0001

The file has an unexpected encoding and was not translated

### Description

This error occurs when the tool cannot recognize the character encoding format of a source code file. Character encoding is a method of converting text characters into numerical values that computers can process. When the tool encounters characters it cannot interpret, it generates this error.

### Best Practices

* Ensure all files in the input folder use the same character encoding to prevent encoding-related errors.
* Choose the correct encoding using either the conversion settings or by specifying the –encoding parameter in the [CLI](../../../user-guide/snowconvert/command-line-interface/README.md). You can identify the correct encoding using tools like [Free Online Formater](https://freeonlineformatter.com/encoding-string), or by running `file -i *` on Linux or macOS.
* For additional assistance, contact us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

# Source: https://docs.envzero.com/guides/integrations/plugins/tflint-plugin.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using the TFlint Plugin

> Integrate the TFLint plugin with env zero to analyze Terraform code for errors and best practices

## Overview

This plugin executes the `TFLint` CLI and lets you easily analyze your code so you could find possible errors, receive warning about deprecated syntax and enforce best practices and naming conventions.

This plugin will install the `TFLint` binary, call `init` and execute `tflint` on the given directory.

For more information, check out the [TFLint Plugin git repository](https://github.com/env0/env0-tflint-plugin)

For an example repository that integrates the TFLint plugin, click [here](https://github.com/env0/templates/tree/master/plugins/tflint).

## Inputs

1. `version` (required) - the specific version of tflint you wish to use
2. `directory` (required) - the path to the directory with the IaC code to analyze (the root folder is your project's root folder)
3. `flags` - a string containing additional flags as one string

<Info>
  Additional Content

* [What is Checkov: Benefits, Key Features, and Examples](https://www.env0.com/blog/best-iac-scan-tool-what-is-checkov)
* [What is tfsec: Benefits, Key Features, and Examples](https://www.env0.com/blog/best-iac-scan-tool-what-is-tfsec)
* [What is Terrascan: Benefits, Key Features, and Examples](https://www.env0.com/blog/best-iac-scan-tools-what-is-terrascan)
* [Best IaC Scanning Tools](https://www.env0.com/blog/best-iac-scan-tool)
</Info>

Built with [Mintlify](https://mintlify.com).

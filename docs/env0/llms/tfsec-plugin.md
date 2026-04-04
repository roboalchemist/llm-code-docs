# Source: https://docs.envzero.com/guides/integrations/plugins/tfsec-plugin.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using the TFsec Plugin

> Integrate the tfsec plugin with env zero to scan Terraform code for security misconfigurations

## Overview

This plugin executes the `tfsec` CLI and lets you easily analyze your code so you could find misconfigurations and enforce built in rules.

This plugin will install the `tfsec` binary and execute it on the given directory.

For more information, check out the [tfsec Plugin git repository](https://github.com/env0/env0-tfsec-plugin).

For an example repository that integrates the TFSec plugin, [here](https://github.com/env0/templates/tree/master/plugins/tfsec).

## Inputs

1. `version` (required) - the specific version of tfsec you wish to use
2. `directory` (required) - the path to the directory with the IaC code to analyze (the root folder is your project's root folder)
3. `flags` - a string containing additional flags as one string

## Suggested Blog Content

[What is tfsec: Benefits, Key Features, and Examples](https://www.env0.com/blog/best-iac-scan-tool-what-is-tfsec)

[What is Checkov: Benefits, Key Features, and Examples](https://www.env0.com/blog/best-iac-scan-tool-what-is-checkov)

[What is Terrascan: Benefits, Key Features, and Examples](https://www.env0.com/blog/best-iac-scan-tools-what-is-terrascan)

[Best IaC Scanning Tools](https://www.env0.com/blog/best-iac-scan-tool)

Built with [Mintlify](https://mintlify.com).

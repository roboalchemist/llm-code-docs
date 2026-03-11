# Source: https://docs.envzero.com/guides/integrations/plugins/checkov-plugin.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using the Checkov Plugin

> Integrate the Checkov plugin with env zero for Infrastructure-as-Code security scanning in deployments

## Overview

This plugin executes the `checkov` CLI  and lets you easily integrate Infrastructure-as-Code security best practices within your env zero deployments.

The plugin will install the `checkov` binary and execute it.

For more information, check out the [Checkov Plugin git repository](https://github.com/env0/env0-checkov-plugin).

For an example repository that integrates the Checkov plugin, click [here](https://github.com/env0/templates/blob/master/plugins/checkov/env0.yml).

## Inputs

To use the Checkov plugin, you need to pass the following inputs:

1. `directory` (**Required**) - the path to the directory with the IaC code to scan (the root folder is your project's root folder)\
   flags - a string containing additional flags as one string
2. `flags` - a string containing additional flags as one string

## Suggested Blog Content

[What is tfsec: Benefits, Key Features, and Examples](https://www.env0.com/blog/best-iac-scan-tool-what-is-tfsec)

[What is Checkov: Benefits, Key Features, and Examples](https://www.env0.com/blog/best-iac-scan-tool-what-is-checkov)

[What is Terrascan: Benefits, Key Features, and Examples](https://www.env0.com/blog/best-iac-scan-tools-what-is-terrascan)

[Best IaC Scanning Tools](https://www.env0.com/blog/best-iac-scan-tool)

Built with [Mintlify](https://mintlify.com).

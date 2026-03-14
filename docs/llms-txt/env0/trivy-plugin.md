# Source: https://docs.envzero.com/guides/integrations/plugins/trivy-plugin.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using the Trivy Plugin

> Integrate the Trivy plugin with env zero to scan IaC code for misconfigurations and security issues

## Overview

This plugin executes the `trivy` CLI - it lets you easily analyze your code so you could find misconfigurations and enforce built-in rules.

This plugin will install the `trivy` binary and execute a `config` command on the given directory.

For more information, check out the [Trivy Plugin git repository](https://github.com/env0/env0-trivy-plugin).

For an example repository that integrates the Trivy plugin, [here](https://github.com/env0/templates/tree/master/plugins/trivy).

## Inputs

To use the Trivy plugin, you need to pass the following inputs:

1. `version` (**Required**) - the specific version of Trivy you wish to use
2. `directory` (**Required**) - the path to the directory with the IaC code to analyze (the root folder is your project's root folder)
3. `global-flags` (Optional) - a string containing global flags as one string, read more [here](https://aquasecurity.github.io/trivy/v0.36/docs/references/customization/config-file/#global-options)
4. `flags` (Optional) - a string containing additional flags as one string, read more [here](https://aquasecurity.github.io/trivy/v0.36/docs/references/cli/config/)

## Example

In this example, we will run trivy analysis on your root folder before the `terraform plan` step of the deployment. We will call that step "Execute Trivy":

```yaml  theme={null}
version: 2  
deploy:  
  steps:  
    terraformPlan:  
      before:  
        - name: Execute Trivy # The name that will be presented in the UI for this step  
          use: https://github.com/env0/env0-trivy-plugin
          inputs:  
            version: v0.36.1  
            directory: .  
            global-flags: --format table  
            flags: --exit-code 1
```

Built with [Mintlify](https://mintlify.com).

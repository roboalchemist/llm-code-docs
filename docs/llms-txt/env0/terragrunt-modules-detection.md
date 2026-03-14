# Source: https://docs.envzero.com/guides/integrations/plugins/terragrunt-modules-detection.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Terragrunt Module Detection

> Detect changed Terragrunt modules in pull requests to run plans only for affected modules

If you use [Terragrunt run all](/guides/admin-guide/templates/terragrunt/#run-all-terragrunt-command-checkbox) with [PR Plan](/guides/admin-guide/environments/plan-on-pull-request) feature you can use this [plugin](https://github.com/env0/env0-terragrunt-modules-detection-plugin) for running plan only for changed modules in the PR by using this code:

```
version: 2
deploy:
  steps:
    terraformPlan:
      before:
        - name: Terragrunt Modules Detection
          use: https://github.com/env0/env0-terragrunt-modules-detection-plugin
```

This will detect which code was changed and based on that will decide which module to run based on the files that were changed as part of the Pull request.

For more information, check out the [Modules Detection Plugin Repository](https://github.com/env0/env0-terragrunt-modules-detection-plugin)

Built with [Mintlify](https://mintlify.com).

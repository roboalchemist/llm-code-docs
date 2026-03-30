# Source: https://docs.envzero.com/guides/admin-guide/additional-controls.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Additional Deployment Controls

> Configure advanced deployment controls via environment variables at organization, template, or project level

<Warning>
  Disclaimer

  Additional Controls are features that aren’t available through the user interface, but can be used by setting the appropriate environment variables, at the Organization, Template, Project, or Environment level.
</Warning>

<Info>
  **OpenTofu Support**

  All controls that relate to Terraform should control OpenTofu the same way.
</Info>

## Terraform Targeted Apply

Using the `ENV0_TERRAFORM_TARGET` environment variable, you can allocate specific resources that will be targeted for apply. The variable’s value will be passed to Terraform via the '-target\` flag.\
Read more [here](https://www.terraform.io/docs/commands/plan.html#target-resource).

## Specify Terraform/Terragrunt Versions

Using the `ENV0_TF_VERSION` environment variable, you can specify the Terraform version you would like your environment to use. You can read more [here](/guides/admin-guide/templates/iac-binaries-versions).

You can also use the `ENV0_TERRAGRUNT_VERSION` environment variable to specify the Terragrunt version for your applicable Terragrunt deployments.

Another way to determine the version for both Terraform and Terragrunt is a version file. When a file with a name. `{type}-version` (type being either "terraform" or "terragrunt") exists in the project's root directory the version is resolved based on the content of the file. The sole content of the file should be the version you wish to use.

The order of precedence whenever the version is specified using more than one option is as follows: env zero environment variable, version file, version selected when creating/updating the template.

<Info>
  **Specifying version in Terraform code**

  You can also set the version in your [Terraform code](https://www.terraform.io/docs/configuration/terraform.html#specifying-a-required-terraform-version) and env zero will automatically detect and install the minimum required version specified in your code.
</Info>

## Custom Terraform Variables File

Using the `ENV0_TERRAFORM_CONFIG_FILE_PATH` environment variable, you can select multiple Terraform variable files to pass on to Terraform. The list of filenames should be comma delimited.

## Terraform Backend Config

Using the `ENV0_TERRAFORM_BACKEND_CONFIG` environment variable, you can pick a custom backend config to be used in `terraform init`. The value of the variable will be passed to the `-backend-config` flag.\
If you would like to have multiple `-backend-config` declarations, you can pass the multiple values in the `ENV0_TERRAFORM_BACKEND_CONFIG` environment variable as a comma-delimited string. For example, a value of `/path/to/config/file,key=value` will result in the flags `-backend-config="/path/to/config/file" -backend-config="key=value"`.\
Read more [here](https://developer.hashicorp.com/terraform/language/backend#partial-configuration).

## Enable Cost Tagging Per Environment

Cost tagging works on the project level and once enabled, env zero will tag every environment under that project. Sometimes (mainly for debugging purposes) you might wish to turn on cost tagging only for a specific environment and not for the whole project.\
You can do that using the `ENV0_ENABLE_COST_TAG` environment variable.

## Adding Custom Resource Tagging

When cost tagging is enabled for an environment, using the `ENV0_CUSTOM_TAGS` environment variable will enable custom resource tags to be applied using terratag (for Terraform and Terragrunt) or natively for other IaCs.\
The variable value should be supplied in the form of: `{"aTagName": "aTagValue", ...}`.\
This would apply the tags to all taggable resources in the environment.\
You can use other environment variables in the tags, for example `{"created_by": "$ENV0_ENVIRONMENT_CREATOR_NAME"}`. See [this list](/guides/admin-guide/custom-flows/#exposed-env0-system-environment-variables) for the environment variables that env zero exposes.

## Skip Workspace Commands

For each environment, select the existing terraform workspace or create one if necessary. The workspace will be deleted upon destroying the environment.\
If you wish not to execute these commands you can skip them by using the`ENV0_SKIP_WORKSPACE` environment variable and set its value to true. Please remove the environment variable altogether or set its value to empty to run the workspace commands.

## Custom Git Clone Arguments

By default, your repository will be cloned with the arguments `--depth=1 --single-branch`.\
You can override this by supplying the environment variable `ENV0_GIT_CLONE_ARGS`, the value of which will be sanitized and appended to the Git clone command instead of the default arguments.

## Skip Git Submodules

By default, if you have Git submodules configured in your repository, env zero clones them with a depth of 1.\
If you do not wish to clone your Git submodules, you can manage that via the `ENV0_SKIP_SUBMODULE_GIT_CLONE` environment variable and set its value to `true`.\
If you remove the environment variable altogether or set its value to be empty, env zero will clone your Git submodules.

## Skip Get Working Directory

If you do not want to use the current working directory, set `ENV0_IGNORE_STATE=true`

## Skip Plan Step in Terragrunt Run-All

If `run-all apply` is failing, you can try skipping the plan step by setting `ENV0_TERRAGRUNT_RUN_ALL_SKIP_PLAN=true` with "Approve Plan Automatically" enabled. Read more [here](/guides/admin-guide/templates/terragrunt/#run-all-terragrunt-command-checkbox)

## Ansible Flags and Variables

You can set any environment variable prefixed by `ANSIBLE_CLI_` to set any flag for `ansible-playbook`.

Additionally - you can set any environment variable prefixed by `ANSIBLE_VAR_` to set any extra variable to be added under the `--extra-vars` flag.

Read more [here](/guides/admin-guide/templates/ansible/#additional-controls).

## Ansible Custom Playbook File

By default, env zero will try to run `ansible-playbook` on `playbook.y[a]ml`.

You can control that file's name by setting the `ENV0_ANSIBLE_PLAYBOOK` variable.

## Skip Ansible Check Playbook Step

If you like to skip the Ansible check step, add an environment variable named `ENV0_SKIP_ANSIBLE_CHECK` and set the value to `true`. Read more [here](/guides/admin-guide/templates/ansible/#skipping-ansible-check-step).

## Suggested Blog Content

[Terraform Modules Guide](https://www.env0.com/blog/terraform-modules)

[Terraform Plan Examples](https://www.env0.com/blog/terraform-plan)

[Managing Terraform Variable Hierarchy](https://www.env0.com/blog/managing-terraform-variable-hierarchy)

[Manage Terraform Remote State with a Remote Backend](https://www.env0.com/blog/terraform-remote-state-using-a-remote-backend)

Built with [Mintlify](https://mintlify.com).

# Source: https://docs.envzero.com/guides/admin-guide/remote-backend/working-with-terraform-cloud-remote-backend.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Integrating With Terraform Cloud Remote Backend

> Use env zero with Terraform Cloud remote backend for state storage during evaluation or migration

<Warning>
  **Disclaimer**

  As a default when using env zero we don't recommend to store your state in Terraform Cloud, and if using env zero we would recommend using a different remote backend.

  There are a few limitations to using this setup and it's hard to maintain.

  We recommend using this setup only for evaluating the env zero platform and if you are currently managing your state with Terraform Cloud.
</Warning>

If you are currently working with Terraform Cloud remote backend and would like to use env zero with this setup you will need to do the following:

1. Local execution mode - First you need to change the workspace settings in Terraform Cloud to enable local runs, so you need to go to the `General Settings` of the workspace and change the `Execution Mode` to Local.
2. Generating a token for authentication - In order to authenticate to Terraform Cloud remote backend you need to generate an API token, so under the `User settings` under `Tokens` and create an API token. Please save the token, we will need it in the further steps.
3. If you are running terraform version 1.2.0 or up you will need to add the following environment variables:

| Variable Name                | Value                                           |
| :--------------------------- | :---------------------------------------------- |
| `TF_TOKEN_app_terraform_io` | The API token you've created in Terraform Cloud |
| `ENV0_SKIP_WORKSPACE`        | `true`                                          |

1. If not you will need to add an `env0.yml` file -  In your Terraform git repo you will need to add an `env0.yml` file in the Terraform folder and add the following code:

```text  theme={null}
version: 1
deploy:
  steps:
    setupVariables:
      after:
        - printf "credentials \"app.terraform.io\" {\n token = \"${TF_CLOUD_TOKEN}\"\n}" > ~/.terraformrc
destroy:
  steps:
    setupVariables:
      after:
        - printf "credentials \"app.terraform.io\" {\n token = \"${TF_CLOUD_TOKEN}\"\n}" > ~/.terraformrc
```

In addition, you will need to add template variables - you'll need to add 2 variables in your env zero template:

| Variable Name         | Value                                           |
| :-------------------- | :---------------------------------------------- |
| `TF_CLOUD_TOKEN`      | The API token you've created in Terraform Cloud |
| `ENV0_SKIP_WORKSPACE` | `true`                                          |

1. Now you are ready to run your Template and the remote backend should be stored in Terraform Cloud.

## Suggested Blog Content

[Terraform Modules Guide](https://www.env0.com/blog/terraform-modules)

[Terraform Plan Examples](https://www.env0.com/blog/terraform-plan)

[Managing Terraform Variable Hierarchy](https://www.env0.com/blog/managing-terraform-variable-hierarchy)

[Manage Terraform Remote State with a Remote Backend](https://www.env0.com/blog/terraform-remote-state-using-a-remote-backend)

Built with [Mintlify](https://mintlify.com).

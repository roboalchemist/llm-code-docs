# Source: https://docs.envzero.com/changelogs/2023/01/remote-plans.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 🕹 Remote Plans

> Centralizing Terraform execution is a great way to make sure you have effective IaC governance. While it’s preferred that teams directly use env zero to run IaC, sometimes you just need to run a terraform plan, apply, or destroy locally. Now, with env zero Remote Plans, you can run `terraform plan` locally - even with uncommitted code - and the run will be executed inside the env zero Platform, keeping with your organization policies, governance, and auditing requirements.

Centralizing Terraform execution is a great way to make sure you have effective IaC governance. While it’s preferred that teams directly use env zero to run IaC, sometimes you just need to run a terraform plan locally.

Now, with env zero Remote Plans, you can run `terraform plan` locally - even with uncommitted code - and the run will be executed inside the env zero Platform, keeping with your organization policies, governance, and auditing requirements.

## ✨ Running a Remote Plan ✨

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/4i75qYgyhlssLgkA/images/changelogs/2023/01/3b838b3-image_5.png?fit=max&auto=format&n=4i75qYgyhlssLgkA&q=85&s=0c5bdd5e569424dffb4552e20492a378" alt="Remote Plan execution interface showing terraform plan command execution in env zero platform" width="2910" height="1412" data-path="images/changelogs/2023/01/3b838b3-image_5.png" />
</Frame>

In order to use run a remote plan your env zero environment needs to be using the env zero [Remote Backend](/guides/admin-guide/remote-backend). Once you create a [personal API key](/guides/admin-guide/user-role-and-team-management/api-keys#personal-api-key) and use the [login](/guides/admin-guide/remote-backend/login#local-login-to-env0-remote-backend) command, every time you will run a `terraform plan` command, env zero will handle the execution.

For more information, please visit our [docs](/guides/admin-guide/remote-backend/remote-plan).

## Suggested Blog Content

[Terraform Modules Guide](https://www.env0.com/blog/terraform-modules)

[Terraform Plan Examples](https://www.env0.com/blog/terraform-plan)

[Managing Terraform Variable Hierarchy](https://www.env0.com/blog/managing-terraform-variable-hierarchy)

[Manage Terraform Remote State with a Remote Backend](https://www.env0.com/blog/terraform-remote-state-using-a-remote-backend)

Built with [Mintlify](https://mintlify.com).

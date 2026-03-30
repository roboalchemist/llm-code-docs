# Source: https://docs.envzero.com/changelogs/2022/07/terragrunt-run-all-support.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 🏃🏻‍♀️ Terragrunt run-all support

> env0 supports a wide variety of IaC platforms, including Terragrunt, but up until now, it lacked the support for running multiple modules at the same deployment, a feature that is supported by Terragrunt's run-all command. Another advantage is the ability to define dependencies between Terraform modules in code. Today we are proud to deliver this support out of the box with env0!

env zero supports a wide variety of IaC platforms, including [Terragrunt](https://terragrunt.gruntwork.io/), but up until now it lacked the support for running multiple modules at the same deployment, a feature that is supported by Terragrunt's [run-all command](https://terragrunt.gruntwork.io/docs/features/execute-terraform-commands-on-multiple-modules-at-once/#the-run-all-command). Another advantage is the ability to define dependencies between Terraform modules in code. Today we are proud to deliver this support out of the box with env zero!

### ✨ Terragrunt run-all support ✨

env zero now supports the `run-all` command, which will allow you to utilize all of its features for multiple modules in the same environment: CI/CD, drift detection, cost estimation, and more.

Within Terragrunt template configuration, under `Advanced` settings - check `Execute run-all commands on multiple modules`

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/4i75qYgyhlssLgkA/images/changelogs/2022/07/screen_shot_2022-07-04_at_91213.png?fit=max&auto=format&n=4i75qYgyhlssLgkA&q=85&s=42f64b49aeffbfe3be1d0e1741663d7a" alt="Screen Shot 2022-07-04 at 9.12.13" width="1702" height="946" data-path="images/changelogs/2022/07/screen_shot_2022-07-04_at_91213.png" />
</Frame>

<Callout type="info" title="Version Support">
  The minimum supported Terragrunt version for run-all is <strong>0.28.1</strong>.
</Callout>

*That's it!* When you use a template with `Execute run-all commands on multiple modules` configuration, env0 runs the `terragrunt run-all` command for you, and every module in your templates project is deployed simultaneously.

Built with [Mintlify](https://mintlify.com).

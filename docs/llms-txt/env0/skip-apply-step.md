# Source: https://docs.envzero.com/guides/policies-governance/skip-apply-step.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Skipping the Apply Step

> Automatically skip the apply step when a Terraform plan has no resource changes in env zero

If you mark "Skip apply when plan has no changes", under "Project Settings" -> "Policies" tab, the apply step will be skipped completely when there are no pending resource changes in the terraform plan.

This is especially useful for automated deploys, in case you want to have your continuous deployment / scheduled environments require user approval to apply. In such a case, checking this box will only require user approval for plans that have actual resource changes in them.

<Frame caption="Project Settings - Policies">
  <img src="https://mintcdn.com/envzero-b61043c8/t0QBBK-2O7wlTUvX/images/guides/policies-governance/project_settings_policies_skip_apply_configuration.png?fit=max&auto=format&n=t0QBBK-2O7wlTUvX&q=85&s=e8e3027b1a210f6ced64f0f4f9711b08" alt="Project settings policies skip apply configuration" width="2230" height="1880" data-path="images/guides/policies-governance/project_settings_policies_skip_apply_configuration.png" />
</Frame>

Built with [Mintlify](https://mintlify.com).

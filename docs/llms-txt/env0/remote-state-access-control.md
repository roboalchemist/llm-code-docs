# Source: https://docs.envzero.com/changelogs/2023/03/remote-state-access-control.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 🤳🔑 Remote State Access Control

> When working with Terraform, it's common to need access to the state of a remote backend environment. However, because this state can contain sensitive information, it's important to restrict access to it in order to prevent misuse.
With our new remote state access control feature, you can now specify who is authorized to access your environment's state.

When working with Terraform, it's common to need access to the state of a remote backend environment. However, since this state can contain sensitive information, it's crucial to restrict access to prevent misuse.

That's where env0's new remote state access control feature comes in. With it, you can specify who is authorized to access your environment's state.

## ✨ Setting Your Environment State Access ✨

To set up access control, simply go to the Environment -> Settings tab and select which projects are allowed to access the environment's state. You have the option to limit access to specific projects or their subprojects or allow access to all environments in your organization.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/U9rcMIDzc38oPcXx/images/changelogs/2023/03/d3bf3db-image.png?fit=max&auto=format&n=U9rcMIDzc38oPcXx&q=85&s=0cd894b81858f46937fdd6ccd9fcf327" alt="Feature demonstration screenshot showing new functionality" width="2630" height="1496" data-path="images/changelogs/2023/03/d3bf3db-image.png" />
</Frame>

By using this feature, you can ensure that only the right people have access to the sensitive information in your Terraform state. This helps you maintain the security of your infrastructure while enabling your team to work efficiently.

After saving these settings only environments in the selected projects or their subprojects will be allowed to fetch that environment's state. see [our docs](/guides/admin-guide/remote-backend/state-access-control) for more information

## Suggested Blog Content

[Terraform Modules Guide](https://www.env0.com/blog/terraform-modules)

[Terraform Plan Examples](https://www.env0.com/blog/terraform-plan)

[Managing Terraform Variable Hierarchy](https://www.env0.com/blog/managing-terraform-variable-hierarchy)

[Manage Terraform Remote State with a Remote Backend](https://www.env0.com/blog/terraform-remote-state-using-a-remote-backend)

Built with [Mintlify](https://mintlify.com).

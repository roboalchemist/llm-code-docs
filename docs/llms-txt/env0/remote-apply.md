# Source: https://docs.envzero.com/guides/admin-guide/remote-backend/remote-apply.md

# Source: https://docs.envzero.com/changelogs/2023/12/remote-apply.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 🛜 Remote Apply

> with env zero Remote Apply, you can run `terraform apply` locally - even with uncommitted code - and the run will be executed inside the env zero Platform, keeping with your organization policies, governance, and auditing requirements.

Centralizing Terraform execution is a great way to make sure you have effective IaC governance. While it's preferred that teams directly use env zero to run IaC, sometimes you just need to run a terraform apply locally.

Now, with env zero Remote Apply, you can run `terraform apply` locally - even with uncommitted code - and the run will be executed inside the env zero Platform, keeping with your organization policies, governance, and auditing requirements.

## ✨ Running a Remote Apply ✨

First, you will have to turn it on for the specific environment you'd like to remote apply

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/hr9e779VSnIZk8JC/images/changelogs/2023/12/b70bb3e-image.png?fit=max&auto=format&n=hr9e779VSnIZk8JC&q=85&s=db8483a292f267708b8889d274628ffc" alt="Remote Apply configuration interface showing how to enable remote apply for a specific environment" width="866" height="681" data-path="images/changelogs/2023/12/b70bb3e-image.png" />
</Frame>

To use remote apply, your env zero environment must be configured with env zero's [Remote Backend](/guides/admin-guide/remote-backend). After creating a [personal API key](/guides/admin-guide/user-role-and-team-management/api-keys#personal-api-key) and executing the [login](/guides/admin-guide/remote-backend/login#local-login-to-env0-remote-backend) command,  every time you will run a `terraform apply -auto-approve` command, env zero will handle the execution.

For more information, please visit our [docs](/guides/admin-guide/remote-backend/remote-apply).

Built with [Mintlify](https://mintlify.com).

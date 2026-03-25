# Source: https://docs.envzero.com/changelogs/2023/07/plan-and-apply-from-pr-comments-support-for-azure-devops.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 🔵 Plan and Apply from PR comments support for Azure DevOps

> If you are not familiar with our Plan and Apply from PR comments feature, env0 lets you manage your Infrastructure as Code (IaC) deployments directly from your VCS provider.   By commenting with env0 commands on a pull request, it is possible to interact with your env0 environments without the need to log in to the env0 platform. We now support Plan and Apply from PR comments for Azure DevOps.

If you are not familiar with our Plan and Apply from PR comments feature, env0 lets you manage your Infrastructure as Code (IaC) deployments directly from your VCS provider.\
By commenting with env0 commands on a pull request, it is possible to interact with your env0 environments without the need to log in to the env0 platform. We now support Plan and Apply from PR comments for Azure DevOps.

## ✨ Invoking deployments from PR comments   ✨

For full details about this feature follow the [env0 documentation](/guides/admin-guide/environments/plan-and-apply-from-pr-comments).\
Here are the main commands you can use:

### env0 plan command

🔂    `env0 plan -e {environments aliases}` - runs a plan on the env0 environments aliases. Aliases can be comma-separated if you like to run more than one environment.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/U9rcMIDzc38oPcXx/images/changelogs/2023/07/cfc6207-image.png?fit=max&auto=format&n=U9rcMIDzc38oPcXx&q=85&s=afd63a581964ccdef70bfae405e26455" alt="Feature demonstration screenshot showing new functionality" width="1968" height="664" data-path="images/changelogs/2023/07/cfc6207-image.png" />
</Frame>

### env0 apply command

⏯️     `env0 apply -e {environments aliases}` - runs apply on the env0 environments aliases. Aliases can be comma-separated if you like to run more than one environment.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/U9rcMIDzc38oPcXx/images/changelogs/2023/07/f79d0d4-image.png?fit=max&auto=format&n=U9rcMIDzc38oPcXx&q=85&s=094b049d87f9a5569e63aa8d527f049f" alt="Feature demonstration screenshot showing new functionality" width="1958" height="564" data-path="images/changelogs/2023/07/f79d0d4-image.png" />
</Frame>

Built with [Mintlify](https://mintlify.com).

# Source: https://docs.envzero.com/changelogs/2024/06/approval-flow-for-workflows.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 🤹📝 Approval Flow for Workflows

> Managing your team's dependencies between environments is now easier and more powerful than ever! With the newly available approval flow for workflows, you can now define what environments’ plans you would like to review and have more refined control over your workflows.

Managing your team's dependencies between environments is now easier and more powerful than ever! With the newly available approval flow for workflows, you can now define what environments’ plans you would like to review and have more refined control over your workflows.

## ✨ Defining your environments to require approval✨

Defining the environments in your workflow to require approval can be done in a couple of ways:

1. By defining the new `requiresApproval` field in the workflow file in the environments definition.
2. By using the UI now available approval checkbox after selecting your desired environment to have approval for.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/hr9e779VSnIZk8JC/images/changelogs/2024/06/7b7f30d-image.png?fit=max&auto=format&n=hr9e779VSnIZk8JC&q=85&s=62086fc0c8317717d23f901446bd5053" alt="Feature demonstration screenshot showing new functionality" width="2660" height="986" data-path="images/changelogs/2024/06/7b7f30d-image.png" />
</Frame>

1. By using OPA approval policies for the project/templates applying them to the environments in the workflow.

Once you've defined your workflow to require approvals and it's been run you will be able to go over the pending deployments and have control over continuing/canceling the downstream environments.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/hr9e779VSnIZk8JC/images/changelogs/2024/06/fbce52c-image.png?fit=max&auto=format&n=hr9e779VSnIZk8JC&q=85&s=48a70fd44fed44acf2304e518daa188d" alt="Feature demonstration screenshot showing new functionality" width="2808" height="1674" data-path="images/changelogs/2024/06/fbce52c-image.png" />
</Frame>

Built with [Mintlify](https://mintlify.com).

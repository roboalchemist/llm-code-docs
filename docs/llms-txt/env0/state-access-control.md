# Source: https://docs.envzero.com/guides/admin-guide/remote-backend/state-access-control.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring State Access Control

> Control which environments and projects can access an environment's remote state in env zero

## State Access Control

Terraform allows accessing states stored on remote backends using its built in [terraform\_remote\_state](https://developer.hashicorp.com/terraform/language/state/remote-state-data) data resource, env zero allows specifying which environments would be allowed to access an environment's state on env zero triggered deployments.

## Setting Your Environment State Access

To set your environment's state access, simply go to the Environment -> Settings tab and select which projects are allowed to access the environment's state. You can choose to allow access to all environments in your organization or limit access to specific projects or their subprojects.

<img src="https://mintcdn.com/envzero-b61043c8/pvGFjFxaiqGDTFG3/images/guides/admin-guide/remote-backend/5c9c358-image.png?fit=max&auto=format&n=pvGFjFxaiqGDTFG3&q=85&s=a439ded099f406140ce26173896fe063" alt="" width="2630" height="1496" data-path="images/guides/admin-guide/remote-backend/5c9c358-image.png" />

After saving these settings only environments in the selected projects or their subprojects will be allowed to fetch that environment's state.

<Info>
  **Note:**

  These settings will only affect deployments that are running inside env zero, for local runs or state access that is from outside env zero the logged-in API key / User personal key permissions will determine if they can access the state or not.
</Info>

Built with [Mintlify](https://mintlify.com).

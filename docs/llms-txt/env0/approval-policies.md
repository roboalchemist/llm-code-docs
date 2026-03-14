# Source: https://docs.envzero.com/guides/policies-governance/approval-policies.md

# Source: https://docs.envzero.com/changelogs/2023/07/approval-policies.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# ✅ Approval Policies

> Guardrails are essential for managing infrastructure. While popular IaC tools make provisioning of resources easy, they often lack the capability to prevent changes when their outcome is not desired. Role-based access grants separation of concerns regarding different actions in the system, but is not flexible enough to prevent more granular changes that might happen to the infrastructure.

Guardrails are essential for managing infrastructure. While popular IaC tools make provisioning of resources easy, they often lack the capability to prevent changes when their outcome is not desired. Role-based access grants separation of concerns regarding different actions in the system, but is not flexible enough to prevent more granular changes that might happen to the infrastructure.

## ✨ Configuring Approval Policies✨

env zero enables applying approval policies for the environments managed using the app.

env zero leverages the power of the [Open Policy Agent](https://www.openpolicyagent.org/) engine to allow users to define custom policies for their deployed environments.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/U9rcMIDzc38oPcXx/images/changelogs/2023/07/267f119-project_policy_arrow.jpg?fit=max&auto=format&n=U9rcMIDzc38oPcXx&q=85&s=9bc26243e9794a98e313741c49f8d03f" alt="Feature demonstration screenshot showing new functionality" width="841" height="863" data-path="images/changelogs/2023/07/267f119-project_policy_arrow.jpg" />
</Frame>

### Examples

There are many cases where approval policies may come useful:

* Requiring more than a certain threshold of approvers
* Deny any change that its expected cost cross a predefined limit
* Prevent removing critical resources from an environment
* Allowing only a sub-set of users to change specific resources within an environment

And the list can go on and on.

Examples may be found in our [GitHub repository](https://github.com/env0/approval-policies)

Read all about it in [our docs - Approval Policies](/guides/policies-governance/approval-policies)

Built with [Mintlify](https://mintlify.com).

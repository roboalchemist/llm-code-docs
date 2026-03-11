# Source: https://docs.envzero.com/guides/policies-governance/ready-to-use-policies.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Ready-To-Use Policies

> Pre-configured guardrails that you can integrate into your Infrastructure as Code workflows to enforce governance, security, and compliance standards

env zero's ready-to-use policies provide pre-configured guardrails that you can integrate into your Infrastructure as Code (IaC) workflows. These policies help enforce governance, security, and compliance standards without requiring you to write custom policy code from scratch.

<Note>
  All policy code is open source, allowing you to review exactly what each policy does and how it works.
</Note>

## Policy categories

Policies are organized into seven categories that cover key areas of infrastructure governance:

* **Security**: Protect your infrastructure from vulnerabilities and ensure secure configurations
* **Networking**: Control network access, configuration, and connectivity rules
* **IAM**: Manage identity and access permissions across your cloud resources
* **Compliance**: Meet regulatory requirements and industry standards
* **Cost**: Monitor and control infrastructure spending and resource usage
* **Performance**: Optimize resource allocation and system performance
* **Governance**: Enforce organizational policies and operational standards

## Viewing your policies

To see all policies currently configured in your organisation:

<Steps>
  <Step title="Navigate to policies">
    Click on **Policies** in the organisation menu to access your policy dashboard.
  </Step>

  <Step title="Review policy table">
    The policy table displays:

    * All configured policies in your organisation
    * Policy categories and names
    * Assignment scope (organisation, specific projects, or environments)

    The table gives you a clear view of where each policy is applied, helping you understand current governance coverage across projects and environments.

    <Frame caption="Organization settings policies configuration">
      <img src="https://mintcdn.com/envzero-b61043c8/rxuvpp4wRqrrS0PC/images/guides/policies-governance/ready-to-use-policies/policies-table.png?fit=max&auto=format&n=rxuvpp4wRqrrS0PC&q=85&s=62bc2d1b920ef105d130258f3a8ff2e1" alt="Organization settings policies configuration showing policy table and management interface" width="2980" height="796" data-path="images/guides/policies-governance/ready-to-use-policies/policies-table.png" />
    </Frame>
  </Step>
</Steps>

## Adding policies

To add a new policy to your workflow:

<Steps>
  <Step title="Start policy creation">
    Click **Add Policy** in the policies section to open the policy selection screen.
  </Step>

  <Step title="Select policy">
    Browse the available policies and select the one that matches your requirements. You can filter by category or search by name.

    <Frame caption="Approval policy configuration interface">
      <img src="https://mintcdn.com/envzero-b61043c8/rxuvpp4wRqrrS0PC/images/guides/policies-governance/ready-to-use-policies/policies-catalog.png?fit=max&auto=format&n=rxuvpp4wRqrrS0PC&q=85&s=ef3e62b9e5cacce940f08990698d837f" alt="Approval policy configuration interface showing policy setup and validation options" width="1668" height="824" data-path="images/guides/policies-governance/ready-to-use-policies/policies-catalog.png" />
    </Frame>

    <Note>
      Review the policy details and open source code to understand exactly what the policy enforces before selection.
    </Note>
  </Step>

  <Step title="Configure policy settings">
    Fill in the required parameters for the selected policy. Each policy includes specific settings relevant to its function.

    <Frame caption="Approval policy configuration interface">
      <img src="https://mintcdn.com/envzero-b61043c8/nCK-nFJibRgxdxVW/images/guides/policies-governance/ready-to-use-policies/policy-settings.png?fit=max&auto=format&n=nCK-nFJibRgxdxVW&q=85&s=a5628ebc58d640a879ac1319100c387b" alt="Approval policy configuration interface showing policy setup and validation options" width="2956" height="924" data-path="images/guides/policies-governance/ready-to-use-policies/policy-settings.png" />
    </Frame>
  </Step>

  <Step title="Set assignment scope">
    Choose where the policy should apply:

    * **Organisation-wide**: Applies to all projects and environments
    * **Specific projects**: Applies only to selected projects
    * **Specific environments**: Applies only to selected environments

    <Frame caption="Approval policies step during deployment">
      <img src="https://mintcdn.com/envzero-b61043c8/rxuvpp4wRqrrS0PC/images/guides/policies-governance/ready-to-use-policies/policies-assignment-scope.png?fit=max&auto=format&n=rxuvpp4wRqrrS0PC&q=85&s=16fa07eefe7ff480b8f8e3770eee427d" alt="Interface screenshot showing approval policies step with policy evaluation results" width="2986" height="1078" data-path="images/guides/policies-governance/ready-to-use-policies/policies-assignment-scope.png" />
    </Frame>

    <Warning>
      Organisation-wide policies affect all deployments. Consider scope carefully.
    </Warning>
  </Step>

  <Step title="Activate policy">
    Save the configuration to activate the policy. It will now be enforced according to the chosen scope.
  </Step>
</Steps>

## Policy enforcement during deployment

Once configured, policies are enforced as part of the deployment workflow and appear during the approval process.

### Approval policies step

During deployment runtime, you can view active policies in the **Approval policies** step of the deployment process. This step shows:

* Which policies are being evaluated
* Policy evaluation results
* Any policy violations that need attention
* Approval requirements based on policy outcomes

<Frame caption="Approval policies step during deployment">
  <img src="https://mintcdn.com/envzero-b61043c8/rxuvpp4wRqrrS0PC/images/guides/policies-governance/ready-to-use-policies/approval-policies-step.png?fit=max&auto=format&n=rxuvpp4wRqrrS0PC&q=85&s=9b629eb0bc6c81b10778b02a2fc2b23c" alt="Interface screenshot showing approval policies step with policy evaluation results" width="1414" height="672" data-path="images/guides/policies-governance/ready-to-use-policies/approval-policies-step.png" />
</Frame>

<Note>
  The Approval policies step ensures that all governance requirements are validated before infrastructure changes are applied.
</Note>

Ready-to-use policies streamline governance by providing battle-tested rules you can deploy immediately, reducing the time and effort needed to establish comprehensive infrastructure oversight.

Built with [Mintlify](https://mintlify.com).

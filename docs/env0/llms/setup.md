# Source: https://docs.envzero.com/guides/policies-governance/code-optimizer/setup.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Setup & Prerequisites

> Configure Code Optimizer for your infrastructure repositories

## Prerequisites

Before using Code Optimizer, ensure you have:

<Steps>
  <Step title="User Permissions">
    Your permissions determine what you can do in Code Optimizer:

    **Admin role or Edit Organization Settings permission:**

    * Configure VCS integrations
    * Run scans
    * Generate fixes

    **View Dashboard permission:**

    * View Code Optimizer
    * Run scans

    Learn more: [User Roles & Permissions](/guides/admin-guide/user-role-and-team-management/user-management)
  </Step>

  <Step title="VCS Integration">
    Connect your VCS provider with env zero. Choose the connection type based on your provider:

    **For GitHub/GitHub Enterprise:**

    * **Deployment Pipeline** - Scanning only
    * **Code Write** - Scanning + PR creation

    **For other VCS providers** (GitLab, Bitbucket, Azure DevOps):

    * **Deployment Pipeline** - Scanning only (PR creation not yet supported)

    Learn more: [VCS Connection Types](/guides/admin-guide/manage-vcs#connection-types)
  </Step>

  <Step title="Repository Selection">
    Select the repositories you want to scan during the VCS integration process. Code Optimizer will scan all authenticated repositories.
  </Step>

  <Step title="Terraform Code">
    Code Optimizer currently supports **Terraform / OpenTofu** (HCL). Support for other IaC frameworks coming soon.
  </Step>
</Steps>

<Warning>
  **Self-Hosted Agent Version Requirement**: Code Optimizer is supported on self-hosted agents from version **v4.0.29** and up. If you're using a self-hosted agent, ensure it's running at least this version to use Code Optimizer features.
</Warning>

## Next Steps

<CardGroup cols={2}>
  <Card title="Start Scanning" icon="magnifying-glass" href="/guides/policies-governance/code-optimizer/scanning">
    Trigger your first repository scan
  </Card>

  <Card title="Generate Fixes" icon="wand-magic-sparkles" href="/guides/policies-governance/code-optimizer/fixes">
    Create AI-powered pull requests
  </Card>
</CardGroup>

Built with [Mintlify](https://mintlify.com).

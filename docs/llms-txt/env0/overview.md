# Source: https://docs.envzero.com/guides/policies-governance/code-optimizer/overview.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Code Optimizer Overview

> AI-powered static analysis and automated fixes for your HCL infrastructure code

<Note>
  **Beta Feature** - Code Optimizer is currently in beta. We're actively improving the feature and welcome your feedback.
</Note>

## What is Code Optimizer?

Code Optimizer is an AI-powered static analyzer that helps platform engineers and DevOps teams maintain high-quality infrastructure-as-code without slowing down delivery. It automatically scans your HCL code for technical issues and best-practice violations, then generates AI-powered fixes and creates pull requests, all with one click.

## Why Code Optimizer?

Platform engineers push IaC changes rapidly, but thorough code reviews are time-consuming and often deprioritized. Code Optimizer helps catch critical issues like:

* **Security risks** - Unencrypted storage, open security groups, compliance violations
* **Code structure** - Poorly structured modules, inconsistent naming, unused variables
* **Configuration gaps** - Missing lifecycle rules, backend configurations, or state drift safeguards
* **Technical debt** - Deprecated syntax, non-compliant patterns that break at scale

**The result?** Hidden technical debt that breaks at scale, inconsistent code quality across teams, and slow manual remediation.

## How Code Optimizer Solves This

1. **Detecting Issues** - Scans repositories using industry-standard tools (for example, TFLint and Checkov)
2. **AI-Powered Remediation** - Generates context-aware code fixes using AI and creates pull requests on-demand
3. **Centralized Visibility** - Track and manage all issues in one place

## Key Features

* **Automated Scanning** - Detect quality, security, and compliance issues across all repositories
* **AI-Powered Fixes** - Generate context-aware code fixes with one click
* **Pull Request Workflow** - Fixes are submitted as PRs for team review
* **Centralized View** - Track, prioritize, and manage all issues in one place

## How It Works

<Frame>
  ```mermaid  theme={null}
  %%{init: {'theme':'neutral', 'themeVariables': { 'fontSize':'16px', 'primaryColor':'#3b82f6', 'primaryTextColor':'#fff', 'primaryBorderColor':'#1e40af', 'lineColor':'#6b7280', 'secondaryColor':'#10b981', 'tertiaryColor':'#8b5cf6'}}}%%
  graph TB
      A["📂 Repository Connected"] --> B["🔍 Manual Scan Trigger"]
      B --> C["⚡ TFLint + Checkov Analysis"]
      C --> D["📊 Issues Table"]
      D --> E{"🎯 Action Required?"}
      E -->|"Generate Fix"| F["🤖 AI Analysis"]
      F --> G["📝 Create GitHub PR"]
      G --> H["👥 Team Review"]
      H --> I["✅ Merge & Re-scan"]
      I --> J["Auto-Resolve"]
      E -->|"Ignore"| K["🔇 Mark as Ignored"]

      style A fill:#3b82f6,stroke:#1e40af,stroke-width:2px,color:#fff
      style D fill:#f59e0b,stroke:#d97706,stroke-width:2px,color:#fff
      style F fill:#8b5cf6,stroke:#7c3aed,stroke-width:2px,color:#fff
      style J fill:#10b981,stroke:#059669,stroke-width:2px,color:#fff

  ```
</Frame>

### Workflow

1. **Scan** - Trigger manual scans to detect issues
2. **Review** - View issues with severity and context
3. **Fix** - Generate AI-powered fixes for selected issues
4. **Merge** - Review and merge PRs created by Code Optimizer
5. **Verify** - Re-scan to confirm issues are resolved

## Getting Started

<CardGroup cols={2}>
  <Card title="Setup & Prerequisites" icon="gear" href="/guides/policies-governance/code-optimizer/setup">
    Configure VCS integration and connect your repositories
  </Card>

  <Card title="Scanning Your Code" icon="magnifying-glass" href="/guides/policies-governance/code-optimizer/scanning">
    Learn how to trigger scans and view results
  </Card>

  <Card title="Generating Fixes" icon="wand-magic-sparkles" href="/guides/policies-governance/code-optimizer/fixes">
    Create AI-powered fixes and automated pull requests
  </Card>
</CardGroup>


Built with [Mintlify](https://mintlify.com).

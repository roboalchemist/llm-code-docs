# Source: https://docs.envzero.com/guides/policies-governance/code-optimizer/scanning.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Scanning Your Code

> Trigger scans and view infrastructure code quality issues

## Overview

Code Optimizer scans your HCL code using industry-standard tools (for example, **TFLint** and **Checkov**). Scans are triggered manually and provide comprehensive coverage of quality, security, and best-practice issues.

## How Scanning Works

When you trigger a scan:

1. **Code Retrieval** - env zero fetches the latest code from your repository using default branch
2. **Parallel Analysis** - Scanners (such as TFLint and Checkov) analyze your files simultaneously
3. **Issue Detection** - Each scanner identifies violations based on its own rules
4. **Results Aggregation** - Issues are combined, deduplicated, and categorized by severity
5. **Results Display** - Issues appear in Code Optimizer with full context

<Note>
  Scans analyze the **current state** of your repository. They don't automatically run on every commit. You trigger them manually when needed.
</Note>

## The Scanners

### TFLint

[TFLint](https://github.com/terraform-linters/tflint) is a Terraform-focused linter that checks for:

* **Syntax errors** and deprecated syntax
* **Provider-specific issues** (AWS, Azure, GCP)
* **Best practice violations** (e.g., missing required variables)
* **Module usage patterns**

TFLint uses a plugin architecture, allowing it to understand provider-specific APIs and constraints.

**Example Issues Detected:**

* Deprecated Terraform syntax (e.g., `v0.11` style interpolations)
* Invalid resource attribute references
* Provider version constraints not specified
* Missing required variables in modules

### Checkov

[Checkov](https://www.checkov.io/) is a static code analysis tool that scans for:

* **Security vulnerabilities** (e.g., open security groups, unencrypted storage)
* **Compliance violations** (CIS, HIPAA, PCI-DSS benchmarks)
* **Cloud best practices** across AWS, Azure, GCP, and more
* **Supply chain security** (suspicious modules, insecure sources)

Checkov uses policy-as-code to define rules, making it highly customizable.

**Example Issues Detected:**

* S3 buckets without encryption
* Security groups allowing unrestricted ingress
* EC2 instances without IMDSv2 enforcement
* Missing tags required for compliance

## Triggering a Scan

<Steps>
  <Step title="Navigate to Code Optimizer">
    From the main navigation, click **Code Optimizer**.
  </Step>

  <Step title="Trigger Scan">
    Click **"Scan Now"** to start the analysis. The scan runs against all authenticated repositories from your VCS integration.
  </Step>

  <Step title="Wait for Results">
    Scan completion time varies based on the number and size of your repositories.
  </Step>
</Steps>

<Tip>
  **Pro Tip**: Run scans after major changes to your infrastructure code or before important releases to catch issues early.
</Tip>

<Info>
  **For Self-Hosted Customers**:

* **Agent Version Requirement**: Code Optimizer is supported on self-hosted agents from version **v4.0.29** and up. Ensure your agent is running at least this version.
* **Batch Size Configuration**: You can configure the repository batch size for scanning by setting the `CODE_OPTIMIZER_REPOSITORY_BATCH_SIZE` environment variable using the `podAdditionalEnvVars` Helm value. Default batch size is **10**.

  Learn more: [Self-Hosted Kubernetes Agent Configuration](/guides/admin-guide/self-hosted-kubernetes-agent#custom/optional-configuration)
</Info>

## Viewing Scan Results

### Issue Details

Click any issue to view:

* **Description** - What the issue is and why it matters
* **File** - File path
* **Severity** - Risk level (High, Medium, Low)
* **Labels** - Best Practice or Security Misconfiguration
* **Affected Environments** - Relevant environments impacted by this issue
* **Generate Code Fix** - Create Pull Request with fix

### Understanding Severity Levels

| Severity   | Description                                   | Typical Examples                                              |
| ---------- | --------------------------------------------- | ------------------------------------------------------------- |
| **High**   | Significant security or compliance violations | Unencrypted secrets, public S3 buckets, overly permissive IAM |
| **Medium** | Best practice violations with moderate impact | Missing encryption, non-optimal configurations, missing tags  |
| **Low**    | Minor quality issues or style violations      | Deprecated syntax, missing descriptions                       |

## Issue States

Issues progress through three states:

### Ongoing

* **Meaning**: Issue detected and not yet addressed
* **Available Actions**: Generate fix, ignore, view details
* **When it appears**: After initial scan or when reappearing in subsequent scans

### Resolved

* **Meaning**: Issue no longer detected in latest scan
* **How it happens**: After merging a fix and triggering a new scan
* **Note**: Will reappear as "Ongoing" if detected again in future scans

### Ignored

* **Meaning**: Marked as false positive or intentional pattern
* **Available Actions**: Un-ignore

## Next Steps

<CardGroup cols={2}>
  <Card title="Generate Fixes" icon="wand-magic-sparkles" href="/guides/policies-governance/code-optimizer/fixes">
    Create AI-powered fixes for detected issues
  </Card>

  <Card title="Back to Overview" icon="arrow-left" href="/guides/policies-governance/code-optimizer/overview">
    Return to Code Optimizer overview
  </Card>
</CardGroup>

Built with [Mintlify](https://mintlify.com).

# Source: https://docs.datadoghq.com/security/code_security/iac_security.md

---
title: Infrastructure as Code (IaC) Security
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security
---

# Infrastructure as Code (IaC) Security

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

Datadog Infrastructure as Code (IaC) Security detects misconfigurations in Terraform and Kubernetes configurations before they're deployed. It flags issues such as missing encryption or overly permissive access in files stored in your connected GitHub, GitLab, or Azure DevOps repositories. Supported file types include standalone Terraform files, local modules, and Kubernetes manifests.

{% image
   source="https://datadog-docs.imgix.net/images/security/infrastructure_as_code/iac_misconfiguration_side_panel.200a8d4d9d125d03ab371fbe4d1d3704.png?auto=format"
   alt="IaC misconfiguration side panel showing details for the high severity IMDSv1 Enabled issue, including a security summary, code snippet, detection timestamps, and remediation steps." /%}

## How it works{% #how-it-works %}

IaC Security integrates with your repositories to continuously scan for misconfigurations. It analyzes every commit across all branches and performs a full daily scan of each configured repository. When violations are detected, findings are surfaced and linked to the relevant repository, branch, and file path. This helps you identify, prioritize, and fix misconfigurations directly at the source.

## Key capabilities{% #key-capabilities %}

### Review and fix violations in pull requests{% #review-and-fix-violations-in-pull-requests %}

When a pull request includes infrastructure-as-code changes, Datadog adds inline comments to flag any violations. Where applicable, it also suggests code fixes that can be applied directly in the pull request. You can also open a new pull request from Datadog to remediate a finding. For more information, see [Pull Request Comments](https://docs.datadoghq.com/security/code_security/dev_tool_int/github_pull_requests/).

### Automatically block risky changes with PR Gates{% #automatically-block-risky-changes-with-pr-gates %}

Use [PR Gates](https://docs.datadoghq.com/pr_gates/) to enforce security standards on infrastructure-as-code changes before they're merged. Datadog scans the IaC changes in each pull request, identifies any vulnerabilities above your configured severity threshold, and reports a pass or fail status to GitHub or Azure DevOps.

By default, checks are informational, but you can make them blocking in GitHub or Azure DevOps to prevent merging when critical issues are detected. For setup instructions, see [Set up PR Gate Rules](https://docs.datadoghq.com/pr_gates/setup).

### View and filter findings{% #view-and-filter-findings %}

After setting up IaC Security, each commit to a scanned repository triggers a scan. Findings are summarized on the [Code Security Vulnerabilities](https://app.datadoghq.com/security/code-security/iac) page and grouped per repository on the [Code Security Repositories](https://app.datadoghq.com/ci/code-analysis?) page.

Use filters to narrow results by:

- Severity
- Status (open, muted, fixed)
- Resource type
- Cloud provider
- File path
- Team
- Repository

Click any finding to open a side panel that shows:

- **Details**: A description and the relevant code that triggered the finding. (To view code snippets, [install the GitHub App](https://app.datadoghq.com/integrations/github/).)
- **Remediation**: If available, suggested code fixes are provided for findings that support remediation.

### Create Jira tickets from findings{% #create-jira-tickets-from-findings %}

You can create a bidirectional Jira ticket directly from any finding to track and remediate issues in your existing workflows. Ticket status remains synced between Datadog and Jira. For more information, see [Bidirectional ticket syncing with Jira](https://docs.datadoghq.com/security/ticketing_integrations#bidirectional-ticket-syncing-with-jira).

### Mute findings{% #mute-findings %}

To suppress a finding, click **Mute** in the finding details panel. This opens a workflow where you can [create a Muting Rule](https://docs.datadoghq.com/security/automation_pipelines/) for context-aware filtering by tag values (for example, by `service` or `environment`). Muting a finding hides it and excludes it from reports.

To restore a muted finding, click **Unmute** in the details panel. You can also use the **Status** filter on the [Code Security Vulnerabilities](https://app.datadoghq.com/security/code-security/iac) page to review muted findings.

### Exclude specific rules, files, or resources{% #exclude-specific-rules-files-or-resources %}

You can configure exclusions to prevent certain findings from appearing in scan results. Exclusions can be based on rule ID, file path, resource type, severity, or tag.

Exclusions are managed through a configuration file or inline comments in your IaC code. For supported formats and usage examples, see [Configure IaC Security Exclusions](https://docs.datadoghq.com/security/code_security/iac_security/exclusions/?tab=yaml).

## Next steps{% #next-steps %}

1. [Set up IaC Security](https://docs.datadoghq.com/security/code_security/iac_security/setup) in your environment.
1. Configure [scanning exclusions](https://docs.datadoghq.com/security/code_security/iac_security/exclusions) to reduce false positives or ignore expected results.
1. Review and triage findings on the [Code Security Vulnerabilities](https://app.datadoghq.com/security/code-security/iac) page.

## Further reading{% #further-reading %}

- [Prevent cloud misconfigurations from reaching production with Datadog IaC Security](https://www.datadoghq.com/blog/datadog-iac-security/)
- [Set up IaC Security](https://docs.datadoghq.com/security/code_security/iac_security/setup)
- [Configure IaC Security Exclusions](https://docs.datadoghq.com/security/code_security/iac_security/exclusions)
- [IaC Security Rules](https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/)
- [PR Gates](https://docs.datadoghq.com/pr_gates/)
- [Detect and block exposed credentials with Datadog Secret Scanning](https://www.datadoghq.com/blog/code-security-secret-scanning)

# Source: https://docs.datadoghq.com/bits_ai/bits_ai_dev_agent.md

---
title: Bits AI Dev Agent
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Bits AI > Bits AI Dev Agent
source_url: https://docs.datadoghq.com/bits_ai_dev_agent/index.html
---

# Bits AI Dev Agent

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

{% callout %}
##### Join the Preview!

Bits AI Dev Agent is in Preview. To sign up, click **Request Access** and complete the form.

[Request Access](http://datadoghq.com/product-preview/bits-ai-dev-agent)
{% /callout %}

## Overview{% #overview %}

{% image
   source="https://datadog-docs.imgix.net/images/bits_ai/dev_agent/error_tracking_assistant.e174296b715eaaf2911d42f6ab3be580.png?auto=format"
   alt="Bits AI Dev Agent suggesting a fix for an IndexError in a Django app" /%}

Bits AI Dev Agent is a generative AI coding assistant that uses observability data from Datadog to automatically diagnose and fix issues in your code. It integrates with GitHub to create production-ready pull requests, iterates on fixes using CI logs and developer feedback, and draws on multiple Datadog products to generate contextual fixes.

## Supported Datadog products{% #supported-datadog-products %}

Bits AI Dev Agent is available for the following Datadog products:

| Product                                                              | Availability | Capabilities                                                                                                              |
| -------------------------------------------------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------- |
| [Error Tracking](https://docs.datadoghq.com/error_tracking)          | Preview      | Diagnoses issues and generates code fixes on-demand or autonomously                                                       |
| [Trace Explorer](https://docs.datadoghq.com/tracing/trace_explorer/) | Preview      | Analyzes traces and provides remediations for errors and latency bottlenecks                                              |
| [Code Security](https://docs.datadoghq.com/security/code_security)   | Preview      | Remediates code vulnerabilities individually or in bulk                                                                   |
| [Test Optimization](https://docs.datadoghq.com/tests/)               | Preview      | Provides code fixes for flaky tests and verifies that tests remain stable                                                 |
| [Continuous Profiler](https://docs.datadoghq.com/profiler/)          | Preview      | Provides code changes for [Automated Analysis](https://docs.datadoghq.com/profiler/automated_analysis/) insights          |
| [Containers](https://docs.datadoghq.com/containers/)                 | Preview      | Provides code changes for [Kubernetes Remediations](https://docs.datadoghq.com/containers/bits_ai_kubernetes_remediation) |

**Note**: Enabling Bits AI Dev Agent is product-specific. Even if it's active for one Datadog product, it must be separately enabled for each additional product you use.

## Key capabilities{% #key-capabilities %}

The following sections detail how Bits AI Dev Agent integrates with Datadog products to generate contextual code fixes.

### Pull request assistance{% #pull-request-assistance %}

Bits AI Dev Agent integrates with GitHub to create pull requests, respond to comments, update commits, and fix CI failures.

- Generates PR titles and descriptions based on your PR template.

- Opens PRs as drafts, iterates using CI logs, and marks the PRs as ready for review when checks pass.

- Continues iterating in response to chat messages and review feedback.

**Note**: Comment `@Datadog` to prompt Bits for updates to the PR. Bits Dev never auto-merges PRs.

Go to **Bits AI** > **Dev Agent** > **[Code sessions](https://app.datadoghq.com/code?tab=my-sessions)** to see all Dev Agent code sessions and generated PRs. You can search sessions and filter by service, product source, and status.

### Auto-push{% #auto-push %}

Auto-push allows the Dev Agent to create branches, push code, and open PRs when it detects something it can help you with. For example, the Dev Agent can:

- Auto-create PRs for high-impact errors (such as 500s or crashes).
- Update PRs in response to your comments in GitHub.
- Update PRs to address CI failures.

Auto-push only opens PRs and pushes changes; it never merges code. When auto-push is disabled, you must review code in Datadog before it gets pushed.

Auto-push is available for Error Tracking and Test Optimization.

#### Security considerations{% #security-considerations %}

Allowing any AI-based tool to read untrusted data can let attackers trick it into outputting malicious code or other output. In some environments, an attacker could craft errors, traces, or other telemetry containing malicious payloads that the Dev Agent reads. Datadog runs security scanning on the output of the Dev Agent, but it is not foolproof.

### Error tracking{% #error-tracking %}

In [Error Tracking](https://docs.datadoghq.com/error_tracking), Bits AI Dev Agent diagnoses and remediates code issues with context and unit-tested fixes:

- Determines whether an error can be fixed through code and generates a fix with unit tests.
- Provides links within the chat to relevant files and methods for streamlined navigation.
- Analyzes errors asynchronously as they arrive.
- Marks errors with a **Fix available** status and enables filtering to surface those issues.

Auto-push is available for this feature.

### Flaky test management{% #flaky-test-management %}

Bits AI Dev Agent fixes flaky tests that are detected through Flaky Test Management in [Test Optimization](https://docs.datadoghq.com/tests/) and attempts to verify that tests remain stable.

Auto-push is available for this feature.

### Trace investigation{% #trace-investigation %}

Bits AI Dev Agent debugs errors and latency directly from [traces](https://docs.datadoghq.com/tracing/trace_explorer/) using natural language queries:

- Analyzes and summarizes large traces.
- Determines likely root causes for errors and latency.
- Generates code fixes when prompted.

### Product recommendations{% #product-recommendations %}

Bits AI Dev Agent applies automated code changes based on Datadog insights such as CCM Recommendations, APM Recommendations, and Profiling Insights.

### Code security{% #code-security %}

Bits AI Dev Agent remediates vulnerabilities at scale, from single issues to large backlogs. You can:

- Create PR batches to fix multiple vulnerabilities at once.
- Use the Campaign tool to push PRs incrementally and manage review workload across teams.

## Get started{% #get-started %}

To enable Bits AI Dev Agent, see [Setup](https://docs.datadoghq.com/bits_ai/bits_ai_dev_agent/setup/).

## Limitations{% #limitations %}

- Bits Dev is an AI product, which means it can make mistakes. Use best practices when reviewing and testing agent-generated code.
- Bits AI Dev Agent does not support multi-repository investigations.

## Further reading{% #further-reading %}

- [Automatically identify issues and generate fixes with the Bits AI Dev Agent](https://www.datadoghq.com/blog/bits-ai-dev-agent/)

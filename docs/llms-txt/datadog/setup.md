# Source: https://docs.datadoghq.com/deployment_gates/setup.md

# Source: https://docs.datadoghq.com/security/workload_protection/setup.md

# Source: https://docs.datadoghq.com/security/sensitive_data_scanner/setup.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/setup.md

# Source: https://docs.datadoghq.com/security/code_security/iast/setup.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/setup.md

# Source: https://docs.datadoghq.com/security/cloud_security_management/setup.md

# Source: https://docs.datadoghq.com/security/application_security/setup/go/setup.md

# Source: https://docs.datadoghq.com/security/application_security/setup.md

# Source: https://docs.datadoghq.com/data_streams/setup.md

# Source: https://docs.datadoghq.com/dora_metrics/setup.md

# Source: https://docs.datadoghq.com/containers/cluster_agent/setup.md

# Source: https://docs.datadoghq.com/code_coverage/setup.md

# Source: https://docs.datadoghq.com/cloud_cost_management/setup.md

# Source: https://docs.datadoghq.com/bits_ai/bits_ai_dev_agent/setup.md

# Source: https://docs.datadoghq.com/agentic_onboarding/setup.md

---
title: Agentic Onboarding Setup
description: >-
  Set up the Datadog MCP server to instrument your frontend applications with
  coding agents like Cursor or Claude Code.
breadcrumbs: Docs > Agentic Onboarding Setup
---

# Agentic Onboarding Setup

{% callout %}
##### Join the Preview!

Agentic Onboarding is in Preview.
{% /callout %}

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com



{% alert level="danger" %}
Agentic Onboarding is not available in the selected site () at this time.
{% /alert %}


{% /callout %}

## Overview{% #overview %}

Agentic Onboarding lets LLM coding agents instrument your frontend applications for [Error Tracking](https://docs.datadoghq.com/error_tracking/frontend/), [Real User Monitoring (RUM)](https://docs.datadoghq.com/real_user_monitoring/), and [Product Analytics](https://docs.datadoghq.com/product_analytics/) with a single prompt.

Your coding assistant, such as [Cursor](https://cursor.com/) or [Claude Code](https://claude.ai/), detects your project's frameworks, adds configuration, and provisions required tokens and apps directly from your IDE.

## Supported frameworks{% #supported-frameworks %}

Agentic Onboarding is available for the following frameworks: Android, Angular, iOS, Next.js, React, Svelte, Vanilla JS, and Vue.

## Setup{% #setup %}

### Install the Datadog Onboarding MCP server{% #install-the-datadog-onboarding-mcp-server %}

To install the Datadog Onboarding Model Context Protocol (MCP) server, follow the steps for your coding assistant:

{% tab title="Claude Code" %}

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com



{% alert level="danger" %}
Agentic Onboarding is not available in the selected site () at this time.
{% /alert %}


{% /callout %}

{% callout %}
# Important note for users on the following Datadog sites: app.datadoghq.com, us3.datadoghq.com, us5.datadoghq.com, app.datadoghq.eu, ap1.datadoghq.com, ap2.datadoghq.com



1. Open an active Claude Code session with the /mcp command:

   ```
   
   claude mcp add --transport http datadog-onboarding- "https://mcp./api/unstable/mcp-server/mcp?toolsets=onboarding"
   ```

1. Select the MCP server installed in Step 1. You should see a `disconnected - Enter to login` message. Press `Enter`.

1. When you see the option to authenticate, press `Enter`. This brings you to the OAuth screen.

1. After authentication, choose **Open** to continue and grant access to your Datadog account.

1. Confirm that MCP tools appear under the **datadog-onboarding-** server.


{% /callout %}

{% /tab %}

{% tab title="Cursor" %}

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com



{% alert level="danger" %}
Agentic Onboarding is not available in the selected site () at this time.
{% /alert %}


{% /callout %}

{% callout %}
# Important note for users on the following Datadog sites: app.datadoghq.com, us3.datadoghq.com, us5.datadoghq.com, app.datadoghq.eu, ap1.datadoghq.com, ap2.datadoghq.com



1. Copy and paste the following deeplink into your browser:

   ```
   
   
   ```

1. In Cursor, click **Install** for the **datadog-onboarding-** server.

1. If the MCP server shows a **Needs login** or **Connect** link, select it and complete the OAuth flow. When prompted, choose **Open** to continue and grant access to your Datadog account.

1. After authentication, return to Cursor and confirm that MCP tools appear under the **datadog-onboarding-** server.


{% /callout %}

{% /tab %}

### Set up your project{% #set-up-your-project %}

Your AI coding agent can help configure Datadog for your project. When you provide a setup prompt, the agent:

- Analyzes your project and identifies the framework, language, and bundler
- Calls the MCP tool and requests permission before running
- Applies the configuration changes specified by the tool
- Provides steps to verify that your application is sending telemetry to Datadog

**Note**: Your coding agent makes changes locally but does not commit them.

To get started:

1. Choose the product you want to use and paste its setup prompt into your AI agent:

   {% tab title="Error Tracking" %}

   ```console
   Add Datadog Error Tracking to my project
   ```

   {% /tab %}

   {% tab title="Real User Monitoring" %}

   ```console
   Add Datadog Real User Monitoring to my project
   ```

   {% /tab %}

   {% tab title="Product Analytics" %}

   ```console
   Add Datadog Product Analytics to my project
   ```

   {% /tab %}

1. Review and accept each action your AI agent proposes to complete the setup process.

### Deploy your app to production{% #deploy-your-app-to-production %}

Commit the changes to your repository and configure the provided environment variables in your production environment.

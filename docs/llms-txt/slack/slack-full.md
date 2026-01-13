# Slack Platform

> Slack Platform is a comprehensive set of tools, APIs, and SDKs that enables developers to build applications and integrations with Slack.

The Slack Platform helps developers build apps that extend the functionality of Slack, integrate with external services, and create custom workflows that improve team productivity and collaboration.

## Core Platform

This section covers fundamental documentation about the Slack Platform and its AI capabilities, providing the essential knowledge for getting started with Slack development.

- [Slack Platform overview](https://docs.slack.dev): the primary hub for all Slack development resources, API references, and guides.
- [Slack Platform quickstart](https://docs.slack.dev/quickstart): a beginner-friendly introduction to building your first Slack app.
- [Slack Platform FAQ](https://docs.slack.dev/faq): answers to the most common questions about Slack Platform. 
- [Slack Web API overview](https://docs.slack.dev/apis/web-api): the HTTP-based API that allows you to build apps that interact with Slack workspaces, read data, and perform actions programmatically.
- [Slack Events API overview](https://docs.slack.dev/apis/events-api): documentation for receiving and processing real-time events from Slack, such as messages, channel changes, and user activities.

## Slack CLI

The Slack Command Line Interface (CLI) provides the fastest and most efficient way to build Slack apps. With the Slack CLI you can scaffold a new project, configure your app, and start developing immediately.

The `slack create` command generates a fully-functional app template in JavaScript, Python, or TypeScript, complete with proper project structure and configuration files. This eliminates setup time and starts you off with a project following best practices.

- [Slack CLI overview](/tools/slack-cli/): complete documentation for the Slack CLI tool.
- [Installing the Slack CLI](/tools/slack-cli/guides/installing-the-slack-cli-for-mac-and-linux): step-by-step installation instructions for various platforms.
- [Running Slack CLI commands](/tools/slack-cli/guides/running-slack-cli-commands): guide to the various commands available in the Slack CLI.
- [Creating Bolt apps with the Slack CLI](/tools/slack-cli/guides/using-slack-cli-with-bolt-frameworks): use the Slack CLI to quickly set up and run Slack apps built with the Bolt Framework (currently supports JavaScript and Python)
- [Using environment variables with the Slack CLI](/tools/slack-cli/guides/using-environment-variables-with-the-slack-cli): how to manage configuration through environment variables.

## JavaScript development

Below are resources specifically for JavaScript developers looking to build Slack apps using the Bolt framework, the recommended approach for JavaScript-based Slack app development.

- [Bolt for JavaScript overview](/tools/bolt-js/): complete documentation for the Bolt JavaScript framework.
- [Getting started with Bolt for JavaScript](/tools/bolt-js/getting-started): a step-by-step guide to building your first JavaScript Slack app.
- [Bolt for JavaScript AI apps](/tools/bolt-js/concepts/ai-apps): a specialized guide for developing AI-powered apps with JavaScript.
- [Bolt for JavaScript code assistant tutorial](/tools/bolt-js/tutorials/code-assistant): learn to build an AI code assistant using Bolt and Hugging Face.

## Python development

Below are resources for Python developers using the Bolt framework, providing the tools and knowledge needed to build robust Slack apps with Python.

- [Bolt for Python framework overview](/tools/bolt-python/): complete documentation for the Bolt for Python framework.
- [Bolt for Python framework getting started](/tools/bolt-python/getting-started): a step-by-step guide to building your first Python Slack app.
- [Bolt for Python framework AI apps](/tools/bolt-python/concepts/ai-apps): a specialized guide for developing AI-powered apps with Python.
- [Bolt for Python framework AI chatbot tutorial](/tools/bolt-python/tutorial/ai-chatbot): a detailed tutorial for building an AI chatbot in Slack using Python.

## TypeScript development with Deno

Resources for developers building workflow-based Slack apps with Deno, a modern runtime for TypeScript with enhanced security features.

- [Deno Slack SDK overview](/tools/deno-slack-sdk/): complete documentation for the Deno Slack SDK.
- [Deno Slack SDK getting started](/tools/deno-slack-sdk/guides/getting-started): learn how to build Slack apps using the Deno runtime.
- [Deno Slack SDK creating functions](/tools/deno-slack-sdk/guides/creating-functions): a guide to creating serverless functions with the Deno Slack SDK.
- [Deno Slack SDK Following Security Best Practices](/tools/deno-slack-sdk/guides/following-security-best-practices): security guidelines for Deno Slack SDK development.

## Sending messages with Incoming webhooks

This section provides a guide for sending messages to Slack using incoming webhooks, an efficient way to post messages from external sources.

Incoming webhooks provide a straightforward method to send messages to Slack from any application that can make HTTP requests, without requiring full Slack API authentication.

### Step-by-step guide:

1. Create a webhook URL:
   - Go to your [Slack App configuration page](https://api.slack.com/apps)
   - Create a new app or select an existing one
   - Navigate to "Incoming Webhooks" and activate the feature
   - Click "Add New Webhook to Workspace" and select the channel to post to
   - Copy the generated webhook URL

2. Send a basic message:
   ```bash
   curl -X POST -H 'Content-type: application/json' --data '{"text":"Hello, Slack!"}' YOUR_WEBHOOK_URL
   ```

3. Send a message with advanced formatting:
   ```json
   {
     "text": "New support ticket received",
     "blocks": [
       {
         "type": "section",
         "text": {
           "type": "mrkdwn",
           "text": "*Ticket #1234*\nCustomer reported an issue with login"
         }
       },
       {
         "type": "actions",
         "elements": [
           {
             "type": "button",
             "text": {
               "type": "plain_text",
               "text": "View Ticket"
             },
             "url": "https://example.com/tickets/1234"
           }
         ]
       }
     ]
   }
   ```

- [Sending messages using incoming webhooks](https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks): complete documentation on incoming webhooks.
- [Creating interactive messages](https://docs.slack.dev/messaging/creating-interactive-messages): how to add buttons and other interactive elements to messages.
- [Block Kit](https://docs.slack.dev/block-kit): documentation for Slack's UI framework for building rich message layouts.

## Managing app approvals in Slack

This section explains how administrators can control which apps can be installed in their Slack workspace, crucial for maintaining security and compliance.

The app approval system allows organizations to review and govern which third-party applications can access Slack workspace data and interact with users, providing necessary oversight for enterprise environments.

### App approval workflow guide:

1. Configure approval settings:
   - Access the Slack Admin Console (admin.slack.com)
   - Navigate to "Settings & Permissions" → "App Management"
   - Choose between "All apps require approval" or "Only restricted apps require approval"

2. Set up automation rules (recommended):
   - In the Admin Console, go to "App Management" → "Approval Automations"
   - Create rules based on app characteristics (e.g., publisher, permissions requested)
   - Example rule: Auto-approve apps from verified publishers requesting only channel:read scope

3. Process app requests:
   - When a user attempts to add an unapproved app, they'll submit a request
   - Admins receive notifications about pending requests
   - Review app details, requested scopes, and security information
   - Approve or deny with optional explanatory message

4. Monitor app usage:
   - Regularly audit installed apps via "App Management" dashboard
   - Review app permissions and user adoption metrics
   - Revoke access for problematic or unused applications

- [Manage app approval for your workspace](https://slack.com/help/articles/222386767-Manage-app-approval-for-your-workspace): complete guide to setting up and managing app approvals.
- [Configure automations for app approval](https://slack.com/help/articles/9487088123411-Configure-automations-for-app-approval): how to set up automated rules for app approvals.
- [Guide to automation rules for app approval](https://slack.com/help/articles/9978438318227-Guide-to-automation-rules-for-app-approval): best practices for creating effective approval automation rules.
- [Manage app requests for your workspace](https://slack.com/help/articles/360024269514-Manage-app-requests-for-your-workspace): how to handle incoming app installation requests from users.

## Enterprise administration

Below are resources for administrators managing Slack at an enterprise level, covering advanced administration topics for large organizations.

- [Set up and manage Agentforce in Slack](https://slack.com/help/articles/36218109305875-Set-up-and-manage-Agentforce-in-Slack): guide to configuring Agentforce in Slack.
- [5 steps to managing apps securely and at scale](https://slack.com/resources/slack-for-admins/app-management): best practices for app governance in large organizations.
- [Manage apps in an Enterprise org](https://slack.com/help/articles/360000281563-Manage-apps-in-an-Enterprise-organization): specialized guidance for managing apps across multiple workspaces in an Enterprise organization.
- [Set organization policies for apps in an Enterprise org](https://slack.com/help/articles/360038559694-Set-organization-level-policies-for-apps): how to create and enforce organization-wide app policies.

## Authentication & security

Below are essential docs for implementing secure authentication and following best practices for Slack app security.

- [Slack authentication](https://docs.slack.dev/authentication): comprehensive guide to authentication methods for Slack apps.
- [Following security best practices](/tools/deno-slack-sdk/guides/following-security-best-practices): security guidelines to protect your Slack app and its users.
- [Authenticating OAuth](/tools/bolt-js/concepts/authenticating-oauth): implementing the OAuth flow for Slack apps.
- [Token rotation](https://docs.slack.dev/authentication/using-token-rotation): maintaining secure authentication by implementing token rotation.

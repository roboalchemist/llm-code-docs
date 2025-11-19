# Source: https://docs.hypermode.com/agents/connections.md

# Connections

> All the capabilities your agent needs to take action across your stack

**Connections** enable Hypermode Agents to securely access and interact with
external tools, APIs, and services. With over 2,000 available integrations,
agents can execute tasks across your entire technology stack.

## Overview

A Connection is a secure link between your agent and an external service (for
example GitHub, Slack, Stripe, or your internal APIs). Connections allow agents
to perform actions, retrieve data, and automate flows using these services.

* **2,000+ integrations** to connect to popular tools across development,
  analytics, productivity, marketing, finance, and more.
* **Role-based access control** limits agent access to only the necessary tools
  and permissions
* **Audit logging** tracks all agent interactions with external services for
  compliance and troubleshooting
* **Powered by Model Context Protocol** for secure, structured, and
  context-aware tool interactions
* **Custom API support** with encrypted credentials and scoped access

## Getting started

### Add a connection

Open the information details of your agent. Select "Add connection" and search
from more than 2,000 connection options.

<img src="https://mintcdn.com/hypermode/Bu7AIG01ktGbhJIf/images/agents/connections-sidebar.png?fit=max&auto=format&n=Bu7AIG01ktGbhJIf&q=85&s=bce82a1d2959eac949f4a446bee22185" alt="Add a new connection" width="1990" height="766" data-path="images/agents/connections-sidebar.png" srcset="https://mintcdn.com/hypermode/Bu7AIG01ktGbhJIf/images/agents/connections-sidebar.png?w=280&fit=max&auto=format&n=Bu7AIG01ktGbhJIf&q=85&s=ceaa1e9f62f602cd637718dd692eba00 280w, https://mintcdn.com/hypermode/Bu7AIG01ktGbhJIf/images/agents/connections-sidebar.png?w=560&fit=max&auto=format&n=Bu7AIG01ktGbhJIf&q=85&s=de28d73674505e251a31c97c492a5f67 560w, https://mintcdn.com/hypermode/Bu7AIG01ktGbhJIf/images/agents/connections-sidebar.png?w=840&fit=max&auto=format&n=Bu7AIG01ktGbhJIf&q=85&s=8d33b06f8f5a8bf556e3d6edfc3253f7 840w, https://mintcdn.com/hypermode/Bu7AIG01ktGbhJIf/images/agents/connections-sidebar.png?w=1100&fit=max&auto=format&n=Bu7AIG01ktGbhJIf&q=85&s=faf9e599d96d1daf8ce7d6370414cd81 1100w, https://mintcdn.com/hypermode/Bu7AIG01ktGbhJIf/images/agents/connections-sidebar.png?w=1650&fit=max&auto=format&n=Bu7AIG01ktGbhJIf&q=85&s=81392cb13f31468f2477d8a3d4511875 1650w, https://mintcdn.com/hypermode/Bu7AIG01ktGbhJIf/images/agents/connections-sidebar.png?w=2500&fit=max&auto=format&n=Bu7AIG01ktGbhJIf&q=85&s=ae6c6929a8de21066d1e90cf965f7c68 2500w" data-optimize="true" data-opv="2" />

### Authenticate

You'll be prompted to complete the OAuth flow if you haven't enabled the
connection yet for your workspace.

Once authenticated, save the changes made to the agent.

<Note>
  All connections use secure authentication methods including OAuth 2.0, API
  keys, and service account credentials. Credentials are encrypted and never
  exposed to the agent's reasoning process.
</Note>

### Manage connections

Existing connections can be viewed and managed from the "Connections" tab in the
Workspace settings page. Connections can also be added to your workspace from
this page.

<img src="https://mintcdn.com/hypermode/Bu7AIG01ktGbhJIf/images/agents/connections-manage.png?fit=max&auto=format&n=Bu7AIG01ktGbhJIf&q=85&s=3a3505437e387232f1de1eca6122f3ae" alt="Manage connections" width="2572" height="1020" data-path="images/agents/connections-manage.png" srcset="https://mintcdn.com/hypermode/Bu7AIG01ktGbhJIf/images/agents/connections-manage.png?w=280&fit=max&auto=format&n=Bu7AIG01ktGbhJIf&q=85&s=482281b2dbafc51f7120d559efc2cc91 280w, https://mintcdn.com/hypermode/Bu7AIG01ktGbhJIf/images/agents/connections-manage.png?w=560&fit=max&auto=format&n=Bu7AIG01ktGbhJIf&q=85&s=66ae48f1052f6fa3f5589173fae93bed 560w, https://mintcdn.com/hypermode/Bu7AIG01ktGbhJIf/images/agents/connections-manage.png?w=840&fit=max&auto=format&n=Bu7AIG01ktGbhJIf&q=85&s=e70bf6c755a3a2d0cfeb63e512593aae 840w, https://mintcdn.com/hypermode/Bu7AIG01ktGbhJIf/images/agents/connections-manage.png?w=1100&fit=max&auto=format&n=Bu7AIG01ktGbhJIf&q=85&s=9d8f4aac8cc5865cb156105c1a205002 1100w, https://mintcdn.com/hypermode/Bu7AIG01ktGbhJIf/images/agents/connections-manage.png?w=1650&fit=max&auto=format&n=Bu7AIG01ktGbhJIf&q=85&s=20dd5055918aded0f46f934492147382 1650w, https://mintcdn.com/hypermode/Bu7AIG01ktGbhJIf/images/agents/connections-manage.png?w=2500&fit=max&auto=format&n=Bu7AIG01ktGbhJIf&q=85&s=fef4c23dcb54a178701d3161efb58f48 2500w" data-optimize="true" data-opv="2" />

### Edit or remove connections

Update credentials, change permissions, or remove connections at any time form
the "Connections" tab in your agent information card or in the Workspace
settings page.

<Tip>
  Start with a small set of essential tools for your agent's role, then expand
  as you identify additional needs through usage patterns.
</Tip>

## FAQs

**Why is there a "token not found" or "failed to get connection token" error?**

This error usually means the connection’s credentials are missing, expired, or
weren't saved correctly. Please re-authenticate the connection in Workspace
Settings > Connections. If the issue persists, ensure you have completed the
OAuth flow and granted all required permissions.

**The agent can't access repositories, calendar, or Notion pages even though the
service is connected?**

Double-check that you completed the OAuth authorization and selected the correct
account or workspace. Some services require you to explicitly grant access to
specific resources (for example repositories, calendars, pages). You can update
these permissions in your service’s settings or by reconnecting the integration.

**Is there a way to add or manage connections directly from the agent setup
flow?**

Yes. You can add new connections during agent creation. Look for the “Add
Connection” tab in your agent card once the agent is created.

**Can one connection power multiple agents?**

Yes. Connections are created at the Workspace level and can be assigned to
multiple agents. You can grant access to the same connection for any agents that
need it.

**Can we connect to a service not listed in the catalog?**

Custom integrations can be built for internal APIs and proprietary systems.
Contact us for assistance with custom connection development.

**How do we restrict agent access to sensitive data?**

Hypermode uses OAuth to connect to external services, allowing you to grant only
the minimum required permissions (scopes) for each agent. Use role-based access
control and permission scoping when assigning connections to agents to ensure
they only access the data and actions necessary for their tasks.

**How do we know which permissions or scopes are being requested during OAuth?**

During the OAuth flow, you’ll see a list of permissions requested by Hypermode.
Only the minimum required scopes are requested for the tools you assign to your
agent. You can review and adjust these permissions in your service’s settings.

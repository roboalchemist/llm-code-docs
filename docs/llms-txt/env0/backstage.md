# Source: https://docs.envzero.com/guides/integrations/internal-developer-platforms/backstage.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Backstage Integration

> Set up the env zero Backstage plugin to manage IaC environments from your internal developer portal

[Backstage](https://backstage.io/) is an open platform that allows organizations to create internal developer portals. These portals centralize tools, documentation, and workflows, providing developers with a single interface to access the resources they need for their projects. By integrating env zero's Backstage plugin, teams can extend their developer portal to include IaC management.

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/1IphQfKpx9g" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

## About env zero's Backstage Plugin

The env zero Backstage plugin integrates env zero's Infrastructure as Code automation platform into Backstage. This enables administrators to configure templates and workflows that provide developers with self-service access to IaC environments while maintaining oversight and governance.

With this plugin

**Admins can:**

* **Configure Backstage templates** tailored to organizational needs and policies.
* **Enable developers** to create and manage environments via env zero.

**Developers can:**

* **Select the appropriate template** for the infrastructure they need and create new environments in env zero directly from Backstage.

<Frame caption="Creating an env zero environment using a Backstage form">
  <img src="https://mintcdn.com/envzero-b61043c8/OvzlPx-zFGXzf_QN/images/guides/integrations/internal-developer-platforms/468.png?fit=max&auto=format&n=OvzlPx-zFGXzf_QN&q=85&s=df0869f4699cfa24437b8e6636270ae3" alt="Backstage integration interface showing configuration options" width="1999" height="753" data-path="images/guides/integrations/internal-developer-platforms/468.png" />
</Frame>

* **Search for and view environments** within the Backstage catalog to efficiently find and manage resources.

<Frame caption="Viewing and managing env zero environments within the Backstage catalog">
  <img src="https://mintcdn.com/envzero-b61043c8/OvzlPx-zFGXzf_QN/images/guides/integrations/internal-developer-platforms/468.png?fit=max&auto=format&n=OvzlPx-zFGXzf_QN&q=85&s=df0869f4699cfa24437b8e6636270ae3" alt="Backstage integration interface showing configuration options" width="1999" height="753" data-path="images/guides/integrations/internal-developer-platforms/468.png" />
</Frame>

* **Access detailed environment views**, including deployment history and options to redeploy environments with updated variables.

<Frame caption="Environment details with status, drift information, and VCS data">
  <img src="https://mintcdn.com/envzero-b61043c8/OvzlPx-zFGXzf_QN/images/guides/integrations/internal-developer-platforms/468.png?fit=max&auto=format&n=OvzlPx-zFGXzf_QN&q=85&s=df0869f4699cfa24437b8e6636270ae3" alt="Backstage integration interface showing configuration options" width="1999" height="753" data-path="images/guides/integrations/internal-developer-platforms/468.png" />
</Frame>

<Frame caption="Overview of deployment history, including statuses and timestamps">
  <img src="https://mintcdn.com/envzero-b61043c8/OvzlPx-zFGXzf_QN/images/guides/integrations/internal-developer-platforms/468.png?fit=max&auto=format&n=OvzlPx-zFGXzf_QN&q=85&s=df0869f4699cfa24437b8e6636270ae3" alt="Backstage integration interface showing configuration options" width="1999" height="753" data-path="images/guides/integrations/internal-developer-platforms/468.png" />
</Frame>

<Frame caption="Redeployment with updated variables in the env zero tab">
  <img src="https://mintcdn.com/envzero-b61043c8/OvzlPx-zFGXzf_QN/images/guides/integrations/internal-developer-platforms/468.png?fit=max&auto=format&n=OvzlPx-zFGXzf_QN&q=85&s=df0869f4699cfa24437b8e6636270ae3" alt="Backstage integration interface showing configuration options" width="1999" height="753" data-path="images/guides/integrations/internal-developer-platforms/468.png" />
</Frame>

## Getting Started

* **Install the Plugin**: Visit the [env zero Backstage Plugin repository on GitHub](https://github.com/env0/env0-backstage-plugin) and follow the installation instructions.
* **Configure the Plugin**: Link env zero to Backstage using your organization's [API key](/guides/admin-guide/user-role-and-team-management/api-keys), and set up templates with variables, approval workflows, and policies.

For additional information, advanced configurations, and troubleshooting, refer to the documentation available in the [GitHub repository](https://github.com/env0/env0-backstage-plugin).

Built with [Mintlify](https://mintlify.com).

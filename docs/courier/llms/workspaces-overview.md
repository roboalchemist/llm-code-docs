# Source: https://www.courier.com/docs/platform/workspaces/workspaces-overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Workspace Overview

> Your Courier workspace isolates environments, API keys, templates, team access, and settings. Learn the core concepts and how to configure your workspace.

A workspace is the top-level container for everything in Courier. Each workspace has its own environments, API keys, templates, integrations, user profiles, and analytics; nothing leaks between workspaces. Most teams use a single workspace. If you need to separate billing, data residency, or team access boundaries, you can create additional workspaces.

## Core Concepts

### Environments

Every workspace has two isolated environments: **Production** and **Test**. Each environment has its own templates, integrations, user profiles, API keys, and log data. Changes in one environment never affect the other until you explicitly migrate assets.

Use Test for development and QA; use Production for live traffic. You can switch environments from the settings menu in the lower-left corner of the dashboard. See [Environments, API Keys, and Assets](/platform/workspaces/environments-api-keys) for details on switching, migrating assets, and scoping keys.

### API Keys

Each environment has its own set of API keys scoped to specific permissions (published or draft access). You can create multiple keys per environment for different services or team members. Keep Production keys out of client-side code; use Test keys during development. See [Environments, API Keys, and Assets](/platform/workspaces/environments-api-keys) for key management and permission scoping.

### Team Access

Courier supports four roles: **Administrator** (full access), **Editor** (create and edit templates), **Viewer** (read-only), and **Developer** (API access only). Assign the narrowest role each team member needs. See [Roles & Permissions](/platform/workspaces/roles-permissions) for a full breakdown of what each role can do.

### Security

Require Google SSO or [Okta SSO](/platform/workspaces/okta-integration) to control how team members authenticate. Make your workspace discoverable so colleagues with matching email domains can request access, or lock it down so members must be added manually. See [Team Security](/platform/workspaces/team-security) for setup steps.

***

## Configuration

You can manage workspace-level settings from [Settings > General](https://app.courier.com/settings/general), including tracking, tenant behavior, and webhooks.

<Frame caption="Workspace General Settings">
  <img src="https://mintcdn.com/courier-4f1f25dc/sVfvclV8cUQ_BbRz/assets/platform/workspaces/workspace-general-settings.png?fit=max&auto=format&n=sVfvclV8cUQ_BbRz&q=85&s=1c642dfda18a94d96df920b0b8355b8f" alt="Workspace General Settings page showing tracking toggles, tenant settings, and webhooks" width="3452" height="1992" data-path="assets/platform/workspaces/workspace-general-settings.png" />
</Frame>

### Email Open and Click Tracking

You can enable open and click tracking for email notifications in [Settings > General](https://app.courier.com/settings/general). This applies to your Production environment.

Some providers require additional configuration on their end:

* **SendGrid**: Enable [Tracking Settings](https://sendgrid.com/docs/ui/account-and-settings/tracking/) in your SendGrid dashboard
* **Mailgun**: Enable [Tracking Messages](https://documentation.mailgun.com/en/latest/user_manual.html#tracking-messages) in Mailgun

If you have tracking enabled globally, you can disable it on individual links. In the template designer, open the action block settings or the hyperlink settings for a text block and toggle tracking off for that link.

### Outbound Webhooks

Subscribe to webhook events (sent, delivered, opened, clicked, undeliverable, and more) to push notification lifecycle data into your own systems. See [Outbound Webhooks](/platform/workspaces/outbound-webhooks) for event types, payload format, and setup.

### EU Data Residency

If you need to keep data within the EU, Courier offers a dedicated EU datacenter. See [EU Datacenter](/platform/workspaces/eu-datacenter) for migration steps and endpoint configuration.

***

## Common Patterns

**Single workspace (most teams)**: One workspace with Production and Test environments covers the majority of use cases. Use roles and API key scoping to control access.

**Separate workspaces per product**: If you ship multiple products with different notification stacks, separate workspaces keep templates, integrations, and analytics cleanly isolated.

**Separate workspaces for data residency**: Use an EU workspace for customers who require EU data residency and a US workspace for everyone else.

***

## FAQ

<AccordionGroup>
  <Accordion title="Can I move templates between workspaces?">
    Yes. Export a template from one workspace and import it into another. Within a single workspace, you can migrate templates between Production and Test environments. See [Environments, API Keys, and Assets](/platform/workspaces/environments-api-keys) for details.
  </Accordion>

  <Accordion title="What happens if I switch from Production to Test?">
    Switching environments only changes your dashboard view. It does not affect live notifications or any data in either environment.
  </Accordion>

  <Accordion title="How do I enforce SSO for my team?">
    Go to Settings > Team and enable "Require Google SSO" for your approved domains, or set up [Okta SSO](/platform/workspaces/okta-integration) if you use Okta. Once enabled, all team members must authenticate through SSO.
  </Accordion>

  <Accordion title="Can I restrict API key permissions?">
    Yes. Each API key is scoped to a specific environment and permission level (published or draft). Create separate keys for different services so you can rotate or revoke them independently.
  </Accordion>
</AccordionGroup>

## Related Resources

<CardGroup cols={2}>
  <Card title="Environments & API Keys" href="/platform/workspaces/environments-api-keys" icon="key">
    Manage environments, keys, and asset migration
  </Card>

  <Card title="Roles & Permissions" href="/platform/workspaces/roles-permissions" icon="shield">
    Configure team access and role assignments
  </Card>

  <Card title="Outbound Webhooks" href="/platform/workspaces/outbound-webhooks" icon="webhook">
    Push notification events to your systems
  </Card>

  <Card title="EU Datacenter" href="/platform/workspaces/eu-datacenter" icon="globe">
    Set up EU data residency
  </Card>
</CardGroup>

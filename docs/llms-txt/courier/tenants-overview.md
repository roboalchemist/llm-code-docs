# Source: https://www.courier.com/docs/platform/tenants/tenants-overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Tenants Overview

> Tenants in Courier are hierarchical groups that manage user preferences, metadata, and branding. They support scoped notifications, default routing, custom branding, and can inherit settings from parent tenants.

## Overview

Tenants are hierarchical groups that map to organizations, teams, projects, or environments. They scope notifications with tenant-specific preferences, branding, and metadata.

### Why tenants matter

One workspace can serve many customers or orgs without duplicating templates. Each tenant gets its own defaults (preferences, branding, provider credentials), so the same flows adapt per context. Useful for B2B SaaS, white-label products, and scoped inboxes or preferences per customer or project.

## Key Features

Courier's tenant system provides comprehensive multi-tenant notification management with features including:

* **Hierarchical Organization** - Create parent-child tenant relationships with up to four layers of inheritance
* **Scoped Preferences** - Set tenant-specific default preferences that users can override on a per-tenant basis
* **Custom Branding** - Apply different brands and visual styling based on tenant context
* **Provider Credentials** - Store tenant-specific provider keys (Slack workspace tokens, custom SMTP credentials)
* **Flexible Targeting** - Send to individual users with tenant context, all tenant members, or nested hierarchies
* **Metadata Management** - Attach custom properties and profile data that templates can reference
* **Send Limits** - Configure maximum send limits per tenant for usage control

## Core Components

### [Hierarchical Organization](/platform/tenants/tenant-deepdive#hierarchical-inheritance)

Create parent-child tenant relationships with up to four layers of inheritance. Child tenants inherit and can override parent metadata, preferences, and branding.

Example mapping: `Companies` → `Teams` → `Projects` → `Environments`

### [Tenant Sending](/platform/tenants/sending-with-tenants)

Send notifications to entire tenant groups, individual users with tenant context, or leverage hierarchical relationships to target nested organizational structures.

### [Tenant Preferences](/platform/tenants/user-tenant-preferences)

Set tenant-specific default preferences that users can override on a per-tenant basis. Support layered preference systems where users have different notification settings per tenant.

### [Tenant Inboxes](/platform/tenants/inbox-with-tenants)

Create isolated notification experiences that respect organizational boundaries. Messages sent with tenant context only appear in tenant-configured inboxes.

## Next Steps

<CardGroup cols={2}>
  <Card title="Sending with Tenants" href="/platform/tenants/sending-with-tenants" icon="paper-plane">
    Send notifications with tenant context and targeting
  </Card>

  <Card title="Inbox with Tenants" href="/platform/tenants/inbox-with-tenants" icon="inbox">
    Configure tenant-specific inboxes and user experiences
  </Card>

  <Card title="User Tenant Preferences" href="/platform/tenants/user-tenant-preferences" icon="user-gear">
    Manage layered preference systems per tenant
  </Card>

  <Card title="Tenant Deep Dive" href="/platform/tenants/tenant-deepdive" icon="book">
    Comprehensive technical guide to tenant hierarchies and metadata
  </Card>

  <Card title="Tenants API Reference" href="/api-reference/tenants/get-a-tenant" icon="code">
    Complete API documentation for tenant management
  </Card>
</CardGroup>

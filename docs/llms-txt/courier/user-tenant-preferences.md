# Source: https://www.courier.com/docs/platform/tenants/user-tenant-preferences.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# User Tenant Preferences

> Courier allows users to manage notification preferences per tenant, supporting layered opt-in/out choices based on tenant-specific or inherited defaults.

## Overview

User tenant preferences enable user-driven notification control by allowing users to set different preference choices for each tenant they belong to. This creates a layered preference system where users can have fine-grained control over notifications across different organizational contexts.

For example, a user might want to receive production alerts for their main project but opt out of development notifications for staging environments, or receive different types of notifications for different teams or organizations.

<Note>
  **Availability**: User-Tenant Preferences are available for Enterprise customers. Contact [Courier Support](mailto:support@courier.com) for access or [Request a Demo](https://www.courier.com/request-demo) to learn more about how Courier could help you.
</Note>

## Key Features

Courier's tenant preference system provides:

* **Per-Tenant Preferences** - Users can set different preferences for each tenant relationship
* **Layered Defaults** - Preferences inherit from tenant defaults but can be overridden by users
* **Hierarchical Inheritance** - Parent tenant preferences flow down to child tenants
* **Flexible Opt-in/Out** - Users can opt in to some tenants while opting out of others
* **Context-Aware Delivery** - Notifications respect the preference context of the specific tenant

## Preference Hierarchy

Adding tenant context creates multiple layers of preferences for a single user. For example, if you design tenants to map to your organizational structure (cloud provider with multiple projects), a user can:

* Opt in to production notifications for `prod-project`
* Opt out of notifications for `stage-project`
* Receive different channel preferences for `team-alpha` vs `team-beta`

This granular control ensures users receive contextually appropriate notifications without being overwhelmed by irrelevant alerts from different organizational contexts.

## Tenant Defaults

If a user has not updated their own preferences for a tenant, they will use the defaults as provided by the tenant. Each tenant can have their own defaults, see more in [Default Preferences](/platform/tenants/tenants-overview#default-preferences).

**Example tenant default behavior:**

* Tenant A defaults: Opted IN for alerts, Email + Slack channels
* User has no preferences set for Tenant A
* Result: User receives alerts via Email + Slack for Tenant A notifications

### Parent Tenant Defaults

When using parent tenants, tenant preferences follow the same hierarchy loading technique described in [Parent Tenants](/platform/tenants/tenants-overview#parent-tenants). When loading the hierarchy, parent tenants' default preferences will be pulled in first and can be updated by child tenants.

**Example inheritance:**

* Parent Tenant: Alerts OPTED\_IN, channels: \[email]
* Child Tenant: Alerts OPTED\_IN, channels: \[email, slack]
* User preference: None set
* Result: User receives alerts via Email + Slack (child overrides parent)

<Note>
  **TENANT AUTO-INFER**

  Courier may also be auto-inferring the Tenant based on a single-user tenant membership, so if you have created tenant memberships, you need to set up your Inbox and Toast SDKs with a `tenantId`. More details on [auto-infer here](/platform/tenants/tenant-deepdive#auto-infer-tenant-context)
</Note>

## Related Resources

<CardGroup cols={2}>
  <Card title="Tenants Overview" href="/platform/tenants/tenants-overview" icon="building">
    Learn about tenant hierarchies and default preferences
  </Card>

  <Card title="Preferences Overview" href="/platform/preferences/preferences-overview" icon="sliders">
    Complete preference management documentation
  </Card>
</CardGroup>

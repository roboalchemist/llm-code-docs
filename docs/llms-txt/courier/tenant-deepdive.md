# Source: https://www.courier.com/docs/platform/tenants/tenant-deepdive.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Tenant Deep Dive

> Comprehensive technical guide to tenant hierarchies, metadata management, inheritance patterns, and integration details for complex multi-tenant architectures.

## Overview

This page provides comprehensive technical details for implementing complex tenant architectures. For basic tenant concepts, see the [Tenants Overview](/platform/tenants/tenants-overview).

## Tenant Object Structure

Tenants store defaults (preferences, profile) that take effect when users don't have specific configurations, plus custom properties for template usage:

```json  theme={null}
{
  "id": "acme-corp-engineering",
  "name": "Acme Corp Engineering Team",
  "parent_tenant_id": "acme-corp",
  "default_preferences": {
    "items": [
      {
        "status": "OPTED_IN",
        "has_custom_routing": true,
        "custom_routing": [
          "email",
          "slack"
        ],
        "id": "production-alerts"
      },
      {
        "status": "OPTED_OUT",
        "has_custom_routing": false,
        "id": "marketing-updates"
      }
    ]
  },
  "properties": {
    "department": "engineering",
    "timezone": "America/Los_Angeles",
    "budget_code": "ENG-2024",
    "slack_workspace": "acme-engineering"
  },
  "user_profile": {
    "company_name": "Acme Corp",
    "team_name": "Engineering",
    "environment": "production"
  },
  "brand_id": "acme-engineering-brand"
}
```

<Info>
  For complete tenant structure details and all available fields, see the [Tenants API Reference](/api-reference/tenants/get-a-tenant).
</Info>

## Hierarchical Inheritance

### Four-Layer Hierarchy Limit

Courier supports up to four layers of tenant hierarchy. Here's how the system handles deeper hierarchies:

<Note>
  Courier supports four layers of tenant hierarchy. For example if you have a hierarchy like the following.

  ```treeview  theme={null}
  tenant0
  └── tenantQ
      └── tenantP
          ├── tenantR1
          │   └── tenantR1D1
          └── tenantR2
              ├── tenantR2D1
              └── tenantR2D2
  ```

  Loading a tenant context of tenantR2 will load in tenant0, tenantQ, tenantP, tenantR2.

  However, loading a tenant context of tenantR2D2 will start at tenantQ, and also load tenantP, tenantR2, then finally tenantR2D2
</Note>

### Metadata Merging Behavior

When data is loaded through a hierarchy, the topmost parent is loaded first, then the next, and next, overwriting keys within the metadata properties as it goes.

**Parent Tenant:**

```json  theme={null}
{
  "brand_id": "brandX",
  "user_profile": {
    "key1": "value1",
    "key3": "valueA"
  }
}
```

**Child Tenant:**

```json  theme={null}
{
  "brand_id": "brandY",
  "user_profile": {
    "key2": "value2",
    "key3": "valueB"
  }
}
```

**Merged Result:**

```json  theme={null}
{
  "brand_id": "brandY",
  "user_profile": {
    "key1": "value1",
    "key2": "value2",
    "key3": "valueB"
  }
}
```

## User Profile Merging

Tenant user profile data merges with user data following a specific precedence order:

1. **Tenant hierarchy merge** (parent → child)
2. **User profile data from Courier**
3. **Send API call to/profile context** (highest priority)

**Resolved Tenant Context:**

```json  theme={null}
{
  "user_profile": {
    "key1": "value1",
    "key2": "valueA",
    "key3": "X",
    "foo": "bar"
  }
}
```

**Courier User Profile:**

```json  theme={null}
{
  "key2": "valueB",
  "key4": "Y",
  "foo": "baz"
}
```

**Send Context:**

```json  theme={null}
{
  "to": {
    "key2": "valueC",
    "key5": true
  }
}
```

**Final Merged Profile Context:**

```json  theme={null}
{
  "foo": "baz",
  "key1": "value1",
  "key2": "valueC",
  "key3": "X",
  "key4": "Y",
  "key5": "true"
}
```

### Provider Credentials Storage

Tenant user profiles commonly store per-tenant provider credentials:

```json  theme={null}
{
  "user_profile": {
    "slack": {
      "access_token": "xoxb-..."
    },
    "microsoft_teams": {
      "webhook_url": "https://outlook.office.com/webhook/..."
    }
  }
}
```

## Default Preferences Management

### Setting Tenant Defaults

Configure tenant-specific default preferences for subscription topics:

**Via Courier Studio:**

```javascript  theme={null}
{
  "items": [
    {
      "id": "72YE3TJK7S40KWN427Y69FD4D4FH",
      "status": "OPTED_IN",
      "type": "subscription_topic"
    }
  ]
}
```

**Via REST API:**

```javascript  theme={null}
// PUT /tenants/:tenant_id
{
  "name": "default-preferences-test",
  "default_preferences": {
    "items": [
      {
        "id": "72YE3TJK7S40KWN427Y69FD4D4FH",
        "status": "OPTED_IN"
      }
    ]
  }
}
```

### Custom Routing Defaults

Set default channel routing per tenant:

```javascript  theme={null}
{
  "items": [
    {
      "id": "72YE3TJK7S40KWN427Y69FD4D4FH",
      "status": "OPTED_IN",
      "type": "subscription_topic",
      "has_custom_routing": true,
      "custom_routing": ["inbox", "push", "sms"]
    }
  ]
}
```

<Note>
  **USER PREFERENCE PRECEDENCE**

  Default Tenant Preferences will change the default behavior for any user/tenant combination who has not updated their preferences for the subscription\_topic\_id yet. Users who have already made a selection for this tenant will keep their current preference.
</Note>

## Branding Integration

Specify a brand as the default for a tenant. This allows inbox, inbox messages, and email messages to be applied based on tenant context instead of global level. Providing the brand in the Notification Send can still override this setting.

To learn more about creating and managing brands, see [Brands in Email Notifications](/platform/content/brands/brands-overview).

## Customer Data Platform Integrations

For both [RudderStack](/external-integrations/cdp/rudderstack) and [Segment](/external-integrations/cdp/segment) integrations, we support the `group` event, which will create a user tenant membership between the `userId` in the group call and the `groupId`.

## Auto-Infer Tenant Context

By default, if a user has a single User Tenant Membership and a Send request does not specify the tenant in the context, Courier will load the tenant information into the context by default. Auto-infer is excellent for studio, list, or audience messages because required provider information may be stored at the tenant level.

You can control this setting under your general workspace settings.

<Frame caption="Workspace Settings - Auto-Infer Tenant Context">
  <img src="https://mintcdn.com/courier-4f1f25dc/PORkmbk0rlaTrsFx/assets/platform/tenants/auto-infer-tenant-context.png?fit=max&auto=format&n=PORkmbk0rlaTrsFx&q=85&s=43d4254e8d0ce08a4ba5a0f72f7ca7fe" alt="Workspace settings showing auto-infer tenant context toggle" width="447" height="125" data-path="assets/platform/tenants/auto-infer-tenant-context.png" />
</Frame>

## Related Resources

<CardGroup cols={2}>
  <Card title="Tenants Overview" href="/platform/tenants/tenants-overview" icon="building">
    Basic tenant concepts and use cases
  </Card>

  <Card title="Tenants API Reference" href="/api-reference/tenants/get-a-tenant" icon="code">
    Complete API documentation for tenant management
  </Card>
</CardGroup>

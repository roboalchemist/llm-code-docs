# Source: https://www.courier.com/docs/platform/tenants/sending-with-tenants.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Sending With Tenants

> Send notifications to tenant members, individual users with tenant context, multiple recipients, or across tenant hierarchies.

When you send with a tenant context, Courier automatically applies the tenant's metadata, preferences, branding, and provider credentials to every notification. You can target:

* **All tenant members** with a single `tenant_id` in `to`
* **Individual users** with explicit tenant context
* **Multiple users** with shared or per-recipient tenant context
* **Tenant hierarchies** using `include_children` or `include_parent`

## Send to tenant members

Specify a `tenant_id` in the `to` field and Courier fans out the message to every user with a membership in that tenant:

```json  theme={null}
{
  "to": {
    "tenant_id": "tenantA"
  },
  "content": {
    "title": "Hello, {first_name}!",
    "body": "Brought to you by {$.tenant.name}"
  },
  "routing": {
    "method": "single",
    "channels": ["inbox"]
  }
}
```

Courier looks up the tenant's members and sends to each one:

```json  theme={null}
// GET /tenants/tenantA/users
// Returns:
{
  "has_more": false,
  "items": [
    {
      "tenant_id": "tenantA",
      "profile": {},
      "type": "user",
      "user_id": "billy_williams"
    },
    {
      "tenant_id": "tenantA",
      "profile": {},
      "type": "user",
      "user_id": "ron_santo"
    },
    {
      "tenant_id": "tenantA",
      "profile": {},
      "type": "user",
      "user_id": "kerry_wood"
    }
  ],
  "next_url": null,
  "type": "list",
  "url": "/tenants/tenantA"
}
```

## Send to a user with tenant context

Set `context.tenant_id` on a recipient to attach tenant metadata, preferences, and branding to their notification:

```json  theme={null}
{
  "to": {
    "user_id": "user1",
    "context": {
      "tenant_id": "tenantA"
    }
  },
  "content": {
    "title": "Hello, {first_name}!",
    "body": "Brought to you by {$.tenant.name}"
  },
  "routing": {
    "method": "single",
    "channels": ["inbox"]
  }
}
```

This sends to `user1` with tenantA's preferences, branding, and metadata. User-level preferences and data take precedence over tenant values.

<Note>
  A user doesn't need to be a tenant member to receive a notification with tenant context. This is useful when tenants hold provider credentials or metadata but you don't need fan-out to all members.
</Note>

## Send to multiple users with tenant context

When sending to an array of users, you can set a shared tenant context at the message level with `message.context.tenant_id`. Every recipient inherits that context.

```json  theme={null}
{
  "message": {
    "template": "WELCOME_TEMPLATE",
    "context": {
      "tenant_id": "tenantA"
    },
    "to": [
      { "user_id": "user1" },
      { "user_id": "user2" },
      { "user_id": "user3" }
    ]
  }
}
```

All three users receive the notification with tenantA's branding, preferences, and metadata.

### Override tenant context per recipient

You can override the message-level tenant for specific recipients by setting `context.tenant_id` on individual entries in the `to` array. Per-recipient context takes precedence over the message-level context.

```json  theme={null}
{
  "message": {
    "template": "MONTHLY_REPORT",
    "context": {
      "tenant_id": "tenantA"
    },
    "to": [
      { "user_id": "user1" },
      { "user_id": "user2" },
      {
        "user_id": "user3",
        "context": {
          "tenant_id": "tenantB"
        }
      }
    ]
  }
}
```

In this example, `user1` and `user2` receive the notification with tenantA's context, while `user3` receives it with tenantB's context.

## Users with multiple tenant memberships

Courier auto-infers tenant context for users who belong to exactly one tenant. For users with multiple memberships, you must specify `tenant_id` explicitly; otherwise Courier returns a `"Tenant Context Not Found"` error.

```json  theme={null}
{
  "message": {
    "template": "tenant/demotemplate",
    "context": {
      "tenant_id": "your-tenant-id"
    },
    "to": {
      "user_id": "user-with-multiple-tenants",
      "email": "user@example.com"
    }
  }
}
```

<Warning>
  When using Courier Create templates with the `tenant/<template_id>` format, `tenant` is the literal word, not your tenant ID. Your actual tenant ID goes in `context.tenant_id`.
</Warning>

**Rules of thumb:**

* **Single-tenant users**: tenant context is auto-inferred; specifying it is optional
* **Multi-tenant users**: always specify `context.tenant_id`
* **Courier Create templates**: always include `context.tenant_id` when using the `tenant/<template_id>` format

## Send to child tenant users

To fan out a message to all users in a tenant's child tenants, set `include_children: true`:

```json  theme={null}
{
  "to": {
    "tenant_id": "ParentTenantA",
    "include_children": true
  },
  "content": {
    "title": "Hello, {first_name}!",
    "body": "Brought to you by {$.tenant.name}"
  },
  "routing": {
    "method": "single",
    "channels": ["inbox"]
  }
}
```

Given the following hierarchy, Courier fans out to all five users (User1 through User5):

```yaml  theme={null}
- ParentTenantA
  child tenants:
    - ChildTenantA1
      user members:
        - User1
        - User2
    - ChildTenantA2
      child tenants:
        - ChildTenantA2-admin
          user_members:
            - User5
      user members:
        - User2
        - User3
  user members:
    - User4
```

## Send to parent tenant users

To fan out upward through the hierarchy, set `include_parent: true`:

```json  theme={null}
{
  "to": {
    "tenant_id": "ChildTenantA2",
    "include_parent": true
  },
  "content": {
    "title": "Hello, {first_name}!",
    "body": "Brought to you by {$.tenant.name}"
  },
  "routing": {
    "method": "single",
    "channels": ["inbox"]
  }
}
```

Given the same hierarchy, Courier fans out to User2, User3, and User4. User1 isn't in the chain upward from ChildTenantA2, and User5 is in a child tenant (not a parent):

```yaml  theme={null}
- ParentTenantA
  child tenants:
    - ChildTenantA1
      user members:
        - User1
        - User2
    - ChildTenantA2
      child tenants:
        - ChildTenantA2-admin
          user_members:
            - User5
      user members:
        - User2
        - User3
  user members:
    - User4
```

<CardGroup cols={2}>
  <Card title="Tenants Overview" href="/platform/tenants/tenants-overview" icon="building">
    Tenant hierarchies, metadata, and configuration.
  </Card>

  <Card title="Tenant Deep Dive" href="/platform/tenants/tenant-deepdive" icon="magnifying-glass">
    Advanced tenant patterns and data model.
  </Card>

  <Card title="Inbox With Tenants" href="/platform/tenants/inbox-with-tenants" icon="inbox">
    Tenant-scoped in-app notification feeds.
  </Card>

  <Card title="Tenants API" href="/api-reference/tenants/get-a-tenant" icon="code">
    Full API reference for tenant operations.
  </Card>
</CardGroup>

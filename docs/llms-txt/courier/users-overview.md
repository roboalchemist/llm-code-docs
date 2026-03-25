# Source: https://www.courier.com/docs/platform/users/users-overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# User Overview

> Learn about Courier's user management system including profiles, audiences, lists, and tenants for organizing users and scaling across multiple organizations.

Courier's user management system is the foundation for targeting notifications. Profiles store contact details and preferences so you can target by `user_id` instead of hardcoding addresses. Lists and audiences let you scale from one-off sends to campaigns and segments.

Getting user management right means consistent delivery, working preferences, and a single place to update when users change.

## Key Concepts

### Profiles

A user profile holds everything Courier needs to reach someone: email, phone, push tokens, custom attributes, and notification preferences. You can create profiles explicitly through the API or let Courier create them implicitly when you first send to a `user_id`.

**Inline vs. stored profiles**: For simple use cases, you can pass contact details directly in each send request. For anything beyond one-off sends, store profiles so you have a single source of truth for each recipient. Stored profiles also enable preferences, lists, and audiences.

### Lists vs. Audiences

Both let you target groups of users, but they work differently:

* **Lists** are static; you manually add and remove members. Use them for curated groups like beta testers, VIP customers, or internal teams.
* **Audiences** are dynamic; you define filter rules (e.g. `plan = "enterprise"`) and Courier automatically matches users as their profiles change. Use them for segments that should update themselves.

You can send to either a list or an audience in a single API call.

### Multi-Tenancy

If you're building a B2B SaaS product, [tenants](/platform/tenants/tenants-overview) let you organize users into customer accounts. Each tenant can have its own branding, preferences, and inbox. Tenants are optional; most consumer-facing products don't need them.

## Common Patterns

**Single-product consumer app**: Store user profiles with email and push tokens. Use audiences to segment by behavior (e.g. active users, churned users). No tenants needed.

**B2B SaaS platform**: Create a tenant per customer account. Store user profiles with a `tenant_id`. Use tenant-scoped preferences so each customer controls their own notification settings.

**Marketing campaigns**: Create lists for campaign recipients. Use [bulk notifications](/tutorials/sending/how-to-send-bulk-notifications) for large-volume sends. Use audiences for recurring segments that should update automatically.

## Next Steps

<CardGroup cols={2}>
  <Card title="User Management" href="/platform/users/users" icon="user">
    Profile structure, send examples, and push tokens
  </Card>

  <Card title="Lists & Audiences" href="/platform/users/audiences" icon="users">
    Static lists and dynamic audience rules
  </Card>

  <Card title="Tenants" href="/platform/tenants/tenants-overview" icon="building">
    Multi-tenant architecture for B2B platforms
  </Card>

  <Card title="Bulk Notifications" href="/tutorials/sending/how-to-send-bulk-notifications" icon="layer-group">
    Large-volume sends and campaign targeting
  </Card>
</CardGroup>

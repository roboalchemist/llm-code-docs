# Source: https://www.courier.com/docs/platform/tenants/inbox-with-tenants.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Inbox and Tenants

> Send Inbox notifications to tenant-specific or global inboxes by configuring tenantId, enabling multi-workspace support and ensuring proper visibility across SDKs.

## Overview

Tenant-specific inboxes enable you to create isolated notification experiences that respect your application's organizational boundaries. By configuring tenant context in both your notification sending and SDK initialization, you can ensure users only see messages relevant to their current organizational context.

This is particularly powerful for B2B SaaS applications where users may belong to multiple organizations, teams, or projects, each requiring separate notification streams.

## Tenant Message Visibility

Messages sent with tenant context are only visible when the SDK is initialized with the same tenant ID. For example, if you send an inbox notification to `user1` with context `tenantA` but do not instantiate the Inbox SDK with `tenantA`, the user will not see the message.

This isolation allows you to build inbox configurations that map to your different workspaces, ensuring users only see contextually relevant notifications.

<Note>
  **TENANT AUTO-INFER**

  Courier may also be auto-inferring the Tenant based on a single-user tenant membership, so if you have created tenant memberships, you need to set up your Inbox and Toast SDKs with a `tenantId`. More details on [auto-infer here](/platform/tenants/tenants-overview#auto-infer-tenant-context-for-user)
</Note>

## SDK Configuration

### React Components

You can instantiate the Courier React [Inbox](https://www.npmjs.com/package/@trycourier/react-inbox) and [Toast](https://www.npmjs.com/package/@trycourier/react-toast) components with tenant context:

```jsx  theme={null}
// Show inbox for specific tenant context
<CourierProvider clientKey="..." userId="user1" tenantId="tenantA">
  <Inbox />
  <Toast />
  {children}
</CourierProvider>

// Dynamic tenant switching example
const [currentTenant, setCurrentTenant] = useState("acme-corp");

<CourierProvider clientKey="..." userId="user1" tenantId={currentTenant}>
  <select onChange={(e) => setCurrentTenant(e.target.value)}>
    <option value="acme-corp">Acme Corp</option>
    <option value="beta-inc">Beta Inc</option>
  </select>
  <Inbox />
</CourierProvider>
```

### JavaScript Components

For vanilla JavaScript implementations, configure the tenant during initialization:

```javascript  theme={null}
// Initialize with specific tenant
window.courier.init({
  clientKey: "...",
  userId: "user1",
  tenantId: "tenantA",
});

// Switch tenant context dynamically
function switchTenant(newTenantId) {
  window.courier.init({
    clientKey: "...",
    userId: "user1", 
    tenantId: newTenantId,
  });
}
```

## Common Issues

### Tenant Context Mismatch

If messages aren't appearing in the inbox, verify that:

* The message was sent with the same `tenant_id` used in SDK initialization
* Auto-infer behavior isn't affecting tenant context (see [auto-infer documentation](/platform/tenants/tenants-overview#auto-infer-tenant-context-for-user))
* User has proper tenant membership if required

## Related Resources

<CardGroup cols={2}>
  <Card title="Tenants Overview" href="/platform/tenants/tenants-overview" icon="building">
    Learn about tenant hierarchies and auto-infer behavior
  </Card>

  <Card title="Courier Inbox SDK" href="/platform/inbox/inbox-overview" icon="inbox">
    Complete inbox implementation documentation
  </Card>
</CardGroup>

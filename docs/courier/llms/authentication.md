# Source: https://www.courier.com/docs/platform/inbox/authentication.md

# Source: https://www.courier.com/docs/platform/create/authentication.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Authenticating the Embeddable Designer

> Courier Create uses JWT authentication to securely authorize access to template and brand editing features. While development can begin using a client key, production environments should rely on JWTs with appropriate scopes for fine-grained access control.

## Generating a JWT

To generate a JWT, make a POST request to the Courier API with the required scopes and authentication details:

```bash  theme={null}
POST https://api.courier.com/auth/issue-token
```

### Full Tenant Access

Grants access to all tenants and their notification data.

```bash  theme={null}
curl --request POST \
  --url https://api.courier.com/auth/issue-token \
  --header 'Accept: application/json' \
  --header 'Authorization: Bearer $YOUR_AUTH_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "scope": "user_id:$YOUR_USER_ID tenants:read tenants:notifications:read tenants:notifications:write",
    "expires_in": "30 days"
  }'
```

### Specific Tenant Notification Access

Limits access to a specific tenant.

```bash  theme={null}
curl --request POST \
  --url https://api.courier.com/auth/issue-token \
  --header 'Accept: application/json' \
  --header 'Authorization: Bearer $YOUR_AUTH_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "scope": "user_id:$YOUR_USER_ID tenant:tenant-123:read tenant:tenant-123:notification:read tenant:tenant-123:notification:write",
    "expires_in": "30 days"
  }'
```

## Available JWT Scopes

Use these scopes to fine-tune access and secure your integration. Ensure your frontend tokens are limited to the least privileges necessary for the intended operations.

* `tenants:read` | Read all tenant data

* `tenants:notifications:read` | Read all notification templates

* `tenants:notifications:write` | Write notification templates

* `tenants:brand:read` | Read brand settings across tenants

* `tenant:$TENANT_ID:read` | Read data for a specific tenant

* `tenant:$TENANT_ID:notification:read` | Read specific tenant's notifications

* `tenant:$TENANT_ID:notification:write` | Write specific tenant's notifications

* `tenant:$TENANT_ID:brand:read` | Read brand settings for a specific tenant

* `tenant:$TENANT_ID:brand:write` | Write brand settings for a specific tenant

# Source: https://docs.knock.app/api-reference/tenants/schemas/tenant_request.md

### TenantRequest

A tenant to be set in the system. You can supply any additional properties on the tenant object.

#### Attributes

- **channel_data** (unknown) - The channel data for the tenant.
- **id** (string) *required* - The unique identifier for the tenant.
- **name** (string) - An optional name for the tenant.
- **preferences** (unknown) - The preferences for the tenant.
- **settings** (object) - The settings for the tenant. Includes branding and preference set.

#### Example

```json
{
  "id": "tenant_123",
  "name": "ACME Corp, Inc.",
  "settings": {
    "branding": {
      "icon_url": "https://example.com/icon.png",
      "logo_url": "https://example.com/logo.png",
      "primary_color": "#000000",
      "primary_color_contrast": "#FFFFFF"
    }
  }
}
```


# Source: https://docs.knock.app/api-reference/tenants/schemas/tenant.md

### Tenant

A tenant entity.

#### Attributes

- **__typename** (string) *required* - The typename of the schema.
- **id** (string) *required* - The unique identifier for the tenant.
- **name** (string) - An optional name for the tenant.
- **settings** (object) - The settings for the tenant. Includes branding and preference set.

#### Example

```json
{
  "__typename": "Tenant",
  "id": "tenant_jp123",
  "name": "Jurassic Park",
  "settings": {
    "branding": {
      "icon_url": "https://example.com/trex_silhouette_icon.png",
      "logo_url": "https://example.com/amber_fossil_logo.png",
      "primary_color": "#DF1A22",
      "primary_color_contrast": "#FFDE00"
    },
    "preference_set": {
      "categories": {
        "safety": {
          "channel_types": {
            "email": true,
            "push": true
          }
        }
      },
      "channel_types": {
        "email": true,
        "in_app_feed": true,
        "push": true
      },
      "id": "default",
      "workflows": {
        "park_alert": {
          "channel_types": {
            "email": true,
            "push": true
          }
        }
      }
    }
  }
}
```


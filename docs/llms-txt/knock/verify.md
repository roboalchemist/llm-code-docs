# Source: https://docs.knock.app/mapi-reference/auth/verify.md

### Verify scope

Return information about the current calling scope. Will either be a service token or from an OAuth context.

#### Endpoint

`GET /v1/whoami`

#### Responses

##### 200

OK

###### Example

```json
{
  "account_features": {
    "batch_items_render_limit_allowed": false,
    "custom_branding_allowed": false,
    "data_retention_days": 30,
    "data_warehouse_extension_allowed": false,
    "datadog_extension_allowed": true,
    "dsync_allowed": false,
    "guides_monthly_notified_recipients_limit": 500,
    "guides_per_tenant_scope_allowed": false,
    "heap_extension_allowed": false,
    "knock_branding_required": true,
    "litmus_email_preview_allowed": false,
    "message_sent_limit": 10000,
    "new_relic_extension_allowed": false,
    "segment_extension_allowed": false,
    "self_serve_allowed": true,
    "sso_allowed": false,
    "tenant_preferences_allowed": false,
    "translations_allowed": false
  },
  "account_name": "Acme, Inc.",
  "account_slug": "acme",
  "service_token_name": "My Service Token",
  "type": "service_token",
  "user_id": null
}
```


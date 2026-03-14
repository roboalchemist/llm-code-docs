# Source: https://docs.acceldata.io/api/labels.md

# Labels

Labels are key–value metadata that provide richer detail than tags. For example, you could label an asset with `owner=marketing` or `sensitivity=PII`. This helps enforce governance — policies can be applied based on label values, such as requiring stricter monitoring for `sensitivity=PII` assets.

> ⚠️ All endpoints require authentication. See [Authentication & Headers](https://docs.acceldata.io/acceldata-data-observability-cloud/api/authentication).

## Endpoint(s)

- `GET /catalog-server/api/assets/:id/labels`
- `PUT /catalog-server/api/assets/:id/labels`
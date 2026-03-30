# Source: https://docs.verda.com/welcome-to-verda/release-notes/verda-api-changes.md

# Verda API changes

For full API documentation go to [Verda API docs](https://api.verda.com/v1/docs)

### 2026-03-11 API rate limits

Introduced rate limits to our Public API to ensure the stability of our API and platform for everyone. Rate limits are restrictions our API enforces on how frequently a user or client can make requests to our services within a given timeframe.

Please take a look at our API documentation section ["Rate limits"](https://api.verda.com/v1/docs#description/rate-limits).

### 2026-02-03 Spot instance volume policy

When creating a spot instance, it is now possible to specify a removal policy for the OS volume and any additional volumes created alongside it. Use the `on_spot_discontinue` field:

[POST /v1/instances](https://api.verda.com/v1/docs#tag/instances/POST/v1/instances)

```js
POST v1/instances
{
  "instance_type": "CPU.4V.16G",
  "image": "ubuntu-24.04",
  "ssh_key_ids": ["442e6a59-26c2-4cea-a619-39762c0d2385"],
  "hostname": "test-instance",
  "location_code": "FIN-03",
  "is_spot": true,
  "os_volume": {
    "name": "test-instance-os-volume",
    "size": 55,
    // If "delete_permanently", the volume will be deleted when the spot instance is discontinued
    "on_spot_discontinue": "keep_detached" | "move_to_trash" | "delete_permanently"
  }
}
```

### 2026-02-03 Delete volumes permanently when deleting an instance

When deleting an instance, you can now specify whether its volumes should be moved to deleted storage (default) or deleted permanently:

[PUT /v1/instances](https://api.verda.com/v1/docs#tag/instances/PUT/v1/instances)

```js
PUT v1/instances
{
  "action": "delete",
  "id": "442e6a59-26c2-4cea-a619-39762c0d2385",
  "volume_ids": ["5e9e63a9-fc3b-427b-b259-0c77dce61090"],
  // Will delete the instance and volumes permanently
  "delete_permanently": true
}
```

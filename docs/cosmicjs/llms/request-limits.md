# Source: https://www.cosmicjs.com/docs/api/request-limits.md

# Request limits

Learn about request limits to the Cosmic API.

### API rate limits

All Cosmic Buckets have the following rate limits:

- **Rate limit:** `100` requests per second
- **Burst limit:** `200` requests

These limits apply to non-cached API requests. Non-cached requests include any initial `GET` request and all `POST`, `PUT`, `PATCH`, and `DELETE` requests to the API. This does not apply to any files or images served via the Cosmic CDN or imgix CDN.

If you exceed these limits, the API will return a `429 Too Many Requests` response. The burst limit allows for short spikes in traffic while the rate limit ensures sustained request rates remain within acceptable bounds.

### Response time limits

Endpoints have a timeout limit of `30` seconds. If you find yourself hitting this limit, you can reduce your payload size with `limit` and `props` options. See [Objects API Reference](/docs/api/objects) for more info.

### Size limits

Except for the upload media endpoint, which allows up to `900MB` files to be uploaded, all Cosmic requests and responses have a size limit of `6MB`.

### Optimizations

All requests allow `gzip` ecoding. If connecting to the API directly, adding `Accept-Encoding: gzip` can dramatically reduce response time and size. This is added by default on all Cosmic open source clients.
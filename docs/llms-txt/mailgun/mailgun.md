# Source: https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun.md

# Mailgun API

Mailgun API defined by OpenAPI Specification (OAS) 3.1.0

Version: 3.0.0

## Servers

US Mailgun
```
https://api.mailgun.net
```

EU Mailgun
```
https://api.eu.mailgun.net
```

## Security

### basicAuth

HTTP Basic auth using api:YOUR_API_KEY. See [documentation](https://documentation.mailgun.com/docs/mailgun/api-reference/authentication/)

Type: http
Scheme: basic

## Download OpenAPI description

[Mailgun API](https://documentation.mailgun.com/_spec/docs/mailgun/api-reference/send/mailgun.yaml)

## Messages

Send email two ways via our REST API:
1. Send emails using MIME format using a MIME building library
2. Submit the individual parts (Text, html, attachments, etc.)

Reminder: You can also send email via SMTP with Mailgun. Please reference the user manual.

### Send an email

 - [POST /v3/{domain_name}/messages](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/messages/post-v3--domain-name--messages.md): Pass the components of the messages such as To, From, Subject, HTML, text parts, attachments, etc. Mailgun will build a MIME representation of the message and send it. In order to send you must provide one of the following parameters: 'text', 'html', 'amp-html' or 'template'. Important: Send options (parameters starting with o:, h:, v:, or t:) are limited to 16KB total

### Send an email in MIME format

 - [POST /v3/{domain_name}/messages.mime](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/messages/post-v3--domain-name--messages-mime.md): Build a MIME string yourself using a MIME library and submit it to Mailgun. Important: Send options (parameters starting with o:, h:, v:, or t:) are limited to 16KB total

### Retrieve a stored email

 - [GET /v3/domains/{domain_name}/messages/{storage_key}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/messages/get-v3-domains--domain-name--messages--storage-key-.md): Event(s) created from sending an email with Mailgun will contain a  to use to retrieve the email.

### Resend an email

 - [POST /v3/domains/{domain_name}/messages/{storage_key}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/messages/post-v3-domains--domain-name--messages--storage-key-.md)

### Get messages queue status

 - [GET /v3/domains/{name}/sending_queues](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/messages/get-v3-domains--name--sending-queues.md): Provides default and scheduled message queue information.

### Delete scheduled and undelivered mail

 - [DELETE /v3/{domain_name}/envelopes](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/messages/delete-v3--domain-name--envelopes.md): Deletes all scheduled and undelivered mail from the domain queue.  This endpoint must be called on the same storage API host as the mail's generated storage URL.  e.g. https://storage-us-east4.api.mailgun.net/v3/example.com/envelopes

The storage hosts are: , , and .

## Domains

Domains API manages domains, domain keys and DNS verification.

### Get domains

 - [GET /v4/domains](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/domains/get-v4-domains.md): Get the list of domains. Can be filtered by state or authority. Sorting is optional. The list is paginated and limited to 1000 items per page.

### Create a domain

 - [POST /v4/domains](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/domains/post-v4-domains.md): Creates a domain for sending emails

### Get domain details

 - [GET /v4/domains/{name}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/domains/get-v4-domains--name-.md): Fetches json representation of a domain that includes details about the domain's state and settings.

### Update domain

 - [PUT /v4/domains/{name}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/domains/put-v4-domains--name-.md): Update domain configuration like smtp credentials, enable/disable automatic sender security, spam actions, wildcard, or tracking web scheme.

### Verify Domain

 - [PUT /v4/domains/{name}/verify](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/domains/put-v4-domains--name--verify.md): Verify the domains DNS records (includes A, CNAME, SPF, DKIM and MX records) to ensure the domain is ready and able to send

### Delete a domain

 - [DELETE /v3/domains/{name}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/domains/delete-v3-domains--name-.md): The domain must not be disabled or used as an authority for an other domain. Sandbox domain can't be deleted.

## Domain Keys

An authentication standard used to prevent email spoofing.

### List keys for all domains

 - [GET /v1/dkim/keys](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/domain-keys/get-v1-dkim-keys.md): List domain keys, and optionally filter by signing domain or selector. Results are paginated - use the 'limit' parameter to control page size (default 10, max 100). Use the 'page' parameter from the paging response URLs to navigate through pages.

### Create a domain key

 - [POST /v1/dkim/keys](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/domain-keys/post-v1-dkim-keys.md): Create a domain key. Note that once private keys are created or imported they are never exported.
Alternatively, you can import an existing PEM file containing a RSA private key in PKCS #1, ASn.1 DER
			   format. Note, the pem can be passed as a file attachment or as a form-string parameter.

### Delete a domain key

 - [DELETE /v1/dkim/keys](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/domain-keys/delete-v1-dkim-keys.md): Domain keys are not recoverable after deletion so use with care

### Activate a domain key

 - [PUT /v4/domains/{authority_name}/keys/{selector}/activate](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/domain-keys/put-v4-domains--authority-name--keys--selector--activate.md): Activate a key to be used to DKIM sign emails with. Note: dns records must be valid for a domain key to be activated

### List domain keys

 - [GET /v4/domains/{authority_name}/keys](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/domain-keys/get-v4-domains--authority-name--keys.md): List all domain keys for your domain, including active/inactive and valid/invalid ones.

### Deactivate a domain key

 - [PUT /v4/domains/{authority_name}/keys/{selector}/deactivate](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/domain-keys/put-v4-domains--authority-name--keys--selector--deactivate.md): Deactivating for a specified authority and/or selector means a key won't be used for signing email anymore, even if they are valid.

### Update DKIM authority

 - [PUT /v3/domains/{name}/dkim_authority](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/domain-keys/put-v3-domains--name--dkim-authority.md): You can delegate the domain authority to an other domain. Domain's authority is set to itself by default.

### Update a DKIM selector

 - [PUT /v3/domains/{name}/dkim_selector](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/domain-keys/put-v3-domains--name--dkim-selector.md): Selector is the unique identifier of your key. It has to be different from other keys selector.

## Domain Tracking

Mailgun offers tracking for clicks, unsubscribes, and opens, with optional HTTPS protocol support on tracking URLs. To enable HTTPS, Mailgun uses Letâs Encrypt with HTTP-01 challenges through your existing tracking CNAME record to issue a TLS certificate. This setup also includes support for HTTP Strict Transport Security (HSTS) for enhanced security.

### Get tracking settings

 - [GET /v3/domains/{name}/tracking](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/domain-tracking/get-v3-domains--name--tracking.md): Use to check if open, click and unsubscribe tracking are active/inactive.

### Update click tracking settings

 - [PUT /v3/domains/{name}/tracking/click](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/domain-tracking/put-v3-domains--name--tracking-click.md): Use to turn on/off the click tracking at the domain level.

### Update open tracking settings

 - [PUT /v3/domains/{name}/tracking/open](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/domain-tracking/put-v3-domains--name--tracking-open.md): Use to turn on/off the open tracking at the domain level.

### Update unsubscribe tracking settings

 - [PUT /v3/domains/{name}/tracking/unsubscribe](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/domain-tracking/put-v3-domains--name--tracking-unsubscribe.md): Use to turn on/off the unsubscribe tracking at the domain level.

### Tracking Certificate: Get certificate and status

 - [GET /v2/x509/{domain}/status](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/domain-tracking/get-v2-x509--domain--status.md): Get x509 TLS certificate and status

### Tracking Certificate: Regenerate expired certificate

 - [PUT /v2/x509/{domain}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/domain-tracking/put-v2-x509--domain-.md): Initiates regeneration of an expired TLS certificate for the tracking domain in a background task.  Once generation is enqueued, you may poll status endpoint in location field to check for success.  This will not regenerate an existing certificate that is still valid

### Tracking Certificate: Generate

 - [POST /v2/x509/{domain}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/domain-tracking/post-v2-x509--domain-.md): Initiates generation of a TLS certificate for the tracking domain in a background task.  Once generation is enqueued, you may poll the status endpoint in  field to check for success

## DKIM Security

Automatic Sender Security DKIM Key APIs. To enable this feature please see 'Update a domain' API docs.

### Update Automatic Sender Security DKIM key rotation for a domain

 - [PUT /v1/dkim_management/domains/{name}/rotation](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/dkim-security/put-v1-dkim-management-domains--name--rotation.md): The minimum allowed interval for rotation is 5 days.

### Rotate Automatic Sender Security DKIM key for a domain

 - [POST /v1/dkim_management/domains/{name}/rotate](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/dkim-security/post-v1-dkim-management-domains--name--rotate.md): Immediately rotate your DKIM key. This will trigger a rotation even if auto-rotation is disabled on the domain.

## Webhooks

Webhooks API manages domain's webhooks. You can create, access and delete webhooks programmatically.

### Get domain webhooks

 - [GET /v3/domains/{domain}/webhooks](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/webhooks/get-v3-domains--domain--webhooks.md): Returns all webhooks for the domain.

### Create a domain webhook

 - [POST /v3/domains/{domain}/webhooks](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/webhooks/post-v3-domains--domain--webhooks.md): Create a list of webhook URLs you'd like to receive Mailgun's POST requests containing event information.

### Get domain webhooks by type

 - [GET /v3/domains/{domain_name}/webhooks/{webhook_name}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/webhooks/get-v3-domains--domain-name--webhooks--webhook-name-.md): Get the list of url(s) for a webhook identified by its webhook_name.

### Update domain webhook

 - [PUT /v3/domains/{domain_name}/webhooks/{webhook_name}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/webhooks/put-v3-domains--domain-name--webhooks--webhook-name-.md): Replace the list of urls by the given one with the  param. Here is the list of supported webhook: , , , , , ,  and .

### Delete domain webhooks by type

 - [DELETE /v3/domains/{domain_name}/webhooks/{webhook_name}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/webhooks/delete-v3-domains--domain-name--webhooks--webhook-name-.md): Remove all url(s) for a specified webhook type.

### Update domain webhooks (v4)

 - [PUT /v4/domains/{domain}/webhooks](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/webhooks/put-v4-domains--domain--webhooks.md): Update webhook URL to associate it with different event types. This replaces the existing event type associations for the given URL.

### Create domain webhooks (v4)

 - [POST /v4/domains/{domain}/webhooks](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/webhooks/post-v4-domains--domain--webhooks.md): Create webhook URLs for multiple event types in a single operation. This v4 endpoint allows associating one URL with multiple webhook event types.

### Delete domain webhooks (v4)

 - [DELETE /v4/domains/{domain}/webhooks](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/webhooks/delete-v4-domains--domain--webhooks.md): Delete webhook URLs from all event types they are associated with. Supports deleting multiple URLs at once by providing a comma-separated list.

## Metrics

The Mailgun Metrics API provides programmatic access to detailed analytics data about your email sending activity. This API allows you to query, filter, and analyze email performance metrics to gain insights into deliverability, engagement, and overall sending health.

## Metrics vs. Stats API

The Metrics API is the modern replacement for the deprecated Stats API:

| Feature | Stats API (Deprecated) | Metrics API (Current) |
|---------|----------------------|---------------------|
| Flexibility | Limited filtering | Advanced filtering with logical operators |
| Dimensions | Fixed groupings | Flexible dimension combinations |
| Metrics | Basic counts | Comprehensive metrics including rates |
| Performance | Slower | Optimized for large datasets |
| Future Support | None | Active development |

**Migration:** If you're using the Stats API, plan to migrate to the Metrics API for continued support and new features.

## What Are Metrics?

Metrics are quantitative measurements of your email activity. The Mailgun platform collects event data in real-time and aggregates it into meaningful metrics that help you understand how your emails are performing.

## Types of Metrics

Mailgun provides two categories of metrics:

### Sending Metrics (via `/v1/analytics/metrics`)

These metrics track the lifecycle and performance of your outbound emails:

- **Volume Metrics**: Messages accepted, delivered, failed, queued
- **Engagement Metrics**: Opens, clicks, unsubscribes
- **Deliverability Metrics**: Bounces (permanent and temporary), complaints (spam reports)
- **Rate Metrics**: Delivered rate, open rate, click rate, bounce rate
- **ESP-Specific Metrics**: Performance broken down by email service provider

See [metric definitions](https://documentation.mailgun.com/docs/mailgun/user-manual/reporting/metric-definitions) for a complete list of available metrics.

### Usage Metrics (via `/v1/analytics/usage/metrics`)

These metrics track your consumption of Mailgun services and features:

- **Email Validation**: Single validations, bulk validations, API calls
- **Email Preview**: Preview generation counts and failures
- **Blocklist Monitoring**: Domain and IP blocklist checks
- **Accessibility Checks**: Accessibility validation counts
- **Seed Testing**: Seed test campaigns sent

## Core Concepts

### Dimensions

Dimensions are the attributes by which you can slice and group your metrics data. Think of them as the "categories" or "labels" for your data.

**Available Dimensions:**

See [dimensions](https://documentation.mailgun.com/docs/mailgun/user-manual/reporting/dimensions) for a complete list of available dimensions.

**Example:** If you query with dimensions `["time", "domain"]`, your results will be grouped by time period for each sending domain.

### Resolution

Resolution determines the time granularity of your results:

- **hour**: Data grouped by hour (useful for real-time monitoring)
- **day**: Data grouped by day (most common for daily reports)
- **month**: Data grouped by month (useful for trend analysis)

The resolution you choose affects how the `time` dimension groups your data.

### Time Range Selection

You have flexible options for specifying the time range:

**Option 1: Start and End Dates**
```json
{
"start": "Mon, 13 Nov 2023 00:00:00 -0600",
"end": "Mon, 20 Nov 2023 23:59:59 -0600"
}
```

**Option 2: Duration**
```json
{
"duration": "7d"
}
```

This calculates the start date and end date automatically (7 days before the today).

**Date Format:** RFC 2822 format with timezone support

### Filters

Filters allow you to narrow down your data to specific criteria. The filter system uses a logical structure:

```json
{
"filter": {
  "AND": [
    {
      "attribute": "domain",
      "comparator": "=",
      "values": [
        {"value": "example.com"}
      ]
    },
    {
      "attribute": "tag",
      "comparator": "=",
      "values": [
        {"value": "newsletter"}
      ]
    }
  ]
}
}
```

**Note:** Filters only support the "AND" operator. "OR" is not supported.  In the example above, only data where the sending domain equals `example.com` and the tag equals `newsletter` will be returned.

**Filter Components:**
- **attribute**: The field to filter on (domain, tag, subaccount)
- **comparator**: The comparison operator (=, !=, contains, not contains)
- **values**: Array of values to match against

### Aggregates

When `include_aggregates` is set to `true`, the API returns top-level summary statistics across all your queried data. This gives you totals and averages without having to sum the individual items yourself.

### Subaccounts

If you use Mailgun's subaccount feature, you can:
- Query metrics for a specific subaccount using filters
- Include all subaccounts' data with `include_subaccounts: true`
- View aggregated data across all subaccounts

## Data Retention

Mailgun retains metrics data for different durations based on resolution:
- **Hourly**: 60 days
- **Daily**: 1 year
- **Monthly**: Indefinitely 

## Pagination

For queries that return large result sets, the API uses offset-based pagination with `skip` and `limit` request attributes.

- `skip` specifies how many items to offset (skip) from the beginning of the result set.
- `limit` specifies the maximum number of items to return in a single request.

Defaults and limits:
- Default page size varies by dimension. Default for time dimension is 1500 items. All other dimensions default to 10 items.
- Maximum `limit` is 1500 for the time dimension and 1000 for all other dimensions.

How pagination works:
- Start with `skip=0` and a desired `limit` (for example, `limit=1000`).
- Retrieve the next page by increasing `skip` by the value of `limit`:
- First page: `skip=0`, `limit=1000`
- Second page: `skip=1000`, `limit=1000`
- Third page: `skip=2000`, `limit=1000`
- Continue paging until fewer items than the specified `limit` are returned.

Additional details:
- The response includes a `pagination` object containing the total number of available items.
- Results can be sorted using the `sort` parameter, for example `time:asc` or `time:desc`. 
For consistent pagination, use a deterministic sort order.

## Rate Limits and Quotas

- API calls are subject to a rate limit of 500 requests every 10 seconds

### Query account metrics

 - [POST /v1/analytics/metrics](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/metrics/post-v1-analytics-metrics.md): Queries filtered metrics for an account

### Query account usage metrics

 - [POST /v1/analytics/usage/metrics](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/metrics/post-v1-analytics-usage-metrics.md): Queries filtered usage metrics for an account

## Logs

Mailgun keeps track of every inbound and outbound message event and stores this log data. This data can be queried and filtered to provide insights into the health of your email infrastructure.

### List logs

 - [POST /v1/analytics/logs](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/logs/post-v1-analytics-logs.md): Gets customer event logs for an account

## Bounce Classification

### List statistic v2

 - [POST /v2/bounce-classification/metrics](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/bounce-classification/post-v2-bounce-classification-metrics.md): Items that have no bounces and no delays(classified_failures_count==0) are not returned.

### List statistics, ordered by total bounces (deprecated)

 - [GET /v1/bounce-classification/stats](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/bounce-classification/get-v1-bounce-classification-stats.md): Deprecated: use POST /v2/bounce-classification/metrics instead

### List domains statistic per account (deprecated)

 - [GET /v1/bounce-classification/domains](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/bounce-classification/get-v1-bounce-classification-domains.md): Deprecated: use POST /v2/bounce-classification/metrics

### List statistic per domain (deprecated)

 - [GET /v1/bounce-classification/domains/{domain}/entities](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/bounce-classification/get-v1-bounce-classification-domains--domain--entities.md): Deprecated: use POST /v2/bounce-classification/metrics

### List statistic per entity (deprecated)

 - [GET /v1/bounce-classification/domains/{domain}/entities/{entity-id}/rules](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/bounce-classification/get-v1-bounce-classification-domains--domain--entities--entity-id--rules.md): Deprecated: use POST /v2/bounce-classification/metrics

### List Bounce Logs (deprecated)

 - [GET /v1/bounce-classification/domains/{domain}/events](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/bounce-classification/get-v1-bounce-classification-domains--domain--events.md): Deprecated: use POST /v1/analytics/logs - https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/logs

### List entities (deprecated)

 - [GET /v1/bounce-classification/config/entities](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/bounce-classification/get-v1-bounce-classification-config-entities.md): Deprecated: use POST /v2/bounce-classification/metrics

### List rules (deprecated)

 - [GET /v1/bounce-classification/config/rules](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/bounce-classification/get-v1-bounce-classification-config-rules.md): Deprecated: use GET /v2/bounce-classification/config/groups/{group-id}

## Tags New

Mailgun allows you to tag your email with unique identifiers. Tags are visible via our analytics tags API endpoint.

### Update account tag

 - [PUT /v1/analytics/tags](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/tags-new/put-v1-analytics-tags.md): Updates the tag description for an account

### Post query to list account tags or search for single tag

 - [POST /v1/analytics/tags](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/tags-new/post-v1-analytics-tags.md): Gets the list of all tags, or filtered by tag prefix, for an account

### Delete account tag

 - [DELETE /v1/analytics/tags](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/tags-new/delete-v1-analytics-tags.md): Deletes the tag for an account

### Get account tag limit information

 - [GET /v1/analytics/tags/limits](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/tags-new/get-v1-analytics-tags-limits.md): Gets the tag limit and current number of unique tags for an account

## Stats

Mailgun collects many different events and generates event statistics which are available in your Control Panel. This data is also available via our stats API endpoint.<br><br>WARNING:<i> This API is deprecated in favor of our [Metrics](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/metrics) API. </i>

### Totals for entire account (deprecated)

 - [GET /v3/stats/total](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/stats/get-v3-stats-total.md): Gets stat totals for an entire account

### Totals for entire domain (deprecated)

 - [GET /v3/{domain}/stats/total](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/stats/get-v3--domain--stats-total.md): Gets stat totals for an entire domain

### Totals for account domains for a single time resolution (deprecated)

 - [GET /v3/stats/total/domains](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/stats/get-v3-stats-total-domains.md): Gets stat  totals for domains in an account for a single time resolution

### Filtered/grouped totals for entire account (deprecated)

 - [GET /v3/stats/filter](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/stats/get-v3-stats-filter.md): Gets filtered and group stat totals for an entire account

### Aggregate counts by ESP (deprecated)

 - [GET /v3/{domain}/aggregates/providers](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/stats/get-v3--domain--aggregates-providers.md): Gets aggregate counts by email service provider

### Aggregate counts by devices triggering events  (deprecated)

 - [GET /v3/{domain}/aggregates/devices](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/stats/get-v3--domain--aggregates-devices.md): Gets  aggregate counts on devices that triggered events ('tablet', 'phone', 'pc', etcâ¦)

### Aggregate counts by country (deprecated)

 - [GET /v3/{domain}/aggregates/countries](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/stats/get-v3--domain--aggregates-countries.md): Gets aggregate counts by country (USA, RUS, etcâ¦)

## Tags

Mailgun lets you tag each outgoing message with a custom value. When you access stats on your messages, they will be aggregated by these tags.<br><br>WARNING:<i> This API is deprecated in favor of our new [Tags](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/tags-new) API. </i>

### List all tags (deprecated)

 - [GET /v3/{domain}/tags](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/tags/get-v3--domain--tags.md): List all tags associated with a domain

### Get a tag (deprecated)

 - [GET /v3/{domain}/tag](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/tags/get-v3--domain--tag.md): Get a tag associated with a domain

### Update tag  (deprecated)

 - [PUT /v3/{domain}/tag](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/tags/put-v3--domain--tag.md): Update a tag associated with a domain

### Delete tag (deprecated)

 - [DELETE /v3/{domain}/tag](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/tags/delete-v3--domain--tag.md): Delete a tag associated with a domain

### Get aggregate stat types by tag (deprecated)

 - [GET /v3/{domain}/tag/stats/aggregates](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/tags/get-v3--domain--tag-stats-aggregates.md): Returns a list  for a given domain for different event types

### Get stats by tag (deprecated)

 - [GET /v3/{domain}/tag/stats](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/tags/get-v3--domain--tag-stats.md): Retrieve stats by tag

### Get tag limits (deprecated)

 - [GET /v3/domains/{domain}/limits/tag](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/tags/get-v3-domains--domain--limits-tag.md): Get tag limits by domain

## Events

Mailgun keeps track of every inbound and outbound message event and stores this data for at least 3 days.<br><br>WARNING:<i> This API is deprecated in favor of our [Logs](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/logs) API. </i>

### Retrieves a paginated list of events

 - [GET /v3/{domain_name}/events](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/events/get-v3-domain_name-events.md): Mailgun tracks every inbound and outbound message event and retains this data for at least 3 days.
See Filter expression for details about filtering expressions


## Alerts

Mailgun allows you to get instant notifications on the sending metrics that matter most, configured specifically for your unique business needs and assets. Route these alerts to the channels your team relies on. Stay on top of sending performance without the need to manually monitor.

### List send alerts

 - [GET /v1/thresholds/alerts/send](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/alerts/get-v1-thresholds-alerts-send.md)

### Create a send alert for an account

 - [POST /v1/thresholds/alerts/send](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/alerts/post-v1-thresholds-alerts-send.md)

### Get a send alert

 - [GET /v1/thresholds/alerts/send/{name}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/alerts/get-v1-thresholds-alerts-send--name-.md)

### Update a send alert

 - [PUT /v1/thresholds/alerts/send/{name}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/alerts/put-v1-thresholds-alerts-send--name-.md)

### Delete a send alert

 - [DELETE /v1/thresholds/alerts/send/{name}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/alerts/delete-v1-thresholds-alerts-send--name-.md)

### List account hits

 - [GET /v1/thresholds/hits](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/alerts/get-v1-thresholds-hits.md)

## Unsubscribe

Unsubscribe list stores email addresses of recipients who unsubscribed from your mailings by clicking a Mailgun generated unsubscribe link.

### Import unsubscribe list

 - [POST /v3/{domain_name}/unsubscribes/import](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/unsubscribe/post-v3--domainid--unsubscribes-import.md): Import a CSV file containing a list of addresses to add to the unsubscribe list. The CSV file must be 25MB or under and can contain the following column headers: address, tags, created_at. address is a valid email address (required). tags is tag to unsubscribe from, use ). created_at is timestamp of unsubscribe event in RFC2822 format (optional, default: current time)

### Lookup unsubscribe record

 - [GET /v3/{domain_name}/unsubscribes/{address}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/unsubscribe/get-v3--domainid--unsubscribes--address-.md): Fetch a single unsubscribe record to check if a given address is present in a list of unsubscribed users.

### Remove unsubscribe

 - [DELETE /v3/{domain_name}/unsubscribes/{address}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/unsubscribe/delete-v3--domainid--unsubscribes--address-.md): Delivery to the deleted email address resumes until it unsubscribes again.

### List all unsubscribes

 - [GET /v3/{domain_name}/unsubscribes](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/unsubscribe/get-v3--domainid--unsubscribes.md): Paginate over a list of unsubscribes for domain.

### Add unsubscribes

 - [POST /v3/{domain_name}/unsubscribes](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/unsubscribe/post-v3--domainid--unsubscribes.md): Request body is expected to be a valid JSON encoded sting containing up to 1000 unsubscribe records or a single unsubscribe record as application/form-data

### Clear all unsubscribes

 - [DELETE /v3/{domain_name}/unsubscribes](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/unsubscribe/delete-v3--domainid--unsubscribes.md): Clear all unsubscribe email addresses for the domain. Delivery to the deleted email addresses will no longer be suppressed.

## Complaints

Email addresses of recipients who marked your messages as a spam (for ESPs that support FBL).

### Import complaint list

 - [POST /v3/{domain_name}/complaints/import](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/complaints/post-v3--domainid--complaints-import.md): Import a CSV file containing a list of addresses to add to the complaint list. The CSV file must be 25MB or under and can contain the following column headers: address, created_at. address is a valid email address (required). created_at is timestamp of complaint event in RFC2822 format (optional, default: current time)

### Lookup complaint record

 - [GET /v3/{domain_name}/complaints/{address}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/complaints/get-v3--domainid--complaints--address-.md): Fetch a single complaint records to check if a given address is present in the list of complaints.

### Remove complaint

 - [DELETE /v3/{domain_name}/complaints/{address}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/complaints/delete-v3--domainid--complaints--address-.md): Delivery to the deleted email address resumes until there is another complaint.

### List all complaints

 - [GET /v3/{domain_name}/complaints](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/complaints/get-v3--domainid--complaints.md): Paginate a list of complaints for the domain.

### Add complaints

 - [POST /v3/{domain_name}/complaints](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/complaints/post-v3--domainid--complaints.md): Request body is expected to be a valid JSON encoded sting containing up to 1000 complaint records or a single complaint record as application/form-data

### Clear all complaints

 - [DELETE /v3/{domain_name}/complaints](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/complaints/delete-v3--domainid--complaints.md): Clears all email addresses with complaints from the domain. Delivery to the deleted email addresses will longer be suppressed.

## Bounces

Bounces - Bounce list stores events of delivery failures due to permanent recipient mailbox errors such as non-existent mailbox. Soft bounces (for example, mailbox is full) and other failures (for example, ESP rejects an email because it thinks it is spam) are not added to the list.

### Import list of bounces

 - [POST /v3/{domain_name}/bounces/import](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/bounces/post-v3--domainid--bounces-import.md): Import a CSV file containing a list of addresses to add to the bounce list. The CSV file must be 25MB or under and must contain the following column headers: address, code, error, created_at. address is a valid email address. code is error code (optional, default: 550). error is error description (optional, default: empty string). created_at is timestamp of bounce event in RFC2822 format (optional, default: current time)

### Lookup bounce record

 - [GET /v3/{domain_name}/bounces/{address}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/bounces/get-v3--domainid--bounces--address-.md): Fetch a single bounce event by a given email address.

### Remove bounce

 - [DELETE /v3/{domain_name}/bounces/{address}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/bounces/delete-v3--domainid--bounces--address-.md): Delivery to the deleted email address resumes until it bounces again.

### List all bounces

 - [GET /v3/{domain_name}/bounces](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/bounces/get-v3--domainid--bounces.md): Paginate over a list of bounces for a domain.

### Add bounces

 - [POST /v3/{domain_name}/bounces](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/bounces/post-v3--domainid--bounces.md): Request body is expected to be a valid JSON encoded sting containing up to 1000 bounce records or a single bounce record as application/form-data

### Clear all bounces

 - [DELETE /v3/{domain_name}/bounces](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/bounces/delete-v3--domainid--bounces.md): Clears all email addresses with bounces from the domain. Delivery to the deleted email addresses will longer be suppressed.

## Allowlist

The allowlist API provides the ability to allowlist specific addresses from being added to bounce list. You can allowlist by domain name (i.e example.com) or by specific address (i.e. alice@example.com). Mailgun doesnât add an address to bounce list if the address is allowlisted. This API is very useful if you test against your private services and donât want to constantly clean up bounce lists

### Import allowlist

 - [POST /v3/{domain_name}/whitelists/import](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/allowlist/post-v3--domainid--whitelists-import.md): Import a CSV file containing a list of addresses and/or domains to add to the allowlist. The CSV file must be 25MB or under and must contain the following column headers: address, domain. For each row provide either an address or a domain, but not both - choose one, keep the other blank.

### Lookup allowlist record

 - [GET /v3/{domain_name}/whitelists/{value}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/allowlist/get-v3--domainid--whitelists--value-.md): Fetch a single allowlist record to check if a given address or domain is present.

### Remove entry from allowlist

 - [DELETE /v3/{domain_name}/whitelists/{value}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/allowlist/delete-v3--domainid--whitelists--value-.md): Remove a single entry from the allowlist

### List allowlist records for domain

 - [GET /v3/{domain_name}/whitelists](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/allowlist/get-v3--domainid--whitelists.md): Paginate over  all allowlist records for a domain.

### Add allowlist record

 - [POST /v3/{domain_name}/whitelists](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/allowlist/post-v3--domainid--whitelists.md): Add an address or domain to the allowlist table

### Clear allowlist

 - [DELETE /v3/{domain_name}/whitelists](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/allowlist/delete-v3--domainid--whitelists.md): Delete an entire allowlist for a domain

## Routes

Define a list of routes to handle incoming emails. When a message matches a route expression, Mailgun can forward it on to your application via HTTP or another email address, or store the message temporarily (3 days) for subsequent retrieval.

### Create a route

 - [POST /v3/routes](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/routes/post-v3-routes.md): Adds a new route to the account

### Get all routes

 - [GET /v3/routes](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/routes/get-v3-routes.md): Get the list of routes. Note that routes are defined globally, per account, not per domain.

### Get a route

 - [GET /v3/routes/{id}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/routes/get-v3-routes-id.md): Returns a detailed view of the route

### Update a route

 - [PUT /v3/routes/{id}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/routes/put-v3-routes-id.md): Updates a given route. All parameters are optional. This only updates the specified fields, leaving others unchanged.

### Delete a route

 - [DELETE /v3/routes/{id}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/routes/delete-v3-routes-id.md): Remove the rotue from the account.

### Match address to route

 - [GET /v3/routes/match](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/routes/get-v3-routes-match.md): Checks if an address matches at least one route.

## Mailing Lists

Programatically create mailing lists.

### Create a mailing list

 - [POST /v3/lists](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/mailing-lists/post-v3-lists.md): Adds a mailing list to the account.

### Get mailing lists

 - [GET /v3/lists](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/mailing-lists/get-v3-lists.md): A mailing list is a group of members (recipients) which itself has an email address. This address becomes an ID for this mailing list.

### Get mailing lists members

 - [GET /v3/lists/{list_address}/members](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/mailing-lists/get-lists-string:list_address-members.md): Lists members in a given mailing list

### Create a mailing list member

 - [POST /v3/lists/{list_address}/members](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/mailing-lists/post-lists-string:list_address-members.md): Adds a new member to the mailing list.  For adding many list members, consider bulk upload endpoints "POST /v3/lists/{list_address}/members.json" or "members.csv".

### Bulk upload members to a mailing list (JSON)

 - [POST /v3/lists/{list_address}/members.json](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/mailing-lists/post-lists-list_address-members.json.md): Adds multiple members, up to 1000 per call, to a mailing list, using JSON array format.
If the request includes more than 100 entries, the mailing list will be updated asynchronously.


### Bulk upload members to a mailing list (CSV)

 - [POST /v3/lists/{list_address}/members.csv](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/mailing-lists/post-lists-list_address-members.csv.md): Adds multiple members, up to 1000 per call, to a mailing list via CSV file.

### Get a member

 - [GET /v3/lists/{list_address}/members/{member_address}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/mailing-lists/get-lists-list_address-members-member_address.md): Get details about a specific mailing list member

### Update a mailing list member

 - [PUT /v3/lists/{list_address}/members/{member_address}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/mailing-lists/put-lists-list_address-members-member_address.md): Updates a mailing list member with the given properties. Existing properties not included in the request will not be changed.

### Delete a member

 - [DELETE /v3/lists/{list_address}/members/{member_address}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/mailing-lists/delete-lists-list_address-members-member_address.md): Deletes a member from a mailing list

### Update a mailing list

 - [PUT /v3/lists/{list_address}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/mailing-lists/put-v3-lists-address.md): Update mailing list properties, such as address, description or name

### Delete a mailing list

 - [DELETE /v3/lists/{list_address}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/mailing-lists/delete-v3-lists-address.md): Deletes a mailing list

### Get a mailing list by address

 - [GET /v3/lists/{list_address}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/mailing-lists/get-v3-lists-address.md): Returns the matching mailing list for the given address

### Get mailing lists by page

 - [GET /v3/lists/pages](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/mailing-lists/get-v3-lists-pages.md): Paginate over mailing lists

### Get members by page

 - [GET /v3/lists/{list_address}/members/pages](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/mailing-lists/get-lists-list_address-members-pages.md): Paginate over list members in a given mailing list in ascending order

## Templates

This API allows you to store predefined templates and use them to send messages using the Sending API.

### Get templates

 - [GET /v3/{domain_name}/templates](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/templates/get-v3--domain-name--templates.md): Returns a list of templates for the domain.

### Create a template

 - [POST /v3/{domain_name}/templates](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/templates/post-v3--domain-name--templates.md): Store a new template, including its name, description and (optionally) the template content. If the template content is provided, a new version is automatically created and becomes the active version.

### Delete all templates

 - [DELETE /v3/{domain_name}/templates](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/templates/delete-v3--domain-name--templates.md): Delete all templates and their versions for the domain.

### Get all template versions

 - [GET /v3/{domain_name}/templates/{template_name}/versions](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/templates/get-v3--domain-name--templates--template-name--versions.md): Returns a paginated list of template versions.

### Create a template version

 - [POST /v3/{domain_name}/templates/{template_name}/versions](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/templates/post-v3--domain-name--templates--template-name--versions.md): Adds a new template version. If the template doesnât contain any other versions, the first version becomes active. A template can store up to 40 versions.

### Get template

 - [GET /v3/{domain_name}/templates/{template_name}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/templates/get-v3--domain-name--templates--template-name-.md): Returns metadata information about the stored template specified in the url. If the active flag is provided, the content of the active version of the template is returned. If the version_name flag is provided, version information will be included as well. By default: the  field is not provided. To see available versions other than the active version, use the  API instead

### Update template

 - [PUT /v3/{domain_name}/templates/{template_name}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/templates/put-v3--domain-name--templates--template-name-.md): Update the description of a template.

### Delete a template

 - [DELETE /v3/{domain_name}/templates/{template_name}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/templates/delete-v3--domain-name--templates--template-name-.md): Delete the template specified in the url. NOTE: This method deletes all versions of the specified template.

### Get a version

 - [GET /v3/{domain_name}/templates/{template_name}/versions/{version_name}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/templates/get-v3--domain-name--templates--template-name--versions--version-name-.md): Retrieve the information and content of the specified version of a template.

### Update a version

 - [PUT /v3/{domain_name}/templates/{template_name}/versions/{version_name}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/templates/put-v3--domain-name--templates--template-name--versions--version-name-.md): Update information or content of the specific template version. Existing fields not included in the request will not be changed

### Delete a version

 - [DELETE /v3/{domain_name}/templates/{template_name}/versions/{version_name}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/templates/delete-v3--domain-name--templates--template-name--versions--version-name-.md): Delete a specific template version.

### Copy a version

 - [PUT /v3/{domain_name}/templates/{template_name}/versions/{version_name}/copy/{new_version_name}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/templates/put-v3--domain-name--templates--template-name--versions--version-name--copy--new-version-name-.md): Copies an existing version into a new version with the provided name.

## IPs

The IP API endpoint allows you to access information regarding the IPs allocated to your Mailgun account that are used for outbound sending.

### Remove an IP from the domain pool, unlink a DIPP or remove the domain pool

 - [DELETE /v3/domains/{name}/ips/{ip}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/ip-pools/delete-v3-domains--name--ips--ip-.md): The behavior of the endpoint depends on the value of the  parameter. It can be
one of the following:
 * a valid IP address: this IP address will be removed from the domain pool.
 * string : the entire domain pool will be removed. As far as the system is
   concerned, such domain will no longer exist.
 * string : the DIPP which is currently linked to the domain will be
   unlinked.

### Removing An IP
Note that it's impossible to alter domain IPs if a DIPP is linked to the domain.

If the account is not eligible for shared IPs, additional rules apply:
 * removing the last IP from the domain is not allowed;
 * if all of the remaining dedicated IPs are on warmup, an extra IP might be added to
   the domain pool.

### Unlinking The DIPP
The account must have 'DIPPs' feature enabled.

Either  or  query parameter must be specified, but not both.

If the special value  is used for the replacement IP, the account must be
eligible for shared IPs. In this case the system will assign a shared IP as the
replacement.

### Remove an IP from the domain pool, unlink a DIPP or remove the domain pool

 - [DELETE /v3/domains/{name}/pool/{ip}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/ip-pools/delete-v3-domains--name--pool--ip-.md): The behavior of the endpoint depends on the value of the  parameter. It can be
one of the following:
 * a valid IP address: this IP address will be removed from the domain pool.
 * string : the entire domain pool will be removed. As far as the system is
   concerned, such domain will no longer exist.
 * string : the DIPP which is currently linked to the domain will be
   unlinked.

### Removing An IP
Note that it's impossible to alter domain IPs if a DIPP is linked to the domain.

If the account is not eligible for shared IPs, additional rules apply:
 * removing the last IP from the domain is not allowed;
 * if all of the remaining dedicated IPs are on warmup, an extra IP might be added to
   the domain pool.

### Unlinking The DIPP
The account must have 'DIPPs' feature enabled.

Either  or  query parameter must be specified, but not both.

If the special value  is used for the replacement IP, the account must be
eligible for shared IPs. In this case the system will assign a shared IP as the
replacement.

### Remove an IP from the domain pool, unlink a DIPP or remove the domain pool

 - [DELETE /v3/domains/{name}/ips/{ip}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/ips/delete-v3-domains--name--ips--ip-.md): The behavior of the endpoint depends on the value of the  parameter. It can be
one of the following:
 * a valid IP address: this IP address will be removed from the domain pool.
 * string : the entire domain pool will be removed. As far as the system is
   concerned, such domain will no longer exist.
 * string : the DIPP which is currently linked to the domain will be
   unlinked.

### Removing An IP
Note that it's impossible to alter domain IPs if a DIPP is linked to the domain.

If the account is not eligible for shared IPs, additional rules apply:
 * removing the last IP from the domain is not allowed;
 * if all of the remaining dedicated IPs are on warmup, an extra IP might be added to
   the domain pool.

### Unlinking The DIPP
The account must have 'DIPPs' feature enabled.

Either  or  query parameter must be specified, but not both.

If the special value  is used for the replacement IP, the account must be
eligible for shared IPs. In this case the system will assign a shared IP as the
replacement.

### Remove an IP from the domain pool, unlink a DIPP or remove the domain pool

 - [DELETE /v3/domains/{name}/pool/{ip}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/ips/delete-v3-domains--name--pool--ip-.md): The behavior of the endpoint depends on the value of the  parameter. It can be
one of the following:
 * a valid IP address: this IP address will be removed from the domain pool.
 * string : the entire domain pool will be removed. As far as the system is
   concerned, such domain will no longer exist.
 * string : the DIPP which is currently linked to the domain will be
   unlinked.

### Removing An IP
Note that it's impossible to alter domain IPs if a DIPP is linked to the domain.

If the account is not eligible for shared IPs, additional rules apply:
 * removing the last IP from the domain is not allowed;
 * if all of the remaining dedicated IPs are on warmup, an extra IP might be added to
   the domain pool.

### Unlinking The DIPP
The account must have 'DIPPs' feature enabled.

Either  or  query parameter must be specified, but not both.

If the special value  is used for the replacement IP, the account must be
eligible for shared IPs. In this case the system will assign a shared IP as the
replacement.

### List account IPs

 - [GET /v3/ips](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/ips/get-v3-ips.md):  in response lists which IPs can be assigned to DIPPs; this
field is present only if the account has 'DIPPs' feature enabled.

 contains the number of items returned in  (this depends on the
filters applied).

### Get details about account IP

 - [GET /v3/ips/{ip}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/ips/get-v3-ips--ip-.md)

### Get all domains of an account where a specific IP is assigned

 - [GET /v3/ips/{ip}/domains](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/ips/get-v3-ips--ip--domains.md): The IP must belong to the account.

Matching domains are ordered by increasing id, then the  and  parameters
are applied.

If the  parameter is present, it is used to limit the results to domains
whose names match the search query. The search query is split into words by 
whitespace and punctuation, then the logical OR is applied.

### Assign an IP to all account domains

 - [POST /v3/ips/{ip}/domains](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/ips/post-v3-ips--ip--domains.md): The IP must belong to the account.

### Remove an IP from all account domains

 - [DELETE /v3/ips/{ip}/domains](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/ips/delete-v3-ips--ip--domains.md): The IP must belong to the account.

If the  parameter is present, it is used to replace the removed ip on all domains.

### Place account IP into a dedicated IP band

 - [POST /v3/ips/{addr}/ip_band](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/ips/post-v3-ips--addr--ip-band.md): The  feature must be enabled for the account.

The IP must be a dedicated one belonging to the account.

### Return the number of IPs available to the account per its billing plan

 - [GET /v3/ips/request/new](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/ips/get-v3-ips-request-new.md): This endpoint remains active for backwards compatibility. Do not use it in new code.

Field  in the response is deprecated and should not be used.

### Add a new dedicated IP to the account

 - [POST /v3/ips/request/new](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/ips/post-v3-ips-request-new.md): A new IP can be assigned only if billing limits allow that.

## IP Pools

IP Pools allow you to group your dedicated IPs into customized "pools" to help manage your sending reputation for different mail sending streams.

### Remove an IP from the domain pool, unlink a DIPP or remove the domain pool

 - [DELETE /v3/domains/{name}/ips/{ip}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/ip-pools/delete-v3-domains--name--ips--ip-.md): The behavior of the endpoint depends on the value of the  parameter. It can be
one of the following:
 * a valid IP address: this IP address will be removed from the domain pool.
 * string : the entire domain pool will be removed. As far as the system is
   concerned, such domain will no longer exist.
 * string : the DIPP which is currently linked to the domain will be
   unlinked.

### Removing An IP
Note that it's impossible to alter domain IPs if a DIPP is linked to the domain.

If the account is not eligible for shared IPs, additional rules apply:
 * removing the last IP from the domain is not allowed;
 * if all of the remaining dedicated IPs are on warmup, an extra IP might be added to
   the domain pool.

### Unlinking The DIPP
The account must have 'DIPPs' feature enabled.

Either  or  query parameter must be specified, but not both.

If the special value  is used for the replacement IP, the account must be
eligible for shared IPs. In this case the system will assign a shared IP as the
replacement.

### Remove an IP from the domain pool, unlink a DIPP or remove the domain pool

 - [DELETE /v3/domains/{name}/pool/{ip}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/ip-pools/delete-v3-domains--name--pool--ip-.md): The behavior of the endpoint depends on the value of the  parameter. It can be
one of the following:
 * a valid IP address: this IP address will be removed from the domain pool.
 * string : the entire domain pool will be removed. As far as the system is
   concerned, such domain will no longer exist.
 * string : the DIPP which is currently linked to the domain will be
   unlinked.

### Removing An IP
Note that it's impossible to alter domain IPs if a DIPP is linked to the domain.

If the account is not eligible for shared IPs, additional rules apply:
 * removing the last IP from the domain is not allowed;
 * if all of the remaining dedicated IPs are on warmup, an extra IP might be added to
   the domain pool.

### Unlinking The DIPP
The account must have 'DIPPs' feature enabled.

Either  or  query parameter must be specified, but not both.

If the special value  is used for the replacement IP, the account must be
eligible for shared IPs. In this case the system will assign a shared IP as the
replacement.

### List dedicated IP pools of the account

 - [GET /v3/ip_pools](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/ip-pools/get-v3-ip-pools.md): #### Description
Lists all dedicated IP pools of the account. For each pool
returns its basic properties (name, description, the list of IPs)
and indicates whether the pool is linked to any domains and
whether it's an inherited one. Only one pool can be inherited
from the parent account.

### Add a new DIPP to the account

 - [POST /v3/ip_pools](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/ip-pools/post-v3-ip-pools.md): The account must have 'DIPPs' feature enabled.

Returns the id of the newly created DIPP.

### Get DIPP details

 - [GET /v3/ip_pools/{pool_id}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/ip-pools/get-v3-ip-pools--pool-id-.md):  in the response indicates whether the DIPP is currently linked to any
domains. If it's ,  lists those domains.

### Delete the DIPP

 - [DELETE /v3/ip_pools/{pool_id}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/ip-pools/delete-v3-ip-pools--pool-id-.md): The  feature must be enabled for the account.

It is not allowed to delete a DIPP inherited from the parent account.

If the DIPP is delegated to subaccounts, those will also be updated.

If the replacement DIPP is specified, all domains linked to the deleted DIPP will be
relinked to the replacement DIPP. The latter must contain at least one IP.

If the replacement IP is specified, all domains linked to the deleted DIPP will be
unlinked, and the replacement IP will be assigned to them. It is not allowed to
delete a DIPP inherited from the parent account and replace it with an IP
(subaccounts do not explicitly manage their IPs).

The replacement IP must be a dedicated one; it can't belong to another DIPP. If a
special value  is used, appropriate shared IPs will be used (the account must
be eligible for shared IPs in this case).

Omitting both replacement DIPP and replacement IP is allowed only if the DIPP being
deleted contains no IPs.

The processing of affected domains and subaccounts happens asynchronously after the
endpoint returns a response.

### Edit DIPP

 - [PATCH /v3/ip_pools/{pool_id}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/ip-pools/patch-v3-ip-pools--pool-id-.md): The account must have 'DIPPs' feature enabled.

It's not allowed to edit a DIPP inherited from the parent account.

IPs being added to the DIPP must be dedicated ones and belong to the account.

If IPs of the DIPP end up modified, and the DIPP is linked to domains, the domains
will be updated asynchronously (after this endpoint returns response).

Returns an error if the passed parameters won't result in any changes.

### Get domains linked to DIPP

 - [GET /v3/ip_pools/{pool_id}/domains](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/ip-pools/get-v3-ip-pools--pool-id--domains.md): Returns a paginated list of domains that are linked to the specified
dedicated IP pool.

### Add an IP to a DIPP

 - [PUT /v3/ip_pools/{pool_id}/ips/{ip}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/ip-pools/put-v3-ip-pools--pool-id--ips--ip-.md): The account must have 'DIPPs' feature enabled.

It is not allowed to modify a DIPP inherited from the parent account.

The IP must be a dedicated one, belong to the account and not belong to any other
DIPP.

All domains linked to the DIPP will be updated so that their IPs include the newly
added address. If the DIPP is delegated to subaccounts, those will also be updated.

The processing of affected domains and subaccounts happens asynchronously after the
endpoint returns a response.

### Remove an IP from a DIPP

 - [DELETE /v3/ip_pools/{pool_id}/ips/{ip}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/ip-pools/delete-v3-ip-pools--pool-id--ips--ip-.md): The account must have 'DIPPs' feature enabled.

It's not allowed to edit a DIPP inherited from the parent account.

If the DIPP is linked to domains, the domains will be updated asynchronously (after
this endpoint returns response).

### Add multiple IPs to the DIPP

 - [POST /v3/ip_pools/{pool_id}/ips.json](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/ip-pools/post-v3-ip-pools--pool-id--ips-json.md): The account must have 'DIPPs' feature enabled.

It is not allowed to modify a DIPP inherited from the parent account.

All IPs must be dedicated ones, belong to the account and not belong to any other
DIPP.

All domains linked to the DIPP will be updated so that their IPs include the newly
added addresses. If the DIPP is delegated to subaccounts, those will also be updated.

The processing of affected domains and subaccounts happens asynchronously after the
endpoint returns a response.

### Remove an IP from the domain pool, unlink a DIPP or remove the domain pool

 - [DELETE /v3/domains/{name}/ips/{ip}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/ips/delete-v3-domains--name--ips--ip-.md): The behavior of the endpoint depends on the value of the  parameter. It can be
one of the following:
 * a valid IP address: this IP address will be removed from the domain pool.
 * string : the entire domain pool will be removed. As far as the system is
   concerned, such domain will no longer exist.
 * string : the DIPP which is currently linked to the domain will be
   unlinked.

### Removing An IP
Note that it's impossible to alter domain IPs if a DIPP is linked to the domain.

If the account is not eligible for shared IPs, additional rules apply:
 * removing the last IP from the domain is not allowed;
 * if all of the remaining dedicated IPs are on warmup, an extra IP might be added to
   the domain pool.

### Unlinking The DIPP
The account must have 'DIPPs' feature enabled.

Either  or  query parameter must be specified, but not both.

If the special value  is used for the replacement IP, the account must be
eligible for shared IPs. In this case the system will assign a shared IP as the
replacement.

### Remove an IP from the domain pool, unlink a DIPP or remove the domain pool

 - [DELETE /v3/domains/{name}/pool/{ip}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/ips/delete-v3-domains--name--pool--ip-.md): The behavior of the endpoint depends on the value of the  parameter. It can be
one of the following:
 * a valid IP address: this IP address will be removed from the domain pool.
 * string : the entire domain pool will be removed. As far as the system is
   concerned, such domain will no longer exist.
 * string : the DIPP which is currently linked to the domain will be
   unlinked.

### Removing An IP
Note that it's impossible to alter domain IPs if a DIPP is linked to the domain.

If the account is not eligible for shared IPs, additional rules apply:
 * removing the last IP from the domain is not allowed;
 * if all of the remaining dedicated IPs are on warmup, an extra IP might be added to
   the domain pool.

### Unlinking The DIPP
The account must have 'DIPPs' feature enabled.

Either  or  query parameter must be specified, but not both.

If the special value  is used for the replacement IP, the account must be
eligible for shared IPs. In this case the system will assign a shared IP as the
replacement.

## Dynamic IP Pools

Dynamic IP Pools allow you to group your dedicated IPs into customized "pools" based on sender reputation. Domains enrolled in Dynamic IP Pools will be assigned to a pool based on the result of periodic health checks.

### Enroll domain

 - [POST /v3/domains/{name}/dynamic_pools](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/dynamic-ip-pools/post-v3-domains--name--dynamic-pools.md): Domains enrolled in the Dynamic IP pools feature will be assigned an IP pool based on reputation.
The feature must be enabled and configured before enrolling domains.

### Remove domain from dynamic IP pools

 - [DELETE /v3/domains/{name}/dynamic_pools](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/dynamic-ip-pools/delete-v3-domains--name--dynamic-pools.md): The behavior of this endpoint depends on the value of the  and  parameters.
One of these parameters (but not both) must be provided. If  is provided, the IP(s) will be assigned to the domain.
 can include one of the following:
 * valid IP(s): this IP address or addresses will be added to the domain
 * string : if the account is eligible for shared IPs, a suitable shared IP will be chosen and added to the domain
The 'replacement_ip' parameter cannot include any IPs that are already assigned to a Dedicated IP Pool or a Dynamic IP Pool.
If  is provided, the Dedicated IP Pool will be assigned to the domain.

### List assignable domains

 - [GET /v3/domains/dynamic_pools/assignable](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/dynamic-ip-pools/get-v3-domains-dynamic-pools-assignable.md): Lists all domains that are not already enrolled in dynamic IP pools.

### Enroll all account domains

 - [POST /v3/domains/all/dynamic_pools/enroll](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/dynamic-ip-pools/post-v3-domains-all-dynamic-pools-enroll.md): Begins an asynchronous background job to assign all domains to Dynamic IP Pools.
This can also include domains belonging to subaccounts depending on the provided parameters.
The Dynamic IP Pools feature must be enabled for the account and the request must come from a parent account user.

### List all Dynamic IP pools

 - [GET /v3/dynamic_pools](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/dynamic-ip-pools/get-v3-dynamic-pools.md): Returns the list of IPs belonging to each of the account's Dynamic IP Pools.

### Initialize/set IPs for all pools

 - [POST /v3/dynamic_pools/all](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/dynamic-ip-pools/post-v3-dynamic-pools-all.md): Any existing IPs in dynamic IP pools will be replaced. All IPs must be dedicated IPs and
belong to the account. Additionally, each dynamic IP pool must contain at least 1 IP that
is not currently warming.

### Remove all dynamic IP pools

 - [DELETE /v3/dynamic_pools/all](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/dynamic-ip-pools/delete-v3-dynamic-pools-all.md): Removes all dynamic IP pools from the account. All domains on the account (and subaccounts, if any) must be removed from dynamic IP pools before the pools can be removed. Any standard dedicated IP pools will not be modified.

### Add IP to Dynamic IP Pool

 - [POST /v3/dynamic_pools/{pool_name}/{ip}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/dynamic-ip-pools/post-v3-dynamic-pools--pool-name---ip-.md): Adds a given IP to a Dynamic IP Pool. The IP must be dedicated and belong to the account.

### Update pool IPs

 - [PATCH /v3/dynamic_pools/{pool_name}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/dynamic-ip-pools/patch-v3-dynamic-pools--pool-name-.md): Adds and/or removes IPs to/from the specified dynamic IP pool.
A given pool is required to have at least 1 IP that is not
actively warming. Additionally, a single IP cannot be assigned to
multiple dynamic pools.

### List all domains assigned to dynamic IP pools

 - [GET /v1/dynamic_pools/domains](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/dynamic-ip-pools/get-v1-dynamic-pools-domains.md): Retrieves all domains enrolled in dynamic IP pools across the parent account and subaccounts.

### Preview domain assignment

 - [GET /v1/dynamic_pools/domains/{name}/preview](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/dynamic-ip-pools/get-v1-dynamic-pools-domains--name--preview.md): Runs a health check on a domain and returns which pool it would be placed in. It does NOT enroll the domain or set the band

### List domain history

 - [GET /v1/dynamic_pools/domains/{name}/history](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/dynamic-ip-pools/get-v1-dynamic-pools-domains--name--history.md): Retrieves a domain's history records

### Override domain assignment

 - [PUT /v1/dynamic_pools/domains/{name}/override](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/dynamic-ip-pools/put-v1-dynamic-pools-domains--name--override.md): Overrides a domain's dynamic IP pool assignment. A domain's pool will not be updated by health checks while an override is present.

### Remove override

 - [DELETE /v1/dynamic_pools/domains/{name}/override](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/dynamic-ip-pools/delete-v1-dynamic-pools-domains--name--override.md): Removes any dynamic IP pool override for a domain. The domain's pool assignment will be managed by health checks.

### List account history

 - [GET /v1/dynamic_pools/history](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/dynamic-ip-pools/get-v1-dynamic-pools-history.md): Retrieve history records for all domains assigned to Dynamic IP Pools across the parent and subaccounts.

## IP Address Warmup

### Retrieves the list of in-flight IP address warmup statuses.

 - [GET /v3/ip_warmups](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/ip-address-warmup/get-v3-ip-warmups.md): Retrieves a list of in-flight IP warmup statuses for dedicated IP addresses owned by the account. The response includes pagination URLs for navigating through the results.

### Retrieves the status of an in-flight IP warmup

 - [GET /v3/ip_warmups/{addr}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/ip-address-warmup/get-v3-ip-warmups--addr-.md): Retrieves the status of an in-flight IP warmup, which must be a dedicated IP owned by the account.

### Creates a warmup plan for an IP Address

 - [POST /v3/ip_warmups/{addr}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/ip-address-warmup/post-v3-ip-warmups--addr-.md): Creates a new warmup plan for an IP address. The IP must be dedicated and owned by the account.

### Cancels the warmup plan for an IP address

 - [DELETE /v3/ip_warmups/{addr}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/ip-address-warmup/delete-v3-ip-warmups--addr-.md): Cancels the warmup plan for an IP address. The IP must be dedicated and owned by the account.

## Subaccounts

Mailgun supports the creation, modification, and deletion of subaccounts. A subaccount is a child account of a parent account. The parent account can have multiple subaccounts. The subaccounts are created and managed by the parent account.

### Get a single subaccount

 - [GET /v5/accounts/subaccounts/{subaccount_id}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/subaccounts/get-v5-accounts-subaccounts-subaccount_id.md): Fetch the details of a single subaccount

### List all subaccounts

 - [GET /v5/accounts/subaccounts](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/subaccounts/get-v5-accounts-subaccounts.md): Fetch all subaccounts

### Create a subaccount

 - [POST /v5/accounts/subaccounts](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/subaccounts/post-v5-accounts-subaccounts.md): Create a subaccount

### Delete a subaccount

 - [DELETE /v5/accounts/subaccounts](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/subaccounts/delete-v5-accounts-subaccounts-subaccount_id.md): Delete a subaccount

### Disable a subaccount

 - [POST /v5/accounts/subaccounts/{subaccount_id}/disable](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/subaccounts/post-v5-accounts-subaccounts-subaccount_id-disable.md): Disable a subaccount

### Enable a subaccount

 - [POST /v5/accounts/subaccounts/{subaccount_id}/enable](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/subaccounts/post-v5-accounts-subaccounts-subaccount_id-enable.md): Enable a subaccount

### Get current custom sending limit

 - [GET /v5/accounts/subaccounts/{subaccount_id}/limit/custom/monthly](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/subaccounts/get-v5-accounts-subaccounts-subaccount_id-limit-custom-monthly.md): Fetch the details of custom sending limit on the account

### Set a custom sending limit

 - [PUT /v5/accounts/subaccounts/{subaccount_id}/limit/custom/monthly](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/subaccounts/put-v5-accounts-subaccounts-subaccount_id-limit-custom-monthly.md): Set a custom sending limit

### Delete a custom sending limit

 - [DELETE /v5/accounts/subaccounts/{subaccount_id}/limit/custom/monthly](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/subaccounts/delete-v5-accounts-subaccounts-subaccount_id-limit-custom-monthly.md): Delete a custom sending limit

### Update subaccount feature

 - [PUT /v5/accounts/subaccounts/{subaccount_id}/features](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/subaccounts/put-v5-accounts-subaccounts-subaccount_id-features.md): Update subaccount feature

## Custom Message Limit

The custom message limit imposes a hard limit on how many messages your account can send during a calendar month.

### Get current custom sending limit

 - [GET /v5/accounts/limit/custom/monthly](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/custom-message-limit/get-v5-accounts-limit-custom-monthly.md): Fetch the details of custom sending limit on the account

### Set a custom sending limit

 - [PUT /v5/accounts/limit/custom/monthly](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/custom-message-limit/put-v5-accounts-limit-custom-monthly.md): Set a custom sending limit

### Delete a custom sending limit

 - [DELETE /v5/accounts/limit/custom/monthly](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/custom-message-limit/delete-v5-accounts-limit-custom-monthly.md): Delete a custom sending limit

### Re-enable account disabled for hitting send limit

 - [PUT /v5/accounts/limit/custom/enable](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/custom-message-limit/put-v5-accounts-limit-custom-enable.md): Re-enable an account that was disabled for reaching the custom sending limit

## Account Management

Perform account-level CRUD operations.

### Update variable account settings

 - [PUT /v5/accounts](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/account-management/put-v5-accounts.md): Update variable account settings

### Get webhook signing key saved on the account

 - [GET /v5/accounts/http_signing_key](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/account-management/get-v5-accounts-http_signing_key.md): Get webhook signing key saved on the account

### Create or regenerate webhook signing key on an account

 - [POST /v5/accounts/http_signing_key](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/account-management/post-v5-accounts-http_signing_key.md): Create or regenerate webhook signing key on an account

### Get authorized email recipients for a sandbox domain

 - [GET /v5/sandbox/auth_recipients](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/account-management/get-v5-sandbox-auth_recipients.md): Get webhook signing key saved on the account

### Add authorized email recipient for a sandbox domain

 - [POST /v5/sandbox/auth_recipients](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/account-management/post-v5-sandbox-auth_recipients.md): Add authorized email recipient for a sandbox domain

### Remove an authorized sandbox domain email recipient

 - [DELETE /v5/sandbox/auth_recipients/{email}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/account-management/delete-v5-sandbox-auth_recipients-email.md): Remove an authorized sandbox domain email recipient

### Resend account activation email to the account owner

 - [POST /v5/accounts/resend_activation_email](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/account-management/post-v5-accounts-resend_activation_email.md): Resend account activation email to the account owner

## Keys

The Keys API lets you view and manage API keys.

### List Mailgun API keys

 - [GET /v1/keys](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/keys/get-v1-keys.md): List Mailgun API keys

### Create Mailgun API key

 - [POST /v1/keys](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/keys/post-v1-keys.md): Create Mailgun API key

### Delete Mailgun API key

 - [DELETE /v1/keys/{key_id}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/keys/delete-v1-keys--key-id-.md): Delete Mailgun API key

### Regenerate Mailgun Public API key

 - [POST /v1/keys/public](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/keys/post-v1-keys-public.md): Regenerate Mailgun Public API key

## Credentials

The Credentials API lets you view and manage SMTP credentials.

### List Mailgun SMTP credential metadata for a given domain

 - [GET /v3/domains/{domain_name}/credentials](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/credentials/get-v3-domains--domain-name--credentials.md): List Mailgun SMTP credential metadata for a given domain

### Create Mailgun SMTP credentials for a given domain

 - [POST /v3/domains/{domain_name}/credentials](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/credentials/post-v3-domains--domain-name--credentials.md): Create Mailgun SMTP credentials for a given domain

### Delete all Mailgun SMTP credentials for a domain

 - [DELETE /v3/domains/{domain_name}/credentials](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/credentials/delete-v3-domains--domain-name--credentials.md): Delete Mailgun SMTP credentials for a given domain

### Update Mailgun SMTP credentials

 - [PUT /v3/domains/{domain_name}/credentials/{spec}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/credentials/put-v3-domains--domain-name--credentials--spec-.md): Update Mailgun SMTP credentials for a given domain and SMTP user

### Delete Mailgun SMTP credentials

 - [DELETE /v3/domains/{domain_name}/credentials/{spec}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/credentials/delete-v3-domains--domain-name--credentials--spec-.md): Delete Mailgun SMTP credentials for a given domain and SMTP user

## IP Allowlist

The IP Allowlist API lets you view and manage allowlisted IP addresses to which API key and SMTP credential usage is restricted.

### List Mailgun account IP allowlist entries

 - [GET /v2/ip_whitelist](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/ip-allowlist/get-v2-ip-whitelist.md): List Mailgun account IP allowlist entries

### Update individual Mailgun account IP allowlist entry's description

 - [PUT /v2/ip_whitelist](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/ip-allowlist/put-v2-ip-whitelist.md): Update individual Mailgun account IP allowlist entry's description

### Add Mailgun account IP allowlist entry

 - [POST /v2/ip_whitelist](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/ip-allowlist/post-v2-ip-whitelist.md): Add Mailgun account IP allowlist entry

### Delete Mailgun account IP allowlist entry

 - [DELETE /v2/ip_whitelist](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/ip-allowlist/delete-v2-ip-whitelist.md): Delete Mailgun account IP allowlist entry

## Users

Mailgun API supports viewing user entities.

### Get users on an account

 - [GET /v5/users](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/users/get-v5-users.md): Get users on an account

### Get a user's details

 - [GET /v5/users/{user_id}](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/users/get-v5-users-user_id.md): Get details for a user on the account

### Get one's own user details

 - [GET /v5/users/me](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/users/get-v5-users-me.md): Get one's own user details, requires use of an API key with a  saved on it, typically of 'web' kind


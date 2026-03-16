# Source: https://scrapfly.io/docs/crawler-api/webhook

Title: | Scrapfly

URL Source: https://scrapfly.io/docs/crawler-api/webhook

Markdown Content:
Webhook
-------

Scrapfly's [webhook](https://scrapfly.io/docs/crawler-api/getting-started#webhook_name) feature is ideal for managing crawler jobs asynchronously. When webhook is specified through the `webhook_name` parameter, Scrapfly will notify your HTTP endpoint about crawl events in real-time, eliminating the need for polling.

To start using webhooks, first one must be created using the [webhook web interface](https://scrapfly.io/dashboard/webhook).

webhook management page

The webhook will be called for each event you subscribe to during the crawl lifecycle. For reconciliation, you will receive the `crawler_uuid` and `webhook_uuid` in the [response headers](https://scrapfly.io/docs/crawler-api/webhook#headers).

webhook status report on monitoring log page

> **Webhook Queue Size**
> The webhook queue size indicates the maximum number of queued webhooks that can be scheduled. After the crawler event is processed and your application is notified, the queue size is reduced. This allows you to schedule additional crawler jobs beyond the concurrency limit of your subscription. The scheduler will handle this and ensure that your concurrency limit is met.
> 
> 
> | ###### FREE $0.00/mo | ###### DISCOVERY $30.00/mo | ###### PRO $100.00/mo | ###### STARTUP $250.00/mo | ###### ENTERPRISE $500.00/mo |
> | --- | --- | --- | --- | --- |
> | 0 | 500 | 2,000 | 5,000 | 10,000 |

[See in Your Dashboard](https://scrapfly.io/dashboard/webhook)

[Scope](https://scrapfly.io/docs/crawler-api/webhook#scope)
-----------------------------------------------------------

Webhooks are scoped per Scrapfly [projects](https://scrapfly.io/docs/project) and environments. Make sure to create a webhook for each of your projects and environments (test/live).

[Usage](https://scrapfly.io/docs/crawler-api/webhook#api)
---------------------------------------------------------

> Webhooks can be used for multiple purposes. In the context of the Crawler API, to ensure you received a crawler event, you must check the header `X-Scrapfly-Webhook-Resource-Type`and verify the value is `crawler`.

To enable webhook callbacks, specify the `webhook_name` parameter in your crawler requests and optionally provide a list of `webhook_events` you want to be notified about. Scrapfly will then call your webhook endpoint as crawl events occur.

Note that your webhook endpoint must respond with a `2xx` status code for the webhook to be considered successful. The `3xx` redirect responses will be followed, and response codes `4xx` and `5xx` are considered failures and will be retried as per the retry policy.

> The below examples assume you have a webhook named **my-crawler-webhook**registered. You can create webhooks via the [web dashboard](https://scrapfly.io/dashboard/webhook).

[Webhook Events & Payloads](https://scrapfly.io/docs/crawler-api/webhook#events)
--------------------------------------------------------------------------------

The Crawler API supports multiple webhook events that notify you about different stages of the crawl lifecycle. Each event sends a JSON payload with the crawler state and event-specific data.

> **Default Subscription**
> If you don't specify `webhook_events`, you'll receive: `crawler_started`, `crawler_stopped`, `crawler_cancelled`, and `crawler_finished`.

Every webhook request includes these HTTP headers for easy routing and verification:

| Header | Purpose | Example Value |
| --- | --- | --- |
| `X-Scrapfly-Crawl-Event-Name` | **Fast routing** - Use this to route events without parsing JSON | `crawler_started` |
| `X-Scrapfly-Webhook-Resource-Type` | Resource type (always `crawler` for crawler webhooks) | `crawler` |
| `X-Scrapfly-Webhook-Job-Id` | Crawler UUID for tracking and reconciliation | `550e8400-e29b...` |
| `X-Scrapfly-Webhook-Signature` | HMAC-SHA256 signature for verification | `a3f2b1c...` |

### [Event Types & Examples](https://scrapfly.io/docs/crawler-api/webhook#event-types)

Click each tab below to see the event description and full JSON payload example:

##### crawler_started

**When:** Crawler execution begins

**Use case:** Track when crawls start, log crawler UUID, initialize tracking systems

**Frequency:** Once per crawl

> **Key Fields:**`crawler_uuid`, `seed_url`, `links.status`

```
{
    "event": "crawler_started",
    "payload": {
        "crawler_uuid": "60cf1121-9de4-43fc-a0c6-7dda1721a65b",
        "project": "default",
        "env": "LIVE",
        "seed_url": "https://web-scraping.dev/products",
        "action": "started",
        "state": {
            "duration": 1,
            "urls_visited": 0,
            "urls_extracted": 0,
            "urls_failed": 0,
            "urls_skipped": 0,
            "urls_to_crawl": 0,
            "api_credit_used": 0,
            "stop_reason": null,
            "start_time": 1762939798,
            "stop_time": 1762939799
        },
        "links": {
            "status": "https://api.scrapfly.io/crawl/60cf1121-9de4-43fc-a0c6-7dda1721a65b/status"
        }
    }
}
```

##### crawler_url_visited

**When:** Each URL is successfully crawled

**Use case:** Real-time progress tracking, streaming results, monitoring performance

**Frequency:**High - Fires for every successfully crawled URL (can be thousands per crawl)

> **Performance Warning:**Your endpoint must handle high throughput. Use `X-Scrapfly-Crawl-Event-Name`header for fast routing without parsing JSON body.

```
{
    "event": "crawler_url_visited",
    "payload": {
        "crawler_uuid": "60cf1121-9de4-43fc-a0c6-7dda1721a65b",
        "project": "default",
        "env": "LIVE",
        "url": "https://web-scraping.dev/products",
        "action": "visited",
        "state": {
            "duration": 1,
            "urls_visited": 0,
            "urls_extracted": 0,
            "urls_failed": 0,
            "urls_skipped": 0,
            "urls_to_crawl": 0,
            "api_credit_used": 1,
            "stop_reason": null,
            "start_time": 1762939798,
            "stop_time": 1762939799
        },
        "scrape": {
            "status_code": 200,
            "country": "de",
            "log_uuid": "01K9VPD22494F0ZEX7DGEZQ4ES",
            "log_url": "https://scrapfly.io/dashboard/monitoring/log/01K9VPD22494F0ZEX7DGEZQ4ES",
            "content": {
                "html": "[...]",
                "text": "[...]"
                ...
            }
        }
    }
}
```

##### crawler_url_failed

**When:** A URL fails to crawl (network error, timeout, block, etc.)

**Use case:** Error monitoring, retry logic, debugging failed scrapes

**Frequency:** Per failed URL

> **Debugging Features:**
> *   `error` - Error code for classification
> *   `links.log` - Direct link to scrape log for debugging
> *   `scrape_config` - Complete configuration to replay the scrape
> *   `links.scrape` - Ready-to-use retry URL with same configuration

```
{
    "event": "crawler_url_failed",
    "payload": {
        "state": {
            "duration": 3,
            "urls_visited": 0,
            "urls_extracted": 0,
            "urls_failed": 0,
            "urls_skipped": 0,
            "urls_to_crawl": 0,
            "api_credit_used": 0,
            "stop_reason": null,
            "start_time": 1762944028,
            "stop_time": 1762944031
        },
        "action": "failed",
        "crawler_uuid": "5caa5439-03a4-4c74-9a4c-0597e190dd72",
        "project": "default",
        "env": "LIVE",
        "url": "https://web-scraping.dev/products",
        "error": "ERR::SCRAPE::NETWORK_ERROR",
        "scrape_config": {
            "method": "GET",
            "url": "https://web-scraping.dev/products",
            "body": null,
            "project": "default",
            "env": "LIVE",
            "render_js": false,
            "rendering_timeout": 0,
            "asp": false,
            "proxy_pool": null,
            "country": "de",
            "headers": {},
            "format": "raw",
            "retry": true,
            "correlation_id": "5caa5439-03a4-4c74-9a4c-0597e190dd72",
            "tags": [
                "crawler"
            ],
            "wait_for_selector": null,
            "cache": false,
            "cache_ttl": 86400,
            "cache_clear": false,
            "geolocation": null,
            "screenshot_api_cost": 60,
            "screenshot_flags": null,
            "format_options": [],
            "auto_scroll": false,
            "js_scenario": null,
            "screenshots": {},
            "lang": null,
            "os": null,
            "js": null,
            "rendering_stage": "complete",
            "extraction_prompt": null,
            "extraction_model": null,
            "extraction_model_custom_schema": null,
            "extraction_template": null
        },
        "links": {
            "log": "https://api.scrapfly.io/crawl/5caa5439-03a4-4c74-9a4c-0597e190dd72/logs?url=https://web-scraping.dev/products"
        }
    }
}
```

##### crawler_url_skipped

**When:** URLs are skipped (already visited, filtered, depth limit, etc.)

**Use case:** Monitor filtering effectiveness, track duplicate discovery

**Frequency:** Per batch of skipped URLs

> **Key Fields:**`urls`contains a map of each skipped URL to its skip reason

```
{
    "event": "crawler_url_skipped",
    "payload": {
        "state": {
            "duration": 2,
            "urls_visited": 1,
            "urls_extracted": 22,
            "urls_failed": 0,
            "urls_skipped": 21,
            "urls_to_crawl": 1,
            "api_credit_used": 3,
            "stop_reason": "page_limit",
            "start_time": 1762940028,
            "stop_time": 1762940030
        },
        "action": "skipped",
        "crawler_uuid": "b4867c50-318c-47cd-bfc9-bed67f24771a",
        "project": "default",
        "env": "LIVE",
        "urls": {
            "https://web-scraping.dev/product/2?variant=one": "page_limit",
            "https://web-scraping.dev/product/25": "page_limit",
            "https://web-scraping.dev/product/15": "page_limit",
            "https://web-scraping.dev/product/9": "page_limit",
            "https://web-scraping.dev/product/2?variant=six-pack": "page_limit"
        }
    }
}
```

##### crawler_url_discovered

**When:** New URLs are discovered from crawled pages

**Use case:** Track crawl expansion, monitor discovery patterns, sitemap building

**Frequency:**High - Fires for each batch of discovered URLs

> **Key Fields:**`origin`(source URL where links were found), `discovered_urls`(list of new URLs)

```
{
    "event": "crawler_url_discovered",
    "payload": {
        "state": {
            "duration": 3,
            "urls_visited": 0,
            "urls_extracted": 0,
            "urls_failed": 0,
            "urls_skipped": 0,
            "urls_to_crawl": 0,
            "api_credit_used": 1,
            "stop_reason": null,
            "start_time": 1762940138,
            "stop_time": 1762940141
        },
        "action": "url_discovery",
        "crawler_uuid": "92e97a67-a962-4dcd-9b3e-261e4d4cb6f5",
        "project": "default",
        "env": "LIVE",
        "origin": "navigation",
        "discovered_urls": [
            "https://web-scraping.dev/product/5",
            "https://web-scraping.dev/product/1",
            "https://web-scraping.dev/product/3",
            "https://web-scraping.dev/product/4",
            "https://web-scraping.dev/product/2"
        ]
    }
}
```

##### crawler_finished

**When:** Crawler completes successfully (at least one URL visited)

**Use case:** Trigger post-processing, download results, send completion notifications

**Frequency:** Once per successful crawl

> **Success Indicators:**`state.urls_visited`>0 confirms at least one URL was crawled. Check `state.stop_reason`to understand why the crawler completed (e.g., `no_more_urls`, `page_limit`).

```
{
    "event": "crawler_finished",
    "payload": {
        "crawler_uuid": "b4867c50-318c-47cd-bfc9-bed67f24771a",
        "project": "default",
        "env": "LIVE",
        "seed_url": "https://web-scraping.dev/products",
        "action": "finished",
        "state": {
            "duration": 6.11,
            "urls_visited": 5,
            "urls_extracted": 49,
            "urls_failed": 0,
            "urls_skipped": 44,
            "urls_to_crawl": 5,
            "api_credit_used": 5,
            "stop_reason": "page_limit",
            "start_time": 1762940028,
            "stop_time": 1762940034.1143808
        },
        "links": {
            "status": "https://api.scrapfly.io/crawl/b4867c50-318c-47cd-bfc9-bed67f24771a/status"
        }
    }
}
```

##### crawler_stopped

**When:** Crawler stops due to failure (seed URL failed, errors, no URLs visited)

**Use case:** Error alerting, failure logging, retry automation

**Frequency:** Once per failed crawl

> **Failure Reasons:**Check `state.stop_reason`for the exact cause: 
> *   `seed_url_failed` - Initial URL couldn't be crawled
> *   `crawler_error` - Internal crawler error occurred
> *   `no_api_credit_left` - Account ran out of API credits mid-crawl
> *   `max_api_credit` - Configured credit limit reached

```
{
    "event": "crawler_stopped",
    "payload": {
        "crawler_uuid": "d1f6f97a-c48d-440f-86ca-b21b254ba12f",
        "project": "default",
        "env": "LIVE",
        "seed_url": "https://web-scraping.dev/products",
        "action": "stopped",
        "state": {
            "duration": 8.53,
            "urls_visited": 0,
            "urls_extracted": 1,
            "urls_failed": 1,
            "urls_skipped": 0,
            "urls_to_crawl": 1,
            "api_credit_used": 0,
            "stop_reason": "seed_url_failed",
            "start_time": 1762951426,
            "stop_time": 1762951434.5287035
        },
        "links": {
            "status": "https://api.scrapfly.home/crawl/d1f6f97a-c48d-440f-86ca-b21b254ba12f/status"
        }
    }
}
```

##### crawler_cancelled

**When:** User manually cancels the crawl via API or dashboard

**Use case:** Update tracking systems, release resources, log cancellations

**Frequency:** Once per user cancellation

> **Cancellation State:**`state.stop_reason`will be `user_cancelled`. Partial crawl results are available via the status endpoint and can be retrieved normally.

```
{
    "event": "crawler_cancelled",
    "payload": {
        "crawler_uuid": "60cf1121-9de4-43fc-a0c6-7dda1721a65b",
        "project": "default",
        "env": "LIVE",
        "seed_url": "https://web-scraping.dev/products",
        "action": "cancelled",
        "state": {
            "duration": 45,
            "urls_visited": 23,
            "urls_extracted": 87,
            "urls_failed": 2,
            "urls_skipped": 5,
            "urls_to_crawl": 57,
            "api_credit_used": 230,
            "stop_reason": "user_cancelled",
            "start_time": 1762939798,
            "stop_time": 1762939843
        },
        "links": {
            "status": "https://api.scrapfly.io/crawl/60cf1121-9de4-43fc-a0c6-7dda1721a65b/status"
        }
    }
}
```

[Development](https://scrapfly.io/docs/crawler-api/webhook#development)
-----------------------------------------------------------------------

Useful tools for local webhook development:

*   [https://webhook.site](https://webhook.site/) - Collect and display webhook notifications
*   [https://ngrok.com](https://ngrok.com/) - Expose your local application through a secured tunnel to the internet

[Security](https://scrapfly.io/docs/crawler-api/webhook#security)
-----------------------------------------------------------------

Webhooks are signed using HMAC (Hash-based Message Authentication Code) with the SHA-256 algorithm to ensure the integrity of the webhook content and verify its authenticity. This mechanism helps prevent tampering and ensures that webhook payloads are from trusted sources.

#### HMAC Overview

HMAC is a cryptographic technique that combines a secret key with a hash function (in this case, SHA-256) to produce a fixed-size hash value known as the HMAC digest. This digest is unique to both the original message and the secret key, providing a secure way to verify the integrity and authenticity of the message.

#### Signature in HTTP Header

When Scrapfly sends a webhook notification, it includes an HMAC signature in the `X-Scrapfly-Webhook-Signature` HTTP header. This signature is generated by applying the HMAC-SHA256 algorithm to the entire request body using your webhook's secret key (configured in the webhook settings).

#### Verification Example

To verify the authenticity of a webhook notification, compute the HMAC-SHA256 signature of the request body using your secret key and compare it with the signature provided in the `X-Scrapfly-Webhook-Signature` header:

```
import hmac
import hashlib

# Example secret key (replace with actual secret key from webhook settings)
secret_key = b'my_secret_key'

# Example webhook payload (replace with actual payload)
webhook_payload = b'{"event": "crawler_finished", "crawler_uuid": "..."}'

# Compute HMAC-SHA256 signature
computed_signature = hmac.new(secret_key, webhook_payload, hashlib.sha256).hexdigest()

# Compare computed signature with received signature
received_signature = '...'  # Extracted from X-Scrapfly-Webhook-Signature header
if computed_signature == received_signature:
    print("Signature verification successful. Payload is authentic.")
else:
    print("Signature verification failed. Payload may have been tampered with.")
```

> **Security Best Practices**
> *   Always verify the HMAC signature before processing webhook payloads
> *   Keep your webhook secret key confidential and rotate it periodically
> *   Use HTTPS endpoints for webhook URLs to encrypt data in transit
> *   Implement rate limiting on your webhook endpoint to handle high-frequency events

[Next Steps](https://scrapfly.io/docs/crawler-api/webhook#next-steps)
---------------------------------------------------------------------

*   Create your first webhook in the [webhook dashboard](https://scrapfly.io/dashboard/webhook)
*   Learn about [crawler configuration options](https://scrapfly.io/docs/crawler-api/getting-started)
*   Review [error handling](https://scrapfly.io/docs/crawler-api/errors) for webhook failures

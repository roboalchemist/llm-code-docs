# Source: https://scrapfly.io/docs/crawler-api/errors

Title: | Scrapfly

URL Source: https://scrapfly.io/docs/crawler-api/errors

Markdown Content:
Crawler API Errors
------------------

The Crawler API returns standard HTTP status codes and detailed error information to help you troubleshoot issues. This page lists error codes specific to crawler operations and inherited errors from the Web Scraping API.

[Crawler-Specific Errors](https://scrapfly.io/docs/crawler-api/errors#crawler-specific-errors)
----------------------------------------------------------------------------------------------

The Crawler API has specific error codes that are unique to crawler operations:

*   **Retryable:** No
*   **HTTP status code:**`400`
*   **Documentation:**
    *   [Crawler Documentation](https://scrapfly.io/docs/crawler-api/getting-started)
    *   [Related Error Doc](https://scrapfly.io/docs/crawler-api/error/ERR::CRAWLER::CONFIG_ERROR)

[Intelligent Error Handling](https://scrapfly.io/docs/crawler-api/errors#intelligent-error-handling)
----------------------------------------------------------------------------------------------------

The Crawler automatically monitors and responds to errors during execution, protecting your crawl budget and preventing wasted API credits. Different error types trigger different automated responses.

### [Fatal Errors - Immediate Stop](https://scrapfly.io/docs/crawler-api/errors#fatal-errors)

These errors immediately stop the crawler to prevent unnecessary API credit consumption. When encountered, the crawler terminates gracefully and returns results for URLs already crawled.

**Fatal error codes:**

*   [`ERR::SCRAPE::PROJECT_QUOTA_LIMIT_REACHED`](https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::PROJECT_QUOTA_LIMIT_REACHED) - Your project has reached its API credit limit 
*   [`ERR::SCRAPE::QUOTA_LIMIT_REACHED`](https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::QUOTA_LIMIT_REACHED) - Your account has reached its API credit limit 
*   [`ERR::THROTTLE::MAX_API_CREDIT_BUDGET_EXCEEDED`](https://scrapfly.io/docs/scrape-api/error/ERR::THROTTLE::MAX_API_CREDIT_BUDGET_EXCEEDED) - Monthly budget exceeded 
*   [`ERR::ACCOUNT::PAYMENT_REQUIRED`](https://scrapfly.io/docs/scrape-api/error/ERR::ACCOUNT::PAYMENT_REQUIRED) - Payment required to continue service 
*   [`ERR::ACCOUNT::SUSPENDED`](https://scrapfly.io/docs/scrape-api/error/ERR::ACCOUNT::SUSPENDED) - Account suspended 

**What happens when a fatal error occurs:**

1.   Crawler stops immediately (no new URLs are crawled)
2.   URLs already crawled are saved with their results
3.   Crawler status transitions to `completed` or `failed`
4.   Error details are included in the crawler response

### [Throttle Errors - Automatic Pause](https://scrapfly.io/docs/crawler-api/errors#throttle-errors)

These errors trigger an automatic 5-second pause before the crawler continues. This prevents overwhelming your account limits or proxy resources while allowing the crawl to complete successfully.

**Throttle error codes:**

*   [`ERR::THROTTLE::MAX_REQUEST_RATE_EXCEEDED`](https://scrapfly.io/docs/scrape-api/error/ERR::THROTTLE::MAX_REQUEST_RATE_EXCEEDED) - Request rate limit exceeded 
*   [`ERR::THROTTLE::MAX_CONCURRENT_REQUEST_EXCEEDED`](https://scrapfly.io/docs/scrape-api/error/ERR::THROTTLE::MAX_CONCURRENT_REQUEST_EXCEEDED) - Concurrent request limit exceeded 
*   [`ERR::PROXY::RESOURCES_SATURATION`](https://scrapfly.io/docs/scrape-api/error/ERR::PROXY::RESOURCES_SATURATION) - Proxy pool temporarily saturated 
*   [`ERR::SESSION::CONCURRENT_ACCESS`](https://scrapfly.io/docs/scrape-api/error/ERR::SESSION::CONCURRENT_ACCESS) - Session concurrency limit reached 

**What happens during throttling:**

1.   Crawler pauses for 5 seconds
2.   Failed URL is added back to the queue for retry
3.   Crawler continues with next URLs after pause
4.   Process repeats if throttle error occurs again

```
{
  "status": "running",
  "urls_crawled": 47,
  "urls_pending": 153,
  "recent_event": "Throttle pause: MAX_REQUEST_RATE_EXCEEDED - resuming in 5s"
}
```

### [High Failure Rate Protection](https://scrapfly.io/docs/crawler-api/errors#high-failure-rate)

For certain error types (anti-scraping protection and internal errors), the crawler monitors the failure rate and automatically stops if it becomes too high. This prevents wasting credits on a crawl that's unlikely to succeed.

**Monitored error codes:**

*   [`ERR::ASP::SHIELD_ERROR`](https://scrapfly.io/docs/scrape-api/error/ERR::ASP::SHIELD_ERROR) - Anti-scraping protection error 
*   [`ERR::ASP::SHIELD_PROTECTION_FAILED`](https://scrapfly.io/docs/scrape-api/error/ERR::ASP::SHIELD_PROTECTION_FAILED) - Failed to bypass anti-scraping protection 
*   [`ERR::API::INTERNAL_ERROR`](https://scrapfly.io/docs/scrape-api/error/ERR::API::INTERNAL_ERROR) - Internal API error 

**Failure rate threshold:**

*   **Monitoring window:** Last 10 scrape requests
*   **Threshold:** 70% failure rate (7 or more failures out of 10)
*   **Action:** Crawler stops immediately to prevent credit waste
*   **Reason:** Indicates systematic issue (website blocking, ASP changes, API issues)

```
{
  "status": "failed",
  "urls_crawled": 15,
  "urls_failed": 12,
  "error": {
    "code": "ERR::CRAWLER::HIGH_FAILURE_RATE",
    "message": "Crawler stopped: High failure rate detected (8/10 requests failed)",
    "details": {
      "failure_rate": 0.80,
      "threshold": 0.70,
      "recent_errors": ["ERR::ASP::SHIELD_ERROR", "ERR::ASP::SHIELD_PROTECTION_FAILED"]
    }
  }
}
```

**How to handle high failure rate stops:**

1.   **Review error logs:** Check which specific errors are occurring most frequently
2.   **ASP errors:** The target site may have updated their protection - contact support for assistance
3.   **Adjust configuration:** Try different `asp` settings, proxy pools, or rendering options
4.   **Wait and retry:** Some sites have temporary blocks that clear after a period
5.   **Contact support:** If issues persist, our team can help analyze and resolve ASP challenges

### [Error Statistics & Monitoring](https://scrapfly.io/docs/crawler-api/errors#error-statistics)

When a crawler completes (successfully or due to errors), comprehensive error statistics are logged and available for analysis. This helps you understand what went wrong and how to improve future crawls.

**Statistics tracked:**

*   Total errors encountered
*   Breakdown by error code (e.g., 3x `ERR::THROTTLE::MAX_REQUEST_RATE_EXCEEDED`)
*   Fatal errors that stopped the crawler
*   Throttle events and pause counts
*   High failure rate trigger details

```
{
  "crawler_id": "abc123...",
  "status": "completed",
  "urls_crawled": 847,
  "urls_failed": 23,
  "error_summary": {
    "total_errors": 23,
    "by_code": {
      "ERR::THROTTLE::MAX_REQUEST_RATE_EXCEEDED": 15,
      "ERR::PROXY::CONNECTION_TIMEOUT": 5,
      "ERR::ASP::SHIELD_ERROR": 3
    },
    "throttle_pauses": 15,
    "fatal_stops": 0,
    "high_failure_rate_stops": 0
  }
}
```

**Accessing error details:**

1.   **Crawler summary:** Use `GET /crawl/{uuid}` to view overall error statistics
2.   **Failed URLs:** Use `GET /crawl/{uuid}/urls?status=failed` to retrieve specific failed URLs with error codes
3.   **Logs:** Check your crawler logs for detailed error tracking information

[Inherited Web Scraping API Errors](https://scrapfly.io/docs/crawler-api/errors#inherited-errors)
-------------------------------------------------------------------------------------------------

Since the Crawler API makes individual scraping requests for each page crawled, it can return **any error from the Web Scraping API**. Each page crawled follows the same error handling as a single scrape request.

**Common inherited errors by category:**

### [Scraping Errors](https://scrapfly.io/docs/crawler-api/errors#scrape)

*   **Retryable:** No
*   **HTTP status code:**`422`
*   **Documentation:**
    *   [Related Error Doc](https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::BAD_PROTOCOL)

*   **Retryable:** No
*   **HTTP status code:**`200`
*   **Documentation:**
    *   [Related Error Doc](https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::BAD_UPSTREAM_RESPONSE)

*   **Retryable:** No
*   **HTTP status code:**`400`
*   **Documentation:**
    *   [Getting Started](https://scrapfly.io/docs/scrape-api/getting-started)
    *   [Related Error Doc](https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::CONFIG_ERROR)

*   **Retryable:** Yes
*   **HTTP status code:**`422`
*   **Documentation:**
    *   [Checkout ASP documentation](https://scrapfly.io/docs/scrape-api/anti-scraping-protection)
    *   [Related Error Doc](https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::COST_BUDGET_LIMIT)

*   **Retryable:** No
*   **HTTP status code:**`422`
*   **Documentation:**
    *   [Related Error Doc](https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::COUNTRY_NOT_AVAILABLE_FOR_TARGET)

*   **Retryable:** No
*   **HTTP status code:**`422`
*   **Documentation:**
    *   [Related Error Doc](https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::DNS_NAME_NOT_RESOLVED)

*   **Retryable:** No
*   **HTTP status code:**`422`
*   **Documentation:**
    *   [Related Error Doc](https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::DOMAIN_NOT_ALLOWED)

*   **Retryable:** No
*   **HTTP status code:**`422`
*   **Documentation:**
    *   [Javascript Documentation](https://scrapfly.io/docs/scrape-api/javascript-rendering)
    *   [Related Error Doc](https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::DOM_SELECTOR_INVALID)

*   **Retryable:** No
*   **HTTP status code:**`422`
*   **Documentation:**
    *   [Javascript Documentation](https://scrapfly.io/docs/scrape-api/javascript-rendering)
    *   [Related Error Doc](https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::DOM_SELECTOR_INVISIBLE)

*   **Retryable:** No
*   **HTTP status code:**`422`
*   **Documentation:**
    *   [Javascript Documentation](https://scrapfly.io/docs/scrape-api/javascript-rendering)
    *   [Related Error Doc](https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::DOM_SELECTOR_NOT_FOUND)

*   **Retryable:** Yes
*   **HTTP status code:**`422`
*   **Documentation:**
    *   [Related Error Doc](https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::DRIVER_CRASHED)

*   **Retryable:** Yes
*   **HTTP status code:**`422`
*   **Documentation:**
    *   [Related Error Doc](https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::DRIVEDRIVER_INSUFFICIENT_RESOURCES)

*   **Retryable:** Yes
*   **HTTP status code:**`422`
*   **Documentation:**
    *   [Related Error Doc](https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::DRIVER_TIMEOUT)

*   **Retryable:** No
*   **HTTP status code:**`422`
*   **Documentation:**
    *   [API Format Parameter](https://scrapfly.io/docs/scrape-api/getting-started#api_param_format)
    *   [Related Error Doc](https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::FORMAT_CONVERSION_ERROR)

*   **Retryable:** Yes
*   **HTTP status code:**`422`
*   **Documentation:**
    *   [Related Error Doc](https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::NETWORK_ERROR)

*   **Retryable:** No
*   **HTTP status code:**`422`
*   **Documentation:**
    *   [Related Error Doc](https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::NETWORK_SERVER_DISCONNECTED)

*   **Retryable:** Yes
*   **HTTP status code:**`422`
*   **Documentation:**
    *   [Related Error Doc](https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::NO_BROWSER_AVAILABLE)

*   **Retryable:** Yes
*   **HTTP status code:**`504`
*   **Documentation:**
    *   [Related Error Doc](https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::OPERATION_TIMEOUT)
    *   [Timeout Documentation](https://scrapfly.io/docs/scrape-api/understand-timeout)

*   **Retryable:** No
*   **HTTP status code:**`422`
*   **Documentation:**
    *   [Related Error Doc](https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::PLATFORM_NOT_AVAILABLE_FOR_TARGET)

*   **Retryable:** Yes
*   **HTTP status code:**`429`
*   **Documentation:**
    *   [Project Documentation](https://scrapfly.io/docs/project)
    *   [Quota Pricing](https://scrapfly.io/pricing)
    *   [Related Error Doc](https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::PROJECT_QUOTA_LIMIT_REACHED)

*   **Retryable:** No
*   **HTTP status code:**`422`
*   **Documentation:**
    *   [Related Error Doc](https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::SCENARIO_EXECUTION)

*   **Retryable:** No
*   **HTTP status code:**`422`
*   **Documentation:**
    *   [Related Error Doc](https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::SSL_ERROR)

*   **Retryable:** Yes
*   **HTTP status code:**`429`
*   **Documentation:**
    *   [Quota Pricing](https://scrapfly.io/pricing)
    *   [Related Error Doc](https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::TOO_MANY_CONCURRENT_REQUEST)

*   **Retryable:** Yes
*   **HTTP status code:**`422`
*   **Documentation:**
    *   [Related Error Doc](https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::UNABLE_TO_TAKE_SCREENSHOT)

*   **Retryable:** No
*   **HTTP status code:**`422`
*   **Documentation:**
    *   [Related Error Doc](https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::UPSTREAM_TIMEOUT)

*   **Retryable:** Yes
*   **HTTP status code:**`422`
*   **Documentation:**
    *   [Related Error Doc](https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::UPSTREAM_WEBSITE_ERROR)

### [Proxy Errors](https://scrapfly.io/docs/crawler-api/errors#proxy)

*   **Retryable:** No
*   **HTTP status code:**`422`
*   **Documentation:**
    *   [API Usage](https://scrapfly.io/docs/scrape-api/getting-started#api_param_proxy_pool)
    *   [Proxy Documentation](https://scrapfly.io/docs/scrape-api/proxy)
    *   [Related Error Doc](https://scrapfly.io/docs/scrape-api/error/ERR::PROXY::POOL_NOT_AVAILABLE_FOR_TARGET)

*   **Retryable:** No
*   **HTTP status code:**`400`
*   **Documentation:**
    *   [API Usage](https://scrapfly.io/docs/scrape-api/getting-started#api_param_proxy_pool)
    *   [Proxy Documentation](https://scrapfly.io/docs/scrape-api/proxy)
    *   [Related Error Doc](https://scrapfly.io/docs/scrape-api/error/ERR::PROXY::POOL_NOT_FOUND)

*   **Retryable:** No
*   **HTTP status code:**`400`
*   **Documentation:**
    *   [API Usage](https://scrapfly.io/docs/scrape-api/getting-started#api_param_proxy_pool)
    *   [Proxy Documentation](https://scrapfly.io/docs/scrape-api/proxy)
    *   [Related Error Doc](https://scrapfly.io/docs/scrape-api/error/ERR::PROXY::POOL_UNAVAILABLE_COUNTRY)

*   **Retryable:** Yes
*   **HTTP status code:**`422`
*   **Documentation:**
    *   [Related Error Doc](https://scrapfly.io/docs/scrape-api/error/ERR::PROXY::RESOURCES_SATURATION)

*   **Retryable:** Yes
*   **HTTP status code:**`422`
*   **Documentation:**
    *   [Related Error Doc](https://scrapfly.io/docs/scrape-api/error/ERR::PROXY::TIMEOUT)
    *   [Timeout Documentation](https://scrapfly.io/docs/scrape-api/understand-timeout)

### [Throttle Errors](https://scrapfly.io/docs/crawler-api/errors#throttle)

*   **Retryable:** Yes
*   **HTTP status code:**`429`
*   **Documentation:**
    *   [API Documentation](https://scrapfly.io/docs/scrape-api/getting-started#api_param_cost_budget)
    *   [Related Error Doc](https://scrapfly.io/docs/scrape-api/error/ERR::THROTTLE::MAX_API_CREDIT_BUDGET_EXCEEDED)

*   **Retryable:** Yes
*   **HTTP status code:**`429`
*   **Documentation:**
    *   [Related Error Doc](https://scrapfly.io/docs/scrape-api/error/ERR::THROTTLE::MAX_CONCURRENT_REQUEST_EXCEEDED)
    *   [Throttler Documentation](https://scrapfly.io/docs/throttling)

### [Anti Scraping Protection (ASP) Errors](https://scrapfly.io/docs/crawler-api/errors#asp)

*   **Retryable:** Yes
*   **HTTP status code:**`422`
*   **Documentation:**
    *   [Related Error Doc](https://scrapfly.io/docs/scrape-api/error/ERR::ASP::CAPTCHA_TIMEOUT)

*   **Retryable:** Yes
*   **HTTP status code:**`422`

*   **Retryable:** No
*   **HTTP status code:**`422`
*   **Documentation:**
    *   [Related Error Doc](https://scrapfly.io/docs/scrape-api/error/ERR::ASP::SHIELD_NOT_ELIGIBLE)

*   **Retryable:** Yes
*   **HTTP status code:**`422`
*   **Documentation:**
    *   [Checkout ASP documentation](https://scrapfly.io/docs/scrape-api/anti-scraping-protection#maximize_success_rate)
    *   [Related Error Doc](https://scrapfly.io/docs/scrape-api/error/ERR::ASP::SHIELD_PROTECTION_FAILED)

*   **Retryable:** Yes
*   **HTTP status code:**`422`
*   **Documentation:**
    *   [Checkout ASP documentation](https://scrapfly.io/docs/scrape-api/anti-scraping-protection)
    *   [Related Error Doc](https://scrapfly.io/docs/scrape-api/error/ERR::ASP::TIMEOUT)

*   **Retryable:** Yes
*   **HTTP status code:**`422`
*   **Documentation:**
    *   [Related Error Doc](https://scrapfly.io/docs/scrape-api/error/ERR::ASP::UNABLE_TO_SOLVE_CAPTCHA)

*   **Retryable:** No
*   **HTTP status code:**`422`
*   **Documentation:**
    *   [Related Error Doc](https://scrapfly.io/docs/scrape-api/error/ERR::ASP::UPSTREAM_UNEXPECTED_RESPONSE)

### [Webhook Errors](https://scrapfly.io/docs/crawler-api/errors#webhook)

*   **Retryable:** Yes
*   **HTTP status code:**`422`
*   **Documentation:**
    *   [Checkout Webhook Documentation](https://scrapfly.io/docs/scrape-api/webhook)
    *   [Related Error Doc](https://scrapfly.io/docs/scrape-api/error/ERR::WEBHOOK::ENDPOINT_UNREACHABLE)

*   **Retryable:** Yes
*   **HTTP status code:**`429`
*   **Documentation:**
    *   [Checkout Webhook Documentation](https://scrapfly.io/docs/scrape-api/webhook)
    *   [Related Error Doc](https://scrapfly.io/docs/scrape-api/error/ERR::WEBHOOK::MAX_CONCURRENCY_REACHED)

*   **Retryable:** No
*   **HTTP status code:**`429`
*   **Documentation:**
    *   [Checkout Webhook Documentation](https://scrapfly.io/docs/scrape-api/webhook)
    *   [Related Error Doc](https://scrapfly.io/docs/scrape-api/error/ERR::WEBHOOK::MAX_RETRY)

*   **Retryable:** No
*   **HTTP status code:**`400`
*   **Documentation:**
    *   [Checkout Webhook Documentation](https://scrapfly.io/docs/scrape-api/webhook)
    *   [Related Error Doc](https://scrapfly.io/docs/scrape-api/error/ERR::WEBHOOK::NOT_FOUND)

*   **Retryable:** Yes
*   **HTTP status code:**`429`
*   **Documentation:**
    *   [Checkout Webhook Documentation](https://scrapfly.io/docs/scrape-api/webhook)
    *   [Related Error Doc](https://scrapfly.io/docs/scrape-api/error/ERR::WEBHOOK::QUEUE_FULL)

### [Session Errors](https://scrapfly.io/docs/crawler-api/errors#session)

For complete details on each inherited error, see the [Web Scraping API Error Reference](https://scrapfly.io/docs/scrape-api/errors).

[HTTP Status Codes](https://scrapfly.io/docs/crawler-api/errors#status-codes)
-----------------------------------------------------------------------------

| Status Code | Description |
| --- | --- |
| `200 OK` | Request successful |
| `201 Created` | Crawler job created successfully |
| `400 Bad Request` | Invalid parameters or configuration |
| `401 Unauthorized` | Invalid or missing API key |
| `403 Forbidden` | API key doesn't have permission for this operation |
| `404 Not Found` | Crawler job UUID not found |
| `422 Request Failed` | Request was valid but execution failed |
| `429 Too Many Requests` | Rate limit or concurrency limit exceeded |
| `500 Server Error` | Internal server error |
| `504 Timeout` | Request timed out |

[Error Response Format](https://scrapfly.io/docs/crawler-api/errors#error-response)
-----------------------------------------------------------------------------------

All error responses include detailed information in a consistent format:

```
{
  "error": {
    "code": "CRAWLER_TIMEOUT",
    "message": "Crawler exceeded maximum duration of 3600 seconds",
    "retryable": false,
    "details": {
      "max_duration": 3600,
      "elapsed_duration": 3615,
      "urls_crawled": 847
    }
  }
}
```

**Error response headers:**

*   `X-Scrapfly-Error-Code` - Machine-readable error code
*   `X-Scrapfly-Error-Message` - Human-readable error description
*   `X-Scrapfly-Error-Retryable` - Whether the operation can be retried

*   [Web Scraping API Errors (Complete List)](https://scrapfly.io/docs/scrape-api/errors)
*   [Crawler API Getting Started](https://scrapfly.io/docs/crawler-api/getting-started)
*   [Contact Support](https://scrapfly.io/docs/support)

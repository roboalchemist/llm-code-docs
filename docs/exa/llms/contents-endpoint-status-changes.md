# Source: https://exa.ai/docs/changelog/contents-endpoint-status-changes.md

> ## Documentation Index
> Fetch the complete documentation index at: https://exa.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Contents Endpoint Status Changes

> The /contents endpoint now returns detailed status information for each URL instead of HTTP error codes, providing better visibility into individual content fetch results.

***

**Date: 22 May 2025**

We've updated the `/contents` endpoint to provide more granular status information for each URL you request. Instead of returning HTTP error codes directly, the endpoint now includes a `statuses` field that gives you detailed information about each content fetch operation.

<Info>
  The `/contents` endpoint will now only return an error if there's an internal issue on our end. All other cases are handled through the new `statuses` field.
</Info>

## What Changed

Previously, the `/contents` endpoint would return HTTP error codes when content fetching failed. This approach had limitations when multiple URLs failed for different reasons, making it unclear which specific error to return.

Now, the endpoint returns a `statuses` field containing individual status information for each URL, allowing you to handle different failure scenarios appropriately.

## Response Structure

The new response structure includes:

```json  theme={null}
{
  "results": [...],
  "statuses": [
    {
      "id": "https://example.com",
      "status": "success" | "error",
      "error": {
        "tag": "CRAWL_NOT_FOUND" | "CRAWL_TIMEOUT" | "SOURCE_NOT_AVAILABLE" | "CRAWL_UNKNOWN_ERROR",
        "httpStatusCode": 404 | 408 | 403 | 500
      }
    }
  ]
}
```

### Status Fields Explained

* **id**: The URL that was requested
* **status**: Either `"success"` or `"error"`
* **error** (optional): Only present when status is `"error"`
  * **tag**: Specific error type
    * `CRAWL_NOT_FOUND`: Content not found (404)
    * `CRAWL_TIMEOUT`: Request timed out (408)
    * `SOURCE_NOT_AVAILABLE`: Access forbidden or source unavailable (403)
    * `CRAWL_UNKNOWN_ERROR`: Other errors (500+)
  * **httpStatusCode**: The corresponding HTTP status code

## How to Update Your Code

Instead of catching HTTP errors, you should now check the `statuses` field:

```python Python theme={null}
# Old approach (no longer recommended)
try:
    result = exa.get_contents(["https://example.com"])
except HTTPError as e:
    print(f"Error: {e.status_code}")

# New approach
result = exa.get_contents(["https://example.com"])
for status in result.statuses:
    if status.status == "error":
        print(f"Error for {status.id}: {status.error.tag} ({status.error.httpStatusCode})")
```

## Need More Information?

If you'd like more information about the status of a crawl or have specific use cases that require additional status details, please contact us at [hello@exa.ai](mailto:hello@exa.ai) with your use case.

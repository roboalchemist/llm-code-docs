# Source: https://docs.asapp.com/getting-started/developers/rate-limits.md

# API Rate Limits and Retry Logic

> Learn about API rate limits and recommended retry logic.

ASAPP implements rate limits on our APIs to ensure system stability and optimal performance for all users. To maintain a smooth integration with our APIs, you need to:

1. Be aware of the rate limits in different environments
2. Implement retry logic to handle rate limit errors effectively

## Spike Arrest Limits

ASAPP sets a **100 requests per second** limit to prevent API abuse rather than restrict regular expected usage. If your implementation is expected to approach or exceed these limits, contact your ASAPP account team in advance to discuss potential changes and prevent service interruptions.

## Behavior When Limits are Reached

If daily limits are reached:

* Calls to the endpoint will receive a 429 'Too Many Requests' response status code for the remainder of the day.
* In cases of suspected abuse, API tokens may be revoked to temporarily suspend access to production services. ASAPP will inform you via ServiceDesk in such cases.

## Recommended Retry Logic

ASAPP recommends implementing the following retry logic using an exponential backoff strategy only in response to **429** and **5xx** errors:

### On 429 Errors

* 1st retry: 1s delay
* 2nd retry: 2s delay
* 3rd retry: 4s delay

### On 5xx Errors and Other Retriable Codes

* 1st retry: 250ms delay
* 2nd retry: 500ms delay
* 3rd retry: 1000ms delay

### Other 4XX errors

**Do not implement retries** for 4xx error codes except for 429.

<Note>
  If you receive a `409 Conflict`, then the entity has been persisted.
</Note>

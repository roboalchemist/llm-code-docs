# Source: https://smartcar.com/docs/api-reference/webhooks/delivery-behavior.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delivery Behavior

> HTTP delivery mechanics, retry policies, timeouts, and ordering guarantees

Understanding how Smartcar delivers webhook events helps you build a reliable integration. This page covers the technical details of webhook delivery, including HTTP semantics, retry behavior, and timing expectations.

## HTTP Request Format

### Request Method

All webhook deliveries use `HTTP POST` requests sent to your configured callback URI.

### Request Headers

Smartcar includes the following headers with every webhook delivery:

<ResponseField name="Content-Type" type="string" required>
  Always set to `application/json`. All webhook payloads are JSON-encoded.
</ResponseField>

<ResponseField name="SC-Signature" type="string" required>
  HMAC-SHA256 signature for payload verification. See [Payload Verification](/integrations/webhooks/payload-verification) for details on how to validate this signature.
</ResponseField>

<ResponseField name="User-Agent" type="string" required>
  Identifies requests as coming from Smartcar. Format: `Smartcar/{version}`.
</ResponseField>

### Request Body

The request body contains a JSON payload matching one of the event types documented in [Event Reference](/api-reference/webhooks/events/overview).

All requests include:

* Valid JSON formatting
* UTF-8 encoding
* Content-Length header matching the payload size

## Expected Response

### Success Response

Your webhook endpoint must return a **2xx status code** (200, 201, 202, 204, etc.) within the timeout window to acknowledge successful receipt. Any 2xx response is treated as success.

<CodeGroup>
  ```http HTTP Response theme={null}
  HTTP/1.1 200 OK
  Content-Type: application/json

  {}
  ```

  ```python Python theme={null}
  @app.post("/webhooks/smartcar")
  def handle_webhook(request):
      # Persist payload first
      save_to_queue(request.body)
      
      # Return 200 immediately
      return {"status": "received"}, 200
  ```

  ```javascript Node.js theme={null}
  app.post('/webhooks/smartcar', (req, res) => {
    // Persist payload first
    saveToQueue(req.body);
    
    // Return 200 immediately
    res.status(200).json({ status: 'received' });
  });
  ```

  ```java Java theme={null}
  @PostMapping("/webhooks/smartcar")
  public ResponseEntity<Map<String, String>> handleWebhook(@RequestBody String payload) {
      // Persist payload first
      saveToQueue(payload);
      
      // Return 200 immediately
      return ResponseEntity.ok(Map.of("status", "received"));
  }
  ```
</CodeGroup>

<Info>
  **Any 2xx status code is accepted.** You can return 200, 201, 202, 204, or any other 2xx response. Smartcar treats all 2xx codes as successful delivery.
</Info>

<Warning>
  **Response body is ignored.** Smartcar only checks the HTTP status code. You can return an empty body or a simple acknowledgment object.
</Warning>

### Response Timeout

**Your endpoint must respond within 15 seconds.** Requests that exceed this timeout are treated as delivery failures, even if your server eventually responds with a 200 status.

<Tip>
  **Decouple receiving from processing.** Persist the webhook payload to a queue or database immediately, return `200 OK`, then process the data asynchronously. This prevents timeouts from long-running business logic.
</Tip>

### Failed Responses

Any of the following are considered delivery failures and will trigger retries:

* Non-2xx HTTP status codes (including 3xx redirects, 4xx client errors, 5xx server errors)
* Connection timeouts (> 15 seconds)
* Connection refused or DNS resolution failures
* TLS/SSL handshake failures
* Network errors or connection resets

## Retry Behavior

### Retry Policy

When a delivery fails, Smartcar automatically retries up to **3 times** using an **exponential backoff** strategy with an initial delay of 25 seconds:

| Attempt       | Wait Time   | Total Elapsed        |
| ------------- | ----------- | -------------------- |
| 1st (initial) | 0s          | 0s                   |
| 2nd           | 25 seconds  | 25 seconds           |
| 3rd           | 50 seconds  | 1 minute 15 seconds  |
| 4th (final)   | 100 seconds | 2 minutes 55 seconds |

<Info>
  If all 4 delivery attempts fail, the payload is permanently dropped. Future events will still be attempted as long as the webhook remains active.
</Info>

### What Triggers Retries

Retries occur for:

* Non-2xx HTTP status codes (3xx, 4xx, 5xx)
* Request timeouts (> 15 seconds)
* Network errors (connection refused, DNS failures, etc.)
* TLS/SSL errors

### What Doesn't Trigger Retries

Once your endpoint returns any 2xx status code, Smartcar considers the delivery successful and will not retry, even if:

* Your processing logic fails later
* You detect the payload is invalid
* Your database write fails after responding

<Warning>
  **Always validate before responding.** If you return a 2xx status code and then discover the payload is invalid, you cannot trigger a retry. The delivery is considered complete.
</Warning>

### Retry Identification

Each delivery attempt receives a unique `deliveryId`, but the `eventId` remains the same across all retry attempts. Use the `eventId` to identify retries of the same event:

```json  theme={null}
{
  "eventId": "f7c0f3e6-4c9d-4f0e-8e5d-6e7f8a9b0c1d",  // Same across all retries
  // ... event data ...
  "meta": {
    "deliveryId": "5d569643-3a47-4cd1-a3ec-db5fc1f6f03b",  // Different for each attempt
    "deliveredAt": 1678901234567
  }
}
```

If the first delivery fails and Smartcar retries, the payload will have:

* **Same `eventId`**: `f7c0f3e6-4c9d-4f0e-8e5d-6e7f8a9b0c1d`
* **New `deliveryId`**: `a1b2c3d4-e5f6-7890-abcd-ef1234567890`
* **Updated `deliveredAt`**: timestamp of the retry attempt

<Tip>
  Use `eventId` for deduplication, not `deliveryId`. The `eventId` uniquely identifies the webhook event, while `deliveryId` only identifies the specific delivery attempt.
</Tip>

See [Idempotency & Deduplication](/integrations/webhooks/best-practices#implement-idempotency) for best practices on handling retries.

## Concurrent Deliveries

### Multiple Events for the Same Vehicle

Smartcar can deliver **multiple events for the same vehicle simultaneously**. This most commonly occurs when a vehicle is in a partial error state and triggers both:

* A `VEHICLE_STATE` event with signal data
* A `VEHICLE_ERROR` event with error details

Your webhook endpoint must handle concurrent requests for the same vehicle. Design your processing logic to be thread-safe and avoid race conditions.

<CodeGroup>
  ```python Python - Thread-Safe Processing theme={null}
  from threading import Lock

  vehicle_locks = {}

  @app.post("/webhooks/smartcar")
  def handle_webhook(request):
      payload = request.json
      vehicle_id = payload['data']['vehicle']['id']
      
      # Get or create a lock for this vehicle
      if vehicle_id not in vehicle_locks:
          vehicle_locks[vehicle_id] = Lock()
      
      # Process with vehicle-specific lock
      with vehicle_locks[vehicle_id]:
          process_payload(payload)
      
      return {"status": "received"}, 200
  ```

  ```javascript Node.js - Async Queue theme={null}
  const async = require('async');
  const vehicleQueues = {};

  app.post('/webhooks/smartcar', (req, res) => {
    const vehicleId = req.body.data.vehicle.id;
    
    // Create queue for this vehicle if it doesn't exist
    if (!vehicleQueues[vehicleId]) {
      vehicleQueues[vehicleId] = async.queue(processPayload, 1);
    }
    
    // Add to vehicle-specific queue
    vehicleQueues[vehicleId].push(req.body);
    
    // Return 200 immediately
    res.status(200).json({ status: 'received' });
  });
  ```
</CodeGroup>

### Cross-Vehicle Concurrency

Events for **different vehicles** can and will be delivered concurrently. If you have 1,000 vehicles subscribed to a webhook, you may receive events for multiple vehicles at the same time.

Your infrastructure should be able to handle concurrent requests proportional to your fleet size.

## Event Batching

### Single vs Multiple Deliveries

**One event per delivery.** Each webhook request contains a single event (either `VEHICLE_STATE` or `VEHICLE_ERROR`).

However, the number of deliveries depends on how the vehicle reports changes:

<AccordionGroup>
  <Accordion title="Scenario 1: Simultaneous Changes (1 delivery)">
    If a vehicle reports 3 signal changes at the same time (e.g., during a single vehicle data poll), Smartcar delivers **one `VEHICLE_STATE` event** containing all changed signals:

    ```json  theme={null}
    {
      "eventType": "VEHICLE_STATE",
      "data": {
        "triggers": ["Charge.IsCharging", "TractionBattery.StateOfCharge", "TractionBattery.Range"],
        "signals": {
          "Charge.IsCharging": { "value": true, ... },
          "TractionBattery.StateOfCharge": { "value": 85, ... },
          "TractionBattery.Range": { "value": 250, ... }
        }
      }
    }
    ```
  </Accordion>

  <Accordion title="Scenario 2: Sequential Changes (3 deliveries)">
    If a vehicle reports the same 3 signals as separate changes in quick succession, Smartcar delivers **three separate `VEHICLE_STATE` events**:

    **Delivery 1:**

    ```json  theme={null}
    {
      "eventType": "VEHICLE_STATE",
      "data": {
        "triggers": ["Charge.IsCharging"],
        "signals": { "Charge.IsCharging": { "value": true, ... }, ... }
      }
    }
    ```

    **Delivery 2:**

    ```json  theme={null}
    {
      "eventType": "VEHICLE_STATE",
      "data": {
        "triggers": ["TractionBattery.StateOfCharge"],
        "signals": { "TractionBattery.StateOfCharge": { "value": 85, ... }, ... }
      }
    }
    ```

    **Delivery 3:**

    ```json  theme={null}
    {
      "eventType": "VEHICLE_STATE",
      "data": {
        "triggers": ["TractionBattery.Range"],
        "signals": { "TractionBattery.Range": { "value": 250, ... }, ... }
      }
    }
    ```
  </Accordion>
</AccordionGroup>

<Info>
  **The behavior depends on the vehicle manufacturer.** Some OEMs batch updates, while others stream individual changes. Your integration should handle both patterns.
</Info>

## Payload Size Limits

The maximum webhook payload size is **50 KB**. This limit applies to the entire JSON payload.

<Info>
  Most webhook payloads are well under this limit. A typical `VEHICLE_STATE` event with 10-20 signals usually under 5 KB, depending on the signals.
</Info>

If you're approaching this limit, consider:

* Reducing the number of signals in your webhook subscription
* Splitting data across multiple webhooks with different signal sets

## Delivery Logs & Monitoring

### Dashboard Logs

View delivery attempt history in the [Smartcar Dashboard](https://dashboard.smartcar.com) under the **Logs** tab. The logs show:

* **Successful deliveries**: Events that received a 2xx response
* **Failed deliveries**: Events that failed after all retry attempts
* **Individual retry attempts**: Each attempt with timestamp, status code, and response time
* **Signal names**: The signals that were included in the webhook payload

<Tip>
  Use the dashboard logs to:

  * Debug delivery failures
  * Monitor webhook health
  * Track which signals triggered events
  * Verify retry behavior
</Tip>

### Delivery Metrics

Track key metrics to ensure webhook reliability:

* **Success rate**: Percentage of events delivered successfully on first attempt
* **Retry rate**: Percentage of events requiring retries
* **Average response time**: How quickly your endpoint responds
* **Failure patterns**: Common error codes or failure reasons

<Warning>
  Set up monitoring alerts for:

  * Success rate drops below 95%
  * Average response time exceeds 5 seconds
  * Consecutive failures for the same vehicle
</Warning>

## Webhook Lifecycle

### Disabling Webhooks

When you disable a webhook in the Smartcar Dashboard:

* Smartcar **stops monitoring** subscribed vehicles for changes
* Smartcar **stops attempting deliveries** immediately
* No events are queued or stored while the webhook is disabled

### Re-enabling Webhooks

When you re-enable a webhook:

* Smartcar **resumes monitoring** subscribed vehicles for changes
* The next event will include a `FIRST_DELIVERY` trigger with current signal values
* **Not supported:** Events that occurred while disabled are not retroactively delivered

<Info>
  **No event history while disabled.** Smartcar does not queue events during the disabled period. When you re-enable, you'll receive current state, not historical changes.
</Info>

## Delivery Guarantees

### At-Least-Once Delivery

Smartcar guarantees **at-least-once delivery** for all webhook events. This means:

* **Guaranteed:** You will receive every event at least once (unless all retry attempts fail)
* **Expected:** You may receive the same event multiple times
* **Not guaranteed:** Events are not delivered in order (see below)

### Ordering

**Events are not guaranteed to be delivered in order.** Due to network conditions, retry behavior, and distributed systems, events may arrive out of sequence.

For example:

1. Vehicle's state of charge changes from 50% → 60% at 10:00 AM
2. Vehicle's state of charge changes from 60% → 70% at 10:05 AM
3. You might receive the 70% event before the 60% event

<Tip>
  **Use timestamps to establish order.** Each signal includes `meta.oemUpdatedAt` and `meta.fetchedAt` timestamps. Compare these values to determine the actual sequence of events:

  ```javascript  theme={null}
  function isNewerThan(signalA, signalB) {
    return signalA.meta.oemUpdatedAt > signalB.meta.oemUpdatedAt;
  }
  ```
</Tip>

### Duplicate Prevention

While Smartcar delivers each event at least once, duplicates can occur due to:

* **Retry attempts**: If your endpoint doesn't return a 2xx response within 15 seconds, Smartcar will retry the same event, resulting in duplicate deliveries
* **Network issues**: Temporary connectivity problems may cause duplicate sends
* **Distributed systems**: Race conditions in distributed infrastructure

<Warning>
  **Most duplicates are caused by slow or failed responses.** If your endpoint takes longer than 15 seconds to respond or returns a non-2xx status code, Smartcar will retry the delivery. Always return a 2xx response quickly to minimize duplicates.
</Warning>

#### Rare Edge Case: Multiple Deliveries During Confirmation

In extremely rare circumstances, you may receive multiple deliveries for the same error **even when responding quickly**. This can occur when:

1. Smartcar detects a vehicle error (e.g., expired authorization)
2. A webhook delivery is initiated to your endpoint
3. **While confirming delivery**, the same error is detected again (e.g., another API request encounters the same expired authorization)
4. This triggers a second, independent delivery with a **different `eventId`**

**Key characteristics:**

* Happens during a narrow time window (typically milliseconds to seconds)
* Results in **different `eventId` values** for what is logically the same error condition
* Each delivery is a legitimate, distinct event from Smartcar's perspective
* Most common with `VEHICLE_ERROR` events when multiple operations encounter the same error state

**How to handle this:**

If your application is sensitive to duplicate error notifications (e.g., sending user alerts), implement additional deduplication. Use a combination of `userId`, `vehicleId`, error `code`, and a time window (2-5 minutes) in addition to standard `eventId` deduplication.

<Info>
  **This edge case is rare in practice.** Most applications won't need special handling beyond standard `eventId` deduplication.
</Info>

Always implement idempotent processing using the unique `eventId` for standard deduplication. See [Reliability Best Practices](/integrations/webhooks/best-practices/reliability#implement-idempotency) for implementation patterns.

## Latency & Timing

### Understanding Webhook Latency

Webhook delivery latency consists of two components:

**1. Detection Latency** - Time for Smartcar to detect a vehicle data change

* Depends on the vehicle manufacturer's integration and data reporting frequency
* Varies significantly by OEM (from seconds to minutes)
* Outside of Smartcar's control

**2. Delivery Latency** - Time from detection to HTTP delivery

* Smartcar delivers webhooks within seconds of detecting a change
* Actual delivery time depends on network conditions and your endpoint's location

<Info>
  **Total end-to-end latency** = Detection latency (OEM-dependent) + Delivery latency (typically seconds)

  The detection latency varies by manufacturer and is the primary factor in total webhook latency. Once Smartcar detects a change, delivery occurs quickly.
</Info>

### Delivery Latency

Webhook deliveries typically occur within **seconds** of the triggering event. Latency depends on:

* **Vehicle OEM latency**: Time for the vehicle manufacturer to report data to Smartcar
* **Change detection**: Time for Smartcar to detect a signal value change
* **Network latency**: Time to deliver the HTTP request to your endpoint

<Info>
  Most deliveries complete within 1-5 seconds of Smartcar detecting a change, but OEM latency can vary significantly by manufacturer.
</Info>

### Event Freshness

Each signal includes two timestamps to help you understand data freshness:

* **`meta.oemUpdatedAt`**: When the vehicle manufacturer recorded the value (Unix timestamp in milliseconds)
* **`meta.fetchedAt`**: When Smartcar retrieved the value from the OEM (Unix timestamp in milliseconds)

The difference between these timestamps indicates how fresh the data is from the vehicle's perspective.

## Network Requirements

### HTTPS & SSL

All webhook endpoints must:

* Use HTTPS (not HTTP)
* Have a valid SSL/TLS certificate
* Support TLS 1.2 or higher

Self-signed certificates and internal corporate CAs are not supported.

### Public Internet Access

Your webhook endpoint must be accessible from the public internet. Smartcar cannot deliver to:

* `localhost` or `127.0.0.1`
* Private IP addresses (10.x.x.x, 192.168.x.x, 172.16-31.x.x)
* Internal corporate networks without public DNS

### IP Addresses

Smartcar sends webhook requests from **public IPv4 addresses** that may change over time. We do not publish a static list of IP addresses.

<Warning>
  **Avoid IP-based firewall rules.** Instead of allowlisting specific IP addresses, use signature verification to authenticate webhook requests. See [Payload Verification](/integrations/webhooks/payload-verification).
</Warning>

### Firewall Configuration

If you must use firewall rules:

* Allow inbound HTTPS (port 443) from any IP
* Use signature verification for authentication
* Monitor for delivery failures that might indicate blocked IPs

## Error Handling

### Temporary vs Permanent Failures

**Temporary failures** (worth retrying):

* 500, 502, 503, 504 status codes
* Connection timeouts
* Temporary DNS failures
* Network blips

**Permanent failures** (not worth retrying):

* 400, 401, 403, 404, 405 status codes
* Invalid SSL certificates
* DNS resolution failures for non-existent domains

Smartcar retries both types, but you should fix permanent failures quickly to avoid dropped events.

### Monitoring Delivery Health

Monitor your webhook delivery success rate in the [Smartcar Dashboard](https://dashboard.smartcar.com) **Logs** tab. High failure rates may indicate:

* Your endpoint is down or unreachable
* Responses are too slow (> 15 seconds)
* Your endpoint is rejecting requests (4xx errors)
* SSL certificate issues

<Tip>
  Set up alerts for:

  * Delivery success rate drops below 95%
  * Average response time exceeds 5 seconds
  * Consecutive delivery failures (3+)
</Tip>

## Best Practices

To build a reliable webhook integration, follow these essential practices:

1. **Respond Quickly** - Return `200 OK` within 200ms. Queue the payload and process asynchronously to avoid timeouts.

2. **Validate Signatures** - Always verify the `SC-Signature` header before processing payloads to ensure authenticity.

3. **Handle Duplicates** - Use `eventId` to detect and skip duplicate deliveries due to retries or network issues.

4. **Use Timestamps** - Compare `meta.oemUpdatedAt` values to establish correct event ordering, as events may arrive out of sequence.

5. **Monitor Failures** - Track delivery success rates and set up alerts for anomalies or consecutive failures.

6. **Test Error Cases** - Verify your retry and error handling logic with test scenarios during development.

For detailed implementation guidance, see our comprehensive [Best Practices Guide](/integrations/webhooks/best-practices/overview).

***

## Related Resources

<CardGroup cols={2}>
  <Card title="Event Reference" icon="list" href="/api-reference/webhooks/events/overview">
    Complete reference for all webhook event types and payloads
  </Card>

  <Card title="Payload Verification" icon="signature" href="/integrations/webhooks/payload-verification">
    How to verify webhook signatures for security
  </Card>

  <Card title="Idempotency" icon="arrows-rotate" href="/integrations/webhooks/best-practices#implement-idempotency">
    Handle duplicate deliveries and ensure idempotent processing
  </Card>

  <Card title="Building a Receiver" icon="code" href="/integrations/webhooks/receiving-webhooks">
    Step-by-step guide to implementing a webhook endpoint
  </Card>
</CardGroup>

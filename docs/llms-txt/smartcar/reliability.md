# Source: https://smartcar.com/docs/integrations/webhooks/best-practices/reliability.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Reliability

> Build resilient webhook processing that handles retries and out-of-order delivery

Design your webhook integration to handle the realities of distributed systems: retries, out-of-order delivery, and duplicate events.

## Implement Idempotency

Use the `eventId` field to ensure you process each event exactly once, even if Smartcar retries delivery or you reprocess from your queue.

### Why Idempotency Matters

* Smartcar retries failed deliveries with the same `eventId`
* Your queue worker might process the same message multiple times
* Prevents duplicate database updates or notifications
* Enables safe reprocessing of historical events

### Implementation Strategies

<Tabs>
  <Tab title="Redis">
    ```python  theme={null}
    import redis

    redis_client = redis.Redis()

    def process_webhook(payload):
        event_id = payload.get("eventId")
        
        # Check if already processed
        if redis_client.exists(f"processed:{event_id}"):
            print(f"Already processed {event_id}, skipping")
            return
        
        # Process the event
        process_vehicle_data(payload)
        
        # Mark as processed (expires after 7 days)
        redis_client.setex(
            f"processed:{event_id}",
            time=604800,  # 7 days
            value="1"
        )
    ```
  </Tab>

  <Tab title="DynamoDB">
    ```javascript  theme={null}
    const processWebhook = async (payload) => {
      const { eventId } = payload;
      
      // Check if already processed
      const existing = await dynamodb.get({
        TableName: 'ProcessedEvents',
        Key: { eventId }
      }).promise();
      
      if (existing.Item) {
        console.log(`Already processed ${eventId}, skipping`);
        return;
      }
      
      // Process the event
      await processVehicleData(payload);
      
      // Mark as processed with TTL
      await dynamodb.put({
        TableName: 'ProcessedEvents',
        Item: {
          eventId,
          processedAt: new Date().toISOString(),
          ttl: Math.floor(Date.now() / 1000) + 604800 // 7 days
        }
      }).promise();
    };
    ```
  </Tab>

  <Tab title="PostgreSQL">
    ```python  theme={null}
    def process_webhook(payload):
        event_id = payload.get("eventId")
        
        # Use unique constraint to prevent duplicates
        try:
            db.execute(
                "INSERT INTO processed_events (event_id, processed_at) VALUES (%s, NOW())",
                (event_id,)
            )
        except IntegrityError:
            # Already processed
            print(f"Already processed {event_id}, skipping")
            return
        
        # Process the event
        process_vehicle_data(payload)
    ```

    ```sql  theme={null}
    -- Table schema
    CREATE TABLE processed_events (
        event_id VARCHAR(255) PRIMARY KEY,
        processed_at TIMESTAMP NOT NULL
    );

    -- Add TTL-style cleanup (run periodically)
    DELETE FROM processed_events 
    WHERE processed_at < NOW() - INTERVAL '7 days';
    ```
  </Tab>
</Tabs>

<Tip>
  **Retention period:** Store processed `eventId` values for at least 7 days to handle all retries and late reprocessing scenarios.
</Tip>

***

## Handle Out-of-Order Delivery

Webhook events are delivered **concurrently** and may arrive out of order. Never assume events arrive in chronological sequence.

### Use Timestamps for Freshness

Always check if incoming data is newer than your current stored state:

```python  theme={null}
def update_vehicle_state(payload):
    vehicle_id = payload.get("vehicleId")
    delivered_at = payload["meta"]["deliveredAt"]
    
    # Get current stored state
    current = db.get_vehicle_state(vehicle_id)
    
    # Only update if this event is newer
    if current and current.updated_at > delivered_at:
        print(f"Ignoring older event for {vehicle_id}")
        return
    
    # Safe to update
    db.update_vehicle_state(vehicle_id, payload["data"], delivered_at)
```

### Why Order Matters

<AccordionGroup>
  <Accordion title="Network Delays" icon="network-wired">
    Events sent at different times may experience different network latencies, causing them to arrive out of sequence.
  </Accordion>

  <Accordion title="Retry Timing" icon="rotate">
    If an older event fails initially and is retried later, it might arrive after newer events that succeeded on first attempt.
  </Accordion>

  <Accordion title="Concurrent Delivery" icon="arrows-split-up-and-left">
    Smartcar delivers events concurrently for performance. Events sent milliseconds apart might arrive in reverse order.
  </Accordion>
</AccordionGroup>

### Timestamp-Based Updates

<CodeGroup>
  ```python Python theme={null}
  def update_signal_value(vehicle_id, signal_path, value, timestamp):
      """Update signal only if timestamp is newer"""
      with db.transaction():
          current = db.query(
              "SELECT value, updated_at FROM signals WHERE vehicle_id = %s AND path = %s",
              (vehicle_id, signal_path)
          )
          
          if current and current['updated_at'] >= timestamp:
              # Existing value is newer or same age
              return False
          
          # Update with newer value
          db.execute(
              "INSERT INTO signals (vehicle_id, path, value, updated_at) VALUES (%s, %s, %s, %s) ON CONFLICT (vehicle_id, path) DO UPDATE SET value = EXCLUDED.value, updated_at = EXCLUDED.updated_at WHERE signals.updated_at < EXCLUDED.updated_at",
              (vehicle_id, signal_path, value, timestamp)
          )
          return True
  ```

  ```javascript Node.js theme={null}
  async function updateSignalValue(vehicleId, signalPath, value, timestamp) {
    // Conditional update: only if timestamp is newer
    const result = await db.query(`
      UPDATE signals 
      SET value = $1, updated_at = $2
      WHERE vehicle_id = $3 
        AND path = $4 
        AND (updated_at < $2 OR updated_at IS NULL)
      RETURNING *
    `, [value, timestamp, vehicleId, signalPath]);
    
    return result.rowCount > 0;
  }
  ```
</CodeGroup>

***

## Handle Retries Gracefully

Smartcar automatically retries failed deliveries up to 3 times with exponential backoff.

### Retry Identification

Each delivery attempt receives a unique `deliveryId`, but the `eventId` remains constant:

```json  theme={null}
{
  "eventId": "abc-123",         // Same across all retries
  "meta": {
    "deliveryId": "xyz-789",    // Unique per attempt
    "deliveredAt": "2025-01-15T10:30:45Z"
  }
}
```

### Processing Strategy

<Steps>
  <Step title="Check for duplicate eventId">
    Use idempotency check to skip already-processed events
  </Step>

  <Step title="Process the payload">
    Perform your business logic
  </Step>

  <Step title="Mark as processed">
    Store the eventId to prevent reprocessing
  </Step>

  <Step title="Return 200">
    Acknowledge successful processing
  </Step>
</Steps>

<Warning>
  **Don't trigger retries manually.** If you return a 2xx status code and then discover an issue, you cannot ask Smartcar to retry. The delivery is considered successful.
</Warning>

***

## Transactional Processing

Ensure database updates and idempotency tracking happen atomically:

<CodeGroup>
  ```javascript Node.js (PostgreSQL) theme={null}
  async function processWebhook(payload) {
    const { eventId } = payload;
    
    const client = await pool.connect();
    try {
      await client.query('BEGIN');
      
      // Try to insert processed event
      const result = await client.query(
        `INSERT INTO processed_events (event_id, processed_at) 
         VALUES ($1, NOW()) 
         ON CONFLICT (event_id) DO NOTHING 
         RETURNING event_id`,
        [eventId]
      );
      
      if (result.rowCount === 0) {
        // Already processed
        await client.query('ROLLBACK');
        return;
      }
      
      // Process within same transaction
      await updateVehicleData(client, payload);
      await sendNotifications(client, payload);
      
      await client.query('COMMIT');
    } catch (error) {
      await client.query('ROLLBACK');
      throw error;
    } finally {
      client.release();
    }
  }
  ```

  ```python Python (PostgreSQL) theme={null}
  def process_webhook(payload):
      event_id = payload.get("eventId")
      
      with db.transaction():
          # Check and mark as processed in one transaction
          result = db.execute(
              """
              INSERT INTO processed_events (event_id, processed_at)
              VALUES (%s, NOW())
              ON CONFLICT (event_id) DO NOTHING
              RETURNING event_id
              """,
              (event_id,)
          )
          
          if not result:
              # Already processed in another transaction
              return
          
          # Process within same transaction
          update_vehicle_data(payload)
          send_notifications(payload)
          
          # Both updates committed together
  ```
</CodeGroup>

***

## Recovery Strategies

### Dead Letter Queue

Route persistently failing events to a dead letter queue for manual investigation:

```javascript  theme={null}
async function processWebhook(payload) {
  const maxRetries = 3;
  let retryCount = 0;
  
  while (retryCount < maxRetries) {
    try {
      await doProcessing(payload);
      return; // Success
    } catch (error) {
      retryCount++;
      if (retryCount >= maxRetries) {
        // Move to DLQ
        await dlq.send({
          payload,
          error: error.message,
          attempts: retryCount
        });
      } else {
        // Wait before retry
        await sleep(Math.pow(2, retryCount) * 1000);
      }
    }
  }
}
```

### Circuit Breaker

Stop processing if downstream dependencies are failing:

```python  theme={null}
class CircuitBreaker:
    def __init__(self, failure_threshold=5):
        self.failure_count = 0
        self.failure_threshold = failure_threshold
        self.is_open = False
        self.last_failure_time = None
    
    def call(self, func, *args):
        if self.is_open:
            # Check if we should try again
            if time.time() - self.last_failure_time > 60:
                self.is_open = False
                self.failure_count = 0
            else:
                raise Exception("Circuit breaker is open")
        
        try:
            result = func(*args)
            self.failure_count = 0
            return result
        except Exception as e:
            self.failure_count += 1
            self.last_failure_time = time.time()
            
            if self.failure_count >= self.failure_threshold:
                self.is_open = True
            
            raise e

# Usage
breaker = CircuitBreaker()

def process_webhook(payload):
    try:
        breaker.call(update_database, payload)
    except Exception:
        # Return 503 to trigger Smartcar retry later
        return {"error": "Service unavailable"}, 503
```

***

## Next Steps

<CardGroup cols={2}>
  <Card title="Monitoring" icon="chart-line" href="/integrations/webhooks/best-practices/monitoring">
    Track idempotency hits and processing failures
  </Card>

  <Card title="VEHICLE_ERROR Events" icon="triangle-exclamation" href="/api-reference/webhooks/events/vehicle-error">
    Handle error notifications and resolution tracking
  </Card>

  <Card title="Delivery Behavior" icon="truck-fast" href="/api-reference/webhooks/delivery-behavior">
    Understanding retry policies
  </Card>

  <Card title="Testing" icon="flask" href="/integrations/webhooks/best-practices/testing">
    Test retry scenarios
  </Card>
</CardGroup>

# Source: https://smartcar.com/docs/integrations/webhooks/best-practices/monitoring.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Monitoring & Observability

> Track webhook performance and detect issues early

Comprehensive logging and monitoring help you debug issues, track performance, and maintain reliability.

## Log Key Events

Track every stage of webhook processing for complete observability.

### What to Log

<AccordionGroup>
  <Accordion title="Webhook Receipt" icon="inbox">
    ```json  theme={null}
    {
      "timestamp": "2025-01-15T10:30:45Z",
      "event": "webhook.received",
      "eventId": "abc123",
      "eventType": "VEHICLE_STATE",
      "vehicleId": "def456",
      "deliveryId": "ghi789"
    }
    ```
  </Accordion>

  <Accordion title="Signature Verification" icon="shield-check">
    ```json  theme={null}
    {
      "timestamp": "2025-01-15T10:30:45Z",
      "event": "signature.verified",
      "eventId": "abc123",
      "valid": true
    }
    ```
  </Accordion>

  <Accordion title="Processing Start/End" icon="play">
    ```json  theme={null}
    {
      "timestamp": "2025-01-15T10:30:46Z",
      "event": "processing.started",
      "eventId": "abc123",
      "eventType": "VEHICLE_STATE"
    }
    ```
  </Accordion>

  <Accordion title="Processing Errors" icon="triangle-exclamation">
    ```json  theme={null}
    {
      "timestamp": "2025-01-15T10:30:47Z",
      "event": "processing.failed",
      "eventId": "abc123",
      "error": "Database connection timeout",
      "stackTrace": "..."
    }
    ```
  </Accordion>
</AccordionGroup>

***

## Critical Metrics

Monitor these metrics and set up alerts:

| Metric                              | What It Measures              | Alert Threshold                        |
| ----------------------------------- | ----------------------------- | -------------------------------------- |
| **Signature verification failures** | Invalid or spoofed requests   | > 5 in 5 minutes                       |
| **Processing error rate**           | Code or infrastructure issues | > 5% of events                         |
| **Queue depth**                     | Processing backlog            | > 1000 messages                        |
| **Response time**                   | Endpoint performance          | > 10 seconds (approaching 15s timeout) |
| **Duplicate processing**            | Idempotency check hits        | Track for debugging                    |
| **VEHICLE\_ERROR rate**             | Signal retrieval issues       | > 10% of vehicles                      |

***

## Implementation Examples

<CodeGroup>
  ```javascript Node.js (Winston) theme={null}
  const winston = require('winston');

  const logger = winston.createLogger({
    format: winston.format.json(),
    transports: [new winston.transports.Console()]
  });

  app.post('/webhooks/smartcar', async (req, res) => {
    const payload = req.body;
    const { eventId, eventType, vehicleId } = payload;
    
    // Log receipt
    logger.info('webhook.received', {
      eventId,
      eventType,
      vehicleId
    });
    
    // Verify signature
    const isValid = verifySignature(req.rawBody, req.headers['sc-signature']);
    logger.info('signature.verified', { eventId, valid: isValid });
    
    if (!isValid) {
      logger.warn('signature.failed', {
        eventId,
        sourceIp: req.ip
      });
      return res.status(401).json({ error: 'Invalid signature' });
    }
    
    // Queue and return
    await queue.add(payload);
    res.status(200).json({ status: 'received' });
  });

  async function processWebhook(payload) {
    const { eventId } = payload;
    const startTime = Date.now();
    
    logger.info('processing.started', { eventId });
    
    try {
      await updateVehicleData(payload);
      logger.info('processing.completed', {
        eventId,
        durationMs: Date.now() - startTime
      });
    } catch (error) {
      logger.error('processing.failed', {
        eventId,
        error: error.message,
        stack: error.stack
      });
      throw error;
    }
  }
  ```

  ```python Python (Structured Logging) theme={null}
  import structlog

  logger = structlog.get_logger()

  @app.post("/webhooks/smartcar")
  def webhook_handler():
      payload = request.get_json()
      event_id = payload.get("eventId")
      
      # Log receipt
      logger.info("webhook.received",
          event_id=event_id,
          event_type=payload.get("eventType"),
          vehicle_id=payload.get("vehicleId")
      )
      
      # Verify signature
      is_valid = verify_signature(request.data, request.headers.get('SC-Signature'))
      logger.info("signature.verified",
          event_id=event_id,
          valid=is_valid
      )
      
      if not is_valid:
          logger.warning("signature.failed",
              event_id=event_id,
              source_ip=request.remote_addr
          )
          return {"error": "Invalid signature"}, 401
      
      # Queue and return
      queue.enqueue(process_webhook, payload)
      return {"status": "received"}, 200

  def process_webhook(payload):
      event_id = payload.get("eventId")
      
      logger.info("processing.started", event_id=event_id)
      
      try:
          update_vehicle_data(payload)
          logger.info("processing.completed", 
              event_id=event_id,
              duration_ms=duration
          )
      except Exception as e:
          logger.error("processing.failed",
              event_id=event_id,
              error=str(e),
              exc_info=True
          )
          raise
  ```
</CodeGroup>

***

## Next Steps

<CardGroup cols={2}>
  <Card title="VEHICLE_ERROR Events" icon="triangle-exclamation" href="/api-reference/webhooks/events/vehicle-error">
    Track error notifications and resolution
  </Card>

  <Card title="Reliability" icon="shield" href="/integrations/webhooks/best-practices/reliability">
    Implement idempotency
  </Card>

  <Card title="Testing" icon="flask" href="/integrations/webhooks/best-practices/testing">
    Test your monitoring setup
  </Card>
</CardGroup>

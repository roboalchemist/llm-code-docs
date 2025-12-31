# Source: https://smartcar.com/docs/integrations/webhooks/best-practices/architecture.md

# Architecture Patterns

> Design patterns for reliable webhook processing

The most critical pattern for reliable webhook handling is separating acknowledgment from processing.

## Decouple Receipt from Processing

**Return 200 immediately, process asynchronously.** This is the foundation of a reliable webhook integration.

<Steps>
  <Step title="Receive the webhook">
    Your endpoint receives the POST request from Smartcar
  </Step>

  <Step title="Persist immediately">
    Write the raw payload to a queue, database, or object storage
  </Step>

  <Step title="Return 200">
    Acknowledge receipt with a 200 status code (within 15 seconds)
  </Step>

  <Step title="Process asynchronously">
    A background worker processes the persisted payload
  </Step>
</Steps>

### Why This Matters

* **Prevents timeouts** from slow business logic
* **Allows retry of processing** without requesting redelivery
* **Enables processing updates** without losing historical events
* **Survives outages** in downstream systems

### Implementation Examples

<CodeGroup>
  ```javascript Node.js (Express + AWS SQS) theme={null}
  const express = require('express');
  const AWS = require('aws-sdk');

  const app = express();
  const sqs = new AWS.SQS();

  app.post('/webhooks/smartcar', async (req, res) => {
    try {
      // 1. Get the raw payload
      const payload = req.body;
      
      // 2. Queue for processing
      await sqs.sendMessage({
        QueueUrl: process.env.WEBHOOK_QUEUE_URL,
        MessageBody: JSON.stringify(payload)
      }).promise();
      
      // 3. Return immediately
      res.status(200).json({ status: 'received' });
    } catch (error) {
      console.error('Failed to queue webhook:', error);
      res.status(500).json({ error: 'Internal error' });
    }
  });

  // Separate worker processes the queue
  async function processWebhook(payload) {
    const { eventType } = payload;
    
    if (eventType === 'VEHICLE_STATE') {
      await updateVehicleState(payload);
    } else if (eventType === 'VEHICLE_ERROR') {
      await handleVehicleError(payload);
    }
  }
  ```

  ```python Python (Flask + Redis Queue) theme={null}
  from flask import Flask, request
  from rq import Queue
  from redis import Redis

  app = Flask(__name__)
  redis_conn = Redis()
  queue = Queue(connection=redis_conn)

  @app.post("/webhooks/smartcar")
  def webhook_handler():
      # 1. Get the raw payload
      payload = request.get_json()
      
      # 2. Queue for processing
      queue.enqueue(process_webhook, payload)
      
      # 3. Return immediately
      return {"status": "received"}, 200

  def process_webhook(payload):
      # This runs asynchronously in a worker
      event_type = payload.get("eventType")
      
      if event_type == "VEHICLE_STATE":
          update_vehicle_state(payload)
      elif event_type == "VEHICLE_ERROR":
          handle_vehicle_error(payload)
  ```

  ```java Java (Spring Boot + RabbitMQ) theme={null}
  @RestController
  public class WebhookController {
      
      @Autowired
      private RabbitTemplate rabbitTemplate;
      
      @PostMapping("/webhooks/smartcar")
      public ResponseEntity<Map<String, String>> handleWebhook(
          @RequestBody String payload
      ) {
          // 1. Queue for processing
          rabbitTemplate.convertAndSend(
              "webhook-queue", 
              payload
          );
          
          // 2. Return immediately
          return ResponseEntity.ok(
              Map.of("status", "received")
          );
      }
  }

  @Component
  public class WebhookProcessor {
      
      @RabbitListener(queues = "webhook-queue")
      public void processWebhook(String payload) {
          // This runs asynchronously
          JsonNode json = objectMapper.readTree(payload);
          String eventType = json.get("eventType").asText();
          
          if ("VEHICLE_STATE".equals(eventType)) {
              updateVehicleState(json);
          } else if ("VEHICLE_ERROR".equals(eventType)) {
              handleVehicleError(json);
          }
      }
  }
  ```
</CodeGroup>

<Warning>
  **Don't do this:** If you perform heavy processing before returning a response, your endpoint may timeout and Smartcar will retry, creating duplicate processing work.

  ```python Bad Example theme={null}
  @app.post("/webhooks/smartcar")
  def webhook_handler():
      payload = request.get_json()
      
      # DON'T DO THIS: These operations might take too long
      update_database(payload)
      call_external_api(payload)
      send_notifications(payload)
      
      # Might timeout before reaching this line
      return {"status": "received"}, 200
  ```
</Warning>

***

## Production-Ready Pattern

For a complete serverless implementation, see the [Webhook Receiver Recipe](/getting-started/tutorials/webhook-receiver-recipe), which provides:

* API Gateway for HTTPS endpoint
* Lambda function for webhook receipt
* SQS queue for async processing
* Dead letter queue for failed messages
* CloudWatch monitoring and alerts

***

## Next Steps

<CardGroup cols={2}>
  <Card title="Security" icon="shield-check" href="/integrations/webhooks/best-practices/security">
    Verify payload signatures
  </Card>

  <Card title="Reliability" icon="shield" href="/integrations/webhooks/best-practices/reliability">
    Implement idempotency
  </Card>

  <Card title="Delivery Behavior" icon="truck-fast" href="/api-reference/webhooks/delivery-behavior">
    Understand retry policies
  </Card>

  <Card title="Webhook Recipe" icon="book" href="/getting-started/tutorials/webhook-receiver-recipe">
    Deploy serverless infrastructure
  </Card>
</CardGroup>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://smartcar.com/docs/llms.txt
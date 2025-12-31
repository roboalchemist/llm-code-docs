# Source: https://smartcar.com/docs/integrations/webhooks/receiving-webhooks.md

# Receiving Webhooks

> Set up an endpoint to receive and parse webhook payloads from Smartcar

Learn how to build a basic webhook endpoint that receives, parses, and acknowledges Smartcar webhook deliveries.

<Tip>
  **Want to skip the manual setup?**

  Deploy a production-ready webhook receiver to AWS in minutes with our [Webhook Receiver Recipe](/getting-started/tutorials/webhook-receiver-recipe). It includes complete serverless infrastructure (Lambda + API Gateway + SQS), built-in signature verification, automatic error handling, and TypeScript type safety.

  **Perfect for:** New implementations, AWS environments, or teams wanting to deploy quickly without infrastructure overhead.
</Tip>

## Basic Requirements

Your webhook endpoint must meet these requirements:

* **Accept POST requests** - Smartcar sends all webhooks as HTTP POST requests
* **Return 2xx status code** - Any status code from 200-299 acknowledges successful receipt
* **Use HTTPS** - Your endpoint must use HTTPS with a valid SSL certificate
* **Respond within 15 seconds** - Return a status code before the timeout window
* **Publicly accessible** - Your endpoint must be accessible from the public internet

***

## Quick Start Examples

Here are minimal webhook receivers that handle the required `VERIFY` event and acknowledge all other events:

<CodeGroup>
  ```javascript Node.js (Express) theme={null}
  const express = require('express');
  const smartcar = require('smartcar');
  const app = express();

  app.use(express.json());

  app.post('/webhooks/smartcar', (req, res) => {
    const { eventType, data } = req.body;
    
    // Handle VERIFY event (required)
    if (eventType === 'VERIFY') {
      const hmac = smartcar.hashChallenge(
        process.env.SMARTCAR_MANAGEMENT_TOKEN,
        data.challenge
      );
      return res.status(200).json({ challenge: hmac });
    }
    
    // Log other events
    console.log('Received webhook:', eventType);
    
    // Acknowledge receipt
    res.status(200).json({ status: 'received' });
    
    // Process asynchronously (recommended)
    // processWebhook(req.body);
  });

  app.listen(3000);
  ```

  ```python Python (Flask) theme={null}
  from flask import Flask, request, jsonify
  import smartcar
  import os

  app = Flask(__name__)

  @app.post('/webhooks/smartcar')
  def webhook_handler():
      payload = request.get_json()
      event_type = payload.get('eventType')
      
      # Handle VERIFY event (required)
      if event_type == 'VERIFY':
          hmac = smartcar.hash_challenge(
              os.environ['SMARTCAR_MANAGEMENT_TOKEN'],
              payload['data']['challenge']
          )
          return jsonify({"challenge": hmac}), 200
      
      # Log other events
      print(f"Received webhook: {event_type}")
      
      # Acknowledge receipt
      return jsonify({"status": "received"}), 200
      
      # Process asynchronously (recommended)
      # process_webhook(payload)

  if __name__ == '__main__':
      app.run(port=3000)
  ```

  ```java Java (Spring Boot) theme={null}
  import com.smartcar.sdk.Webhook;
  import org.springframework.web.bind.annotation.*;
  import org.springframework.http.ResponseEntity;
  import java.util.Map;

  @RestController
  public class WebhookController {
      
      @PostMapping("/webhooks/smartcar")
      public ResponseEntity<Map<String, String>> handleWebhook(
          @RequestBody Map<String, Object> payload
      ) {
          String eventType = (String) payload.get("eventType");
          
          // Handle VERIFY event (required)
          if ("VERIFY".equals(eventType)) {
              Map<String, Object> data = (Map<String, Object>) payload.get("data");
              String challenge = (String) data.get("challenge");
              
              String hmac = Webhook.hashChallenge(
                  System.getenv("SMARTCAR_MANAGEMENT_TOKEN"),
                  challenge
              );
              return ResponseEntity.ok(Map.of("challenge", hmac));
          }
          
          // Log other events
          System.out.println("Received webhook: " + eventType);
          
          // Acknowledge receipt
          return ResponseEntity.ok(Map.of("status", "received"));
          
          // Process asynchronously (recommended)
          // processWebhook(payload);
      }
  }
  ```

  ```ruby Ruby (Sinatra) theme={null}
  require 'sinatra'
  require 'smartcar'
  require 'json'

  post '/webhooks/smartcar' do
    payload = JSON.parse(request.body.read)
    event_type = payload['eventType']
    
    # Handle VERIFY event (required)
    if event_type == 'VERIFY'
      hmac = Smartcar.hash_challenge(
        ENV['SMARTCAR_MANAGEMENT_TOKEN'],
        payload['data']['challenge']
      )
      
      status 200
      content_type :json
      return { challenge: hmac }.to_json
    end
    
    # Log other events
    puts "Received webhook: #{event_type}"
    
    # Acknowledge receipt
    status 200
    content_type :json
    { status: 'received' }.to_json
    
    # Process asynchronously (recommended)
    # process_webhook(payload)
  end
  ```
</CodeGroup>

<Warning>
  **VERIFY event required** - Your endpoint must successfully respond to the `VERIFY` event before Smartcar delivers any vehicle data. See [Callback Verification](/integrations/webhooks/callback-verification) for detailed instructions and troubleshooting.
</Warning>

<Tip>
  **Best practice:** Return 200 immediately and process the webhook asynchronously. See [Architecture Best Practices](/integrations/webhooks/best-practices/architecture) for the queue-based pattern.
</Tip>

<Info>
  **Any 2xx works:** You can return 200, 201, 202, 204, or any other 2xx status code. Smartcar treats all 2xx responses as successful delivery.
</Info>

***

## What Happens After Verification

After your endpoint successfully responds to the `VERIFY` event, Smartcar will begin delivering `VEHICLE_STATE` and `VEHICLE_ERROR` events for [subscribed vehicles](/integrations/webhooks/subscribing-vehicles).

<Info>
  **Understanding payloads:** For detailed payload structure, field definitions, and event-specific schemas, see the [Event Reference Overview](/api-reference/webhooks/events/overview).
</Info>

***

## Next Steps

<Warning>
  **Complete the VERIFY challenge first** - Your endpoint must successfully respond to the `VERIFY` event before Smartcar delivers any vehicle data. See [Handling the VERIFY Event](#handling-the-verify-event) above.
</Warning>

Once your endpoint is verified and receiving webhooks, continue implementing your integration with these guides:

<CardGroup cols={2}>
  <Card title="Payload Verification" icon="shield-check" href="/integrations/webhooks/payload-verification">
    Verify all payloads are authentic using the SC-Signature header
  </Card>

  <Card title="Event Reference" icon="list" href="/api-reference/webhooks/events/overview">
    Understand VEHICLE\_STATE, VEHICLE\_ERROR, and VERIFY event structures
  </Card>

  <Card title="Best Practices" icon="star" href="/integrations/webhooks/best-practices/overview">
    Implement idempotency, queuing, monitoring, and error handling
  </Card>

  <Card title="Delivery Behavior" icon="truck-fast" href="/api-reference/webhooks/delivery-behavior">
    Learn about retry policies, timeouts, and ordering guarantees
  </Card>
</CardGroup>

***

## FAQ

<AccordionGroup>
  <Accordion title="Why isn't my webhook receiving vehicle data?" icon="triangle-exclamation">
    Your endpoint must successfully respond to the `VERIFY` event before Smartcar delivers any `VEHICLE_STATE` or `VEHICLE_ERROR` events. Check the Dashboard to confirm your webhook shows "Verified" status.
  </Accordion>

  <Accordion title="How do I test locally?" icon="laptop">
    Use [ngrok](https://ngrok.com) or similar to expose your local server:

    ```bash  theme={null}
    ngrok http 3000
    ```

    Then use the ngrok URL in Dashboard as your callback URI.
    Note that you will have to re-verify the webhook after changing the callback URI.
  </Accordion>

  <Accordion title="What about signature verification?" icon="key">
    Always verify the `SC-Signature` header to ensure payloads are authentic. See [Payload Verification](/integrations/webhooks/payload-verification).
  </Accordion>

  <Accordion title="Should I process webhooks synchronously?" icon="clock">
    No. Return 200 immediately and process asynchronously using a queue. This prevents timeouts and retry storms. See [Architecture Best Practices](/integrations/webhooks/best-practices/architecture).
  </Accordion>
</AccordionGroup>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://smartcar.com/docs/llms.txt
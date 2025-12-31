# Source: https://smartcar.com/docs/api-reference/webhooks/events/verify.md

# VERIFY Event

> One-time challenge to verify your webhook endpoint

A one-time event sent when you first create a webhook to verify that Smartcar can successfully deliver payloads to your callback URL.

<Warning>
  **Required Before Data Delivery**

  Your endpoint must successfully respond to the `VERIFY` event before Smartcar will deliver any `VEHICLE_STATE` or `VEHICLE_ERROR` events. This confirms your endpoint is configured correctly and ready to receive webhooks.
</Warning>

## When This Event Fires

The `VERIFY` event fires once when you:

* Create a new webhook in the Smartcar Dashboard
* Update the callback URL of an existing webhook
* Click "Verify this webhook" in the Dashboard

***

## Payload Structure

<CodeGroup>
  ```json Version 4.0 (Current) theme={null}
  {
    "eventId": "52f6e0bb-1369-45da-a61c-9e67d092d6db",
    "eventType": "VERIFY",
    "data": {
      "challenge": "3a5c8f72-e6d9-4b1a-9f2e-8c7d6a5b4e3f"
    },
    "meta": {
      "version": "4.0",
      "webhookId": "5a8e5e38-1e12-4011-a36d-56f120053f9e",
      "webhookName": "Example Webhook",
      "deliveryId": "5d569643-3a47-4cd1-a3ec-db5fc1f6f03b",
      "deliveredAt": 1761896351529
    }
  }
  ```

  ```json Version 2.0 (Legacy) theme={null}
  {
    "version": "2.0",
    "webhookId": "5a8e5e38-1e12-4011-a36d-56f120053f9e",
    "eventName": "verify",
    "payload": { 
      "challenge": "3a5c8f72-e6d9-4b1a-9f2e-8c7d6a5b4e3f"
    }
  }
  ```
</CodeGroup>

### Payload Fields

<ResponseField name="eventId" type="string" required>
  Unique identifier for this verification event.
</ResponseField>

<ResponseField name="eventType" type="string" required>
  Always `"VERIFY"` for this event type.
</ResponseField>

<ResponseField name="data" type="object" required>
  Container for the challenge.

  <Expandable title="data object">
    <ResponseField name="challenge" type="string" required>
      Random string that must be hashed with your Application Management Token and returned in your response.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="meta" type="object" required>
  Webhook delivery metadata. See [Event Reference Overview](/api-reference/webhooks/events/overview#common-fields) for the complete `meta` object schema.
</ResponseField>

***

## Required Response

Your endpoint must respond with:

1. **Status code**: `200 OK`
2. **Content-Type header**: `application/json`
3. **Response body**: JSON object with the HMAC-SHA256 hash

```json Response Body theme={null}
{
  "challenge": "a3f5c8e9d2b4a1f6e8c7d9a5b3e1f2c4d6a8b9c1e3f5a7b9c2d4e6f8a1b3c5d7"
}
```

### Generate the HMAC

Create an HMAC-SHA256 hash of the `challenge` string using your **Application Management Token** as the secret key, then hex-encode the result:

<Tip>
  Our [backend SDKs](/api-reference/api-sdks) have helper methods to generate the HMAC automatically.
</Tip>

<CodeGroup>
  ```python Python theme={null}
  import smartcar

  hmac = smartcar.hash_challenge(
      application_management_token, 
      challenge
  )

  # Return in response body
  return {"challenge": hmac}, 200
  ```

  ```javascript Node.js theme={null}
  const smartcar = require('smartcar');

  const hmac = smartcar.hashChallenge(
      application_management_token, 
      challenge
  );

  // Return in response body
  res.status(200).json({ challenge: hmac });
  ```

  ```java Java theme={null}
  import com.smartcar.sdk.Smartcar;

  String hmac = Smartcar.hashChallenge(
      application_management_token, 
      challenge
  );

  // Return in response body
  return ResponseEntity.ok(Map.of("challenge", hmac));
  ```

  ```ruby Ruby theme={null}
  require 'smartcar'

  hmac = Smartcar.hash_challenge(
      application_management_token, 
      challenge
  )

  # Return in response body
  { challenge: hmac }
  ```
</CodeGroup>

***

## Complete Handler Example

Here's a complete webhook handler that responds to the `VERIFY` event:

<CodeGroup>
  ```javascript Node.js (Express) theme={null}
  const express = require('express');
  const smartcar = require('smartcar');

  const app = express();
  app.use(express.json());

  app.post('/webhooks/smartcar', (req, res) => {
    const { eventType, data } = req.body;
    
    if (eventType === 'VERIFY') {
      // Generate HMAC challenge response
      const hmac = smartcar.hashChallenge(
        process.env.SMARTCAR_MANAGEMENT_TOKEN,
        data.challenge
      );
      
      return res.status(200).json({ challenge: hmac });
    }
    
    // Handle other event types...
    res.status(200).json({ status: 'received' });
  });
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
      
      if event_type == 'VERIFY':
          # Generate HMAC challenge response
          hmac = smartcar.hash_challenge(
              os.environ['SMARTCAR_MANAGEMENT_TOKEN'],
              payload['data']['challenge']
          )
          
          return jsonify({"challenge": hmac}), 200
      
      # Handle other event types...
      return jsonify({"status": "received"}), 200
  ```

  ```java Java (Spring Boot) theme={null}
  @RestController
  public class WebhookController {
      
      @Value("${smartcar.management.token}")
      private String managementToken;
      
      @PostMapping("/webhooks/smartcar")
      public ResponseEntity<?> handleWebhook(@RequestBody Map<String, Object> payload) {
          String eventType = (String) payload.get("eventType");
          
          if ("VERIFY".equals(eventType)) {
              // Generate HMAC challenge response
              Map<String, Object> data = (Map<String, Object>) payload.get("data");
              String challenge = (String) data.get("challenge");
              
              String hmac = Smartcar.hashChallenge(managementToken, challenge);
              
              return ResponseEntity.ok(Map.of("challenge", hmac));
          }
          
          // Handle other event types...
          return ResponseEntity.ok(Map.of("status", "received"));
      }
  }
  ```

  ```ruby Ruby (Sinatra) theme={null}
  require 'sinatra'
  require 'json'
  require 'smartcar'

  post '/webhooks/smartcar' do
    payload = JSON.parse(request.body.read)
    event_type = payload['eventType']
    
    if event_type == 'VERIFY'
      # Generate HMAC challenge response
      hmac = Smartcar.hash_challenge(
        ENV['SMARTCAR_MANAGEMENT_TOKEN'],
        payload['data']['challenge']
      )
      
      status 200
      content_type :json
      return { challenge: hmac }.to_json
    end
    
    # Handle other event types...
    status 200
    content_type :json
    { status: 'received' }.to_json
  end
  ```
</CodeGroup>

***

## Troubleshooting

<AccordionGroup>
  <Accordion title="Verification fails in Dashboard" icon="circle-xmark">
    **Common causes:**

    * Wrong Application Management Token used
    * HMAC not hex-encoded
    * Response body doesn't match `{ "challenge": "..." }` format
    * Endpoint returns non-200 status code
    * Response takes longer than 15 seconds

    **Solution:** Use the Dashboard's verification modal to see the expected challenge and response. Compare your implementation against the provided code snippets.
  </Accordion>

  <Accordion title="How do I test VERIFY locally?" icon="laptop">
    Use [ngrok](https://ngrok.com) or similar to expose your local server:

    ```bash  theme={null}
    ngrok http 3000
    ```

    Then use the ngrok URL as your callback URI in the Dashboard. The Dashboard will send a real `VERIFY` event to your local endpoint.
  </Accordion>

  <Accordion title="Can I re-verify my webhook?" icon="rotate">
    Yes! You can click "Verify this webhook" in the Dashboard at any time to send a new `VERIFY` event to your endpoint.
  </Accordion>

  <Accordion title="Do I need to handle VERIFY in production?" icon="question">
    Yes, your production webhook endpoint should always handle the `VERIFY` event type, even after initial verification. This allows you to re-verify from the Dashboard if needed.
  </Accordion>
</AccordionGroup>

<Warning>
  **Timeout Requirement**

  Your endpoint must respond to the `VERIFY` event within **15 seconds**. If verification times out, Smartcar will not activate the webhook.
</Warning>

***

## Next Steps

After successfully responding to the `VERIFY` event, your webhook is activated and will begin receiving vehicle data.

<CardGroup cols={2}>
  <Card title="VEHICLE_STATE Event" icon="car" href="/api-reference/webhooks/events/vehicle-state">
    Learn about signal data deliveries
  </Card>

  <Card title="VEHICLE_ERROR Event" icon="triangle-exclamation" href="/api-reference/webhooks/events/vehicle-error">
    Handle error notifications
  </Card>

  <Card title="Callback Verification Guide" icon="book" href="/integrations/webhooks/callback-verification">
    Complete step-by-step implementation
  </Card>

  <Card title="Receiving Webhooks" icon="code" href="/integrations/webhooks/receiving-webhooks">
    Build a complete webhook handler
  </Card>
</CardGroup>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://smartcar.com/docs/llms.txt
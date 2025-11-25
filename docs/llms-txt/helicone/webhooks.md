# Source: https://docs.helicone.ai/features/webhooks.md

# Webhooks

<Note>
  **March 2025 Update**: We've enhanced our webhook implementation to provide a
  unified `request_response_url` field that contains both request and response
  data in a single object. This improves performance and simplifies data
  retrieval. [Learn more](#understanding-webhooks).
</Note>

When building LLM applications, you often need to react to events in real-time, track usage patterns, or trigger downstream actions based on AI interactions. Webhooks provide instant notifications when LLM requests complete, allowing you to automate workflows, score responses, and integrate AI activity with external systems.

## Why use Webhooks

* **Real-time evaluation**: Automatically score and evaluate LLM responses for quality, safety, and relevance
* **Data pipeline integration**: Stream LLM data to external systems, data warehouses, or analytics platforms
* **Automated workflows**: Trigger downstream actions like notifications, content moderation, or process automation

## Quick Start

<Steps>
  <Step title="Set up webhook endpoint">
    Navigate to the [webhooks page](https://us.helicone.ai/webhooks) and add your webhook URL:

        <img src="https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/webhooks/webhook-name.webp?fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=1e33234a69e66e2301579529814c96cb" alt="webhook name" data-og-width="1320" width="1320" data-og-height="1256" height="1256" data-path="images/webhooks/webhook-name.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/webhooks/webhook-name.webp?w=280&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=2acb74a46a727a84d1e7965482550ee2 280w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/webhooks/webhook-name.webp?w=560&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=87f61a938fb3d28b0d477173a581dc0c 560w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/webhooks/webhook-name.webp?w=840&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=6fac06949cc9821a7446d987df3dcc5b 840w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/webhooks/webhook-name.webp?w=1100&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=c6bdb704a5c9735bc1513fc1bcadfee5 1100w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/webhooks/webhook-name.webp?w=1650&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=139040b5aca1034247385a4f9c9813fb 1650w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/webhooks/webhook-name.webp?w=2500&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=348e99461ce86907bec9a3ac416778c4 2500w" />

    <Note>
      Your webhook endpoint should accept POST requests.
    </Note>
  </Step>

  <Step title="Configure events and filters">
    Select which events trigger webhooks and add any property filters:

        <img src="https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/webhooks/webhooks2.webp?fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=b3f0894fc03b6e45cf72dc23f19919c5" alt="webhook configuration" data-og-width="1326" width="1326" data-og-height="1258" height="1258" data-path="images/webhooks/webhooks2.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/webhooks/webhooks2.webp?w=280&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=9d2a16f400f146936df153304dce9545 280w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/webhooks/webhooks2.webp?w=560&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=31de3ca76c01613eaa4a0d4bc84c6d58 560w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/webhooks/webhooks2.webp?w=840&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=225d7a15f70ef1c3ca8212fdf37e31b9 840w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/webhooks/webhooks2.webp?w=1100&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=4c1ea92574b1d9ff7ac7db65690792e0 1100w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/webhooks/webhooks2.webp?w=1650&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=5dd461df9c87a5c1af53632979e21fc2 1650w, https://mintcdn.com/helicone/H0xDJmuTzfSrq5RW/images/webhooks/webhooks2.webp?w=2500&fit=max&auto=format&n=H0xDJmuTzfSrq5RW&q=85&s=05cd9da82d7bdb1e8945284490011bd3 2500w" />

    <Note>
      You can also create webhooks programmatically using our [REST API](/rest/webhooks/post-v1webhooks).
    </Note>
  </Step>

  <Step title="Secure your endpoint">
    Copy the HMAC key from the dashboard and validate webhook signatures:

    ```javascript  theme={null}
    import crypto from "crypto";

    function verifySignature(payload, signature, secret) {
      const hmac = crypto.createHmac("sha256", secret);
      hmac.update(JSON.stringify(payload));
      const calculatedSignature = hmac.digest("hex");
      
      return crypto.timingSafeEqual(
        Buffer.from(calculatedSignature, "hex"),
        Buffer.from(signature, "hex")
      );
    }
    ```
  </Step>
</Steps>

## Configuration Options

Configure your webhook behavior through the [dashboard](https://us.helicone.ai/webhooks) or [REST API](/rest/webhooks/post-v1webhooks):

### Basic Settings

| Setting             | Description                                          | Default |
| ------------------- | ---------------------------------------------------- | ------- |
| **Destination URL** | URL where webhook payloads are sent                  | None    |
| **Sample Rate**     | Percentage of requests that trigger webhooks (0-100) | 100%    |
| **Include Data**    | Include enhanced metadata and S3 URLs                | Enabled |

### Advanced Settings

| Setting              | Description                                              | Default |
| -------------------- | -------------------------------------------------------- | ------- |
| **Property Filters** | Only send webhooks for requests with specific properties | None    |

<AccordionGroup>
  <Accordion title="Property Filters">
    Filter webhooks based on custom properties you set in requests:

    ```javascript  theme={null}
    // In your LLM request
    headers: {
      "Helicone-Property-Environment": "production",
      "Helicone-Property-UserId": "user-123"
    }

    // Webhook filter configuration
    {
      "environment": "production",
      "userId": "user-123"
    }
    ```

    Only requests matching ALL specified properties will trigger webhooks.
  </Accordion>
</AccordionGroup>

## Use Cases

<Tabs>
  <Tab title="Compliance Monitoring">
    Monitor AI responses for regulatory compliance and policy violations:

    ```javascript  theme={null}
    export default async function handler(req, res) {
      const { request_id, request_response_url, user_id, metadata } = req.body;
      
      // Verify webhook signature
      if (!verifySignature(req.body, req.headers["helicone-signature"], process.env.WEBHOOK_SECRET)) {
        return res.status(401).json({ error: "Unauthorized" });
      }
      
      // Fetch complete interaction data
      const response = await fetch(request_response_url);
      const { request, response: llmResponse } = await response.json();
      
      const userMessage = request.messages[0].content;
      const aiResponse = llmResponse.choices[0].message.content;
      
      // Check for PII in user input
      const piiDetected = await detectPII(userMessage);
      if (piiDetected.found) {
        await complianceAlerts.sendPIIAlert({
          requestId: request_id,
          userId: user_id,
          piiTypes: piiDetected.types,
          content: userMessage
        });
      }
      
      // Monitor AI response for policy violations
      const policyCheck = await checkCompliancePolicy(aiResponse);
      if (policyCheck.violations.length > 0) {
        await complianceAlerts.sendPolicyViolation({
          requestId: request_id,
          violations: policyCheck.violations,
          severity: policyCheck.severity,
          content: aiResponse
        });
      }
      
      // Log compliance metrics
      await complianceLogger.log({
        requestId: request_id,
        timestamp: new Date().toISOString(),
        piiDetected: piiDetected.found,
        policyViolations: policyCheck.violations.length,
        complianceScore: policyCheck.score
      });
      
      return res.status(200).json({ message: "Compliance check completed" });
    }
    ```
  </Tab>

  <Tab title="Data Pipeline">
    Stream LLM data to external systems:

    ```javascript  theme={null}
    export default async function handler(req, res) {
      const { request_id, request_response_url, user_id, model } = req.body;
      
      // Fetch complete interaction data
      const response = await fetch(request_response_url);
      const fullData = await response.json();
      
      // Transform data for your analytics system
      const analyticsEvent = {
        id: request_id,
        userId: user_id,
        model: model,
        timestamp: new Date().toISOString(),
        prompt: fullData.request.messages[0].content,
        response: fullData.response.choices[0].message.content,
        metadata: req.body.metadata
      };
      
      // Send to your data pipeline
      await Promise.all([
        // Send to analytics platform
        analytics.track(analyticsEvent),
        
        // Store in data warehouse
        dataWarehouse.store(analyticsEvent),
        
        // Update real-time dashboards
        dashboards.updateMetrics(analyticsEvent)
      ]);
      
      return res.status(200).json({ message: "Data processed" });
    }
    ```
  </Tab>
</Tabs>

## Understanding Webhooks

### Webhook Payload Structure

Webhooks deliver structured data about completed LLM requests:

**Standard payload:**

```json  theme={null}
{
  "request_id": "550e8400-e29b-41d4-a716-446655440000",
  "user_id": "user-123", // Only if set in original request
  "request_body": "truncated-request-data",
  "response_body": "truncated-response-data"
}
```

**Enhanced payload (when `include_data` is enabled):**

```json  theme={null}
{
  "request_id": "550e8400-e29b-41d4-a716-446655440000",
  "user_id": "user-123",
  "request_body": "truncated-request-data", 
  "response_body": "truncated-response-data",
  "request_response_url": "https://s3-url-containing-full-data",
  "model": "gpt-4o-mini",
  "provider": "openai",
  "metadata": {
    "cost": 0.0015,
    "promptTokens": 10,
    "completionTokens": 15,
    "totalTokens": 25,
    "latencyMs": 1200
  }
}
```

### Request/Response URL Data

The `request_response_url` contains complete, untruncated data:

```javascript  theme={null}
// Fetch complete data
const response = await fetch(request_response_url);
const { request, response: llmResponse } = await response.json();

// Access full request data
console.log("Model:", request.model);
console.log("Messages:", request.messages);
console.log("Parameters:", request.temperature, request.max_tokens);

// Access full response data  
console.log("Response:", llmResponse.choices[0].message.content);
console.log("Usage:", llmResponse.usage);
console.log("Finish reason:", llmResponse.choices[0].finish_reason);
```

### Security Best Practices

**Always verify webhook signatures:**

```javascript  theme={null}
function verifyWebhookSignature(payload, signature, secret) {
  const hmac = crypto.createHmac("sha256", secret);
  hmac.update(JSON.stringify(payload));
  const calculatedSignature = hmac.digest("hex");
  
  return crypto.timingSafeEqual(
    Buffer.from(calculatedSignature, "hex"),
    Buffer.from(signature, "hex")
  );
}

// In your webhook handler
const isValid = verifyWebhookSignature(
  req.body,
  req.headers["helicone-signature"],
  process.env.HELICONE_WEBHOOK_SECRET
);

if (!isValid) {
  return res.status(401).json({ error: "Invalid signature" });
}
```

### Performance Considerations

**URL expiration:**

* `request_response_url` expires after 30 minutes
* Always use `request_response_url` for complete data

**Webhook timeouts:**

* Webhook delivery times out after 2 minutes

**Payload size limits:**

* Request/response bodies are truncated at 10KB in webhook payload

## Related Features

<CardGroup cols={2}>
  <Card title="Scores" icon="star" href="/features/advanced-usage/scores">
    Score LLM responses automatically via webhooks for quality monitoring
  </Card>

  <Card title="Custom Properties" icon="tag" href="/features/advanced-usage/custom-properties">
    Add metadata to requests for filtering and organizing webhook deliveries
  </Card>

  <Card title="User Metrics" icon="chart-line" href="/features/advanced-usage/user-metrics">
    Track per-user usage patterns and costs via webhook data
  </Card>

  <Card title="Local Testing" icon="laptop" href="/features/webhooks-testing">
    Test webhooks locally using ngrok or other tunneling tools
  </Card>
</CardGroup>

***

<Accordion title="Need more help?">
  Additional questions or feedback? Reach out to
  [help@helicone.ai](mailto:help@helicone.ai) or [schedule a
  call](https://cal.com/team/helicone/helicone-discovery) with us.
</Accordion>

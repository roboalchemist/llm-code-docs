# Source: https://docs.edgeimpulse.com/tutorials/topics/lifecycle-management/ota-particle-webhook.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Particle Webhook

## Setting Up Particle Webhook for Edge Impulse Ingestion

This guide supplements the tutorial on OTA Model Updates with Edge Impulse on Particle Workbench, focusing on configuring a Particle webhook for sending data to the Edge Impulse ingestion API.

### Steps for Webhook Configuration:

1. **Access Particle Console**:
   * Visit [Particle Console](https://console.particle.io).
   * Log in with your Particle account credentials.

2. **Navigate to Integrations**:
   * Click on the "Integrations" tab in the left-hand menu.
   * Select "Webhooks" from the available options.

3. **Create a New Webhook**:
   * Click "New Integration".
   * Choose "Webhook".

4. **Webhook Configuration**:
   * **Name**: Assign a descriptive name to your webhook.
   * **Event Name**: Specify the event name that triggers the webhook (e.g., "edge/ingest").
   * **URL**: Set this to the Edge Impulse ingestion API URL, typically something like `https://ingestion.edgeimpulse.com/api/training/data`.
   * **Request Type**: Choose "POST".
   * **Request Format**: Select "Custom".

5. **Custom Request Body**:
   * Input the JSON structure required by Edge Impulse. This will vary based on your project's data schema.

6. **HTTP Headers**:
   * Add necessary headers:
     * `x-api-key`: Your Edge Impulse API key.
     * `Content-Type`: "application/json".
     * `x-file-name`: Use a dynamic data field like `{{PARTICLE_EVENT_NAME}}`.

7. **Advanced Settings**:
   * **Response Topic**: Create a custom topic for webhook responses, e.g., `{{PARTICLE_DEVICE_ID}}/hook-response/{{PARTICLE_EVENT_NAME}}`.
   * **Enforce SSL**: Choose "Yes" for secure transmission.

8. **Save the Webhook**:
   * After entering all details, click "Save".

9. **Test the Webhook**:
   * Use example device firmware to trigger the webhook.
   * Observe the responses in the Particle Console.

10. **Debugging**:

* If errors occur, review the logs for detailed information.
* Ensure payload format aligns with Edge Impulse requirements.
* Verify the accuracy of your API key and other details.

### Custom Template Example:

Copy and paste the following into the Custom Template section of the webhook:

```json  theme={"system"}
{
    "name": "edgeimpulse.com",
    "event": "edge/ingest",
    "responseTopic": "",
    "disabled": true,
    "url": "http://ingestion.edgeimpulse.com/api/training/data",
    "requestType": "POST",
    "noDefaults": true,
    "rejectUnauthorized": false,
    "headers": {
        "x-api-key": "ei_1855db...",
        "x-file-name": "{{PARTICLE_EVENT_NAME}}",
        "x-label": "coffee"
    },
    "json": "{\n  \"payload\": {\n    \"device_name\": \"0a10a...\",\n    \"device_type\": \"photon2\",\n    \"interval_ms\": 20,\n    \"sensors\": [\n      {\n        \"name\": \"volt\",\n        \"units\": \"V\"\n      },\n      {\n        \"name\": \"curr\",\n        \"units\": \"A\"\n      }\n    ],\n    \"values\": [\n{{{PARTICLE_EVENT_VALUE}}}\n    ]\n  },\n  \"protected\": {\n    \"alg\": \"none\",\n    \"ver\": \"v1\"\n  },\n  \"signature\": \"00\"\n}"
}
[]: # (end)

```

### Additional Resources:

* [Particle Webhooks Documentation](https://docs.particle.io/reference/device-cloud/webhooks/)
* [Particle Webhooks Tutorial](https://docs.particle.io/tutorials/device-cloud/webhooks/)
* [Particle Webhooks API](https://docs.particle.io/reference/cloud-apis/api/#integrations-webhooks-)
* [Edge Impulse Ingestion API](/apis/ingestion)


Built with [Mintlify](https://mintlify.com).
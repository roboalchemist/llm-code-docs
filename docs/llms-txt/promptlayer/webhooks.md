# Source: https://docs.promptlayer.com/features/prompt-registry/webhooks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.promptlayer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Webhooks

Webhooks can be set up to receive notifications about changes to prompt templates. This functionality is particularly useful for storing prompts in cache, allowing for quicker retrieval without slowing down releases.

### Event Payload Format

When an event occurs, we send a POST request with a payload in this structure:

```json  theme={null}
{
  "event_type": "string",
  "details": "object",
  "user_id": "number",
  "user_name": "string or null",
  "user_email": "string or null",
  "workspace_id": "number",
  "timestamp": "ISO 8601 format timestamp",
}
```

### Supported Event Types

We notify you for these events:

| Event Type                                   | Description                                                                                                                                                                                                | Details                                                                                                                                                                                                                                  |
| -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `prompt_template_version_created`            | When a new version of a prompt template is created.                                                                                                                                                        | <ul><li>`prompt_template_name` (string)</li><li>`prompt_template_version_number` (number)</li><li>`prompt_template_id` (number)</li></ul>                                                                                                |
| `prompt_template_name_changed`               | When a prompt template's name is changed.                                                                                                                                                                  | <ul><li>`prompt_template_id` (number)</li><li>`prompt_template_name` (string)</li><li>`old_prompt_template_name` (string)</li></ul>                                                                                                      |
| `prompt_template_deleted`                    | When a prompt template is deleted.                                                                                                                                                                         | <ul><li>`prompt_template_id` (number)</li><li>`prompt_template_name` (string)</li></ul>                                                                                                                                                  |
| `prompt_template_label_created`              | When a new release label for a prompt template is created.                                                                                                                                                 | <ul><li>`prompt_template_id` (number)</li><li>`prompt_template_name` (string)</li><li>`prompt_template_version_number` (number)</li><li>`prompt_template_label` (string)</li></ul>                                                       |
| `prompt_template_label_deleted`              | When a release label for a prompt template is deleted.                                                                                                                                                     | <ul><li>`prompt_template_id` (number)</li><li>`prompt_template_name` (string)</li><li>`prompt_template_version_number` (number)</li><li>`prompt_template_label` (string)</li></ul>                                                       |
| `prompt_template_label_moved`                | When a release label is moved between prompt template versions.                                                                                                                                            | <ul><li>`prompt_template_id` (number)</li><li>`prompt_template_name` (string)</li><li>`prompt_template_version_number` (number)</li><li>`old_prompt_template_version_number` (number)</li><li>`prompt_template_label` (string)</li></ul> |
| `prompt_template_label_change_requested`     | When a change to a protected release label is requested and requires approval.                                                                                                                             | <ul><li>`prompt_template_id` (number)</li><li>`prompt_template_name` (string)</li><li>`prompt_template_label` (string)</li><li>`change_type` (string: "move" or "deletion")</li></ul>                                                    |
| `prompt_template_label_change_approved`      | When a pending change to a protected release label is approved.                                                                                                                                            | <ul><li>`prompt_template_id` (number)</li><li>`prompt_template_name` (string)</li><li>`prompt_template_label` (string)</li><li>`change_type` (string: "move" or "deletion")</li></ul>                                                    |
| `prompt_template_label_change_denied`        | When a pending change to a protected release label is denied.                                                                                                                                              | <ul><li>`prompt_template_id` (number)</li><li>`prompt_template_name` (string)</li><li>`prompt_template_label` (string)</li><li>`change_type` (string: "move" or "deletion")</li></ul>                                                    |
| `prompt_template_updated`                    | When a snippet imported in a prompt template is updated.                                                                                                                                                   | <ul><li>`prompt_template_id` (number)</li><li>`prompt_template_name` (string)</li><li>`prompt_template_version_number` (number)</li></ul>                                                                                                |
| `agent_run_finished`                         | When an agent (workflow) run is completed. <br /><br /> Note: This event may fire multiple times for the same execution and is not triggered for runs from the dashboard, only when called via SDK or API. | <ul><li>`agent_name` (string)</li><li>`agent_id` (number)</li><li>`agent_execution_id` (number)</li></ul>                                                                                                                                |
| `report_finished`                            | When a evaluation report is completed.                                                                                                                                                                     | <ul><li>`report_id` (number)</li><li>`report_name` (string)</li></ul>                                                                                                                                                                    |
| `dataset_version_created_by_file`            | When a dataset version is successfully created from a file upload.                                                                                                                                         | <ul><li>`dataset_id` (number)</li><li>`dataset_version_number` (number)</li></ul>                                                                                                                                                        |
| `dataset_version_created_by_file_failed`     | When dataset file processing fails.                                                                                                                                                                        | <ul><li>`error_message` (string)</li></ul>                                                                                                                                                                                               |
| `dataset_version_created_from_filter_params` | When a dataset version is created from filter parameters.                                                                                                                                                  | <ul><li>`dataset_id` (number)</li><li>`rows_added` (number)</li><li>`dataset_version_number` (number)</li></ul>                                                                                                                          |

### Example Payload

```json  theme={null}
{
  "event_type":"prompt_template_label_moved",
  "details":{
    "prompt_template_id":12,
    "prompt_template_name":"Hello",
    "prompt_template_version_number":9,
    "old_prompt_template_version_number":8,
    "prompt_template_label":"prod"
  },
  "user_id":1,
  "user_name":"John Doe",
  "user_email":"john.doe@example.com",
  "workspace_id":1,
  "timestamp":"2023-12-01T22:05:57.924833"
}
```

### Configuring a Webhook

To set up a webhook, go to the **Webhook** section in the **Settings** page. Enter the URL of the endpoint you want to send the webhook to and click **Submit**.

<img src="https://mintcdn.com/promptlayer/v0RzaTvbzopITX7U/images/webhooks-form.png?fit=max&auto=format&n=v0RzaTvbzopITX7U&q=85&s=9fcbc2bbe5af10959ee4fffd9baa4249" alt="Creating Webhook" data-og-width="1166" width="1166" data-og-height="472" height="472" data-path="images/webhooks-form.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/v0RzaTvbzopITX7U/images/webhooks-form.png?w=280&fit=max&auto=format&n=v0RzaTvbzopITX7U&q=85&s=c218a7fe3032ccd0a599e3df62a6eafb 280w, https://mintcdn.com/promptlayer/v0RzaTvbzopITX7U/images/webhooks-form.png?w=560&fit=max&auto=format&n=v0RzaTvbzopITX7U&q=85&s=e642d75b99fba7688e4fd086c5aef028 560w, https://mintcdn.com/promptlayer/v0RzaTvbzopITX7U/images/webhooks-form.png?w=840&fit=max&auto=format&n=v0RzaTvbzopITX7U&q=85&s=d6ccbb108031ac2c89d7fca87b2fb50c 840w, https://mintcdn.com/promptlayer/v0RzaTvbzopITX7U/images/webhooks-form.png?w=1100&fit=max&auto=format&n=v0RzaTvbzopITX7U&q=85&s=fc9d0aba80cd3ff60bb2c67b5e05a1ef 1100w, https://mintcdn.com/promptlayer/v0RzaTvbzopITX7U/images/webhooks-form.png?w=1650&fit=max&auto=format&n=v0RzaTvbzopITX7U&q=85&s=642f17467b9fb70356c4bb5817b1af5e 1650w, https://mintcdn.com/promptlayer/v0RzaTvbzopITX7U/images/webhooks-form.png?w=2500&fit=max&auto=format&n=v0RzaTvbzopITX7U&q=85&s=70f38c817201bc64c8014016bd807d86 2500w" />

### Securing Your Webhook

When you create a webhook, you'll receive a webhook secret signature that looks like this:

<img src="https://mintcdn.com/promptlayer/v0RzaTvbzopITX7U/images/webhook-secret-signature.png?fit=max&auto=format&n=v0RzaTvbzopITX7U&q=85&s=9d2095002aa831c5352e372ade4f5d05" alt="Webhook Secret Signature" data-og-width="1732" width="1732" data-og-height="1272" height="1272" data-path="images/webhook-secret-signature.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/v0RzaTvbzopITX7U/images/webhook-secret-signature.png?w=280&fit=max&auto=format&n=v0RzaTvbzopITX7U&q=85&s=78835594a4da91e1bb74dc785a2b7c93 280w, https://mintcdn.com/promptlayer/v0RzaTvbzopITX7U/images/webhook-secret-signature.png?w=560&fit=max&auto=format&n=v0RzaTvbzopITX7U&q=85&s=8bf5ca9889b4dd438fe96dd7a0ab4d5d 560w, https://mintcdn.com/promptlayer/v0RzaTvbzopITX7U/images/webhook-secret-signature.png?w=840&fit=max&auto=format&n=v0RzaTvbzopITX7U&q=85&s=48e00c71118cd008dc56c4002bb64b97 840w, https://mintcdn.com/promptlayer/v0RzaTvbzopITX7U/images/webhook-secret-signature.png?w=1100&fit=max&auto=format&n=v0RzaTvbzopITX7U&q=85&s=de60097cd154a0226ae0e73b171755b9 1100w, https://mintcdn.com/promptlayer/v0RzaTvbzopITX7U/images/webhook-secret-signature.png?w=1650&fit=max&auto=format&n=v0RzaTvbzopITX7U&q=85&s=22b84eb64b73243dfd8793dfaf712840 1650w, https://mintcdn.com/promptlayer/v0RzaTvbzopITX7U/images/webhook-secret-signature.png?w=2500&fit=max&auto=format&n=v0RzaTvbzopITX7U&q=85&s=5ae163546f278af060aebb3bf837988a 2500w" />

This secret is used to verify that incoming webhook requests are authentic and come from PromptLayer. The signature is included in the `X-PromptLayer-Signature` header of each webhook request.

#### Verifying Webhook Signatures

Here are code examples showing how to verify the signatures:

<CodeGroup>
  ```python Python theme={null}

  import hmac
  import hashlib
  import json

  signature = "HEADER FROM X-PromptLayer-Signature" # Replace with actual header value
  secret_key = "SECRET KEY FROM PROMPTLAYER DASHBOARD" # Replace with actual secret key
  payload = {} # Replace with actual payload
  payload_str = json.dumps(payload, sort_keys=True)
  expected_signature = hmac.new(
      key=secret_key.encode(),
      msg=payload_str.encode('utf-8'),
      digestmod=hashlib.sha256
  ).hexdigest()

  if hmac.compare_digest(expected_signature, signature):
      print("Signature is valid")
  else:
      print("Signature is invalid")
  ```

  ```javascript JavaScript theme={null}
  import crypto from "crypto";
  import stringify from "json-stable-stringify";

  // Replace these with actual values
  const signature = "HEADER FROM X-PromptLayer-Signature"; // From request header
  const secretKey = "SECRET KEY FROM PROMPTLAYER DASHBOARD"; // Your webhook secret
  const payload = {}; // Replace with actual request body

  export function formatPayload(payload) {
    const raw = stringify(payload);
    const spacedColons = raw.replace(/"([^"]+)"\s*:/g, '"$1": ');
    const spaced = spacedColons.replace(/,(?=(?:\s*[\{"\[]))/g, ", ");
    return spaced;
  }

  export function generateSignature(payload, secretKey) {
    const normalized = formatPayload(payload);
    return crypto
      .createHmac("sha256", secretKey)
      .update(normalized)
      .digest("hex");
  }

  export function verifySignature(signature, payload, secretKey) {
    const expected = generateSignature(payload, secretKey);
    try {
      return crypto.timingSafeEqual(
        Buffer.from(signature, "hex"),
        Buffer.from(expected, "hex")
      );
    } catch {
      return false;
    }
  }
   
  const isValid = verifySignature(signature, payload, secretKey);
  console.log("Signature is", isValid ? "valid" : "invalid");
  ```
</CodeGroup>

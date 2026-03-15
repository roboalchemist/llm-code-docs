# Source: https://docs.firehydrant.com/docs/runbook-step-send-a-webhook.md

# Send a Webhook

<Image alt="Send a Webhook Runbook step" align="center" width="650px" src="https://files.readme.io/119aff8-image.png">
  Send a Webhook Runbook step
</Image>

If you have internal systems that perform tasks like rolling back deployments, you may want to dispatch an HTTP request from FireHydrant to those systems. This article explains how to set up a Runbook step that sends a webhook to an endpoint of your choice.

## Configuration

1. To add this step, go to Create a Runbook or Edit an existing Runbook and click "+ Add Step."
2. Search for "webhook" and then click the step.
3. This step contains the following available fields:
   1. **Endpoint** - The destination endpoint to send the request
   2. **HMAC Secret** - A short string you define and use to verify that the webhook came from FireHydrant in your application
   3. **JSON Payload** - The JSON payload to send. This field supports [Template Variables](https://docs.firehydrant.com/docs/template-variables).
   4. **JSON Headers** - You can specify the necessary request headers here.

### GET, PATCH, DELETE Requests

By default, the Webhook step's method is `POST`. To override this, specify an additional argument in the **JSON Headers** for `X-HTTP-Method-Override`, like so:

```json
{
  "Content-Type": "application/json",
  "Authorization": "Bearer example-token-123",
  "X-HTTP-Method-Override": "PATCH"
}
```

## JSON Payload Templating

You can format the payload to your endpoint however you like, as long as the result is in valid JSON format. If you'd like to include a JSON version of certain payload parts, you can also use liquid filters to convert input to JSON. For example:

This converts the `labels` attribute on the incident to JSON so it can easily be sent in the JSON payload:

```json Example JSON Body w/ Liquid
{
  "incident_id": "{{ incident.id }}",
  "labels": {{ incident.labels | toJSON }}
}
```

> 📘 Note:
>
> If you are sending incident data or parameters that may contain new lines (e.g. Incident Description, Customer Impact, etc.), make sure you use `toJSON` to escape the newlines, otherwise it will insert as literal newlines in the request body making it invalid.

## Signature Verification

Every payload request you receive from FireHydrant will have a `fh-signature` header containing the computed signature of your HMAC Secret and the JSON payload. FireHydrant uses SHA256 to compute the signature.

Using Ruby as an example, you could use the following code to calculate the signature with the secret key and check it against the one received:

```ruby
key = "super-secret-key"
data = request.body
signature = headers['Fh-Signature']
if signature == OpenSSL::HMAC.hexdigest("SHA256", key, data)
    # perform taskend
```

## Organization Secrets

This Runbook step is currently the only step that can access [Secrets](https://docs.firehydrant.com/docs/secrets) via Liquid templating. To learn more about hiding and encrypting secret values, visit the [documentation on Secrets](https://docs.firehydrant.com/docs/secrets).
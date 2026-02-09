# Source: https://smartcar.com/docs/integrations/webhooks/callback-verification.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Callback URI Verification

> Verify your webhook endpoint can receive deliveries

<Info>
  **This page covers initial endpoint verification.** For verifying webhook payload signatures from vehicles, see [Payload Verification](/integrations/webhooks/payload-verification).
</Info>

When you create a webhook or update a callback URI in the Smartcar Dashboard, Smartcar sends a one-time `VERIFY` event to confirm your endpoint is ready. Your endpoint must respond correctly before Smartcar will deliver any vehicle data.

## The VERIFY Event

Smartcar sends a challenge request to your callback URI in this format:

<CodeGroup>
  ```json Version 4.0 (NEW) theme={null}
  {
    "eventId": "52f6e0bb-1369-45da-a61c-9e67d092d6db",
    "eventType": "VERIFY",
    "data": {
      "challenge": "<random-string>"
    },
    "meta": {
      "version": "4.0",
      "webhookId": "5a8e5e38-1e12-4011-a36d-56f120053f9e",
      "webhookName": "Example Webhook",
      "deliveryId": "5d569643-3a47-4cd1-a3ec-db5fc1f6f03b",
      "deliveredAt": "2025-07-31T19:38:42.332Z"
    }
  }
  ```

  ```json Version 2.0 theme={null}
  {
    "version": "2.0",
    "webhookId": "<uuid>",
    "eventName": "verify",
    "payload": { 
      "challenge": "<random-string>" 
    }
  }
  ```
</CodeGroup>

## Required Response

Your endpoint must respond with:

1. **Status code**: `200 OK`
2. **Content-Type header**: `application/json`
3. **Response body**: A JSON object containing the HMAC-SHA256 hash of the challenge

### Generate the HMAC

Create an HMAC-SHA256 hash of the `challenge` string using your **Application Management Token** as the secret key:

<Tip>
  Our [backend SDKs](/api-reference/api-sdks) have helper methods to generate the HMAC.
</Tip>

<CodeGroup>
  ```js Node theme={null}
      let hmac = smartcar.hashChallenge(
          application_management_token, 
          payload.challenge
      ); 
  ```

  ```python Python theme={null}
      hmac = smartcar.hash_challenge(
              application_management_token, 
              payload.challenge
          )
  ```

  ```java Java theme={null}
  String hmac =  Smartcar.hashChallenge(
              application_management_token, 
              payload.challenge
          );
  ```

  ```ruby Ruby theme={null}
      hmac = Smartcar.hash_challenge(
          application_management_token, 
          payload.challenge
      )
  ```
</CodeGroup>

### Return the Response

Return the hex-encoded hash in your response body with the key `challenge`:

```json Response Body theme={null}
{
  "challenge": "{HMAC-hex-string}"
}
```

<Warning>
  If your endpoint fails to respond correctly within 15 seconds, Smartcar will not activate the webhook. You can retry verification from the Dashboard at any time.
</Warning>

***

## Verify webhook challenges inside the Dashboard

Use the Smartcar Dashboard to understand exactly what Smartcar expects before you enable webhooks in production. The **Verify webhook** modal shows a sample challenge string plus language-specific snippets so you can implement the same HMAC signature in your code.

<Frame>
    <img src="https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge.png?fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=9106c3a746b703281d6fc2ada9bd6249" alt="" data-og-width="1344" width="1344" data-og-height="1095" height="1095" data-path="images/changelog/webhook-challenge.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge.png?w=280&fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=2af7016d356c723b2c5f2abf8f55e130 280w, https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge.png?w=560&fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=c402b715adfe634727c3db3777518002 560w, https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge.png?w=840&fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=663b8794492a757bc94bb456642ba025 840w, https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge.png?w=1100&fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=c94a590072ee00fe31f2381424ab4866 1100w, https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge.png?w=1650&fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=c36a0f87b244b4a1915d30d9440724c0 1650w, https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge.png?w=2500&fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=f4870c0fed07dab78526f68c81bd989a 2500w" />
</Frame>

<Steps>
  <Step title="Implement the signature in your handler">
    Copy the challenge string from the modal and use the embedded snippets (Python, Node, Java, or Ruby) as references while you code the signature logic on your server. Run your handler locally or in staging so it is ready to answer Smartcar’s challenge.
  </Step>

  <Step title="Trigger Smartcar’s verification call">
    Once your server is ready, click **Verify this webhook**. Smartcar sends the challenge payload to your callback URL, and your code responds with the signature it just produced.
  </Step>

  <Step title="Compare expected vs actual responses">
    The Response tab displays the HTTP status, the challenge Smartcar sent, the signature Smartcar expected, and the body your server returned. Use this side-by-side view to confirm success or adjust your implementation before retrying.
  </Step>
</Steps>

<Frame>
    <img src="https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge-calculator.png?fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=12cd5091ce9d0c9f0355569227931374" alt="" data-og-width="1344" width="1344" data-og-height="1095" height="1095" data-path="images/changelog/webhook-challenge-calculator.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge-calculator.png?w=280&fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=01c41a08770277ac722cf56d2207755d 280w, https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge-calculator.png?w=560&fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=eb0f7b5c79d5f1d5001cf2b4e0c1fc94 560w, https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge-calculator.png?w=840&fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=e6a0dedfdd279d20479326bcd0f855e2 840w, https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge-calculator.png?w=1100&fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=a8fe313d141c595525270f50f960da76 1100w, https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge-calculator.png?w=1650&fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=b671a190797c06c85e5fea49b0dab359 1650w, https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge-calculator.png?w=2500&fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=bc0b603ce9b29e082e1c5372681297e3 2500w" />
</Frame>

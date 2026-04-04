# Source: https://developers.cash.app/cash-app-pay-partner-api/guides/technical-guides/api-fundamentals/requests/using-api-keys.mdx

***

## stoplight-id: 07daf7ae5ecbe

# Using API Keys

Cash App Pay APIs are primarily authenticated using API keys. These keys are provisioned and rotated using automation. These keys can be used for different actions. Therefore, we recommend provisioning multiple API Keys with the lowest privilege required.

## First Instantiation

1. Using your provided client ID and client secret in the `Authorization` header for the request, [create an API key](/cash-app-pay-partner-api/api-reference/management-api/create-api-key) with `API_KEYS_READ` and `API_KEYS_WRITE` scopes
2. Using the newly created API Key (not your client secret), you should [create](/cash-app-pay-partner-api/api-reference/management-api/create-api-key) a new set of API keys with the payment/operational scopes required (`PAYMENTS_READ`, `PAYMENTS_WRITE`, etc.)
3. You can now make requests using the API key created in **Step 2** above.

## Before expiration

We strongly recommend rotating keys several days before they expire to provide a buffer for unexpected problems.

Use a key with the `API_KEYS_WRITE` scope to generate new keys for each key created in **Step 1** and **Step 2** under **First Instantiation**.

## FAQ

**Q: How long do API keys remain valid?**

**A:** API keys expire after 30 days. The `expires_at` field contains the exact expiration date.

**Q: Does generating a new key cause the previous one to expire?**

**A:** No, keys only expire based on their `expires_at` timestamp.

**Q: What are some of the technical notes about key rotations?**

**A:** These are some of the technical notes or "gotchas" that you must be aware of while using our API keys:

* Our webhooks are signed using whichever API Key is associated with the webhook configuration when the webhook event is delivered. Using your private key, you can decrypt the webhook’s signature and validate that its contents match the actual data, ensuring that the payload hasn’t been tampered with and that it authentically came from Cash App Pay. See more about [Signing Requests](/cash-app-pay-partner-api/guides/technical-guides/api-fundamentals/requests/signing-requests).<br />Therefore, your API key and webhook logic should be able to handle instances where a webhook is fired using key\_1, but you receive the webhook after the API Key has been rotated to key\_2.
* Depending on your infrastructure, you should also consider cases where—if you have multiple instances of your app—API Keys don’t propagate to all instances synchronously.
* You should also build in appropriate retry and escalation policies if API Keys fail to rotate in production to avoid service outages.

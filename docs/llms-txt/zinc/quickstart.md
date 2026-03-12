# Source: https://zinc-staging.vercel.app/docs/quickstart.md

> ## Documentation Index
> Fetch the complete documentation index at: https://zinc-staging.vercel.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Quickstart

> Get started with Zinc API in minutes.

<Steps>
  <Step title="Create your Zinc account" stepNumber={1}>
    <a href="https://app.zinc.com" target="_blank">Sign up here</a> to get started. You will need to deposit funds into your Zinc account to use the API.
  </Step>

  <Step title="Get Your API Credentials" stepNumber={2}>
    After signing up, visit your <a href="https://app.zinc.com" target="_blank">Zinc dashboard</a> to find your client token.
  </Step>

  <Step title="Make Your First API Call" stepNumber={3}>
    Here's h ow to place an order using `curl`:

    ```bash  theme={null}
    export ZINC_API_KEY=<api_key>;
    curl -X POST https://api.zinc.com/orders \
        -H "Authorization: Bearer $ZINC_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{
          "products": [{
            "url": "https://www.zinc.com/shop/stickers",
            "quantity": 1
          }],
          "max_price": 100,
          "shipping_address": {
            "first_name": "...",
            "last_name": "...",
            "address_line1": "...",
            "address_line2": null,
            "city": "...",
            "state": "...",
            "postal_code": "...",
            "phone_number": "..."
          }
        }';
    ```

    <Info>
      Replace <code>\<api\_key></code> with your actual token. Never share your client token publicly.
    </Info>

    If successful, you'll get a successful JSON response with the request data. The order will now show
    up in your dashboard.
  </Step>
</Steps>

***

Need help? <a href="mailto:support@zinc.com">Contact support</a> or check out the [What is Zinc?](/what-is-zinc) page for more info.


Built with [Mintlify](https://mintlify.com).
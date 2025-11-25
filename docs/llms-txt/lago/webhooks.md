# Source: https://getlago.com/docs/guide/webhooks.md

# Webhooks

When using Lago, the app generates [several events](/api-reference/webhooks/messages) that you can listen to in order to trigger workflows. Each time an event is generated, you can view it in the Lago application using the webhook logs. This allows you to take a closer look at the generated events, detect possible errors, and retry them.

## Adding a webhook URL

To add a webhook endpoint via the Lago app, follow these steps:

1. Go to the **Developers** section via the sidebar;
2. Open the **Webhooks** tab;
3. Click **Add a webhook**;
4. Enter the webhook URL;
5. Choose the webhook signature between JWT and HMAC; and
6. Click **Add webhook** to confirm.

<Info>
  Note that you can add up to 10 webhook endpoints.
</Info>

## The webhook signature

By creating a webhook endpoint, you have two signature options.

<Tabs>
  <Tab title="Dashboard">
    * The first is `JWT`, with a possibly lengthy payload header and potential size limits;
    * The second is `HMAC`, which features a shorter payload header and no size restrictions.

    <Frame caption="Webhook endpoint signature">
      <img src="https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/webhook-signature.png?fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=86200416b2a5959b4f8b25233010f9d5" data-og-width="2128" width="2128" data-og-height="1300" height="1300" data-path="guide/images/webhook-signature.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/webhook-signature.png?w=280&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=6e7363d9cbb2e16caec24f0f7932ee2d 280w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/webhook-signature.png?w=560&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=6bf8451936b443056bd61f27da7f5249 560w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/webhook-signature.png?w=840&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=4d529141b427569ac5181c21c03a36a8 840w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/webhook-signature.png?w=1100&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=ff5df538ab0f1b2abed040f0babeae4d 1100w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/webhook-signature.png?w=1650&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=c78979561a4520c9ccd087f4d3063d80 1650w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/webhook-signature.png?w=2500&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=e20c67cf5efd9983eca20338288a6d82 2500w" />
    </Frame>
  </Tab>

  <Tab title="API">
    <CodeGroup>
      ```bash Choosing the webhook signature theme={"dark"}
      LAGO_URL="https://api.getlago.com"
      API_KEY="__YOUR_API_KEY__"

      curl --location --request POST "$LAGO_URL/api/v1/webhook_endpoints" \
        --header "Authorization: Bearer $API_KEY" \
        --header 'Content-Type: application/json' \
        --data-raw '{
          "webhook_endpoint": {
            "webhook_url": "https://foo.bar",
            "signature_algo": "hmac"
          }
        }'
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Locate your HMAC signature token

To find your HMAC signature token, navigate to **Developers > Webhooks** and locate the **HMAC Signature Token**. Then, reveal and copy the key.

<Frame caption="Locate your HMAC siganture token">
  <img src="https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/hmac-signature-token.png?fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=28386bce4de7802dd35bfa95d944df9f" data-og-width="2720" width="2720" data-og-height="1672" height="1672" data-path="guide/images/hmac-signature-token.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/hmac-signature-token.png?w=280&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=1173c2a642fbe6ba5f916ca1452d0077 280w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/hmac-signature-token.png?w=560&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=a7e991595ec2516790e3d33a0f672124 560w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/hmac-signature-token.png?w=840&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=9e40354356eae1cbf92866ac46a83e29 840w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/hmac-signature-token.png?w=1100&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=db59f6db5f2b7b93b9c415e951fdbc3a 1100w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/hmac-signature-token.png?w=1650&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=46e2708dda1df0c65c16f60f173bf2b9 1650w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/hmac-signature-token.png?w=2500&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=f5407e14524e7375e214cbbef2e126e3 2500w" />
</Frame>

## Accessing the webhook logs

Once a webhook is registered in the app, you can access the webhook logs:

1. Go to the **Developers** section via the sidebar;
2. Open the **Webhooks** tab;
3. Click on the webhook endpoint to see the list of events; and
4. Click the reload icon to see new events (optional).

<Frame caption="Webhook logs">
  <img src="https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/webhook-logs.png?fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=915eaee9d5ef1281a68a1d92e8608ef1" data-og-width="2922" width="2922" data-og-height="1876" height="1876" data-path="guide/images/webhook-logs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/webhook-logs.png?w=280&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=8784d75aa247121993863d81e040bb4a 280w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/webhook-logs.png?w=560&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=85b5eb3f5a24030c111e3919b84d1638 560w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/webhook-logs.png?w=840&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=8f46ac92702b8ce716a9ae5e3bcafcab 840w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/webhook-logs.png?w=1100&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=5c546878d3f0328694cf70b2d70d0f8f 1100w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/webhook-logs.png?w=1650&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=08ee5ad8ee10ec9b4725adac75678c49 1650w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/webhook-logs.png?w=2500&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=586fc6260ecc836d36c92e56f6b0ec8f 2500w" />
</Frame>

## Accessing a specific event

You can see the details of a specific event by clicking on it. Depending on the event status, you will have access to two or three main blocks:

1. **A list of properties, including:**
   1. **Timestamp:** the timestamp of the event;
   2. **Webhook URL:** the URL used to listen to events;
   3. **Unique key:** idempotency key associated with the event;
   4. **Webhook type:** the webhook type used to understand the action triggered;
   5. **Response:** the response code (i.e. acknowledgement of receipt);
   6. **Number of retries:** if the event failed, the number of retries attempted;
2. **A JSON snippet with the arguments sent by Lago; and**
3. **If the event failed, an error response will be included.**

## Errors and retries

Your webhook server should response with a 2xx (`200`, `201`, `202`, `204`) status code to acknowledge the receipt of the event. If the response is not supported as a success, Lago will consider it as failed.
Some events generated by Lago may not be received on the user side, which is why Lago displays an error status in the user interface.

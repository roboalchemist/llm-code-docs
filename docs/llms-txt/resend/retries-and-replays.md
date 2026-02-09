# Source: https://resend.com/docs/webhooks/retries-and-replays.md

> ## Documentation Index
> Fetch the complete documentation index at: https://resend.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Retries and Replays

> Learn how to use the retries and replays to handle webhook failures.

## Automatic Retries

We attempt to deliver each webhook message based on a schedule with exponential backoff.

Each message is attempted based on the following schedule, where each period is started following the failure of the preceding attempt:

* Immediately
* 5 seconds
* 5 minutes
* 30 minutes
* 2 hours
* 5 hours
* 10 hours
* 10 hours (in addition to the previous)

If an endpoint is removed or disabled delivery attempts to the endpoint will be disabled as well.

To see when a message will be retried next, check the webhook message details in the dashboard.

For example, an attempt that fails three times before eventually succeeding will be delivered roughly 35 minutes and 5 seconds following the first attempt.

## Manual Replays

If a webhook message fails, you can manually replay it.

You can replay both `failed` and `succeeded` webhook messages.

<img alt="Replay Webhook" src="https://mintcdn.com/resend/qZ1nhePh39wY_UO4/images/webhooks-replay-1.jpg?fit=max&auto=format&n=qZ1nhePh39wY_UO4&q=85&s=aeae9936eeea92d71da580af9f82cbb5" data-og-width="1476" width="1476" data-og-height="448" height="448" data-path="images/webhooks-replay-1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/qZ1nhePh39wY_UO4/images/webhooks-replay-1.jpg?w=280&fit=max&auto=format&n=qZ1nhePh39wY_UO4&q=85&s=ee31d3927e2c86ecc5a42ca25874ede0 280w, https://mintcdn.com/resend/qZ1nhePh39wY_UO4/images/webhooks-replay-1.jpg?w=560&fit=max&auto=format&n=qZ1nhePh39wY_UO4&q=85&s=f6f6b06c7f816f3de687b5a5aba6e23b 560w, https://mintcdn.com/resend/qZ1nhePh39wY_UO4/images/webhooks-replay-1.jpg?w=840&fit=max&auto=format&n=qZ1nhePh39wY_UO4&q=85&s=84e8fd0104b1303705560333960f23fa 840w, https://mintcdn.com/resend/qZ1nhePh39wY_UO4/images/webhooks-replay-1.jpg?w=1100&fit=max&auto=format&n=qZ1nhePh39wY_UO4&q=85&s=54f4ff5ff9d21bb63ff473f2d674260d 1100w, https://mintcdn.com/resend/qZ1nhePh39wY_UO4/images/webhooks-replay-1.jpg?w=1650&fit=max&auto=format&n=qZ1nhePh39wY_UO4&q=85&s=ad23a45979c1f0b31074eae093dd834a 1650w, https://mintcdn.com/resend/qZ1nhePh39wY_UO4/images/webhooks-replay-1.jpg?w=2500&fit=max&auto=format&n=qZ1nhePh39wY_UO4&q=85&s=b51f0e14690599ba97c4b8beaf983351 2500w" />

Here's how to replay a webhook message:

1. Go to the [Webhooks](https://resend.com/webhooks) page
2. Navigate to the Webhook Endpoint you are using
3. Go to the Webhook Message you want to replay
4. Click on the "Replay" button

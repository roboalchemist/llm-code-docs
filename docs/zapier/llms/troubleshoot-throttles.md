# Source: https://docs.zapier.com/platform/build/troubleshoot-throttles.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Troubleshoot throttles

## Throttling by your API

### Constraint

Your API has request limits.

### Errors user will see if constraint is hit

* If a trigger, user will receive an email with an error message about the trigger error
* If an action, user will see an error in Zap history

### Best practice

Add a specific `Retry-After` header to your 429 response, or specify a timed delay in your error response using a special `ThrottledError`. Instead of a user's Zap erroring and halting, the request will be retried at the specified time.

More on the retry [here](https://github.com/zapier/zapier-platform/blob/main/packages/cli/README.md#handling-throttled-requests). The user will see a [Waiting/Scheduled](https://help.zapier.com/hc/en-us/articles/20505304170637-Review-Zap-run-statuses) message in Zap history instead of an error while the limit is still in place.

<Frame>
  {" "}

  <img src="https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/0933736266259b11771a0eba0aff23ce.webp?fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=1efe774c999092e898ff473deb283210" data-og-width="718" width="718" data-og-height="182" height="182" data-path="images/0933736266259b11771a0eba0aff23ce.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/0933736266259b11771a0eba0aff23ce.webp?w=280&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=5648e106738b551a9531a4330f74c1c4 280w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/0933736266259b11771a0eba0aff23ce.webp?w=560&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=91e720fce8d3dc1ba2df5852aa0f7b10 560w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/0933736266259b11771a0eba0aff23ce.webp?w=840&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=365e7c3da8f442332a0adc7731fe47e1 840w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/0933736266259b11771a0eba0aff23ce.webp?w=1100&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=2dcb7d7771c55c11fb9fb9e45139f0a4 1100w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/0933736266259b11771a0eba0aff23ce.webp?w=1650&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=19f9b96f452b8dd6c2630f3a9cff516f 1650w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/0933736266259b11771a0eba0aff23ce.webp?w=2500&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=80c99b3fe9caa31bb4a9a19d5617fb19 2500w" />

  {" "}
</Frame>

If implementing a `ThrottledError`, you could consider implementing a jitter for handling 429 errors, that could look something like this to randomize the frequency of the retries as well:

`throw new z.errors.ThrottledError('message here', 60 + Math.floor(Math.random() * 60))`

Keep in mind that adding custom error handling with `ThrottledError` would likely require a [new integration version](/platform/manage/versions), whereas adding to the headers could be implemented on your API's end.

## Webhook throttles by Zapier

### Constraint

Zapier's current webhook limits are [here](https://help.zapier.com/hc/en-us/articles/8496181445261#h_01H91ED0PQ56S166BSB7MJNZNT). A 429 response is returned if your integration exceeds these limits in number of webhooks sent to Zapier.

### Errors user will see if constraint is hit

* User will receive an email with an error message about the trigger error

### Best practice

You should support a retry/back-off schedule to make sure the data is eventually received.

## Polling trigger throttles by Zapier

### Constraint

There is a default limit of 100 new items recognized per poll after deduplication. More on that [here](https://help.zapier.com/hc/en-us/articles/8496181445261-Rate-limits-and-throttling-in-Zapier#h_01H91ED0PQ1HK1G1YFTZ9NSPRN).

### Errors user will see if constraint is hit

* The user will receive an email about held Zap runs, as well as a banner with the same information in their Zap history.

### Best practice

If your trigger will be returning > 100 new records consistently, consider converting your trigger to be REST Hook based. Webhook limits are higher (up to 10,000 requests in a 5 minute period).

***

*Need help? [Tell us about your problem](https://developer.zapier.com/contact) and we'll connect you with the right resource or contact support.*

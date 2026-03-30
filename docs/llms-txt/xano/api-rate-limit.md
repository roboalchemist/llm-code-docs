# Source: https://docs.xano.com/instances/api-rate-limit.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# API Rate Limit

To keep Xano's free plan safe and fair for everyone sharing the resources of our free server instance, a rate limit of **10 requests every 20 seconds** is enforced.

When you encounter the rate limit, you'll see a message like this:

```json  theme={null}
{"code":"ERROR_CODE_TOO_MANY_REQUESTS","message":"Whoa there! Your plan only supports 10 requests per 20 seconds. Upgrade options and additional information is available at: https://xano.gitbook.io/xano/instances/api-rate-limit"}
```

### What can I do when I hit the rate limit?

* Wait up to 20 seconds before sending a new request

* Upgrade to a [paid plan](https://www.xano.com/pricing).

<Info>
  Rate limits **do not apply** when testing inside of Xano — you can use our [Run and Debug features](/the-function-stack/building-with-visual-development#testing-a-draft) to test as much as you'd like!
</Info>


Built with [Mintlify](https://mintlify.com).
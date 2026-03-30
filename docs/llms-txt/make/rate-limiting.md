# Source: https://developers.make.com/api-documentation/getting-started/rate-limiting.md

# Rate limiting

Make API limits the number of requests you can send to the Make API. Make sets the rate limits based on your organization plan:

* **Core:** 60 per minute
* **Pro:** 120 per minute
* **Teams:** 240 per minute
* **Enterprise:** 1 000 per minute

If you exceed your rate limit, you get `error 429` with the message:

```
Requests limit for organization exceeded, please try again later.
```

{% hint style="info" %}
You can check your organization API rate limit with the API call `GET {base-url}/organizations/{organizationId}`. In the API call response, the `license` object contains the property `apiLimit` with your organization's rate limit.

Check the organization detail API endpoint [documentation](https://developers.make.com/api-documentation/getting-started/broken-reference).
{% endhint %}

Read more about Make [pricing](https://www.make.com/en/help/general/pricing-parameters).

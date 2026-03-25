# Source: https://uptimerobot.com/api/v3/

Title: API V3 Documentation | UptimeRobot

URL Source: https://uptimerobot.com/api/v3/

Markdown Content:
![Image 1](https://uptimerobot.com/assets/images/uptimerobot-logo.svg)

UptimeRobot has an easy-to-use API. It lets you get the details of your monitors, create / edit / delete monitors, alert contacts, maintenance windows and public status pages.

### Response format

The API returns data in JSON format.

### Rate limits

We are trying to prevent abusive use of our API. We have rate limits based on user plan.

`FREE plan : 10 req/minPRO plan : monitor limit * 2 req/min ( with maximum value 5000 req/min )`
We will return 429 HTTP status code in the response from API, when you hit the rate limits. Also we will return common rate limit response headers in the response:

`X-RateLimit-Limit - your current rate limitX-RateLimit-Remaining - number of calls left in current durationX-RateLimit-Reset - time since epoch in seconds at which the rate limiting period will end (or already ended)Retry-After - Number of second after you should retry the call`

### Type of API keys

HTTP Basic Access Authentication is used for verifying accounts.

There are 3 types of api_keys for reaching the data:

*   **Account-specific api_key:** Allows using all the API methods on all the monitors of an account.
*   **Monitor-specific api_keys:** Allows using only the `getMonitors` method for the given monitor.
*   **Read-only api_key:** Allows fetching data with all the `get*` API endpoints.

### How to get API keys

You can get your API keys from the [Integrations page](https://dashboard.uptimerobot.com/integrations) under section **API**.

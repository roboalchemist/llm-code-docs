# Source: https://docs.port.io/api-reference/rate-limits.md

# Rate limits

Rate limits restrict the number of requests or actions allowed within a certain timeframe to prevent overuse or abuse. Port enforces multiple rate limits to control extensive usage of Port's API.

Port's rate limits vary based on the API being accessed and may be more lenient for some APIs.<br /><!-- -->Rate limits are enforced at the **Organization level**.

When usage exceeds acceptable thresholds, requests may take longer to be processed.

## Rate limits table[â](#rate-limits-table "Direct link to Rate limits table")

| Description              | Rate limit                    |
| ------------------------ | ----------------------------- |
| Unauthenticated requests | 100 requests per 5 minutes    |
| Entities API requests    | 35,000 requests per 5 minutes |
| All other API requests   | 15,000 requests per 5 minutes |

Port's API rate limits are subject to change as new features are added, functionality is changed or in order to protect system health. The most up to date rate limit information will always be available in the headers returned in API responses.

## How to avoid getting rate limited[â](#how-to-avoid-getting-rate-limited "Direct link to How to avoid getting rate limited")

### Monitor rate limit headers[â](#monitor-rate-limit-headers "Direct link to Monitor rate limit headers")

Each API response includes headers that provide information about your current rate limit status:

| Header name                                                                                    | Description                                                                 |
| ---------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `x-ratelimit-period`                                                                           | The period of time the rate is calculated                                   |
| `x-ratelimit-limit`                                                                            | The limit of the rate the user can achieve                                  |
| `x-ratelimit-remaining`                                                                        | The number of requests to send during the period before the user is limited |
| `x-ratelimit-reset`                                                                            | The number of seconds before the rate limit is reset                        |
| To avoid hitting rate limits, you should monitor the rate limit headers in your API responses. |                                                                             |

The `x-ratelimit-remaining` header shows how many requests you have left in the current window. When this number gets low, you should reduce your request frequency or implement a backoff strategy.

The `x-ratelimit-reset` header tells you when the rate limit window will reset, which can help you plan when to resume normal request rates.

Rate limit enforcement levels

Rate limits are enforced at the organization level by default. Service account users are an exception and are rate-limited at the user level.

### Use exponential backoff[â](#use-exponential-backoff "Direct link to Use exponential backoff")

Exponential backoff is a technique used to prevent overwhelming a server with too many requests in a short period of time. It involves progressively increasing the delay between retries when encountering rate limits or server errors.

To implement exponential backoff, you can follow these steps:

1. *Define a base delay*: Start with a small delay, such as 1 second, as the base delay for the first retry.
2. *Define a maximum number of retries*: Determine the maximum number of retries you want to attempt before giving up.
3. *Implement retry logic*: Wrap your API request code in a retry loop that will retry the request if it encounters a rate limit or server error.
4. *Calculate the delay*: Use an exponential function to calculate the delay for each retry. The delay can be calculated using the formula: `delay` = `baseDelay` \* (2 ^ `retryCount`), where `retryCount` starts from 0 for the first retry.
5. *Apply the delay*: Before each retry, pause the execution of the code for the calculated delay duration.

Here's are examples of how you can implement exponential backoff:

* Python
* Javascript

```
import time

base_delay = 1  # 1 second
max_retries = 5
max_delay = 32

def make_api_request():
    # Your API request code goes here
    pass

def retry_with_exponential_backoff():
    attempt = 0
    delay = base_delay
    
    while attempt < max_retries:
        try:
            result = make_api_request()
            return result
        except Exception as e:
            attempt += 1
            if attempt >= max_retries:
                raise e
            sleep_time = min(delay * (2 ** attempt), max_delay)
            print(f"Attempt {attempt} failed. Retrying in {sleep_time:.2f} seconds...")
            time.sleep(sleep_time)
    raise Exception("All retry attempts failed.")

retry_with_exponential_backoff()
```

```
const baseDelay = 1000; // 1 second
const maxRetries = 5;
let retryCount = 0;

function makeApiRequest() {
  // Your API request code goes here
}

function retryWithExponentialBackoff() {
  if (retryCount < maxRetries) {
    const delay = baseDelay * Math.pow(2, retryCount);
    setTimeout(() => {
      retryCount++;
      makeApiRequest();
    }, delay);
  } else {
    console.log('Exceeded maximum retries');
  }
}

retryWithExponentialBackoff();
```

In this example, the `makeApiRequest` function represents your actual API request code. The `retryWithExponentialBackoff` function is responsible for calculating the delay and retrying the request using exponential backoff. It uses the `setTimeout` function to pause the execution for the calculated delay duration. Remember to adjust the `baseDelay` and `maxRetries` values according to your specific requirements.

Exponential backoff helps to distribute the load on the server and increases the chances of a successful request without exceeding rate limits.

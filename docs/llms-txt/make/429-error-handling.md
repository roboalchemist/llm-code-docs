# Source: https://developers.make.com/custom-apps-documentation/best-practices/base/429-error-handling.md

# 429 error handling

An error with the status code 429 is an API rate limit error.

However, the default module error type for an error code between 400 - 500 is always a `RuntimeError`.

There are advantages to handling a 429 error as a `RateLimitError` instead.

## RuntimeError handling vs RateLimitError handling

In a scenario with scheduling turned on, if one of the scenario modules throws a `RuntimeError`, your scenario will break and retry to run according to the number of consecutive errors from your scenario settings (the default is 3 times).

If the number of consecutive errors is consumed, the scenario scheduling will be switched off and you will need to manually switch your scenario scheduling on again.

To prevent this, use the module error type `RateLimitError` to handle the 429 error. This error type has the same functionality as `ConnectionError` and returns the warning message instead of the error sign.

The advantage of using `RateLimitError` is that, instead of using the number of consecutive errors and then switching the scheduling off, the retries continue with [increasing time intervals](https://help.make.com/types-of-errors#QJ_-W).

For example:

* A scenario with scheduling turned on suddenly has one module throw a `RateLimitError`.
* It will retry after 1 minute.
* If it throws the `RateLimitError` again, it will retry after 2 minutes.
* Repeatedly the scenario increases the interval by 1, 2, 5, 10 minutes, and 1, 3, 12, and 24 hours.

{% tabs %}
{% tab title="Example code to handle 429 errors" %}

```javascript
{
  "response": {
    "error": {
      "429": {
        "type": "RateLimitError",
        "message": "{{body.message}}"
      },
      "message": "{{body.message}}"
    }
  }
} 
```

{% endtab %}
{% endtabs %}

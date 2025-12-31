# Source: https://docs.baseten.co/development/model-apis/rate-limits-and-budgets.md

# Rate Limits & Budgets

> Learn about rate limits for Baseten's Model APIs and how to set usage budgets to control costs.

## Rate Limits

To ensure fair use and system stability, Baseten enforces two rate limits:

* **Request rate limits** — maximum number of API requests per minute
* **Token rate limits** — maximum number of tokens processed per minute (input + output combined)

Default limits vary based on your account status.

| Account                  |                                         RPM |                                         TPM |
| :----------------------- | ------------------------------------------: | ------------------------------------------: |
| **Starter** (unverified) |                                          15 |                                     100,000 |
| **Starter** (verified)   |                                         120 |                                     500,000 |
| **Business**             |                                         120 |                                   1,000,000 |
| **Enterprise**           | [Custom](https://www.baseten.co/talk-to-us) | [Custom](https://www.baseten.co/talk-to-us) |

<Warning>
  If you exceed these limits, the API will return a `429 Too Many Requests`
  error. Request a higher rate limit by [contacting us](https://www.baseten.co/talk-to-us/increase-rate-limits/).
</Warning>

### Requesting higher limits

If you have high volume, are a verified customer, and need more headroom, you can [contact us](https://www.baseten.co/talk-to-us/increase-rate-limits/) to request a rate limit increase.

***

## Setting budgets

Setting a budget allows you to control your Model API usage and avoid unexpected costs. Usage budgets apply only to Model APIs (not dedicated deployments). Your team will be notified by email at 75%, 90%, and 100% of budget.

### Enforcing budgets

When setting a budget, you can choose to enforce it or not.

* **If you choose to enforce it**, requests will be rejected once the budget is reached.
* **If you choose not to enforce it**, you will be notified at 75%, 90%, and 100% of budget and you'll be responsible for any costs incurred over the budget.

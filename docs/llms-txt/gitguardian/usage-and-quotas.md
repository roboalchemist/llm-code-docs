# Source: https://docs.gitguardian.com/api-docs/usage-and-quotas.md

# Usage and quotas

> GitGuardian API usage details including stateless scanning, quota limits per plan, monthly quota calculations, and rate limiting.

## Usage

The **GitGuardian API and its scan capability** can be used to scan simple content quickly, or even to write complex
integrations for non-publicly available services.

Most of GitGuardian's Open Source projects use the **GitGuardian API** as their backbone.
[ggshield](../ggshield-docs/getting-started.md) and [py-gitguardian](https://github.com/GitGuardian/py-gitguardian)
are two examples.

## Stateless scanning

The GitGuardian API endpoints are stateless, meaning any scanned documents or found secrets are not stored on our servers when performing a secrets scan. We do, however, collect and store some metadata for purposes such as quota usage and access logs.

## Quotas

API quotas are only consumed by API calls related to the [`scan` scope](./authentication#scopes):

- the [`/scan` endpoint](https://api.gitguardian.com/docs#operation/content_scan) ingests only one document (piece of text) and consumes 1 quota.
- the [/multiscan endpoint](https://api.gitguardian.com/docs#operation/multiple_scan) ingests several documents at a time (20 max) and consumes 1 quota.
  If a commit contains 40 different documents to scan, scanning this commit will require 2 quotas.

Quota usage is based on requests, not on the size of the content you scan.

**The quota is set on a rolling month**, not on a calendar month.
This means that if 200 API calls are made on the last day of the month, you will need to wait 30 days before 200 new calls are credited back to your account.
This quota is applied at the workspace level, not at the individual API key level. Consequently, exceeding the quota with one API key will restrict all other API keys in the same workspace from making further API calls.
The quota depends on your plan but you can always contact us to increase it (see [GitGuardian Pricing](https://www.gitguardian.com/pricing) for more details):

|           | Free plan          | Business plan       | Enterprise plan |
| --------- | :----------------- | :------------------ | :-------------- |
| **Quota** | 10,000 calls/month | 100,000 calls/month | Unlimited       |

Workspace Managers can track usage of their quota in the [Quota section](https://dashboard.gitguardian.com/api/quota) of their workspace:

![API usage](/img/api/quota.png)

## Rate limiting

The GitGuardian API implements rate limiting to manage the number of requests made to the API.
This helps prevent abuse, ensures fair usage, and maintains the performance and availability of the API.

The GitGuardian API implements rate limiting at the API key level, ensuring that each key is allocated a predetermined maximum number of requests within a designated timeframe.
If the limit is exceeded, the GitGuardian API will return error with status code 429 and the requests will not be processed.
The rate limiting varies based on the type of API key (personal access token or service account) and the plan of your workspace:

|                           | Free plan                                                      | Business plan        | Enterprise plan       |
| ------------------------- | :------------------------------------------------------------- | :------------------- | :-------------------- |
| **Personal access token** | 50 requests/minute                                             | 200 requests/minute  | 2000 requests/minute  |
| **Service account**       | N/AService accounts are not available under the Free plan | 1000 requests/minute | 10000 requests/minute |

> By default, API rate limiting is not applied to GitGuardian self-hosted instances.

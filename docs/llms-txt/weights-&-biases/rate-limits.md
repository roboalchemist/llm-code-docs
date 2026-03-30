# Source: https://docs.wandb.ai/platform/hosting/self-managed/rate-limits.md

# Source: https://docs.wandb.ai/platform/hosting/hosting-options/dedicated-cloud/rate-limits.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Rate limits

> Default rate limits on Dedicated Cloud and how to request changes

W\&B Dedicated Cloud applies rate limits to maintain instance stability. W\&B can adjust limits when you scale up training or need higher throughput.

## Default limits and notification

The following default limits help maintain platform stability:

| Limit                            | Default | Scope   |
| -------------------------------- | ------- | ------- |
| Filestream requests per second   | 500     | Project |
| Filestream ingestion per second  | 120 MB  | Project |
| Filestream requests per second   | 2       | Run     |
| Run creation requests per second | 80      | Project |

When a limit is exceeded, the W\&B SDK returns HTTP response `429`, and the message `HTTP 429: rate limited exceeded` appears in the SDK logs.

* Filesystem rate limits never cause logging to crash or fail. When the SDK receives a `429` response on a filestream request, it will back off and retry the rate-limited request as-is, while subsequent updates accumulate.

* Run creation rate limits block further training.

```
HTTP 429: rate limit exceeded
```

These defaults are recommended for typical production workloads. If your workloads consistently exceed these limits, contact [W\&B support](mailto:support@wandb.com) or your Account Solutions Engineer (AISE) to request higher limits. Provide details of your experimental setup and usage patterns.

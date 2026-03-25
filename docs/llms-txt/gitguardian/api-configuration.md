# Source: https://docs.gitguardian.com/self-hosting/management/application-management/api-configuration.md

# Use the API

> Configure the GitGuardian API for self-hosted installations, including rate limiting and endpoint settings.

As for the GitGuardian SaaS version, you can enable the API for your Self-Hosted
environment.

The base URL of the API routes will be different for the Self-Hosted environment
than the SaaS one.
You should use `[your_domain_name]/exposed`.

For example, if your dashboard URL is `https://gitguardian.mycorp.local`,
the URL to use for the API will be
`https://gitguardian.mycorp.local/exposed/`.

If you want to check the status of the API, you should use the following query:

```bash
curl -H "Authorization: Token ${TOKEN}" \
https://gitguardian.mycorp.local/exposed/v1/health
```

:::tip
If you are not certain of your API URL, you can find your dashboard, in the
**API** part, in the Quota section:

![API URL](/img/self-hosting/management/application-management/api_url.png)
:::

You can find more information about how to use the API
[in the GitGuardian documentation](/platform/gitguardian-suite/api).

# Source: https://jam.dev/docs/debug-a-jam/devtools/secrets.md

# Secrets

## Why do I see "JAM\_DOES\_NOT\_SAVE\_SECRETS"?

<figure><img src="https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2FJYzZ1hAtytaPtjEDPltO%2FScreenshot%202023-07-07%20at%209.36.58%20PM.png?alt=media&#x26;token=27b8ba5d-ca8a-4afd-852a-e3180453ab6f" alt=""><figcaption></figcaption></figure>

We understand sensitive information can be present in network requests, which is why Jam scans all network requests for any possible sensitive information including tokens, cookies and PII. We filter out these fields on the client side so they never reach Jam's servers.

We remove any potentially sensitive fields from request headers, and (if in JSON), request bodies. This is done prior to Jam creation, so the Jam data you see on the page (with the `JAM_DOES_NOT_SAVE_SECRETS` strings as the values of these headers) has already been filtered before leaving your laptop. It does not reach Jam's servers.

In the resulting Jam, you will see `JAM_DOES_NOT_SAVE_SECRETS` in place of any possible secret information.&#x20;

We prefer to over-filter than under-filter and are taking the route of being overly cautious, so sometimes you will see information filtered out that probably should not have been. Please help us improve our filtering accuracy by sending your feedback to <hello@jam.dev>.

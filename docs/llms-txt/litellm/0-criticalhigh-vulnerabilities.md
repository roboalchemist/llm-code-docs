# 0 Critical/High Vulnerabilities

![](https://docs.litellm.ai/assets/ideal-img/security.8eb0218.1200.png)

## What changed? [​](https://docs.litellm.ai/release_notes\#what-changed "Direct link to What changed?")

- LiteLLMBase image now uses `cgr.dev/chainguard/python:latest-dev`

## Why the change? [​](https://docs.litellm.ai/release_notes\#why-the-change "Direct link to Why the change?")

To ensure there are 0 critical/high vulnerabilities on LiteLLM Docker Image

## Migration Guide [​](https://docs.litellm.ai/release_notes\#migration-guide "Direct link to Migration Guide")

- If you use a custom dockerfile with litellm as a base image + `apt-get`

Instead of `apt-get` use `apk`, the base litellm image will no longer have `apt-get` installed.

**You are only impacted if you use `apt-get` in your Dockerfile**

```codeBlockLines_e6Vv
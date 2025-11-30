# Source: https://developer.1password.com/docs/connect

On this page

# 1Password Connect

1Password Connect Servers allow you to securely access your 1Password items and vaults in your company\'s apps and cloud infrastructure using a private REST API.

Because Connect servers cache your data in your infrastructure, they allow unlimited re-requests after the server fetches your secrets.

The only request quotas that apply to Connect servers are the internal rate limits 1Password employs to keep our services stable and available. These only apply when a Connect server fetches secrets for the first time, like when the Connect server starts.

You can integrate a Connect server into your infrastructure and communicate with it over HTTP using one of the Connect SDK libraries (such as [Go](https://github.com/1Password/connect-sdk-go), [Python](https://github.com/1Password/connect-sdk-python), or [JavaScript](https://github.com/1Password/connect-sdk-js)) or using a custom integration.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6IiAvPjwvc3ZnPg==)]Not sure if Connect servers are for you?

See the [Secrets Automation comparison table](/docs/secrets-automation#comparison).

![The Connect server is part of your environment, and communicates to Your Apps using access tokens and a REST API.](/img/connect-diagram.png)![The Connect server is part of your environment, and communicates to Your Apps using access tokens and a REST API.](/img/connect-diagram.png)

## Use cases[â€‹](#use-cases "Direct link to Use cases") 

You can use 1Password Connect to accomplish a variety of tasks:

## Availability 

### Reduce latency and downtime 

Deploy a Connect server in your infrastructure, giving you complete control. Self-hosting also reduces latency and has security benefits, as only your services can interact with Connect.

You can also deploy redundant Connect servers to further increase availability.
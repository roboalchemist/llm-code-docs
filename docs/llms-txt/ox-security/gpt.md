# Source: https://docs.ox.security/fix-with-ox/gpt.md

# OX GPT

The GPT connector lets OX run AI-powered capabilities with your own GPT account and policies.

When connected, OX routes all LLM requests with your GPT token. Ownership, logging, and billing stay on your side, and your network rules apply.

For on-prem, the connector is required to enable AI capabilities. For SaaS, it lets you use AI without relying on an OX-managed account, whether for compliance, data-handling, or internal policy.

During operation, OX sends only the context required to fulfill a request, for example, prompts or short code snippets, to your configured provider, so confirm that this aligns with your organization’s data-handling policy.

### GPT SaaS vs on-prem

| Deployment Mode | Without GPT Connector                                   | With GPT Connector                                        | Data Path                                                                             |
| --------------- | ------------------------------------------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| OX SaaS         | AI capabilities are available by default with OX token. | Requests are routed to your GPT account using your token. | OX calls the provider API on your behalf.                                             |
| OX On-Prem      | AI capabilities are unavailable until configured.       | Required. Requests run with your GPT token.               | Requests leave your environment only to the approved provider or proxy you configure. |

## Prerequisites

| Item           | Details                             |
| -------------- | ----------------------------------- |
| GPT API token  | Active API token for your provider. |
| OX permissions | OX Admin account.                   |

## Connecting to GPT

1. In the OX platform, go to the **Connectors** page.
2. Select **Add Connector** and search for **GPT**.
3. In the **Configure your ChatGPT credentials** dialog, select **CONNECT**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-b938f3a23e05af025b41305c488540fe4bfa8d6e%2FGPT_Connect.png?alt=media" alt=""><figcaption></figcaption></figure>

| Field     | Description                                          |
| --------- | ---------------------------------------------------- |
| **Token** | The provider token OX uses to authenticate requests. |

1. Select **CONNECT**. AI capabilities become available. OX does not use an OX-managed account.

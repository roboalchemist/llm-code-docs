# Source: https://plivo.com/docs/aiagent/aistudio/secrets.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Secret Variables

> Secret Variables securely store and manage sensitive data like API keys and tokens

**Secret Variables** are used to securely store and use sensitive data (e.g., API keys, tokens, passwords) within your workflows. They are encrypted and can be referenced in nodes like **Custom Code** and **HTTP Request** to ensure security and privacy.

#### Benefits of Secret Variables

* **Security**: Sensitive data is encrypted and only accessible when necessary, avoiding exposure in your workflow.
* **Ease of Use**: Secret variables can be easily inserted into nodes like **HTTP Request** and **Custom Code** with minimal setup, allowing for seamless integration.
* **Centralized Management**: Secrets are stored in one place, and they can be reused across multiple workflows and nodes.

#### Managing Secrets

To securely store sensitive information, you can create **Secret Variables** as follows:

1. **Key**: Enter a unique identifier for the secret (e.g., `API_KEY`).
2. **Value**: Enter the sensitive data (e.g., an API token).
3. **Description** (optional): Provide a brief description to clarify what the secret is for.

<Frame>
  <img src="https://mintcdn.com/plivo/R0bB3pSVhMhsNJEx/aiagent/images/secrets1.gif?s=a44d5dffe45e107463abcf311a653d91" width="2386" height="1640" data-path="aiagent/images/secrets1.gif" />
</Frame>

Once created, the variables are securely stored and can be used across your workflows.

You can also **edit** or **delete** secret variables as needed.

#### Using Secret Variables in Nodes

Secret Variables can be inserted into nodes like **Custom Code** and **HTTP Request** to securely access sensitive information. Here’s how you use them:

1. In nodes that support secret variables (like **Custom Code** or **HTTP Request**), you will see an **Insert Secret Variable** option.
2. When configuring a node, click the button to select a secret from your list.
3. The selected secret will automatically be inserted into the node’s configuration, ensuring secure access to sensitive data without exposing it in the workflow.

<Frame>
  <img src="https://mintcdn.com/plivo/R0bB3pSVhMhsNJEx/aiagent/images/secrets2.png?fit=max&auto=format&n=R0bB3pSVhMhsNJEx&q=85&s=aefeaa9b047704367856a49dbd4255e0" width="866" height="512" data-path="aiagent/images/secrets2.png" />
</Frame>

By using **Secret Variables**, you ensure that sensitive information remains protected while still being functional and accessible when needed in your workflow.

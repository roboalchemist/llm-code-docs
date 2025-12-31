# Source: https://resend.com/docs/knowledge-base/how-to-handle-api-keys.md

# How to Handle API Keys

> Learn our suggested practices for handling API keys.

API Keys are secret tokens used to authenticate your requests. They are unique to your account and should be kept confidential. You can create API keys in two ways:

* [via the Resend Dashboard](/dashboard/api-keys/introduction)
* [via the API](/api-reference/api-keys/create-api-key)

<Info>
  For more help creating, deleting, and managing API keys, see the [API Keys
  documentation](/dashboard/api-keys/introduction).
</Info>

## Best Practices

It's crucial you handle your API keys securely. Do not share your API key with others or expose it in the browser or other client-side code.

Here are some general guidelines:

* Store API keys in environment variables.
* Never commit API keys to version control.
* Never hard-code API keys in your code or share them publicly.
* Rotate API keys regularly. If an API key hasn't been used in the last 30 days, consider deleting it to keep your account secure.

<Info>
  When you create an API key in Resend, you can view the key only once. This
  practice helps encourage these best practices.
</Info>

## Example

Many programming languages have built-in support for environment variables. Here's an example of how to store an API key in an environment variable in a Node.js application.

<Steps>
  <Step title="Create an environment variable">
    Once you create the API key, you can store it in an environment variable in a `.env` file.

    ```ts .env theme={null}
    RESEND_API_KEY = 're_xxxxxxxxx';
    ```
  </Step>

  <Step title="Add the file to your gitignore">
    Add the `.env` file to your `.gitignore` file to prevent it from being committed to version control. Many frameworks already add `.env` to the `.gitignore` file by default.

    ```ts .gitignore theme={null}
    .env
    ```
  </Step>

  <Step title="Use the environment variable in your code">
    `ts const resend = new Resend(process.env.RESEND_API_KEY); `
  </Step>
</Steps>

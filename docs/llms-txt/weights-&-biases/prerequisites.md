# Source: https://docs.wandb.ai/training/prerequisites.md

# Source: https://docs.wandb.ai/inference/prerequisites.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Prerequisites

> Set up your environment, API key, and dependencies before using the W&B Inference service through the API or UI.

Complete these steps before using the W\&B Inference service through the API or UI.

<Tip>
  Before starting, review the [usage information and limits](/inference/usage-limits/) to understand costs and restrictions.
</Tip>

## Set up your W\&B account and project

You need these items to access W\&B Inference:

1. **A W\&B account**\
   Sign up at [W\&B](https://app.wandb.ai/login?signup=true)

2. **A W\&B API key**

   To create an API key, select the **Personal API key** or **Service Account API key** tab for details.

   <Tabs>
     <Tab title="Personal API key">
       To create a personal API key owned by your user ID:

       1. Log in to W\&B, click your user profile icon, then click **User Settings**.
       2. Click **Create new API key**.
       3. Provide a descriptive name for your API key.
       4. Click **Create**.
       5. Copy the displayed API key immediately and store it securely.
     </Tab>

     <Tab title="Service account API key">
       To create an API key owned by a service account:

       1. Navigate to the **Service Accounts** tab in your team or organization settings.
       2. Find the service account in the list.
       3. Click the action menu (`...`), then click **Create API key**.
       4. Provide a name for the API key, then click **Create**.
       5. Copy the displayed API key immediately and store it securely.
       6. Click **Done**.

       You can create multiple API keys for a single service account to support different environments or workflows.
     </Tab>
   </Tabs>

   <Warning>
     The full API key is only shown once at creation time. After you close the dialog, you cannot view the full API key again. Only the key ID (first part of the key) is visible in your settings. If you lose the full API key, you must create a new API key.
   </Warning>

   For secure storage options, see [Store API keys securely](/platform/app/settings-page/user-settings/#store-and-handle-api-keys-securely).

3. **A W\&B project**\
   Create a project in your W\&B account to track usage

## Set up your environment (Python)

To use the Inference API with Python, you also need to:

1. Complete the general requirements above

2. Install the required libraries:

   ```bash  theme={null}
   pip install openai weave
   ```

<Note>
  **Note**

  The `weave` library is optional but recommended. It lets you trace your LLM applications. Learn more in the [Weave Quickstart](/models/quickstart/).

  See [usage examples](/inference/examples/) for code samples using W\&B Inference with Weave.
</Note>

## Next steps

After completing the prerequisites:

* Check the [API reference](/inference/api-reference/) to learn about available endpoints
* Try the [usage examples](/inference/examples/) to see the service in action
* Use the [UI guide](/inference/ui-guide/) to access models through the web interface

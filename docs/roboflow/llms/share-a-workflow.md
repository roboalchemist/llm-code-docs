# Source: https://docs.roboflow.com/roboflow/roboflow-ko/workflows/share-a-workflow.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/workflows/share-a-workflow.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/workflows/share-a-workflow.md

# Source: https://docs.roboflow.com/workflows/share-a-workflow.md

# Share a Workflow

Share a workflow to let people view, run, and fork the workflow.

1. Go to your Workflow page and click on the Share Workflow button\\

   <figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-a8912d092b367a194caee4b6c03614ad1c0a7179%2FCleanShot%202025-01-29%20at%2021.57.42%402x.png?alt=media" alt=""><figcaption><p>Share Workflow button on Workflow Editor.</p></figcaption></figure>
2. Click on the button **Copy Share Link**\\

   <figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-ef6e0e7581a1f4db871d9d385e090a69ec13bd8a%2Fimage.png?alt=media" alt=""><figcaption><p>Share Workflow configuration modal.</p></figcaption></figure>
3. Send to someone or open in your browser. You will see that this will open a read-only version of your workflow that allows people to see what you built and run previews on it.\\

   <figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-2a336cad470a9523991b1e1847acd51f75a47345%2FCleanShot%202025-01-29%20at%2021.57.13%402x.png?alt=media" alt=""><figcaption><p>Shareable Workflow URL.</p></figcaption></figure>

By default, a shared Workflow does not run under your API Keys and credentials. This means that it does not consume your usage limits and replaces any credentials like OpenAI API Key on your blocks as input parameters the user should provide. You can modify that behavior by changing the Workflow Sharing Configuration.

Here's an example of a shareable Workflow that takes a picture as an input and determines the winner of a Rock, Paper & Scissors game. Give it a try!

{% embed url="<https://app.roboflow.com/workflows/embed/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ3b3JrZmxvd0lkIjoidXFSSDgwVlFrcUV5OXp4cHp0bUYiLCJ3b3Jrc3BhY2VJZCI6ImtyT1RBYm5jRmhvUU1DZExPbGU0IiwidXNlcklkIjoiRVJNUFBZY3FQMmZWWjB1NkRpNXZaYXJDdlZPMiIsImlhdCI6MTcyNzA5NTQ0MX0.ZViKmHztQzhyLhyGjWEVF0zaku1DD0OjnfoM0YGvDIY>" %}

### How Workflow sharing works with private credentials

By default, a shared Workflow does not run under your API Keys and credentials. This means that it does not consume your usage limits and replaces any credentials like OpenAI API Key on your blocks as input parameters the user should provide. You can change this behavior by changing sharing configurations:

#### Allow people to run a Workflow under your API Key

This is useful when you want to share a Workflow containing a private Model - since the default behavior is not to run under your API key, a Workflow containing a private Model will fail to execute - so you change that to allow a protected run: it will affect your usage limits, but your API Key and model data will always be private.

To do so, go to the **Run access** section and change it to allow anyone to run the Workflow.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-d26fba6623e48dc7c9e8a779183b7add91dd8010%2Fimage.png?alt=media" alt=""><figcaption><p>Run Access dropdown options.</p></figcaption></figure>

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-a8b14327a158e2cc74279cffac87f627b94757a7%2Fimage.png?alt=media" alt=""><figcaption><p>Run Access option to allow private models being executed in shareable links.</p></figcaption></figure>

This option is **only available when a private Model is detected in the workflow steps**.

This configuration side effects are:

{% hint style="warning" %}
Any previews run under the shareable link will affect your Wokflow usage.
{% endhint %}

{% hint style="success" %}
Your private Models data and your API Key will always remain private.
{% endhint %}

#### Allow people to run a Workflow under your hidden credentials

This is useful when you want to share a workflow that has any step with credentials (LMM, OpenAI, Anthropic, etc.) and let people securely use your own credentials to make it easier for them to try your Workflow - your credentials won't be exposed and will be redacted on any client-facing data.

To do so, go to the **Credentials** section and change it to allow users to execute the Workflow with your hidden credentials.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-fac19094707fbe3d8d5296c882dbf8dbb365d828%2Fimage.png?alt=media" alt=""><figcaption><p>Credentials configuration dropdwn options.</p></figcaption></figure>

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-614524198499acb327b60028e33fca2e3261ca80%2Fimage.png?alt=media" alt=""><figcaption><p>Credentials option to allow people running a Workflow under your pre-configured credentials.</p></figcaption></figure>

This option is **only available when a step that needs credentials is detected in the workflow.**

This configuration side effects are:

{% hint style="warning" %}
Any previews run under the shareable link will affect your specific credential usage limits (e.g. OpenAI Api Keys).
{% endhint %}

{% hint style="success" %}
Your credentials values will always be private and are redacted from any client-facing data.
{% endhint %}

Here's an example of a Workflow that runs under a hidden OpenAI API Key to run a License Plate detection + OCR. Give it a try!

{% embed url="<https://app.roboflow.com/workflows/embed/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ3b3JrZmxvd0lkIjoiR2N3MFdxQnVQWXdJY0tqdDY3MkoiLCJ3b3Jrc3BhY2VJZCI6IjFsY25TMDdFSVJTb08xUHo5RkFmIiwidXNlcklkIjoiRVJNUFBZY3FQMmZWWjB1NkRpNXZaYXJDdlZPMiIsImlhdCI6MTcyODU2NDI0NH0.vvKMTOE_H6xWFaJe8YLYjuNcA-x9X2IxvtdL_6Kzd2g>" %}

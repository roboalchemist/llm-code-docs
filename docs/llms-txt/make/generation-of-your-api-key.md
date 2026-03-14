# Source: https://developers.make.com/custom-apps-documentation/get-started/make-apps-editor/apps-sdk/generation-of-your-api-key.md

# Generate your API key

To set up the VS Code extension you must provide an API key with the appropriate API key scopes.

To generate your API key:

{% stepper %}
{% step %}
Navigate to your profile settings in Make.
{% endstep %}

{% step %}
Click **API access** in the left navigation.
{% endstep %}

{% step %}
Click **+ Add token**.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-fc8ea9cdb3b8f88d1ccbcfdcccba82a0dde531cf%2Fvisualstudiocode_apikey.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Set the API scopes for the API key.

The required scopes for the Make Apps Editor are:

* `sdk-apps:read`
* `sdk-apps:write`

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2FLkpn8f2P7iorS4IbAxXC%2Faddtoken_vscode.png?alt=media&#x26;token=6e944400-48a2-4530-b80c-958d8127be4a" alt="" width="364"><figcaption></figcaption></figure></div>

Add more API scopes to your API key as needed. You can find descriptions of the API scopes in the [Make API documentation](https://developers.make.com/api-documentation/authentication/api-scopes-overview).
{% endstep %}

{% step %}
Click **Save** to confirm the selected permissions.
{% endstep %}

{% step %}
Copy your new API key to your clipboard and store it in a safe place. **This is the only time you can see the whole API key.** The API key is required to set up the VS code extension.
{% endstep %}
{% endstepper %}

You have created a new Make API key. All your Make API keys are listed in your Make profile in the **API access** section. You can view permissions for all your keys and delete unused Make API keys.

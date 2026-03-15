# Source: https://help.aikido.dev/code-scanning/connect-your-source-code/connect-bitbucket-account-to-aikido/code-scanning-with-a-workspace-access-token.md

# Code Scanning with a Workspace Access Token

{% hint style="warning" %}
Bitbucket only supports the creation of Workspace Access Tokens for their premium plan.
{% endhint %}

### Introduction <a href="#introduction" id="introduction"></a>

You can easily configure Bitbucket Code Scanning via the Aikido interface via the account settings page, or by navigating directly to [this link](https://app.aikido.dev/onboarding/bitbucket/update-workspace-access-token).&#x20;

### Creating a Workspace Access Token <a href="#creating-a-personal-access-token" id="creating-a-personal-access-token"></a>

{% stepper %}
{% step %}

### Navigate to the workspace settings

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FO0UPQ4AE27X0DjlzyEGl%2F11.jpg?alt=media&#x26;token=6874f843-b8ae-4f0c-a74b-a08b8e92ebe9" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Create access token

Click on the "Create access token" button to start creating a workspace access token.
{% endstep %}

{% step %}

### Select the required scopes

Choose a descriptive name for the token like "**Aikido Security Code Scanning**", and select the following scopes: **Account:Read** & **Repsitories:Read**
{% endstep %}

{% step %}

### Copy the token

After clicking "**Create**", you can copy the token and enter it in the input field on [this page](https://app.aikido.dev/onboarding/bitbucket/update-workspace-access-token)
{% endstep %}
{% endstepper %}

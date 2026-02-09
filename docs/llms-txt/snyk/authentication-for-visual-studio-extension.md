# Source: https://docs.snyk.io/developer-tools/snyk-ide-plugins-and-extensions/visual-studio-extension/authentication-for-visual-studio-extension.md

# Authentication for Visual Studio extension

To scan your Projects, you must authenticate with Snyk.

Snyk supports the following protocols for authentication:

* OAuth 2.0 (Recommended)
* Personal Access Token
* API token (Legacy)

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-183e690111cc5a1d5a060c233ca3e6128893488b%2Fimage.png?alt=media" alt=""><figcaption><p>Authentication methods available in the Snyk extension in Visual Studio</p></figcaption></figure>

## Steps to authenticate using the OAuth 2.0 protocol

Follow the next steps to authenticate:

1. After the extension is installed, navigate to **Extensions** > **Snyk** > **Windows**, and then **Snyk** to open the Snyk panel.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-acd35d116482e968e8d8826ba6e0d8beeed5c413%2FSCR-20240822-llxy.png?alt=media" alt="" width="563"><figcaption><p>Snyk extension navigation</p></figcaption></figure>

2. On the welcome screen, click **Trust project and scan.**

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-a25b370989e7fc80b121c2ffc19ee63eaa08a010%2FSCR-20240822-lmdw.png?alt=media" alt="" width="563"><figcaption><p>Trust project and scan</p></figcaption></figure>

3. A new browser window opens, requiring you to log in to your Snyk account.
4. In the next prompt, the Snyk IDE extension requests access to act on your behalf. Click **Grant app access**.
5. When you have authenticated successfully, a confirmation message appears. Close the browser window and return to the IDE.

The analysis starts automatically. The IDE reads and saves the authentication on your local machine.

{% hint style="info" %}
OAuth 2.0 tokens are not static and cannot be copied from the Snyk account page.
{% endhint %}

If you have problems, see [OAuth 2.0 authentication does not work](https://docs.snyk.io/developer-tools/snyk-ide-plugins-and-extensions/troubleshooting-ides/how-to-set-environment-variables-by-operating-system-os-for-ides-and-cli-1).

## Steps to authenticate using your Personal Access Token

{% hint style="warning" %}
This method is inferior to the OAuth method.
{% endhint %}

{% hint style="warning" %}
The Personal Access Token (PAT) authentication is progressively rolled out to all Enterprise customers. To check if this feature is available for your Organization at this time, please reach out to your Snyk account team.
{% endhint %}

To authenticate using the Personal Access token, follow these steps:

1. Navigate to **Preferences** > **Snyk**.
2. Set the flag to **Use Personal Access Token.**

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-2c216caa3a7d6a8ebfedab8ec7e6aef7d8b2b131%2Fimage%20(318).png?alt=media" alt=""><figcaption></figcaption></figure>
3. Click the **Connect IDE to Snyk** button.
4. Create your **Personal Access** **Token**. For details, see the [Authentication for API](https://docs.snyk.io/snyk-api/authentication-for-api) page.
5. Paste or enter the token in the **Token** field.
6. Click **Apply and Close.**

## Steps to authenticate using your Snyk API token

{% hint style="warning" %}
This method is inferior to the OAuth method.
{% endhint %}

Follow these steps to authenticate:

1. After the extension is installed, navigate to **Extensions > Snyk** > **Settings**:

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-fc4658a16c8cc19e03e1a970e92c39e26f068ffc%2FSCR-20240822-lyzs.png?alt=media" alt="" width="375"><figcaption><p>Snyk Settings navigation</p></figcaption></figure>

2. Find the **Authentication Method** and change it to **API Token** authentication.

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-2c216caa3a7d6a8ebfedab8ec7e6aef7d8b2b131%2Fimage%20(318).png?alt=media" alt=""><figcaption></figcaption></figure>
3. Click the **Connect IDE to Snyk** button.
4. Click **Authenticate** in the web browser window that opens.

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-64d49e101674a64bb63c3ec5d72dd3f9411201a3%2Fimage%20(317).png?alt=media" alt=""><figcaption></figcaption></figure>
5. The API token is automatically updated in the **API Token field**.
6. Click **Apply and Close.**

The analysis starts automatically.

{% hint style="info" %}
Alternatively, copy the personal API token from your Snyk Web UI instance (default is [https://app.snyk.io](https://app.snyk.io/)). Paste the token in the **API Token** field. For details, see [Obtain and use your Snyk API token](https://docs.snyk.io/discover-snyk/getting-started#obtain-and-use-your-snyk-api-token).
{% endhint %}

## How to switch accounts

To re-authenticate with a different account, follow these steps:

1. Navigate to **Extensions > Snyk > Settings.**
2. Clear the value of the **Token** field.
3. Click **OK**.
4. When you have logged out, start authentication again from the beginning.

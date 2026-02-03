# Source: https://docs.snyk.io/developer-tools/snyk-ide-plugins-and-extensions/eclipse-plugin/authentication-for-the-eclipse-plugin.md

# Authentication for the Eclipse plugin

To scan your Projects, you must authenticate with Snyk.

Snyk supports the following protocols for authentication:

* OAuth 2.0 (Recommended)
* Personal Access Token
* Snyk API token (Legacy)

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-ac0554c4d605f54f865cf17471b3b77d3618a62f%2Fimage.png?alt=media" alt=""><figcaption><p>Authentication methods available in the Snyk plugin in Eclipse</p></figcaption></figure>

## Steps to authenticate using the OAuth 2.0 protocol

After the plugin is installed, follow these steps to authenticate:

1. In the dialog that opens, set the Snyk API endpoint for a custom multi-tenant or single-tenant setup. For details, see [IDE URLs](https://docs.snyk.io/snyk-data-and-governance/regional-hosting-and-data-residency#ides-urls).\
   \
   Multi-tenant users who do not belong to the `SNYK-US-01` region ( `https://api.snyk.io`) will be automatically redirected to the correct domain for the email with which the user authenticated. This redirect will not happen if users are expected to use a custom URL, such as in single-tenant company configurations.\
   \
   When you are finished with the settings on this page, click **Next**.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-fe8a4e4225c01838eda2d0087feb9a2e7ac461ea%2FSCR-20240822-mgxw.png?alt=media" alt="" width="563"><figcaption><p>Snyk endpoint configuration</p></figcaption></figure>

2. On the next page, follow the prompts, then click **Finish**.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-e14e5138071ab47f6bcbb350f76a8337714062f3%2FSCR-20240822-mibb.png?alt=media" alt="" width="563"><figcaption><p>Additional information and finish</p></figcaption></figure>

3. A new browser page opens, requiring you to log in to your Snyk account.
4. In the next prompt, the Snyk IDE plugin requests access to act on your behalf. Click **Grant app access**.
5. After you have successfully authenticated, a confirmation message appears. Close the browser window and return to the IDE.

The analysis starts automatically. The IDE reads and saves the authentication tokens on your local machine.

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

To authenticate using the Personal Access Token, follow these steps:

1. Navigate to **Eclipse** > **Settings** > **Snyk**.\
   (On Windows/Linux navigate to **Window** > **Preferences** > **Snyk**)
2. Set the **Authentication Method** to **Use Personal Access Token**.

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-77d34a4721f2097e8230090f1cf312ed27572302%2Fimage%20(321).png?alt=media" alt=""><figcaption></figcaption></figure>
3. Click the **Connect IDE to Snyk** button.
4. Create your **Personal Access** **Token**. For details, see the [Authentication for API](https://docs.snyk.io/snyk-api/authentication-for-api) page.
5. Add the token in the **Token** field.
6. Click **Apply and Close.**

The analysis starts automatically.

## Steps to authenticate using your Snyk API token

{% hint style="warning" %}
This method is inferior to the OAuth method.
{% endhint %}

To authenticate using the API token, follow these steps:

1. Navigate to **Eclipse** > **Settings** > **Snyk**.\
   (On Windows/Linux navigate to **Window** > **Preferences** > **Snyk**)
2. Set the **Authentication Method** to **API token**.

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-f3d3a5da7e809e2ef77fa211fec0d7f3805c3364%2Fimage%20(323).png?alt=media" alt=""><figcaption></figcaption></figure>
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

1. Navigate to **Preferences** > **Snyk**.
2. Clear the value in the **Token** field.
3. Click **Apply and Close**.
4. When you have logged out, start authentication again from the beginning.

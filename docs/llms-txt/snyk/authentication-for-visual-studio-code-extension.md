# Source: https://docs.snyk.io/developer-tools/snyk-ide-plugins-and-extensions/visual-studio-code-extension/authentication-for-visual-studio-code-extension.md

# Authentication for Visual Studio Code extension

To scan your Projects, you must authenticate with Snyk.

Snyk supports the following protocols for authentication:

* OAuth 2.0 (Recommended)
* Personal Access Token
* Snyk API token (Legacy)

For all authentication methods, Snyk uses the [Secret Storage API](https://code.visualstudio.com/api/references/vscode-api#SecretStorage) to store the token securely. This storage uses the keychain of the system to manage the token.

{% hint style="warning" %}
Before authenticating, ensure you have set your region properly. For details, see [IDEs URLs](https://docs.snyk.io/snyk-data-and-governance/regional-hosting-and-data-residency#ides-urls).
{% endhint %}

## Steps to authenticate using the OAuth 2.0 protocol

Follow these steps to authenticate:

1. After the extension is installed, click the **Snyk Icon** in the navigation bar, then click **Connect & Trust Workspace**:

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-6f5e7a91ba092e9c0c3acf97c3eda025dbb09d88%2FSCR-20240821-qmuv.png?alt=media" alt="" width="359"><figcaption><p>Connect and trust workspace</p></figcaption></figure>
2. A new browser window opens, requiring you to log in to your Snyk account.
3. In the next prompt, the Snyk IDE extension requests access to act on your behalf. Click **Grant app access**.
4. When you have authenticated successfully, a confirmation message appears. Close the browser window and return to the IDE.
5. The IDE reads and saves the authentication on your local machine. Close the browser window and return to the IDE.

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

When using this feature, ensure you generate and use a Personal Access Token (PAT). This feature is not compatible with Service Account tokens, and using them may result in unexpected behavior or errors.

{% hint style="info" %}
Whenever you use this feature in your IDE, ensure to also retrieve the PAT details from the Snyk Web UI. Contact Snyk Support to enable the PAT feature within your Snyk Web UI Organization.
{% endhint %}

To authenticate using the Personal Access token, follow these steps:

1. Click the **Snyk Icon** in the navigation bar, then click the **Settings** icon, find **Authentication Method,** and change it to **Personal Access Token**.

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-c321912bb32c66bf91d68cf3f3292f8e9fe242e2%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>
2. Create your **Personal Access** **Token**. For details, see the [Authentication for API](https://docs.snyk.io/snyk-api/authentication-for-api) page.
3. Run the `Snyk: Set Token` command and paste the token in the text field.

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-ea33fe22ec7751aa182d1b43b1481cdb622e68d9%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

## Steps to authenticate using your Snyk API token

{% hint style="warning" %}
This method is inferior to the OAuth method.
{% endhint %}

Follow these steps to authenticate:

1. After the extension is installed, click the **Snyk Icon** in the navigation bar, then click the **Settings** icon, find **Authentication Method,** and change it to **Token authentication**:

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-e5d0768274e2cd7f7772b287297c3fa374f5b631%2FSCR-20240821-tarb.png?alt=media" alt=""><figcaption><p>Change authentication method</p></figcaption></figure>

2. Press **Connect & Trust Workspace**.
3. Click **Authenticate** in the web browser window that opens.

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-64d49e101674a64bb63c3ec5d72dd3f9411201a3%2Fimage%20(317).png?alt=media" alt=""><figcaption></figcaption></figure>

The analysis starts automatically.

{% hint style="info" %}
Alternatively, run the `Snyk: Set Token` command and paste the token in the text field.
{% endhint %}

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-4636de75116782d5c5a5e643568cca8989c0e86e%2Fimage%20(80)%20(1).png?alt=media&#x26;token=ae8d1b32-a925-4abf-9d20-e6d01eac8423" alt=""><figcaption><p>Set token manually</p></figcaption></figure>

## How to switch accounts

To re-authenticate with a different account, follow these steps:

1. Run the provided `Snyk: Log Out` command.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-1defc168d9d73b3aaf191022de2382c26effdba6%2Flogging-out-command.png?alt=media" alt=""><figcaption><p>Snyk: Log out</p></figcaption></figure>

2. When you have logged out, start authentication again from the beginning.

## Requirements for Linux and Unix

When authenticating with Snyk, users have the option to copy the authentication URL to their clipboard.

For Linux and Unix users, this requires the `xclip` or `xsel` utility to be installed.

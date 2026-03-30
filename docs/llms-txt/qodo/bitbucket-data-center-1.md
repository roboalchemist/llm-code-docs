# Source: https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/getting-started/setup-and-installation/bitbucket-data-center-1.md

# Bitbucket Data Center

{% hint style="warning" %}
**Git Integration (formerly Qodo Merge)** – AI code review agents for pull requests.\
This documentation describes the Qodo v1 experience. For the Qodo v2 documentation, click [here.](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/)
{% endhint %}

This guide will help you install and configure Qodo with your Bitbucket Data Center (BBDC) instance.

You can install it for a single repository or expand it across multiple projects as needed.

Assuming your Qodo environment is setup, expect configuring BBDC to take about 20 minutes, including creating tokens, configuring the service, and setting up webhooks.

Once complete, Qodo will process pull requests and deliver actionable output—such as code reviews and insights—directly to your PRs. Setting up Qodo for BBDC brings automated PR intelligence to your self-hosted environment.

***

{% hint style="success" %}
**This connection method is available only to Enterprise customers.** [**Contact Qodo**](https://www.qodo.ai/contact/#pricing) **to use Qodo Git interface on your private Bitbucket server.**
{% endhint %}

### Prerequisites

Before you begin, ensure you have:

1. A Qodo Single Tenant Deployment (for Code Review)
2. Receive your Qodo Single Tenant URL from your Qodo Account Manager
3. A Bitbucket Data Center instance (version 8.x or 9.x)
4. System administrator access to your BBDC instance
5. App upload capability enabled in BBDC

{% hint style="info" %}
If you require version 10.x of Bitbucket Data Center contact your Qodo Account Manager.&#x20;
{% endhint %}

#### Verify App Upload is Enabled

1. Navigate to **Settings → Manage Apps**
2. Confirm the "Upload app" link is visible
3. If not visible, ask your Bitbucket admin to add `upm.plugin.upload.enabled=true` to your `bitbucket.properties` file&#x20;

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FVjG5KvJ9GdBXIKfdltyX%2Fimage.png?alt=media&#x26;token=d5f1318e-4bce-4577-b51f-0acbecd5443e" alt=""><figcaption></figcaption></figure>

### Installation Steps

#### Step 1: Install the Qodo App

1. Go to **Settings → Manage Apps → Upload App**
2. Download the appropriate version ([download JAR file](https://github.com/qodo-ai/BBDC-App-Releases?tab=readme-ov-file#installation)):
   * **BBDC 8.x**: Use `qodo-app-bbdc-2.x.x.jar`
   * **BBDC 9.x**: Use `qodo-app-bbdc-3.x.x.jar`
3. Upload the JAR file to your BBDC instance
4. Verify the app is enabled after installation (check "Manage Apps" if needed)

> **Note**: Contact your Qodo representative for the latest app version compatible with your BBDC instance is not available.

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2F4JpQmfY1t7MonWqrIxo1%2Fimage.png?alt=media&#x26;token=b7a3feb8-b4d0-4a5f-851d-529161c37e6b" alt=""><figcaption></figcaption></figure>

#### Step 2: Create Access Token

You'll need to create an HTTP access token for Qodo to communicate with BBDC.

**Optional: Create a Dedicated Service Account**

For better visibility, create a dedicated system administrator user (e.g., "Qodo") before generating the token. All PR comments will appear under this user's name.

**Generate the Token**

1. Log in to BBDC as a system administrator
2. Click **Profile Picture → Manage Account → HTTP Access Tokens**
3. Click **Create Token**
4. Configure the token:
   * **Name**: Qodo Integration
   * **Permissions**: Repository Write access (minimum required)
5. Click **Create**
6. **Important**: Copy and save the bearer token immediately—you won't be able to see it again

![Qodo app enabled in Manage Apps](https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FmoRdZ6EoOO9dIRuqNtj1%2FEdit-Access-Token.png?alt=media\&token=68967c81-e11d-491a-8c89-c70fa1e7467a)

#### Step 3: Create a shared webhook secret

Choose a strong secret (it can be anything). You can use any secret generation tool you prefer.&#x20;

#### Step 4: Configure the Qodo App in BBDC

1. Navigate to **Administration → Add-ons → Qodo**
2. Select the **Qodo Merge** tab
3. In the **Connection** section, enter:
   * **Single Tenant Qodo Merge URL**: Your Qodo Merge instance URL (ask your Qodo Account manager)
   * **Shared Webhook Secret**: The same webhook secret you create in step 3

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FkgVuIBgTjekuHshfGeIS%2Fimage%20(5).png?alt=media&#x26;token=e4a2f727-522e-4906-8c8d-0a944ae3bd5f" alt=""><figcaption></figcaption></figure>

#### Step 5: Configure Repository Integration

Choose how Qodo Merge will integrate with your repositories:

**Integration Modes:**

* **All repositories** (default): Qodo Merge will be active on all repositories
* **Selected repositories only**: Choose specific repositories to integrate
* **All repositories except**: Exclude specific repositories from integration

1. In the Qodo App configuration, navigate to the **Repositories** section
2. Select your preferred integration mode
3. If using selective modes, specify the repositories
4. Make sure your changes are saved

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FqjV9PWYRChGMs3GZYI0U%2Fimage.png?alt=media&#x26;token=57dac6c0-8269-49d5-b85d-44ed966adac4" alt=""><figcaption></figcaption></figure>

#### Step 6: Send Bitbucket App Details to Qodo

Provide Qodo account contact the following details to configure your Qodo instance with the following settings:

```toml
# URL to your BitBucket Data Center instance
url = "https://your-bbdc-instance.com"

# Bearer token from Step 2
bearer_token = "your-bearer-token-here"

# Shared secret for webhook verification 
webhook_secret = "your-webhook-secret-here"
```

> **Production Note**: For production environments, follow your organization's secret management procedures to securely store these credentials.

{% hint style="success" %}
Well Done. Now wait for the Qodo Team to confirm installation was successful.&#x20;
{% endhint %}

### Verification

After confirmation, you can test the installation.&#x20;

#### Test Connection

* Navigate to **Administration → Add-ons → Qodo**
* Select the **Qodo Merge** tab
* In the **Connection** section, click **"Test Connection"**

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2F69ADZF53YxUWoft3Nsrf%2Fimage.png?alt=media&#x26;token=617d2479-c2c3-4568-8629-521eb339352e" alt=""><figcaption></figcaption></figure>

#### Run a Test PR

1. **Open a new pull request** in one of your integrated repositories
2. Qodo Merge should automatically post a review comment
3. Alternatively, add a comment with `/improve` to an existing PR
4. Verify that Qodo Merge responds with code suggestions

#### Troubleshooting

If Qodo Merge isn't responding:

* Verify the app is enabled in **Settings → Manage Apps**
* Check that your repository matches your integration mode settings
* Confirm the bearer token has appropriate permissions
* Verify the webhook secret matches in both BBDC and Qodo Merge configurations
* Check the Qodo Merge logs for connection errors

### Available Commands

Once installed, you can use Qodo Merge commands in PR comments:

* `/review` - Perform a code review
* `/improve` - Suggest code improvements
* `/describe` - Generate a PR description
* `/ask` - Ask questions about the code changes

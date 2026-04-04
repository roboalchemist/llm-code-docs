# Source: https://docs.qodo.ai/qodo-documentation/on-prem/context-engine/setup-context-engine/bitbucket-data-center.md

# Source: https://docs.qodo.ai/qodo-documentation/qodo-aware/getting-started/enterprise-self-hosted/3.-index-your-codebase/bitbucket-data-center.md

# Source: https://docs.qodo.ai/qodo-documentation/code-review/get-started/install/bitbucket-data-center.md

# Install Qodo on Bitbucket Data Center

This guide helps you install and configure Qodo with your Bitbucket Data Center (BBDC) instance.

You can install Qodo on a single repository to start small or expand it across multiple projects as needed.

Assuming your Qodo environment is already set up, configuring BBDC typically takes about 20 minutes. This includes creating access tokens, configuring the service, and setting up webhooks.

Once complete, Qodo processes pull requests and delivers actionable output, such as code reviews and insights, directly in your pull requests. Setting up Qodo for BBDC brings automated pull request intelligence to your self-hosted environment.

{% hint style="info" %}
This connection method is available only to Enterprise customers. [Contact the Qodo team](https://www.qodo.ai/contact/#pricing) to enable the Git integration for your private Bitbucket Data Center instance.
{% endhint %}

### Prerequisites

Before you begin, ensure you have:

* **A Qodo single-tenant deployment (for code review)**\
  You will receive your Qodo single-tenant URL from your Qodo Account Manager.
* **A Bitbucket Data Center instance**\
  Version 8.x or 9.x
* **System administrator access** to your Bitbucket Data Center instance.
* **App upload capability enabled** in Bitbucket Data Center.

{% hint style="info" %}
If you require Bitbucket Data Center version 10.x, contact your Qodo Account Manager.
{% endhint %}

### **Verify App Upload is enabled**

1. Navigate to **Settings → Manage Apps.**
2. Confirm the **Upload app** link is visible.
3. If not visible, ask your Bitbucket admin to add `upm.plugin.upload.enabled=true` to your `bitbucket.properties` file.

![](https://docs.qodo.ai/qodo-documentation/~gitbook/image?url=https%3A%2F%2F4090466057-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FzLhdlSjTSQhS3ANJsKST%252Fuploads%252FVjG5KvJ9GdBXIKfdltyX%252Fimage.png%3Falt%3Dmedia%26token%3Dd5f1318e-4bce-4577-b51f-0acbecd5443e\&width=768\&dpr=3\&quality=100\&sign=c6557371\&sv=2)

### Installation  <a href="#installation-steps" id="installation-steps"></a>

#### **Step 1: Install the Qodo App**

1. Go to **Settings → Manage Apps → Upload App**
2. Download the appropriate version ([download JAR file](https://github.com/qodo-ai/BBDC-App-Releases?tab=readme-ov-file#installation)):
   * **BBDC 8.x**: Use `qodo-app-bbdc-2.x.x.jar`
   * **BBDC 9.x**: Use `qodo-app-bbdc-3.x.x.jar`
3. Upload the JAR file to your BBDC instance
4. Verify the app is enabled after installation (check "Manage Apps" if needed)

{% hint style="info" %}
Contact your Qodo representative for the latest app version compatible with your BBDC instance is not available.
{% endhint %}

![](https://docs.qodo.ai/qodo-documentation/~gitbook/image?url=https%3A%2F%2F4090466057-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FzLhdlSjTSQhS3ANJsKST%252Fuploads%252F4JpQmfY1t7MonWqrIxo1%252Fimage.png%3Falt%3Dmedia%26token%3Db7a3feb8-b4d0-4a5f-851d-529161c37e6b\&width=768\&dpr=3\&quality=100\&sign=ab8b621c\&sv=2)

#### **Step 2: Create access token**

You need to create an HTTP access token for Qodo to communicate with Bitbucket Data Center.

(Optional) Create a dedicated service account\
For better visibility and auditability, consider creating a dedicated system administrator user (for example, **Qodo**) before generating the token. All pull request comments will appear under this user’s name.

1. Log in to Bitbucket Data Center as a system administrator.
2. Click **Profile picture → Manage account → HTTP access tokens**.
3. Click **Create token**.
4. Configure the token with the following settings:
   * **Name:** Qodo Integration
   * **Permissions:** Repository write access (minimum required)
5. Click **Create**. \
   Copy and save the bearer token immediately—you will not be able to view it again.

![](https://docs.qodo.ai/qodo-documentation/~gitbook/image?url=https%3A%2F%2F4090466057-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FzLhdlSjTSQhS3ANJsKST%252Fuploads%252FmoRdZ6EoOO9dIRuqNtj1%252FEdit-Access-Token.png%3Falt%3Dmedia%26token%3D68967c81-e11d-491a-8c89-c70fa1e7467a\&width=768\&dpr=3\&quality=100\&sign=c7dc3aa5\&sv=2)Qodo app enabled in Manage Apps

#### **Step 3: Create a shared webhook secret**

Select a strong secret value (it can be any string). You can use any secret generation tool you prefer.

#### **Step 4: Configure the Qodo App in BBDC**

1. Navigate to **Administration → Add-ons → Qodo**
2. Select the **Qodo Merge** tab
3. In the **Connection** section, enter:
   * **Single Tenant Qodo Merge URL**: Your Qodo Merge instance URL provided by your Qodo Account manager.
   * **Shared Webhook Secret**: The webhook secret you create in step 3.

![](https://docs.qodo.ai/qodo-documentation/~gitbook/image?url=https%3A%2F%2F4090466057-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FzLhdlSjTSQhS3ANJsKST%252Fuploads%252FkgVuIBgTjekuHshfGeIS%252Fimage%2520%285%29.png%3Falt%3Dmedia%26token%3De4a2f727-522e-4906-8c8d-0a944ae3bd5f\&width=768\&dpr=3\&quality=100\&sign=ad26dfb0\&sv=2)

#### **Step 5: Configure repository integration**

Select how Qodo integrates with your repositories.

**Integration modes:**

* **All repositories (default):** Qodo is active on all repositories
* **Selected repositories only:** Choose specific repositories to integrate
* **All repositories except:** Exclude specific repositories from integration

In the Qodo app configuration:

1. Navigate to the **Repositories** section.
2. Select your preferred integration mode.
3. If using a selective mode, specify the relevant repositories.
4. Save your changes.

![](https://docs.qodo.ai/qodo-documentation/~gitbook/image?url=https%3A%2F%2F4090466057-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FzLhdlSjTSQhS3ANJsKST%252Fuploads%252FqjV9PWYRChGMs3GZYI0U%252Fimage.png%3Falt%3Dmedia%26token%3D57dac6c0-8269-49d5-b85d-44ed966adac4\&width=768\&dpr=3\&quality=100\&sign=8eef356f\&sv=2)

#### **Step 6: Send Bitbucket App details to Qodo**

Provide Qodo account contact the following details to configure your Qodo instance with the following settings:

<a class="button secondary">Copy</a>

```
# URL to your BitBucket Data Center instance
url = "https://your-bbdc-instance.com"

# Bearer token from Step 2
bearer_token = "your-bearer-token-here"

# Shared secret for webhook verification 
webhook_secret = "your-webhook-secret-here"
```

> **Production Note**: For production environments, follow your organization's secret management procedures to securely store these credentials.

You’re all set. Wait for the Qodo team to confirm that the installation was successful.

### Verification <a href="#verification" id="verification"></a>

After receiving confirmation from the Qodo team, you can test the installation.

#### Test the connection

1. Navigate to **Administration → Add-ons → Qodo**.
2. Select the **Qodo** tab.
3. In the **Connection** section, click **Test Connection**.

![](https://docs.qodo.ai/qodo-documentation/~gitbook/image?url=https%3A%2F%2F4090466057-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FzLhdlSjTSQhS3ANJsKST%252Fuploads%252F69ADZF53YxUWoft3Nsrf%252Fimage.png%3Falt%3Dmedia%26token%3D617d2479-c2c3-4568-8629-521eb339352e\&width=768\&dpr=3\&quality=100\&sign=3423e97a\&sv=2)

#### Run a test pull request

1. Open a new pull request in one of the integrated repositories.
2. Qodo should automatically post a review response on the pull request.

Alternatively, add a comment such as `/agentic_review` to an existing pull request to trigger a review manually.

Verify that Qodo responds with code suggestions and review feedback.

#### Troubleshooting

If Qodo is not responding:

* Verify that the app is enabled under **Settings → Manage apps**.
* Check that the repository matches your selected integration mode.
* Confirm that the bearer token has the required permissions.
* Verify that the webhook secret matches in both Bitbucket Data Center and Qodo configuration.
* Review the Qodo logs for connection or authentication errors.

### Available commands

Once installed, you can use the following commands in pull request comments:

* `/agentic_describe`
* `/agentic_review`

# Source: https://docs.qodo.ai/qodo-documentation/code-review/get-started/install/bitbucket/qodo-single-tenant-bitbucket-cloud.md

# Source: https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/getting-started/setup-and-installation/bitbucket/qodo-single-tenant-bitbucket-cloud.md

# Qodo Single Tenant - Bitbucket Cloud

{% hint style="warning" %}
**Git Integration (formerly Qodo Merge)** – AI code review agents for pull requests.\
This documentation describes the Qodo v1 experience. For the Qodo v2 documentation, click [here.](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/)
{% endhint %}

This guide will help you install and configure Qodo with your Bitbucket workspace.

Assuming your Qodo environment is setup, expect configuring BB to take about 10 minutes.

Once complete, Qodo will process pull requests and deliver actionable output—such as code reviews and insights—directly to your PRs.

### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

Before you begin, ensure you have:

1. A Qodo Single Tenant Deployment (for Code Review)
2. Receive your Qodo Single Tenant URL from your Qodo Account Manager. It will look like *qodo-merge.yourcompanyname.st.qodo.ai*
3. System administrator access to your BB workspace

### Installation steps

#### Step 1: Navigate to Workspace settings

* Go to “Settings cog wheel” > “Workspace settings”

<div align="left"><figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FoSQfRg1cuaeAgkhVydWH%2Fimage.png?alt=media&#x26;token=381193bb-64ed-4f54-8a6a-bc7ed55fbed0" alt=""><figcaption></figcaption></figure></div>

#### Step 2: Navigate to Installed apps

* On left side menu

<div align="left"><figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FQ3fLBz60mBEpDUHwhdZK%2Fimage.png?alt=media&#x26;token=4e6d9307-a9c4-46b9-9808-529b51a6378c" alt=""><figcaption></figcaption></figure></div>

#### Step 3: Install App

* First **"Enable development mode"** (to be able install app)
* Install app from URL (Url that was provided by Qodo )

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FS0LNEkmdnSQt916CZYjd%2Fimage.png?alt=media&#x26;token=0c743ca0-1dc9-41fa-a901-f65b72a80502" alt=""><figcaption></figcaption></figure>

* Enter the URL (provided to you by Qodo team) and click Install.

{% hint style="info" %}
The URL should look like this: *qodo-merge.yourcompanyname.st.qodo.ai*
{% endhint %}

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FpvJx3RoDlqJOJy9IZUwc%2Fimage.png?alt=media&#x26;token=c1f44f9b-87d9-432f-8e6e-78255288ee68" alt=""><figcaption></figcaption></figure>

* Grant access to App

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FVtH6eM0i4NpT6GfhFPRQ%2Fimage.png?alt=media&#x26;token=e3cdb48d-17ee-4b0d-9a1c-1d6f3e73e26b" alt=""><figcaption></figcaption></figure>

#### Step 4: Send Bitbucket Workspace ID to Qodo

* Send the Workspace ID.
* Qodo Team will confirm that this was added to the Single Tenant  configuration

{% hint style="success" %}
Note: Qodo Merge is now enabled for all the repos within your BB workspace
{% endhint %}

### Verification <a href="#verification" id="verification"></a>

After confirmation, you can test the installation.

#### **Run a Test PR**

1. **Open a new pull request** in one of your integrated repositories
2. Qodo Merge should automatically post a review comment
3. Alternatively, add a comment with `/improve` to an existing PR
4. Verify that Qodo Merge responds with code suggestions

{% hint style="info" %}
In case you fail any of the above tests please contact Qodo team
{% endhint %}

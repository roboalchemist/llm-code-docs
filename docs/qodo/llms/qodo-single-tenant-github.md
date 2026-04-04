# Source: https://docs.qodo.ai/qodo-documentation/code-review/get-started/install/github/qodo-single-tenant-github.md

# Source: https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/getting-started/setup-and-installation/github/qodo-single-tenant-github.md

# Qodo Single Tenant - Github

{% hint style="warning" %}
**Git Integration (formerly Qodo Merge)** – AI code review agents for pull requests.\
This documentation describes the Qodo v1 experience. For the Qodo v2 documentation, click [here.](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/)
{% endhint %}

{% hint style="success" %}
Qodo can be integrated with all versions of Github. Enterprise, Cloud & Cloud Enterprise.&#x20;
{% endhint %}

This guide will help you install and configure Qodo with Github. You can install it for a single repository or expand it across multiple Orgs as needed.

Assuming your Qodo environment is setup, expect configuring Github to take about 20 minutes, including creating tokens, configuring the service, and setting up web hooks.

Once complete, Qodo will process pull requests and deliver actionable output—such as code reviews and insights—directly to your PRs. Setting up Qodo for Github brings automated PR intelligence to your github installation.

### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

Before you begin, ensure you have:

1. A Qodo Single Tenant Deployment
2. Receive your Qodo Single Tenant URL from your Qodo Account Manager. It will look like *qodo-merge.yourcompanyname.st.qodo.ai*
3. System administrator access to your Github Org

### Installation Steps <a href="#installation-steps" id="installation-steps"></a>

#### **Step 1:** Navigate to the GitHub apps section

* Login using an administrative account
* Click your profile picture → **Your organizations**

<div align="left"><figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2Fm9fONa7cdErGv8EBvCDU%2Fimage.png?alt=media&#x26;token=b65f5fab-a5b2-40c8-94e6-b81207888079" alt=""><figcaption></figcaption></figure></div>

* Select your organization (click on the org name)

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FPOpUTpAMmCzHzaT5At9w%2Fimage.png?alt=media&#x26;token=f4aeec5d-29e1-4d5c-83ef-ea0a1cf6f101" alt=""><figcaption></figcaption></figure>

* Click “**Settings**”

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FIF5CDfoRLt6jGC2IHi7J%2Fimage.png?alt=media&#x26;token=656916d2-7d0f-4c18-ad38-5caedc5abfbe" alt=""><figcaption></figcaption></figure>

* Go to Developer settings → GitHub Apps

<div align="left"><figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FHlrjJzT68ALR2LTy85bP%2Fimage.png?alt=media&#x26;token=8337fa61-008a-4776-8448-4dfa02557c61" alt=""><figcaption></figcaption></figure></div>

* Click “**New GitHub App**”

#### Step 2: Create the GitHub App

* Register a new Github App:

  * App name: **Qodo**
  * Homepage URL: [**http://qodo.ai**](http://qodo.ai)

  <div align="left"><figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FEOmEa9peZIEjqMPHhsQO%2Fimage.png?alt=media&#x26;token=bee95471-48d9-4b29-a328-e0d87f958563" alt=""><figcaption></figcaption></figure></div>
* Configure the webhook
  * Check the “**Active**” checkbox.
  * Webhook URL: use the following format (URL to be provided to you by Qodo):
    * &#x20;`https://qodo-merge.[yourcompanyname].st.qodo.ai/api/v1/github_webhooks`
  * Secret: generate a random secret and add it here. Keep the webhook secret safe, it will be needed to configure the Qodo service. Choose a strong secret (it can be anything). You can use any secret generation tool you prefer.&#x20;
  * Select “**Enable SSL verification**”

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FbKX9nGUU0YBjiQxoDhXN%2Fimage.png?alt=media&#x26;token=fc910009-5b94-4e3a-943d-b12e1f2f3702" alt=""><figcaption></figcaption></figure>

* Set the following Repository permissions:

| Permission Name | Description                                                                  | Access         |
| --------------- | ---------------------------------------------------------------------------- | -------------- |
| Actions         | Workflows, workflow runs and artifacts                                       | Read-only      |
| Checks          | Checks on code                                                               | Read-only      |
| Contents        | Repository contents commits. branches, downloads, releases and merges        | Read and write |
| Discussions     | Discussions and related comments and labels                                  | Read and write |
| Issues          | Issues and related comments, assignees, labels and milestones                | Read and write |
| Pull requests   | Pull requests and related comments, assignees, labels, milestones and merges | Read and write |

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2Ft0mBeQOR8kUPJ7Iugb2s%2Fimage.png?alt=media&#x26;token=82ea3f9c-01d4-4dfa-b369-6a42ce5c5277" alt=""><figcaption></figcaption></figure>

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FE0CO2ZzzmQADeGHsJtQj%2Fimage.png?alt=media&#x26;token=fa1d9338-d53d-4e0c-82fa-dbb55e1c01c4" alt=""><figcaption></figcaption></figure>

<div align="left"><figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FteyQUrxkyqpwPZF6QxK5%2Fimage.png?alt=media&#x26;token=2d3268a1-a49a-43f9-a6e9-1301565811f6" alt=""><figcaption></figcaption></figure></div>

<div align="left"><figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FyAUZ8F5HepFMTRsFFc8t%2Fimage.png?alt=media&#x26;token=a8e87dea-2214-4b43-96af-6f697b9c8929" alt=""><figcaption></figcaption></figure></div>

<div align="left"><figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FFr12096MVrtoVdZlfb1S%2Fimage.png?alt=media&#x26;token=f738d1f8-0e78-4ee5-9188-df23901f7027" alt=""><figcaption></figcaption></figure></div>

<div align="left"><figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2F7WSf8WVP1dCx1Ukw1nAr%2Fimage.png?alt=media&#x26;token=0042ef2e-f46b-4ca0-bc8e-552aa373e0a7" alt=""><figcaption></figcaption></figure></div>

* Subscribe to the following events:

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FEVdK3MlwEhrjfUl51VfI%2Fimage.png?alt=media&#x26;token=a1267421-e315-429d-8d47-83a9ca09ae11" alt=""><figcaption></figcaption></figure>

* In the “Where can this GitHub App be installed?” section:
  * Choose “**Any account**”\
    \
    (If you have multiple organizations, this will avoid creating a separate application for each org).&#x20;

<div align="left"><figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FHdaSqZkVGpKmoyp5D9PJ%2Fimage.png?alt=media&#x26;token=e59b4784-75bd-4f44-a864-be03ad29a31a" alt=""><figcaption></figcaption></figure></div>

* Finally, click “**Create GitHub App**”

<div align="left"><figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FWSRa4ova95nE9pszr7sh%2Fimage.png?alt=media&#x26;token=6f179d86-49bb-4bae-871b-99840fd504e4" alt=""><figcaption></figcaption></figure></div>

#### Step 3: Post creation actions

* Write down the App ID, it will be needed for Qodo Merge configuration

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2Fm9KWJObrEAt6bMGxKVqU%2Fimage.png?alt=media&#x26;token=c254953f-86c3-4890-984f-0ce4dd974b57" alt=""><figcaption></figcaption></figure>

* Generate a private key, it will be needed for Qodo Merge configuration

<div align="left"><figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FCHV1ffshMGnawRnvtbFf%2Fimage.png?alt=media&#x26;token=9132d647-34e9-46a9-ae5c-502f51d612a9" alt=""><figcaption></figcaption></figure></div>

* Upload a logo that will be used on Qodo GitHub posts on issues and PRs.

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FzJvksLakq5LuzXUEVoc6%2Fimage.png?alt=media&#x26;token=639ef20b-0f64-4695-bf7a-fec84af88140" alt=""><figcaption></figcaption></figure>

* Use the Qodo Anteater logo:

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FpmpHiRGhWCgVkZTunsY5%2Fimage.png?alt=media&#x26;token=38fa9b85-a962-425d-a5c4-7e1a29a57870" alt=""><figcaption></figcaption></figure>

#### Step 4: Install the App

* Go to Your Organization -> Settings -> Developer Settings -> Github Apps:

<div align="left"><figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FTkb83yLePU2R2rzKjAJh%2Fimage.png?alt=media&#x26;token=e5cda753-071f-460f-81ba-4d570cf030a2" alt=""><figcaption></figcaption></figure></div>

* Click on the Qodo App name

<div align="left"><figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FZTiXcrZUzCN4tkyqqJMd%2Fimage.png?alt=media&#x26;token=f66c5f73-4c8a-4433-a421-3b018f2948a8" alt=""><figcaption></figcaption></figure></div>

* **Install** the App on each of the relevant Orgs

<div align="left"><figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2Fapu23sOV7VWsWpgVDLAm%2Fimage.png?alt=media&#x26;token=76da10c8-1fc5-4f7a-9bef-5782ff5a5851" alt=""><figcaption></figcaption></figure></div>

#### Step 5: App Configuration

Select the repositories you wish to include for Qodo Merge.

* Go  to the GitHub Apps section in your organization’s Settings menu:

  * Click “**Configure**” on the Qodo app

  <figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FE53kOchFMEFZyqdnqN46%2Fimage.png?alt=media&#x26;token=b9327957-7680-4e52-aeeb-be9073171d4d" alt=""><figcaption></figcaption></figure>
* Under Repository Access choose “**Only select repositories**” and select the repositories that you wish to include:

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2F5x6cGdNvOUlwMD4XWCn3%2Fimage.png?alt=media&#x26;token=9ed0ea0a-1e22-46d7-9428-740d7d976681" alt=""><figcaption></figcaption></figure>

#### Step 6: Send Github App Details to Qodo

Provide Qodo account contact the following details to configure your Qodo instance with the following settings:

> **Production Note**: For production environments, follow your organization's secret management procedures to securely store these credentials.

```
# Github App ID
AppID = 3

# Shared secret for webhook verification 
webhook_secret = "your-webhook-secret-here"

# Private key (.pem file)

# Organization IDs (the name of the organization where the application is installed)
```

{% hint style="info" %}
The organization ID is available in the organization settings in Github. You can provide multiple organizations if you have installed Qodo several times.&#x20;
{% endhint %}

{% hint style="success" %}
Well Done. Now wait for the Qodo Team to confirm Server configuration is complete.
{% endhint %}

### Verification

After confirmation from the Qodo team, you can proceed to testing the installation

#### **Run a Test PR**

1. **Open a new pull request** in one of your integrated repositories
2. Qodo Merge should automatically post a review comment
3. Alternatively, add a comment with `/improve` to an existing PR
4. Verify that Qodo Merge responds with code suggestions

#### **Troubleshooting**

If Qodo Merge isn't responding:

* Verify that you are raising the PR in a repo that was selected in the App settings
* Contact Qodo team and provide the installation ID of the App.

Once installed, you can use Qodo Merge commands in PR comments:

* `/review` - Perform a code review
* `/improve` - Suggest code improvements
* `/describe` - Generate a PR description
* `/ask` - Ask questions about the code changes

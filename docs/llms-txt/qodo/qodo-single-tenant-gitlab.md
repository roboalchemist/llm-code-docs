# Source: https://docs.qodo.ai/qodo-documentation/code-review/get-started/install/gitlab/qodo-single-tenant-gitlab.md

# Source: https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/getting-started/setup-and-installation/gitlab/qodo-single-tenant-gitlab.md

# Qodo Single Tenant - Gitlab

{% hint style="warning" %}
**Git Integration (formerly Qodo Merge)** – AI code review agents for pull requests.\
This documentation describes the Qodo v1 experience. For the Qodo v2 documentation, click [here.](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/)
{% endhint %}

This guide will help you install and configure Qodo with Gitlab (both Cloud and Self hosted). You can install it for a single project or expand it across multiple projects as needed.

Assuming your Qodo environment is setup, expect configuring Gitlab to take about 20 minutes, including creating tokens, configuring the service, and setting up web hooks.

Once complete, Qodo will process pull requests and deliver actionable output—such as code reviews and insights—directly to your MRs. Setting up Qodo for Gitlab brings automated MR intelligence to your gitlab installation.

### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

Before you begin, ensure you have:

1. A Qodo Single Tenant Deployment
2. Receive your Qodo Single Tenant URL from your Qodo Account Manager. It will look like *qodo-merge.yourcompanyname.st.qodo.ai*
3. System administrator access (if you want to set up Qodo at group level)

### Installation Steps (at Group level) <a href="#installation-steps" id="installation-steps"></a>

#### **Step 1: Generate a Token**

* Navigate to the groups section in Gitlab and choose the group you want to setup Qodo in

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FFb6bGoQxqUVCE1da3AQA%2Fimage.png?alt=media&#x26;token=92c24755-bfab-46e4-b52b-6d7fc0987878" alt=""><figcaption></figcaption></figure>

* (within the chosen group) Navigate to **Group settings -> Access tokens**

<div align="left"><figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FHm7OdvJ6YJK5C3GC4cez%2Fimage.png?alt=media&#x26;token=ff819b15-346d-457f-9563-d11aced12c04" alt=""><figcaption></figcaption></figure></div>

* Configure the Access token:

  * Name: Any name will suffice
  * Expiration date: Choose the relevant period (for a POV 1-2 months, for a customer - 1 year)
  * Role: at least Developer
  * Select Scopes: check only the **api** option

  <figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FE6oAIMmBQozAdWOM4nFY%2Fimage.png?alt=media&#x26;token=2b3001dc-8d20-4560-81e6-43c4d8eddfe9" alt=""><figcaption></figcaption></figure>

  * **Important**: Copy and save the bearer token immediately—you won't be able to see it again

  <figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2F3vRjzMjAYDRjvdRLgzOL%2Fimage.png?alt=media&#x26;token=3fe8b8ad-db6e-45a8-aaf9-8c98e51741a0" alt=""><figcaption></figcaption></figure>

#### Step &#x32;**: Create a shared webhook secret**

Choose a strong secret (it can be anything). You can use any secret generation tool you prefer.

#### Step 3: Create a Group Webhook

* (within the chosen group) Navigate to **Group settings -> Webhooks**

<div align="left"><figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FKHtKRbXxrevFdu8AlxXe%2Fimage.png?alt=media&#x26;token=2cad3e45-bcdb-41c8-a98c-e409cd6540e3" alt=""><figcaption></figcaption></figure></div>

* choose **Add new webhook**

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2F6dI9DQ4PV5wlc2uJjnHX%2Fimage.png?alt=media&#x26;token=eaa9810b-5034-41ce-bcfc-877766d69750" alt=""><figcaption></figcaption></figure>

* Create the Webhook
  * Name - choose an appropriate name (no specific requirement)
  * Description - free text
  * URL - Qodo Merge Single Tenant URL received from your Qodo Account Manager. It will look like *qodo-merge.yourcompanyname.st.qodo.ai*
  * *Secret token - the secret you created in step 2*
  * *Triggers - select **Comments** and **Merge request events***

<div align="left"><figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2Fde3LpzRiEx57NZsq1DS8%2Fimage.png?alt=media&#x26;token=ec0d5d56-d0b6-4d50-99c9-0180c41f3f2b" alt=""><figcaption></figcaption></figure></div>

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FuSdhmSkneCoYGNnNINH3%2Fimage.png?alt=media&#x26;token=261edd26-2ec0-461f-9bee-49fa53fd2e24" alt=""><figcaption></figcaption></figure>

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FkUtPuQ1zjXkquZcbzg1s%2Fimage.png?alt=media&#x26;token=d6cea4ec-2364-4567-add1-d93daa11f20d" alt=""><figcaption></figcaption></figure>

#### Step 4: **Send  Gitlab integration Details to Qodo**

Provide Qodo account contact the following details to configure your Qodo instance with the following settings:

* Access Token created in step 1&#x20;
* Webhook Secret created in step 3&#x20;
* Gitlab group ID's (Group that was chosen in Step 1)
* (If deployed on Gitlab self hosted) Your Gitlab URL

{% hint style="success" %}
Well Done. Now wait for the Qodo Team to confirm installation was successful.
{% endhint %}

### Installation Steps (at project level) <a href="#installation-steps" id="installation-steps"></a>

{% hint style="info" %}
If you wish to limit the scope of Qodo Merge to a specific Gitlab project (repo) you can complete the same above steps (steps 1-4) just at the project level. You can repeat this for multiple projects, however for each project the webhook secret needs to be unique (and provide all the information to Qodo team for EACH project)
{% endhint %}

### Verification <a href="#verification" id="verification"></a>

After confirmation from the Qodo team, you can proceed to testing the installation

#### **Run a Test MR**

1. **Open a new merge request** in one of your projects from chosen group (where Qodo Merge was configured)
2. Qodo Merge should automatically post a review comment
3. Alternatively, add a comment with `/review` to an existing MR
4. Verify that Qodo Merge responds with code suggestions

#### **Troubleshooting**

If Qodo Merge isn't responding:

* Verify that you are raising the MR in a repo that is included in the appropriate group.
* Contact Qodo team.

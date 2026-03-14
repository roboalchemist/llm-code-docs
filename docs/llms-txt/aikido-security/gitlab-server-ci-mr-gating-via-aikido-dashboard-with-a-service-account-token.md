# Source: https://help.aikido.dev/pr-and-release-gating/gitlab-mr-gating/gitlab-server-ci-mr-gating-via-aikido-dashboard-with-a-service-account-token.md

# GitLab Premium, Ultimate & Server: MR Scans Setup

{% hint style="warning" %}
This setup is meant for **GitLab Premium, GitLab Ultimate, or GitLab Server**.

Service Accounts are available on these plans. They’re the recommended way to run MR scans.

If you’re on **GitLab Free**, use the [**user-based setup**](https://help.aikido.dev/pr-and-release-gating/gitlab-mr-gating/gitlab-free-mr-scans-setup) instead.
{% endhint %}

## Set up GitLab MR scanning

{% stepper %}
{% step %}

### Create a dedicated Service Account

In GitLab, go to **Group** → **Settings** → **Service accounts**.

Select **Add service account**.

Set a **Name** and **Username**:

* Name: `Aikido Security`
* Username: `AikidoSec`
* Select **Create**.

Use this account only for Aikido.

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FOisWq9N7jLdQZHeb1Pm8%2FScreenshot%202026-03-02%20at%2016.36.22.png?alt=media&#x26;token=433d59ad-eaad-4f27-8bed-140682a0d1cc" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}

### Create an Access Token

On the service account select the vertical ellipsis → **Manage access tokens**.

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FYKpNvN0JgtysQMCxsPbo%2Fimage.png?alt=media&#x26;token=0affb51b-44f0-4aa7-9f37-232f692a20a2" alt="GitLab Service Accounts overview"><figcaption></figcaption></figure></div>

Add a new token:

* Name: for example `Aikido Scans`
* Expiration date: Set an expiry date that matches your rotation policy
* Scopes: `api`

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FUnt6GRTBZnH0kXM38mFi%2FScreenshot%202026-03-02%20at%2013.56.26.png?alt=media&#x26;token=0fdf98b5-266d-4119-8178-fdbaef392cb1" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}

### Save the token

Copy the token now. GitLab won’t show it again.

You’ll paste it into Aikido in step 6.

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FtGopvLXZNnkApUY6IngD%2FScreenshot%202026-03-02%20at%2013.58.27.png?alt=media&#x26;token=62072e75-5a99-4622-bee6-8b2bdc458260" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}

### Invite the account to your group(s)

Go to **Groups** in GitLab.

For each group you want to enable, open the group.

Go to **Manage** → **Members** → **Invite members**.

Invite the service account.

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FeyAWVZor3jHbjkm3ByN1%2FScreenshot%202026-03-02%20at%2013.47.09.png?alt=media&#x26;token=e898b51f-c031-4fdf-8f1c-4d417aafd668" alt=""><figcaption></figcaption></figure></div>

Give it at least **Maintainer** access.

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FtD60VXOLHLsQMu1rtrou%2FScreenshot%202026-03-02%20at%2016.16.56.png?alt=media&#x26;token=8317b194-1f4a-483b-8ce9-82df898926fb" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}

### Enable the integration

In Aikido, open the [Integrations](https://app.aikido.dev/settings/integrations?section=ci) page. Then select **GitLab CI** under **MR Quality Gating**.

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FanPFjh0BJsrtmWtLrA94%2FScreenshot%202026-03-02%20at%2015.11.44.png?alt=media&#x26;token=d9c0c7fe-14bd-46a4-9181-be67cc4aceac" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}

### Paste the access token

Paste the token you created in step 3.

Click **Update token**.

Aikido validates group access and required permissions.

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FNuq99an4JilKNEjoDe9U%2FScreenshot%202026-03-02%20at%2015.02.03.png?alt=media&#x26;token=df2165cf-22e7-4baa-a55c-70e829bebe9b" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}

### Configure your first repository

After authorization, Aikido opens the [GitLab MR Checks](https://app.aikido.dev/settings/integrations/gitlab/checks) page.

Start with **one repository** first. Confirm everything works before rolling out broadly.

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FyGyP56cjP5G9bnyqvDgP%2FScreenshot%202026-03-02%20at%2015.17.32.png?alt=media&#x26;token=6ca94375-2a90-4dde-a8bb-56142ada60fa" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}

### Verify with a new MR

Open a new merge request (MR) in the repo you configured.

Then confirm the checks run in the **Pipelines** tab.

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FeuigB2tJr7nYSif4fJ6K%2FScreenshot%202026-03-02%20at%2015.20.37.png?alt=media&#x26;token=6e45daf5-95a8-4981-9e3d-dadeaad410f2" alt=""><figcaption></figcaption></figure></div>

Comments should appear as the service account. For example, `@AikidoSec`.

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FUfWkRo2jPPGVcT4XrSlE%2FScreenshot%202026-03-02%20at%2016.22.11.png?alt=media&#x26;token=a95bac2b-da0c-4c2d-8112-c105711da713" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}

### Require the scan to succeed <a href="#require-the-scan-as-a-merge-check" id="require-the-scan-as-a-merge-check"></a>

If you want to block merging until the scan succeeds, configure **merge checks** in GitLab.

In GitLab, go to **\[Repository]** → **Settings** → **Merge Requests**. Enable the check `Pipelines must succeed`.

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FgVXDYKRiyGl9U51g5nL5%2FScreenshot%202026-03-02%20at%2015.56.26.png?alt=media&#x26;token=7caa525e-a307-483a-8e6f-fdc96aa2d38d" alt=""><figcaption></figcaption></figure></div>

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fdrd5txIFU9iM76NYDAy9%2FScreenshot%202026-03-02%20at%2015.57.29.png?alt=media&#x26;token=db94e148-d522-48d8-8443-03b65f56e882" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}

### Enable for all repositories

Once you’re happy with the results, go back to the [GitLab MR Checks](https://app.aikido.dev/settings/integrations/gitlab/checks) page and enable checks for the rest of your repositories.

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fu4odXQtfh1zqSP2cg8jf%2FScreenshot%202026-03-02%20at%2015.36.19.png?alt=media&#x26;token=bd3c2e6f-5026-4a69-ba20-7a2ffb94d3dd" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}

### Set the default for new repositories

In the top-right, open `Actions` and select `Set Default for New Repos` and enable automatic configuration for newly added repositories in the future.

Need the UI walkthrough? See [Default PR/MR gating configuration for new repositories](https://help.aikido.dev/pr-and-release-gating/aikido-ci-gating-functionality/default-pr-mr-gating-configuration-for-new-repositories).
{% endstep %}
{% endstepper %}

# Source: https://help.aikido.dev/pr-and-release-gating/gitlab-mr-gating/gitlab-free-mr-scans-setup.md

# GitLab Free: MR Scans Setup

{% hint style="warning" %}
This setup is meant for the **GitLab Free** plan, where Service Accounts aren’t available and a dedicated user is used instead.

If you’re on **GitLab Premium, GitLab Ultimate or GitLab Server**, use a [**Service Account**](https://help.aikido.dev/pr-and-release-gating/gitlab-mr-gating/gitlab-server-ci-mr-gating-via-aikido-dashboard-with-a-service-account-token) instead of a user-based setup.
{% endhint %}

## Set up GitLab MR scanning

{% stepper %}
{% step %}

### Create a dedicated GitLab user

Create a dedicated user like `AikidoSecurity[YourCompany]`. Use it only for Aikido.

For easy recognition, use the [Aikido logo](https://www.aikido.dev/press-kit) as the profile picture.

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FExMKDK0Kq5GaL5zFgLXE%2FScreenshot%202026-03-02%20at%2013.12.14.png?alt=media&#x26;token=c3d98063-0a4f-4616-81d5-9b36f646f2d3" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}

### Create a Personal Access Token

Log in as the new user.

Go to **Preferences** → [**Personal access tokens**](https://gitlab.com/-/user_settings/personal_access_tokens).

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

### Invite your Aikido user to your group

Log back in with your own GitLab account.

Go to [**Groups**](https://gitlab.com/dashboard/groups).

For each group you want to enable, open the group.

Go to **Manage** → **Members** → **Invite members**.

Invite the dedicated Aikido user.

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FeyAWVZor3jHbjkm3ByN1%2FScreenshot%202026-03-02%20at%2013.47.09.png?alt=media&#x26;token=e898b51f-c031-4fdf-8f1c-4d417aafd668" alt=""><figcaption></figcaption></figure></div>

Give it at least **Maintainer** access.

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FdKbXaGuCkyIIE0Ec4x5U%2FScreenshot%202026-03-02%20at%2016.16.56.png?alt=media&#x26;token=49960b51-c8c8-4e34-af96-46a6e1f9fa75" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}

### Enable the integration

In Aikido, open the [Integrations](https://app.aikido.dev/settings/integrations?section=ci) page. Then select **GitLab CI** under **MR Quality Gating**.

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FanPFjh0BJsrtmWtLrA94%2FScreenshot%202026-03-02%20at%2015.11.44.png?alt=media&#x26;token=d9c0c7fe-14bd-46a4-9181-be67cc4aceac" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}

### Paste the Personal Access Token

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

Comments should appear as the dedicated user. For example, `@AikidoSecurity[YourCompany]`.

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F7ndP1pShIKSuT1XNfUxf%2FScreenshot%202026-03-02%20at%2015.28.18.png?alt=media&#x26;token=da586c8f-62ac-4501-aae8-5156262e1e12" alt=""><figcaption></figcaption></figure></div>
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

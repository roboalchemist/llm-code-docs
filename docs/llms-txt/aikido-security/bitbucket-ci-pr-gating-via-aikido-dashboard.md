# Source: https://help.aikido.dev/pr-and-release-gating/bitbucket-pr-gating/bitbucket-ci-pr-gating-via-aikido-dashboard.md

# Bitbucket Free & Standard: PR Scans Setup

{% hint style="warning" %}
This setup is meant for **Bitbucket Free and Standard** plans, where Workspace Access Tokens aren’t available and a dedicated user is used instead.

If you’re on **Bitbucket Premium**, use a [**Workspace Access Token**](https://help.aikido.dev/pr-and-release-gating/bitbucket-pr-gating/bitbucket-server-ci-pr-gating-via-aikido-dashboard-with-a-workspace-access-token) instead of a user-based setup.
{% endhint %}

## Set up Bitbucket PR Scanning <a href="#setting-up-bitbucket-ci" id="setting-up-bitbucket-ci"></a>

{% stepper %}
{% step %}

### Create a dedicated Bitbucket user

Create a dedicated user like `AikidoSec`. Use it only for Aikido.

Give this user admin access on the repositories you want to gate. Aikido needs it to create and manage repository webhooks.
{% endstep %}

{% step %}

### Enable the integration

Log in to Bitbucket as the new user.

In Aikido, open the [Integrations](https://app.aikido.dev/settings/integrations?section=ci) page. Then select **Bitbucket** under **PR Quality Gating**.

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FyhWUQUTioYABz0cFLreH%2FScreenshot%202026-02-26%20at%2016.57.41.png?alt=media&#x26;token=a067db95-0e43-446e-9138-60f375435d69" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}

### Grant access

You’ll be redirected to Bitbucket. Approve the requested access.

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FHmKJKlGthJTJe0B1TYbi%2FScreenshot%202026-02-26%20at%2016.35.57.png?alt=media&#x26;token=e370079f-f31a-4bdd-a52f-d8f28298d484" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}

### Configure your first repository

After authorization, Aikido opens the [Bitbucket PR Checks](https://app.aikido.dev/settings/integrations/bitbucket/checks) page.

Start with **one repository** first. Confirm everything works before rolling out broadly.

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F0eibK8ojKanuDITxflWu%2FScreenshot%202026-02-26%20at%2017.02.36.png?alt=media&#x26;token=1705263e-d2c4-449f-8e3f-f34d0f07af2d" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}

### Verify with a new PR

Open a new PR in the repo you configured. Then confirm the checks run.

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FeSH1ZoYhzYiLxzKmDhnm%2FScreenshot%202026-02-26%20at%2018.04.55.png?alt=media&#x26;token=af5885b8-bf74-4ad8-a25a-c71cc58f123b" alt=""><figcaption></figcaption></figure></div>

Comments should appear as the user you created in step 1 (for example, `AikidoSec`).

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F8wfRFz2ab6HXIU1kCW8R%2FScreenshot%202026-02-26%20at%2018.09.19.png?alt=media&#x26;token=bce9dfa7-8a41-4a24-b6c4-add7a045c982" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Enable for all repositories

Once you’re happy with the results, go back to the [Bitbucket PR Checks](https://app.aikido.dev/settings/integrations/bitbucket/checks) page and enable checks for the rest of your repositories.

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FWLLXnzjfz5188drBhv49%2FScreenshot%202026-02-26%20at%2018.13.59.png?alt=media&#x26;token=728ac22b-687a-4a69-80a5-7050288ea8e0" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}

### Set the default for new repositories

In the top-right, open `Actions` and select `Set Default for New Repos` and enable automatic configuration for newly added repositories in the future.

Need the UI walkthrough? See [Default PR/MR gating configuration for new repositories](https://help.aikido.dev/pr-and-release-gating/aikido-ci-gating-functionality/default-pr-mr-gating-configuration-for-new-repositories).
{% endstep %}
{% endstepper %}

{% hint style="info" %}
On **Bitbucket Free and Standard**, you **can’t require** the Aikido scan to be successful to prevent merges. This requires **Bitbucket Premium**.

See Atlassian: [Suggest or require checks before a merge](https://support.atlassian.com/bitbucket-cloud/docs/suggest-or-require-checks-before-a-merge/).
{% endhint %}

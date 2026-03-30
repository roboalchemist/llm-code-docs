# Source: https://help.aikido.dev/pr-and-release-gating/bitbucket-pr-gating/bitbucket-server-ci-pr-gating-via-aikido-dashboard-with-a-workspace-access-token.md

# Bitbucket Premium: PR Gating Setup

{% hint style="warning" %}
This setup is for **Bitbucket Premium**.

Use it when you want to authenticate via a **Workspace Access Token**. It also supports required checks before merge (PR gating).

If you’re on **Bitbucket Free or Standard**, use the [**user-based setup**](https://help.aikido.dev/pr-and-release-gating/bitbucket-pr-gating/bitbucket-ci-pr-gating-via-aikido-dashboard) instead.
{% endhint %}

## Set up Bitbucket PR Scanning <a href="#setting-up-bitbucket-ci" id="setting-up-bitbucket-ci"></a>

{% stepper %}
{% step %}

### Create a Workspace Access Token <a href="#creating-a-personal-access-token" id="creating-a-personal-access-token"></a>

In Bitbucket, go to `Workspace settings > Access tokens`.

Select **Create access token**.

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F0tMqyBiE0uIaVTbwK1XG%2FScreenshot%202026-02-27%20at%2011.50.37.png?alt=media&#x26;token=361d4f48-ea69-49ce-baa5-5b0e4b6bb458" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}

### Give it the right access

Name the token (for example, `AikidoSec`). Set an expiry date that matches your rotation policy.

Enable these scopes:

* **Repositories:** Read & Write
* **Pull Requests:** Read & Write
* **Webhooks:** Read & Write
* **Pipelines:** Read & Write

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FRbDyKsJGjoeu9Q9aOCUm%2FScreenshot%202026-02-27%20at%2012.25.21.png?alt=media&#x26;token=b1352514-c9a1-43ea-acd4-3937edda6509" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}

### Copy the access token

Copy the generated token. Paste it in step 5.

The token is only shown once. You can’t retrieve it later.

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FoKEuxddb6aBxiBUhbW8W%2FScreenshot%202026-02-27%20at%2012.06.22.png?alt=media&#x26;token=74139e62-8adb-4deb-adc9-da6d64cbb198" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}

### Enable the integration

In Aikido, open the [Integrations](https://app.aikido.dev/settings/integrations?section=ci) page. Then select **Bitbucket** under **PR Quality Gating**.

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FyhWUQUTioYABz0cFLreH%2FScreenshot%202026-02-26%20at%2016.57.41.png?alt=media&#x26;token=a067db95-0e43-446e-9138-60f375435d69" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}

### Add the token to Aikido

Paste the Workspace Access Token in Aikido. Aikido will validate the token and its permissions.

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FrWGbwSbblttruJO62DwY%2FScreenshot%202026-02-27%20at%2012.07.45.png?alt=media&#x26;token=44b8e9d2-951c-41a8-80f0-47e2a4637898" alt=""><figcaption></figcaption></figure></div>
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

Comments and check updates should appear as the Workspace Access Token identity (for example, `AikidoSec`).

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F8wfRFz2ab6HXIU1kCW8R%2FScreenshot%202026-02-26%20at%2018.09.19.png?alt=media&#x26;token=bce9dfa7-8a41-4a24-b6c4-add7a045c982" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Require the scan as a Merge Check

If you want to block merging until the scan succeeds, configure **required checks** in Bitbucket.

In Bitbucket, go to `Repository settings > Workflow > Branch restrictions`. Add or update a restriction for your target branch (for example, `main`).

Atlassian reference: [Suggest or require checks before a merge](https://support.atlassian.com/bitbucket-cloud/docs/suggest-or-require-checks-before-a-merge/).
{% endstep %}

{% step %}

### Enable for all repositories

Once you’re happy with the results, go back to the [Bitbucket PR Checks](https://app.aikido.dev/settings/integrations/bitbucket/checks) page and enable checks for the rest of your repositories.

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FWLLXnzjfz5188drBhv49%2FScreenshot%202026-02-26%20at%2018.13.59.png?alt=media&#x26;token=728ac22b-687a-4a69-80a5-7050288ea8e0" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}

### Set the default for new repositories

In the top-right, open `Actions` and select `Set Default for New Repos`.

See [Default PR/MR gating configuration for new repositories](https://help.aikido.dev/pr-and-release-gating/aikido-ci-gating-functionality/default-pr-mr-gating-configuration-for-new-repositories) for UI guidance.
{% endstep %}
{% endstepper %}

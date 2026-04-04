# Source: https://help.aikido.dev/pr-and-release-gating/aikido-ci-gating-functionality/default-pr-mr-gating-configuration-for-new-repositories.md

# Default PR/MR gating configuration for new repositories

If you frequently add repositories to Aikido, you can set a single default PR/MR gating configuration once, and Aikido will automatically apply it to every newly added repository in the future.

### Prerequisite <a href="#prerequisite" id="prerequisite"></a>

Make sure Aikido automatically **activates new repositories**.

If Aikido doesn’t activate the repository, it can’t apply the default configuration.

1. Go to [Repository Settings](https://app.aikido.dev/settings/integrations/repositories).
2. Enable **Automatically activate new repos**.

Need the UI walkthrough? See [Ensuring Aikido Scans New Repositories](https://help.aikido.dev/code-scanning/miscellaneous/ensuring-aikido-scans-new-repositories).

### Steps <a href="#steps" id="steps"></a>

{% stepper %}
{% step %}

### Go to the configuration page

Open [Repositories](https://app.aikido.dev/repositories) → [Pull/Merge Requests](https://app.aikido.dev/repositories/prs) → `Manage PR/MR Checks`.

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F1CAGcnPxwfF6vEcEgogJ%2FScreenshot%202026-02-27%20at%2014.56.43.png?alt=media&#x26;token=32195cd7-d1e6-41d3-8630-02c93034d7ca" alt=""><figcaption></figcaption></figure></div>

In the top-right, open `Actions` and select `Set Default for New Repos`.

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fyc4F5KjLO7ULkwnwvIs0%2Fimage.png?alt=media&#x26;token=517a2384-f8f1-41d7-a95d-139980c97431" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}

### Turn on auto-apply for new repositories

Enable **Automatically activate scan configuration for new repos**.

This makes Aikido apply your default PR/MR gating settings to new repositories.

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FPZfGFDe8zsLoSWeYhH2X%2Fimage.png?alt=media&#x26;token=86c0a597-8bbf-44de-b7c9-805e549bbd3e" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}

### Choose the default settings

Set the configuration you want Aikido to apply by default.

This includes:

* Which scans run on PRs/MRs
* The severity threshold that fails the check
* When comments are added

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fa6a3WFJxxNzQnG7bDfH9%2FScreenshot%202026-02-27%20at%2014.40.40.png?alt=media&#x26;token=9375ef18-fcec-417d-afff-609698e43d76" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}

### Save your settings

Click **Save Settings**.

Going forward repositories that are added will have this new configuration applied.

Existing repositories will not be affected by this change.
{% endstep %}
{% endstepper %}

# Source: https://docs.luciq.ai/product-guides-and-integrations/product-guides/ai-features/resolve-agent/configure-github-webhooks-to-track-ci-and-merge-status.md

# Configure GitHub Webhooks to Track CI & Merge Status

To track the full journey from crash to fix to validation, Smart Resolve integrates with your CI system by listening to GitHub events through a webhook. This guide walks you through setting up a repository-level GitHub webhook to track CI build status and pull request merges, enabling automated validation inside the Luciq dashboard.

{% hint style="info" %}
Before continuing, make sure you’ve [connected your GitHub repository to Luciq](https://docs.luciq.ai/product-guides-and-integrations/product-guides/ai-features/resolve-agent/source-code-connection-github) using the CodeLink GitHub app.
{% endhint %}

### Why Connect Your CI to Luciq?

Once your repository is connected, setting up a webhook allows Smart Resolve to:

* Monitor whether AI-generated fixes pass your test suite.
* Display CI status and merge results directly in your Smart Resolve workflow.
* Block unvalidated or failing fixes from progressing to release.
* Streamline your crash resolution lifecycle with minimal manual effort.

{% hint style="warning" %}

### **Security and Privacy**<br>

Luciq listens only to metadata events (`status`, `check_run`, and `pull_request`). Webhook communication is encrypted and authenticated using a shared secret provided by Luciq Support.
{% endhint %}

### What This Webhook Tracks?

The GitHub webhook enables Smart Resolve to track:

* **CI Status**
  * `status`: External CI tools (e.g. CircleCI, Jenkins, Bitrise)
  * `check_run`: GitHub Actions workflows
* **Merge Status**
  * `pull_request`: Detects when pull requests are merged into target branches

#### Prerequisites

* Your GitHub repo is connected to Luciq via CodeLink ([Set it up here](https://docs.luciq.ai/docs/product-guides-connect-github)).
* **Admin access** to the GitHub repository
* Your **Luciq Application Token**
* A **Webhook Secret**, you can get it by reaching out to Luciq Support

#### Step 1: Get Your Webhook Secret

1. Open a **GetHelp ticket** by contacting Luciq Support or reaching out to your designated customer success manager.
2. Request a **GitHub Webhook Secret** tied to your application
3. Save this token securely — it will be used to validate incoming webhook events and other integrations.

#### Step 2: Open GitHub Webhook Settings

1. On GitHub, navigate to the main page of the repository.
2. Under your repository name, click **Settings → Webhooks → Add webhook.**

#### Step 3: Configure the Webhook

| Field        | Value                                                                                                                                                                                                     |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Payload URL  | <p><code><https://api.instabug.com/api/web/public/agent_webhooks/github?application_token=YOUR_APP_TOKEN></code></p><p>Replace <code>YOUR\_APP\_TOKEN</code> with your actual Luciq Application Token</p> |
| Content type | `application/json`                                                                                                                                                                                        |
| Secret       | The Webhook Secret you obtained from Luciq Support                                                                                                                                                        |

#### Step 4: Select Events

Under "**Which events would you like to trigger this webhook?**", choose:

* Status – Tracks CI status from external CI tools.
* Check run – Tracks CI status from GitHub Actions workflows.
* Pull request – Tracks PR merge status.

{% hint style="warning" %}
**Do not select “Send me everything”**
{% endhint %}

#### Step 5: Save and Test

1. Click **Add webhook**
2. GitHub will automatically send a ping event to test delivery
3. In **Recent Deliveries**, verify a successful response (green checkmark)

### Troubleshooting

If your webhook doesn’t appear to be working as expected:

* **No events showing in Luciq dashboard**
  * Make sure the correct events (`status`, `check_run`, `pull_request`) are selected
  * Confirm that the repo is connected to Luciq
* **Webhook returns 401 (Unauthorized)**
  * Double-check that you’re using the correct webhook secret provided by Luciq
  * Ensure the secret hasn’t expired or been changed
* **CI status not updating**
  * For GitHub Actions, confirm that your workflow triggers a `check_run` event
  * For external CI tools, make sure they emit GitHub `status` events
* **Merge not detected**
  * Verify that the pull request is merged into the same branch Smart Resolve is tracking (e.g. `main` or `master`)
  * Ensure the `pull_request` event is enabled in webhook settings

If the issue persists, contact our Support team with a screenshot of your webhook settings and recent deliveries.

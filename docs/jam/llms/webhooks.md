# Source: https://jam.dev/docs/integrations/webhooks.md

# Webhooks

Webhooks allow you to connect Jam to external systems and receive real-time notifications when key events occur.\
This makes it possible to automate workflows, trigger actions in Intercom, or log events in your internal systems without relying on polling.

{% hint style="warning" %}
Webhooks are currently in **beta**. To enable access for your workspace, please contact our Sales team.
{% endhint %}

***

### 🧪 Supported Events (Beta)

At this stage, Jam supports two events related to the Intercom workflow:

* **`intercom.recorder.recorded`** – fired when a customer records and submits their screen.
* **`intercom.recorder.opted_out`** – fired when a customer chooses not to record their screen.

{% hint style="info" %}
More events will be added as we expand the webhook beta.
{% endhint %}

***

### Sample Payloads

All webhook events share the same general structure:

* **`id`** – unique identifier for the event.
* **`type`** – the event type (e.g. `intercom.recorder.recorded`).
* **`created_at`** – timestamp of when the event occurred.
* **`data`** – object containing event-specific information.

Example (`intercom.recorder.recorded`):

```json
{
  "id": "evt_12345",
  "type": "intercom.recorder.recorded",
  "created_at": "2025-09-09T12:00:00Z",
  "data": {
    "conversationId": "215470686832743",
    "jamId": "9573a43b-3ec9-49ab-b7e4-bf6cfc4bdfc",
    "recording_url": "https://jam.dev/r/rec_12345"
  }
}
```

***

### The Webhooks Tab in Jam Dashboard

Inside the **Jam Dashboard**, you’ll find a dedicated tab for Webhooks under:\
**Settings → Integrations → Webhooks**

From this tab you can:

* Create and manage endpoints.
* Subscribe to supported events.
* Monitor active integrations.

<figure><img src="https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2F8a1bZHXOtNkZF8O1Tr13%2Fimage.png?alt=media&#x26;token=4bffe5a1-63a4-4a7d-850d-262a80b4acd2" alt=""><figcaption></figcaption></figure>

***

### The Webhook Portal

Beyond the initial configuration, you can monitor and debug deliveries in the **Webhook Portal**. It allows you to:

* **View logs** of all delivery attempts (success and failure).
* **Replay events** that failed to deliver.
* **Access your Signing Secret** to validate incoming requests.
* **Monitor statistics** such as delivery success vs failure rates.
* **Inspect messages** and see full payloads with headers.

<figure><img src="https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2F0jX9xkCbMBvm4Mne9blp%2FScreenshot%202025-09-10%20at%2009.32.46.png?alt=media&#x26;token=fdfc9ad2-5d0a-42b0-a6f1-00b7af01e8bf" alt=""><figcaption></figcaption></figure>

<figure><img src="https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2FUGsQxrlGcVwNm8t2A99B%2Fimage.png?alt=media&#x26;token=b364b29e-a863-4bb6-ba2e-9ad599d888e5" alt=""><figcaption></figcaption></figure>

***

### How to Configure

#### 1. Creating a Manual Endpoint

1. Go to **Settings → Integrations → Webhooks → Manage**.
2. Click **Add Endpoint**.

<figure><img src="https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2FufVVSNvzmIGOWngQmgvS%2Fimage.png?alt=media&#x26;token=64488a74-8656-4db7-943d-b20f6d81a8fd" alt=""><figcaption></figcaption></figure>

3. Enter your endpoint URL.
4. Select the events you want to subscribe to (e.g. `intercom.recorder.recorded`, `intercom.recorder.opted_out`).
5. Click **Create**.

***

#### 2. Using Connectors

In addition to generic endpoints, Jam also provides **specific connectors** for popular integrations like Intercom.

**a) Intercom Fin Connector**

If you’re integrating with **Intercom Fin**:

1. In the **Webhook** dropdown, select **Intercom Fin**.
2. Paste the URL you copied from Intercom.
3. Under **Subscribe to Events**, ensure only the following are checked:
   * `intercom.recorder.recorded`
   * `intercom.recorder.opted_out`
4. Click **Create**.

<figure><img src="https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2FR8gb0OutUohiigoYHJsu%2FScreen%20Cast%202025-09-10%20at%209.38.55%20AM.gif?alt=media&#x26;token=46d938c9-f3c0-4ff9-b279-f1bce24df58f" alt=""><figcaption></figcaption></figure>

That’s it — Jam will now send Intercom events directly into your workflow.

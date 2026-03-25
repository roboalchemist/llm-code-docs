# Source: https://docs.luciq.ai/product-guides-and-integrations/integrations/datadog.md

# Datadog

### Visualize Luciq App Health in Datadog

Easily monitor your app’s performance and stability directly within Datadog by using our prebuilt **Luciq Blueprint**. This guide walks you through setting up the integration via HTTP, allowing you to visualize app health metrics like crash-free sessions, frustration-free sessions, and more.

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FH9RHj77cyTw5QpYlBb50%2Fimage.png?alt=media&#x26;token=4e519706-6680-49a5-a314-9c6ddfc9b65c" alt=""><figcaption></figcaption></figure>

#### 📌 Prerequisites

* A Datadog account with access to **App Builder**.
* An Luciq account with access to your project's **App Health dashboard**.
* Luciq API token and email (reach out to <support@luciq.ai> to obtain these).

### 🛠️ Steps to Set Up the Integration

{% stepper %}
{% step %}

#### Navigate to App Builder

From the left-hand navigation in Datadog, go to **Actions > App Builder**.

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2F0mpAizPLHFnA4BK5iSE4%2Fimage.png?alt=media&#x26;token=7d35e32b-683a-4b7f-a37d-b9ef64604baa" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

#### Select “Blueprints”

Click on the **Blueprints** tab at the top to access available integrations.

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2Fnqas0cUXtBypU52t2lGP%2Fimage.png?alt=media&#x26;token=04068988-cae4-410b-9776-a969c7eb1f6e" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

#### Search for Luciq

In the search bar, type **Luciq** and select the blueprint titled **Explore Luciq Sessions**.

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FEYIE8lDhmFdRYnZ4PiUP%2Fimage.png?alt=media&#x26;token=9e3a5387-8ae5-45b5-808f-3fc437e192fc" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

#### Click “Set up your connection”

Click the blueprint card to open the editor. On the left side, select **New Connection**.

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FKJ8Lu88nwJh4HM3wODTX%2Fimage.png?alt=media&#x26;token=bd8e1c66-ae37-4d38-a6a5-fc5521710534" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

#### Choose HTTP Connection

Select **HTTP Connection** as the integration method.

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2Fy1sPr9mcin0DoBClKFzE%2Fimage.png?alt=media&#x26;token=0879a14a-3b5d-4fbc-916f-31285c0ba665" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

#### Fill in Connection Details

In the modal, enter the following:

* **Base URL**: `https://dashboard-api.instabug.com`
* **Authentication Type**: `Token Auth`
* Add two token fields:
  * `token` → Luciq API token
  * `email` → Your registered Luciq email
* Then under **Request Headers**, add:\
  `authorization: Token token="{{ token }}", email="{{ email }}"`

Click **Next, Confirm Access**.

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FU7tDZV8P8mNT3M0ltoIp%2Fimage.png?alt=media&#x26;token=a24af112-7c16-46f2-9a1b-5f7b26b123ef" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

#### Set Access Permissions

Choose who can access this connection (e.g., only you, the org, or a team), then click **Create**.

You should now see a success message indicating the connection was created.

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FgkzLCIqKduxAcVvHHQxH%2Fimage.png?alt=media&#x26;token=881a4601-2af6-48a8-a6da-594d63340a2b" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}

#### ✅ You’re Done!

Once the connection is active, Datadog will begin visualizing live Luciq metrics like:

* Crash-free sessions
* Frustration-free sessions
* Session breakdowns over time

You can now fully monitor app health using Datadog’s native dashboards powered by Luciq data.

{% hint style="info" %}

#### 🧠 Need Help?

If you run into issues, please reach out to <support@luciq.ai> or your dedicated CSM.
{% endhint %}

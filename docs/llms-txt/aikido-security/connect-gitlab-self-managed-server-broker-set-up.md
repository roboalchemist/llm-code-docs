# Source: https://help.aikido.dev/code-scanning/connect-your-source-code/connect-gitlab-self-managed-server-to-aikido/connect-gitlab-self-managed-server-broker-set-up.md

# Connect GitLab Self-Managed Server (Broker Set-Up)

Aikido lets you connect a self-managed GitLab instance to scan and secure your code. Follow the steps below to connect your GitLab server to Aikido.

### Before you start

* The person setting this up needs access to both the GitLab instance **and** the GitLab group you want to connect.

{% hint style="warning" %}
An Aikido workspace always maps to a single GitLab group.

We recommend connecting Aikido to a top-level (root) group that contains all subgroups. If you don’t have a root group, create one workspace per GitLab group. You can do this after creating your first workspace via the top-left dropdown: “Add another workspace”.
{% endhint %}

## Configuration

{% stepper %}
{% step %}

### Create an Aikido account

To connect your GitLab server, first sign up or log in to Aikido using Google or Microsoft. On the [signup screen](https://app.aikido.dev/login), click **Google / Microsoft**.
{% endstep %}

{% step %}

### Start the GitLab setup

Once you’re authenticated, create a new workspace by clicking **Self-Managed** in the GitLab section.

![Select a source control provider to connect: GitHub, Azure DevOps, GitLab, or Bitbucket.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-4be1bf4a3d0bcc9641482ed36641a7c4d97ed5d9%2Fconnect-gitlab-self-managed-server-to-aikido_38929d5c-805a-4ee2-9881-67b5a316190d.png?alt=media)
{% endstep %}

{% step %}

### Enable Broker access

Enable the **Aikido broker** by clicking the toggle in the "Advanced Connection Options" section.

Click **Create Group** to continue.

![Aikido onboarding: Enter GitLab Self-Managed URL and access token to authenticate.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FDMVpZt1bwxhnZElIoGu5%2FScherm%C2%ADafbeelding%202026-01-27%20om%2015.15.28.png?alt=media\&token=c26da44c-6d3f-4237-bdf1-bb2b8de833fd)
{% endstep %}

{% step %}

### Configure the Broker

Configure the Broker using the guide below. After you deploy it, return here to finish the GitLab setup.

{% content-ref url="../../../miscellaneous-info/aikido-broker-for-internal-applications" %}
[aikido-broker-for-internal-applications](https://help.aikido.dev/miscellaneous-info/aikido-broker-for-internal-applications)
{% endcontent-ref %}

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F4TexnG7f9FVyi8mkOG9Q%2FScreenshot%202025-12-22%20at%2010.48.21.png?alt=media&#x26;token=e69fac71-7a6e-4efd-8ea6-25ca01b1692d" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Complete GitLab server setup

After you create the broker and deploy it in your environment, you can complete the GitLab setup.

First, copy the **Broker URL**. It looks similar to this:

```
https://55673-355dsfwea68cb.aikidobroker.com
```

Then click **Complete GitLab Server Setup**.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgrhts0YhFD1PjvtW3NvL%2FBroker_Clients_-_Gitlab_Server_EVAfKobo3u_-_Aikido_Security_%E2%80%94_Aikido.png?alt=media&#x26;token=c4a247df-8483-4ec4-80d9-2bfb494d40f8" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Enter the Broker URL

Paste the Broker resource URL from the previous step in the input field for the "server URL".

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fo4hRI8ViDdYpreixIVos%2FScherm%C2%ADafbeelding%202026-01-27%20om%2015.16.49.png?alt=media&#x26;token=8cf2b417-b61c-43e5-b2e1-5334a93c0578" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Create a GitLab personal access token (PAT)

Next, create a personal access token (PAT). We recommend using a dedicated service account

* Log in to your GitLab server
* Go to the admin area (`/admin`)
* Go to **Settings** → **Service accounts**
* Click **Add service account**, enter a name, then save

{% hint style="warning" %}
Add the service account to the GitLab group you want to connect, like any other user. See GitLab’s docs on [group members](https://docs.gitlab.com/ee/user/group/members/).
{% endhint %}

Now that the service account is created, you can create a PAT for it by clicking the three dots and select "**Manage access tokens**"

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FFT7nRO99qhMkOcxnWAP5%2FScherm%C2%ADafbeelding%202025-08-11%20om%2014.57.42.png?alt=media&#x26;token=f9ba8fbb-e70c-44ec-8b79-dd6cb09214aa" alt=""><figcaption></figcaption></figure>

* Click on "**Add new token**"
* Enter a name for the token, for example: `Aikido Security Access Token`
* Set an expiration date that matches your internal policy. Rotate the token before it expires.
* We need the following scopes to be selected:
  * **read\_user**
  * **read\_api**
  * **read\_repository**
* Click the **Create token** button at the bottom of the form.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FnVQ5yJX7Y287k8x4KoCQ%2FScherm%C2%ADafbeelding%202025-08-11%20om%2015.00.51.png?alt=media&#x26;token=d49e8025-7601-46af-93bb-bd48f797f421" alt=""><figcaption></figcaption></figure>

* Copy the token being shown on the screen and enter it in the input field.

**Important:** You won’t be able to see the token again after you leave this screen. Copy it before you continue.

Aikido will now check the connection to your GitLab server. If it fails, double-check the server URL and the token.
{% endstep %}

{% step %}

### Complete the installation

After you click **Next, Connect Group**, select the group you want to start with. You can always connect more groups later.

In the final step, select the repositories you want Aikido to monitor.
{% endstep %}
{% endstepper %}

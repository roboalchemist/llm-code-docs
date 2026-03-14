# Source: https://docs.mailtrap.io/guides/ai-powered-integrations/vercel.md

# Vercel

Mailtrap’s native integration with Vercel removes manual setup friction, minimizes configuration mistakes, and makes it easy to follow a reliable testing-to-production email workflow.&#x20;

This integration automatically configures the environment variables necessary for both testing (Sandbox) and production sending in your Vercel projects.&#x20;

{% hint style="info" %}
The integration adds a set of three variables (`API_KEY`, `USE_SANDBOX`, and `INBOX_ID`) for each of the three Vercel environments: **Development**, **Preview**, and **Production**.
{% endhint %}

#### Prerequisites

* **Admin rights** for your Mailtrap account.
* A [verified sending domain](https://docs.mailtrap.io/email-api-smtp/setup/sending-domain) set up within Mailtrap.
* An existing **Vercel account** with one or more projects.

### Step-by-step integration guide

{% stepper %}
{% step %}

### Initiate the integration

* Log in to your Mailtrap account
* Navigate to the [**Integrations** page](https://mailtrap.io/integrations) from the sidebar.
* Locate the **Vercel** card under the **AI & Development** section.
* Click the **Integrate** button.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FhlvHtPQkqMk70wTXIbva%2Fvercel%201.png?alt=media&#x26;token=4f9ac4f7-1fda-457b-8938-874bb871d59b" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Authorize with Vercel account

Click the **Authorize with Vercel** account button. You will be redirected to the Mailtrap listing page.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FZlDLXoaqCo0RAPDYfjjv%2Fvercel%202.png?alt=media&#x26;token=8224dd68-6261-409f-a7e7-3ce6c5367550" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Connect your Mailtrap account

On the Vercel integration page, click on **Connect Account** and then:

* Select your Vercel team.
* Select the specific project you want the integration to apply to.
  * **Note**: You’ll need to choose the project again on the Mailtrap side in the next step.
* Click **Connect Account** to proceed, and a new popup will appear.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FJthlJgavjqgy4v4yB58J%2Fvercel%204.png?alt=media&#x26;token=bed41d69-da6d-47c0-a60b-69ec97cc247c" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Currently, the integration cannot be added to all projects, only to specific ones.
{% endhint %}
{% endstep %}

{% step %}

### Select a Vercel project in Mailtrap

Select the specific Vercel project you want to configure from the dropdown menu.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FNOECYOxMfl4LQwzvQtbM%2Fvercel%205.png?alt=media&#x26;token=237c196f-4e29-41f9-85e6-73be861729ac" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Create an API Token

Choose the domain from which you intend to send emails and click **Create Token**. The token will be generated at the domain level.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FzukqKxnVpT7sBl7hJ8IM%2Fvercel%206.png?alt=media&#x26;token=b1688902-8de0-4e47-9713-89c0655497c0" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Add environment variables and complete the installation

The following variables will be added to your Vercel project:

* `MAILTRAP_API_KEY` – Required for both testing and sending.&#x20;
* `MAILTRAP_USE_SANDBOX` – Set to **True** to use Mailtrap's Sandbox for testing, or **False** for production sending.&#x20;
* `MAILTRAP_INBOX_ID` – Required if using the Sandbox. Select the desired Inbox from the dropdown.

Once you’re done reviewing the variables, click **Set Environment Variables**. This will finalize the integration and close the setup window.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FRZdyqkRZOdiOHs4K4iVa%2Fvercel%207.png?alt=media&#x26;token=44e03138-c66e-4719-b4ee-221ddc0071fa" alt=""><figcaption></figcaption></figure>

### Verifying the integration in Vercel

Once the setup is complete, you can verify the environment variables in your Vercel account:

1. Go to your Vercel project settings.
2. Navigate to the **Environment Variables** section.
3. You should see nine Mailtrap environment variables. A set of three variables (`API_KEY`, `USE_SANDBOX`, and `INBOX_ID`) for each of the three Vercel environments: **Development**, **Preview**, and **Production**.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FnHtxYFn0yAs9hcLAQk9K%2Fvercel%208.png?alt=media&#x26;token=6e11354f-6ec6-4312-89c0-0bd30dcd9e95" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}

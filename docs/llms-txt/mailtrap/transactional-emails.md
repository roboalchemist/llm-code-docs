# Source: https://docs.mailtrap.io/guides/integrations/supabase/transactional-emails.md

# Supabase Transactional Emails Integration

With Mailtrap SMTP, you can move beyond Supabase's limit of [2 emails per hour](https://supabase.com/docs/guides/auth/rate-limits) to a production-ready [email-sending solution](https://mailtrap.io/email-sending/) with comprehensive [analytics](https://mailtrap.io/actionable-analytics/).

Mailtrap’s native integration with Supabase streamlines your workflow by automatically populating your Supabase project with Mailtrap’s SMTP credentials. You can access this setup via the Integrations page in Mailtrap or through the [Supabase Marketplace](https://supabase.com/docs/guides/integrations/supabase-marketplace).

{% hint style="info" %}
Currently, this integration supports Sending Domains (API/SMTP) only and does not include Email Sandbox configuration. If you would like to see Sandbox support in the future, please [leave a feature request here](https://feedback.mailtrap.io/).
{% endhint %}

#### Prerequisites:

* **Admin rights** for your Mailtrap account.
* A [**verified sending domain**](https://app.gitbook.com/s/S3xyr7ba7aGO19rc8dSK/email-api-smtp/setup/sending-domain) set up within Mailtrap.
* An existing **Supabase account** with an active project.

#### Use cases:

* **Supabase Auth**: Managing email confirmations, magic links, and password resets.
* **Database Events**: Triggering transactional emails based on database changes.
* **User Interaction**: Powering contact forms or "Send Message" features.

{% hint style="info" %}
Sending automated emails via Supabase Edge Functions is not covered by this integration. Please refer to our [dedicated guide for Edge Functions](https://mailtrap.io/blog/supabase-send-email/#Configure-Supabase-Edge-Functions-and-Database-Webhooks).
{% endhint %}

### Step-by-step integration guide

{% stepper %}
{% step %}
**Initiate the integration**

* Log in to your Mailtrap account.
* Navigate to the [**Integrations** page](https://mailtrap.io/integrations) from the sidebar.
* Scroll to the **AI & Development** section (or search for "Supabase") and locate the **Supabase** card.
* Click the **Integrate** button.

<div align="left" data-with-frame="true"><figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FgAqvZPrITWKCnXGqlvMB%2FScreenshot%202025-12-18%20at%2012.49.46.png?alt=media&#x26;token=eb0177b8-a2ca-4303-9383-d5af2e0fd996" alt="" width="563"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
**Authorize access**

* On the setup screen, click **Connect Supabase**.

<div align="left" data-with-frame="true"><figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2F6gZbPLj7bTHLxR5Z7rS8%2FScreenshot%202025-12-18%20at%2012.50.24.png?alt=media&#x26;token=078f32de-c759-4bb4-8bf8-60e8d47cc7da" alt="" width="563"><figcaption></figcaption></figure></div>

* Review the permissions for the access of your Supabase organizations and projects, and click **Authorize Mailtrap**.

<div align="left" data-with-frame="true"><figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fd0g8GG8Tulyfdb7kEBr3%2FScreenshot%202025-12-18%20at%2013.08.34.png?alt=media&#x26;token=e6fe2a3f-5464-4573-8b19-2d5b28750bd8" alt="" width="375"><figcaption></figcaption></figure></div>

{% hint style="info" %}
**Write** and **Read** access is required to update configurations. Moreover, you can revoke the authorization at any time.
{% endhint %}
{% endstep %}

{% step %}
**Select your project**

Once authorized, Mailtrap will load your available Supabase projects. Then, all you need to do is:

* Click the **Select a Supabase project** dropdown menu
* Choose the specific project you wish to integrate (e.g., Test Integration).

<div align="left" data-with-frame="true"><figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2F9UTVQOupWXHZrkCpJm1D%2FScreenshot%202025-12-18%20at%2013.12.29.png?alt=media&#x26;token=50021618-45ad-4903-91d9-23e7cc8f1861" alt="" width="563"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
**Create an API Token**

* In the **Create an API token** section, use the dropdown menu to select the Mailtrap Domain you want to use for sending emails.
* Click **Create Token**.

<div align="left" data-with-frame="true"><figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FkuV2zVSH9DVZD2nwWeSs%2FScreenshot%202025-12-18%20at%2013.15.57.png?alt=media&#x26;token=c8594ec4-7665-4290-8e7c-5cd64697f4ea" alt="" width="563"><figcaption></figcaption></figure></div>

{% endstep %}

{% step %}
**Configure sender details**

Define who the emails will appear to be coming from.

* Sender name: The name you want displayed in the recipient's inbox (e.g., Julia or Support Team).
* Sender email: The local part of the email address (e.g., enter noreply to create <noreply@your-domain.com>).
* Mailtrap will generate a preview of the SMTP settings (Host, Port, Username, etc.).
* Click Configure SMTP to finish the process.

You will see a confirmation message stating: "*Successfully configured Supabase SMTP*."

<div align="left" data-with-frame="true"><figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2F9BK40321SbpbSVlcrw47%2FScreenshot%202025-12-18%20at%2013.18.09.png?alt=media&#x26;token=7997f97f-f06e-48ee-81b2-36f4b2cc10bf" alt="" width="563"><figcaption></figcaption></figure></div>
{% endstep %}
{% endstepper %}

### Manual integration

You can also integrate Mailtrap SMTP with Supabase manually.&#x20;

{% stepper %}
{% step %}
**Obtain your sending credentials**

* Go to **Sending Domains** and select your domain.

<div align="left" data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-4020842616295e82743e1641477299033f219fe1%2Fsupabase-and-mailtrap-integration-1.png?alt=media" alt="" width="563"></div>

* Click on **Integration**, select **Transactional Stream**, and click **Integrate**.

<div align="left" data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-b35663fb2b9a82ebedfc9d1922f3e2c4ba61ff3e%2Fsupabase-and-mailtrap-integration-2.png?alt=media" alt="" width="375"></div>

* Under the **SMTP** tab, you can find your sending credentials, which include **Host**, **Port**, **Username**, and **Password**.

<div align="left" data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-540a8cd275ed18974c92d80c2ab774113ac41af3%2Fsupabase-and-mailtrap-integration-3.png?alt=media" alt="" width="375"></div>
{% endstep %}

{% step %}
**Update the SMTP server in Supabase**

* Open your Supabase [project dashboard](https://supabase.com/dashboard/projects) and select your project.

<div align="left" data-with-frame="true"><figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FS4ZCZOCo4Astw64lSwel%2Fsupabase%20and%20mailtrap%20integration.png?alt=media&#x26;token=e64ddb83-9a72-4d5e-9efe-1b7876186df2" alt="" width="375"><figcaption></figcaption></figure></div>

* Click on **Authentication** → **SMTP settings**.

<div align="left" data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-0e65d08e755f313ec97dc39a1a13ea283a255f76%2Fsupabase-and-mailtrap-integration-5.png?alt=media" alt="" width="563"></div>

* Click on **Emails** → **SMTP Settings** and enable the **Enable Custom SMTP** toggle. Update **Host**, **Port**, **Username**, and **Password** with your Mailtrap credentials, then click **Save changes**.
* Update the **Sender details** and **SMTP provider settings** like in the screenshot below, and hit **Save changes**.

<div data-with-frame="true"><figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FXn3hr9e9j3YtJUJMYAPh%2Fimage.png?alt=media&#x26;token=6cc48892-4fa1-46e3-8b61-1a884d4299da" alt=""><figcaption></figcaption></figure></div>

### **Monitor your email performance**

Once you send emails from your Supabase project, they should arrive in both your recipient's inbox and your **Mailtrap Email Logs**. There, you can see useful information such as delivery time, opens/clicks, email HTML source, [spam analysis](https://app.gitbook.com/s/S3xyr7ba7aGO19rc8dSK/email-sandbox/deliverability-tests), and more.

<div align="left" data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-f4a4d4962b57d9d579a962d326a03186a5764219%2Fsupabase-and-mailtrap-integration-9.png?alt=media" alt="" width="563"></div>

You can read more about **Mailtrap Email Logs** in our [dedicated article](https://app.gitbook.com/s/S3xyr7ba7aGO19rc8dSK/email-api-smtp/analytics/logs).

Additionally, you'll be able to see all important stats regarding your sent emails, such as opens, clicks, bounces, and more.

For more information on **Mailtrap Analytics**, [click here](https://app.gitbook.com/s/S3xyr7ba7aGO19rc8dSK/email-api-smtp/analytics/dashboard).
{% endstep %}
{% endstepper %}

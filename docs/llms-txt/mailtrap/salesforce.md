# Source: https://docs.mailtrap.io/guides/integrations/salesforce.md

# Salesforce

[Salesforce](https://www.salesforce.com/ap/) is a cloud-based CRM platform used by businesses to manage customer relationships, sales, and marketing.

With the Mailtrap App for Salesforce, you can route your transactional and marketing emails through [Email Sandbox](https://mailtrap.io/email-sandbox/) to test and inspect them before they reach real recipients.&#x20;

In this guide, you'll learn how to:

* [Configure Named Credentials](https://docs.mailtrap.io/guides/integrations/salesforce#id-1-how-to-configure-named-credentials)
* [Configure Mailtrap App](https://docs.mailtrap.io/guides/integrations/salesforce#id-2-configure-mailtrap-app)
* [Enable the Sandbox mode](https://docs.mailtrap.io/guides/integrations/salesforce#id-3-enabling-the-sandbox-mode)

## 1) How to configure Named Credentials

The Mailtrap package requires a [Named Credential](https://help.salesforce.com/s/articleView?id=xcloud.named_credentials_about.htm\&type=5) called MailTrap\_To\_SF to communicate with your Salesforce org. To set it up, you need to:

* [Assign permission set](https://docs.mailtrap.io/guides/integrations/salesforce#assign-permission-set)
* [Create Named Credentials](https://docs.mailtrap.io/guides/integrations/salesforce#create-named-credentials)
* [Add access to the Named Credentials](https://docs.mailtrap.io/guides/integrations/salesforce#add-access-to-the-named-credentials)

{% hint style="info" %}
**Useful link**: [What are Named Credentials?](https://help.salesforce.com/s/articleView?id=xcloud.nc_basics.htm\&type=5)
{% endhint %}

### Assign permission set

First, you need to assign Mailtrap Admin permission set to User who will configure the app.

* In **Setup** go to **Users** (under **Administration**) and open the **Users** settings.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2F2nOkpA4XwMEQJB5T7X7R%2Fsalesforce%201.png?alt=media&#x26;token=c0777dfc-9a56-450b-85c0-a6067fa8bab0" alt=""><figcaption></figcaption></figure>

* Under the **Permission Set Assignments** list, click on **Edit Assignments**.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FWwuxgHndaN1X9SXwBklG%2Fsalesforce%202.png?alt=media&#x26;token=cf0a7dad-8587-4255-892e-033ad0e219f8" alt=""><figcaption></figcaption></figure>

* Select **MailTrap Admin** and hit the **Save** button.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FHJtCCKDDwWZOVF7rOMrT%2Fsalesforce%203.png?alt=media&#x26;token=c56b85f4-a590-400d-b370-98b236d8f862" alt=""><figcaption></figcaption></figure>

### Create Named Credentials

#### Step 1. Connected App to Salesforce

* Navigate to **Setup** → **Apps** → **External Client Apps** → **External Client App Manager** and click on **New External Client App**.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fjn4PQgQELQoxTRBchutj%2Fstep%204.png?alt=media&#x26;token=fcc38125-4881-401a-9e7d-701f4958bb57" alt=""><figcaption></figcaption></figure>

* Then, enter the required **Basic Information**, such as **External Client App Name**, **API Name**, **Contact Email**, and **Distribution State**.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fo0UMl3aofzAntIYJ6zWB%2Fstep%205.png?alt=media&#x26;token=0fa903eb-7d7e-477c-9ea8-d3aca1551664" alt=""><figcaption></figcaption></figure>

* Next, make sure to check the **Enable OAuth** box and configure it with the following settings:
  * **Callback URL** – For now, use `https://www.example.com` (we will change it later);
  * **OAuth Scopes**  – Select **Manage user data via APIs (api)** and Perform **requests at any time (refresh\_token, offline\_access)**.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2F3Rhjj4s3jlD0xZTvRm7m%2Fstep%206.png?alt=media&#x26;token=6ebabba1-964f-4efd-bc5f-52e24f36e3ae" alt=""><figcaption></figcaption></figure>

* Under **Flow Enablement**, tick the **Client Credentials Flow** and hit the **Create** button.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FtqafZCMaThxYGcwozPqI%2Fstep%207.png?alt=media&#x26;token=536ae0da-1034-4a18-976c-843fdf0304eb" alt=""><figcaption></figcaption></figure>

* Under the **Policies** tab, click **Edit**. This will allow you to make the required changes to **OAuth Policies**.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fv1lyp98LFZhgQx0p2tfp%2Fstep%208.png?alt=media&#x26;token=7712f0b2-f49f-4f0e-aa7b-25eace74a9fb" alt=""><figcaption></figcaption></figure>

* Enable **Client Credentials Flow** and enter the email address of the **Admin User** with **MailTrap Admin permission** set assigned.&#x20;
* Select **Refresh Token** is valid until revoked.&#x20;
* Hit the **Save** button.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fh1YhPrhndfbat1vg9LnN%2Fstep%209.png?alt=media&#x26;token=eec681b8-f72d-4fd2-aedc-0b0bc501b223" alt=""><figcaption></figcaption></figure>

* Go to the **Settings** tab, expand the **OAuth Settings**, and click on **Consumer Key and Secret**.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FPmnlle73GHXtRN5cdj9K%2Fstep%2010.png?alt=media&#x26;token=a40d708f-d955-4413-b411-d1baf4f2a85c" alt=""><figcaption></figcaption></figure>

* You will be redirected to a page where you can see your **Consumer Key** and **Consumer Secret**, you should copy both of them.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FRcGlEmyfjurvOyHa1Stv%2Fstep%2011.png?alt=media&#x26;token=08075dfa-ac0d-4b5d-a185-f6fca6891687" alt=""><figcaption></figcaption></figure>

#### Step 2. Create Auth.Provider

{% hint style="info" %}
**Useful links**:

* [Configure a Salesforce Authentication Provider](https://help.salesforce.com/s/articleView?id=xcloud.sso_provider_sfdc.htm\&type=5)

* [My Domain (for finding your domain URL)](https://help.salesforce.com/s/articleView?id=xcloud.domain_name_overview.htm\&type=5)
  {% endhint %}

* Navigate to **Setup** → **Identity** (Under **Settings**) → **Auth.Providers** and click on **New**.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2F42DzX2T20uE5mXcktrDw%2Fstep%2012.png?alt=media&#x26;token=b3d1913e-adfc-43fd-9d32-152be7fc15a9" alt=""><figcaption></figcaption></figure>

* Then, enter the following settings for **Auth. Provider**:
  * For **Provider Type**, select **Salesforce**.
  * For **Consumer Key** and **Consumer Secret** you should paste from the **Connected App**.
  * Paste ***api refresh\_token offline\_access*** in **Default Scopes**.
  * **Authorize Endpoint URL**: Your domain URL + `/services/oauth2/authorize`
  * **Token Endpoint URL**: Your domain URL + `/services/oauth2/token`

{% hint style="info" %}
Domain URL can be found under Company Settings → My Domain.
{% endhint %}

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FQtOlyKQDm7GViMPFviPX%2Fstep%2013.png?alt=media&#x26;token=28ef40be-a650-4559-826d-c8b5034597e9" alt=""><figcaption></figcaption></figure>

* Copy **Callback URL** from **Auth.Providers**.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2F2YiKNaB3DbVOo4qqpkUR%2Fstep%2014.png?alt=media&#x26;token=8feccdf6-2e60-49f7-906a-5e4c49b1f1a7" alt=""><figcaption></figcaption></figure>

* Paste the **Callback URL** into the **Connected App** instead of `https://www.example.com`.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FOY8OGSTHDNSSvSeAdSwV%2Fstep%2015.png?alt=media&#x26;token=c0da5522-4b0f-4db6-8fe6-3632a95968fb" alt=""><figcaption></figcaption></figure>

#### Step 3. Named Credentials to Salesforce

{% hint style="info" %}
**Useful links**:

* [External Credentials](https://help.salesforce.com/s/articleView?language=en_US\&id=sf.nc_create_edit_external_credential.htm\&type=5)

* [Enable External Credentials Principals](https://help.salesforce.com/s/articleView?id=xcloud.nc_enable_ext_cred_principal.htm\&type=5)
  {% endhint %}

* Navigate to **Setup** → **Named Credentials** (under **Security**)→ click on **External Credentials** and hit the **New** button.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2F3sZShH6fTk66OATyJhOl%2F1.png?alt=media&#x26;token=136f5dfd-38ed-41e3-82ce-e0999c69e21e" alt=""><figcaption></figcaption></figure>

* Then, fill in all necessary information:
  * **Name**: MailTrap\_To\_SF
  * **Authentication Protocol**: OAuth 2.0
  * **Authentication Flow Type**: Browser Flow
  * **Scope**: api refresh\_token offline\_access
  * **Identity Provider**: select the Auth.Provider you created – `ThisOrg`

Once you’re done, make sure to hit the **Save** button.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FyUI98deeWVBGBW80QHBF%2F2.png?alt=media&#x26;token=1d062fc5-09ef-413d-a791-bcd4be765804" alt=""><figcaption></figcaption></figure>

* Navigate to **Named Credentials**, click **New**.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FNfUpxxrD1qHkGSMFH1Mi%2F3.png?alt=media&#x26;token=1e735c4c-748c-4307-8b47-1205c30c5726" alt=""><figcaption></figcaption></figure>

* Fill in all necessary information:
  * **Label and Name**: MailTrap\_To\_SF&#x20;
  * **URL**: Your domain URL
  * **External Credential**: select External Credential you created before – MailTrap\_To\_SF
  * **Allowed Namespaces for Callouts**: RWMailtrap

{% hint style="danger" %}
Name should specifically be **MailTrap\_To\_SF**, no other can be used for MailTrap package.
{% endhint %}

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2F6usC2R2qyYQ7J0VMLeeR%2F4.png?alt=media&#x26;token=4e378e59-fb0e-4e50-ae11-195d250ab09f" alt=""><figcaption></figcaption></figure>

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fw4iLMQLqKH6xdiHpx5nK%2F5.png?alt=media&#x26;token=951d60c6-58bc-4835-86e7-98f7e0238884" alt=""><figcaption></figcaption></figure>

* Once you’re done, click **Save**, and go back to the **External Credentials** tab to open it.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FZQsA8cHiAKK0AbWXyhbj%2F6.png?alt=media&#x26;token=666dce16-023d-4976-8054-3bdd71820949" alt=""><figcaption></figcaption></figure>

* In the **Principals** section click **New**.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FvTjAXE5PcjO2bVAqF4oI%2F7.png?alt=media&#x26;token=a6c311f7-c383-4542-9013-e6f87ee5ad19" alt=""><figcaption></figcaption></figure>

* Configure it as in the screenshot below, then click **Save**.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FCXPF4hQIYOHXsiofT37b%2F8.png?alt=media&#x26;token=6bc8366c-0d84-4569-a951-566ee5342376" alt=""><figcaption></figcaption></figure>

* In the **Principals** section click the menu button underneath **Actions**:

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FIOv9cbfgwaSNXeFrrGvJ%2F9.png?alt=media&#x26;token=82332b4f-527d-436c-aeb8-d0212fa5a99c" alt=""><figcaption></figcaption></figure>

* Then, **Authenticate**:

<div align="center"><figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FaSZxmnrodEzzbKiqFdLt%2F10.png?alt=media&#x26;token=72517a8a-a940-48cf-916c-c50e121d0a88" alt=""><figcaption></figcaption></figure></div>

* Login to the Salesforce organization, **Allow** access, and confirm.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FUcBEAeTp3TC8Xf7LDAPP%2F11.png?alt=media&#x26;token=7f29e72a-7695-438f-9675-e5bc68ad79ac" alt=""><figcaption></figcaption></figure>

### Add access to the Named Credentials

* Go to the **Profiles** page and open the profile used for your use.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FWA0mUz0snqbqb76wxX36%2F12.png?alt=media&#x26;token=a3262a3d-f5c5-43c6-a984-da371871a3d7" alt=""><figcaption></figcaption></figure>

* At the **Enabled External Credential Principal** **Access** section click **Edit**.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FGQvlt73eaxEE2YOI0RSn%2F13.png?alt=media&#x26;token=e6f578c2-1a92-4e8a-ae6a-232327492dad" alt=""><figcaption></figcaption></figure>

* Select **MailTrap\_To\_SF – 1** and click **Save**.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fnr5lbkE3k5yGIy4XBuPz%2F14.png?alt=media&#x26;token=504555a4-ba74-43ab-8dc9-95efbdfeed32" alt=""><figcaption></figcaption></figure>

And that’s it, your application is ready!

## 2) Configure Mailtrap App

To enable the Mailtrap app for Salesforce, you need to connect your Mailtrap account by adding a [Mailtrap API Token](https://docs.mailtrap.io/email-api-smtp/setup/api-tokens). To do this:

* First, navigate to the Mailtrap app via **App Launcher**.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FdjG1csJQMHuaOTm77vcD%2F1.png?alt=media&#x26;token=ff9b9e5d-ded0-4ace-bf61-47128e6a2e54" alt=""><figcaption></figcaption></figure>

* Then, click on **Connect Mailtrap account**.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FGrasFzWxw3SmClaXLHYt%2F2.png?alt=media&#x26;token=8e03e201-dcae-43ec-a824-5bc5b2bda76a" alt=""><figcaption></figcaption></figure>

**If you’re a free user**, create your Mailtrap API key (or copy it if you already have one) and paste it in the following bar.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FiNNS2W07UTWoXpYR6m7K%2Ffree.png?alt=media&#x26;token=8c30da2a-a78b-4522-a0a1-4ea91951936f" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
**Free account limitations**:

* Due to the rate limits on the free plan, if an email has multiple recipients (including CC and BCC), only the first one will receive it. Additionally, the free plan is limited to 50 testing emails per month.
* If you plan to upgrade later, we recommend following the Paid users flow in the next section, so the add-on will be added to your account and you'll be charged for it correctly when upgrading.
  {% endhint %}

**If you’re a paid user** or **don’t have an account yet**, follow the follow the **Click here** link since the add-on is not added automatically and you need to create a Mailtrap API token.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FpTO63Hvenw09KgRXuoVB%2F3.png?alt=media&#x26;token=3c044bce-0fc0-4113-8178-cf8cb9f5955c" alt=""><figcaption></figcaption></figure>

You will also be redirected to the Mailtrap API Token page, where you’ll see instructions to contact customer support.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FUPcOazJgs1Iq42hxFfSS%2F5.jpg?alt=media&#x26;token=d4ff840f-6df0-4f62-a4f6-1e62030e58ba" alt=""><figcaption></figcaption></figure>

Once the support team enables the add-on, the charge will be applied automatically (prorated), and you can start using it.

## 3) Enabling the Sandbox mode

**Before we start**: The Mailtrap API token you intend to use for the Salesforce integration with Sandbox should have:

* At least **Viewer** permission for *the whole account*.
* **Admin** permission for *one or multiple sandboxes*.

If your API token doesn’t meet one of these requirements, you won’t be able to activate the add-on.

#### Step 1. Enable Sandbox mode

To enable the Sandbox mode, navigate to **Account Settings** again, and then:

* Paste your API key in the bar, hit **Save**.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FEKz8BYBvlNOvNHAwd2qD%2F6.png?alt=media&#x26;token=4c76e1a1-3ceb-4a6b-932c-9c2407766421" alt=""><figcaption></figcaption></figure>

* Select a sandbox to receive emails
* Activate the sandbox mode

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2F963ZsDELIUkLCPXYrE7x%2F7.jpg?alt=media&#x26;token=7bf49950-6e21-4fa1-8e8d-ad38c3af67aa" alt=""><figcaption></figcaption></figure>

This will open a new window, where you simply have to click the **Turn on** button.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FS7Iyj6Ip0xfdeuk2tNX9%2F8.png?alt=media&#x26;token=74b0f78b-e74a-4785-b6de-3baddd57447d" alt=""><figcaption></figcaption></figure>

#### Step 2. Sending a test email

To verify the integration, go to the **Contacts** page and try to send an email to one of your contacts. For example:

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FHsiOSkVofZ5LbvEXiFlQ%2F9.jpg?alt=media&#x26;token=f3df4c56-3a51-485b-8617-6c0db621eca5" alt=""><figcaption></figcaption></figure>

If you’ve followed everything correctly so far, once you click on **Send**, an email should arrive in your Sandbox, just like so:

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fv8aGfntxnYgqNGJPenOp%2F10.jpg?alt=media&#x26;token=0468e105-71fe-46da-b475-f5425acd23d2" alt=""><figcaption></figcaption></figure>

And that’s it, the integration is complete! 🎉

# Source: https://docs.getint.io/guides/integration-synchronization/jira-salesforce-integration/salesforce-oauth-authentication.md

# Salesforce OAuth Authentication

Starting version 1.78, Salesforce customers must configure OAuth authentication, deprecating our previous connection method. To do this, start by creating the necessary credentials in Salesforce. These credentials will connect your Salesforce instance and Getint, facilitating smooth and efficient data synchronization.

### How to Set Up OAuth Authentication in Salesforce <a href="#how-to-set-up-oauth-authentication-in-salesforce" id="how-to-set-up-oauth-authentication-in-salesforce"></a>

1. Log in to your Salesforce instance, click the **Cog icon** in the top right corner of your screen, and click on **Setup** to open your user settings.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FVQqhPKV4BmH8BgZxNpAt%2Fa6c9112bffc8242333cbcb242573c2f6.png?alt=media&#x26;token=aadf95ad-d071-4117-9a98-20236e2c809f" alt=""><figcaption></figcaption></figure>

1. Go to **Platform Tools** > **Apps** > **External Client Apps** > **External Client App Manager.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FkMTgXBtjiwoA9MNg7DJT%2FExternal%20Client%20App%20Manager.png?alt=media&#x26;token=7b09ab4a-e82f-4b5a-badf-c94c4762f3f5" alt=""><figcaption></figcaption></figure>

1. Click **New External Client App.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FOyZLjcBeLP9SWNcfGs80%2FNew%20External%20Client%20App.png?alt=media&#x26;token=520c5714-b60e-4119-b23d-eb99bc0d54bc" alt=""><figcaption></figcaption></figure>

1. Provide a **custom name**, **your email**, and the **API name.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FsDLojbocuKUMO6OZqijl%2FExternal%20Client%20App%20Manager%20Setup.png?alt=media&#x26;token=dfb9525c-882e-4338-a10c-d61d30fb1b47" alt=""><figcaption></figcaption></figure>

1. **Enable OAuth**:
   * Scroll down and enable **OAuth.**
   * Provide the **Callback URL:** `https://login.salesforce.com/services/oauth2/callback`.
   * Select the **OAuth Scope:** The only one required is *Manage user data via APIs (API).*

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FI85U9OjfcVAAGOfI0UuB%2FEnabling%20API%20Settings.png?alt=media&#x26;token=5590ba5b-5581-4549-b621-aa963d9bd84a" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Salesforce requires the Callback URL to use HTTPS for security purposes.
{% endhint %}

1. Scroll down to the section **Flow Enablement** and enable **Client Credentials Flow**. Then, disable the rest of the options in the **Security** section.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FvUPHXsxVYX2EH2QYmurf%2FEnable%20Client%20Credentials%20Flow.png?alt=media&#x26;token=b072a14a-a81f-4860-a67b-08cbb7e4b101" alt=""><figcaption></figcaption></figure>

1. **Create the External Client App**:
   * Click **Create** at the bottom of the screen.
   * After creation, navigate back to edit settings. The new Client should’ve been created.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FlGZxon9zRTWIwfwuITzH%2FNew%20client%20created%20(1).png?alt=media&#x26;token=056f78bd-ce9c-42bd-9d76-e57ebff3a17d" alt=""><figcaption></figcaption></figure>

1. **Edit Settings for the new Client**:
   * Click **Edit**, and display the **OAuth Policies**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FIqvo3Na3RMQHFpEkZJC8%2FNew%20client%20created.png?alt=media&#x26;token=4712917e-5b34-437b-bb79-cca997dcf1c5" alt=""><figcaption></figcaption></figure>

1. Enable **Client Credentials Flow** and provide the username found under **Personal Information** in your profile. Then, click **Save** to submit your changes.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fb03ppB2fZCtf9huCVhnN%2FOAuth%20Flows%20and%20External%20Client%20app%20Enhancements.png?alt=media&#x26;token=b8b2e41f-ae3e-4e14-b85b-eb193b328fb3" alt=""><figcaption></figcaption></figure>

1. **Generate** `client_id` **and** `client_secret`**:**
    * Switch from the **Policies** tab to the **Settings** tab.
    * Click **Consumer Key and Secret**.
    * It will redirect you to the verification screen.
    * Copy the **Consumer Key (**`client_id`**)** and **Consumer Secret (**`client_secret`**)**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FEuJc4jgls9nAO4wUFyOx%2Fgenerating%20ID%20and%20Secret.png?alt=media&#x26;token=397cd405-475b-4889-8e12-4d9bc0e4cc4e" alt=""><figcaption></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FAkuqHtW9dPOxOhuSXSy6%2FClient%20ID%20and%20Secret.png?alt=media&#x26;token=6ed14864-b0fe-4373-8319-b1a751b15c89" alt=""><figcaption><p>With these credentials, you can create a connection with Salesforce in Getint.</p></figcaption></figure>

1. **Create a Salesforce Connection in Getint**:
    * Select **Salesforce** and click **Create a Connection.**
    * Enter your **Salesforce Instance URL** in the URL field and click **Next.**
    * Name the connection and provide the **client\_id** and **client\_secret.**
    * Add and select the connection to finalize the process.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FMqy14CoUOm09U74YGxOk%2FCreating%20a%20connection%20with%20Salesforce.png?alt=media&#x26;token=55e9c9d8-4a81-417e-a856-65a80f555f82" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Ensure to use the correct URLs to connect to your instance:

* <https://YOUR\\_INSTANCE\\_NAME.develop.lightning.force.com>
* <https://YOUR\\_INSTANCE\\_NAME.develop.my.salesforce.com>
  {% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FU4wZvYTDfP4G94OnTsEe%2FGetint%20Banner%20-%20Schedule%20a%20Demo.jpg?alt=media&#x26;token=09b1ea50-e0e3-47c0-bdc3-97ad8c38ef6e" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues to build your integration? Schedule a free consultation with our Integration Experts now!</a><br></p></figcaption></figure>

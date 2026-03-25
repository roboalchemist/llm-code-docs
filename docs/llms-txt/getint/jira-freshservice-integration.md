# Source: https://docs.getint.io/guides/integration-synchronization/jira-freshservice-integration.md

# Jira Freshservice integration

Integrating Jira with Freshservice via the Getint platform transforms how organizations handle project management and customer service in today's interconnected business environment. This essential link creates a streamlined interface that aligns project tracking with IT service management, significantly enhancing operational efficiency and team communication. Our guide offers a clear, straightforward setup process, allowing companies of all sizes to boost collaboration and elevate their service delivery capabilities. Harness the power of the Jira-Freshservice integration with Getint, and move towards a more efficient and effective framework for managing projects and support services.

### **Optimize Your Team's Productivity with Getint 's Jira-Freshservice Integration**

#### &#x20;**0. Access the** [**Getint**](http://getint.io/) **App in Jira:**

* Navigate to Jira, go to "Apps," and select "Jira - Freshdesk integration"

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F5hTfLvMtTE0UKWCw62oP%2Fimage-20240404-113459.png?alt=media&#x26;token=d8240af9-c9fe-4153-8dd7-568e84e732ef" alt=""><figcaption></figcaption></figure>

* Choose "Continuous Sync" or "Migration" based on your integration needs.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F2Z9X8IKZDi7VCj5f83w2%2Fimage-20240109-123756.png?alt=media&#x26;token=db32b39b-c73a-460c-ab4f-7fa0f0ce4838" alt=""><figcaption></figcaption></figure>

#### **1. Token Generation for Jira Cloud:** <a href="#id-1.-token-generation-for-jira-cloud" id="id-1.-token-generation-for-jira-cloud"></a>

* Visit your Atlassian Account Settings and go to the Security section.
* Generate an API token in the API Token section. This token will authenticate your Jira Cloud.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FCYziHUpTlaIl4TtquGld%2FUntitled%20design-20240514-103351.jpg?alt=media&#x26;token=95575920-8c25-40c1-8696-91e6d6d7ec1d" alt=""><figcaption></figcaption></figure>

#### **2. Establish a** **Connection with Jira:** <a href="#id-2.-establish-a-connection-with-jira" id="id-2.-establish-a-connection-with-jira"></a>

* Ensure you're logged in as a user with the correct permissions
* Click "Select App" and choose Jira.
* Select "Create New" to connect with your Jira instance.
* Name your connection, and add the URL of your Jira instance (without "/" at the end).
* Provide the login credentials.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FuXZjNY9ijf1XiVx7eb5X%2FScreenshot%202024-05-14%20074340.png?alt=media&#x26;token=fba8cf20-246f-4005-ad74-c6325af579ed" alt=""><figcaption></figcaption></figure>

#### **3. Choose the Jira Project:** <a href="#id-3.-choose-the-jira-project" id="id-3.-choose-the-jira-project"></a>

* With a successful connection, a dropdown menu will appear.
* Select the Jira project you want to integrate.&#x20;

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F8nH8zo9lx0ZgaMBmg3Sj%2FScreenshot%20from%20May%2014%2C%202024%2C%207_39%20AM.png?alt=media&#x26;token=744ff639-2203-48ee-97fd-4a8d3c184784" alt=""><figcaption></figcaption></figure>

#### **4. Connect to Freshservice:** <a href="#id-4.-connect-to-freshservice" id="id-4.-connect-to-freshservice"></a>

* Log in to your Freshservice account, click on your profile picture in the top right corner, and select “profile settings”
* On the new page, on the right, click on 'Your API Key' and select the check button to access the API key:
* Complete the captcha verification when prompted, and copy the API Key.

{% hint style="info" %}
You can reset the API Key to stop an app from connecting to your helpdesk if you need to. Remember that doing so will also disconnect other apps that use the same key.
{% endhint %}

#### **5. Configure** [**Getint**](http://getint.io/) **for Freshservice:**

* Open the Getint app and select "Freshservice" as the connection app.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FXOuBNoTC3SED6ffBqywU%2FUntitled%20design%20(2).jpg?alt=media&#x26;token=a29f4c8f-6418-4fe1-ae6c-08bdb2ae332c" alt=""><figcaption></figcaption></figure>

* Enter your Freshservice instance URL and click "Next".
* Name the connection and provide your login credentials, using the token captured as the password.
* Choose an existing connection or create a new one and select “Connect”

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FLc8njeCyUxaXK8vPm7pD%2FScreenshot%202024-05-14%20080419.png?alt=media&#x26;token=87b8b6a6-0902-4701-98aa-afd666baf229" alt=""><figcaption></figcaption></figure>

#### **6. Map Types:**

**Quick Build:**

* Consider using the "Quick Build" beta feature for automated type and field mapping. Quick Build automatically performs the mappings based on the most common configurations used by our customers, making it an ideal initial setup for a Minimum Viable Product (MVP). This feature simplifies the setup process by pre-configuring types, fields, and values, allowing you to quickly get started with a functional integration. Once the initial setup is complete, you can review and adjust the mappings to better suit your specific needs and requirements.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FaCwU8IXeUFL9kZSLlkbr%2Fe9281c80-3b60-4eda-91be-a0b476809f2a.jfif?alt=media&#x26;token=e851f182-5358-4199-b56f-aa85a3e552fd" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Quick build is currently in the beta stage, if you have feedback or questions about it, please get in touch with our support at <support@geint.io>
{% endhint %}

**Manual Setup:**

* Select to synchronize Jira issue types such as Task, Bug, Epic, and Story with their Freshservice counterparts.
* Define which fields should be integrated or synchronized during this process.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Ffzfu5EqZaYcKji8MGPxG%2Fimage-20240514-114435.png?alt=media&#x26;token=a3f569bc-51be-418f-a8f9-f2303693300e" alt=""><figcaption></figcaption></figure>

#### **7. Field Mapping:**

Proper field mapping ensures data integrity across both platforms. Below are essential fields that require mapping:

* For the Freshservice connection to work, it is necessary to map some key fields:

1. **Reporter/Requester Mapping**:
   * Link the "Reporter" field in Jira to the "Requester" field in Freshservice.
   * Ensure that requesters on both platforms are mapped to allow Getint to match them appropriately.
     * In case a fixed value, like an email, is supposed to be defined for this field, the configuration can be done like this:
2. **Status Field**:
   * Freshservice mandates status mapping for the integration to function. A default value needs to be set for the ticket creation only, pointing towards the Freshservice side, avoiding this option being picked up again when the issues are updated:
3. **Priority Field**:
   * Mapping the priority field is necessary for the integration's operation within Freshservice.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FIIVQQjgTlkTjuDK2zcIV%2FUntitled%20design%20(4).jpg?alt=media&#x26;token=e02a456e-c15d-4db2-8056-25000412b613" alt=""><figcaption></figcaption></figure>

* After all fields and types have been configured, give your integration a distinctive name and save the settings.
* Consider using the "Quick Build" beta feature for automated type and field mapping, which can streamline the setup process.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FoDwgJ7sfZloIauZJeYdg%2FUntitled%20design%20(3).jpg?alt=media&#x26;token=c3df1527-88d6-4073-b658-ebe64687f054" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Quick build is currently in the beta stage, if you have feedback or questions about it, please get in touch with our support at <support@geint.io>
{% endhint %}

#### **8. Filtering:** <a href="#id-8.-filtering" id="id-8.-filtering"></a>

It is possible to filter the synchronization to have them customized for your needs and requirements.

**UI Filtering Option:**

* Click on the filtering icon near the app icon in your integration. This will apply to that side of the integration.
* Select if the filtering applies to All, New, and Synced items.
* Note that if the option “New items” is selected, the filtering will apply only to the new items, and the already synced items will continue to sync and update. If the option “Synced items” is selected, only the already synced items will be updated based on that filter.
* Choose the options and add the value for the filter. It is possible to filter more than one option for each field.
* Select Apply once you have created the filters and Save the integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FKfCUK4qqsEhjMJiytxo9%2FUntitled%20design%20(5).jpg?alt=media&#x26;token=f8cbedab-ae09-4acf-a420-3e784afb86d2" alt=""><figcaption></figcaption></figure>

**JQL Filtering:**

* Select the app that will receive the filter.
* Under the field Custom JQL, it is possible to provide a JQL, which will be the filter for your sync and appended to the one generated when searching for issues in Jira (e.g., status in ('In Progress')).
* Save the integration.

#### &#x20;9. Duplicate Setup and Select Different Projects: <a href="#id-9.-duplicate-setup-and-select-different-projects" id="id-9.-duplicate-setup-and-select-different-projects"></a>

* Go to Workflows.
* Click the 3 dots on the right side and select "duplicate."
* A side panel will appear. Select a new name for the integration (by default, the integration will be called “copy of” if the same projects are established).
* On the dropdown menu, select the projects you would like to integrate.
* For each side, select Connect. Then Duplicate.
* Save the new integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FI9E62kiAff0YYQim4X1H%2FUntitled%20design%20(6).jpg?alt=media&#x26;token=df6dbac9-bbde-4879-a952-53cc26c3e3f6" alt=""><figcaption></figcaption></figure>

Leverage the Jira-Freshservice integration by Getint to optimize your customer service processes. For further assistance or feedback, contact <support@getint.io>

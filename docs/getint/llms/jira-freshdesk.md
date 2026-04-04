# Source: https://docs.getint.io/guides/integration-synchronization/jira-freshdesk.md

# Jira Freshdesk integration

In the ever-evolving landscape of project management and customer support, the seamless integration between Jira and Freshdesk stands out as a game-changer. Facilitated by Getint, this powerful connection bridges the divide between tracking project milestones and delivering exceptional customer service. By enabling a dynamic flow of information between Jira and Freshdesk, businesses can now manage their projects and customer queries from a single, unified interface. This guide simplifies the setup process and unlocks a world of efficiency and collaboration for teams of all sizes. Embrace the future of work with the Jira-Freshdesk integration and transform your project management experience.

**Optimize Your Team's Productivity with Getint 's Jira-Freshdesk Integration**

### &#x20;**Access the Getint App in Jira**

* Navigate to Jira, go to "Apps," and select "Jira - Freshdesk integration"

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FpYJVr120PJGxzgWk14Qh%2Fimage.png?alt=media&#x26;token=5cf2440a-aa43-4fe4-b8dd-2d70830591b1" alt=""><figcaption></figcaption></figure>

* Choose "Continuous Sync" or "Migration" based on your integration needs.<br>

  <figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fi2otPII3wowoLtKOuxdp%2Fimage.png?alt=media&#x26;token=d26f2713-7900-4b4e-bdeb-dadcdcfb383c" alt=""><figcaption></figcaption></figure>

### **Establish a** **Connection with Jira** <a href="#id-2.-establish-a-connection-with-jira" id="id-2.-establish-a-connection-with-jira"></a>

* Ensure you're logged in as a user with the correct permissions
* Click "Select App" and choose Jira.
  * **Token Generation for Jira Cloud:**
    * Visit your Atlassian Account Settings and go to the Security section.
    * Generate an API token in the API Token section. This token will authenticate your Jira Cloud.

{% embed url="<https://youtu.be/XKt7uOtFngk>" %}

* Select "Create New" to connect with your Jira instance.
* Name your connection, and add the URL of your Jira instance (without "/" at the end).
* Provide the login credentials.

{% embed url="<https://youtu.be/FiMSX3J4v2Q>" %}

#### **Choose the Jira Project** <a href="#id-3.-choose-the-jira-project" id="id-3.-choose-the-jira-project"></a>

* With a successful connection, a dropdown menu will appear.
* Select the Jira project you want to integrate.&#x20;

{% embed url="<https://youtu.be/z-fG4bEyl_o>" %}

### **Connect to Freshdesk** <a href="#id-4.-connect-to-freshdesk" id="id-4.-connect-to-freshdesk"></a>

* Log in to your Freshdesk account, click on your profile picture in the top right corner, and select 'Profile Settings.'
* In the sidebar on the right, click on the 'View API key' button to access the API key.
* Complete the captcha verification when prompted.

{% embed url="<https://youtu.be/odlS2evq4p4>" %}

{% hint style="info" %}
You can reset the API Key to stop an app from connecting to your helpdesk if you need to. Keep in mind that doing so will also disconnect other apps that use the same key.
{% endhint %}

**Configure** [**Getint**](http://getint.io/) **for Freshdesk**

* Open the Getint app and select "Freshdesk" as the connection app.
* Enter your Freshdesk instance URL and click "Next".
* Name the connection and provide your login credentials, using the token captured as the password.
* Choose an existing connection or create a new one and select “Connect”

### **Map Types**

* Synchronize Jira issue types such as Task, Bug, Epic, and Story with their Freshdesk counterparts.
* Clearly define which fields should be integrated or synchronized during this process.

{% embed url="<https://youtu.be/Oaii88uCfyI>" %}

### **Field Mapping**

Proper field mapping ensures data integrity across both platforms. Below are essential fields that require mapping:

* For the Freshdesk connection to work, it is necessary to map some key fields:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FYR4VqjuPHUzjQ9yXkIAn%2Fimage.png?alt=media&#x26;token=3e180257-e52d-4208-8c62-6bf1428330fd" alt=""><figcaption></figcaption></figure>

**Reporter/Requester Mapping**

* Link the 'Reporter' field in Jira to the 'Requester' field in Freshdesk.
* Ensure that requesters on both platforms are mapped to allow Getint to match them appropriately.
  * In case a fixed value, like an email, is supposed to be defined for this field, the configuration can be done like this:

{% embed url="<https://youtu.be/LJHIho1pQVo>" %}

#### **Status Field**

* Freshdesk mandates status mapping for the integration to function. A default value needs to be set for the ticket creation only, pointing towards the Freshdesk side, avoiding this option being picked up again when the issues are updated:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FYN6dmkFAadsRCgoCR7jY%2Fimage.png?alt=media&#x26;token=f38a35fb-8c6a-4b46-b7cd-3edcb1bff8d7" alt=""><figcaption></figcaption></figure>

**Priority Field**

* Mapping the priority field is a necessity for the integration's operation within Freshdesk.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FTKNpA81kI1TNoXcBHOrH%2Fimage.png?alt=media&#x26;token=c206ed82-c2b0-403b-a15a-42a4cfe3d60b" alt=""><figcaption></figcaption></figure>

* After all fields and types have been configured, give your integration a distinctive name and save the settings.
* Consider using the "Quick Build" beta feature for automated type and field mapping, which can streamline the setup process.

{% embed url="<https://youtu.be/1BF4mOmzbzU>" %}

{% hint style="info" %}
Quick build is currently in the beta stage, if you have feedback or questions about it, please get in touch with our support at <support@geint.io>
{% endhint %}

### **Filtering** <a href="#id-8.-filtering" id="id-8.-filtering"></a>

It is possible to filter the synchronization to have them customized for your needs and requirements.

#### **UI Filtering Option**

* Click on the filtering icon near the app icon in your integration. This will apply to that side of the integration.
* Select if the filtering applies to All, New, and Synced items.
* Note that if the option “*New items”* is selected, the filtering will apply only to the new items, and the already synced items will continue to sync and update. If the option “*Synced items”* is selected, only the already synced items will be updated based on that filter.
* Choose the options and add the value for the filter. It is possible to filter more than one option for each field.
* Select Apply once you created the filters and Save the integration.

{% embed url="<https://youtu.be/qDj5KmG0w7U>" %}

#### **JQL Filtering**

* Select the app that will receive the filter.
* Under the field Custom JQL, it is possible to provide a JQL, which will be the filter for your sync and appended to the one generated when searching for issues in Jira (e.g., status in ('In Progress')).
* Save the integration.

{% embed url="<https://youtu.be/oNjFSqRRUSA>" %}

#### Duplicate Setup and Select Different Projects <a href="#id-9.-duplicate-setup-and-select-different-projects" id="id-9.-duplicate-setup-and-select-different-projects"></a>

* Go to Workflows.
* Click the 3 dots on the right side and select "duplicate."
* A side panel will appear. Select a new name for the integration (by default, the integration will be called “copy of” if the same projects are established).
* On the dropdown menu, select the projects you would like to integrate.
* For each side, select Connect. Then Duplicate.
* Save the new integration.&#x20;

{% embed url="<https://youtu.be/6su7bE9VZyc>" %}

Leverage the Jira-Freshdesk integration by Getint to optimize your project management and customer service processes. For further assistance or feedback, contact <support@getint.io>.

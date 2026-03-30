# Source: https://docs.getint.io/guides/integration-synchronization/jira-zendesk-integration.md

# Jira Zendesk integration

In the ever-evolving world of project management and customer support, the integration between Jira and Zendesk facilitated by Getint is a true game-changer. This powerful connection bridges the gap between tracking project milestones and delivering exceptional customer service. By enabling a seamless flow of information between Jira and Zendesk, businesses can now manage projects and customer queries from a single, unified interface. This guide not only simplifies the setup process but also unlocks a world of efficiency and collaboration for teams of all sizes. Embrace the future of work with the Jira-Zendesk integration and revolutionize your project management experience.

**Optimize Your Team's Productivity with Getint 's Jira-Zendesk Integration**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F7QX86ZcIqIPnKN2syttO%2Fimage.png?alt=media&#x26;token=c9892a32-846c-4c36-9249-382ab42714de" alt=""><figcaption></figcaption></figure>

### **Access the** [**Getint**](http://getint.io/) **App in Jira:** <a href="#id-0.-access-the-getint-app-in-jira" id="id-0.-access-the-getint-app-in-jira"></a>

Navigate to Jira, go to "Apps," and select "Jira Zendesk integration"

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FDQZhsLc1XhhWHNIn4Z45%2Fimage.png?alt=media&#x26;token=567b072d-df61-43e6-afe9-a29e840a7a8c" alt=""><figcaption></figcaption></figure>

Choose between "Continuous Sync" or "Migration" based on your integration needs.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FwEh44mzYpKVSF4HCunjX%2Fimage.png?alt=media&#x26;token=79f92da2-4a75-448e-a898-1b6b6189879d" alt=""><figcaption></figcaption></figure>

#### **1. Token Generation for Jira Cloud:** <a href="#id-1.-token-generation-for-jira-cloud" id="id-1.-token-generation-for-jira-cloud"></a>

* Visit your Atlassian Account Settings and go to the Security section.
* Generate an API token in the API Token section. This token will authenticate your Jira Cloud.

{% embed url="<https://youtu.be/ERTZMVmWcCs>" %}

### **Establish a** **Connection with Jira:** <a href="#id-2.-establish-a-connection-with-jira" id="id-2.-establish-a-connection-with-jira"></a>

* Ensure you're logged in as a user with the correct permissions
* Click "Select App" and choose Jira.
* Select "Create New" to connect with your Jira instance.
* Name your connection, and add the URL of your Jira instance (without "/" at the end).
* Provide the login credentials.

#### **Choose the Jira Project:** <a href="#id-3.-choose-the-jira-project" id="id-3.-choose-the-jira-project"></a>

* With a successful connection, a dropdown menu will appear.
* Select the Jira project you want to integrate.&#x20;

{% embed url="<https://youtu.be/FiMSX3J4v2Q>" %}

### **Connect to Zendesk:** <a href="#id-4.-connect-to-zendesk" id="id-4.-connect-to-zendesk"></a>

* Access your Zendesk instance with Admin credentials. Select the four squares icon and choose ‘Admin Center’.
* Log in to Zendesk as an Admin. Select the four squares icon and go to ‘Admin Center' then navigate to ‘Apps and integrations’ -> 'Zendesk API'.
* Enable ‘Token Access’ and create an API token for the integration.

{% embed url="<https://youtu.be/Unnp9UrFCAw>" %}

#### **Configure** [**Getint**](http://getint.io/) **for Zendesk:**

* Open the Getint app and select "Zendesk" as the connection app.
* Enter your Zendesk instance URL and click "Next".
* Name the connection and provide your login credentials, using the token captured as the password.
* Choose an existing connection or create a new one.
* On the next page, select your organization and click "Connect".

{% embed url="<https://youtu.be/Aje-HxH4bEA>" %}

### &#x20;**Map Types:**

* Link Jira types (Task, Bug, Epic, Story) to synchronize in Zendesk.
* Specify the fields for integration or synchronization.

### &#x20;**Field Mapping:**

* Map key fields such as title/summary and description
* After configuring, name and save your integration settings.

{% embed url="<https://youtu.be/5GiMTj6khP4>" %}

Try the beta feature "auto-build" for automatic field mapping.

{% embed url="<https://youtu.be/w-xDO-IsMew>" %}

{% hint style="info" %}
Auto-build is currently in beta stage, if you have a feedback or have questions about it, please contact our support at <support@geint.io>
{% endhint %}

### **Filtering:** <a href="#id-8.-filtering" id="id-8.-filtering"></a>

It is possible to filter the synchronization to have them customized for your needs and requirements.

**UI Filtering Option:**

* Click on the filtering icon near the app icon in your integration. This will apply to that side of the integration.
* Select if the filtering applies to All, New, and Synced items.
* Note that if the option “*New items”* is selected, the filtering will apply only to the new items, and the already synced items will continue to sync and update. If the option “*Synced items”* is selected, only the already synced items will be updated based on that filter.
* Choose the options and add the value for the filter. It is possible to filter more than one option for each field.
* Select Apply once you created the filters and Save the integration.

{% embed url="<https://youtu.be/yhkjBnRR8x4>" %}

**JQL Filtering:**

* Select the app that will receive the filter.
* Under the field Custom JQL, it is possible to provide a JQL, which will be the filter for your sync and appended to the one generated when searching for issues in Jira (e.g., status in ('In Progress')).
* Save the integration.&#x20;

{% embed url="<https://youtu.be/jXKPNzunoPk>" %}

**Duplicate Setup and Select Different Projects:**

* Go to Workflows.
* Click the 3 dots on the right side and select "duplicate."
* A side panel will appear. Select a new name for the integration (by default, the integration will be called “copy of” if the same projects are established).
* On the dropdown menu, select the projects you would like to integrate.
* For each side, select Connect. Then Duplicate.
* Save the new integration.

{% embed url="<https://youtu.be/lHW9IbvrFtQ>" %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FiwAmwiuWcOM1s8joTmD9%2Fimage.png?alt=media&#x26;token=115af02b-d2a7-45fa-9590-2824b5b93fb7" alt=""><figcaption></figcaption></figure>

Leverage the Jira-Zendesk integration by Getint to optimize your project management and customer service processes. For further assistance or feedback, contact [getint.io/help-center](https://getint.io/help-center).

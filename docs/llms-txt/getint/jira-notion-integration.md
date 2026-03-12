# Source: https://docs.getint.io/guides/integration-synchronization/jira-notion-integration.md

# Jira Notion integration

Getint's Jira-Notion integration enables users to sync project data between the two platforms. Once set up, users can view and manage Jira tickets, tasks, bugs, and epics directly within Notion, providing a unified workspace for project tracking and team collaboration. Initially, the integration supports syncing only the title and description fields between Jira and Notion items, with plans to map additional fields like assignees, statuses, labels, and custom fields in future updates.

As a relatively new integration, full feature parity between Jira and Notion may not yet be available. However, Getint is committed to ongoing development and values user feedback to prioritize and expand integration capabilities. If certain functionalities are missing or challenges arise during setup, users are encouraged to reach out. The guide below offers a 3-minute setup process for a functional MVP integration, with Getint's dedicated team available for personalized onboarding, expert support, custom script assistance for complex scenarios, and bespoke development solutions.

{% embed url="<https://youtu.be/ZNZPsiZNzps>" %}

#### **1. Access the** [**Getint**](http://getint.io/) **App in Jira:** <a href="#id-0.-access-the-getint-app-in-jira" id="id-0.-access-the-getint-app-in-jira"></a>

* Navigate to Jira, go to "Apps," and select "the Getint app."

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FFPDFjQAZcRht2DpWeCsE%2FNotion%20integration%20app%20for%20Jira.png?alt=media&#x26;token=f867ab55-ee7e-4e07-b8f3-44f144b6fa53" alt=""><figcaption></figcaption></figure>

* Select "Create Integration" then "Continuous Sync" or "Migration" based on your requirements.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FxPQuHRml69V0fkrvIo4P%2FSelecting%20Continuos%20Sync%20or%20Migration.png?alt=media&#x26;token=516a4fc0-d24a-4642-9699-ce6f852b9dd6" alt=""><figcaption></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fa1Z99b8khISGbcsrb4qr%2FGetint%20White%20Banner%20-%20Schedule%20a%20Demo.jpg?alt=media&#x26;token=526d7a99-8a15-4fda-b829-7263c748214b" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues building your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>

#### **2. Token Generation for Jira Cloud:** <a href="#id-1.-token-generation-for-jira-cloud" id="id-1.-token-generation-for-jira-cloud"></a>

* Visit Atlassian Account Settings.

{% embed url="<https://www.loom.com/share/21ed10cc0c7c4b34893f04497ca04ddd?sid=773e4e8d-98ee-4820-8aa9-2e561500474f>" %}

* Go to Security
* Navigate to the API Token section and generate a token. This token serves as the password for Jira Cloud.

{% embed url="<https://www.loom.com/share/f8246071639a484193fb5ee247e07a9b?sid=a5718d6a-1033-4cf7-9df2-002998207c36>" %}

#### **3. Establish a** **Connection with Jira:**  <a href="#id-2.-establish-a-connection-with-jira" id="id-2.-establish-a-connection-with-jira"></a>

* Ensure you're logged in as a user with the correct permissions
* Click "Select App" and choose Jira.
* Select "Create New" to establish a new connection with your Jira instance.
* Name your connection, and add the URL of your Jira instance (without "/" at the end).
* Provide the login credentials.

{% embed url="<https://youtu.be/xOg076frYw4>" %}

**4. Choose the Jira Project:**

* With a successful connection, a dropdown menu will appear.
* Select the Jira project you want to integrate.

{% embed url="<https://youtu.be/aiknGfYdbD8>" %}

**5. Connect to Notion:**

* In the Notion app, click on the three dots in the top right corner.
* Select "Add a Connection," then navigate to "Manage Connections" and choose "Develop or Manage integrations."

{% embed url="<https://youtu.be/IXr52732ppM>" %}

* Select "New Integration."
* Provide a name for your integration, grant necessary permissions, and copy the API token.

{% embed url="<https://youtu.be/yliJs_muuJQ>" %}

* Close the window, return to the Notion dashboard, and click on the three dots again.
* Scroll down to add a connection and select the name of the connection that you have already created.

{% embed url="<https://youtu.be/XL5xE3xe0Ps>" %}

{% hint style="info" %}
It might be necessary to refresh your browser to see the new connection in the list.
{% endhint %}

#### **6. Configure** [**Getint**](http://getint.io/) **for Notion:** <a href="#id-5.-configure-getint-for-notion" id="id-5.-configure-getint-for-notion"></a>

* In the [Getint](http://getint.io/) app, choose "Notion" as the connection app.
* Select "Create a new connection," name it, and provide the API Token.
* Select the connection you want to integrate.
* Choose the Notion database to synchronize.

{% embed url="<https://youtu.be/XKd0gczYqNU>" %}

#### **7. Map Types:** <a href="#id-6.-map-types" id="id-6.-map-types"></a>

* Link Jira types (Task, Bug, Epic, Story) to synchronize in Notion.
* Specify the fields for integration or synchronization.

{% embed url="<https://youtu.be/Dn5ZclInIcY>" %}

{% hint style="info" %}
Please note that the current version of Getint for Notion only supports the "Title" and "Description" fields. For syncing other fields like assignees, statuses, labels, or custom fields, please contact us directly at <https://getint.io/help-center>.
{% endhint %}

#### **8. Field Mapping:** <a href="#id-7.-field-mapping" id="id-7.-field-mapping"></a>

* Map key fields such as title/summary and description
* After configuring, name and save your integration settings.

{% embed url="<https://youtu.be/BMJJtQk3YW0>" %}

{% hint style="warning" %}
The "Description" field in Notion supports a maximum of 2000 characters. To avoid sync errors and blank description fields when transferring text from Jira to Notion, ensure your content does not exceed this limit. Keeping descriptions concise and within the character count helps maintain data integrity and prevents synchronization issues.
{% endhint %}

#### **9. Filtering:** <a href="#id-8.-filtering" id="id-8.-filtering"></a>

It is possible to filter the synchronization to have them customized for your needs and requirements.

**UI Filtering Option:**&#x20;

* Click on the filtering icon near the app icon in your integration. This will apply to that side of the integration.
* Select if the filtering will apply to All items, New items, and Synced items.
* Note that if the option "*New items"* is selected, the filtering will apply only to the new items, and the already synced items will continue to sync and update. If the option "*Synced items"* is selected, only the already synced items will be updated based on that filter.
* Choose the options and add the value for the filter. It is possible to filter more than one option for each field.
* Select Apply once you created the filters and Save the integration.

{% embed url="<https://youtu.be/Hp7q8IQwFng>" %}

**JQL Filtering:**&#x20;

* Select the app that will receive the filter.
* Under the field Custom JQL, it is possible to provide a JQL, which will be the filter for your sync and appended to the one generated when searching for issues in Jira (e.g., status in ('In Progress')).
* Save the integration.

{% embed url="<https://youtu.be/1uy9T0hKl7o>" %}

#### **10. Duplicate Setup and Select Different Projects:** <a href="#id-9.-duplicate-setup-and-select-different-projects" id="id-9.-duplicate-setup-and-select-different-projects"></a>

* Go to Workflows.
* Click on the 3 dots on the right side and select "duplicate."
* A side panel will appear. Select a new name for the integration (by default, the integration will be called “copy of” if the same projects are established).
* On the dropdown menu, select the projects that you would like to integrate.
* For each side, select Connect. Then Duplicate.
* Save the new integration.

{% embed url="<https://youtu.be/ut7MxxAQ8Vk>" %}

{% hint style="info" %}
If you require further assistance with your integration or if you have any questions about Getint, feel free to open a ticket at our [Support Center](https://getint.io/help-center) or [Schedule a Demo](https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team).
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F4q6IDb8EZjgAx52jlppF%2FGetint%20Banner%20-%20Schedule%20a%20Demo.jpg?alt=media&#x26;token=faae9475-d471-4886-adbe-386a97632e80" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

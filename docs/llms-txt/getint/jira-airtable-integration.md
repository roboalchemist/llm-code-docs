# Source: https://docs.getint.io/guides/integration-synchronization/jira-airtable-integration.md

# Jira Airtable integration

**Introduction**

The Jira–Airtable integration with Getint provides a practical solution for project and data management. It combines Jira’s structured task tracking with Airtable’s flexible database features, creating a single interface that supports efficiency and collaboration. This guide explains how to set up the integration step by step, helping teams improve productivity, maintain data accuracy, and achieve real‑time synchronization aligned with business needs.

### Step-by-Step Setup Guide <a href="#step-by-step-setup-guide" id="step-by-step-setup-guide"></a>

**1. Launch Getint within Jira**

* Navigate to "Apps" and select "Airtable integration for Jira."

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FKmva55Sdg26TS9rqSHen%2Fimage-20240626-144813.png?alt=media&#x26;token=29d9fba4-4814-44a7-8f82-e91f538f41bb" alt=""><figcaption></figcaption></figure>

**2. Create Integration**

* Click "Continuous Sync" or "Migration."

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FvBdztsn0Y6eU6q8qdVe7%2Fimage-20240619-115231%20(1).png?alt=media&#x26;token=623d4c18-950a-4492-970e-111fe7fb1e5e" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
**Note:** The "Continuous Sync" functionality ensures consistent data integration, which is Getint's standard operation mode. For transferring pre-existing data, consider the "Migration" feature available as a premium option. For more details, contact our support team.
{% endhint %}

**3. Token Generation (Password for Jira Cloud)**

* For Jira Cloud, generate a Jira token. This token will act as your password:
  * Go to Atlassian Account Settings.
  * Navigate to Security and generate an API token, then use this token as the password for Jira integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FVYN4z7XPyRqTKAPOUqFD%2FCreating%20API%20token.png?alt=media&#x26;token=028cb340-303b-49c8-b828-5b9affa50892" alt=""><figcaption></figcaption></figure>

**4. Choose the Apps and Establish Connections**

* Ensure you are logged in as a user with admin rights, click on "Select App" and choose Jira.
* Select "Create New" to establish a new connection with your Jira instance and add the URL of your Jira instance (omit the trailing "/ ").
* Enter the login credentials of the admin user.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FCjhtyzJGdkbyM45qdwgq%2Fimage-20240620-165801%20(1).png?alt=media&#x26;token=31a83bbb-7c3c-402b-8a17-6bbdaa8aa0ad" alt=""><figcaption></figcaption></figure>

**5. Select the Jira Project**

* Once the connection is established, choose the Jira project you want to connect to from the dropdown menu.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FjfVXiWf993wn6D81YD11%2Fimage-20240620-170315%20(1).png?alt=media&#x26;token=dd022d94-7285-449f-9f03-6cc1d1ba9ff0" alt=""><figcaption></figcaption></figure>

**6. Generate Airtable Token**

* Go to Airtable, ensure that you have created the "Last Modified Time" column, then create the Access Token. Follow the steps [here](https://docs.getint.io/guides/quickstart/connection#airtable) for the token with the correct scope.

**7. Connect to Airtable**

* If no connection is established yet, create a new one.
* Use the Airtable token generated as a password. Then select the space and table.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FfQLYQXjlJa46f2QhJmHM%2Fimage-20240628-114059.png?alt=media&#x26;token=6a62e53e-1197-4aab-80e6-8d846156eb39" alt=""><figcaption></figcaption></figure>

**8. Type Mapping**

* Map Jira issue types such as Task, Bug, Epic, and Story to Task in Airtable.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FpaJXNahmmbbZtoXSjoMh%2Fimage-20240628-114750.png?alt=media&#x26;token=bca52421-c3f8-4ab0-981c-cf17d0648273" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
Please note that at the moment, we only support the "Task" issue type for this integration.
{% endhint %}

**9. Field Mapping**

* Designate specific fields for synchronization and map them accordingly.
* If you need fields that are not appearing for your integration, including labels or custom fields, contact us at <https://getint.io/help-center>. We continually improve our product based on user feedback and value your insights.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FEMICceNkxy8Al4Jk3x6C%2Fimage-20240628-114709.png?alt=media&#x26;token=5373b805-4bf2-49bc-84b5-216ad411f509" alt=""><figcaption></figcaption></figure>

**10. Finalize Integration**

* Name your project and click "Create" to finalize the integration setup.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fc5YXwfyo82bT8HNuSwpY%2FUntitled%20design%20(11).jpg?alt=media&#x26;token=97ce5844-4ea5-4ff3-ac33-179b47696cdf" alt=""><figcaption></figcaption></figure>

**11. Filtering:**

It is possible to filter the synchronization to have it customized for your needs and requirements.

**UI Filtering Option:**

* Click on the filtering icon near the app icon in your integration. This will apply to that side of the integration.
* Select if the filtering applies to All, New, and Synced items.
* Note that if the option *"New items"* is selected, the filtering will apply only to the new items, and the already synced items will continue to sync and update. If the option *"Synced items"* is selected, only the already synced items will be updated based on that filter.
* Choose the options and add the value for the filter. It is possible to filter more than one option for each field.
* Select "Apply" once you have created the filters and "Save" the integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FWEpjf30CfNioo4TCHbQj%2Fimage-20240710-095555.png?alt=media&#x26;token=071da8b3-df1f-4ebe-8701-56b926b86e91" alt=""><figcaption></figcaption></figure>

**12. Test the Integration**

To ensure everything is working correctly, create tasks and go to the reporting section to verify that all syncs are functioning as expected. If you encounter any issues, please contact our support team for assistance.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F6q0zqpHCMoqgo7af5Ldm%2Fimage-20240710-095044.png?alt=media&#x26;token=5c5e5f9e-b2d7-4b23-8c7c-88dc6df9bd3f" alt=""><figcaption></figcaption></figure>

Leverage the Jira-Airtable integration by Getint to optimize your project management and data processes. For further assistance or feedback, contact us at our [Help Center](https://getintio.atlassian.net/servicedesk/customer/portals).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

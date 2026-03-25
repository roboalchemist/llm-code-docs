# Source: https://docs.getint.io/guides/integration-synchronization/azure-devops-asana-integration.md

# Azure DevOps Asana integration

Managing projects across multiple platforms can be difficult, especially when teams rely on different tools for tasks and development. The Asana–Azure DevOps integration with Getint connects these systems, enabling real-time synchronization of tasks, statuses, and project data for a unified workflow. Built for simplicity and flexibility, it lets teams collaborate effectively without disrupting existing processes. This guide offers a step-by-step approach to setting up the integration, helping you improve coordination and enhance project management.

***

### Setting Up Your Asana-Azure DevOps Integration: Step-by-Step Guide <a href="#setting-up-your-asana-azure-devops-integration-step-by-step-guide" id="setting-up-your-asana-azure-devops-integration-step-by-step-guide"></a>

#### **1. Access the Getint App:** <a href="#id-0.-access-the-getint-app" id="id-0.-access-the-getint-app"></a>

* Navigate to Getint and sign in.
* Select "Create Integration" then "Continuous Sync" or "Migration" based on your requirements.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FsBEY8rF6KIh9H4ePEd37%2FCreating%20an%20integration.png?alt=media&#x26;token=0fd82721-d3e3-4a0d-b6b1-f8b1414481ec" alt=""><figcaption></figcaption></figure>

#### 2. Connect to Asana <a href="#id-2.-connect-to-asana" id="id-2.-connect-to-asana"></a>

* Select an existing Asana connection, or create a new connection if this is your first time. Follow the guide [here](https://docs.getint.io/guides/quickstart/connection#asana)on how to create the Asana Token.
* Click "Select App" and choose Asana. Choose "Create New" to establish a new connection.
* Name your connection, use the token generated, then select "Add."

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F4wFLjbCda6qQYTOpp1xK%2FCreate%20a%20connection%20with%20Asana.png?alt=media&#x26;token=0161653a-2387-459c-be41-8c837fd35584" alt=""><figcaption></figcaption></figure>

* Once the connection is established, choose the workspace and project you want to connect to from the dropdown menu.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FWtoIFZicT3MwE3Bk8dQ7%2FSelect%20the%20project%20from%20the%20dropdown%20menu.png?alt=media&#x26;token=7e162960-1137-4ad8-9169-92adcb559fd0" alt=""><figcaption></figcaption></figure>

#### 3. Connect to Azure DevOps <a href="#id-3.-connect-to-azure-devops" id="id-3.-connect-to-azure-devops"></a>

* Log in to the Azure DevOps app as an admin. Follow the steps in our "[Connections](https://docs.getint.io/guides/quickstart/connection#azure-devops)" guide to generate the token.
* Select "Azure DevOps" as the connection application, then choose "Create a new connection." Enter the URL for the connection and click "Next."

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FqZSWGuVhqdbgb4Kue9DF%2FConnect%20to%20Azure%20DevOps.png?alt=media&#x26;token=cafcba14-268c-40c6-aaa1-9b9b5d1a5a4d" alt=""><figcaption></figcaption></figure>

* Provide a name for the connection, enter your email, and paste the token generated in the previous steps. Click "Add" to complete.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FozqsQv1CS8Weut4werqF%2FEnter%20your%20credentials.png?alt=media&#x26;token=b032ef5f-24c6-4d89-a45c-dd84d8f44200" alt=""><figcaption></figcaption></figure>

* Once the connection is established, select the Azure DevOps project you want to synchronize from the dropdown menu and click connect.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FnWsJOhHerCbIXw6bK4Cv%2FClick%20connection%20to%20establish%20the%20connection%20with%20Getint.png?alt=media&#x26;token=4f8535e5-7140-4f9a-a676-7539eaf7267a" alt=""><figcaption></figcaption></figure>

#### 4. Configure Type Mapping <a href="#id-4.-configure-type-mapping" id="id-4.-configure-type-mapping"></a>

Consider using the "Quick Build" beta feature for automated type and field mapping, which can streamline the setup process.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FhnOzfFIMpFRMtcAi69N9%2FUse%20quickbuild%20for%20auto%20type%20mapping.png?alt=media&#x26;token=f02113ce-0dce-43a0-8259-cc8ada28fd80" alt=""><figcaption></figcaption></figure>

* Map task types you wish to sync between Asana and Azure DevOps. This could include:
  * Asana *Tasks* → Azure DevOps *User Stories*.
  * Asana *Sub-Tasks* → Azure DevOps *Tasks*.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fb3VsJhsskhriDhp5VWgP%2FAdapting%20your%20type%20mappings.png?alt=media&#x26;token=e83f4f60-425b-4216-bdbf-6559fb46a638" alt=""><figcaption></figcaption></figure>

This flexibility allows you to adapt the integration to your team's workflow needs.

#### 5. Field Mapping <a href="#id-5.-field-mapping" id="id-5.-field-mapping"></a>

Review or manually map the fields you'd like to integrate and sync, such as title, description, assignees, custom fields, and more.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FnQqgbxatRqpOhyQNEx6Y%2FField%20mapping%20Azure%20Asana.png?alt=media&#x26;token=5facdae2-7dcf-4a63-9368-4d1eabfd81c0" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
If you don’t see a field you need, please reach out to our [support team](https://getint.io/help-center) for assistance! We’re constantly working to enhance your experience.
{% endhint %}

#### 6. Name and Finalize the Integration <a href="#id-6.-name-and-finalize-the-integration" id="id-6.-name-and-finalize-the-integration"></a>

Assign a name to your integration and click "Create" to initiate it.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Ft4v0K1IgZMqMGQBoRgF8%2FName%20and%20finalize%20the%20integration.png?alt=media&#x26;token=74a76a26-54a7-4ad7-af77-14f262002ae5" alt=""><figcaption></figcaption></figure>

### Advanced Configuration Options <a href="#advanced-configuration-options" id="advanced-configuration-options"></a>

#### 7. Configure Statuses Sync <a href="#id-7.-configure-statuses-sync" id="id-7.-configure-statuses-sync"></a>

Enable status synchronization to match the progress stages between Asana and Azure DevOps:

* Go to the "Statuses" tab, enable sync, and define mappings:
  * Asana *Done* → Azure DevOps *Closed/Resolved*.
  * Asana *In Progress* → Azure DevOps *Active*, etc.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FKfndRfowQMJSM345ff71%2FStatus%20mapping%20configuration.png?alt=media&#x26;token=97b83f82-abf6-40c6-8540-dd055c05d2c3" alt=""><figcaption></figcaption></figure>

#### 8. Sync Comments and Attachments <a href="#id-8.-sync-comments-and-attachments" id="id-8.-sync-comments-and-attachments"></a>

To synchronize comments and attachments, navigate to the "Comments & Attachments" tab, enable the setting, and configure options to tailor the integration to your team's workflow needs.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FuLjKBnMNA62ONWobHjeH%2FSync%20comments%20%26%20attachments.png?alt=media&#x26;token=d098f689-5336-4b33-bcc7-f4eb06da12a8" alt=""><figcaption></figcaption></figure>

#### 9. Assignee Mapping <a href="#id-9.-assignee-mapping" id="id-9.-assignee-mapping"></a>

Map and match assignees according to your desired configuration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F0tUkdzK43HtjZrgqlBhY%2FMapping%20assignees.png?alt=media&#x26;token=e3752c76-5f26-482f-8432-21ff49022c6e" alt=""><figcaption></figcaption></figure>

#### 10. Filtering: <a href="#id-10.-filtering" id="id-10.-filtering"></a>

It is possible to filter the synchronization to have it customized for your needs and requirements.

**UI Filtering Option:**

* Click on the filtering icon next to the app icon in your integration. This filter will apply to that side of the integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FGgHBfpjoy4NYOV0p2IuZ%2FUI%20filtering%20configuration.png?alt=media&#x26;token=c508c4f1-3d5b-4709-95fb-8bab07075a0a" alt=""><figcaption></figcaption></figure>

* Choose whether the filter applies to *"All," "New,"* or *"Synced"* items:
  * **New items:** The filter will only apply to new items, while already-synced items continue to sync and update.
  * **Synced items**: The filter will apply only to items that have already been synced, updating them based on the filter criteria.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F0JLD17YhpHOtbC86kEnS%2FSetup%20your%20filters.png?alt=media&#x26;token=fedf202d-ca07-4157-a5d6-07de8253ca18" alt=""><figcaption></figcaption></figure>

* Select your options and enter values for the filter. As needed, you can apply multiple filter options for each field. Once your filters are set, click "Apply" and "Save" the integration.

### Need Assistance? <a href="#need-assistance" id="need-assistance"></a>

Leverage the Asana-Azure DevOps integration by Getint to optimize your task management and project workflows. For further assistance or to request support, please visit our [Help Center](https://getint.io/help-center).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

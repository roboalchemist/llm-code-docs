# Source: https://docs.getint.io/guides/integration-synchronization/jira-asana-integration.md

# Jira Asana integration

Integrate Jira with Asana using Getint to enhance workflows with other teams, facilitate effective communication among teams, companies, and customers, or efficiently migrate to Jira while maintaining your previous backlog.

Asana and Jira are vital tools for companies, offering distinct advantages in project management and collaboration. Asana's user-friendly interface and flexible task management complement Jira's robust issue-tracking and development capabilities. Integrating both platforms through Getint streamlines communication, synchronizing tasks and timelines in real time. This synergy enhances productivity, fosters collaboration, and ensures alignment across teams and departments, driving success in today's competitive landscape. With Getint, you can integrate Asana to your Jira Cloud, Jira Data Center, or On-Premise seamlessly and synchronize tasks across your workspace with efficiency.

To set up two-way Jira Asana Integration, follow the video tutorial below:

{% embed url="<https://youtu.be/PBKYO99Enls>" %}

### Prepare your workspaces, and check the fields you would like to integrate to the counterpart

Different projects have different requirements, with this in mind you may like to track and integrate specific information for your project.

Asana has a multitude of custom field types that can be added to your board, make sure to have your board configured beforehand with all the custom fields you would like to integrate so that when creating the integration, you can visualize them for mapping and map them according to their counterpart in Jira.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FaBWn6VQNSrwt54HibJi3%2Fimage.png?alt=media&#x26;token=a011646c-c811-4ec5-b862-bb449ddc7688" alt=""><figcaption><p>Custom field types creation screen from Asana</p></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FH84fVATjoIyUiMBMM3ro%2Fimage.png?alt=media&#x26;token=b5e5fb56-5bf1-4af3-b411-fe7227f7c77c" alt=""><figcaption><p>Custom field types added to an Asana’s board</p></figcaption></figure>

### **Create the integration and add the connections** <a href="#create-the-integration-and-add-the-connections" id="create-the-integration-and-add-the-connections"></a>

**Access the Getint App in Jira.**

1. Here we are going to select the Jira - Asana Integration app for this integration, then create the connection for Jira with Jira’s API token and create the connection for Asana with Asana’s Access token. Remember to give a name to your integration, then create it.

{% embed url="<https://www.loom.com/share/4942cde250484e999d3af6200564275b?sid=7e5e29f6-fc6a-47ef-8fe8-11b2c77ad1e0>" %}

1. Navigate to Jira, go to “Apps”, and select the “Jira - Asana Integration app” (If you still don’t have the trial for this application, please check it at the Atlassian Marketplace on the [Asana Jira integration by Getint \[2-way sync + migration\] | Atlassian Marketplace](https://marketplace.atlassian.com/apps/1223932/asana-jira-integration-by-getint-2-way-sync-migration?hosting=cloud\&tab=overview)\
   ![](https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FMhJiFCNXNmGvxWtcrhYp%2Fimage.png?alt=media\&token=47cda971-646c-4cf9-85e9-e20e88bd69ab)
2. Select “Create Integration” then “Continuous Sync” or "Migration" based on your requirements.<br>

   <figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FUI8Mr1JOPzNcfspi8BDj%2Fimage.png?alt=media&#x26;token=5b8f86e7-56f1-4537-93bf-8d01c57af6fa" alt=""><figcaption></figcaption></figure>

**Create the tokens for each workspace, and create the connections right after**

To ensure the integration functions properly, grant access to both environments using their respective access tokens.

You can learn how to create the access token on **Jira** with the below, but you can also follow this article: <https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/>

{% embed url="<https://www.loom.com/share/a6bcc913aef240f59ccb278e010f584e?sid=abe94819-52a8-455d-8a72-3b10da384d5c>" %}

In the video below you can learn how to create an access token for **Asana,** you can also read the instructions in the Asana article: [Personal access token](https://developers.asana.com/docs/personal-access-token)

{% embed url="<https://www.loom.com/share/3f4f209accd846eca989aedeb76357f6?sid=3d0080b8-0b11-4eb1-b6c9-cfde98f570dd>" %}

### **Add mapping fields and configure them** <a href="#add-mapping-fields-and-configure-them" id="add-mapping-fields-and-configure-them"></a>

Create a task ↔︎ task, and subtask ↔︎ subtask task type mapping, add your desired fields and define the sync direction (unidirectional or bi-directional) with the arrows. and configure your task status synchronization.\
Save your integration at the end:

{% embed url="<https://www.loom.com/share/f16575ca0ced489f9ccab8c600ef69c1?sid=52d5a050-f04e-418b-83f6-cb735abcd9c7>" %}

For Asana, we selected “Section” as a reflection to Jira tasks statuses, then applied the change, left the screen and re-entered it for the statuses to be displayed.\
**Note that the options at the left are form Jira, and the options from the right are from Asana.**

Click on the “Start with mapping types” button, and the “Map Your Types for a Seamless Integration” tab should pop up:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FHMd9P4EYrDw1wfqwheCf%2Fimage.png?alt=media&#x26;token=4747176f-20d0-4f56-bcc9-6c1c83f30955" alt=""><figcaption></figcaption></figure>

Map task to task, and you can add another mapping type with subtask to subtask:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FeikrNmdb8iybyKaGjyrb%2Fimage.png?alt=media&#x26;token=0017639b-2f98-41c0-b4bb-2f0efbb124d4" alt=""><figcaption></figcaption></figure>

Click on the newly created type mapping to enter the field configuration, then start mapping your fields:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FBHg4Zbs6ejv9sosNJ2Rn%2Fimage.png?alt=media&#x26;token=80d46e5c-c2d3-4695-8213-b324d689103f" alt=""><figcaption></figcaption></figure>

Use the dropdown menus to map your fields, for example, Assignee to Assignee, Priority to Priority, Title to Title, and so on, click on the arrows in the middle to define the synchronization flow (updates only unidirectionally from left to right, from right to left, or bidirectional)

**Click the “Apply” blue button at the right bottom to save the changes made.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fr649gGrpEw0nYgFnVS1H%2Fimage.png?alt=media&#x26;token=fde0b203-e204-49e7-9331-ef021c733fc8" alt=""><figcaption></figcaption></figure>

Map the statuses, use the dropdowns to map them according to your organization parameters, and click Apply to save the changes made

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FbsoTkbOgeFT6AqqExgm0%2Fimage.png?alt=media&#x26;token=ae9583f5-2df4-42fb-9c95-d7f60d97fbd6" alt=""><figcaption></figcaption></figure>

Name your integration, then create it

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fqxr2TrlxlSRi0cGwql67%2Fimage.png?alt=media&#x26;token=3f325f81-22c4-44e3-ae6b-4b571463ab9b" alt=""><figcaption></figcaption></figure>

### **Create a test ticket on both sides to check if it’s working** <a href="#create-a-test-ticket-on-both-sides-to-check-if-its-working" id="create-a-test-ticket-on-both-sides-to-check-if-its-working"></a>

**Create a ticket or tasks on each side to test the integration**:\
\
Add a comment or attachment, and change the task status on one side to ensure the corresponding fields are captured correctly on the other:

{% embed url="<https://www.loom.com/share/32fcee4152c04efc9ef2720026e85545?sid=06f3a4cd-25e6-493f-be4a-261ac7ec6751>" %}

The integration has been successfully set up, the tasks are synchronizing through both workspaces and assigning correctly the data from the fields mapped.

{% hint style="info" %}
In case you bump into an error while trying to integrate your software, please raise a ticket at our support channel: <https://getintio.atlassian.net/servicedesk/customer/portals>\
(You can also email us at <support@getint.io>).
{% endhint %}

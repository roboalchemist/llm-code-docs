# Source: https://docs.getint.io/guides/integration-synchronization/jira-monday.com-integration.md

# Jira Monday.com integration

Integrating Jira with Monday.com using Getint significantly enhances workflows, communication, and migration efficiency. Monday’s user-friendly interface and customizable workflows perfectly complement Jira’s robust issue-tracking capabilities. This integration streamlines tasks, updates, and timelines, thereby maximizing productivity.

With Getint, you can seamlessly integrate your Monday.com boards with Jira Cloud, Jira Data Center, or On-Premise, ensuring efficient synchronization of tasks across your workspace.

### Optimize your workspaces <a href="#optimize-your-workspaces" id="optimize-your-workspaces"></a>

Different projects have different requirements, with this in mind, you may like to track and integrate specific information for your project.

#### How to integrate custom fields for Monday.com integrations <a href="#how-to-integrate-custom-fields-for-monday.com-integrations" id="how-to-integrate-custom-fields-for-monday.com-integrations"></a>

Monday.com has a multitude of custom field types that can be added to your board, make sure to have your board configured beforehand with all the custom fields you would like to integrate so that when creating the integration, you can visualize them for mapping and map them according to their counterpart in Jira.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FAFIwfdw4XKMARc9QLFOA%2FMonday.com%20custom%20fields.png?alt=media&#x26;token=a67c4908-1737-4c7b-ae7f-4c4797802178" alt=""><figcaption><p>Available custom fields in a Monday workspace</p></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FCweZ6JoSfJD9NAQyvz3o%2FAvailable%20custom%20fields%20in%20Monday%20(1).png?alt=media&#x26;token=211884f2-a283-4f9a-b3d3-f22459dc36f0" alt=""><figcaption><p>Monday board with multiple custom field types added</p></figcaption></figure>

{% hint style="info" %}
Please, note that some custom field types may not be supported by us at the moment.\
In case you need a custom development for your product or project, please get in touch with our [support team](https://getint.io/help-center) for pricing.
{% endhint %}

### Create the integration | Add the connections <a href="#create-the-integration-or-add-the-connections" id="create-the-integration-or-add-the-connections"></a>

#### Access the Getint App in Jira <a href="#access-the-getint-app-in-jira" id="access-the-getint-app-in-jira"></a>

Here we will select the Jira - Monday.com Integration app for this integration, then create the connection for Jira with Jira’s API token and create the connection for Monday.com with Monday’s Personal API Token. Remember to give a name to your integration, then build it.

{% embed url="<https://www.loom.com/share/0e7f6f456796480e9336b09eaabd6f54?sid=aad5c2ff-31ca-4be2-ac39-550dde5cb99d>" %}

\
Navigate to Jira, go to **Apps,** and select the **Jira - Monday.com Integration app**.[<img src="https://marketplace.atlassian.com/s/images/favicon.ico" alt="" data-size="line">Monday.com Jira Integration \[2-way sync + migration\] | Atlassian Marketplace](https://marketplace.atlassian.com/apps/1225780/monday-com-jira-integration-2-way-sync-migration?hosting=cloud\&tab=overview)

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F7lXexX2QfUCfTVvmbgUW%2FJira%20Monday%20Integration.png?alt=media&#x26;token=16a99be7-2bfe-4c0b-8503-a0c0b9862e5b" alt=""><figcaption></figcaption></figure>

* Go to **Workflows,** then **Integrations,** select **Create Integration,** and then **Continuous Sync** or **Migration** based on your requirements.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FDD98e4uQUfBVJfbt9rHb%2FIntegration%20setup%20(2).png?alt=media&#x26;token=cdf5284b-e1b7-4cca-8006-28b5606e6fab" alt=""><figcaption></figcaption></figure>

#### Create the tokens for each workspace <a href="#create-the-tokens-for-each-workspace" id="create-the-tokens-for-each-workspace"></a>

For the integration to work properly, you must grant access to both environments through their respective access tokens.

* You can learn how to create the access token on **Jira** with the below, but you can also follow this article: [<img src="https://wac-cdn.atlassian.com/assets/img/favicons/atlassian/favicon.png" alt="" data-size="line">Manage API tokens for your Atlassian account | Atlassian Support](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/)

{% embed url="<https://www.loom.com/share/5f3b465c73f64fdfb09ceb579e8678fe?sid=4bd29d58-523e-463b-a4a9-2876643a6a31>" %}

* In the video below you can learn how to create an access token for **Monday,** you can also read the instructions in the Monday article: [![](https://files.readme.io/cfbc181-small-favicon-monday5-192.png)Authentication](https://developer.monday.com/api-reference/docs/authentication#accessing-api-tokens)

{% embed url="<https://www.loom.com/share/da2bbdaa0f0049609567868de98753e1?sid=db1e50fe-4f40-4b1c-809c-bffd05b3c3db>" %}

#### Mapping fields <a href="#mapping-fields" id="mapping-fields"></a>

Users can now build an entire integration, with multiple item types and fields mapped, with just a few clicks using our **Quick Build** feature.

**Use the quick build in your integration editor to create your integration from scratch:**

{% embed url="<https://www.loom.com/share/f23c366411a84183a8dcc75015e28ffc?sid=09e4ebb0-d48a-47c4-9359-60d6e1c878b9>" %}

* In your integration editor screen, click **Quick Build.** Next, click **Build,** and wait for the tool to load the item types and their fields.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FiIW2AUYQcJMbwPTHFGUK%2FJira%20Monday%20integration%20quickbuild%20(1).png?alt=media&#x26;token=ea35f41b-142b-4ff7-9988-06f14419cb22" alt=""><figcaption></figcaption></figure>

* Once the app loads the item types and their fields, take your time to check if the item types brought are the desired ones, also all fields brought up are configurable through this screen so you can go through each of them and set them as you desire.
* When you decide that everything is set as you expect, click **Apply.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FS9WKvEpCJn7J3T7dS0W4%2FQuickbuild%20options%20(1).png?alt=media&#x26;token=013511f5-cb2b-483d-aab1-e5b3a3e20a5c" alt=""><figcaption></figcaption></figure>

* If undesirable item types were brought, you can simply delete them through the integration editor. Either create your integration or save it right after.

#### Manually add and configure item types/fields

* Click on the **Add type mapping** button, and the **Map Your Types for a Seamless Integration** tab should pop up:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FxaGsQEL5J64ehoiCl0nP%2Fcreate%20integration%20(1).png?alt=media&#x26;token=b3707e73-0bf2-4417-b9b0-4e84fdda56d1" alt=""><figcaption></figcaption></figure>

* Create a task ↔︎ task, and subtask ↔︎ subtask task type mapping, add your desired fields, and define the sync direction (unidirectional or bi-directional) with the arrows. and configure your task status synchronization. Save your integration at the end:

{% embed url="<https://www.loom.com/share/d4b2a6ac3e8d43a1bc643542fceb6667?sid=2a79fda4-930e-4420-89e4-6b5052d3f35d>" %}

* Use the **Add Mapping Field** button to map different fields of your workspaces to integrate them, the menu at the top can be used to navigate the type mapping configuration screen to edit different settings of your mapping, such as **Status** and **Comments & Attachments.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F2HKgpuZXbahub2S49ltK%2Fadd%20field%20mappings%20(1).png?alt=media&#x26;token=9db15b98-3a8b-45b1-a3d2-9c8d4552e8e0" alt=""><figcaption></figcaption></figure>

* For **Comments & Attachments** in a Monday.com integration, please ensure to enable the attachments as they’re disabled by default. Also, attachments need to be uploaded from the **Files** column in your Monday board, otherwise, they will fail to sync.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FFbY2ezsh6yjDSJXARcTu%2FExample%20attachments%20in%20Monday.com%20(1).png?alt=media&#x26;token=b049e723-1032-4c6e-9102-5520f24185a9" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
Always upload attachments from the **FILES** column rather than the **Item/Task** menu to ensure file synchronization with the other app.
{% endhint %}

* Use the step-by-step configurator to add new mappings of different fields from your item types, click on the arrows in the middle to define the synchronization flow (updates only unidirectionally from left to right, from right to left, or bidirectional). At last, click the **Apply** blue button at the right bottom corner to save the changes made.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fl7Jr3cra2jnFI7hU9CCG%2FSync%20direction%20(1).png?alt=media&#x26;token=4a18c55d-34fc-4c47-8eb6-850c426b2e63" alt=""><figcaption></figcaption></figure>

* Map the statuses, use the dropdowns to map them according to your organization parameters, and click Apply to save the changes made.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FTmSPpCi2exPGXDIzdb8K%2FItem%20statuses%20(1).png?alt=media&#x26;token=74499f2e-a623-49a4-b79b-1c03f00d177c" alt=""><figcaption></figcaption></figure>

* Name your integration, then save the changes to create it.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FPnhLKwTad1OvwXvILh55%2FFinishing%20the%20steps%20(1).png?alt=media&#x26;token=04e6a69a-1386-47d7-aea0-758c0a8e1c85" alt=""><figcaption></figcaption></figure>

###

### Create a ticket on both sides to test the integration

Add a comment or attachment and change the task status to ensure the counterpart is capturing the mapped fields correctly:

{% embed url="<https://www.loom.com/share/146ea35ca30b44caad040ceebcc41896?sid=c4221468-de8f-46eb-9dca-bd25a7f372f0>" %}

{% hint style="warning" %}
Please be aware that replies to comments (also known as subcomments) are not supported by Getint, and they will not trigger synchronization. If an update is added before a sync is triggered, and a reply is subsequently added to the update, the tool will bring the subcomment to the other side. However, due to a technical limitation from Monday, we cannot guarantee that this will work consistently, to manage expectations.
{% endhint %}

At Getint, we take feedback and customer inquiries seriously. Therefore, if you bump into an error while trying to integrate your software, or if you have any custom requirements, please raise a ticket at our support channel [here.](https://getint.io/help-center)

# Source: https://docs.getint.io/getintio-platform/import-feature.md

# Import Feature

### Synchronizing Existing Items on Both Sides

Once an integration has been set up via Getint, newly created items on both sides will begin to synchronize. However, any items that existed before the integration was established (such as historical tickets synchronized manually or through another tool) will not sync. These pre-existing items may have been paired outside of Getint, but the initial integration won’t recognize such pairings. Possible cases include migrating from Exalate to Getint, TFS4JIRA to Getint, Backbone to Getint, or ConnectAll to Getint.

In this guide, we’ll explain how to link existing items between the tools to keep information aligned. This helps prevent duplicate tickets from being created and eliminates the need to manually delete existing content.

{% hint style="warning" %}
While we use specific connectors in our examples, this process applies to all Jira-related integrations.
{% endhint %}

#### How to Synchronize Existing Items in a Jira Integration

1. Please navigate to the integration and **Disable** it.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FxASC1YBx90gjjpFQL9hY%2Fd528e027f9e4e77ae7e9c9517c63c240%20(1).png?alt=media&#x26;token=a0f61815-ff8d-45fd-922e-0a2f9b6c4437" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
To avoid duplicate tickets, make sure your integration is disabled before making any changes. If it’s still active, the tool might see your updates as new items and end up creating duplicates.

We recommend disabling the integration at least **10 minutes before** initiating this process to ensure all runs are fully terminated and prevent unintended duplication.
{% endhint %}

1. Go to **Reporting** → **Synced items.** Then click on **Import.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F38Y2iaMYE0wxSUDT2cWB%2F0466d618a9cc153b3f4311791fc879fa%20(1).png?alt=media&#x26;token=00be07c5-0989-4e74-a0e7-fdd3ba852a58" alt=""><figcaption></figcaption></figure>

1. In the **Import** screen:
   * Select the relevant integration.
   * Select the side of the integration that represents the app you want to import the issues from.
   * Select **Automatically capture data of imported items** if data capturing needs to be performed during the first run of the integration. The condition is that Jira must be the left-side app of the integration.\
     **NOTE**: PLEASE do not mark this option if the Jira app is not on the left side of the integration.
   * Paste the relevant item IDs to be mapped from both sides. Sometimes, this list can be generated from one of the apps that the user is syncing. If you have stored a counterpart ID in a custom field, you can create a report with ID and COUNTERPART ID fields, which can be exported to XLS or CSV and then copied here.
   * The correct way to map item IDs would be as follows:
     * **Task ID** then a comma **(,)**, and the **counterpart ID.**
   * Finally, click **Apply** to submit the changes.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FXba3lIz6PRftv5H6bmjt%2FImport%20feature.png?alt=media&#x26;token=9d409824-93da-4402-a631-f05f762e72bc" alt=""><figcaption><p>Ensure the task IDs are in the correct order based on the side of the integration represented by the first column. In our example, the first column represents the left side of our integration.</p></figcaption></figure>

{% hint style="danger" %}
Please note that Getint will not be aware of the pairing if **Automatically capture data** is not selected in the above steps.
{% endhint %}

#### Pairing Related Items with Bulk Changes in Jira

To pair related items, please follow the steps described below:

1. Log in to your Jira instance and navigate to the **Search** screen.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FU07CAcQaqqvEis9LcZ90%2Ff4e28dcea7ac2c6c699ac111a4dbe968%20(1).png?alt=media&#x26;token=00b2bd39-33f7-494a-8314-9176339a92a9" alt=""><figcaption></figcaption></figure>

1. Fetch all the imported items in Jira (in this case, **DEMO-1, DEMO-2, DEMO-3**) and perform a bulk update by clicking on the **3 dots button** on the right-hand side of the screen. You can add a label (for example, **getint\_import\_sync**) to perform an update on these items.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FXg0CzC79oiUZ9xQW3ijr%2Fed1e4def686b05aff0b9318622abd6e0%20(1).png?alt=media&#x26;token=ee03e987-1049-4f04-ab51-8498f41903a4" alt=""><figcaption></figcaption></figure>

1. In the next screen, select all the relevant issues and click **Next.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F5CYVjyiOLzhZm7bnRMMk%2F1cb26a96f2ec563f7fa86ac36fb72546%20(1).png?alt=media&#x26;token=36cd7975-5955-4751-b8c5-6e8221c80eb3" alt=""><figcaption></figcaption></figure>

1. Choose **Edit Issues** in the next screen and click **Next.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FgmeRs63eJ7AimasBRHIC%2F1cb26a96f2ec563f7fa86ac36fb72546%20(1).png?alt=media&#x26;token=2c8a14da-d658-4b65-9072-424e7e3f7eea" alt=""><figcaption></figcaption></figure>

1. Go to Labels, check the box, and enter **getint\_import\_sync,** then click **Next.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fpe2hahY38ZdFqgbjCwsR%2Fca1d4c7f823087ca06336044d3121858%20(1).png?alt=media&#x26;token=73ed685a-e181-4b0a-9f3a-26a21c5038ce" alt=""><figcaption></figcaption></figure>

1. In the next screen, click **Confirm.** This will now bulk update all the related items.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FSQQMHAI4GRSpGeFst3BQ%2Fb540991ff46bb04ab12afaeaec3dd38d%20(1).png?alt=media&#x26;token=f902bbc6-ee40-4520-b371-babea94cda96" alt=""><figcaption></figcaption></figure>

1. **Enable** the integration (disabled above).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FOuWemdhIWSFcqb1K60mu%2Fb55753f4ac9a69c063ddfd88bb1abd88%20(1).png?alt=media&#x26;token=c1563b89-f8bb-4253-b9a1-7d635d71b128" alt=""><figcaption></figcaption></figure>

Once the integration is enabled and execution begins, only the data about imported items will sync during the first run. Subsequent integration runs will synchronize any applied changes according to the integration configuration.

{% hint style="warning" %}
**IMPORTANT NOTE**:

* The import process restricts pairing to 200 records per run for cloud customers and 1000 for customers with DC apps or On-Premise. Ensure that pairing adheres to these limits, which are valid only for users with a full license.
* The import process is limited to pairing 5 records if you are on a trial version.
  {% endhint %}

#### Tutorial Video

{% embed url="<https://www.loom.com/share/d0c8f764b52541ffb6a883ebcc758f1a?sid=d0a4bf00-7e13-4c50-b9e3-a9c03a6c2ee3>" %}

#### How to Copy the Correct Work Item ID Based on Your App

**Asana**

Asana doesn’t show the issue ID up front, so you can either copy it from the task’s web address or add a custom field to retrieve each task ID. The easiest way to find it is through the task’s URL as shown in the below picture.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FqBTc1HO4FrVqptQz6tPC%2FTask%20ID%20Asana.png?alt=media&#x26;token=4d8780ac-8565-4b2e-8f8b-45ea91ccc8c5" alt=""><figcaption></figcaption></figure>

**ServiceNow**

ServiceNow also does not display the issue ID (referred to as the **sys\_id**) in the user interface by default. However, the identifier can be retrieved through the task’s URL or by accessing the record details directly.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FA4gKvv7c4j5zyrj9FsIQ%2FTask%20ID%20for%20ServiceNow%20work%20items.png?alt=media&#x26;token=e8a99397-b0cb-4484-983e-269ce7c247fb" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
These are just two examples of how get IDs from other tools. If you're experiencing issues with the import process, it's a good idea to check with your technical team to confirm that you're pulling the correct work item ID from your app.
{% endhint %}

If you have any questions or need assistance, please do not hesitate to contact us at our [Help Center](https://getint.io/help-center) or [Schedule a Demo](https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

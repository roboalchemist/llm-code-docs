# Source: https://docs.getint.io/getintio-platform/workflows/how-to-map-fields.md

# How to Map Fields

### **Improve Your Workflow with Precise Field Mappings** <a href="#improve-your-workflow-with-precise-field-mappings" id="improve-your-workflow-with-precise-field-mappings"></a>

Unlock the full potential of integrating work items like tasks, bugs, service requests, and incidents across different platforms with our new Getint Field Mappings feature. This tool is designed to fit your workflow perfectly, making it easier to keep everything in sync. Let's dive into what this feature offers.

#### **Understanding Field Mappings** <a href="#understanding-field-mappings" id="understanding-field-mappings"></a>

Field mapping is all about linking important details of your projects, like titles, descriptions, who's in charge, and any attachments, across different tools. Our platform ensures these details match up between all sorts of work items—whether they're tickets, incidents, service requests, bugs, or contacts. This keeps your data in sync almost in real-time.

Here's how you can see this in action on our platform:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FjTHUaTuOpD5uoiiHHPKU%2FHow%20to%20map%20fields.png?alt=media&#x26;token=999c404b-7126-4702-9a04-d7cffe86e562" alt=""><figcaption></figcaption></figure>

#### **Starting with Manual Field Mapping** <a href="#starting-with-manual-field-mapping" id="starting-with-manual-field-mapping"></a>

If you're missing a key piece in your mapping, the **+ Add field mapping** button is there to help you find the right match.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FfP6qTMByqZGKMckdQElG%2FAdding%20a%20Field%20mapping%20manually.png?alt=media&#x26;token=e4834d66-f48a-4cb7-8475-717659fcc677" alt=""><figcaption></figcaption></figure>

Let’s say you're linking the **Assignee** field in Jira with the **Assigned to** field in Azure DevOps. Here's how easy it is:

1. Begin by selecting Jira.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FyWUDEAWcgNCjZTxnUVMF%2FSelecting%20the%20jira%20side%20to%20add%20a%20field%20mapping.png?alt=media&#x26;token=284b77f7-00e6-4afb-ada3-7ff3fe91c5ef" alt=""><figcaption></figcaption></figure>

1. Choose the Jira field you wish to integrate—**Assignee**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FZNyEOYFT4TX6GHL4XWTR%2FSelecting%20Assignee%20for%20synchronization.png?alt=media&#x26;token=9f283c77-a04c-4c1e-a328-f2694cea90d3" alt=""><figcaption></figcaption></figure>

1. Then, select Azure DevOps as the second application, choose the **Assigned to** field, and click the **Add** button.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FJ6LXeDrfAxzw7CR06c6f%2FSelecting%20Assigned%20to%20from%20the%20field%20mappings.png?alt=media&#x26;token=f5747ef5-9c7c-46f4-b056-8048f798a5b5" alt=""><figcaption><p>We’re using Jira DevOps as an example, but these steps apply to all of our connectors.</p></figcaption></figure>

#### **Removing a Field Mapping** <a href="#removing-a-field-mapping" id="removing-a-field-mapping"></a>

To remove a field mapping that's not working for you, just hover over it and click the delete icon. This won’t delete or modify any of your data.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FaNXTIEgn264FtYS6DgIy%2FRemoving%20a%20field%20mapping.png?alt=media&#x26;token=d3d8cabd-767e-4717-9d50-354d12db955b" alt=""><figcaption></figcaption></figure>

#### **Changing How Data Moves** <a href="#changing-how-data-moves" id="changing-how-data-moves"></a>

With Getint, data usually moves back and forth between tools by default. But you can adjust this any way you like. Want to send data only one way? Just click on the arrows to set it up.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fv5DPXrzsJwCMTs0iEZo6%2FDeciding%20the%20sync%20direction%20for%20field%20mappings.png?alt=media&#x26;token=7d0af36c-ef2b-4a22-864f-f18a1a43db57" alt=""><figcaption></figcaption></figure>

#### **Handling Dropdown Fields** <a href="#handling-dropdown-fields" id="handling-dropdown-fields"></a>

You'll see a warning icon for fields like Assignee, Priority, or Status if they need more detail. Hit the cog icon for more options.

* **Map options directly:** Link specific options from one field to another, like matching **Jack Smith** in Jira to **Jack Smith** in DevOps.
* **Use default mapping:** This is great for sending dropdown info to a text field without needing a detailed map. It just turns the dropdown choice into text.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FpOUggP00Ds6DHhVUeo4s%2FField%20mapping%20configuration.png?alt=media&#x26;token=92d1ad03-350d-4709-a43f-bcb5a43ac47b" alt=""><figcaption></figcaption></figure>

#### **Concatenating Fields** <a href="#concatenating-fields" id="concatenating-fields"></a>

Starting from version 1.75, Getint will now allow the synchronization of multiple fields into a text-based field like the Description or the Title. This will be possible by clicking the **Merge fields** checkbox above the field mappings.

**How to Merge Fields:**

1. Select the side that you want to integrate and tick the merge fields checkbox.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FBNX3KEAOQr651NeFxTif%2FMerging%20fields.png?alt=media&#x26;token=a7072fa4-9211-4ecf-afd1-46fadcc90851" alt=""><figcaption></figcaption></figure>

1. Now, integrate fields into the text-based fields. Click the **+Merge here** option to integrate your selected field.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FLCRM32n6f9gZSB1wpSQQ%2FMerge%20here%20button%20to%20concatenate%20fields.png?alt=media&#x26;token=c83ba0fc-774e-449b-8adf-3461e394dda8" alt=""><figcaption></figcaption></figure>

In this case, we'll merge the Assignee and Priority fields with the Title (Jira) and the URL field with the Description field. This means that every time a ticket is created or updated, it will transfer the Title from the issue and include the current Assignee and Priority. Additionally, we're merging the Description with the URL, which will bring the URL from the task to the other side of the integration. However, some fields, like the URL from the task, only sync when the item is created, as this is the only time the URL field is triggered for synchronization. We're using a Jira Azure DevOps integration as an example, but this applies to other integrations as well.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FrqecY4qXCaAO4EljMjPp%2FConcatenating%20fields%20from%20the%20Jira%20side.png?alt=media&#x26;token=8d1e2344-57c6-4e90-aeff-63d09b64196b" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Merging fields operate unidirectionally, meaning synchronization occurs from only one side. Consequently, the Title on the opposite side cannot be synced with other fields simultaneously.
{% endhint %}

1. You can make different combinations as long as you don’t surpass the character limit for the text field on the other side.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FSMagPMJIXmRLd7gJNB1q%2FMerging%20different%20fields%20from%20two%20sides.png?alt=media&#x26;token=8b5144ce-b4f7-4b6d-b1ab-fd824109fc07" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Certain fields, like URL or ID, only sync during creation, as this is the only time when these fields are triggered for synchronization. As a result, updating existing items will not transfer the URL of the issue to the corresponding field you are syncing with.
{% endhint %}

1. Click Apply and Save your integration.

#### **Mapping Special Fields** <a href="#mapping-special-fields" id="mapping-special-fields"></a>

Some fields, like the URL or ID, can't be changed directly. To map these, you might need to create a special field on the other side first. Then, you can link them up. Read more in the following article: [Storing Reference IDs/URLs Across Integrations.](https://docs.getint.io/getintio-platform/workflows/storing-reference-ids-urls-across-integrations)

#### **Conclusion** <a href="#conclusion" id="conclusion"></a>

As we've demonstrated, integrating fields in a unidirectional manner allows for smooth and consistent updates. However, it's important to note that certain fields, like URL or ID, only sync during creation, emphasizing the need for careful planning and implementation.

We hope this article has provided valuable insights into the steps of merging and mapping fields. If you have any questions or require further assistance, please do not hesitate to reach out to us. Our team is always ready to help you achieve a more efficient and effective data management system.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

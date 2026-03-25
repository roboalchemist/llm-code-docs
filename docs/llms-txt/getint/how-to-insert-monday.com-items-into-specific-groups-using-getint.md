# Source: https://docs.getint.io/guides/integration-synchronization/jira-monday.com-integration/how-to-insert-monday.com-items-into-specific-groups-using-getint.md

# How to Insert Monday.com Items into Specific Groups Using Getint

Groups on Monday provide a way to organize tasks, projects, and workflows efficiently. When integrating with Jira, Asana, Azure DevOps, or other tools through Getint, users may need to automatically assign items to specific groups instead of having them placed in a default category.

This guide explains how to configure custom field mapping to ensure that items land in the correct group during synchronization.

### Why Assign Items to Specific Groups <a href="#why-assign-items-to-specific-groups" id="why-assign-items-to-specific-groups"></a>

By default, new tasks synced into Monday may not be placed in the intended group, requiring manual adjustments. Using custom field mapping, teams can ensure items are categorized correctly without additional effort.

#### Benefits <a href="#benefits" id="benefits"></a>

* Improves organization by ensuring items are placed in the right group automatically.
* Reduces the need to manually move tasks after sync.

#### **Step 1: Create a Custom Field in the Source Tool** <a href="#step-1-create-a-custom-field-in-the-source-tool" id="step-1-create-a-custom-field-in-the-source-tool"></a>

To enable group assignment, a custom field must be created in the source tool. This field will determine where each item is placed on Monday.

Since the process varies by platform, refer to the official instructions for creating custom fields. For this guide, we will use Jira - Monday integration:

* [**How to Create a Custom Field in Supported Software**](https://getintio.atlassian.net/wiki/spaces/Support/pages/898170881/How+to+Insert+Monday.com+Items+into+Specific+Groups+Using+Getint) (full guide).
* **Jira** - follow the steps on [Create a Custom Field](https://support.atlassian.com/jira-cloud-administration/docs/create-a-custom-field/) and add the field to the issue types:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FUb2lOFcqaKZkIh3HldpV%2FCreating%20groups%20in%20Jira.png?alt=media&#x26;token=5968a2c6-ae26-4948-8956-4eb5e91dcb61" alt=""><figcaption></figcaption></figure>

When setting up the field:

* Use a **Dropdown (Single Select) or Picklist** to match group values.
* Ensure that all issue types contain the new field.

#### **Step 2: Map the Custom Field to Monday.com** **Groups in Getint** <a href="#step-2-map-the-custom-field-to-monday.com-groups-in-getint" id="step-2-map-the-custom-field-to-monday.com-groups-in-getint"></a>

Once the custom field is set up, configure Getint to recognize and use it for group assignment.

* Open **Getint** and navigate to the integration.
* Select **Type Mapping** then add **Field Mapping** and locate the custom field created in Step 1. Map this field to the **Group** field in Monday.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FvCcxc9MmPTivqMS6xWmf%2FMapping%20the%20Groups.png?alt=media&#x26;token=763ab96f-8246-4f05-b167-4a7cfb7e403b" alt=""><figcaption></figcaption></figure>

* Click on the cog icon to match the groups.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FuPiSUQDUK0zH1h9GxUUy%2FMapping%20the%20available%20options%20in%20the%20groups.png?alt=media&#x26;token=2e310605-243d-4181-9816-51dbb2793790" alt=""><figcaption></figcaption></figure>

* Define the synchronization direction:
  * **Unidirectional (Source to Monday)** – Items are assigned a group based on the source tool but will not update if moved manually
  * **Bidirectional (Sync Both Ways)** – Group changes will reflect in both systems
* Click **Save** to apply the mapping

{% hint style="warning" %}
The Group field **must be** mapped to a dedicated custom field instead of a status field, as statuses function separately in synchronization.
{% endhint %}

#### **Step 3: Test the Integration** <a href="#step-3-test-the-integration" id="step-3-test-the-integration"></a>

Once the setup is complete, verify that it functions correctly by testing with new items.

* Create a task in the source tool and set the **Group Assignment** field to a specific group.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FQwdKDVo5EYfUm3Fm89jA%2FGroup%20assignment%20from%20Jira.png?alt=media&#x26;token=f020dbb7-b0ac-47dd-97ed-7f7b3345a99c" alt=""><figcaption></figcaption></figure>

* Wait for the sync to happen and check that the item appears in the correct group.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FfVfpsJtwv98IQXXo8rhb%2FChecking%20Syncs%20with%20Monday%20Groups.png?alt=media&#x26;token=7aebe415-65e8-4db9-b090-fee2e6c34a17" alt=""><figcaption><p>Ticket assigned to the Group selected</p></figcaption></figure>

If items are not assigned as expected, review:

* The values entered in the custom field
* Field mapping settings in Getint
* Sync logs for potential mapping errors

### Conclusion <a href="#conclusion" id="conclusion"></a>

By mapping a custom field in the source tool to the **Group field**, users can ensure that items are automatically placed in the correct category, eliminating manual adjustments and improving workflow efficiency.

For further assistance, check the [**Getint Help Center**](https://getint.io/help-center) or contact support.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FLilxKjQzV1V0fHEgCW7L%2FGetint%20Banner%20-%20Schedule%20a%20Demo.jpg?alt=media&#x26;token=78a1f8e4-f61d-4357-a8a6-5fa09126b06a" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues to build your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>

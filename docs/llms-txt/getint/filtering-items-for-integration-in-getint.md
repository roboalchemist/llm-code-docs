# Source: https://docs.getint.io/getintio-platform/workflows/filtering-items-for-integration-in-getint.md

# Filtering Items for Integration in Getint

Efficient integrations often require syncing only a subset of items rather than everything in a project. For instance, you may want to sync an item only when it reaches a specific state, acquires a certain status, or has a designated custom field value. With Getint, you can define filtering rules to ensure only relevant items are synchronized between apps, saving time and resources while keeping your data clean and focused.

{% hint style="info" %}
This functionality was officially available starting from version **1.40.0** of Getint.
{% endhint %}

### **Where to Find Item Filtering** <a href="#where-to-find-item-filtering" id="where-to-find-item-filtering"></a>

In Getint, you can specify filters for each app in the integration. To define filter rules:

1. Click the **FILTER** icon located next to the app in your integration setup.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FhcUzarj0sxQKjNgRjpMD%2FWhere%20to%20find%20item%20filtering.png?alt=media&#x26;token=ffe06084-1067-4f41-ba9b-a654c1ca2844" alt=""><figcaption></figcaption></figure>

1. Filters are applied at the beginning of the sync process. If the defined rules are not met, the synchronization for those items will be halted, ensuring only items meeting your criteria are synced.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fd6e7U4gBfSBIGKpdfO26%2FChecking%20error%20message%20about%20wrong%20filters..png?alt=media&#x26;token=59550dac-af0d-462e-bc42-566f224c9848" alt=""><figcaption></figcaption></figure>

### **Setting Up Filter Rules**

Once you click the **FILTER** icon, a sidebar will open where you can define the rules.

#### **1. Define Item Sets**

You can specify which items the rules will apply to by selecting one of the following sets:

* **ALL items filter**: Rules will apply to every item before synchronization begins.
* **NEW items filter**: Rules will apply only to newly created items that have not been synced before.
* **SYNCED items filter**: Rules will apply to items that have already been synchronized.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FMLENq4bLsGqiiZZop86W%2FFilter%20rules.png?alt=media&#x26;token=eab739ff-b381-4130-97a3-3c79b6e539d0" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
If you specify rules for both **ALL items filters** and **NEW items filters**, new items must meet the criteria for both sets before they are synchronized.
{% endhint %}

#### **2. Add Rules**

* **Select a Field**: Choose the field you want the rule to evaluate (e.g., Assignee, Status, custom field).
* **Choose an Operator**:
  * **Contains**: Checks if a field includes a specific substring. Example: Filtering items where the title contains **urgent**.
  * **Contains one of**: Checks if a field contains at least one value from a list. Example: Filtering items where the status contains either **In Progress** or **Completed**.
  * **Equals**: Matches the exact value of a field. Example: Filtering items where the priority equals **High**.
  * **Is empty**: Finds items where the field has no value. Example: Filtering items where the **Due Date** field is empty.
  * **Is not empty**: Finds items where the field has any value. Example: Filtering items where the **Description** field is filled.
  * **Matches (regex)**: Uses a regular expression pattern to find matches in a field. Example: Filtering items where the ID matches a pattern like `TASK-\d{4}` (e.g., **TASK-1234**).
  * **Not contains**: Finds items where a field does *not* include a specific substring. Example: Filtering items where the title does not contain **draft**.
  * **Not equals**: Filters items where the field does *not* match a specific value. Example: Filtering items where the category is *not* **Bug**.
  * **Is after**: Filters based on date or numeric values, finding items where the value is greater than the specified one. Example: Filtering items with a due date *after* May 1st.
  * **Is before**: Finds items where the value is *less* than the specified one. Example: Filtering items with a due date *before* May 1st.

{% hint style="warning" %}
**Contains** operators are case sensitive.

**Is after** and **is before** apply specifically to Date fields, so they will only be available when a Date field is selected from the dropdown options.

As with Date fields, certain operators may be unavailable depending on the fields selected for filters.
{% endhint %}

* **Add the Rule**: Click the **Add** filter and then **Apply** button to save the rule to the list.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FWPWSR7BHM6sSJTXfbxWY%2FFiltering%20Jira%20items.png?alt=media&#x26;token=907aa59d-8377-4f70-8172-8a3a4be55690" alt=""><figcaption></figcaption></figure>

#### **3. Manage Rules**

* **Remove a Rule**: To delete a rule, click the **TRASH** icon next to the rule.
* **Apply Rules**: Once your rules are defined, click **APPLY** to activate the filters for the specific app.
* **Save Integration**: After applying the rules, save the integration to finalize the setup.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F83NgM3IwvZnRxfFuVsIG%2FApplying%20a%20filter.png?alt=media&#x26;token=3e9616cf-ee32-42d2-a3cc-dd63e81393b0" alt=""><figcaption></figcaption></figure>

### **How Rules Are Evaluated**

If you provide multiple rules within a single section (**ALL / NEW / SYNCED**), they will be combined using the **AND** operator. This means **all rules must be satisfied** for an item to pass the filter and be included in the sync.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F38SsMlQcI3TyL0HIfsni%2FHow%20Rules%20Are%20Evaluated.png?alt=media&#x26;token=81735308-5336-4e2a-85e6-7b2b2570e5c8" alt=""><figcaption></figcaption></figure>

### **Conclusion**

The Item Filtering feature in Getint allows you to tailor your integrations to your specific needs, ensuring only the most relevant items are synchronized. This not only optimizes performance but also provides data integrity across platforms.

For further assistance or questions about item filtering, visit our [Help Center](https://getint.io/help-center) or contact our support team.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

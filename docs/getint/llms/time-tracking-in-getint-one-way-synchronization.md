# Source: https://docs.getint.io/guides/integration-synchronization/jira-jira-integration/time-tracking-in-getint-one-way-synchronization.md

# Time Tracking in Getint – One-Way Synchronization

In Getint, time-tracking synchronization is available, but there are some important distinctions to keep in mind. While the **Original Estimate** can be mapped both ways between systems, the **Remaining Estimate** and **Time Spent** are limited to one-way synchronization. These fields must be mapped to a text field in the target system. In this guide, we will explain how time-tracking synchronization works, and the best way to configure your mappings to ensure accurate and effective data flow.

### Understanding Time Tracking Fields <a href="#understanding-time-tracking-fields" id="understanding-time-tracking-fields"></a>

#### **1. Original Estimate:**

This field represents the initial estimate of time required to complete a task or issue.

* **Two-Way Synchronization**: You can map the **Original Estimate** field in both directions, meaning it can be updated and synced from either system.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fi7nkWtKC56cOkYe86G2r%2FTime%20tracking%20synchronization.png?alt=media&#x26;token=0b14f5c6-ad1e-4f48-8169-b7e9440428a6" alt=""><figcaption></figcaption></figure>

#### **2. Remaining Estimate:**

This field represents the amount of time left to complete the task or issue.

* **One-Way Synchronization**: The **Remaining Estimate** can only be synced in one direction. It needs to be mapped to a text field in the target system. You will see a "read-only" indicator when configuring the mapping, meaning that changes made in the target system will not sync back.

#### **3. Time Spent:**

This field tracks the actual time that has been spent working on a task or issue.

* **One-Way Synchronization**:

Similar to the **Remaining Estimate**, the **Time Spent** field can only be synchronized in one direction and must be mapped to a text field. It cannot be updated from the target system and only serves as a reference.

{% hint style="warning" %}
Note: The mapping of these fields is disabled by default to map both ways.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FOqWTAyOH4RiiANbJL1e2%2FMapping%20these%20fields%20is%20disabled%20by%20default.png?alt=media&#x26;token=d2652203-0000-4a00-8a59-f20aba3bd682" alt=""><figcaption></figcaption></figure>

### Configuring Time Tracking in Getint <a href="#configuring-time-tracking-in-getint" id="configuring-time-tracking-in-getint"></a>

To set up time tracking synchronization, follow these steps:

* **Original Estimate Mapping (Two-Way)**:
  * When mapping the **Original Estimate**, you can choose to sync the field in both directions. This is useful if both systems need to keep track of the initial time estimates for tasks.
  * Select the **Original Estimate** field in both systems during the field mapping process. Ensure that it is mapped as a two-way sync to allow updates from either side.
* **Remaining Estimate & Time Spent Mapping (One-Way)**:
  * For the **Remaining Estimate** and **Time Spent**, select these fields in the source system.
  * In the target system, map these fields to text fields. Since these fields are one-way sync only, you will see a "read-only" label when configuring the mappings, indicating that they can only be updated in the source system.
  * Any updates made in the source system will be reflected as text in the target system.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FXwrJ5UIvwH4NpDZS5eIe%2FConfiguring%20Time%20Tracking%20with%20Getint.png?alt=media&#x26;token=9aa77519-a159-4275-abfc-eebfa610edd6" alt=""><figcaption></figcaption></figure>

### Key Considerations <a href="#key-considerations" id="key-considerations"></a>

* **Text Field Mapping**: Since **Remaining Estimate** and **Time Spent** are mapped to text fields in the target system, their values will not be interactable or updateable in the target system. They serve as a static reference point for the time-tracking data.
* **Read-Only Fields**: These fields are marked as "read-only" during the field mapping process, meaning that changes can only be made from the source system and not in the target system.
* **Consistency**: It's crucial to ensure that your team is aware of the one-way synchronization for the **Remaining Estimate** and **Time Spent** fields. All updates to these fields must be made in the source system to maintain accurate and consistent data across integrations.

### Conclusion <a href="#conclusion" id="conclusion"></a>

Time tracking in Getint provides valuable synchronization options but with some limitations. While the **Original Estimate** can be synchronized both ways, the **Remaining Estimate** and **Time Spent** fields are limited to one-way synchronization and must be mapped to text fields in the target system.

For more detailed guidance or assistance with configuring your time-tracking integration, visit our [Help Center](https://getint.io/help-center).

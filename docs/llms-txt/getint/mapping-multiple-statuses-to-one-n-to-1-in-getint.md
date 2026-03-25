# Source: https://docs.getint.io/getintio-platform/workflows/mapping-multiple-statuses-to-one-n-to-1-in-getint.md

# Mapping Multiple Statuses to One (N to 1) in Getint

When setting up an integration in Getint, users often want to consolidate several different statuses from the source system into a single status in the destination system. This is referred to as **N-to-1 status mapping** (many-to-one).

For example, you might want to map To Do, Ready, and Open from Jira to a single Active status in Azure DevOps.

This guide explains how to configure N-to-1 status mappings effectively, avoid common mistakes, and ensure smooth synchronization.

### Why Use N-to-1 Mappings? <a href="#why-use-n-to-1-mappings" id="why-use-n-to-1-mappings"></a>

You might want to reduce complexity in the destination workflow, align with a simplified status model, or maintain a consistent reporting structure across tools.

**Common scenarios include:**

* Unifying multiple "open" states from a detailed workflow
* Migrating from a granular system (e.g., Jira) to a simpler one (e.g., Trello or Monday.com)
* Avoiding sync failures due to unmapped statuses

### How to Configure N-to-1 Status Mapping <a href="#how-to-configure-n-to-1-status-mapping" id="how-to-configure-n-to-1-status-mapping"></a>

#### Step 1: Open Your Integration <a href="#step-1-open-your-integration" id="step-1-open-your-integration"></a>

* Open your [Getint](https://getint.io/) app and navigate to your integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FXjiKFoolOcv9l39z3dbK%2Fopening%20%20your%20integration.png?alt=media&#x26;token=fe82d276-9c6b-4460-b90e-8e7c86b62289" alt=""><figcaption></figcaption></figure>

* Select **Edit** and go to the **Status Mapping** section.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FzQnRDxLEyp0jAoVI8e01%2Fimage-20250529-164727.png?alt=media&#x26;token=9c103789-184e-4bc3-8987-4109b8560da6" alt=""><figcaption></figcaption></figure>

#### Step 2: Add a Status Mapping Rule <a href="#step-2-add-a-status-mapping-rule" id="step-2-add-a-status-mapping-rule"></a>

* Open the status mapping screen and locate the **left-side** dropdown.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FZJ21YKfrf6YxtSQrJaJA%2Fimage-20250529-164840.png?alt=media&#x26;token=be42e221-d975-4ab1-9843-3f8f105dc824" alt=""><figcaption></figcaption></figure>

* On the **right side**, select the corresponding target status that should receive the mapped value.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FtiPCl2hlYBDPLtZfqy39%2Fimage-20250529-165047.png?alt=media&#x26;token=9196ad17-d7c7-4b02-89b0-d2aaa6cd1464" alt=""><figcaption></figcaption></figure>

* To add more statuses from the source side to the same target status, select another source status and click the **+Add option here**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FlLN4WScZidvWfQ3xGZIW%2Fce505147-3b48-406d-8299-8a22e18b9c41.png?alt=media&#x26;token=1929b4db-1703-48ff-9963-2ca126d0c826" alt=""><figcaption></figcaption></figure>

* Both source statuses will now be mapped to the selected target status.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9R9DJIdeVzfI0goptKKo%2Fimage-20250529-170310.png?alt=media&#x26;token=9db1e9a3-6bda-46a1-9a6c-bb86ff008b5b" alt=""><figcaption></figcaption></figure>

* By default, the first mapped status is treated as the default. This means that in a bidirectional sync, the source side will always use this default status when syncing values back from the target side.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F2AX2V2cLaoOVYvvH3VNW%2Fimage-20250529-173044.png?alt=media&#x26;token=9ed14eac-ea1f-4299-8f5a-7b0e0dc7bac8" alt=""><figcaption></figcaption></figure>

* To change the **Default** status, click on **Set Default** on the side of the mapped status.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fi9rWg9UNGq6F3oO9Pr7d%2Fimage-20250529-174124.png?alt=media&#x26;token=e977372d-9d57-48d1-a7cf-5bc90be022f1" alt=""><figcaption></figcaption></figure>

#### Step 3: Repeat for Each Source Status <a href="#step-3-repeat-for-each-source-status" id="step-3-repeat-for-each-source-status"></a>

Repeat the above step for each additional source status that should point to the same target status.

Repeat the above step for each additional source status that should point to the same target status.

**Important:** It is only possible to map each status once, and only in a many-to-one configuration.

### Best Practices

* **Check workflows:** Make sure your target system accepts transitions into the chosen status. Some systems have workflow constraints.
* **Test mappings:** Use the integration logs to validate your mappings after enabling and running the sync.

### Troubleshooting N-to-1 Mapping Issues <a href="#troubleshooting-n-to-1-mapping-issues" id="troubleshooting-n-to-1-mapping-issues"></a>

#### Problem: Status Not Updating as Expected <a href="#problem-status-not-updating-as-expected" id="problem-status-not-updating-as-expected"></a>

**Cause:** The destination status might not allow incoming transitions from all mapped source statuses.\
**Solution:** Review the destination tool’s workflow rules and allow the necessary transitions. We recommend reviewing our doc, Simplifying Workflow Sync with Getint: Jira, which should help to ensure a block-free workflow.

#### Problem: “Unmapped status” Warning <a href="#problem-unmapped-status-warning" id="problem-unmapped-status-warning"></a>

**Cause:** A source status was not included in your mapping.\
**Solution:** Go back to **Status Mapping** and add the missing status manually.

Configuring N-to-1 status mappings can simplify your synchronization process and help align differing workflows across platforms. However, it's essential to define each rule deliberately. Each status can only be mapped once, and mappings must follow a many-to-one structure.

Before finalizing your setup, double-check that each mapped status aligns with your destination workflow’s transition rules and that all relevant statuses are accounted for.

Still have questions or need support with your configuration? Visit our [Help Center](https://getintio.atlassian.net/servicedesk/customer/portal/1/group/4/create/18) for expert assistance.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FxixagBRUPcst9bwPXViB%2FGetint%20Banner%20-%20Schedule%20a%20Demo.jpg?alt=media&#x26;token=a6143a85-9223-4f76-a66c-5a79f945ee21" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

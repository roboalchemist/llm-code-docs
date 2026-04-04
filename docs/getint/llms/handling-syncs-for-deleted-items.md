# Source: https://docs.getint.io/getintio-platform/handling-syncs-for-deleted-items.md

# Handling Syncs for Deleted Items

When working across different platforms or systems, it’s essential to understand the limitations related to data synchronization. One critical area where limitations exist is the synchronization of deleted items. In this article, we’ll explore the current limitations regarding deletion sync and provide a recommended workaround.

### Current Limitation <a href="#current-limitation" id="current-limitation"></a>

The issue arises when an item (such as an issue, task, or record) is deleted on one platform. Unfortunately, this deletion does not automatically trigger a corresponding deletion on the other platform. In other words, if you delete an issue in Platform A, it won’t be automatically removed from Platform B.

### Recommended Workaround <a href="#recommended-workaround" id="recommended-workaround"></a>

To address this limitation, consider implementing the following workaround:

1. **Create a “Deleted” Status or Label:**
   * Go to your app instance and create a **custom status** or **label** specifically for deleted items in your workflow.
   * Apply this status or label to any item you want to mark as **deleted.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Ff2JwzB9bdqdmLKXaPQBx%2F7c402a943e0cf7a605200ee7b0549660%20(1).png?alt=media&#x26;token=2b06d240-5bc2-41c4-bee2-9c9a0f5688d5" alt=""><figcaption><p>Label created to identify <strong>Deleted</strong> issues. We’re using a Jira instance as an example</p></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FD5i4F1YbxbLy3WZapksL%2Fdd5a763cf5a2269ee6c1bd84e4ad4d91%20(1).png?alt=media&#x26;token=b18b11c2-d3cc-42c3-8965-ed492e653bdc" alt=""><figcaption><p>Custom status created for <strong>Deleted</strong> issues</p></figcaption></figure>

{% hint style="info" %}
If you want an in-depth guide on how to create custom fields, please visit our article here: [How to create a custom field](https://docs.getint.io/guides/integration-synchronization/how-to-create-a-custom-field-in-all-support-software).
{% endhint %}

1. **Manual Cleanup:**
   * Regularly review items with the **Deleted** status or label.
   * Manually erase these items from the other platform as needed.

Please note that syncing deleted items is not supported, and there are no current plans to implement it. While this workaround adds an extra step, it helps mitigate the limitation effectively.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

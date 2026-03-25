# Source: https://docs.getint.io/guides/integration-synchronization/jira-monday.com-integration/synchronizing-attachments-in-a-monday.com-integration.md

# Synchronizing Attachments in a Monday.com Integration

Our tool allows users to migrate and synchronize attachments from Monday tasks to other management software we support. However, please note that inline images are not currently supported for synchronization.

### Key Points and Considerations

* **File Size Limit:** Monday enforces a 500MB file size limit for task attachments. Be mindful of this limitation when dealing with large files.
* **Inline Images:** We currently do not support inline images. Please note that they won’t be properly synchronized.
* **Enabling the Feature:** Attachments are disabled by default. They need to be activated manually within your integration settings.
* **Attachments Limitation:** Uploading attachments from the **Files** section within the tasks is not supported. Attachments need to be uploaded from the **Files** column in your Monday.com board.

### How to Sync Attachments

1. Navigate to the **Comments & Attachments** section in the mapping configuration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FQrp8CbILMsi1hHkWofHf%2Fa34213f4177462df29ea7dad21d2f5c6%20(1).png?alt=media&#x26;token=e2c904c4-1970-4a59-b14a-70d3b4491b51" alt=""><figcaption></figcaption></figure>

1. Scroll down to **Synchronize attachments** and enable the option.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fh9b5RJCvyw8z4fhn7OGu%2Fd911384ed3bc3c5ad3d26144c1d4f7ed%20(1).png?alt=media&#x26;token=75eacc76-0380-4c37-a2de-f3e1e281758f" alt=""><figcaption></figcaption></figure>

1. Go to your **Monday.com** workspace and upload attachments from the **FILES** column in your **Monday.com board.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FJ8T51cY4WjQazE4aIwar%2F995b3b95f73710e20e90b5e47dc98ad9%20(1).png?alt=media&#x26;token=f5e4521e-6be0-47ae-950b-d5087710c542" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Always upload attachments from the **FILES** column rather than the **Item/Task** menu to ensure file synchronization with the other app.
{% endhint %}

1. Choose the synchronization direction for your attachments. Options include **Both ways** (bi-directional sync), **Only to app A** (left)**,** and **Only to app B** (right) for unidirectional sync.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FtXA0rXE7wWv1s9lWXpUB%2F89c8394ecae512c8332629137caae364%20(1).png?alt=media&#x26;token=23ff5d7d-5d06-4e07-8352-8792e589b8f2" alt=""><figcaption></figcaption></figure>

1. Click **Apply** at the bottom right to submit your changes. Then, **Save** your integration.

{% hint style="info" %}
If you’re experiencing difficulties syncing attachments or have any other questions, please contact us at our [Support Center.](https://getint.io/help-center)
{% endhint %}

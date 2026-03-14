# Source: https://help.aikido.dev/getting-started/task-management-systems/advanced-functionalities/auto-close-linear-tasks-when-aikido-issues-are-resolved.md

# Auto-Close Linear Tasks When Aikido Issues Are Resolved / Ignored

### Use Case

When Aikido marks issues as **resolved** or **ignored**, you can sync this status with Linear to keep tasks automatically updated.

{% hint style="info" %}
Aikido checks every **8 hours** to detect and update resolved issues. Updates are **not instantaneous**, so some delay is expected between resolution and task closure.
{% endhint %}

### **Setup**

**Step 1.** Go to your [**Task Tracker Integration Settings**](https://app.aikido.dev/settings/integrations/tasktracker) in the Aikido dashboard.

**Step 2.** In the **Advanced** section, enable **Autoclose Tasks**.<br>

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F6GihPWkrzcLQA0cJummE%2Fimage.png?alt=media&#x26;token=cefde62b-590f-43e4-bfee-327c8f143dd5" alt=""><figcaption></figcaption></figure>

**Step 3.** Set the corresponding **completion status** that you are using in Linear (e.g., “Done”).

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FKicmVqVs90BPsRWcQ4yM%2Fimage.png?alt=media&#x26;token=54736314-987a-431e-aadf-d400b4c18b5c" alt=""><figcaption></figcaption></figure>

**Step 4**. Hit Save in the top right

### **Troubleshoot**

* For **Linear**: if tasks don't move to “Done”, you may need to reauthorise the integration.

  * Go to **Manage Integration**
  * Click the **three dots**
  * Select **Re-authorize**

  <figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F0XgLKpuvrpVM37Fi6KQu%2Fimage.png?alt=media&#x26;token=4abe09c8-dae3-4185-98ac-36aef13d47e4" alt="" width="375"><figcaption></figcaption></figure>

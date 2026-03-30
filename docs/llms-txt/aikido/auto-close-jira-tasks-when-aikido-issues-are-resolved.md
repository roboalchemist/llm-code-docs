# Source: https://help.aikido.dev/getting-started/task-management-systems/advanced-functionalities/auto-close-jira-tasks-when-aikido-issues-are-resolved.md

# Auto-Close Jira Tasks When Aikido Issues Are Resolved / Ignored

### Use Case

When Aikido marks issues as **resolved** or **ignored**, you can sync this status with Jira to keep tasks automatically updated.

{% hint style="info" %}
Aikido checks every **8 hours** to detect and update resolved issues. Updates are **not instantaneous**, so some delay is expected between resolution and task closure.
{% endhint %}

### **Setup**

**Step 1.** Go to your [**Task Tracker Integration Settings**](https://app.aikido.dev/settings/integrations/tasktracker) in the Aikido dashboard.

**Step 2.** In the **Advanced** section, enable **Autoclose Tasks**.<br>

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FZghryJHTDXnSI6jBjvgD%2Fimage.png?alt=media&#x26;token=4c126c7c-1ce0-47ea-99fa-c8bd58e081ad" alt=""><figcaption></figcaption></figure>

**Step 3.** Set the corresponding **completion status** that you are using in Jira (e.g., “Done”).

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FPXjzHAKJ8BOi96GX7OLn%2Fimage.png?alt=media&#x26;token=fa30e75d-c868-4022-a87a-950a38a1e1d2" alt=""><figcaption></figcaption></figure>

**Step 4**. Hit Save Settings in the top right

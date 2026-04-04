# Source: https://docs.debricked.com/product/vulnerability-management/set-a-review-status.md

# Set a review status

For each alerted vulnerability, you can assign a status. You can choose to mark the vulnerability as unaffected, or vulnerable or you can choose to snooze or pause. All the vulnerabilities have a default status of unexamined until you decide to change it.

To set a review status:

1. Go to your **Repositories** from the left side menu.
2. Click a specific repository.
3. In the **Repository** view, click a specific CVE.
4. In the **Actions** section, choose one of the following available status choices:

* **Unaffected:** You can mark the CVE as Unaffected to ignore the vulnerability.
* **Vulnerable:** You can flag a CVE as Vulnerable to ensure it is on your radar.
* **Pause rule triggering:** You can wait to take action and pause automation triggering. You can either Snooze or Pause. When you snooze the CVE, you can define a period of time (1 week, 1 month and so on). When you pause the CVE, you can pause until a new fix is available. Pausing is only supported for the Github app.
* **Unexamined:** This is the default status before choosing another one.

### **Use automation to set a review status**

The automation engine can help you remove manual work, by setting review statuses. You can use automations to flag CVEs as unaffected or vulnerable. For example, you can create a rule that when a dependency contains a vulnerability where CVSS is low (0.0-3.9), then mark the vulnerabilities as *unaffected*.&#x20;

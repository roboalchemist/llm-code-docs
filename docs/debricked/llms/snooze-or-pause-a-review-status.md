# Source: https://docs.debricked.com/product/vulnerability-management/set-a-review-status/snooze-or-pause-a-review-status.md

# Snooze or pause a review status

You can flag a vulnerability as snoozed for a set amount of time. By doing so, the specific vulnerability will not be triggered in any automation rules for the specific repository. After the chosen snooze duration expires, your automation rules will again take the before snoozed vulnerability into account and respective actions will be triggered again.&#x20;

{% hint style="info" %}
This could result in unnoticed security issues because the vulnerability will not show up in your existing automations. Therefore, use this feature only if you need to and are aware of the consequences.
{% endhint %}

### **Snooze a vulnerability for a set amount of time** <a href="#howdoisnoozeavulnerabilityforasetamountoftime" id="howdoisnoozeavulnerabilityforasetamountoftime"></a>

To snooze a vulnerability:

1. Go to the vulnerability page.
2. Click **Pause rule triggering** in the **Action** section.

<figure><img src="https://1696666310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FXrChfOBHOF0MXs8qC14m%2Fuploads%2FDk1d9sBQoSFy2AICzxmw%2FVulnerability_Action.png?alt=media&#x26;token=5fb26efd-23aa-424f-856c-e251119be036" alt=""><figcaption></figcaption></figure>

3. Select **Snooze for a set time period** in the newly opened dialog and select your desired snooze period.

<figure><img src="https://1696666310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FXrChfOBHOF0MXs8qC14m%2Fuploads%2F1iKQjAphzqAUoJbUyWIG%2FVulnerability_Action_Pause.png?alt=media&#x26;token=8eaaf4d9-5b1b-4b74-8568-d03fed9c83d5" alt="" width="375"><figcaption></figcaption></figure>

4. Click **Save** to confirm your selection and snooze the automation rules for the vulnerability.

You can see the activated snooze being shown as review status under **Action**. Snoozing the vulnerability is also reflected in the **Activity** section at the bottom of the page.

{% hint style="info" %}
Note: Setting the vulnerability to "snoozed" is only available on a per-repository basis. If you want to snooze the same vulnerability for another repository, you should repeat the same steps for that one.
{% endhint %}

Though any user is able to choose "snoozed" as review status by default, as an admin, you can disable this feature for all users in your company.&#x20;

### **Manually remove a snooze from a vulnerability** <a href="#howdoimanuallyremoveasnoozefromavulnerability" id="howdoimanuallyremoveasnoozefromavulnerability"></a>

You can manually stop snoozing a vulnerability at any time before it resumes automatically:

1. Go to the vulnerability you want to resume.
2. Click **Snoozed for (time)** and confirm that you want to stop snoozing the vulnerability in the displayed dialog. Note that this will enable automation rules to be triggered for this vulnerability again.

<figure><img src="https://1696666310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FXrChfOBHOF0MXs8qC14m%2Fuploads%2F0zewkLQ08p0w3vLqKMNz%2FVulnerability_Action_Snoozed.png?alt=media&#x26;token=eb324af1-a3c4-48c6-9e16-d7459fe9f3a2" alt=""><figcaption></figcaption></figure>

### **Pause review status** <a href="#howdoipausethereviewstatus" id="howdoipausethereviewstatus"></a>

You can flag a vulnerability as paused in a specific repository. The vulnerability will stay paused until a fix is found, if applied, resolves the vulnerability in your repository. In that case, the paused status will be removed automatically, and the vulnerability resumes to being unexamined.

Keep in mind that the pause could potentially be indefinite when a fix is never found. It is recommended to choose a maximum pause time when setting this review status. If the pause duration expires before the fix is found, your automation rules will resume taking the vulnerability into account. This is similarl to how snoozing a vulnerability works.

### **Pause a vulnerability until a fix is available** <a href="#howdoipauseavulnerabilityuntilafixisavailable" id="howdoipauseavulnerabilityuntilafixisavailable"></a>

To pause a vulnerability until a fix is available:

1. Go to the desired repository and vulnerability to pause.&#x20;
2. Select **Pause rule triggering** in the **Action** section.
3. Select **Pause until a fix is available** in the opening dialog and choose an appropriate max pause time.
4. Click **Save** to confirm your selection and pause automation rules for the vulnerability.

&#x20;You can see the activated pause being shown as review status under **Action**. Pausing the vulnerability is also reflected in the **Activity** section at the bottom of the page.

{% hint style="info" %}
Note that setting the vulnerability to "paused until a fix" is available does so only for the specific repository. If you want to pause the same vulnerability for another repository, you will have to repeat the same steps for that one.
{% endhint %}

### **Manually remove a pause until a fix is available from a vulnerability** <a href="#howdoimanuallyremoveapauseuntilafixisavailablefromavulnerability" id="howdoimanuallyremoveapauseuntilafixisavailablefromavulnerability"></a>

You can manually stop pausing a vulnerability at any time before a fix is found or the max pause time has expired.&#x20;

To manually remove a pause:

1. Go to the vulnerability you want to resume.
2. Click **Paused until fix** and confirm that you want to stop pausing the vulnerability in the displayed dialog. Be aware that this will enable automation rules to be triggered for this vulnerability again.

# Source: https://docs.bugbug.io/collaboration/alerts.md

# Alerts

By default, BugBug is sending email notifications about [scheduled runs](https://docs.bugbug.io/running-tests/schedules) to all members of your [organization](https://docs.bugbug.io/collaboration/organization-settings). This makes sure that as soon as your app is not working as it should you will get an email alert.

You can change this rule on the Alerts page:

* when people get notifications
* who will receive them

You can also send additional notifications to email addresses who are not members of your organization, for example, clients or colleagues.&#x20;

{% hint style="info" %}
Alerts are configured **per project**, each project has independent settings.
{% endhint %}

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FCnjTrZaAAAWBqgB6qs8h%2F1emptyScreen.png?alt=media&#x26;token=b7a7f8d7-dc6b-4e61-a32a-fc12c750be0c" alt=""><figcaption><p>Blank screen without alerts</p></figcaption></figure>

## Adding a new alert to your project&#x20;

By clicking on the "**New alert**" button you can set up alerts related to a specific project.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FXQHOlnygRe59osvk6d3A%2F1newAlertbtn.png?alt=media&#x26;token=0f0b190f-4256-4fc6-9c1a-3180adf70842" alt=""><figcaption><p>Blank screen without alerts</p></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FhoUAb20wDeONyXYFslMo%2F1setupAnAlertscrn.png?alt=media&#x26;token=e41ef818-ce6a-4d7e-9896-a0a9a32ea09c" alt=""><figcaption><p>Alerts setup modal</p></figcaption></figure>

### Choose when the alerts should be sent

You can easily select when the alerts should be triggered by clicking and expanding the drop-down list in the "*When*" section.&#x20;

Available options:

* Test started
* Test finished
* Suite started
* Suite finished
* Schedule started
* Schedule finished

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FI2zPNGyHQ1Odw38ePuAP%2F1whenAlert.png?alt=media&#x26;token=d62493bf-fadf-473a-b72a-fa198a1a7905" alt=""><figcaption><p>List of available conditions</p></figcaption></figure>

#### Along with other conditions, such as:

* **Which suites/tests/schedules** - allows you to select various suites, tests, or schedules.
* **Results -** "*Passed*" and "*Failed*" are selected by default, but you can also choose a third option - "*BugBug internal erro*r" that will send an alert when, for example, some technical issues occur on BugBug's side that could impact the test run results.&#x20;
* **Methods&#x20;*****-*** contains "*Local browser*" and "*Cloud*" options to be selected, but this is dependent on your subscription plan settings.
* **Profile** *- a* profile that was used in selected runs.
* **Run by** *-* define what causes the run. Select between: "*Manually by a use*r", "*API*", or "*Automatically by scheduler*".
* **Frequency** *-* define when you want to get an alert. Select between:
  * "*Every time*" - get an alert always when the trigger with the given parameters occurs.
  * "*Only once when the result changes*" - reduce the noise. Don't get alerts if the result is the same as the previous one. For example, if the result is failed 5 times in a row, you will only get an alert the first time.

{% hint style="info" %}
Remember that these fields will change based on what type of event you will select in the "When" section from the listed options.
{% endhint %}

### Set what type of action should be executed\*

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FSCKyzJ58BjMYlxoA32Rg%2FZrzut%20ekranu%202024-03-20%20o%2014.10.48.png?alt=media&#x26;token=57e0ff0b-d223-4fe1-a1d7-c2079ba9a246" alt=""><figcaption></figcaption></figure>

Currently you can choose one of those options:

* [Send email notification](https://docs.bugbug.io/collaboration/alerts/sending-email-notification)
* [Send webhook](https://docs.bugbug.io/collaboration/alerts/sending-webhook)
* [Send Slack message](https://docs.bugbug.io/collaboration/alerts/sending-slack-message)
* [Send Teams message](https://docs.bugbug.io/collaboration/alerts/sending-teams-message)

{% hint style="info" %}
**\*Note:** More will come soon, such as: creating a Jira ticket and sending a notification to other team communicators like Discord, etc.
{% endhint %}

***

## Alerts list and management

Having all the data filled you can add your alert by clicking on the "**Create alert**" button to see it on the list.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FYqX2RI8EFfJ1HYdCrppJ%2F1newAlertAdded.png?alt=media&#x26;token=031c36df-847a-4a2a-baea-729193f20c66" alt=""><figcaption></figcaption></figure>

### Manage your existing alerts

From this level, you can easily manage your listed alerts. From enabling or disabling to duplication them with a few clicks. Editing is also possible - just simply click on a listed alert's box.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FKtVAvwDRsl66HvJkVwgm%2F1multiAlerts.png?alt=media&#x26;token=d2fe503c-cf37-498f-a189-d04bf6556393" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Click on the toggle button to enable/disable each alert.
{% endhint %}

Click on the "**...**" to display the drop-down menu and select between available options:

* Edit
* Duplicate
* Delete

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FONemII4QgmeFWuFZHr2T%2F1moreOptions.png?alt=media&#x26;token=c42e8d02-627a-4c9d-a29f-0c6a28a403c9" alt=""><figcaption></figcaption></figure>

If some alerts aren't needed anymore and you want to tidy your list, just simply delete the selected item.

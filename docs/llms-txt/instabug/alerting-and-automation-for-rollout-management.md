# Source: https://docs.instabug.com/product-guides-and-integrations/product-guides/automation-and-workflows/alerts-and-rules/alerting-and-automation-for-rollout-management.md

# Alerting and Automation for Rollout Management

Luciq helps you automate the entire rollout process, as well as extra automation capabilities that you can utilize to save time and eliminate a handful of manual tasks.

**Workflow Automation Examples**:

* Keep your team updated with the status of the rollout.
* Create alerts to get your team notified about any updates.
* Triage and manage your rollout without the need to use multiple tools.

### Create your rules

To get started with rollout management workflow automation, hover the the left navigation menu and click on “Alerts & Rules”

<figure><img src="https://files.readme.io/4cc11d6cf4d272bf6d5300eb2f60c45c362cdd1828b315b2c14a73550db12432-product-guides-crash-reporting-alerts-1.png" alt="2874"><figcaption><p><em>Go to the Alerts &#x26; Rules page from the Luciq menu</em></p></figcaption></figure>

You can view a list of all created rules or performance metrics, use the filters to view only rules for bugs, crashes, performance metrics or release rollout, and click on “Create” to get started.

<figure><img src="https://files.readme.io/5ab761f026721fafe636b69905bafb8a7ecc5cddbcb457979c07f330773feea4-product-guides-crash-reporting-alerts-2.png" alt="2874"><figcaption><p><em>Click on "Create"</em></p></figcaption></figure>

### Rollout Management Alert

Select “Release Rollout” from the dropdown menu under the “For”.

<figure><img src="https://files.readme.io/3797a44dcb8dcd5690e953d8872f4666820a3a34a43f4a8978208c2e77d736f0-product-guides-crash-reporting-alerts-3.png" alt="2874"><figcaption><p><em>Select "Crashes"</em></p></figcaption></figure>

#### Triggers

Then you need to select a trigger; below is a list of all available triggers:

* **Health Metrics**:
  * ***Apdex***: Halt/Pause or Release the Rollout process based on your application's apdex score within a period of time for a specific or all app versions.
  * ***Crash-Free Sessions***: Halt/Pause or Release the Rollout process based on the Crash-Free percentage within a period of time for a specific or all app versions.
* **Rollout Progress**:
  * ***Rollout Status Change***: Get notified whenever the rollout status is changed for a specific or all app versions.
  * ***Rollout Percentage Change***: Get notified whenever the rollout percentage is changed for a specific or all app versions.
  * ***Daily Rollout Summary***: Get notified if the daily rollout summary is changed for a specific or all app versions.

<figure><img src="https://files.readme.io/c2da648ac7e464b8b81957bd69d7b742eb01dbb07d3b6e98246f5524ad3df3f2-product-guides-alerting-and-automation-for-rollout-management-4.png" alt="Choose a Trigger"><figcaption><p><em>Choose a Trigger</em></p></figcaption></figure>

#### Conditions

After selecting the trigger, you can select a set of conditions that need to be met for the rule to be triggered.

**Below is a list of all available conditions**:

* ***Version Adoption Percentage***: Check if the version adoption percentage is greater or less than a specified percentage.
* ***Version Rollout Percentage***: Check if the version rollout percentage is greater or less than a specified percentage.
* ***Rollout Status***: The status of the rollout is one of the following: Started, Halted/Paused, Resumed, or Completed.

You can add as many conditions as you see fit. You can also choose to “AND” or “OR” the selected conditions.

<figure><img src="https://files.readme.io/d387df3f520adb726c2ab7959e89879327e9eab7d5bdfde3c35792ab078bd283-product-guides-alerting-and-automation-for-rollout-management-5.png" alt="Choose one of the conditions"><figcaption><p><em>Choose one of the conditions</em></p></figcaption></figure>

#### Alerting channels

The last thing you need to do is specify the actions you want to automate using this rule. There are various actions available:

* ***Change status to***: Change the status of the rollout to one of Halt/Pause & Release to All.
* ***Send email to***: Send an email to a dashboard member(s).
* ***Forward it to***: Get notified on Slack if you have an integration set up on your dashboard.

<figure><img src="https://files.readme.io/5813222806c6e5c276456fdf0cd4490df1ce1309a40b4791682277d77afae04f-product-guides-alerting-and-automation-for-rollout-management-6.png" alt="Choose an action to be performed"><figcaption><p><em>Choose an action to be performed</em></p></figcaption></figure>

### Use Cases

Now let's discover different scenarios for workflow automation that help track your app's health, like Apdex and Crash-Free Sessions, if they reach a specific threshold to get notified and how you can use the rules to achieve this:

***Scenario A***:

You have a version being rolled out to your users, and if you're worried it might cause crashes, you can set up an automation that would automatically pause the rollout if the crash-free sessions rate falls below 97% in a 24-hour window to stop the issue from affecting any other customers while you work on a fix.

<figure><img src="https://files.readme.io/dffe46f18968a8774ed84209c59ec8ac897a3c7eefe3c5b1e4bf9659075f5463-product-guides-alerting-and-automation-for-rollout-management-1.png" alt=""><figcaption></figcaption></figure>

***Scenario B***:\
You can set an automation that keeps track of the crash-free sessions for your application, and if a release is performing as well as you expect (e.g., not facing any crashes), you can automatically have it released to all users to quickly increase its adoption.

<figure><img src="https://files.readme.io/4e9295cd41719642ee2caef1cf684f691585874b256946e904a3d1a8b45a78c0-product-guides-alerting-and-automation-for-rollout-management-4.png" alt=""><figcaption></figcaption></figure>

***Scenario C***:

You can stay up to date whenever the rollout status changes to either Started, Halted / Paused, Resumed, or Completed. This can be done by setting up a Slack integration and getting notified on your preferred channel.

<figure><img src="https://files.readme.io/1ad18c065c7305658dd2ffb938274581d1266be9c83f3291fded70083b9df945-product-guides-alerting-and-automation-for-rollout-management-2.png" alt=""><figcaption></figcaption></figure>

***Scenario D***:

You can get a daily update on your release rollout health and progress by sending an e-mail to all team members who are on the dashboard or a selection of them upon your preference.

<figure><img src="https://files.readme.io/12ab02a3b96335cea5a066bb1ad4c970908be6c781b517458680989db1a08f01-product-guides-alerting-and-automation-for-rollout-management-3.png" alt=""><figcaption></figcaption></figure>

If you need further assistance in setting up rules, please feel free to contact our support team.

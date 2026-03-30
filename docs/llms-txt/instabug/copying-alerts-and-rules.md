# Source: https://docs.instabug.com/product-guides-and-integrations/product-guides/automation-and-workflows/alerts-and-rules/copying-alerts-and-rules.md

# Copying Alerts & Rules

Luciq enables you to seamlessly reuse existing alerts and rules across your applications and environments on Luciq. This feature helps you:

* Reduce setup time for new apps or environments
* Preserve consistent alerts & rules across your applications

Instead of manually recreating conditions, triggers, and actions, you can import and adapt rules with just a few clicks.

### When to Use This Feature?

Use import when:

* Launching a new app or environment (e.g., staging → production)
* Scaling your mobile stack across multiple platforms (iOS ↔ Android)
* Standardizing alerting across development squads

### How to Import Alerts & Rules

#### 1) Open Alerts & Rules

* Navigate to your app → **Alerts & rules** page
* Select **Import alerts & rules**

  <figure><img src="https://files.readme.io/0bc8a1bde63dc0187906bddc2b12ddc54601e0aa6e286ae68d4802d78a81b3b5-image.png" alt=""><figcaption></figcaption></figure>

#### 2) Select Source App and Environment

{% hint style="info" %}
You can only import user defined alerts created by your team members, not the predefined alerts created by Luciq
{% endhint %}

You will see your available apps and environments, each showing the number of alerts available to import.

* Search by app or environment name
* Select the application environment you want to import alerts from
* Environments with **0 user-defined alerts** appear disabled

  <figure><img src="https://files.readme.io/a3226330af97a6f1c67094e6883a7639aff7b407dec190c76aa0d58add0a45e2-image.png" alt=""><figcaption></figcaption></figure>

#### 3) Choose Alerts & Rules to Import

{% hint style="info" %}
Some alerts and rules could have some application or environment specific configuration, These alerts would have a tag “Needs update” to highlight that you need to update the configuration of the alert post importing to match it with your current application or environment attributes.
{% endhint %}

On the selection screen:

* Select specific alerts, or choose **All alerts & rules**
* Alerts with missing or app-specific fields display a **Needs update** label
* Click **Import alerts & rules** to complete the import.

  <figure><img src="https://files.readme.io/e8eae752b35994450d227887018617fcb16715e9dbf956cf0941a752eb621b5b-image.png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Some rules may include app-specific logic. These are still imported but require updates to activate.
{% endhint %}

#### Unsupported Import Cases

Rules marked **Not supported** cannot be imported due to incompatible configuration types. These remain visible during import with an explanation tooltip.

Example: You cannot import an OOM Alert to an Android app because OOMs are not supported on Android.

<figure><img src="https://files.readme.io/36bb7f627d4eaeffcad6c7bcee3bb4f63348d8f9962837ed7795eee87e88b560-image.png" alt=""><figcaption></figcaption></figure>

#### After Import: Activation & Updating Settings

Imported alerts that need updates will remain inactive until configured.

You'll see:

* A banner: *“You have inactive alerts & rules that require configuration updates…”*
* A **Review alerts & rules** button
* Each alert marked as `Needs update`

<figure><img src="https://files.readme.io/9bf0901b655bcc4d768344bd059f2d31c62b03d75748ebe1ff8a17570d4b15c7-image.png" alt=""><figcaption></figcaption></figure>

#### Application specific configurations

If any of the following conditions exist in the alert you are importing, the alert would always require an update of these fields after import to activate the alert.

* Integrations
* Teams
* Members
* App version
* Path/Package
* Filename
* Trace name
* Current view
* Assignee
* User attributes
* Feature flags
* Flow name

#### Updating Alerts

Click **Review alerts & rules** → a right-side drawer opens showing each alert needing attention.

For each alert, select **Update** to open the editing screen. Fix highlighted fields, then click **Save**. Once the configuration is valid, the alert becomes active.

Common updates include:

* Adding an integration or selecting one that exists in the new environment
* Selecting an app version or adjusting version logic
* Selecting recipients or teams
* Replacing invalid fields or actions that no longer apply

{% hint style="info" %}
Alerts cannot be saved until all required fields are complete. This prevents accidental activation with incomplete settings.
{% endhint %}

![](https://files.readme.io/65150b7b2dcc1244aef13b02dbbf91f92e14c103859a75c3e5f8e74d396b1529-image.png)![](https://files.readme.io/2814e2300a76c2fe0867a52d2a295a9d5f930e9011833a9539d56cd5fc163479-image.png)<br>

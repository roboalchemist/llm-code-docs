# Source: https://docs.getint.io/getting-started-with-the-platform/starting-the-free-trial-and-accessing-the-getint-app/selecting-the-correct-app-per-license.md

# Selecting the Correct App per License

When installing an app from the [**Atlassian Marketplace**](https://marketplace.atlassian.com/vendors/1218845/getint-integrations-jira-azure-devops-servicenow-salesforce-asana-monday-clickup-gitlab-and-others), you may encounter issues if the installation is not performed using the correct app, especially when initiating the appropriate trial or license. Following the steps below will ensure a smooth installation and help avoid common errors such as licensing mismatches or failed installations.

{% hint style="warning" %}
If the correct app is not installed, you will encounter an **Invalid Jira license** error, which prevents any work items from being synchronized.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F7mQpQDzyWm4GkxfrUWbW%2FInstalling%20the%20correct%20app.png?alt=media&#x26;token=e2d4198d-4e4e-4994-92ae-753c07f19813" alt=""><figcaption><p>On the left, you can see that different apps are available depending on the connectors you want to integrate</p></figcaption></figure>

### Troubleshooting the Invalid Jira License Error <a href="#troubleshooting-the-invalid-jira-license-error" id="troubleshooting-the-invalid-jira-license-error"></a>

After you create an integration, if the runs begin to fail, you'll see this message in the run logs. During this period, the integration will not sync any work items.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fvanv2XduX0uIu4f6hxqk%2FInvalid%20jira%20license%20error.png?alt=media&#x26;token=dbaabe25-bb47-4fa8-a568-3938e00dc5e5" alt=""><figcaption></figcaption></figure>

A warning icon will also appear beneath the license column to indicate an issue with your license.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FzgIV0gotkQZmPU5qYtQj%2FWarning%20icon%20below%20the%20License%20column.png?alt=media&#x26;token=ef4c30b6-de73-449b-927d-3cc1fa045d6e" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
We’re using the Jira Airtable app as an example to build a ServiceNow integration and intentionally force a failure, but this message will appear in any app if you’re using the wrong connector or if your license has expired.
{% endhint %}

To resolve this issue, first assess what integration you would like to build:

1. If you are integrating with **Jira**, first verify if you have an active trial for your integration:

* **Jira Cloud**: Go to the **Subscriptions** section in your billing console and check if your subscription is active.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fpa6uKuJWqnzYLbUgpe4a%2FCheck%20your%20subscription%20in%20the%20billing%20console.png?alt=media&#x26;token=7127bc7e-19a2-424c-b214-c8c60433695e" alt=""><figcaption></figcaption></figure>

* **Jira DC**: Go to the **Manage apps** section and locate the Getint app. Click on it to view more information, where all app details will be available.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FzKcWxMCwfK51PsHlPdBZ%2FWhere%20to%20check%20Jira%20DC%20license.png?alt=media&#x26;token=41eb3c5d-9e7d-41a7-adb0-7fbdc9610445" alt=""><figcaption></figcaption></figure>

1. If your trial is active, go to the **Apps** section and select the appropriate app for your integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Ffyop1YiBMlweNH3KcIIZ%2FSelecting%20the%20correct%20app%20depending%20on%20the%20tools%20you%20want%20to%20integrate.png?alt=media&#x26;token=63c10925-b537-48a3-b489-d698610f683c" alt=""><figcaption></figcaption></figure>

1. If you don’t have an active trial, go to the Atlassian Marketplace and search for **Getint**. All our apps will be listed there. Select the app you need for your integration (in this example, we’ll use ServiceNow).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FMnR4mv4Nt0mAbN8QeYAI%2FSearching%20for%20the%20ServiceNow%20integration%20app%20in%20the%20marketplace.png?alt=media&#x26;token=76027433-bbb0-4175-9f39-223867b66129" alt=""><figcaption></figcaption></figure>

1. Activate the trial if you still don’t have it:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FlaJZolvf6mCDUYEyuzAo%2FActivate%20trial%20for%20ServiceNow%20app.png?alt=media&#x26;token=c4201b04-99fb-420b-b9f8-ec0fcfabd7af" alt=""><figcaption></figcaption></figure>

1. Go back to your **Apps**, and launch the Getint app.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F8dshuVFVwoBbamDsWUkM%2FLaunching%20the%20ServiceNow%20app.png?alt=media&#x26;token=3a162979-63be-47f2-9583-9a245a329753" alt=""><figcaption></figcaption></figure>

1. You should now be able to build your integrations as needed.

{% hint style="warning" %}
Note: If you are using our app to integrate (e.g., Jira-ServiceNow) and would now like to scale to integrate ServiceNow with DevOps, we can generate a new license key that will enable this within the Jira app.

This additional license key must be purchased separately. For more information, please contact our [Support Center](https://getint.io/help-center).
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FmNmcgv7EiaNxX2LTkq5D%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=e3bc4f73-2bed-47ae-a7fa-139dd809c092" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

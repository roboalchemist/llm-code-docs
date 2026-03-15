# Source: https://docs.luciq.ai/product-guides-and-integrations/product-guides/crash-reporting/force-restarts.md

# Force Restarts

A Force Restart occurs when a user forcefully closes an app and immediately restarts it. The underlying frustration that prompts the user to restart the app often goes unnoticed by app developers, as it is not classified as a crash.

Luciq gives you visibility over Force Restarts, which are detected automatically. You can now detect these issues early on, and address them, so you can improve the app quality and retention.

### What does a Force Restart look like?

* User opened the App
* The App was very slow
* User closed the App and opened it again

### How can I see Force Restarts on the dashboard?

Force Restarts are captured by default. You can reach the Force Restarts section as shown in the screenshot below:

<figure><img src="https://files.readme.io/e2b3e20797f42269aa470059b8d2455c93865160a78f5676cf0f26eca2a83259-image.png" alt="" width="188"><figcaption></figcaption></figure>

Similar terminations are grouped together by screen, as shown in the below screenshot.

<figure><img src="https://files.readme.io/739b48c-Screen_Shot_2023-05-18_at_3.53.43_PM.png" alt="User Terminations grouped occurrences grouped together"><figcaption></figcaption></figure>

{% hint style="info" %}
Force Restarts are grouped by events that happened on the same screen.
{% endhint %}

### What data is available in a Force Restart:

* Patterns to highlight which subset of users has triggered the highest number of Force Restarts.
* Occurrences view, where you can view every occurrence of the frustrating experience and what has led to it.
* Occurrences include the following debugging data:
  * Metadata of the device
  * [Session Profiler ](https://app.gitbook.com/s/AM8wNfllcup3GnWJ1WtW/setup-luciq-for-ios/custom-settings/logs-and-profiling/session-profiler)to know the state of the device for the last 60 seconds before the Force Restart was triggered.
  * [Repro steps](https://app.gitbook.com/s/AM8wNfllcup3GnWJ1WtW/setup-luciq-for-ios/custom-settings/privacy-settings/repro-steps) which is a visual step by step reproduction of the session of the user, screen by screen and interaction by interaction on the app up until the user triggered the termination.
  * [Logs section ](https://app.gitbook.com/s/AM8wNfllcup3GnWJ1WtW/setup-luciq-for-ios/custom-settings/logs-and-profiling/report-logs)including console logs and network logs for all API calls that were made during the session.

Luciq's Force Restarts feature can be a critical tool for developers seeking to enhance their app's user experience. By notifying you of user frustrations in real-time, it provides you with the opportunity to address issues promptly, maintaining user satisfaction and improving app performance.

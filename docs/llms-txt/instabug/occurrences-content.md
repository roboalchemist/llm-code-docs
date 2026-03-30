# Source: https://docs.instabug.com/product-guides-and-integrations/product-guides/crash-reporting/occurrences-content.md

# Occurrences Content

When using Luciq [Crash Reporting](https://www.luciq.ai/product/crash-reporting), each occurrence comes with user attributes, user data, and attachments if available.

#### User Attributes

Default attributes as well as any custom user attributes that you set are automatically sent to your dashboard with all crash occurrences.

Default attributes listed in each crash occurrence include:

* Date and time of crash occurrence in UTC
* App version
* Device
* OS version
* App view
* Device location
* Session duration
* Locale
* Screen resolution
* Screen density

More details about how to set custom user attributes can be found [here](https://app.gitbook.com/s/AM8wNfllcup3GnWJ1WtW/setup-luciq-for-ios/custom-settings/user-identification/user-attributes).

<figure><img src="https://files.readme.io/6e6b41508f7679d50443a81b6e94b62e4c0f0aaf182e63617da83304838fe28f-ios-occurrences-content-1.png" alt="2161"><figcaption></figcaption></figure>

User attributes are listed in each occurrence page of all crash reports in your dashboard.

#### User Data

Custom data can be set and sent with each occurrence. To learn more about setting custom user data, check [here](https://app.gitbook.com/s/AM8wNfllcup3GnWJ1WtW/setup-luciq-for-ios/custom-settings/user-identification).

#### Attachments

Any custom files added by you can be sent with each occurrence.

<figure><img src="https://files.readme.io/152b5d6058614e8679c03a50c918f3fe2f687431c5a2174f43cf5d8a4672c0fd-ios-occurrences-content-2.png" alt=""><figcaption></figcaption></figure>

### Repro Steps

Repro Steps help you reproduce a crash by displaying your users' actions in each view of your app. With each view, you will find a list of actions that tell you exactly what the user did in that view. More details can be found [here](https://app.gitbook.com/s/AM8wNfllcup3GnWJ1WtW/setup-luciq-for-ios/custom-settings/privacy-settings/repro-steps).

This is enabled by default depending on your plan.

<figure><img src="https://files.readme.io/194e1be5f6df0bc862324148fa47998b618cde6f40b257c64afc8e4e658b8f11-ios-occurrences-content-3.png" alt=""><figcaption></figcaption></figure>

### Session Profiler

With each crash occurrence, you'll receive a detailed environment profile covering the last 60 seconds before the report was sent. This Session Profiler includes device data like memory load and battery state. This is enabled by default depending on your plan. More details about the information contained in the Session Profiler can be found [here](https://app.gitbook.com/s/AM8wNfllcup3GnWJ1WtW/setup-luciq-for-ios/custom-settings/logs-and-profiling/session-profiler).

<figure><img src="https://files.readme.io/faa62b52223161f5ee3eda64204c9dabbcc5923c41108e15960fa9e3455ab9df-ios-occurrences-content-4.png" alt="2161"><figcaption></figcaption></figure>

This is where the Session Profiler is located in each crash occurrence page.

### Logs

A whole host of logs are sent with every crash occurrence. These logs include:

* **Console Logs:** Default logs that are printed to the console when the application is running.
* **Luciq Logs:** Logs with different verbosity levels that you can add manually.
* **User Steps:** Every step the user has taken in the form of log entries.
* **Repro Steps:** Visual user steps prior to the crash occurrence in the form of images and GIFs.
* **Network Logs:** A log of each network request.
* **User Events:** A manual log of actions that a user has taken.

More details regarding logging can be found [here](https://app.gitbook.com/s/AM8wNfllcup3GnWJ1WtW/setup-luciq-for-ios/custom-settings/logs-and-profiling/report-logs). Different log types are enabled depending on your plan.

<figure><img src="https://files.readme.io/8e2a7424ee3aa2b95c319b7b5f65e4ef2fee57dbd44efd508b48d86b0c6832a8-ios-occurrences-content-5.png" alt="2161"><figcaption></figcaption></figure>

An example of the expanded logs view in the Luciq dashboard.

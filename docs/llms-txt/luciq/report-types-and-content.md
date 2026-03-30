# Source: https://docs.luciq.ai/product-guides-and-integrations/product-guides/bug-reporting/report-types-and-content.md

# Report Types & Content

### Report Types

There are three different types of reports that, while function similarly for the end-user, appear with different types on the dashboard in order to easily separate between incoming issues. All three types will reach your dashboard with the same amount of information and can be filtered so that you can look at specific types only.

![](https://files.readme.io/22284fb638da33f2aa76fb1016bc0a270d3d3151bc25a41567187c29816caaaf-ios-bug-report-content-3.png)![](https://files.readme.io/74bb70bbd5249226c4da54f0f64657be6ef551d2b01d64ea0682ef78482ca8a3-ios-bug-report-content-1.png)

#### Bug

When the user selects "Report a bug" from the prompt options, the sent report will appear with type Bug. This type of report is primarily meant for reporting bugs that were found in the application.

![](https://files.readme.io/77d63c1c3630513dd2235948e2d69663c62c28052b6138aec999eeb6186404cc-ios-bug-report-content-4.png)

#### Improvement

Selecting "Suggest an improvement" from the prompt options will open the improvement suggestion form that your user can use to give you feedback on how you can improve the application in certain areas. These reports are shown on the dashboard with type "Improvement".

![](https://files.readme.io/32bd146e55deab039e9b03a795a5254a59fbb6497be74025c8d7691ead88537c-ios-bug-report-content-2.png)

#### Question

The third option in the prompt options is "Ask a question". The purpose behind this option is for users that don't quite have a bug or an idea for an improvement, but rather a question they'd like to ask you. These show on your dashboard with type "Question".

![](https://files.readme.io/a473ffbf6dc6c7d369013ac65d364d77f63f8888cbebfe228d0116a4fcda9223-ios-bug-report-content-5.png)

### Report Content

The reports (bugs, improvements, and questions) that your users submit from your app (from the Prompt Options) are sent to the bugs page of your dashboard.

With each report, you receive a plethora of details that will help you fix bugs and get more context about the comments you receive. Throughout this page, you will learn about all the information that comes in these reports, as well as any relevant APIs that you can use to customize the data that you receive, including:

* User Attributes
* Bug Report Fields
* Attachments
* Auto Screen Recording
* Logs
* Repro Steps
* Session Profiler
* View Hierarchy
* Tags

#### User Attributes

Default attributes as well as any custom user attributes that you set are automatically sent to your dashboard with all reports.

Default attributes listed in each report include:

* App version
* Device
* OS version
* App view
* Device location
* Session duration

More details about how to set custom user attributes can be found [here](https://app.gitbook.com/s/AM8wNfllcup3GnWJ1WtW/setup-luciq-for-ios/custom-settings/user-identification/user-attributes).

#### Bug Report Fields

The image below shows the first view that your users see when reporting a bug after [invoking the SDK](https://app.gitbook.com/s/AM8wNfllcup3GnWJ1WtW/setup-luciq-for-ios/setup-bug-reporting/showing-luciq).

<figure><img src="https://files.readme.io/d098bb0-3._MB_Compose_Report_Bug.png" alt="696"><figcaption><p><em>The first step of the bug reporting flow that your app users experience.</em></p></figcaption></figure>

#### Email Address

By default, your users are required to enter a valid email address to submit a bug or feedback, You can also remove the email field from the UI completely.

### Attachments

Your users can submit two types of attachments with any report: default Luciq attachments (files that they can select from their device) and custom extra attachments (additional files that you can attach using code).

#### Luciq Attachments

When your app users invoke Luciq, the SDK automatically captures a screenshot of their current view. This is the default attachment that is sent with any report. Your users can annotate this screenshot by drawing on, magnifying, or blurring specific parts.

In addition, there are other attachment types that your users can choose to send with each report. All attachment types can be enabled or disabled.

The attachment options are:

* Extra screenshots
* Images from photo library
* Screen recording

  <figure><img src="https://files.readme.io/8d0025ed8991d209f36a38ef8470795daa2ae0f7a4adea4de5207512898a87d1-image.png" alt=""><figcaption></figcaption></figure>

All attachment options are enabled by default if they are available in your current **plan**.

#### Auto Screen Recording \[Beta]

{% hint style="info" %}

#### Used for Internal Testing

The main purpose behind this feature is to specifically use it for internal testing rather than on production.
{% endhint %}

You can also automatically capture a screen recording of your app up to the last 30 seconds before a report is sent. **By default, this is disabled**. **Your users will also be prompted once the recording starts at the beginning of the session and will have the ability to remove the video from the attachments when sending the report.** The auto screen recording attachment counts towards the limit of 4 attachments in total.

<figure><img src="https://files.readme.io/8d0025ed8991d209f36a38ef8470795daa2ae0f7a4adea4de5207512898a87d1-image.png" alt=""><figcaption></figcaption></figure>

A whole host of logs are sent with every report. These logs include:

* **Console Logs:** Default logs that are printed to the console when the application is running.
* **Luciq Logs:** Logs with different verbosity levels that you can add manually.
* **User Steps:** Every step the user has taken in the form of log entries.
* **Repro Steps:** User steps prior to the bug report grouped by view.
* **Network Logs:** A log of each network request.
* **User Events:** A manual log of actions that a user has taken.

More details regarding logging can be found [here](https://app.gitbook.com/s/AM8wNfllcup3GnWJ1WtW/setup-luciq-for-ios/custom-settings/logs-and-profiling/report-logs). Different log types are enabled depending on your plan.

<figure><img src="https://files.readme.io/0ed473dbae395f24482b2ab6a5236d0253b1b694577a531a43ee6f2d25ebb52e-image.png" alt="An example of the expanded logs view in your dashboard."><figcaption></figcaption></figure>

### Repro Steps

Repro Steps help you reproduce a bug by displaying your users' actions in each view of your app. With each view, you will find a list of actions that tell you exactly what the user did in that view. More details can be found [here](https://app.gitbook.com/s/AM8wNfllcup3GnWJ1WtW/setup-luciq-for-ios/custom-settings/logs-and-profiling/repro-steps).

<figure><img src="https://files.readme.io/74bb70bbd5249226c4da54f0f64657be6ef551d2b01d64ea0682ef78482ca8a3-ios-bug-report-content-1.png" alt=""><figcaption></figcaption></figure>

### Session Profiler

With each report, you'll receive a detailed environment profile covering the last 60 seconds before a bug or feedback was submitted. This Session Profiler includes device data like memory load and battery state. More details about the information contained in the Session Profiler can be found [here](https://app.gitbook.com/s/AM8wNfllcup3GnWJ1WtW/setup-luciq-for-ios/custom-settings/logs-and-profiling/session-profiler).

<figure><img src="https://files.readme.io/173048747ef4f3084479afe370d4d120d9c7e8df9d5d0ec5becfae60f3d5197d-image.png" alt=""><figcaption></figcaption></figure>

#### View Hierarchy

With the View Hierarchy feature, you can visually inspect each layer in your app and see all the properties and constraints of each subview so you can spot errors at a glance.

This feature is critical for investigating UI bugs as it makes the process of finding the problem and fixing it faster and simpler. For example, if you receive a report that a certain UI view is missing, you can use View Hierarchy to easily discover if the missing view is hidden behind a higher layer, out of the parent view's bounds, or missing from the window.

Any editable text or text fields will automatically be replaced with asterisks.

<figure><img src="https://files.readme.io/b53ae9ed108d457d6122c178839f8c520ae242351931fa52a44536c60c953299-image.png" alt=""><figcaption></figcaption></figure>

#### Tags

You can add tags to the reports you receive to help you filter and triage bugs in your dashboard. More details regarding tags can be found [here](https://app.gitbook.com/s/AM8wNfllcup3GnWJ1WtW/setup-luciq-for-ios/custom-settings/user-identification/tags).

<figure><img src="https://files.readme.io/ae430d5077ce40cad8335f91b5f5252b1df2353eca4600a567e720acf57eff64-image.png" alt=""><figcaption></figcaption></figure>

<br>

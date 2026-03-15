# Source: https://docs.luciq.ai/product-guides-and-integrations/product-guides/crash-reporting/crash-report-content.md

# Crash Report Content

When using Luciq [Crash Reporting](https://www.luciq.ai/product/crash-reporting), each crash report reaches your dashboard with all the information you need to resolve it.

### Crash Overview

The crashes page in your dashboard lists all of your crash reports. When you select one, it opens the crash overview page where you can find more details about that crash.

<figure><img src="https://files.readme.io/f20e988eae17a929cb866dcf959a5411cd417c4704d9a32f33be55de983957ed-image.png" alt="An example of a crash report."><figcaption></figcaption></figure>

The graph above depicts the number of crashing sessions caused by this particular crash against the days of the previous month. Each line color represents a different app version.

Here are what the details in the crash page cover:

* **Exception & Crash Cause**: The main application frame that caused the crash.
* **Occurrences**: The number of times this crash occurred.
* **Affected Users**: The number of unique users that experienced this crash.
* **Occurrences over time**: Shows the number of occurrences over time for each app version.
* **Max App Version**: The highest version of the app this crash occurred on.
* **App Versions**: A breakdown of the crash occurrences by app version.
* **Devices**: A breakdown of the crash occurrences by device model.
* **OS version**: A breakdown of the crash occurrences by OS version.
* **App status**: A breakdown of the crash occurrences by background or foreground state.
* **Current view**: A breakdown of the crash occurrences by the app view they occurred on.
* **Experiments**: A breakdown of the crash occurrences by different feature flags (if any are specified).
* **User attributes**: A breakdown of the crash occurrences by custom user attributes (if any are specified).

#### Stack Trace

In each crash report, you can find the stack trace of the crash with the most important frames highlighted in blue. These highlighted frames are your application's frames. In order for these crashes to be readable, symbolication is required. More information on symbolication can be found [here](https://docs.luciq.ai/docs/ios-symbolication). A stack trace is captured and shown per app version within the crash itself.

<figure><img src="https://files.readme.io/f20e988eae17a929cb866dcf959a5411cd417c4704d9a32f33be55de983957ed-image.png" alt="An example of a crash report."><figcaption></figcaption></figure>

### Code Ownership

Sometimes, different stack traces are related to different teams within your organization. In an effort to allow for a more efficient method of assigning crash reports to the related teams, you can set up code ownership rules that use paths and filenames as conditions to allow for a more automated workflow.

You can use code ownership to check for specific paths and filenames, these are then compared against the first non-system frame in the stack trace. For more details on how to set up ownership rules, please check: [Team Ownership](https://docs.luciq.ai/product-guides-and-integrations/product-guides/automation-and-workflows/team-ownership)

### Crash Variants

**Crash Variants** highlight the different stacktrace paths within a single crash group. Instead of showing only one representative stacktrace per app version, Variants let you see all the distinct execution paths that can trigger the same crash. This helps your team uncover edge cases and debug faster.

Crash Variants are automatically grouped based on **stacktrace similarity.**

#### Where to Find Variants

On the **Crash List page**, you’ll see the number of variants created for each crash.

<figure><img src="https://files.readme.io/c72efb51394fb626cfa22764b16442ef656c9d06029382565dce17e39f86bbaa-image.png" alt=""><figcaption></figcaption></figure>

Selecting a specific variant from the details page will filter the entire page to show only that variant’s data.

1. Stacktrace for the variant
2. Percentage of occurrences for that variant
3. Variant Summary
4. Variant Patterns

<figure><img src="https://files.readme.io/44d3abe185f08c675eb5ef09147bb90fc2b28531f0c88177b1a2e7a93b54dc3e-ios-crash-report-content-2.png" alt=""><figcaption></figcaption></figure>

### Occurrences

Each crash has [occurrences](https://docs.luciq.ai/docs/ios-occurrences-content), a unique instance of that crash. With each occurrence, you can find extra details about every instance, such as [logs](https://docs.luciq.ai/docs/ios-logging), [Session Profiler](https://docs.luciq.ai/docs/ios-session-profiler), and [User Attributes](https://docs.luciq.ai/docs/ios-set-custom-data). You can go through these unique occurrences by clicking on the **Occurrences** button.

<figure><img src="https://files.readme.io/f20e988eae17a929cb866dcf959a5411cd417c4704d9a32f33be55de983957ed-image.png" alt="An example of a crash report."><figcaption></figcaption></figure>

### Tags

You can add tags to crash reports for filtering and analysis. More details regarding these tags can be found [here](https://app.gitbook.com/s/AM8wNfllcup3GnWJ1WtW/setup-luciq-for-ios/custom-settings/user-identification/tags).

<figure><img src="https://files.readme.io/dec0d638c3cc1f81eeaca204af2c22b80aa01b36ddcf3235ee7083ec80b06a4c-image.png" alt=""><figcaption></figcaption></figure>

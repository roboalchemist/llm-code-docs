# Source: https://docs.luciq.ai/android/set-up-luciq-for-android/set-up-crash-reporting/reporting-crashes-for-android/capturing-anrs-for-android.md

# Capturing ANRs For Android

At Luciq, we continuously improve our methods to provide the best tools for app performance monitoring. Our ANR (Application Not Responding) detection mechanism has evolved over time, resulting in two distinct versions: v1 and v2. Here’s a detailed comparison of both versions, along with their pros and cons, to help you understand which one suits your needs best.

<figure><img src="https://files.readme.io/15a0725-image-20240721-125739.png" alt="An ANR Modal"><figcaption></figcaption></figure>

#### ANR Detection v1

**Mechanism:**

* **Detection**: v1 captures ANRs by monitoring the main thread. If the main thread is blocked for 5 seconds, and the ANR dialog is displayed, an ANR is considered.
* **Reporting**: It takes a snapshot of the stack trace at runtime and sends it to the Luciq dashboard.
* **Coverage**: v1 captures all types of ANRs, whether the user dismisses the ANR modal or terminates the app.
* **Timeliness**: ANRs are sent in real-time.
* **Availability**: v1 is enabled by default.

**Pros:**

* **Comprehensive Coverage**: Captures all instances of the main thread being blocked for 5 seconds, providing a broad view of ANRs.
* **Real-Time Reporting**: Immediate notification and analysis of ANRs.

**Cons:**

* **Over-Reporting**: May capture transient or less severe ANRs that do not necessarily lead to app termination, potentially overwhelming with data.
* **Crash Without ANR Dialog**: If an ANR happens and the app crashes without showing an ANR dialog, no ANR will be detected.

#### ANR Detection v2

**Mechanism:**

* **Detection**: v2 reports ANRs only when the user receives an ANR and subsequently terminates the app. We do this by calling the ExitInfo System API.
* **Session Monitoring**: It listens in the next session to determine if the previous session was terminated due to an ANR.
* **Accuracy**: v2 is more accurate because the stack trace is provided by the system itself.

**Pros:**

* **Focused Reporting**: Captures fatal ANRs that result in app termination, filtering out less critical issues.
* **Comparable** Data: Since it mirrors the Play Console's method, it provides easily comparable reporting data.

**Cons:**

* **Selective Coverage**: Does not capture non-fatal ANRs, potentially missing out on issues that disrupt user experience but do not cause termination.
* **Delayed Reporting**: Data is sent in the next session, which may delay the analysis of ANR incidents.
* **OS Version Limitation**: Supports Android OS versions 30 and above. Older versions will fallback to ANRs v1.

### Summary: ANR Detection Comparison

| **Aspect**          | **ANR v1**                                                                                                                                                                                                                                      | **ANR v2**                                                                                                                                                                                                                              |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Detection Mechanism | Monitors main thread. If blocked for 5 seconds and ANR dialog is displayed, an ANR is considered.                                                                                                                                               | Reports ANRs only when the user receives an ANR and subsequently terminates the app. We do this by calling the ExitInfo System API.                                                                                                     |
| Reporting           | Takes a snapshot of the stack trace at runtime and sends it to the Luciq dashboard.                                                                                                                                                             | Data is sent in the next session.                                                                                                                                                                                                       |
| Timeliness          | Captures all types of ANRs, whether the user dismisses the ANR modal or terminates the app.                                                                                                                                                     | Captures fatal ANRs that result in app termination.                                                                                                                                                                                     |
| Coverage            | ANRs are sent in real-time.                                                                                                                                                                                                                     | Data is sent in the next session.                                                                                                                                                                                                       |
| Pros                | <p>Comprehensive Coverage: Captures all instances of the main thread being blocked for 5 seconds and showing the ANR dialog.</p><p>Real-Time Reporting: Immediate notification and analysis of ANRs.</p>                                        | <p>Focused Reporting: Captures fatal ANRs that result in app termination.</p><p>Comparable Data: Provides easily comparable reporting data.</p>                                                                                         |
| Cons                | <p>Over-Reporting: May capture transient or less severe ANRs that do not necessarily lead to app termination.</p><p>Crash Without ANR Dialog: If an ANR happens and the app crashes without showing an ANR dialog, no ANR will be detected.</p> | <p>Selective Coverage: Does not capture non-fatal ANRs.</p><p>Delayed Reporting: Data is sent in the next session.</p><p>OS Version Limitation: Supports Android OS versions 30 and above. Older versions will fallback to ANRs v1.</p> |

### Recommendation

We recommend adopting the ANR v2 algorithm. The v2 algorithm's accuracy, due to the stack trace being provided by the system itself, makes the reporting data more reliable. For non-fatal ANRs, you can rely on another metric provided by Luciq, [App Hangs](https://docs.luciq.ai/android/set-up-luciq-for-android/set-up-crash-reporting/reporting-crashes-for-android/broken-reference), which captures instances where the app hangs but does not necessarily terminate.

To enable ANR v2, please reach out to our support team at [support@Luciq.com](mailto:support@instabug.com).

By understanding the differences between v1 and v2, you can choose the approach that best fits your needs for monitoring and improving app performance

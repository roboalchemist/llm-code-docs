# Source: https://docs.instabug.com/product-guides-and-integrations/product-guides/crash-reporting/app-hangs.md

# App Hangs

When your app hangs it causes user frustration and can lead them to abandon your app altogether.

An App Hang occurs when the main thread of your app fails to respond within a reasonable timeframe. This can happen due to tasks that consume a lot of CPU resources or when blocking I/O operations are performed on the main thread.

If your app remains unresponsive for 3 seconds or more we capture it as an “App Hang”. We detect Hangs automatically out of the box.

### Here is how to view app hangs on the dashboard:

<figure><img src="https://files.readme.io/cb18349695bceda931cb83f70dfa6fe1388a6a66c8b51b3374a736d93b495252-image.png" alt="" width="188"><figcaption></figcaption></figure>

### How are occurrences of App Hangs grouped:

App Hangs are now grouped by the **first non-system frame** in the stack, what we call the **crash cause**. This brings more accuracy to how hangs are clustered and aligns with how Luciq already groups crashes.

Previously, grouping was based on the **top-most screen**, which offered helpful context. This new method focuses more on the underlying cause.

### What to Expect

* **New App Hangs** will follow the new crash cause-based grouping.
* **Existing App Hangs** will stay grouped by screen.
* **No data will be lost**. We’re simply improving how data is clustered to improve your workflow.
* You may see both grouping types side by side in your dashboard after the change.

### FAQ

**Can I re-group old hangs using the new logic?**

* **Not at this time.** We’re only applying the new grouping logic to data going forward to avoid disrupting historical reporting and analysis.

**Will this affect other issue types?**

* No, this change only affects **App Hangs**. Fatal crashes, ANRs, and other issue types already use stacktrace-based grouping.

### What information is available inside the app hang:

* Stack trace
* Flame graphs to help debug the root cause of the app hang
* Patterns to highlight which subset of users have experienced app hangs
* Occurrences view, where you can view every occurrence of the frustrating experience and what has led to it
* Occurrences include the following debugging data:
  * Metadata of the device
  * Session Profiler to know the state of the device for the last 60 seconds before the app hang occurred
  * Repro steps which is a visual step by step reproduction of the session of the user, screen by screen and interaction by interaction on the app up until the user triggered the termination
  * Logs section including console logs and network logs for all API calls that were made during the session

An app hang is a mobile specific metric that is being picked up by Luciq to give you visibility on the frustrating experiences that the users are going through while using the app.

The data included in app hang enables developers to proactively pick up the frustrating experiences and how it happened and what led up to it. This gives them a chance to resolve those issues early on and keep the standard of quality of the app as high as possible.

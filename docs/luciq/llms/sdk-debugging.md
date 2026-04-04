# Source: https://docs.luciq.ai/kmp/setup-luciq-for-kmp/setup-application-performance-monitoring/sdk-debugging.md

# Source: https://docs.luciq.ai/flutter/setup-luciq-for-flutter/setup-application-performance-monitoring/sdk-debugging.md

# Source: https://docs.luciq.ai/react-native/setup-luciq-for-react-native/setup-application-performance-monitoring/sdk-debugging.md

# Source: https://docs.luciq.ai/android/set-up-luciq-for-android/set-up-application-performance-monitoring/sdk-debugging.md

# Source: https://docs.luciq.ai/ios/setup-luciq-for-ios/setup-application-performance-monitoring/sdk-debugging.md

# Source: https://docs.luciq.ai/product-guides-and-integrations/product-guides/application-performance-monitoring/sdk-debugging.md

# SDK Debugging

### Debug Mode

In case you would like to view your data on the dashboard without having to wait for the SDK's default 6-hour batching period, you can simply bypass this by **running the app while attached to the debugger**.

Attaching the app to the debugger will sync the data captured by our SDK upon **closing a session and starting a new one**. This can be especially helpful if you are debugging an integration issue or simply trying out APM for the first time.

{% hint style="info" %}
Please note that rate limiting will apply if the number of sessions exceeds 50 per hour. Once this limit is reached, you will have to wait until a full hour has elapsed to be able to keep using Debug Mode. Data collected during this period will not show up on your Dashboard.
{% endhint %}

***

### Logging

APM SDK provides useful console logs in Xcode for you to be able to have visibility into significant events that might be of interest to you. Since not all events are equal in terms of importance or relevance, you can control the level of verbosity of those logs via the following API:

The available levels are:

* **`None`:** disables all APM SDK console logs.
* **`Error`:** prints errors only, we use this level to let you know if something goes wrong.
* **`Warning`:** displays warnings that will not necessarily lead to errors but should be addressed nonetheless.
* **`Info`This** is the default level, and it logs information that we think is useful without being too verbose.
* **`Debug`:** Use this in case you are debugging an issue. Not recommended for production use.
* **`Verbose`:** Use this only if `Debug` was not enough, and you need more visibility on what is going on under the hood. Similar to the `Debug` level, this is not meant to be used on production environments.

{% hint style="info" %}
Please note that each level displays the logs corresponding to its own level as well as all the levels above it. This means that `Info` also includes `Warning` and `Error` logs and so on.
{% endhint %}

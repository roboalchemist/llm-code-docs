# Source: https://docs.luciq.ai/ios/setup-luciq-for-ios/custom-settings/user-identification/feature-flags.md

# Source: https://docs.luciq.ai/product-guides-and-integrations/product-guides/feature-flags.md

# Feature Flags

There are different cases where you end up having different feature flags or experiments for different users. For example, if you are:

* Controlling your rollout by enabling features to a % of your users to monitor Performance and Stability.
* Creating and testing different mobile onboarding experiences concurrently.
* Testing different landing pages for your mobile app.
* Implementing new features with different UI.

Through the “Feature Flags” API you can keep track of your feature flags and its impact on [Bug Reports](https://www.luciq.ai/product/bug-reporting), [Crash Reports](https://www.luciq.ai/product/crash-reporting) and [App Performance](https://www.luciq.ai/product/app-performance-monitoring) for each user and even filter by them. This can help you in:

* Detecting if the the potential source of any latency or issues in the app is introduced by different variants of the experiment or new features.
* Having visibility for the latencies of your variants over different metrics.
* Filtering by your experimental variants to analyze if they impact your performance or cause crashes.
* Debugging issues faster by understanding if the experimental values contributed in a issue.

### Set-up Features & Experiments

#### Adding Feature Flags

**Notes:**

1. Feature Flag Naming: Each feature flag name should not exceed 70 characters and each variant name should not exceed 70 characters. Otherwise, they will get ignored by the SDK. Note that feature flag names are case-insensitive.
2. Feature Flag Persistence: Feature flag persist beyond individual sessions and are not automatically removed at the end of a session. Additionally, calling the logOut function does not impact the existence of the feature flag. The feature flag is only removed when you call the removing method or the clearing method.
3. The amount of feature flags sent in a session is 200 with maximum of 1 variant per a multivariate feature flag. For example, a feature flag that has 3 variants sent within 1 session will only be sent to our backend as the last variant, and not all 3.

#### Boolean Feature Flags - Example Usage

Below is an example of where in your code you would use feature flag. In this example, you are experimenting with feature logic that controls whether or not the user has a Dark Mode toggle available.

{% tabs fullWidth="true" %}
{% tab title="iOS-Swift" %}

```swift
let flag = FeatureFlag(name: "flag")
Luciq.add(featureFlag: flag)
```

{% endtab %}

{% tab title="iOS-ObjC" %}
{% code overflow="wrap" %}

```objective-c
[Luciq addFeatureFlag: [[LCQFeatureFlag alloc] initWithName:@"boolFeatureFlag"]];
```

{% endcode %}
{% endtab %}

{% tab title="Android-Java" %}
{% code overflow="wrap" %}

```java
Luciq.addFeatureFlag(new LCQFeatureFlag("boolFeatureFlag"));
```

{% endcode %}
{% endtab %}

{% tab title="Android-Kotlin" %}

```kotlin
Luciq.addFeatureFlag(LCQFeatureFlag("Flag X"))
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
Luciq.addFeatureFlag({ name: "flag_name" });
```

{% endtab %}

{% tab title="Dart" %}

```dart
Luciq.addFeatureFlags([FeatureFlag(name: "name")]);
```

{% endtab %}

{% tab title="Flutter" %}

```
Luciq.addFeatureFlags([FeatureFlag(name: 'Boolean Feature Flag')]);
```

{% endtab %}

{% tab title="React-Native" %}

```
const boolFeatureFlag: FeatureFlag = {name: 'Boolean Feature Flag'}
Luciq.addFeatureFlags([boolFeatureFlag]);
```

{% endtab %}
{% endtabs %}

#### Multivariant Feature Flags - Example Usage

Below is an example of where in your code you would use feature flag with multiple variants. In this example, you are experimenting with feature logic that controls multiple versions of a specific feature.

{% tabs fullWidth="true" %}
{% tab title="iOS-Swift" %}

```swift
let flagWithVariant = FeatureFlag(name: "flag", variant: "variant")
Luciq.add(featureFlag: flagWithVariant)
```

{% endtab %}

{% tab title="iOS-ObjC" %}
{% code overflow="wrap" %}

```objective-c
[Luciq addFeatureFlag: [[LCQFeatureFlag alloc] initWithName:@"stringFeatureFlag" variant:@"Value1"]];
```

{% endcode %}
{% endtab %}

{% tab title="Android-Java" %}
{% code overflow="wrap" %}

```java
Luciq.addFeatureFlag(new LCQFeatureFlag("StringFeatureFlag", "Value"));
```

{% endcode %}
{% endtab %}

{% tab title="Android-Kotlin" %}

```kotlin
Luciq.addFeatureFlag(LCQFeatureFlag("Flag X", "Value"))
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
Luciq.addFeatureFlag({ name: "flag_name", variant: "variant" });
```

{% endtab %}

{% tab title="Dart" %}

```dart
Luciq.addFeatureFlags([FeatureFlag(name: "name", variant: "variant")]);
```

{% endtab %}

{% tab title="Flutter" %}

```
Luciq.addFeatureFlags([FeatureFlag(name: 'Feature Flag', variant: 'Value')]);
```

{% endtab %}

{% tab title="React-Native" %}

```
const featureFlag: FeatureFlag = {name: 'Boolean Feature Flag'}
Luciq.addFeatureFlags([featureFlag]);
```

{% endtab %}
{% endtabs %}

If you have a team who is responsible for a specific feature flag or an experiment, you can automatically assign them the relevant issues and forward them to their favorite tool. You'll find more information on Team Ownership [here](https://docs.luciq.ai/product-guides-and-integrations/product-guides/broken-reference).

In the screenshot below, we wanted to assign crashes relevant to the feature flag Recommendations\_enabled to the team responsible for this feature and auto-forward it to their Jira board.

#### Feature Flags & Team Ownership

If you have a team who is responsible for a specific feature flag or an experiment, you can automatically assign them the relevant issues and forward them to their favorite tool. For more details on Team Ownership, click here

In the screenshot below, we wanted to assign crashes relevant to the experiment Recommendations\_enabled to the team responsible for this feature and auto-forward it to their Jira board

<figure><img src="https://files.readme.io/d781f48-image.png" alt=""><figcaption></figcaption></figure>

#### Removing Feature Flags

If your feature flag is concluded or you would like to simply remove it, you can use this method:

{% tabs fullWidth="true" %}
{% tab title="iOS-Swift" %}

```swift
Luciq.removeFeatureFlag("stringFeatureFlag")
```

{% endtab %}

{% tab title="iOS-ObjC" %}
{% code overflow="wrap" %}

```objective-c
[Luciq removeFeatureFlag:@"boolFeatureFlag"];
[Luciq removeFeatureFlags:@[flag1]];
```

{% endcode %}
{% endtab %}

{% tab title="Android-Java" %}
{% code overflow="wrap" %}

```java
Luciq.removeFeatureFlag("Flag key");
```

{% endcode %}
{% endtab %}

{% tab title="Android-Kotlin" %}

```kotlin
Luciq.removeFeatureFlag("boolFeatureFlag")
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
Luciq.removeFeatureFlag('flag_name');
```

{% endtab %}

{% tab title="Dart" %}

```dart
Luciq.removeFeatureFlags(["name"]);
```

{% endtab %}

{% tab title="Flutter" %}

```
Luciq.removeFeatureFlags(['feature flag']);
```

{% endtab %}

{% tab title="React-Native" %}

```
Luciq.removeFeatureFLag('FeatureFlag'); // remove single key
Luciq.removeFeatureFlags(['featureFlagA', 'featureFlagB']); // remove multiple feature flags at once
```

{% endtab %}
{% endtabs %}

#### Clearing Feature Flags

You can use the below method to clear all the Feature Flags from your reports

{% tabs fullWidth="true" %}
{% tab title="iOS-Swift" %}

```swift
Luciq.removeAllFeatureFlags()
```

{% endtab %}

{% tab title="iOS-ObjC" %}
{% code overflow="wrap" %}

```objective-c
[Luciq removeFeatureFlag:@"boolFeatureFlag"];
[Luciq removeFeatureFlags:@[flag1]];
```

{% endcode %}
{% endtab %}

{% tab title="Android-Java" %}
{% code overflow="wrap" %}

```java
Luciq.removeAllFeatureFlags();
```

{% endcode %}
{% endtab %}

{% tab title="Android-Kotlin" %}

```kotlin
Luciq.removeAllFeatureFlags()
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
Luciq.removeAllFeatureFlags();
```

{% endtab %}

{% tab title="Dart" %}

```dart
Luciq.clearAllFeatureFlags();
```

{% endtab %}

{% tab title="Flutter" %}

```
Luciq.clearAllFeatureFlags();
```

{% endtab %}

{% tab title="React-Native" %}

```
Luciq.removeAllFeatureFlags();
```

{% endtab %}
{% endtabs %}

## Features Flags Dashboard

Explore the Feature Flags Dashboard for a detailed look into the performance metrics of your feature flags and all of their variants.

<img src="https://files.readme.io/7b445f95eb0b4546c99df4c10c01b3eb0f84a6c30117ec23b9cb88599ce7d4ed-image.png" alt="" data-size="original">

#### Types of Feature Flags

There are two types of feature flags:

* **Boolean**: a feature flag that has no variants. Usually used in kill switch feature flags.
* **Multivariant**: a feature flag with multiple variants.

#### Gain key insights

You are able to view different metrics within the page that allow you to gain more key insights like:

* **Apdex Score:** An overall Apdex score is calculated based on Crashes, App Hangs, and Force Restarts occurring in sessions with this feature.
* **Crash-Free Users Rate:** The percentage of users experiencing this feature without any crashes, relative to the total number of users using this feature.
* **Crash-Free Sessions Rate:** The percentage of sessions with this feature that are crash-free out of the total sessions involving this feature.
* **Total Sessions:** View the total number of sessions where this feature flag was detected, providing an overview of its usage.
* **First Seen**: Sort by and view the dates of the release of your feature flags.

  <figure><img src="https://files.readme.io/a50c5f81df42e2f79f16ff1dc64cc2d02b4ebfdee30109d2f16959e2ebdc5d0f-product-guides-feature-flags-3.png" alt=""><figcaption></figcaption></figure>

#### Details Page: Drill Down

1. Insights Table:
   * Explore a detailed breakdown of your feature othrough the Insights Table, providing a nuanced understanding of its performance. Here's a comprehensive overview of each metric:
     * **Apdex**: combining Crashes, App Hangs, and Force Restarts within sessions featuring this specific feature, gives you an overall performance indicator.
     * **Crash-Free Users Rate**: The percentage of users experiencing this feature without any crashes, relative to the total number of users using this feature.
     * **Crash-Free Sessions Rate**: The percentage of sessions with this feature that are crash-free, out of the total sessions involving this feature.
     * **Total Sessions**: View the total number of sessions where this feature flag was detected, providing an overview of its usage.
     * **App Hang-Free Sessions**: The percentage of sessions without any App hangs, out of the total sessions involving this feature.
     * **Force-Restart Free Sessions**: Understand the percentage of sessions that ended in a force restart of the app, out of the total sessions involving this feature.
   * If you click on any of the metrics, you’ll be redirected into the list issues where filtered by this feature.
   * Compare this feature flag against all users across all metrics to identify potential issues or improvements compared to your baseline.<br>

     <figure><img src="https://files.readme.io/a50c5f81df42e2f79f16ff1dc64cc2d02b4ebfdee30109d2f16959e2ebdc5d0f-product-guides-feature-flags-3.png" alt=""><figcaption></figcaption></figure>
2. Crashes Section:
   * **Crashes Tab**: This section provides details on any crash that occurred at least once with this feature.
   * **Introduced Crashes Tab**: Crashes for which the first occurrence includes this feature. This can help you understand the impact of the feature on the introduction of new crashes.
   * **Exclusive Crashes Tab**: Crashes that exclusively happened in sessions containing this feature and never occurred without it. This can help **identify the issues associated specifically with this feature**.

     <figure><img src="https://files.readme.io/60e3934-image.png" alt=""><figcaption></figcaption></figure>

By examining both the Insights Table and the Crashes Section, you gain a comprehensive understanding of your feature , enabling you to find out the best and worst performing features.

### Feature Flags in Performance Monitoring

Once you add the API to your code, you will be able to view the experiments in the patterns section of Cold App Launch, Screen Loading, and UI Hangs.

<figure><img src="https://files.readme.io/a7a75f8293cf96ec0ae381f40e43d2d1a0515804cd0c83d7d96efd59c9d6dee5-product-guides-feature-flags-5.png" alt=""><figcaption></figcaption></figure>

You can see the different latencies of your metric in correlation with the experimental variant. For example, in the previous screenshot, users who had *guest\_mode* enabled had a very different Apdex score, p50 and p95 latencies.

You can also isolate your feature flags by filtering with a specific flag value for further analysis to understand if they are impacting the latency of App launch, Screen Loading or UI hangs.

If you filter by *guest\_mode* and *No experiments* as shown on the following screenshot, the *No Experiments* presents occurrences without any experiments applied. You can also filter by one or more experimental values.

<figure><img src="https://files.readme.io/570c862-2.png" alt=""><figcaption></figcaption></figure>

The *No Experiments* selection will help you spot and compare any difference in performance in each metric.

<figure><img src="https://files.readme.io/f223108ac25c67028dba3813c54c10d831537ef83928ede43f222c7db90701d6-image.png" alt=""><figcaption></figcaption></figure>

### Feature Flags in Crash Reporting

Rolling out new features or doing modifications in your code can increase the number of errors you are seeing. By analyzing how different feature flag variants are contributing to your crashes, you can minimize the debugging efforts and team members can save time.

For example, if you just rolled out a new recommendation feature for a subset of your users, you can view all the crashes that occurred to the users who had this feature enabled by using the filters.

In the screenshot below, we filtered by feature flag *Recommendations\_enabled*, to view the relevant crashes

<figure><img src="https://files.readme.io/0c6fb07-4.png" alt=""><figcaption></figcaption></figure>

You can also view the feature flag variants attached to each crash report on your dashboard in the patterns section of a crash.

<figure><img src="https://files.readme.io/bdff9bc-5.png" alt=""><figcaption></figcaption></figure>

#### Feature Flags in Bug Reporting

Introducing new features or making changes to existing ones can sometimes lead to an increase in Bugs. By leveraging feature flags, you can isolate and analyze issues related to specific features, making it easier to identify and resolve bugs. This approach helps in reducing the debugging time and effort for your team. This should also help you collect actionable data on the next actions for any experiment you are holding

In the screenshot below, you can easily view which feature flag a bug is associated with in each bug report

<figure><img src="https://files.readme.io/88a291c0195590730bdeb31fc3d621c51f8449a3c7635d747ddaf5bdce1d1997-image.png" alt=""><figcaption></figcaption></figure>

You can also easily navigate and filter by a specific feature flag to focus on the bugs you need to prioritize and it would reflect on the reports column on the left

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FQREHqeoWxpUhSlKvu7mG%2Fimage.png?alt=media&#x26;token=bb246314-0f37-445a-9414-ba026ea1dfbf" alt=""><figcaption></figcaption></figure>

# Source: https://firebase.google.com/docs/remote-config/parameters.md.txt

# Remote Config Parameters and Conditions

<button value="client" default="">Client templates</button> <button value="server">Server templates</button>   

You can configure templates for both client and server use cases. Client
templates are served to any app instances that implement the Firebase
client SDKs for Remote Config, including Android, Apple, Web, Unity,
Flutter, and C++ apps. Remote Config parameters and values from
server-specific templates are served to Remote Config implementations
(including Cloud Run and Cloud Functions) that use the following server
environments:

- Firebase Admin Node.js SDK v12.1.0+
- Firebase Admin Python SDK v6.7.0+
- Firebase Admin Go SDK v4.17.0+
- Firebase Admin Java SDK v9.7.0+

When using Firebase console or the
[Remote Config backend APIs](https://firebase.google.com/docs/remote-config/automate-rc),
you define one or more parameters (key-value
pairs) and provide in-app default values for those parameters. You can override
in-app default values by defining parameter values.
Parameter keys and parameter values are strings, but
parameter values can be cast as other data types when you use these values in
your app.

> [!IMPORTANT]
> **Important:** Don't store confidential data in Remote Config parameter keys or values. Remote Config data is encrypted in transit, but end users can access any default or fetched Remote Config parameter that is available to their client app instance.

Using the Firebase console,
[Admin SDK](https://firebase.google.com/docs/remote-config/automate-rc#use_config_sdk) or the
[Remote Config REST API](https://firebase.google.com/docs/remote-config/automate-rc#use_config_rest),
you can create new default values for your
parameters, as well as conditional values that are used to target groups of app
instances. Each time you update your configuration in the Firebase console,
Firebase creates and publishes a new version of your Remote Config template.
The previous version is stored, allowing you to retrieve or rollback as needed.
These operations are available to you in the Firebase console, the
Firebase Admin SDK, and the REST API and are described more extensively in
[Manage Remote Config template versions](https://firebase.google.com/docs/remote-config/templates#manage_template_versions).

This guide explains parameters, conditions, rules, conditional
values, and how various parameter values are prioritized on the
Remote Config backend and in your app. It also provides details on the
types of rules used to create conditions.

## Conditions, rules, and conditional values

A condition is used to target a group of app instances. Conditions are made
up of one or more rules that must all evaluate to `true` for the condition to
evaluate to `true` for a given app instance. If the value for a rule is
undefined (for example, when no value is available), that rule will evaluate to
`false`.

For example, you could create a parameter that defines a large language
model (LLM) model name and version string, and serve responses from different
models based on [custom signal
rules](https://firebase.google.com/docs/remote-config/parameters?template_type=server#custom-signals). In
this use case, you might use a stable model version as the default value to
serve most requests, and use the custom signal to use an experimental model to
respond to test client requests.

A parameter can have multiple conditional
values that use different conditions, and parameters can share conditions within
a project. In the [Parameters tab](https://https://console.firebase.google.com/project/_/config/env/firebase)
of the Firebase console, you can view the fetch percentage for each
parameter's conditional values. This metric indicates the percentage of requests
in the last 24 hours that received each value.

### IPv6 limitation with IP-based access control

Remote Config has limited support for IPv6 when used with IP-based
access policies. If your organization restricts access to specific public IP
ranges, connecting through an IPv6 network can cause the following issues:

- **Console access:** You might be unable to use certain Remote Config features in the Firebase console, such as loading data or setting up targeting.
- **Client access:** Client apps may encounter PERMISSION_DENIED errors.

To prevent these issues, we recommend configuring your network to use IPv4 or
add the required Firebase IP ranges to your organization's allowlist.

## Parameter value priority

A parameter might have several conditional values associated with it. The
following rules determine which value is fetched from the Remote Config
template, and which value is used in a given app instance at a particular
point in time:

1. First, [conditional values](https://firebase.google.com/docs/remote-config/parameters#condition-rule-types) are applied for any
   conditions that evaluate to `true` for a given client request. If
   multiple conditions evaluate to `true`, the first (top) one shown in the
   Firebase console UI takes precedence, and conditional values
   associated with that condition are provided when an app fetches values
   from the backend. You can change the priority of conditions by dragging
   and dropping conditions in the **Conditions** tab.

2. If there are no conditional values with conditions that evaluate to `true`,
   the Remote Config's default value is provided when an app fetches
   values from the backend. If a parameter doesn't exist in the backend, or if
   the default value is set to **Use in-app default**, then no value is
   provided for that parameter when an app fetches values.

   > [!NOTE]
   > **Note:** When a Remote Config parameter is being used in an active [Firebase A/B Testing](https://firebase.google.com/docs/ab-testing/abtest-config) experiment, then the experiment values take precedence over any Remote Config conditional values.

**In your app, parameter values are returned by `get` methods according to
the following priority list**

1. If a value was fetched from the backend and then activated, the app uses the fetched value. Activated parameter values are persistent.
2. If no value was fetched from the backend, or if values fetched from the
   Remote Config backend have not been activated, the app uses the in-app
   default value.

   For more information on obtaining and setting default values, see
   [Download Remote Config template defaults](https://firebase.google.com/docs/remote-config/templates#download_template_defaults).
3. If no in-app default value has been set, the app uses a static type
   value (such as `0` for `int` and `false` for `boolean`).

This graphic summarizes how parameter values are prioritized in the
Remote Config backend, and in your app:

![Diagram showing the flow described by the ordered lists above](https://firebase.google.com/static/docs/remote-config/images/param-precedence.png)

## Parameter value data types

Remote Config lets you select a data type for each parameter, and
validates all Remote Config values against that type before a template
update. The data type is stored and returned on a `getRemoteConfig`
request.

Supported data types are:

- `String`
- `Boolean`
- `Number`
- `JSON`

In the Firebase console UI, the data type can be selected from a
drop-down next to the parameter key. In the REST API, types can be set using
the `value_type` field within the parameter object.

> [!NOTE]
> **Note:** Selecting a data type does not affect how values are returned to the client SDKs. However, check that in your app the `get` method is casting the value back to the intended data type.

## Parameter groups

Remote Config lets you group parameters together for a more organized
UI and enhance usability.

For example, say you need to enable or disable three different auth types
while rolling out a new login feature. With Remote Config, you can create
the three parameters to enable the types you want, and then organize them in a
group named "New login," with no need to add prefixes or special sorting.

> [!NOTE]
> **Note:** Parameter groups provide organization in the Firebase console and Remote Config REST API. However, they don't change how parameters are referenced by the SDK.

You can create parameter groups using the Firebase console or the
Remote Config REST API. Each parameter group you create has a unique name in
your Remote Config template. When creating parameter groups, keep in mind:

- Parameters can be included in only one group at any time, and a parameter key must still be unique across all parameters.
- Parameter group names are limited to 256 characters.
- If you use both the REST API and the Firebase console, make sure that any REST API logic is updated to handle parameter groups on publish.

### Create or modify parameter groups using the Firebase console

You can group parameters in the
[Parameters](https://https://console.firebase.google.com/project/_/config/env/firebase)
tab of the Firebase console. To create or modify a group:

1. Select **Manage groups**.
2. Select checkboxes for parameters you want to add and select **Move to group**.
3. Select an existing group, or create a new group by entering a name and description, and selecting **Create new group** . After you save a group, it is available to be published using the **Publish changes** button.

## Condition rule types

The following rule types are supported in the Firebase console. Equivalent
features are available in the Remote Config REST API, as detailed in the
[conditional expression reference](https://firebase.google.com/docs/remote-config/condition-reference).

|---|---|---|---|
| Rule type | Operator(s) | Value(s) | Note |
| App | == | Select from a list of App IDs for apps associated with your Firebase project. | When you add an app to Firebase, you enter a bundle ID or Android package name that defines an attribute that's exposed as **App ID** in Remote Config rules. <br /> Use this attribute as follows: - **For Apple platforms:** Use the app's [CFBundleIdentifier](https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CoreFoundationKeys.html#//apple_ref/doc/uid/20001431-102070). You can find the **Bundle Identifier** in the **General** tab for your app's primary target in Xcode. - **For Android:** Use the app's [applicationId](https://developer.android.com/build/configure-app-module#set-application-id). You can find the `applicationId` in your app-level `build.gradle(.kts)` file. |
| App version | **For string values:** exactly matches, contains, does not contain, contains regex <br /> **For numeric values:** \<, \<=, =, !=, \>, \>= | Specify the version(s) of your app to target. Before using this rule, you must use an **App ID** rule to select an Android/Apple app associated with your Firebase project. | **For Apple platforms:** Use the app's [CFBundleShortVersionString](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleshortversionstring). **Note:** Make sure your Apple app is using Firebase Apple platforms SDK version 6.24.0 or higher, as CFBundleShortVersionString is not being sent in earlier versions (see [release notes](https://firebase.google.com/support/release-notes/ios#remote-config_4)). **For Android:** Use the app's [versionName](https://developer.android.com/guide/topics/manifest/manifest-element.html#vname). String comparisons for this rule are case-sensitive. When using the **exactly matches** , **contains** , **does not contain** , or **contains regex** operator, you can select multiple values. When using the **contains regex** operator, you can create regular expressions in [RE2](https://github.com/google/re2/wiki/Syntax) format. Your regular expression can match all or part of the target version string. You can also use the **\^** and **$** anchors to match the beginning, end, or entirety of a target string. |
| Build number | **For string values:** exactly matches, contains, does not contain, regular expression <br /> **For numeric values:** =, ≠, \>, ≥, \<, ≤ | Specify the build(s) of your app to target. Before using this rule, you must use an **App ID** rule to select an Apple or Android app associated with your Firebase project. | This operator is available for Apple and Android apps only. It corresponds to the app's [CFBundleVersion](https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CoreFoundationKeys.html#//apple_ref/doc/uid/20001431-102364) for Apple and [versionCode](https://developer.android.com/studio/publish/versioning#appversioning) for Android. String comparisons for this rule are case-sensitive. When using the **exactly matches** , **contains** , **does not contain** , or **contains regex** operator, you can select multiple values. When using the **contains regex** operator, you can create regular expressions in [RE2](https://github.com/google/re2/wiki/Syntax) format. Your regular expression can match all or part of the target version string. You can also use the **\^** and **$** anchors to match the beginning, end, or entirety of a target string. |
| Platform | == | iOS Android Web |   |
| Operating system | == | Specify the operating system(s) to target. Before using this rule, you must use an **App ID** rule to select a **Web app** associated with your Firebase project. | This rule evaluates to `true` for a given Web app instance if the operating system and its version matches a target value in the specified list. |
| Browser | == | Specify the browser(s) to target. Before using this rule, you must use an **App ID** rule to select a **Web app** associated with your Firebase project. | This rule evaluates to `true` for a given Web app instance if the browser and its version matches a target value in the specified list. |
| Device category | is, is not | mobile | This rule evaluates whether the device accessing your web app is mobile or non-mobile (desktop or console). This rule type is only available for web apps. |
| Languages | is in | Select one or more languages. | This rule evaluates to `true` for a given app instance if that app instance is installed on a device that uses one of the languages listed. |
| Country/Region | is in | Select one or more regions or countries. | This rule evaluates to `true` for a given app instance if the instance is in any of the regions or countries listed. The device country code is determined using the device's IP address in the request or the country code determined by Firebase Analytics (if Analytics data is shared with Firebase). |
| User audience(s) | Includes at least one | Select one or more from a list of Google Analytics audiences that you have set up for your project. | This rule requires an App ID rule to select an app associated with your Firebase project. **Note:** Because many Analytics audiences are defined by events or user properties, which can be based the actions of app users, it may take some time for a **User in audience** rule to take effect for a given app instance. |
| User property | **For string values:** contains, does not contain, exactly matches, contains regex <br /> **For numeric values:** =, ≠, \>, ≥, \<, ≤ <br /> Note: On the client, you can set only string values for user properties. For conditions that use numeric operators, Remote Config converts the value of the corresponding user property into an integer/float. | Select from a list of available Google Analytics user properties. | To learn how you can use user properties to customize your app for very specific segments of your user base, see [Remote Config and user properties](https://firebase.google.com/docs/remote-config/config-analytics#remote_config_and_user_properties). <br /> To learn more about user properties, see the following guides: - [Set user properties on Apple](https://firebase.google.com/docs/analytics/ios/properties) - [Set user properties on Android](https://firebase.google.com/docs/analytics/android/properties) When using the **exactly matches** , **contains** , **does not contain** or **contains regex** operator, you can select multiple values. When using the **contains regex** operator, you can create regular expressions in [RE2](https://github.com/google/re2/wiki/Syntax) format. Your regular expression can match all or part of the target version string. You can also use the **\^** and **$** anchors to match the beginning, end, or entirety of a target string. **Note:** [Automatically collected user properties](https://support.google.com/firebase/answer/6317486) are not available when creating Remote Config conditions. |
| User in random percentage | Slider (in the Firebase console. The [REST API](https://firebase.google.com/docs/remote-config/condition-reference) uses the `<=`, `>`, and `between` operators). | 0-100 | Use this field to apply a change to a random sample of app instances (with sample sizes as small as .0001%), using the slider widget to segment randomly-shuffled users (app instances) into groups. Each app instance is persistently mapped to a random whole or fractional number, according to a *seed* defined in that project. Seed values can contain between one and 32 characters containing alphanumeric values, dots, hyphens, and/or underscores. A rule will use the default key (shown as **Edit seed** in the Firebase console) unless you modify the seed value. You can return a rule to using the default key by clearing the **Seed** field. To consistently address the same app instances within given percentage ranges, use the same seed value across conditions. Or, select a new randomly-assigned group of app instances for a given percentage range by specifying a new seed. For example, to create two related conditions that each apply to a non-overlapping 5% of an app's users, you could configure one condition to match a percentage between 0% and 5% and configure another condition to match a range between 5% and 10%. To allow some users to randomly appear in both groups, use different seed values for the rules within each condition. |
| Imported segment | is in | Select one or more imported segment. | This rule requires setting up custom [imported segments](https://firebase.google.com/docs/projects/import-segments). |
| Date/Time | Before, After | A specified date and time, either in the device timezone or a specified timezone such as "(GMT+11) Sydney time." | Compares the current time to the device fetch time. |
| First open | Before, After | A specified date and time, in the specified timezone. | Matches users who first open the targeted app within the specified time range. Requires the following SDKs: - Firebase SDK for Google Analytics - Apple platforms SDK v9.0.0+ or Android SDK v21.1.1+ (Firebase BoM v30.3.0+) |
| Installation ID | is in | Specify one or more Installation IDs (up to 50) to target. | This rule evaluates to `true` for a given installation if that installation's ID is in the comma-separated list of values. <br /> To learn how you can get installation IDs, see [Retrieve client identifiers](https://firebase.google.com/docs/projects/manage-installations#retrieve_client_identifiers). |
| User exists | (no operator) | Targets all users of all apps within the current project. | Use this condition rule to match all users within the project, regardless of app or platform. When using [Remote Config personalization](https://firebase.google.com/docs/remote-config/personalization), you can use this operator to ensure that all users within the project receive personalized values. |
| Custom signal | **For string values:** contains, does not contain, exactly matches, contains regex <br /> **For numeric values:** =, ≠, \>, ≥, \<, ≤ <br /> **For version values:** =, ≠, \>, ≥, \<, ≤ | String comparisons for this rule are case-sensitive. When using the exactly matches, contains, does not contain, or contains regex operator, you can select multiple values. When using the contains regex operator, you can create regular expressions in [RE2](https://github.com/google/re2/wiki/Syntax) format. Your regular expression can match all or part of the target version string. You can also use the \^ and $ anchors to match the beginning, end, or entirety of a target string. The following data types are supported for client environments: - iOS: int, double - Android: int, long, double - Web: number Numeral that represents the version number(s) to match (for example, 2.1.0). | For more information on custom signal conditions and conditional expressions to use, see [Custom signal conditions](https://firebase.google.com/docs/remote-config/parameters?template_type=client#custom_signal_conditions) and [Elements used to create conditions](https://firebase.google.com/docs/remote-config/condition-reference#elements_used_to_create_conditions). |


## Search parameters and conditions

You can search your project's parameter keys, parameter values, and conditions
from the [Firebase console](https://console.firebase.google.com) using the
search box at the top of the Remote Config **Parameters** tab.

## Limits on parameters and conditions

Within a Firebase project, you can have up to 3000 parameters, and up to 2000
conditions. Parameter keys can be up to 256 characters long, must start with an
underscore or English letter character (A-Z, a-z), and may also include
numbers. The total length of parameter value strings within a project cannot
exceed 1,000,000 characters.


## View changes to parameters and conditions

You can view the latest changes to your Remote Config templates
from the [Firebase console](https://console.firebase.google.com). For
each individual parameter and condition, you can:

- View the name of the user who last modified the parameter or condition.

- If the change occurred within the same day, view the number of minutes or
  hours that have elapsed since the change was published to the active
  Remote Config template.

- If the change occurred one or more days in the past, view the date when
  the change was published to the active Remote Config template.

### Change history for parameters

On the Remote Config
[Parameters](https://https://console.firebase.google.com/project/_/config/env/firebase)
page, the **Last published** column shows the last user who modified each
parameter and the last publish date for the change:

- To view change metadata for grouped parameters, expand the parameter group.

- To sort in ascending or descending order by publish date, click the
  **Last published** column label.

### Change history for conditions

On the Remote Config
[Conditions](https://https://console.firebase.google.com/project/_/config/env/firebase/conditions)
page, you can see the last user who modified the condition and the date
they modified it next to **Last modified** under each condition.

## Next steps

To configure your Firebase project and app to use Remote Config, see [Get started with Firebase Remote Config](https://firebase.google.com/docs/remote-config/get-started).
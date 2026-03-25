# Source: https://docs.luciq.ai/android/set-up-luciq-for-android/set-up-application-performance-monitoring/set-up-flows.md

# Set up Flows

{% hint style="warning" %}

### Minimum Required SDK Version

Flows are supported starting Android SDK v13.0.0
{% endhint %}

Flows gives you **consolidated view of the health and performance of your app's most important flows**. With simple instrumentation, you can measure the time it takes users to complete key user journeys, understand completion and drop-off rates as well as their root causes, learn what crashes are affecting your flows, and gain insight into the various spans and operations occurring within those flows and their performance.

### Instrumentation

To create a flow you just need to **define a start and an end for that flow** in your code. Luciq automatically captures data health and performance data between those two points. All instances of flows with the same name are aggregated on your dashboard.

{% hint style="warning" %}

### Rules around creating Flows:

* Flows are **uniquely identified by their name**.
* You **can** run several flow with **different names** in parallel.
* You **can’t** run different instances of the **same flow** in parallel.
* You **can start a flow** while your app is in the **background**.
* You **can’t end a flow** while your app in the **background**.
* You can create **up to 10,000 unique Flows**.
  {% endhint %}

#### Start a Flow

To mark the **beginning of a Flow**, add the following API call to your code:

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
//Start a Flow
APM.startFlow("flowName")
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
//Start a Flow
APM.startFlow("flowName");
```

{% endcode %}
{% endtab %}
{% endtabs %}

This API call initiates an instance of a flow named “flowName”. If any other instances of the same flow are already started and weren’t ended yet, they are considered drop-offs.

{% hint style="info" %}

### Naming Limitation for Flows:

* Flow **name** can be up to **150 characters**. Any extra characters are truncated.
* Flow **name can't be null** or an **empty string**.
* **Avoid** adding any of these **special characters** \[, (, ), =, {, }, <, >, /, , ] (commas not included) as they will be replaced with \_.
  {% endhint %}

#### End a Flow

To mark the **end of an already started Flow**, use the following API call:

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
// End an existing flow
APM.endFlow("flowName")
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
// End an existing flow
APM.endFlow("flowName");
```

{% endcode %}
{% endtab %}
{% endtabs %}

This API call ends an instance of the flow “flowName”. Be sure to call this at the right point in your call to accurately capture the duration and completion state of the flow.

#### Adding Custom Flow Attributes

Luciq **automatically attaches some attributes** like app version, OS version, and device to all Flows. You can use those attributes to drill-down and find insightful patterns in your data (e.g . if a performance problem is related to a specific device model).

For advanced analysis, you can **create your own custom attributes** and attach them to any flow. This step is **optional** but can provide valuable context for debugging specific user segments or behaviors.

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
// Add custom attributes to an existing flow
APM.setFlowAttribute("flowName", "key", "value")
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
// Add custom attributes to an existing flow
APM.setFlowAttribute("flowName", "key", "value");
```

{% endcode %}
{% endtab %}
{% endtabs %}

This API call creates a new custom attribute called “key” with the value “value” and attaches it to the flow “flowName”.

{% hint style="warning" %}
**When using custom attributes that can have a large number of unique values, please group those values into buckets**. Using a massive number of unique values can negatively impact your dashboard’s performance.
{% endhint %}

{% hint style="info" %}
Rules and Limitations for Custom Flow Attributes:

* The attribute's **key** can be up to **30 characters**.
* The attribute's **value** can be up to **60 characters**.
* **Avoid** adding any of these **special characters** \[, (, ), =, {, }, <, >, /, , ] (commas not included) as they will be replaced with \_.
* You can add up to **5 unique custom attributes to each flow instance.**
* You can have up to **20 unique custom attribute keys across all instances of a flow.**
* The attribute's key **can't** be an **empty string** or **null**.
* The attribute's value **can't** be an **empty string**.
* You can call the API twice with the same key to override a previous value.
* Setting a attribute value to *null* will remove the attribute from the flow.
  {% endhint %}

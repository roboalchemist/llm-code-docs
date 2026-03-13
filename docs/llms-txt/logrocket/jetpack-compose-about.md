# Source: https://docs.logrocket.com/reference/jetpack-compose-about.md

# Jetpack Compose

# About Jetpack Compose

The LogRocket SDK will work with Jetpack Compose in the same way as outlined in these [Android docs](https://docs.logrocket.com/reference/android), with some limitations or differences outlined throughout this doc.

You can find an [overview of Jetpack Compose](https://developer.android.com/jetpack) on the Android developer site. Compose UI elements are not stored and rendered as standard Android views. Because of this, Jetpack Compose capture in LogRocket is a separate capture system from Native Android View capture.

We recommend staying up to date with the latest LogRocket SDK version. However, at least the following versions need to be used depending on which version of [Compose UI](https://developer.android.com/jetpack/androidx/releases/compose-ui) is used in your app.

> 📘 Additional dependency required for Jetpack Compose when using v2.0.0+ of the LogRocket SDK
>
> If you are using v2.0.0+ of the LogRocket SDK and want to capture Jetpack Compose views then you need to [install an additional LogRocket dependency](android-sdk-20#jetpack-compose) in your `build.gradle`.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        LogRocket Version
      </th>

      <th>
        Compose Support
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `1.61.2`
      </td>

      <td>
        Adds Support for Jetpack Compose `1.10.x`
      </td>
    </tr>

    <tr>
      <td>
        `1.59.0`
      </td>

      <td>
        Adds support for Jetpack Compose `1.9.4+`
      </td>
    </tr>

    <tr>
      <td>
        `1.54.1`
      </td>

      <td>
        Adds support for Jetpack Compose `1.8.x` and `1.9.x` through `1.9.3`.
        See [redaction note here](https://docs.logrocket.com/docs/mobile-sdk-changelog#/1541-2025-07-08).
      </td>
    </tr>

    <tr>
      <td>
        `1.39.1`
      </td>

      <td>
        Adds support for Jetpack Compose `1.7.x`
      </td>
    </tr>

    <tr>
      <td>
        `1.33.2`
      </td>

      <td>
        Adds support for Jetpack Compose `1.6.x`
      </td>
    </tr>

    <tr>
      <td>
        `1.25.0`
      </td>

      <td>
        Adds Jetpack Compose support for apps using Proguard minification
      </td>
    </tr>

    <tr>
      <td>
        `1.19.3`
      </td>

      <td>
        Adds support for Jetpack Compose `1.5.x`
      </td>
    </tr>

    <tr>
      <td>
        `1.17.2`
      </td>

      <td>
        Adds support for Jetpack Compose `1.4.x`
      </td>
    </tr>
  </tbody>
</Table>

Jetpack Compose capture can be disabled by setting initialization configuration option: `options.setEnableJetpackCompose(false)`.

### Self Hosted

If your LogRocket server is self hosted, mobile SDK version `1.17.2` requires a minimum server version of `16.462.0`. If your server is between versions `16.329.0 - 16.461.0`, you can capture Jetpack Compose UIs with mobile SDK version `1.16.10` and setting initialization configuration option: `options.setEnableJetpackCompose(true)`, though we recommend updating your LogRocket server and SDKs to the latest available version.

## Redaction

Complete masking rules still apply, such as [Automatically Sanitize Text](https://docs.logrocket.com/reference/android-automatically-sanitize-text) and [Sanitize Network Data](https://docs.logrocket.com/reference/android-capturing-network-traffic).

You can redact specific Jetpack Compose elements by adding a testTag or layoutId with value`"lr-hide"` or another custom Redaction Tag value. See details [here on how to add redaction tag objects](https://docs.logrocket.com/reference/android-redact-view) in addition to the default `"lr-hide"`.

Examples:

```Text Kotlin
// Example 1 - use .testTag()
Text(
  text = "example",
  modifier = Modifier.testTag("lr-hide")
)


// Example 2 - set up other testTags to be redacted in your init call
SDK.init(
  ...
  options -> {
    ...
    options.addRedactionTag("MyRedactionTag");
  }
)
Text(
  text = "example",
  modifier = Modifier.testTag("MyRedactionTag")
)


// Example 3 - use .layoutId()
Text(
  text = "example",
  modifier = Modifier.layoutId("lr-hide")
)


// Example 4 - configure a class to be used for layoutId redaction in your init call
class RedactionId constructor(id: String) {
    override fun equals(other: Any?): Boolean {
        return other is RedactionId // will redact all RedactionId instances
    }
}
SDK.init(
  ...
  options -> {
    ...
    options.addRedactionTag(RedactionId(""));
  }
)
Text(
  text = "example",
  modifier = Modifier.layoutId(RedactionId("some id"))
)
```

#### AndroidView

If you need to redact any [AndroidView Composables](https://developer.android.com/jetpack/compose/migrate/interoperability-apis/views-in-compose) , you will need to redact the entire AndroidView, and not individual Views inside that AndroidView.

Example:

```Text Kotlin
AndroidView(
  factory = { context ->
    ...
  },
  update = {
    ...
  },
  modifier = Modifier.testTag("lr-hide")
)
```

## View Allowlisting

Individual child nodes of a redacted Jetpack Compose element can be allowed for view capture by adding a testTag or layoutId with value`"lr-show"` or another custom Allow Tag value. See details [here on how to add allow tag objects](https://docs.logrocket.com/reference/android-redact-view#optionsaddallowtagobject-tag) in addition to the default `"lr-hide"`.

Examples:

```Text Kotlin
// Example 1 - use .testTag()
Column(Modifier.testTag("lr-hide")){
	Text("uncaptured text")
	Text("uncaptured text")
  Text(
    text = "captured text",
    modifier = Modifier.testTag("lr-show")
  )
}


// Example 2 - set up other testTags to be allowed in your init call
SDK.init(
  ...
  options -> {
    ...
    options.addAllowTag("MyAllowTag");
  }
)
Column(Modifier.testTag("lr-hide")){
	Text("uncaptured text")
	Text("uncaptured text")
  Text(
    text = "captured text",
    modifier = Modifier.testTag("MyAllowTag")
  )
}


// Example 3 - use .layoutId()
Column(Modifier.layoutId("lr-hide")){
	Text("uncaptured text")
	Text("uncaptured text")
  Text(
    text = "captured text",
    modifier = Modifier.layoutId("lr-show")
  )
}


// Example 4 - configure a class to be used for layoutId redaction in your init call
class RedactionId constructor(id: String) {
    override fun equals(other: Any?): Boolean {
        return other is RedactionId // will redact all RedactionId instances
    }
}
SDK.init(
  ...
  options -> {
    ...
    options.addAllowTag(AllowId(""));
  }
)

Column(Modifier.testTag("lr-hide")){
	Text("uncaptured text")
	Text("uncaptured text")
  Text(
    text = "captured text",
	  modifier = Modifier.layoutId(RedactionId("some id"))
  )
}
```

#### AndroidView

The same restriction applies for allowlisting  [AndroidView Composables](https://developer.android.com/jetpack/compose/migrate/interoperability-apis/views-in-compose) as for redacting them , you will need to either allow or redact the entire AndroidView, and not individual Views inside that AndroidView.

## Navigation

As with our prior Android Native SDK, Jetpack Compose screens may not be meaningful on their own. As such, we recommend using the [Manual Page Identification API ](https://docs.logrocket.com/reference/capture-custom-pages-android)to best track navigation events.

## Selectors

A full description of [LogRocket Selectors](https://docs.logrocket.com/docs/query-selectors-for-mobile) and how to use them in the dashboard can be [found here](https://docs.logrocket.com/docs/query-selectors-for-mobile) .

Jetpack Compose views are [rendered in 3 phases](https://developer.android.com/jetpack/compose/phases#3-phases). The Layout phase defines where UI elements are placed on the screen. When users interact with an element on screen, they are interacting with a node in the Layout Tree. The LogRocket SDK defines Selectors based on the node types and modifiers in the Layout Tree.

| Component  | Value                                          | Note                                                         |
| :--------- | :--------------------------------------------- | :----------------------------------------------------------- |
| `NodeName` | Class name of the Layout node's measure policy |                                                              |
| `.testTag` | Value provided in .testTag() Modifier          | Object values are converted to String by calling .toString() |
| `#id`      | Value provided in .layoutId() Modifer          | Object values are converted to String by calling .toString() |

Example:

```Text Kotlin
// This Compose element can be referenced in LogRocket with selector:
//   TextController.HeaderText#abc123
Text(
  text = "My App",
  modifier = Modifier.testTag("HeaderText").layoutId("abc123")
)
```

### Touch Events

The SDK will capture touch events with the text and selector that was touched. Any touch on an [AndroidView Composable](https://developer.android.com/jetpack/compose/migrate/interoperability-apis/views-in-compose)  will appear as a click on the entire AndroidView, and not the individual View inside that AndroidView. Touch HeatMap support was added in SDK version `1.17.1`.

## Limitations

* Currently, Compose Google Maps components are incompatible with LogRocket, and LogRocket may cause these elements to freeze. To prevent this, the Google Maps composable (or an ancestor of this composable) needs to be [redacted from LogRocket](https://docs.logrocket.com/reference/jetpack-compose-about#redaction) in your application. Please reach out to LogRocket support if you have questions.
* As listed above, when redacting or allowlisting any [AndroidView Composables](https://developer.android.com/jetpack/compose/migrate/interoperability-apis/views-in-compose) , the entire AndroidView needs to be redacted and not individual Views inside that AndroidView.
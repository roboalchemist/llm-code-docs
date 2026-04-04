# Source: https://docs.asapp.com/agent-desk/integrations/ios-sdk/deep-links-and-web-links.md

# Source: https://docs.asapp.com/agent-desk/integrations/android-sdk/deep-links-and-web-links.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Deep Links and Web Links

## Handling Deep Links in Chat

Certain chat flows may present buttons that are deep links to another part of your app. To react to taps on these buttons, implement the `ASAPPDeepLinkHandler` interface:

```kotlin  theme={null}
ASAPP.instance.deepLinkHandler = object : ASAPPDeepLinkHandler {
    override fun handleASAPPDeepLink(deepLink: String, data: JSONObject?, activity: Activity) {
        // Handle deep link.
    }
}
```

ASAPP provides an `Activity` instance for convenience, in case you need to start a new activity. Please ask your Implementation Manager if you have questions regarding deep link names and data.

### Example: Parsing and Opening Deep Links in Your Activity

If your app receives deep links through an Intent, you can extract the parameters and forward them to the ASAPP SDK when you reopen a chat.

```kotlin  theme={null}
object AppDeepLinkHelper {

    fun getASAPPDeepLinkDataIfAny(context: Context, intent: Intent): Map<String, Any>? {
        val uri = intent.data ?: return null
        if (context.getString(R.string.app_deep_link_host) != uri.host) return null

        val map = mutableMapOf<String, Any>()
        uri.queryParameterNames
                .map { key ->
                    val value = uri.getQueryParameter(key)
                    val name = if (key == "intentKey") "Code" else key
                    if (value != null) map[name] = value
                }
        return map
    }
}
```

Then handle it in your activity:

```kotlin  theme={null}
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    ...
    handleIntent(intent) // Handle deep link if app is cold-started
}
override fun onNewIntent(intent: Intent) {
    super.onNewIntent(intent)
    handleIntent(intent) // Handle deep link if activity is reused
}
private fun handleIntent(intent: Intent) {
        val deepLinkData = AppDeepLinkHelper.getASAPPDeepLinkDataIfAny(this, intent)
        if (!deepLinkData.isNullOrEmpty()) {
            APP.instance.openChat(this, asappIntent = deepLinkData)
        } else {
            openChatIfNotificationIntent(intent)
        }
}
```

<Note>
  ✅ Tip: This approach ensures your app only responds to deep links from the expected host, and safely maps query parameters into a format that openChat() can consume.
</Note>

## Handling Web Links in Chat

Certain chat flows may present buttons that are web links. To react to taps on these buttons, implement the `ASAPPWebLinkHandler` interface:

```kotlin  theme={null}
ASAPP.instance.webLinkHandler = object : ASAPPWebLinkHandler {
    override fun handleASAPPWebLink(webLink: String, activity: Activity) {
        // Handle web link.
    }
}
```

<Note>
  If you don't implement the handler (see above), the ASAPP SDK will open the link utilizing the system default with `Intent.ACTION_VIEW`.
</Note>

## Implementing Deep Links into Chat

### Getting Started

Please see the Android documentation on [Handling Android App Links](https://developer.android.com/training/app-links).

### Connecting the Pieces

Once you set up a custom URL scheme for your app and handle deep links into your application, you can start chat to pass any data payload that you extract from the link:

```json  theme={null}
ASAPP.instance.openChat(context, asappIntent= mapOf("Code": "EXAMPLE_INTENT"))
```

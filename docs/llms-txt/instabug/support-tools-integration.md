# Source: https://docs.instabug.com/kmp/setup-luciq-for-kmp/setup-session-replay/support-tools-integration.md

# Source: https://docs.instabug.com/flutter/setup-luciq-for-flutter/setup-session-replay/support-tools-integration.md

# Source: https://docs.instabug.com/react-native/setup-luciq-for-react-native/setup-session-replay/support-tools-integration.md

# Source: https://docs.instabug.com/android/set-up-luciq-for-android/set-up-session-replay/support-tools-integration.md

# Source: https://docs.instabug.com/ios/setup-luciq-for-ios/setup-session-replay/support-tools-integration.md

# Support Tools Integration

To be able to debug support tickets effortlessly, all you have to do is extract the session URL from Luciq and send it as a custom attribute to your preferred support tools. This enables your support team to view Session Replays for every reported issue to help in debugging the issue. You can use the below API to extract the session URL:

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
if let sessionLink = SessionReplay.sessionReplayLink {
  print("result: \(sessionLink)")
}
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
NSString *sessionLink = LCQSessionReplay.sessionReplayLink;
if (sessionLink != NULL) {
    NSLog(@"sessionLink: %@", sessionLink);
}
```

{% endcode %}
{% endtab %}
{% endtabs %}

#### Zendesk Example

To automatically attach the session URL to every support ticket submitted through Zendesk, just insert the following snippet into your application's code.

<figure><img src="https://828794017-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAM8wNfllcup3GnWJ1WtW%2Fuploads%2FlHqYwvYXl6sgaflERmVv%2Fimage.png?alt=media&#x26;token=db3b324b-b786-433a-8a45-48c7ac3b7d64" alt=""><figcaption></figcaption></figure>

***Send Session URL as tags:***

{% tabs %}
{% tab title="Swift" %}

```swift
let request = ZDKCreateRequest()
        request.subject = "Session replay"
        request.requestDescription = "Adding session replay url"

        let luciqSessionReplayLink = SessionReplay.sessionReplayLink

        request.tags = [luciqSessionReplayLink]
```

{% endtab %}
{% endtabs %}

***Send Session URL as custom fields:***

{% tabs %}
{% tab title="Swift" %}

```swift
let request = ZDKCreateRequest()
        request.subject = "Session replay"
        request.requestDescription = "Adding session replay url"

        let luciqSessionReplayLink = SessionReplay.sessionReplayLink
        let field = CustomField(fieldId: 1234, value: luciqSessionReplayLink)

        request.customFields = [field]
```

{% endtab %}
{% endtabs %}

#### Intercom Example

To automatically include the Session URL with each support ticket received via Intercom, simply integrate the following code snippet into your application. This will send the session URL to the recent events section.

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
guard let sessionURL = SessionReplay.sessionReplayLink else { return }
        Intercom.logEvent(withName: "session-replay-url", metaData: ["url": sessionURL])
        
        Intercom.present()
```

{% endcode %}
{% endtab %}
{% endtabs %}

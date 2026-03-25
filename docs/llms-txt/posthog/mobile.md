# Source: https://posthog.com/docs/session-replay/mobile.md

# Mobile session replay - Docs

> 🚧 **NOTE:** Mobile session replay is **currently available on [Android](/docs/session-replay/installation/android.md), [iOS](/docs/session-replay/installation/ios.md), [React Native](/docs/session-replay/installation/react-native.md), and [Flutter](/docs/session-replay/installation/flutter.md)**.

Mobile session replay enables you to record user sessions in mobile apps. This includes screen recordings, network requests, logs, and touches. This data can then be used to understand how users are interacting with your app and to identify bugs and issues.

## How it works

We have taken our time to make sure we provide a useful and detailed recording experience whilst keeping the performance and security of your app as a top priority. By default, the configuration is restrictive with automatic masking.

### Wireframe mode (default)

Mobile recording is primarily done using native APIs to grab the view hierarchy state when the screen is drawn. This is done carefully so as not to affect performance in any way a user may notice.

The view hierarchy is transformed to a JSON data structure and later rendered as an HTML [wireframe](https://www.figma.com/resource-library/what-is-wireframing/). Since it is a wireframe, the UI won't have the original look and feel but it should be close enough to understand the user's behavior.

Below is an example of a screen captured in wireframe mode in Android:

### Screenshot mode

If `screenshot` (Android) or `screenshotMode` (iOS) option is enabled, the SDK will take a screenshot of the screen instead of a wireframe representation. The screenshot may contain sensitive information, so proceed with caution and ensure you're masking all relevant views.

Below is an example of a screen captured in screenshot mode in Android:

## Next steps

-   [Android session replay](/docs/session-replay/android.md)
-   [iOS session replay](/docs/session-replay/ios.md)
-   [React Native session replay](/docs/session-replay/react-native.md)
-   [Flutter session replay](/docs/session-replay/flutter.md)

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better
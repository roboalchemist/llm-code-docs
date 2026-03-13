# Source: https://docs.logrocket.com/reference/webviews-on-react-native.md

# Capturing Web Views

Display the contents of a WebView component in React-Native recordings

<HTMLBlock>
  {`
  If your React Native app uses a
  <a href="https://reactnative.dev/docs/0.60/webview" target="_blank">web view</a>
  to render content from a URL, the view’s contents will be included in the mobile
  session playback as long as the following is true:
  `}
</HTMLBlock>

* The app is on version 1.18.1 or higher of the mobile SDK
* The React-Native SDK has been initialized in the mobile app ([see docs](https://docs.logrocket.com/reference/react-native))
* The web SDK is initialized in the rendered web page, using the same app ID as the surrounding mobile session ([see docs](https://docs.logrocket.com/reference/init))
* **note:** In order to record web view content on Android devices, the view must given a `nativeID` attribute and be registered with the LogRocket SDK in order to link the web and mobile sessions. See an example of this below:

```javascript
const viewID = 'my_webview';

if (Platform.OS === 'android') {
  LogRocket.registerWebView(viewID);
}
return (
  <WebView
    nativeID={viewID}
    source={{ uri: 'http://docs.logrocket.com' }}
  />
);
```

The events we record for web sessions (clicks, site navigation, etc.) will appear alongside mobile events in session playback. The linked recordings will only count as a single session against your quota.
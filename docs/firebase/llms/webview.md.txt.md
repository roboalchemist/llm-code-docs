# Source: https://firebase.google.com/docs/analytics/webview.md.txt

<br />

Calls to log events or set user properties fired from within a WebView must be forwarded to native code before they can be sent to Google Analytics.

## Implement JavaScript handler

The first step in using Google Analytics in a WebView is to create JavaScript functions to forward events and user properties to native code. The following example shows how to do this in a way that is compatible with both Android and Apple native code:

```
function logEvent(name, params) {
  if (!name) {
    return;
  }

  if (window.AnalyticsWebInterface) {
    // Call Android interface
    window.AnalyticsWebInterface.logEvent(name, JSON.stringify(params));
  } else if (window.webkit
      && window.webkit.messageHandlers
      && window.webkit.messageHandlers.firebase) {
    // Call iOS interface
    var message = {
      command: 'logEvent',
      name: name,
      parameters: params
    };
    window.webkit.messageHandlers.firebase.postMessage(message);
  } else {
    // No Android or iOS interface found
    console.log("No native APIs found.");
  }
}

function setUserProperty(name, value) {
  if (!name || !value) {
    return;
  }

  if (window.AnalyticsWebInterface) {
    // Call Android interface
    window.AnalyticsWebInterface.setUserProperty(name, value);
  } else if (window.webkit
      && window.webkit.messageHandlers
      && window.webkit.messageHandlers.firebase) {
    // Call iOS interface
    var message = {
      command: 'setUserProperty',
      name: name,
      value: value
   };
    window.webkit.messageHandlers.firebase.postMessage(message);
  } else {
    // No Android or iOS interface found
    console.log("No native APIs found.");
  }
}
```

## Call the JavaScript handler from your WebView

You can properly log events and set user properties from within a WebView by calling the JavaScript functions that you defined in the previous step. The following example shows how to properly log a purchase event and set a user property as an example:

```
function logEventExample() {
   
   // Log an event named "purchase" with parameters
   logEvent("purchase", {
      content_type: "product",
      value: 123,
      currency: "USD",
      quantity: 2,
      items: [{
        item_id: "sample-item-id",
        item_variant: "232323"
      }],
      transaction_id: "1234567"
   });
}

function logUserPropertyExample() {
   // Set a user property named 'favorite_genre'
   setUserProperty("favorite_genre", "comedy")    
}
```

## Implement native interface

You can implement a native interface for
[iOS](https://firebase.google.com/docs/analytics/webview#implement-native-interface-ios) or
[Android](https://firebase.google.com/docs/analytics/webview#implement-native-interface-android).

### iOS

To invoke native Apple code from JavaScript, create a message handler class
conforming to the `WKScriptMessageHandler` protocol. You can make
Google Analytics calls inside the
[`userContentController:didReceiveScriptMessage:`](https://developer.apple.com/reference/webkit/wkscriptmessagehandler/1396222-usercontentcontroller?language=objc)
callback:

### Swift


**Note:** This Firebase product is not available on the macOS target.

```swift
func userContentController(_ userContentController: WKUserContentController,
                         didReceive message: WKScriptMessage) {
  guard let body = message.body as? [String: Any] else { return }
  guard let command = body["command"] as? String else { return }
  guard let name = body["name"] as? String else { return }

  if command == "setUserProperty" {
    guard let value = body["value"] as? String else { return }
    Analytics.setUserProperty(value, forName: name)
  } else if command == "logEvent" {
    guard let params = body["parameters"] as? [String: NSObject] else { return }
    Analytics.logEvent(name, parameters: params)
  }
}
```

### Objective-C

```objective-c
- (void)userContentController:(WKUserContentController *)userContentController
      didReceiveScriptMessage:(WKScriptMessage *)message {
  if ([message.body[@"command"] isEqual:@"setUserProperty"]) {
    [FIRAnalytics setUserPropertyString:message.body[@"value"] forName:message.body[@"name"]];
  } else if ([message.body[@"command"] isEqual: @"logEvent"]) {
    [FIRAnalytics logEventWithName:message.body[@"name"] parameters:message.body[@"parameters"]];
  }
}
```

Finally, add the message handler to the webview's user content controller:

### Swift


**Note:** This Firebase product is not available on the macOS target.

```swift
self.webView.configuration.userContentController.add(self, name: "firebase")
```

### Objective-C


**Note:** This Firebase product is not available on the macOS target.

```objective-c
[self.webView.configuration.userContentController addScriptMessageHandler:self
                                                                     name:@"firebase"];
```

### Android

To invoke native Android code from JavaScript, implement a class with
methods marked `@JavaScriptInterface`:

```
public class AnalyticsWebInterface {

    public static final String TAG = "AnalyticsWebInterface";
    private FirebaseAnalytics mAnalytics;

    public AnalyticsWebInterface(Context context) {
        mAnalytics = FirebaseAnalytics.getInstance(context);
    }

    @JavascriptInterface
    public void logEvent(String name, String jsonParams) {
        LOGD("logEvent:" + name);
        mAnalytics.logEvent(name, bundleFromJson(jsonParams));
    }

    @JavascriptInterface
    public void setUserProperty(String name, String value) {
        LOGD("setUserProperty:" + name);
        mAnalytics.setUserProperty(name, value);
    }

    private void LOGD(String message) {
        // Only log on debug builds, for privacy
        if (BuildConfig.DEBUG) {
            Log.d(TAG, message);
        }
    }

    private Bundle bundleFromJson(String json) {
        // ...
    }

}
```

Once you have created the native interface, register it with your WebView
so that it is visible to JavaScript code running in the WebView:

```
// Only add the JavaScriptInterface on API version JELLY_BEAN_MR1 and above, due to
// security concerns, see link below for more information:
// https://developer.android.com/reference/android/webkit/WebView.html#addJavascriptInterface(java.lang.Object,%20java.lang.String)
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.JELLY_BEAN_MR1) {
    mWebView.addJavascriptInterface(
            new AnalyticsWebInterface(this), AnalyticsWebInterface.TAG);
} else {
    Log.w(TAG, "Not adding JavaScriptInterface, API Version: " + Build.VERSION.SDK_INT);
}
```

## Log in-app purchase events manually in a WebView on iOS

You can manually log IAP events in a WebView using Analytics SDK v12.5.0 or
higher.

    function logManualPurchaseEvent() {
      // For manually tracking in-app purchases within a WebView, log the in-app purchase event:
      logEvent("in_app_purchase", {
        currency: "USD",
        price: 0.99,
        product_id: "prod_123",
        product_name: "Product 123",
        quantity: 1,
        value: 0.99,
      });
    }

Note that the SDK will continue to automatically log in-app purchases where
possible, and won't de-duplicate any manually logged in-app purchase events.

## Next Steps

For a fully functional implementation of Google Analytics in a WebView,
see the [analytics-webview](https://github.com/firebase/analytics-webview)
sample.
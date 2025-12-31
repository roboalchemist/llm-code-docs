# Source: https://firebase.google.com/docs/analytics/webview.md.txt

iOS+Android  

<br />

Calls to log events or set user properties fired from within a WebView must be forwarded to native code before they can be sent toGoogle Analytics.

## Implement JavaScript handler

The first step in usingGoogle Analyticsin a WebView is to create JavaScript functions to forward events and user properties to native code. The following example shows how to do this in a way that is compatible with both Android and Apple native code:  

```gdscript
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
}https://github.com/FirebaseExtended/analytics-webview/blob/79ca8cb28df94241ca64dc3324b5fec82e78e6c1/web/public/index.js#L44-L66
```

## Call the JavaScript handler from your WebView

You can properly log events and set user properties from within a WebView by calling the JavaScript functions that you defined in the previous step. The following example shows how to properly log a purchase event and set a user property as an example:  

```gdscript
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

To invoke native Apple code from JavaScript, create a message handler class conforming to the`WKScriptMessageHandler`protocol. You can makeGoogle Analyticscalls inside the[`userContentController:didReceiveScriptMessage:`](https://developer.apple.com/reference/webkit/wkscriptmessagehandler/1396222-usercontentcontroller?language=objc)callback:  

### Swift

<br />

**Note:**This Firebase product is not available on the macOS target.  

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
}https://github.com/FirebaseExtended/analytics-webview/blob/79ca8cb28df94241ca64dc3324b5fec82e78e6c1/ios/swift/FirebaseAnalyticsWeb/ViewController.swift#L57-L70
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
}https://github.com/FirebaseExtended/analytics-webview/blob/79ca8cb28df94241ca64dc3324b5fec82e78e6c1/ios/objc/FirebaseAnalyticsWeb/ViewController.m#L59-L66
```

Finally, add the message handler to the webview's user content controller:  

### Swift

<br />

**Note:**This Firebase product is not available on the macOS target.  

```swift
self.webView.configuration.userContentController.add(self, name: "firebase")https://github.com/FirebaseExtended/analytics-webview/blob/79ca8cb28df94241ca64dc3324b5fec82e78e6c1/ios/swift/FirebaseAnalyticsWeb/ViewController.swift#L42-L42
```

### Objective-C

<br />

**Note:**This Firebase product is not available on the macOS target.  

```objective-c
[self.webView.configuration.userContentController addScriptMessageHandler:self
                                                                     name:@"firebase"];https://github.com/FirebaseExtended/analytics-webview/blob/79ca8cb28df94241ca64dc3324b5fec82e78e6c1/ios/objc/FirebaseAnalyticsWeb/ViewController.m#L44-L45
```

## Log in-app purchase events manually in a WebView on iOS

You can manually log IAP events in a WebView using Analytics SDK v12.5.0 or higher.  

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

Note that the SDK will continue to automatically log in-app purchases where possible, and won't de-duplicate any manually logged in-app purchase events.

## Next Steps

For a fully functional implementation ofGoogle Analyticsin a WebView, see the[analytics-webview](https://github.com/firebase/analytics-webview)sample.
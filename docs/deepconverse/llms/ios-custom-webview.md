# Source: https://docs.deepconverse.com/product-docs/chatbots/deploy/ios-sdk/ios-custom-webview.md

# iOS (Custom Webview)

In cases where the implementation of the chatbot requires customization of the UI or app elements its recommended to implement a custom webview.&#x20;

We provide our open source SDK for reference. You can find it here on our [Github](https://github.com/converselabs/ios-sdk).

### Webview&#x20;

You can load the webview with the following URL which is configured to auto open the chatbot on receiving the trigger event.&#x20;

```url
https://cdn.deepconverse.com/v1/assets/widget/embedded-chatbot?hostname=<SUBDOMAIN>-<BOT_ID>.deepconverse.com
```

Once your webview has been created with this URL on click of a button or any other action which loads the URL you will invoke the following Javascript in the webview.

```swift
// Load the chatbot with Metadata
private func actionButtonJs() -> String {
    do {
        var metadataJSON = json(from: self.session.metadata)
        print("[DeepConverseSDK] Metadata:", metadataJSON)
        let s = """
    setTimeout(function () {var evt = new CustomEvent('botWidgetInit', { detail: \(metadataJSON!) });document.dispatchEvent(evt);}, 100)

    document.addEventListener('dc.bot', function(e) {
      let payload = { action: e.detail.action };
      window.webkit.messageHandlers.actionTapped.postMessage(payload);
    });
    """
        return s;
    } catch {
        print("[DeepConverseSDK] Error in Metadata" + error.localizedDescription);
        
        // Fallback to load without metadata
        
        let s = """
        setTimeout(function () {var evt = new CustomEvent('botWidgetInit', { detail: {} });document.dispatchEvent(evt);}, 100)
    
        document.addEventListener('dc.bot', function(e) {
          let payload = { action: e.detail.action };
          window.webkit.messageHandlers.actionTapped.postMessage(payload);
        });
        """
        return s;
    }


}
```

Here is the example of how to configure the webview and use the above function.

```swift
// Some code
private func configureWebview() {

    let webConfiguration = WKWebViewConfiguration()
    let contentController = WKUserContentController()
    let js: String = actionButtonJs();
    let userScript = WKUserScript(source: js, injectionTime: WKUserScriptInjectionTime.atDocumentEnd, forMainFrameOnly: false)
    contentController.removeAllUserScripts()
    contentController.addUserScript(userScript)
    contentController.add(
                self,
                name: "actionTapped"
            )
    webConfiguration.userContentController = contentController

    self.webview = WKWebView(frame: self.view.frame, configuration: webConfiguration)
    self.webview.navigationDelegate = self
    self.view.addSubview(self.webview)

    self.webview.scrollView.isScrollEnabled = false
    let webRequest = URLRequest(url: url,
                                cachePolicy: .useProtocolCachePolicy,
                                timeoutInterval: timeout)

    let layoutGuide = self.view.safeAreaLayoutGuide
    self.webview.translatesAutoresizingMaskIntoConstraints = false
    self.webview.leadingAnchor.constraint(
          equalTo: layoutGuide.leadingAnchor).isActive = true
    self.webview.trailingAnchor.constraint(
          equalTo: layoutGuide.trailingAnchor).isActive = true
    self.webview.topAnchor.constraint(
          equalTo: layoutGuide.topAnchor).isActive = true
    self.webview.bottomAnchor.constraint(
          equalTo: layoutGuide.bottomAnchor).isActive = true

    self.webview.load(webRequest)

    DispatchQueue.main.asyncAfter(deadline: .now() + timeout) {
        if (self.webview.isLoading) {
            self.webview.stopLoading()
            self.delegate.didWebViewFail(withError: DeepConverseWebHostError.WebViewTimeout)
        }
    }
}
```

We also provide callbacks to assist closing the webview.

In the above code snippet we register the `actionTapped` handler to listen to the callbacks. Three main actions are sent back in `open`, `minimize`, `close`

```swift
// Some code
extension DeepConverseHostViewController : WKScriptMessageHandler {
    public func userContentController (
        _ userContentController: WKUserContentController,
        didReceive message: WKScriptMessage
    ) {
        do {
            print("[DeepConverseSDK] message:", message.body);
            guard let payload = message.body as? [String: String] else { return }
            print("struct:", payload["action"])

            switch (payload["action"]) {
            case "open":
                print("[DeepConverseSDK] open action");
                break;
            case "minimize":
                print("[DeepConverseSDK] minimize action")
                self.dismiss(animated: true, completion: nil);
                break;
           case "close":
                print("[DeepConverseSDK] close action");
                break;
            default:
                print("[DeepConverseSDK] unknown action")
            }

            delegate.didReceiveEvent(event: payload)
        } catch {
            print("[DeepConverseSDK] Event error")
        }
    }
}
```

With the webview configured you can use now have the custom view controller as child or top level container as required in your app.&#x20;

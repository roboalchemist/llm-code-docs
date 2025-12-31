# Source: https://docs.deepconverse.com/product-docs/chatbots/deploy/ios-sdk.md

# iOS SDK

DeepConverse provides an easy to use SDK for integrating the chatbot into your app. To setup the SDK follow the steps below.

### Installation

You can include the SDK by using ***Cocoapods*** and adding this into your ***Podfile***

```
pod 'DeepConverse', :git => 'https://github.com/converselabs/ios-sdk.git', :branch => 'release'
```

### Setup

Here is a sample ViewController showing how you can include the SDK and load the bot on the click action of a button. You can also pass in metadata to the chatbot.

You will require ***DOMAIN*** and ***BOT\_NAME*** which can be found from the dashboard.

<pre><code><strong>import UIKit
</strong>
<strong>import DeepConverse
</strong>
<strong>class ViewController: UIViewController {
</strong>
<strong>    private var sdk : DeepConverseSDK? = nil  
</strong>
<strong>    override func viewDidLoad() {
</strong><strong>        super.viewDidLoad()
</strong>        // Do any additional setup after loading the view.
<strong>        var metadata = [String:String]()
</strong>        metadata["draft"] = "true"

<strong>        let session = DeepConverseSDKSession.init(
</strong>            subDomain: &#x3C;DOMAIN>,
            botName: &#x3C;BOT_NAME>,
            metadata: metadata,
            webViewTimeout: 60.0
        )

<strong>        sdk = DeepConverseSDK(delegate: self, session: session)
</strong>    }

    

<strong>    @IBAction func Click(_ sender: Any) {
</strong><strong>        sdk?.openBot(viewController: self)
</strong>    }
}

<strong>extension ViewController: DeepConverseDelegate {
</strong>
<strong>    func didWebViewFail(withError: DeepConverseWebHostError) {
</strong>        print("Did fail with error")
    }

<strong>    func didReceiveEvent(event: [String : Any]) {
</strong>
    }

<strong>    func didCloseBot() {
</strong>        print("Did Close")
    }

<strong>    func didOpenBot() {
</strong>        print("Did Open")
    }
}
</code></pre>

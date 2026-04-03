# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADInAppPurchaseDelegate.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADInAppPurchaseDelegate.md.txt

# GoogleMobileAds Framework Reference

# GADInAppPurchaseDelegate

    protocol GADInAppPurchaseDelegate : NSObjectProtocol

In-app purchase delegate protocol for custom purchase handling. The delegate must handle the
product purchase flow then call the GADInAppPurchase object's reportPurchaseStatus: method.
- `
  ``
  ``
  `

  ### [didReceive(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADInAppPurchaseDelegate#/c:objc(pl)GADInAppPurchaseDelegate(im)didReceiveInAppPurchase:)

  `
  `  
  Called when the user clicks on the buy button of an in-app purchase ad. After the receiver
  handles the purchase, it must call the GADInAppPurchase object's reportPurchaseStatus: method.  

  #### Declaration

  Swift  

      func didReceive(_ purchase: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADInAppPurchase.html)
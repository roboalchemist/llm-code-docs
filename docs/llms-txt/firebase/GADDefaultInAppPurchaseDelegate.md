# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADDefaultInAppPurchaseDelegate.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADDefaultInAppPurchaseDelegate.md.txt

# GoogleMobileAds Framework Reference

# GADDefaultInAppPurchaseDelegate

    protocol GADDefaultInAppPurchaseDelegate : NSObjectProtocol

In-app purchase delegate protocol for default purchase handling. The delegate must deliver
the purchased item then call the GADDefaultInAppPurchase object's finishTransaction method.
- `
  ``
  ``
  `

  ### [userDidPay(for:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADDefaultInAppPurchaseDelegate#/c:objc(pl)GADDefaultInAppPurchaseDelegate(im)userDidPayForPurchase:)

  `
  `  
  Called when the user successfully paid for a purchase. You must first deliver the purchased
  item to the user, then call defaultInAppPurchase's finishTransaction method.  

  #### Declaration

  Swift  

      func userDidPay(for defaultInAppPurchase: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADDefaultInAppPurchase.html)

- `
  ``
  ``
  `

  ### [shouldStartPurchase(forProductID:quantity:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADDefaultInAppPurchaseDelegate#/c:objc(pl)GADDefaultInAppPurchaseDelegate(im)shouldStartPurchaseForProductID:quantity:)

  `
  `  
  Called when the user clicks on the buy button of an in-app purchase ad. Return YES if the
  default purchase flow should be started to purchase the item, otherwise return NO. If not
  implemented, defaults to YES.  

  #### Declaration

  Swift  

      optional func shouldStartPurchase(forProductID productID: String, quantity: Int) -> Bool
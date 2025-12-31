# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADInAppPurchase.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADInAppPurchase.md.txt

# GoogleMobileAds Framework Reference

# GADInAppPurchase

    class GADInAppPurchase : NSObject

The in-app purchase item to be purchased with the purchase flow handled by you, the
application developer.
Instances of this class are created and passed to your GADInAppPurchaseDelegate object when
users click a buy button. It is important to report the result of the purchase back to the SDK
in order to track metrics about the transaction.
- `
  ``
  ``
  `

  ### [productID](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADInAppPurchase#/c:objc(cs)GADInAppPurchase(py)productID)

  `
  `  
  The in-app purchase product ID.  

  #### Declaration

  Swift  

      var productID: String { get }

- `
  ``
  ``
  `

  ### [quantity](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADInAppPurchase#/c:objc(cs)GADInAppPurchase(py)quantity)

  `
  `  
  The product quantity.  

  #### Declaration

  Swift  

      var quantity: Int { get }

- `
  ``
  ``
  `

  ### [report(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADInAppPurchase#/c:objc(cs)GADInAppPurchase(im)reportPurchaseStatus:)

  `
  `  
  The GADInAppPurchaseDelegate object must call this method after handling the in-app purchase
  for both successful and unsuccessful purchase attempts. This method reports ad conversion and
  purchase status information to Google.  

  #### Declaration

  Swift  

      func report(_ purchaseStatus: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Enums/GADInAppPurchaseStatus.html)
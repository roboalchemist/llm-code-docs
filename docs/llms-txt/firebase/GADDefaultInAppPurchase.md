# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDefaultInAppPurchase.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADDefaultInAppPurchase.md.txt

# GoogleMobileAds Framework Reference

# GADDefaultInAppPurchase

    class GADDefaultInAppPurchase : NSObject

The consumable in-app purchase item that has been purchased by the user. The purchase flow is
handled by the Google Mobile Ads SDK.
Instances of this class are created and passed to your in-app purchase delegate after the user
has successfully paid for a product. Your code must correctly deliver the product to the user
and then call the didCompletePurchase method to finish the transaction.
- `
  ``
  ``
  `

  ### [+enableDefaultPurchaseFlowWithDelegate:](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADDefaultInAppPurchase#/c:objc(cs)GADDefaultInAppPurchase(cm)enableDefaultPurchaseFlowWithDelegate:)

  `
  `  
  Enables the default consumable product in-app purchase flow handled by the Google Mobile Ads
  SDK. The GADDefaultInAppPurchaseDelegate object is retained while the default purchase flow is
  enabled. This method adds a SKPaymentTransactionObserver to the default SKPaymentQueue.

  Call this method early in your application to handle unfinished transactions from previous
  application sessions. For example, call this method in your application delegate's
  application:didFinishLaunchingWithOptions: method.
- `
  ``
  ``
  `

  ### [disableDefaultPurchaseFlow()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADDefaultInAppPurchase#/c:objc(cs)GADDefaultInAppPurchase(cm)disableDefaultPurchaseFlow)

  `
  `  
  Disables the default in-app purchase flow handled by the Google Mobile Ads SDK and releases the
  associated GADDefaultInAppPurchaseDelegate object.  

  #### Declaration

  Swift  

      class func disableDefaultPurchaseFlow()

- `
  ``
  ``
  `

  ### [productID](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADDefaultInAppPurchase#/c:objc(cs)GADDefaultInAppPurchase(py)productID)

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

  ### [quantity](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADDefaultInAppPurchase#/c:objc(cs)GADDefaultInAppPurchase(py)quantity)

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

  ### [paymentTransaction](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADDefaultInAppPurchase#/c:objc(cs)GADDefaultInAppPurchase(py)paymentTransaction)

  `
  `  
  The purchased item's completed payment transaction. Your application can use this property's
  data to save a permanent record of the completed payment. The default purchase flow will finish
  the transaction on your behalf. Do not finish the transaction yourself.  

  #### Declaration

  Swift  

      var paymentTransaction: SKPaymentTransaction { get }

- `
  ``
  ``
  `

  ### [finishTransaction()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADDefaultInAppPurchase#/c:objc(cs)GADDefaultInAppPurchase(im)finishTransaction)

  `
  `  
  The in-app purchase delegate object must first deliver the user's item and then call this
  method. Failure to call this method will result in duplicate purchase notifications.  

  #### Declaration

  Swift  

      func finishTransaction()
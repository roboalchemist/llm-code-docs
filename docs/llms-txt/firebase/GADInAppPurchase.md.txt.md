# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADInAppPurchase.md.txt

# GoogleMobileAds Framework Reference

# GADInAppPurchase


    @interface GADInAppPurchase : NSObject

The in-app purchase item to be purchased with the purchase flow handled by you, the
application developer.
Instances of this class are created and passed to your GADInAppPurchaseDelegate object when
users click a buy button. It is important to report the result of the purchase back to the SDK
in order to track metrics about the transaction.
- `


  ### [productID](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADInAppPurchase#/c:objc(cs)GADInAppPurchase(py)productID)


  ` The in-app purchase product ID.

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic) NSString *_Nonnull productID;

- `


  ### [quantity](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADInAppPurchase#/c:objc(cs)GADInAppPurchase(py)quantity)


  ` The product quantity.

  #### Declaration

  Objective-C

      @property (readonly, assign, nonatomic) NSInteger quantity;

- `


  ### [-reportPurchaseStatus:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADInAppPurchase#/c:objc(cs)GADInAppPurchase(im)reportPurchaseStatus:)


  ` The GADInAppPurchaseDelegate object must call this method after handling the in-app purchase
  for both successful and unsuccessful purchase attempts. This method reports ad conversion and
  purchase status information to Google.

  #### Declaration

  Objective-C

      - (void)reportPurchaseStatus:(https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Enums/GADInAppPurchaseStatus.html)purchaseStatus;
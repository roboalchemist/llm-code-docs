# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedNativeAppInstallAd.md.txt

# GoogleMobileAds Framework Reference

# GADMediatedNativeAppInstallAd

    @protocol GADMediatedNativeAppInstallAd <https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedNativeAd.html>

Provides methods used for constructing native app install ads. The adapter must return an object
conforming to this protocol for native app install ad requests.
- `


  ### [-headline](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedNativeAppInstallAd#/c:objc(pl)GADMediatedNativeAppInstallAd(im)headline)


  ` App title.

  #### Declaration

  Objective-C

      - (nullable NSString *)headline;

- `


  ### [-images](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedNativeAppInstallAd#/c:objc(pl)GADMediatedNativeAppInstallAd(im)images)


  ` Array of GADNativeAdImage objects related to the advertised application.

  #### Declaration

  Objective-C

      - (nullable NSArray<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAdImage.html *> *)images;

- `


  ### [-body](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedNativeAppInstallAd#/c:objc(pl)GADMediatedNativeAppInstallAd(im)body)


  ` App description.

  #### Declaration

  Objective-C

      - (nullable NSString *)body;

- `


  ### [-icon](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedNativeAppInstallAd#/c:objc(pl)GADMediatedNativeAppInstallAd(im)icon)


  ` Application icon.

  #### Declaration

  Objective-C

      - (nullable https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAdImage.html *)icon;

- `


  ### [-callToAction](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedNativeAppInstallAd#/c:objc(pl)GADMediatedNativeAppInstallAd(im)callToAction)


  ` Text that encourages user to take some action with the ad. For example Install.

  #### Declaration

  Objective-C

      - (nullable NSString *)callToAction;

- `


  ### [-starRating](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedNativeAppInstallAd#/c:objc(pl)GADMediatedNativeAppInstallAd(im)starRating)


  ` App store rating (0 to 5).

  #### Declaration

  Objective-C

      - (nullable NSDecimalNumber *)starRating;

- `


  ### [-store](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedNativeAppInstallAd#/c:objc(pl)GADMediatedNativeAppInstallAd(im)store)


  ` The app store name. For example, App Store.

  #### Declaration

  Objective-C

      - (nullable NSString *)store;

- `


  ### [-price](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedNativeAppInstallAd#/c:objc(pl)GADMediatedNativeAppInstallAd(im)price)


  ` String representation of the app's price.

  #### Declaration

  Objective-C

      - (nullable NSString *)price;

- `


  ### [-adChoicesView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedNativeAppInstallAd#/c:objc(pl)GADMediatedNativeAppInstallAd(im)adChoicesView)


  ` AdChoices view.

  #### Declaration

  Objective-C

      - (nullable UIView *)adChoicesView;

- `


  ### [-mediaView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedNativeAppInstallAd#/c:objc(pl)GADMediatedNativeAppInstallAd(im)mediaView)


  ` Media view.

  #### Declaration

  Objective-C

      - (nullable UIView *)mediaView;

- `


  ### [-hasVideoContent](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedNativeAppInstallAd#/c:objc(pl)GADMediatedNativeAppInstallAd(im)hasVideoContent)


  ` Indicates whether the ad has video content.

  #### Declaration

  Objective-C

      - (BOOL)hasVideoContent;
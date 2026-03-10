# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedNativeContentAd.md.txt

# GoogleMobileAds Framework Reference

# GADMediatedNativeContentAd

    @protocol GADMediatedNativeContentAd <https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedNativeAd.html>

Provides methods used for constructing native content ads.
- `


  ### [-headline](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedNativeContentAd#/c:objc(pl)GADMediatedNativeContentAd(im)headline)


  ` Primary text headline.

  #### Declaration

  Objective-C

      - (nullable NSString *)headline;

- `


  ### [-body](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedNativeContentAd#/c:objc(pl)GADMediatedNativeContentAd(im)body)


  ` Secondary text.

  #### Declaration

  Objective-C

      - (nullable NSString *)body;

- `


  ### [-images](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedNativeContentAd#/c:objc(pl)GADMediatedNativeContentAd(im)images)


  ` List of large images. Each object is an instance of GADNativeAdImage.

  #### Declaration

  Objective-C

      - (nullable NSArray<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAdImage.html *> *)images;

- `


  ### [-logo](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedNativeContentAd#/c:objc(pl)GADMediatedNativeContentAd(im)logo)


  ` Small logo image.

  #### Declaration

  Objective-C

      - (nullable https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAdImage.html *)logo;

- `


  ### [-callToAction](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedNativeContentAd#/c:objc(pl)GADMediatedNativeContentAd(im)callToAction)


  ` Text that encourages user to take some action with the ad.

  #### Declaration

  Objective-C

      - (nullable NSString *)callToAction;

- `


  ### [-advertiser](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedNativeContentAd#/c:objc(pl)GADMediatedNativeContentAd(im)advertiser)


  ` Identifies the advertiser. For example, the advertiser's name or visible URL.

  #### Declaration

  Objective-C

      - (nullable NSString *)advertiser;

- `


  ### [-adChoicesView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedNativeContentAd#/c:objc(pl)GADMediatedNativeContentAd(im)adChoicesView)


  ` AdChoices view.

  #### Declaration

  Objective-C

      - (nullable UIView *)adChoicesView;

- `


  ### [-mediaView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedNativeContentAd#/c:objc(pl)GADMediatedNativeContentAd(im)mediaView)


  ` Media view.

  #### Declaration

  Objective-C

      - (nullable UIView *)mediaView;

- `


  ### [-hasVideoContent](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedNativeContentAd#/c:objc(pl)GADMediatedNativeContentAd(im)hasVideoContent)


  ` Indicates whether the ad has video content.

  #### Declaration

  Objective-C

      - (BOOL)hasVideoContent;
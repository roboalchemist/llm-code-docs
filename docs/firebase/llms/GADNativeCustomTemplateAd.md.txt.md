# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeCustomTemplateAd.md.txt

# GoogleMobileAds Framework Reference

# GADNativeCustomTemplateAd

    @interface GADNativeCustomTemplateAd : https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAd.html

Native custom template ad. To request this ad type, you need to pass
kGADAdLoaderAdTypeNativeCustomTemplate (see GADAdLoaderAdTypes.h) to the \|adTypes\| parameter
in GADAdLoader's initializer method. If you request this ad type, your delegate must conform to
the GADNativeCustomTemplateAdLoaderDelegate protocol.
- `


  ### [templateID](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeCustomTemplateAd#/c:objc(cs)GADNativeCustomTemplateAd(py)templateID)


  ` The ad's custom template ID.

  #### Declaration

  Objective-C

      @property (readonly, nonatomic) NSString *_Nonnull templateID;

- `


  ### [availableAssetKeys](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeCustomTemplateAd#/c:objc(cs)GADNativeCustomTemplateAd(py)availableAssetKeys)


  ` Array of available asset keys.

  #### Declaration

  Objective-C

      @property (readonly, nonatomic) NSArray<NSString *> *_Nonnull availableAssetKeys;

- `


  ### [videoController](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeCustomTemplateAd#/c:objc(cs)GADNativeCustomTemplateAd(py)videoController)


  ` Returns video controller for controlling receiver's video.

  #### Declaration

  Objective-C

      @property (readonly, strong, nonatomic)
          https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADVideoController.html *_Nonnull videoController;

- `


  ### [mediaView](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeCustomTemplateAd#/c:objc(cs)GADNativeCustomTemplateAd(py)mediaView)


  ` Returns media view for rendering video loaded by the receiver. Returns nil if receiver doesn't
  has a video.

  #### Declaration

  Objective-C

      @property (readonly, strong, nonatomic, nullable) https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADMediaView.html *mediaView;

- `


  ### [customClickHandler](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeCustomTemplateAd#/c:objc(cs)GADNativeCustomTemplateAd(py)customClickHandler)


  ` Custom click handler. Set this property only if this template ad is configured with a custom
  click action, otherwise set it to nil. If this property is set to a non-nil value, the ad's
  built-in click actions are ignored and \|customClickHandler\| is executed when a click on the
  asset is received.

  #### Declaration

  Objective-C

      @property (readwrite, copy, atomic, nullable)
          https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions.html#/c:GADNativeCustomTemplateAd.h@T@GADNativeAdCustomClickHandler customClickHandler;

- `


  ### [-imageForKey:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeCustomTemplateAd#/c:objc(cs)GADNativeCustomTemplateAd(im)imageForKey:)


  ` Returns the native ad image corresponding to the specified key or nil if the image is not
  available.

  #### Declaration

  Objective-C

      - (nullable https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeAdImage.html *)imageForKey:(nonnull NSString *)key;

- `


  ### [-stringForKey:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeCustomTemplateAd#/c:objc(cs)GADNativeCustomTemplateAd(im)stringForKey:)


  ` Returns the string corresponding to the specified key or nil if the string is not available.

  #### Declaration

  Objective-C

      - (nullable NSString *)stringForKey:(nonnull NSString *)key;

- `


  ### [-performClickOnAssetWithKey:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeCustomTemplateAd#/c:objc(cs)GADNativeCustomTemplateAd(im)performClickOnAssetWithKey:)


  ` Call when the user clicks on the ad. Provide the asset key that best matches the asset the user
  interacted with. If this ad is configured with a custom click action, ensure the receiver's
  customClickHandler property is set before calling this method.

  #### Declaration

  Objective-C

      - (void)performClickOnAssetWithKey:(nonnull NSString *)assetKey;

- `


  ### [-recordImpression](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeCustomTemplateAd#/c:objc(cs)GADNativeCustomTemplateAd(im)recordImpression)


  ` Call when the ad is displayed on screen to the user. Can be called multiple times. Only the
  first impression is recorded.

  #### Declaration

  Objective-C

      - (void)recordImpression;

- `


  ### [-performClickOnAssetWithKey:customClickHandler:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADNativeCustomTemplateAd#/c:objc(cs)GADNativeCustomTemplateAd(im)performClickOnAssetWithKey:customClickHandler:)


  ` Call when the user clicks on the ad. Provide the asset key that best matches the asset the user
  interacted with. Provide \|customClickHandler\| only if this template is configured with a custom
  click action, otherwise pass in nil. If a block is provided, the ad's built-in click actions are
  ignored and \|customClickHandler\| is executed after recording the click.

  This method is deprecated. See performClickOnAssetWithKey: API.

  #### Declaration

  Objective-C

      - (void)performClickOnAssetWithKey:(nonnull NSString *)assetKey
                      customClickHandler:
                          (nullable dispatch_block_t)customClickHandler;
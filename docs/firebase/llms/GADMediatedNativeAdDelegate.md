# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediatedNativeAdDelegate.md.txt

# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedNativeAdDelegate.md.txt

# GoogleMobileAds Framework Reference

# GADMediatedNativeAdDelegate

    @protocol GADMediatedNativeAdDelegate <NSObject>

GADMediatedNativeAdDelegate objects handle mediated native ad events.
- `
  ``
  ``
  `

  ### [-mediatedNativeAd:didRenderInView:clickableAssetViews:nonclickableAssetViews:viewController:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedNativeAdDelegate#/c:objc(pl)GADMediatedNativeAdDelegate(im)mediatedNativeAd:didRenderInView:clickableAssetViews:nonclickableAssetViews:viewController:)

  `
  `  
  Tells the delegate that the mediated native ad has rendered in \|view\| with clickable asset views
  and nonclickable asset views. viewController should be used to present modal views if the ad
  opens full screen.  

  #### Declaration

  Objective-C  

      - (void)mediatedNativeAd:(nonnull id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedNativeAd.html>)mediatedNativeAd
                 didRenderInView:(nonnull UIView *)view
             clickableAssetViews:
                 (nonnull NSDictionary<NSString *, UIView *> *)clickableAssetViews
          nonclickableAssetViews:
              (nonnull NSDictionary<NSString *, UIView *> *)nonclickableAssetViews
                  viewController:(nonnull UIViewController *)viewController;

- `
  ``
  ``
  `

  ### [-mediatedNativeAdDidRecordImpression:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedNativeAdDelegate#/c:objc(pl)GADMediatedNativeAdDelegate(im)mediatedNativeAdDidRecordImpression:)

  `
  `  
  Tells the delegate that the mediated native ad has recorded an impression. This method is called
  only once per mediated native ad.  

  #### Declaration

  Objective-C  

      - (void)mediatedNativeAdDidRecordImpression:
          (nonnull id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedNativeAd.html>)mediatedNativeAd;

- `
  ``
  ``
  `

  ### [-mediatedNativeAd:didRecordClickOnAssetWithName:view:viewController:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedNativeAdDelegate#/c:objc(pl)GADMediatedNativeAdDelegate(im)mediatedNativeAd:didRecordClickOnAssetWithName:view:viewController:)

  `
  `  
  Tells the delegate that the mediated native ad has recorded a user click on the asset named
  \|assetName\|. Full screen actions should be presented from \|viewController\|. This method is
  called only if -\[GADMAdNetworkAdapter handlesUserClicks\] returns NO.  

  #### Declaration

  Objective-C  

      - (void)mediatedNativeAd:(nonnull id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedNativeAd.html>)mediatedNativeAd
          didRecordClickOnAssetWithName:(nonnull NSString *)assetName
                                   view:(nonnull UIView *)view
                         viewController:(nonnull UIViewController *)viewController;

- `
  ``
  ``
  `

  ### [-mediatedNativeAd:didUntrackView:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedNativeAdDelegate#/c:objc(pl)GADMediatedNativeAdDelegate(im)mediatedNativeAd:didUntrackView:)

  `
  `  
  Tells the delegate that the mediated native ad has untracked \|view\|. This method is called
  when the mediatedNativeAd is no longer rendered in the provided view and the delegate should
  stop tracking the view's impressions and clicks. The method may also be called with a nil view
  when the view in which the mediated native ad has rendered is deallocated.  

  #### Declaration

  Objective-C  

      - (void)mediatedNativeAd:(nonnull id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedNativeAd.html>)mediatedNativeAd
                didUntrackView:(nullable UIView *)view;

- `
  ``
  ``
  `

  ### [-mediatedNativeAd:didRenderInView:viewController:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedNativeAdDelegate#/c:objc(pl)GADMediatedNativeAdDelegate(im)mediatedNativeAd:didRenderInView:viewController:)

  `
  `  
  Tells the delegate that the mediated native ad has rendered in \|view\|. viewController should be
  used to present modal views for the ad.  

  #### Declaration

  Objective-C  

      - (void)mediatedNativeAd:(nonnull id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediatedNativeAd.html>)mediatedNativeAd
               didRenderInView:(nonnull UIView *)view
                viewController:(nonnull UIViewController *)viewController;
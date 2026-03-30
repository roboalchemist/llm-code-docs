# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/DFPCustomRenderedBannerViewDelegate.md.txt

# GoogleMobileAds Framework Reference

# DFPCustomRenderedBannerViewDelegate

    @protocol DFPCustomRenderedBannerViewDelegate <NSObject>

The DFPCustomRenderedAd banner view delegate protocol for notifying the delegate of changes to
custom rendered banners.
- `


  ### [-bannerView:didReceiveCustomRenderedAd:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/DFPCustomRenderedBannerViewDelegate#/c:objc(pl)DFPCustomRenderedBannerViewDelegate(im)bannerView:didReceiveCustomRenderedAd:)


  ` Called after ad data has been received. You must construct a banner from \|customRenderedAd\| and
  call the \|customRenderedAd\| object's finishedRenderingAdView: when the ad has been rendered.

  #### Declaration

  Objective-C

      - (void)bannerView:(nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/DFPBannerView.html *)bannerView
          didReceiveCustomRenderedAd:(nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/DFPCustomRenderedAd.html *)customRenderedAd;
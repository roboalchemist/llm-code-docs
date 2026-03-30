# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/DFPCustomRenderedInterstitialDelegate.md.txt

# GoogleMobileAds Framework Reference

# DFPCustomRenderedInterstitialDelegate

    @protocol DFPCustomRenderedInterstitialDelegate <NSObject>

The DFPCustomRenderedAd interstitial delegate protocol for notifying the delegate of changes to
custom rendered interstitials.
- `


  ### [-interstitial:didReceiveCustomRenderedAd:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/DFPCustomRenderedInterstitialDelegate#/c:objc(pl)DFPCustomRenderedInterstitialDelegate(im)interstitial:didReceiveCustomRenderedAd:)


  ` Called after ad data has been received. You must construct an interstitial from
  \|customRenderedAd\| and call the \|customRenderedAd\| object's finishedRenderingAdView: method when
  the ad has been rendered.

  #### Declaration

  Objective-C

      - (void)interstitial:(nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/DFPInterstitial.html *)interstitial
          didReceiveCustomRenderedAd:(nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/DFPCustomRenderedAd.html *)customRenderedAd;
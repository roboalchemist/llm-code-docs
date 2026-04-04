# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADAdLoaderDelegate.md.txt

# GoogleMobileAds Framework Reference

# GADAdLoaderDelegate

    @protocol GADAdLoaderDelegate <NSObject>

Base ad loader delegate protocol. Ad types provide extended protocols that declare methods to
handle successful ad loads.
- `


  ### [-adLoader:didFailToReceiveAdWithError:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADAdLoaderDelegate#/c:objc(pl)GADAdLoaderDelegate(im)adLoader:didFailToReceiveAdWithError:)


  ` Called when adLoader fails to load an ad.

  #### Declaration

  Objective-C

      - (void)adLoader:(nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADAdLoader.html *)adLoader
          didFailToReceiveAdWithError:(nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes.html#/c:objc(cs)GADRequestError *)error;

- `


  ### [-adLoaderDidFinishLoading:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADAdLoaderDelegate#/c:objc(pl)GADAdLoaderDelegate(im)adLoaderDidFinishLoading:)


  ` Called after adLoader has finished loading.

  #### Declaration

  Objective-C

      - (void)adLoaderDidFinishLoading:(nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADAdLoader.html *)adLoader;
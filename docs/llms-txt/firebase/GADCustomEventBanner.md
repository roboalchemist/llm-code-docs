# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADCustomEventBanner.md.txt

# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADCustomEventBanner.md.txt

# GoogleMobileAds Framework Reference

# GADCustomEventBanner

    @protocol GADCustomEventBanner <NSObject>

The banner custom event protocol. Your banner custom event handler must implement this protocol.
- `
  ``
  ``
  `

  ### [delegate](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADCustomEventBanner#/c:objc(pl)GADCustomEventBanner(py)delegate)

  `
  `  
  Inform \|delegate\| with the custom event execution results to ensure mediation behaves correctly.

  In your class, define the -delegate and -setDelegate: methods or use @synthesize delegate. The
  Google Mobile Ads SDK sets this property on instances of your class.  

  #### Declaration

  Objective-C  

      @property (readwrite, nonatomic, nullable) id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADCustomEventBannerDelegate.html>
          delegate;

- `
  ``
  ``
  `

  ### [-requestBannerAd:parameter:label:request:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADCustomEventBanner#/c:objc(pl)GADCustomEventBanner(im)requestBannerAd:parameter:label:request:)

  `
  `  
  Called by mediation when your custom event is scheduled to be executed. Report execution results
  to the delegate.  

  #### Declaration

  Objective-C  

      - (void)requestBannerAd:(https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Structs/GADAdSize.html)adSize
                    parameter:(nullable NSString *)serverParameter
                        label:(nullable NSString *)serverLabel
                      request:(nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADCustomEventRequest.html *)request;

  #### Parameters

  |-------------------------|-----------------------------------------------------------------------------------|
  | ` `*adSize*` `          | The size of the ad as configured in the mediation UI for the mediation placement. |
  | ` `*serverParameter*` ` | Parameter configured in the mediation UI.                                         |
  | ` `*serverLabel*` `     | Label configured in the mediation UI.                                             |
  | ` `*request*` `         | Contains ad request information.                                                  |
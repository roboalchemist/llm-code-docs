# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADCustomEventExtras.md.txt

# GoogleMobileAds Framework Reference

# GADCustomEventExtras

    @interface GADCustomEventExtras : NSObject <https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols.html#/c:objc(pl)GADAdNetworkExtras>

Create an instance of this class to set additional parameters for each custom event object. The
additional parameters for a custom event are keyed by the custom event label. These extras are
passed to your implementation of GADCustomEventBanner or GADCustomEventInterstitial.
- `


  ### [-setExtras:forLabel:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADCustomEventExtras#/c:objc(cs)GADCustomEventExtras(im)setExtras:forLabel:)


  ` Set additional parameters for the custom event with label \|label\|. To remove additional
  parameters associated with \|label\|, pass in nil for \|extras\|.

  #### Declaration

  Objective-C

      - (void)setExtras:(nullable NSDictionary *)extras
               forLabel:(nonnull NSString *)label;

- `


  ### [-extrasForLabel:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADCustomEventExtras#/c:objc(cs)GADCustomEventExtras(im)extrasForLabel:)


  ` Retrieve the extras for \|label\|.

  #### Declaration

  Objective-C

      - (nullable NSDictionary *)extrasForLabel:(nonnull NSString *)label;

- `


  ### [-removeAllExtras](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADCustomEventExtras#/c:objc(cs)GADCustomEventExtras(im)removeAllExtras)


  ` Removes all the extras set on this instance.

  #### Declaration

  Objective-C

      - (void)removeAllExtras;

- `


  ### [-allExtras](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADCustomEventExtras#/c:objc(cs)GADCustomEventExtras(im)allExtras)


  ` Returns all the extras set on this instance.

  #### Declaration

  Objective-C

      - (nonnull NSDictionary *)allExtras;
# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADAdapterStatus.md.txt

# GoogleMobileAds Framework Reference

# GADAdapterStatus

    @interface GADAdapterStatus : NSObject <NSCopying>

An immutable snapshot of a mediation adapter's initialization status.
- `


  ### [state](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADAdapterStatus#/c:objc(cs)GADAdapterStatus(py)state)


  ` Initialization state of the adapter.

  #### Declaration

  Objective-C

      @property (readonly, nonatomic) https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Enums/GADAdapterInitializationState.html state;

- `


  ### [description](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADAdapterStatus#/c:objc(cs)GADAdapterStatus(py)description)


  ` Detailed description of the status.

  #### Declaration

  Objective-C

      @property (readonly, nonatomic, nonnull) NSString *description;

- `


  ### [latency](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADAdapterStatus#/c:objc(cs)GADAdapterStatus(py)latency)


  ` The adapter's initialization latency in seconds. 0 if initialization has not yet ended.

  #### Declaration

  Objective-C

      @property (readonly, nonatomic) NSTimeInterval latency;
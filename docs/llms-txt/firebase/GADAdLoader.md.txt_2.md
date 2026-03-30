# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADAdLoader.md.txt

# GoogleMobileAds Framework Reference

# GADAdLoader

    @interface GADAdLoader : NSObject

Loads ads. See GADAdLoaderAdTypes.h for available ad types.
- `


  ### [delegate](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADAdLoader#/c:objc(cs)GADAdLoader(py)delegate)


  ` Object notified when an ad request succeeds or fails. Must conform to requested ad types'
  delegate protocols.

  #### Declaration

  Objective-C

      @property (readwrite, nonatomic, nullable) id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADAdLoaderDelegate.html> delegate;

- `


  ### [adUnitID](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADAdLoader#/c:objc(cs)GADAdLoader(py)adUnitID)


  ` The ad loader's ad unit ID.

  #### Declaration

  Objective-C

      @property (readonly, nonatomic) NSString *_Nonnull adUnitID;

- `


  ### [loading](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADAdLoader#/c:objc(cs)GADAdLoader(py)loading)


  ` Indicates whether the ad loader is loading.

  #### Declaration

  Objective-C

      @property (readonly, getter=isLoading, nonatomic) BOOL loading;

- `


  ### [-initWithAdUnitID:rootViewController:adTypes:options:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADAdLoader#/c:objc(cs)GADAdLoader(im)initWithAdUnitID:rootViewController:adTypes:options:)


  ` Returns an initialized ad loader configured to load the specified ad types.

  #### Declaration

  Objective-C

      - (nonnull instancetype)
            initWithAdUnitID:(nonnull NSString *)adUnitID
          rootViewController:(nullable UIViewController *)rootViewController
                     adTypes:(nonnull NSArray<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Type-Definitions.html#/c:GADAdLoaderAdTypes.h@T@GADAdLoaderAdType> *)adTypes
                     options:(nullable NSArray<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes.html#/c:objc(cs)GADAdLoaderOptions *> *)options;

  #### Parameters

  |---|---|
  | ` rootViewController ` | The root view controller is used to present ad click actions. |
  | ` adTypes ` | An array of ad types. See GADAdLoaderAdTypes.h for available ad types. |
  | ` options ` | An array of GADAdLoaderOptions objects to configure how ads are loaded, or nil to use default options. See each ad type's header for available GADAdLoaderOptions subclasses. |

- `


  ### [-loadRequest:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADAdLoader#/c:objc(cs)GADAdLoader(im)loadRequest:)


  ` Loads the ad and informs the delegate of the outcome.

  #### Declaration

  Objective-C

      - (void)loadRequest:(nullable https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRequest.html *)request;
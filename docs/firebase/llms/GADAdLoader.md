# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADAdLoader.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADAdLoader.md.txt

# GoogleMobileAds Framework Reference

# GADAdLoader

    class GADAdLoader : NSObject

Loads ads. See GADAdLoaderAdTypes.h for available ad types.
- `
  ``
  ``
  `

  ### [delegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADAdLoader#/c:objc(cs)GADAdLoader(py)delegate)

  `
  `  
  Object notified when an ad request succeeds or fails. Must conform to requested ad types'
  delegate protocols.  

  #### Declaration

  Swift  

      weak var delegate: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADAdLoaderDelegate.html? { get set }

- `
  ``
  ``
  `

  ### [adUnitID](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADAdLoader#/c:objc(cs)GADAdLoader(py)adUnitID)

  `
  `  
  The ad loader's ad unit ID.  

  #### Declaration

  Swift  

      var adUnitID: String { get }

- `
  ``
  ``
  `

  ### [isLoading](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADAdLoader#/c:objc(cs)GADAdLoader(py)loading)

  `
  `  
  Indicates whether the ad loader is loading.  

  #### Declaration

  Swift  

      var isLoading: Bool { get }

- `
  ``
  ``
  `

  ### [init(adUnitID:rootViewController:adTypes:options:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADAdLoader#/c:objc(cs)GADAdLoader(im)initWithAdUnitID:rootViewController:adTypes:options:)

  `
  `  
  Returns an initialized ad loader configured to load the specified ad types.  

  #### Declaration

  Swift  

      init(adUnitID: String, rootViewController: UIViewController?, adTypes: [https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions.html#/c:GADAdLoaderAdTypes.h@T@GADAdLoaderAdType], options: [https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes.html#/c:objc(cs)GADAdLoaderOptions]?)

  #### Parameters

  |----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*rootViewController*` ` | The root view controller is used to present ad click actions.                                                                                                                 |
  | ` `*adTypes*` `            | An array of ad types. See GADAdLoaderAdTypes.h for available ad types.                                                                                                        |
  | ` `*options*` `            | An array of GADAdLoaderOptions objects to configure how ads are loaded, or nil to use default options. See each ad type's header for available GADAdLoaderOptions subclasses. |

- `
  ``
  ``
  `

  ### [load(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADAdLoader#/c:objc(cs)GADAdLoader(im)loadRequest:)

  `
  `  
  Loads the ad and informs the delegate of the outcome.  

  #### Declaration

  Swift  

      func load(_ request: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRequest.html?)
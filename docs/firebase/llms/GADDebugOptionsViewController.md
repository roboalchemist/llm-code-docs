# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDebugOptionsViewController.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADDebugOptionsViewController.md.txt

# GoogleMobileAds Framework Reference

# GADDebugOptionsViewController

    class GADDebugOptionsViewController : UIViewController

Displays debug options to the user.
- `
  ``
  ``
  `

  ### [init(adUnitID:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADDebugOptionsViewController#/c:objc(cs)GADDebugOptionsViewController(cm)debugOptionsViewControllerWithAdUnitID:)

  `
  `  
  Creates and returns a GADDebugOptionsViewController object initialized with the ad unit ID.  

  #### Declaration

  Swift  

      convenience init(adUnitID: String)

  #### Parameters

  |------------------|----------------------------------------------------------------------------------------------|
  | ` `*adUnitID*` ` | An ad unit ID for the Google Ad Manager account that is being configured with debug options. |

- `
  ``
  ``
  `

  ### [delegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADDebugOptionsViewController#/c:objc(cs)GADDebugOptionsViewController(py)delegate)

  `
  `  
  Delegate for the debug options view controller.  

  #### Declaration

  Swift  

      @IBOutlet weak var delegate: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADDebugOptionsViewControllerDelegate.html? { get set }
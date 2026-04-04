# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDebugOptionsViewController.md.txt

# GoogleMobileAds Framework Reference

# GADDebugOptionsViewController

    @interface GADDebugOptionsViewController : UIViewController

Displays debug options to the user.
- `


  ### [+debugOptionsViewControllerWithAdUnitID:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDebugOptionsViewController#/c:objc(cs)GADDebugOptionsViewController(cm)debugOptionsViewControllerWithAdUnitID:)


  ` Creates and returns a GADDebugOptionsViewController object initialized with the ad unit ID.

  #### Declaration

  Objective-C

      + (nonnull instancetype)debugOptionsViewControllerWithAdUnitID:
          (nonnull NSString *)adUnitID;

  #### Parameters

  |---|---|
  | ` adUnitID ` | An ad unit ID for the Google Ad Manager account that is being configured with debug options. |

- `


  ### [delegate](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDebugOptionsViewController#/c:objc(cs)GADDebugOptionsViewController(py)delegate)


  ` Delegate for the debug options view controller.

  #### Declaration

  Objective-C

      @property (readwrite, nonatomic, nullable)
          id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADDebugOptionsViewControllerDelegate.html>
              delegate;
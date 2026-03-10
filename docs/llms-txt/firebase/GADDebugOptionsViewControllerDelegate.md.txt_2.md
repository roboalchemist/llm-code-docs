# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADDebugOptionsViewControllerDelegate.md.txt

# GoogleMobileAds Framework Reference

# GADDebugOptionsViewControllerDelegate

    @protocol GADDebugOptionsViewControllerDelegate <NSObject>

Delegate for the GADDebugOptionsViewController.
- `


  ### [-debugOptionsViewControllerDidDismiss:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADDebugOptionsViewControllerDelegate#/c:objc(pl)GADDebugOptionsViewControllerDelegate(im)debugOptionsViewControllerDidDismiss:)


  ` Called when the debug options flow is finished.

  #### Declaration

  Objective-C

      - (void)debugOptionsViewControllerDidDismiss:
          (nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADDebugOptionsViewController.html *)controller;
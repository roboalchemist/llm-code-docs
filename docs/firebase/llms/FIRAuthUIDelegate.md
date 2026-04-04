# Source: https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Protocols/FIRAuthUIDelegate.md.txt

# FirebaseAuth Framework Reference

# FIRAuthUIDelegate

    @protocol FIRAuthUIDelegate <NSObject>

@protocol FIRAuthUIDelegate
A protocol to handle user interface interactions for Firebase Auth.
This protocol is available on iOS, macOS Catalyst, and tvOS only.
- `
  ``
  ``
  `

  ### [-presentViewController:animated:completion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Protocols/FIRAuthUIDelegate#/c:objc(pl)FIRAuthUIDelegate(im)presentViewController:animated:completion:)

  `
  `  
  If implemented, this method will be invoked when Firebase Auth needs to display a view
  controller.  

  #### Declaration

  Objective-C  

      - (void)presentViewController:
                  (nonnull UIViewController *)viewControllerToPresent
                           animated:(BOOL)flag
                         completion:(void (^_Nullable)(void))completion;

  #### Parameters

  |---------------------------------|---------------------------------------------------------------------------------------------------------------|
  | ` `*viewControllerToPresent*` ` | The view controller to be presented.                                                                          |
  | ` `*flag*` `                    | Decides whether the view controller presentation should be animated or not.                                   |
  | ` `*completion*` `              | The block to execute after the presentation finishes. This block has no return value and takes no parameters. |

- `
  ``
  ``
  `

  ### [-dismissViewControllerAnimated:completion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Protocols/FIRAuthUIDelegate#/c:objc(pl)FIRAuthUIDelegate(im)dismissViewControllerAnimated:completion:)

  `
  `  
  If implemented, this method will be invoked when Firebase Auth needs to display a view
  controller.  

  #### Declaration

  Objective-C  

      - (void)dismissViewControllerAnimated:(BOOL)flag
                                 completion:(void (^_Nullable)(void))completion;

  #### Parameters

  |--------------------|---------------------------------------------------------------------------------------------------------------|
  | ` `*flag*` `       | Decides whether removing the view controller should be animated or not.                                       |
  | ` `*completion*` ` | The block to execute after the presentation finishes. This block has no return value and takes no parameters. |
# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols/AuthUIDelegate.md.txt

# FirebaseAuth Framework Reference

# AuthUIDelegate

    @objc(FIRAuthUIDelegate)
    public protocol AuthUIDelegate : NSObjectProtocol

A protocol to handle user interface interactions for Firebase Auth.

This protocol is available on iOS, macOS Catalyst, and tvOS only.
- `
  ``
  ``
  `

  ### [present(_:animated:completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols/AuthUIDelegate#/c:@M@FirebaseAuth@objc(pl)FIRAuthUIDelegate(im)presentViewController:animated:completion:)

  `
  `  
  If implemented, this method will be invoked when Firebase Auth needs to display a view
  controller.  

  #### Declaration

  Swift  

      @objc(presentViewController:animated:completion:)
      func present(_ viewControllerToPresent: UIViewController,
                   animated flag: Bool,
                   completion: (() -> Void)?)

  #### Parameters

  |---------------------------------|---------------------------------------------------------------------------------------------------------------|
  | ` `*viewControllerToPresent*` ` | The view controller to be presented.                                                                          |
  | ` `*flag*` `                    | Decides whether the view controller presentation should be animated.                                          |
  | ` `*completion*` `              | The block to execute after the presentation finishes. This block has no return value and takes no parameters. |

- `
  ``
  ``
  `

  ### [dismiss(animated:completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Protocols/AuthUIDelegate#/c:@M@FirebaseAuth@objc(pl)FIRAuthUIDelegate(im)dismissViewControllerAnimated:completion:)

  `
  `  
  If implemented, this method will be invoked when Firebase Auth needs to display a view
  controller.  

  #### Declaration

  Swift  

      @objc(dismissViewControllerAnimated:completion:)
      func dismiss(animated flag: Bool, completion: (() -> Void)?)

  #### Parameters

  |--------------------|---------------------------------------------------------------------------------------------------------------|
  | ` `*flag*` `       | Decides whether removing the view controller should be animated or not.                                       |
  | ` `*completion*` ` | The block to execute after the presentation finishes. This block has no return value and takes no parameters. |
# Source: https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingActionButton.md.txt

# Source: https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingActionButton.md.txt

# FirebaseInAppMessaging Framework Reference

# FIRInAppMessagingActionButton


    @interface FIRInAppMessagingActionButton : NSObject

Contains the display information for an action button. This class is unavailable on macOS,

- macOS Catalyst, and watchOS.
- `
  ``
  ``
  `

  ### [buttonText](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingActionButton#/c:objc(cs)FIRInAppMessagingActionButton(py)buttonText)

  `
  `  
  Gets the text string for the button  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly, nonnull) NSString *buttonText;

- `
  ``
  ``
  `

  ### [buttonTextColor](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingActionButton#/c:objc(cs)FIRInAppMessagingActionButton(py)buttonTextColor)

  `
  `  
  Gets the button's text color.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly, nonnull) UIColor *buttonTextColor;

- `
  ``
  ``
  `

  ### [buttonBackgroundColor](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingActionButton#/c:objc(cs)FIRInAppMessagingActionButton(py)buttonBackgroundColor)

  `
  `  
  Gets the button's background color  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly, nonnull) UIColor *buttonBackgroundColor;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingActionButton#/c:objc(cs)FIRInAppMessagingActionButton(im)init)

  `
  `  
  Unavailable  
  Unavailable.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;

- `
  ``
  ``
  `

  ### [-initWithButtonText:buttonTextColor:backgroundColor:](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingActionButton#/c:objc(cs)FIRInAppMessagingActionButton(im)initWithButtonText:buttonTextColor:backgroundColor:)

  `
  `  
  Exposed for unit testing only, or for use in SwiftUI previews. Don't instantiate this in your
  app directly.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)initWithButtonText:(nonnull NSString *)buttonText
                                 buttonTextColor:(nonnull UIColor *)textColor
                                 backgroundColor:(nonnull UIColor *)backgroundColor;
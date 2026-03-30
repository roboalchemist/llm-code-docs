# Source: https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingActionButton.md.txt

# FirebaseInAppMessagingDisplay Framework Reference

# FIRInAppMessagingActionButton


    @interface FIRInAppMessagingActionButton : NSObject

Contains the display information for an action button.
- `


  ### [buttonText](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingActionButton#/c:objc(cs)FIRInAppMessagingActionButton(py)buttonText)


  ` Gets the text string for the button

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nonnull) NSString *buttonText;

- `


  ### [buttonTextColor](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingActionButton#/c:objc(cs)FIRInAppMessagingActionButton(py)buttonTextColor)


  ` Gets the button's text color.

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nonnull) UIColor *buttonTextColor;

- `


  ### [buttonBackgroundColor](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingActionButton#/c:objc(cs)FIRInAppMessagingActionButton(py)buttonBackgroundColor)


  ` Gets the button's background color

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nonnull) UIColor *buttonBackgroundColor;

- `


  ### [-init](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingActionButton#/c:objc(cs)FIRInAppMessagingActionButton(im)init)


  ` Unavailable.

  #### Declaration

  Objective-C

      - (nonnull instancetype)init;

- `


  ### [-initWithButtonText:buttonTextColor:backgroundColor:](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingActionButton#/c:objc(cs)FIRInAppMessagingActionButton(im)initWithButtonText:buttonTextColor:backgroundColor:)


  ` Deprecated, this class shouldn't be directly instantiated.

  #### Declaration

  Objective-C

      - (nonnull instancetype)initWithButtonText:(nonnull NSString *)btnText
                                 buttonTextColor:(nonnull UIColor *)textColor
                                 backgroundColor:(nonnull UIColor *)bkgColor;
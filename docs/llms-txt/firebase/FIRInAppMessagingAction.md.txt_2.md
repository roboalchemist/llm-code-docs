# Source: https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingAction.md.txt

# FirebaseInAppMessagingDisplay Framework Reference

# FIRInAppMessagingAction


    @interface FIRInAppMessagingAction : NSObject

Defines the metadata for a FIAM action.
- `


  ### [actionText](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingAction#/c:objc(cs)FIRInAppMessagingAction(py)actionText)


  ` The text of the action button, if applicable.

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nullable) NSString *actionText;

- `


  ### [actionURL](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingAction#/c:objc(cs)FIRInAppMessagingAction(py)actionURL)


  ` The URL to follow if the action is clicked.

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nonnull) NSURL *actionURL;

- `


  ### [-init](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingAction#/c:objc(cs)FIRInAppMessagingAction(im)init)


  ` Unavailable.

  #### Declaration

  Objective-C

      - (nonnull instancetype)init;

- `


  ### [-initWithActionText:actionURL:](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingAction#/c:objc(cs)FIRInAppMessagingAction(im)initWithActionText:actionURL:)


  ` This class should only be initialized from a custom in-app message UI component implementation.

  #### Declaration

  Objective-C

      - (nonnull instancetype)initWithActionText:(nullable NSString *)actionText
                                       actionURL:(nonnull NSURL *)actionURL;
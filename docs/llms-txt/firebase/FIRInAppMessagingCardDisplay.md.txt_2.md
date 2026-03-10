# Source: https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingCardDisplay.md.txt

# FirebaseInAppMessagingDisplay Framework Reference

# FIRInAppMessagingCardDisplay


    @interface FIRInAppMessagingCardDisplay : https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingDisplayMessage.html

Undocumented
- `


  ### [title](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingCardDisplay#/c:objc(cs)FIRInAppMessagingCardDisplay(py)title)


  ` Gets the title text for a card FIAM message.

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nonnull) NSString *title;

- `


  ### [body](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingCardDisplay#/c:objc(cs)FIRInAppMessagingCardDisplay(py)body)


  ` Gets the body text for a card FIAM message.

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nullable) NSString *body;

- `


  ### [textColor](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingCardDisplay#/c:objc(cs)FIRInAppMessagingCardDisplay(py)textColor)


  ` Gets the color for text in card FIAM message. It applies to both title and body text.

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nonnull) UIColor *textColor;

- `


  ### [portraitImageData](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingCardDisplay#/c:objc(cs)FIRInAppMessagingCardDisplay(py)portraitImageData)


  ` Image data for the supplied portrait image for a card FIAM messasge.

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nonnull)
          https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingImageData.html *portraitImageData;

- `


  ### [landscapeImageData](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingCardDisplay#/c:objc(cs)FIRInAppMessagingCardDisplay(py)landscapeImageData)


  ` Image data for the supplied landscape image for a card FIAM message.

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nullable)
          https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingImageData.html *landscapeImageData;

- `


  ### [displayBackgroundColor](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingCardDisplay#/c:objc(cs)FIRInAppMessagingCardDisplay(py)displayBackgroundColor)


  ` The background color for a card FIAM message.

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic, nonnull) UIColor *displayBackgroundColor;

- `


  ### [primaryActionButton](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingCardDisplay#/c:objc(cs)FIRInAppMessagingCardDisplay(py)primaryActionButton)


  ` Metadata for a card FIAM message's primary action button.

  #### Declaration

  Objective-C

      @property (readonly, nonatomic, nonnull)
          https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingActionButton.html *primaryActionButton;

- `


  ### [primaryActionURL](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingCardDisplay#/c:objc(cs)FIRInAppMessagingCardDisplay(py)primaryActionURL)


  ` The action URL for a card FIAM message's primary action button.

  #### Declaration

  Objective-C

      @property (readonly, nonatomic, nonnull) NSURL *primaryActionURL;

- `


  ### [secondaryActionButton](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingCardDisplay#/c:objc(cs)FIRInAppMessagingCardDisplay(py)secondaryActionButton)


  ` Metadata for a card FIAM message's secondary action button.

  #### Declaration

  Objective-C

      @property (readonly, nonatomic, nullable)
          https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingActionButton.html *secondaryActionButton;

- `


  ### [secondaryActionURL](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingCardDisplay#/c:objc(cs)FIRInAppMessagingCardDisplay(py)secondaryActionURL)


  ` The action URL for a card FIAM message's secondary action button.

  #### Declaration

  Objective-C

      @property (readonly, nonatomic, nullable) NSURL *secondaryActionURL;

- `


  ### [-init](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingCardDisplay#/c:objc(cs)FIRInAppMessagingCardDisplay(im)init)


  ` Unavailable.

  #### Declaration

  Objective-C

      - (nonnull instancetype)init;
# Source: https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingCardDisplay.md.txt

# FirebaseInAppMessaging Framework Reference

# InAppMessagingCardDisplay

    class InAppMessagingCardDisplay : https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingDisplayMessage.html

A displayable in-app card message.
This class is unavailable on macOS, macOS Catalyst, and watchOS.
- `


  ### [title](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingCardDisplay#/c:objc(cs)FIRInAppMessagingCardDisplay(py)title)


  ` Gets the title text for a card FIAM message.

  #### Declaration

  Swift

      var title: String { get }

- `


  ### [body](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingCardDisplay#/c:objc(cs)FIRInAppMessagingCardDisplay(py)body)


  ` Gets the body text for a card FIAM message.

  #### Declaration

  Swift

      var body: String? { get }

- `


  ### [textColor](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingCardDisplay#/c:objc(cs)FIRInAppMessagingCardDisplay(py)textColor)


  ` Gets the color for text in card FIAM message. It applies to both title and body text.

  #### Declaration

  Swift

      @NSCopying var textColor: UIColor { get }

- `


  ### [portraitImageData](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingCardDisplay#/c:objc(cs)FIRInAppMessagingCardDisplay(py)portraitImageData)


  ` Image data for the supplied portrait image for a card FIAM messasge.

  #### Declaration

  Swift

      @NSCopying var portraitImageData: https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingImageData.html { get }

- `


  ### [landscapeImageData](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingCardDisplay#/c:objc(cs)FIRInAppMessagingCardDisplay(py)landscapeImageData)


  ` Image data for the supplied landscape image for a card FIAM message.

  #### Declaration

  Swift

      @NSCopying var landscapeImageData: https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingImageData.html? { get }

- `


  ### [displayBackgroundColor](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingCardDisplay#/c:objc(cs)FIRInAppMessagingCardDisplay(py)displayBackgroundColor)


  ` The background color for a card FIAM message.

  #### Declaration

  Swift

      @NSCopying var displayBackgroundColor: UIColor { get }

- `


  ### [primaryActionButton](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingCardDisplay#/c:objc(cs)FIRInAppMessagingCardDisplay(py)primaryActionButton)


  ` Metadata for a card FIAM message's primary action button.

  #### Declaration

  Swift

      var primaryActionButton: https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingActionButton.html { get }

- `


  ### [primaryActionURL](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingCardDisplay#/c:objc(cs)FIRInAppMessagingCardDisplay(py)primaryActionURL)


  ` The action URL for a card FIAM message's primary action button.

  #### Declaration

  Swift

      var primaryActionURL: URL? { get }

- `


  ### [secondaryActionButton](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingCardDisplay#/c:objc(cs)FIRInAppMessagingCardDisplay(py)secondaryActionButton)


  ` Metadata for a card FIAM message's secondary action button.

  #### Declaration

  Swift

      var secondaryActionButton: https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingActionButton.html? { get }

- `


  ### [secondaryActionURL](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingCardDisplay#/c:objc(cs)FIRInAppMessagingCardDisplay(py)secondaryActionURL)


  ` The action URL for a card FIAM message's secondary action button.

  #### Declaration

  Swift

      var secondaryActionURL: URL? { get }

- `


  ### [-init](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingCardDisplay#/c:objc(cs)FIRInAppMessagingCardDisplay(im)init)


  ` Unavailable
  Unavailable.
- `


  ### [init(campaignName:titleText:bodyText:textColor:portraitImageData:landscapeImageData:backgroundColor:primaryActionButton:secondaryActionButton:primaryActionURL:secondaryActionURL:appData:)](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingCardDisplay#/c:objc(cs)FIRInAppMessagingCardDisplay(im)initWithCampaignName:titleText:bodyText:textColor:portraitImageData:landscapeImageData:backgroundColor:primaryActionButton:secondaryActionButton:primaryActionURL:secondaryActionURL:appData:)


  ` Exposed for unit testing only, or for use in SwiftUI previews. Don't instantiate this in your
  app directly.

  #### Declaration

  Swift

      init(campaignName: String, titleText title: String, bodyText: String?, textColor: UIColor, portraitImageData: https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingImageData.html, landscapeImageData: https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingImageData.html?, backgroundColor: UIColor, primaryActionButton: https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingActionButton.html, secondaryActionButton: https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingActionButton.html?, primaryActionURL: URL?, secondaryActionURL: URL?, appData: [AnyHashable : Any]?)
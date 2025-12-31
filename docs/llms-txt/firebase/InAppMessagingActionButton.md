# Source: https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingActionButton.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingActionButton.md.txt

# FirebaseInAppMessaging Framework Reference

# InAppMessagingActionButton

    class InAppMessagingActionButton : NSObject

Contains the display information for an action button. This class is unavailable on macOS,

- macOS Catalyst, and watchOS.
- `
  ``
  ``
  `

  ### [buttonText](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingActionButton#/c:objc(cs)FIRInAppMessagingActionButton(py)buttonText)

  `
  `  
  Gets the text string for the button  

  #### Declaration

  Swift  

      var buttonText: String { get }

- `
  ``
  ``
  `

  ### [buttonTextColor](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingActionButton#/c:objc(cs)FIRInAppMessagingActionButton(py)buttonTextColor)

  `
  `  
  Gets the button's text color.  

  #### Declaration

  Swift  

      @NSCopying var buttonTextColor: UIColor { get }

- `
  ``
  ``
  `

  ### [buttonBackgroundColor](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingActionButton#/c:objc(cs)FIRInAppMessagingActionButton(py)buttonBackgroundColor)

  `
  `  
  Gets the button's background color  

  #### Declaration

  Swift  

      @NSCopying var buttonBackgroundColor: UIColor { get }

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingActionButton#/c:objc(cs)FIRInAppMessagingActionButton(im)init)

  `
  `  
  Unavailable  
  Unavailable.
- `
  ``
  ``
  `

  ### [init(buttonText:buttonTextColor:backgroundColor:)](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingActionButton#/c:objc(cs)FIRInAppMessagingActionButton(im)initWithButtonText:buttonTextColor:backgroundColor:)

  `
  `  
  Exposed for unit testing only, or for use in SwiftUI previews. Don't instantiate this in your
  app directly.  

  #### Declaration

  Swift  

      init(buttonText: String, https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingActionButton.html#/c:objc(cs)FIRInAppMessagingActionButton(py)buttonTextColor textColor: UIColor, backgroundColor: UIColor)
# Source: https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingAction.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingAction.md.txt

# FirebaseInAppMessagingDisplay Framework Reference

# InAppMessagingAction

    class InAppMessagingAction : NSObject

Defines the metadata for a FIAM action.
- `
  ``
  ``
  `

  ### [actionText](https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingAction#/c:objc(cs)FIRInAppMessagingAction(py)actionText)

  `
  `  
  The text of the action button, if applicable.  

  #### Declaration

  Swift  

      var actionText: String? { get }

- `
  ``
  ``
  `

  ### [actionURL](https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingAction#/c:objc(cs)FIRInAppMessagingAction(py)actionURL)

  `
  `  
  The URL to follow if the action is clicked.  

  #### Declaration

  Swift  

      var actionURL: URL { get }

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingAction#/c:objc(cs)FIRInAppMessagingAction(im)init)

  `
  `  
  Unavailable.
- `
  ``
  ``
  `

  ### [init(actionText:actionURL:)](https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingAction#/c:objc(cs)FIRInAppMessagingAction(im)initWithActionText:actionURL:)

  `
  `  
  This class should only be initialized from a custom in-app message UI component implementation.  

  #### Declaration

  Swift  

      init(actionText: String?, actionURL: URL)
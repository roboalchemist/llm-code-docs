# Source: https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Enums/FIRInAppMessagingDismissType.md.txt

# FirebaseInAppMessagingDisplay Framework Reference

# FIRInAppMessagingDismissType

    enum FIRInAppMessagingDismissType : Int

The way that an in-app message was dismissed.
- `


  ### [typeUserSwipe](https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Enums/FIRInAppMessagingDismissType#/c:@E@FIRInAppMessagingDismissType@FIRInAppMessagingDismissTypeUserSwipe)


  ` Message was swiped away (only valid for banner messages).

  #### Declaration

  Swift

      case typeUserSwipe = 0

- `


  ### [typeUserTapClose](https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Enums/FIRInAppMessagingDismissType#/c:@E@FIRInAppMessagingDismissType@FIRInAppMessagingDismissTypeUserTapClose)


  ` The user tapped a button to close this message.

  #### Declaration

  Swift

      case typeUserTapClose = 1

- `


  ### [typeAuto](https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Enums/FIRInAppMessagingDismissType#/c:@E@FIRInAppMessagingDismissType@FIRInAppMessagingDismissTypeAuto)


  ` The message was automatically dismissed (only valid for banner messages).

  #### Declaration

  Swift

      case typeAuto = 2

- `


  ### [unspecified](https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Enums/FIRInAppMessagingDismissType#/c:@E@FIRInAppMessagingDismissType@FIRInAppMessagingDismissUnspecified)


  ` Dismiss method unknown.

  #### Declaration

  Swift

      case unspecified = 3
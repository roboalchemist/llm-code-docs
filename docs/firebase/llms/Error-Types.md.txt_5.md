# Source: https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Enums/Error-Types.md.txt

# FirebaseInAppMessaging Framework Reference

# _ErrorType

    typealias InAppMessagingDisplayRenderError.Code._ErrorType = InAppMessagingDisplayRenderError

Error code for an in-app message that failed to display.
This enum is unavailable on macOS, macOS Catalyst, and watchOS.
- `


  ### [imageDataInvalid](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Enums/Error-Types#/c:@E@FIAMDisplayRenderErrorType@FIAMDisplayRenderErrorTypeImageDataInvalid)


  ` The image data for this in-app message is invalid.

  #### Declaration

  Swift

      case imageDataInvalid = 0

- `


  ### [unspecifiedError](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Enums/Error-Types#/c:@E@FIAMDisplayRenderErrorType@FIAMDisplayRenderErrorTypeUnspecifiedError)


  ` Unexpected error.

  #### Declaration

  Swift

      case unspecifiedError = 1
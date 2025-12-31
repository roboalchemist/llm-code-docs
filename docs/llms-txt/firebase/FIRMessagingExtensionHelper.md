# Source: https://firebase.google.com/docs/reference/ios/firebasemessaging/api/reference/Classes/FIRMessagingExtensionHelper.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Classes/FIRMessagingExtensionHelper.md.txt

# FirebaseMessaging Framework Reference

# FIRMessagingExtensionHelper

    class FIRMessagingExtensionHelper : NSObject

This class is used to automatically populate a notification with an image if it is
specified in the notification body via the `image` parameter. Images and other
rich content can be populated manually without the use of this class. See the
`UNNotificationServiceExtension` type for more details.
- `
  ``
  ``
  `

  ### [populateNotificationContent(_:withContentHandler:)](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Classes/FIRMessagingExtensionHelper#/c:objc(cs)FIRMessagingExtensionHelper(im)populateNotificationContent:withContentHandler:)

  `
  `  
  Call this API to complete your notification content modification. If you like to
  overwrite some properties of the content instead of using the default payload,
  make sure to make your customized motification to the content before passing it to
  this call.  

  #### Declaration

  Swift  

      func populateNotificationContent(_ content: UNMutableNotificationContent, withContentHandler contentHandler: @escaping (UNNotificationContent) -> Void)

- `
  ``
  ``
  `

  ### [exportDeliveryMetricsToBigQuery(withMessageInfo:)](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Classes/FIRMessagingExtensionHelper#/c:objc(cs)FIRMessagingExtensionHelper(im)exportDeliveryMetricsToBigQueryWithMessageInfo:)

  `
  `  
  Exports delivery metrics to BigQuery. Call this API to enable logging delivery of alert
  notification or background notification and export to BigQuery.
  If you log alert notifications, enable Notification Service Extension and calls this API
  under `UNNotificationServiceExtension didReceiveNotificationRequest: withContentHandler:`.
  If you log background notifications, call the API under `UIApplicationDelegate
  application:didReceiveRemoteNotification:fetchCompletionHandler:`.  

  #### Declaration

  Swift  

      func exportDeliveryMetricsToBigQuery(withMessageInfo info: [AnyHashable : Any])
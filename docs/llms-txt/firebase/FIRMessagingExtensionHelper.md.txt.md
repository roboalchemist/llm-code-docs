# Source: https://firebase.google.com/docs/reference/ios/firebasemessaging/api/reference/Classes/FIRMessagingExtensionHelper.md.txt

# FirebaseMessaging Framework Reference

# FIRMessagingExtensionHelper


    @interface FIRMessagingExtensionHelper : NSObject

This class is used to automatically populate a notification with an image if it is
specified in the notification body via the `image` parameter. Images and other
rich content can be populated manually without the use of this class. See the
`UNNotificationServiceExtension` type for more details.
- `


  ### [-populateNotificationContent:withContentHandler:](https://firebase.google.com/docs/reference/ios/firebasemessaging/api/reference/Classes/FIRMessagingExtensionHelper#/c:objc(cs)FIRMessagingExtensionHelper(im)populateNotificationContent:withContentHandler:)


  ` Call this API to complete your notification content modification. If you like to
  overwrite some properties of the content instead of using the default payload,
  make sure to make your customized motification to the content before passing it to
  this call.

  #### Declaration

  Objective-C

      - (void)populateNotificationContent:
                  (nonnull UNMutableNotificationContent *)content
                       withContentHandler:
                           (nonnull void (^)(UNNotificationContent *_Nonnull))
                               contentHandler;

- `


  ### [-exportDeliveryMetricsToBigQueryWithMessageInfo:](https://firebase.google.com/docs/reference/ios/firebasemessaging/api/reference/Classes/FIRMessagingExtensionHelper#/c:objc(cs)FIRMessagingExtensionHelper(im)exportDeliveryMetricsToBigQueryWithMessageInfo:)


  ` Exports delivery metrics to BigQuery. Call this API to enable logging delivery of alert
  notification or background notification and export to BigQuery.
  If you log alert notifications, enable Notification Service Extension and calls this API
  under `UNNotificationServiceExtension didReceiveNotificationRequest: withContentHandler:`.
  If you log background notifications, call the API under `UIApplicationDelegate
  application:didReceiveRemoteNotification:fetchCompletionHandler:`.

  #### Declaration

  Objective-C

      - (void)exportDeliveryMetricsToBigQueryWithMessageInfo:
          (nonnull NSDictionary *)info;
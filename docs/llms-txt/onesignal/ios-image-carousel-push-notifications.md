# Source: https://documentation.onesignal.com/docs/en/ios-image-carousel-push-notifications.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# iOS: Image Carousel Push Notifications

> How to implement an image carousel in OneSignal iOS push notifications using Swift.

iOS provides a [UNNotificationContentExtension](https://developer.apple.com/documentation/usernotificationsui/unnotificationcontentextension?language=objc) protocol as the entry point for a notification content app extension. This can be used to display a custom interface for your app’s notifications. This example guide explains how to use this for creating a carousel within an iOS notification.

<Frame caption="Image showing a carousel in a push notification">
  <img src="https://mintcdn.com/onesignal/geJ4PYn1YFXgiEih/images/push/carousel.gif?s=79e3d3f900d3154c99b6d959e05f7e33" width="320" height="463" data-path="images/push/carousel.gif" />
</Frame>

## 1. Add a notification content extension

<Card img="https://mintcdn.com/onesignal/ciRrThfP6xMpI7GY/images/docs/00355f9-Screen_Shot_2020-11-30_at_9.32.26_PM.png?fit=max&auto=format&n=ciRrThfP6xMpI7GY&q=85&s=80e43cac5c764bd0538169f9de8b6743" horizontal="true" width="600" height="315" data-path="images/docs/00355f9-Screen_Shot_2020-11-30_at_9.32.26_PM.png">
  In Xcode, select File > New > Target...
</Card>

<Card img="https://mintcdn.com/onesignal/Xl2NHJvxakrK4JbL/images/docs/efd0fde-Screen_Shot_2020-11-30_at_3.10.58_PM.png?fit=max&auto=format&n=Xl2NHJvxakrK4JbL&q=85&s=1050faa9adf15303846a0cdee4cb0bab" horizontal="true" width="600" height="431" data-path="images/docs/efd0fde-Screen_Shot_2020-11-30_at_3.10.58_PM.png">
  Select "Notification Content Extension"
</Card>

<Card img="https://mintcdn.com/onesignal/6v_cVPknFpo5qSVB/images/docs/0a0fa6a-Screen_Shot_2020-11-30_at_6.44.46_PM.png?fit=max&auto=format&n=6v_cVPknFpo5qSVB&q=85&s=9779778bc953998e3e0ec96642d33e50" horizontal="true" width="600" height="429" data-path="images/docs/0a0fa6a-Screen_Shot_2020-11-30_at_6.44.46_PM.png">
  Confirm the selection on the window that pops up
</Card>

<Card img="https://mintcdn.com/onesignal/6tscVAtiSqz353kV/images/docs/ActivateContentExtension.png?fit=max&auto=format&n=6tscVAtiSqz353kV&q=85&s=8e0cf29704f3e01163074be168c3a597" horizontal="true" width="567" height="409" data-path="images/docs/ActivateContentExtension.png">
  Select activate to debug
</Card>

## 2. Add code to your app

[Download the OSNotificationContentExtension](https://github.com/dombartenope/OSNotificationContentExtension) from Github and replace the `OSNotificationContentExtension` in your Xcode Project with the same file from Github.

You should see the following files added:

<Frame caption="Files under Content Extension">
  <img src="https://mintcdn.com/onesignal/6v_cVPknFpo5qSVB/images/docs/0de83b8-Screen_Shot_2020-11-30_at_8.58.01_PM.png?fit=max&auto=format&n=6v_cVPknFpo5qSVB&q=85&s=ab382c7011a4481ab5cc91ce6d1a09cd" width="261" height="125" data-path="images/docs/0de83b8-Screen_Shot_2020-11-30_at_8.58.01_PM.png" />
</Frame>

## 3. Set your notification category

This example [Declares The Actionable Notification Type](https://developer.apple.com/documentation/usernotifications/declaring_your_actionable_notification_types) within the AppDelegate.swift `didFinishLaunchingWithOptions`.

<CodeGroup>
  ```swift Swift theme={null}
  func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {

      //START Authorize OS Notification Carousel Category
      if #available(iOS 10.0, *) {
          let options: UNAuthorizationOptions = [.alert]
          UNUserNotificationCenter.current().requestAuthorization(options: options) { (authorized, error) in
              if authorized {
                  let categoryIdentifier = "OSNotificationCarousel"
                  let carouselNext = UNNotificationAction(identifier: "OSNotificationCarousel.next", title: "👉", options: [])
                  let carouselPrevious = UNNotificationAction(identifier: "OSNotificationCarousel.previous", title: "👈", options: [])
                  let carouselCategory = UNNotificationCategory(identifier: categoryIdentifier, actions: [carouselNext, carouselPrevious], intentIdentifiers: [], options: [])
                  UNUserNotificationCenter.current().setNotificationCategories([carouselCategory])
              }
          }
      }
      //END Authorize OS Notification Carousel Category

      return true
  }

  ```
</CodeGroup>

## 4. Send your push notification

When [Sending Push Messages](./push) you can set the iOS Category and custom Data.

### iOS category

Use `OSNotificationCarousel` as the iOS Category:

<Tabs>
  <Tab title="Dashboard">
    Set under "Platform Settings" > **Send to Apple iOS** > "Category"

    <Frame caption="iOS platform options on OneSignal dashboard">
      <img src="https://mintcdn.com/onesignal/6tscVAtiSqz353kV/images/docs/OSNotificationCarousel.png?fit=max&auto=format&n=6tscVAtiSqz353kV&q=85&s=2e0ff19d9f383aae03d510a34fc2c7fe" width="1101" height="848" data-path="images/docs/OSNotificationCarousel.png" />
    </Frame>
  </Tab>

  <Tab title="API">
    Set with the `ios_category` [API Parameter](/reference/push-notification).
  </Tab>
</Tabs>

### Custom data

OneSignal doesn't have an option to upload multiple images per notification.

Instead you must list the Image URLs separated by a comma `,`

<Tabs>
  <Tab title="Dashboard">
    Set under "Advanced Settings" > "Additional Data"

    For the "Key" set `images` and the "Value" set the list of comma separated URLs without quotes.

    <Frame>
      <img src="https://mintcdn.com/onesignal/4HyuQPBpu-4xjmQC/images/docs/d07200a-Screen_Shot_2020-11-30_at_9.19.59_PM.png?fit=max&auto=format&n=4HyuQPBpu-4xjmQC&q=85&s=1f4911116d4c3a944d1aa282d6566359" width="635" height="307" data-path="images/docs/d07200a-Screen_Shot_2020-11-30_at_9.19.59_PM.png" />
    </Frame>

    Example, copy paste:

    <CodeGroup>
      ```text text theme={null}
      https://cdn.pixabay.com/photo/2015/12/01/20/28/road-1072823_960_720.jpg,https://cdn.pixabay.com/photo/2013/11/28/10/36/road-220058_960_720.jpg,https://cdn.pixabay.com/photo/2012/08/27/14/19/mountains-55067_960_720.png,https://cdn.pixabay.com/photo/2015/01/28/23/35/landscape-615429_960_720.jpg,https://cdn.pixabay.com/photo/2016/05/05/02/37/sunset-1373171_960_720.jpg
      ```
    </CodeGroup>
  </Tab>

  <Tab title="API">
    Use the `data` [API Parameter](/reference/push-notification) like this:

    <CodeGroup>
      ```json json theme={null}
      data: {
        "images" : "https://cdn.pixabay.com/photo/2015/12/01/20/28/road-1072823_960_720.jpg,https://cdn.pixabay.com/photo/2013/11/28/10/36/road-220058_960_720.jpg,https://cdn.pixabay.com/photo/2012/08/27/14/19/mountains-55067_960_720.png,https://cdn.pixabay.com/photo/2015/01/28/23/35/landscape-615429_960_720.jpg,https://cdn.pixabay.com/photo/2016/05/05/02/37/sunset-1373171_960_720.jpg"
      }
      ```
    </CodeGroup>
  </Tab>
</Tabs>

### Send the push

Once you receive the push, you will need to long press or swipe left and click "View" to expand the notification depending on the iOS version.

### Troubleshooting

The code sample on the Github page has lines that are commented out which show debug positions and print statements to help identify any issues. Uncomment those lines and you should be able to see if the Notification Content Extension is being instantiated. If not, please check that you have not missed any steps in the setup process. If you continue to have issues, please reach out to [support@onesignal.com](mailto:support@onesignal.com)

### Further reading

* [Apple's Docs to Declare Your Actionable Notification Types](https://developer.apple.com/documentation/usernotifications/declaring_your_actionable_notification_types)
* [Helpful Medium Post by Ahmet Keskin](https://medium.com/nsistanbul/carousel-notification-in-ios-5a1e8239d786)

***


Built with [Mintlify](https://mintlify.com).

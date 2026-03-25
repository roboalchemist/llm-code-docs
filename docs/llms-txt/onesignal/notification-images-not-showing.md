# Source: https://documentation.onesignal.com/docs/en/notification-images-not-showing.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Notification Images Not Showing

> Notifications images not appearing.

When sending push notifications that include images, the OneSignal SDK tries to get the external image URLs from the [OSNotification Payload](./osnotification-payload) and display it within the notification. It doesn't matter if the app is closed during this process. The SDK waits for the image to be downloaded, but if it takes longer than \~25 seconds (enforced by Apple), the notification is displayed without the image. OneSignal's SDK does not retry to get the image again if it fails to download.

This guide will cover the most common reasons for images not showing and how to fix them. For details on image specs, see [Images & Rich Media](./rich-media).

## Image configuration

Check these items first to make sure the image is properly configured.

### Image size

The image must be less than 5MB in size. The smaller the image, the faster it will download. More details found in [Images & Rich Media](./rich-media).

### Image URL

* Image URLs need a direct link to the image resource. No redirects and no links to pages that show the image but not the actual image resource.
  * Usually this means the image URL starts with `https://` and ends with a file extension like `.png` or `.jpg`.

Example:

* This will not work: `https://pixabay.com/en/architecture-travel-sky-building-3095716/`
* But if you right click the image and open in a new tab, this will work: `https://cdn.pixabay.com/photo/2018/01/21/01/46/architecture-3095716_960_720.jpg`

### Image host

If you uploaded the image to OneSignal, it will be hosted on our servers for \~33 days. If you need the image for longer, you can use templates or store the image on your own servers and reference the resource URL directly in the template.

If you are self-hosting the image, you need to make sure the server is able to handle the amount of downloads. Each device that receives the notification will need to download the image. Around 30 seconds is how long the device has to download all notification resources, including images. If it takes longer, it will not show on that device.

***

## Device configuration

Check the internet connection on the device. Unstable network connections may cause the image to not show.

* Test on different WiFi networks.
* Test on different cellular networks.
* Test on different devices.

***

## Platform configuration

Check the sections below based on the platform not receiving the image.

### Web push images

* **Only Chrome supports large images in push notifications on Windows and Android**.
  * Chrome for macOS does not support large images.
* Firefox, Safari and Edge do not support big images.
* On Android, when you get the notification, you will need to tap on the notification to expand it and see the image.

<Warning>
  If your mobile browser app has many unread push notifications and/or many tabs open, this can cause notifications to not show.
</Warning>

### Android push images

When you get the notification in the Android notification center, you will need to expand the notification to see the image.

Android does not require any additional configuration to receive images in push notifications.

### iOS push images

iOS notifications require the Notification Service Extension to be setup correctly. The Notification Service Extension setup is covered in our [Mobile SDK setup](./mobile-sdk-setup) guides for the version of our SDK you are using.

If your image URLs are HTTP and you insist on hosting them yourself using an HTTP URL, you will need to set `NSAppTransportSecurity` to `NSAllowsArbitraryLoads` in your Xcode .plist.

<Warning>
  Apple may reject your app if `NSAllowsArbitraryLoads` is enabled when releasing your app to the App Store, as this can create a security vulnerability. For more information, please read Apple's [Security Overview](https://www.apple.com/business/resources/docs/iOS_Security_Overview.pdf).
</Warning>

***

## Technical troubleshooting

If you checked the above items and the image still fails to be shown, use our SDK's [`setLogLevel` method](./mobile-sdk-reference#setloglevel) with `VERBOSE` logging to check for specific errors related to image downloading.

For a detailed guide on generating logs, see our [Capturing a Debug Log](./capturing-a-debug-log) guide.

Common errors include:

* `Could not download image!`
* `Encountered an error while attempting to download file with URL:`
* `OneSignal encountered an exception while downloading file`

### iOS Notification Service Extension Troubleshooting

If images are not showing on iOS, please follow our [Troubleshooting the iOS Notification Service Extension](./service-extensions#troubleshooting-the-ios-notification-service-extension) guide.

This guide will help review your Notification Service Extension setup and identify any issues.

***

Built with [Mintlify](https://mintlify.com).

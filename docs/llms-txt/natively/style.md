# Source: https://docs.buildnatively.com/natively-platform/appearance/style.md

# Style

Some bellows parameters can be updated with SDK later (check [Control Style & Colors](https://docs.buildnatively.com/guides/integration/control-style-and-colors) section)

[#app-background-color](#app-background-color "mention")

[#loader-color](#loader-color "mention")

[#swipe-navigation](#swipe-navigation "mention")

[#pull-to-refresh](#pull-to-refresh "mention")

[#status-bar-style](#status-bar-style "mention")

[#safe-area](#safe-area "mention")

##

## Colors

### App Background Color

The top background (It displays only on iOS devices with notch)

If your page background is transparent, it will be the page's background.

![Top bar background (If iPhone with notch)](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-77879adb6b297e51001cf02cae5f55b3be761a8b%2Ftop.PNG?alt=media)

### Loader Color

The color of a loader on the top (This loader will be displayed only while the page is loading)

![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-e5a3712dbce0a7f6af514b656174539cf3fd96ac%2Floader.PNG?alt=media)

## Device

### Swipe Navigation

Users can navigate between pages with a swipe gesture

![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-d915e854b965ef46b3fbaacd3ae5fd351d92695f%2FRPReplay_Final1653655055.gif?alt=media)

### Pull To Refresh

Drag to the bottom to refresh the page

![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-15b4b60d9df76f7289bf6aeb9314a538f5189776%2FRPReplay_Final1653655071.gif?alt=media)

### Status Bar Style

In iOS: Status bar color, can be "Dark", "Light", or None(Hidden)

![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-68df18790bde9df24fa1838e720cc8f976ba6395%2FIMG_2013.jpg?alt=media)

In Android: "Dark" or "Light"

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FKJSJjCawh4KOIrL4xAG2%2Fdark.png?alt=media&#x26;token=6ad6c3ee-82fd-40bb-830c-a1ccbf0d0756" alt=""><figcaption><p>DARK</p></figcaption></figure>

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2F48HBVd8MyXG72RnqJxD1%2Flight.png?alt=media&#x26;token=1de7c121-c9b4-4249-80b9-d0b8fbec5a63" alt=""><figcaption><p>LIGHT</p></figcaption></figure>

### Safe Area <a href="#safe-area" id="safe-area"></a>

Safe Area - it's a space on the top of the app, that can be Enabled/Disabled.

{% hint style="info" %}
If it's Enabled, the background can be controlled by [App Background Color](#app-background-color)
{% endhint %}

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FsL3sijGMtE92Gjb2kCaE%2FSimulator%20Screen%20Shot%20-%20iPhone%2014%20Pro%20-%202022-10-10%20at%2016.56.14.png?alt=media&#x26;token=9290832b-cadf-426b-a486-a7dbdaf237e8" alt=""><figcaption><p>Disabled</p></figcaption></figure>

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FxfZWJBGOU9HwcmXtIOiB%2FSimulator%20Screen%20Shot%20-%20iPhone%2014%20Pro%20-%202022-10-10%20at%2016.55.45.png?alt=media&#x26;token=2a8aeb36-36ca-47a0-b360-b866949d4062" alt=""><figcaption><p>Enabled</p></figcaption></figure>

### Resize Viewport

Enabling this option adjusts the viewport, allowing users to scroll and access focused input fields that are obscured by the keyboard.

### Bottom Overlay

Enables Android navigation bar.

### Background Audio

Enable this feature if your app requires background audio playback.

{% hint style="warning" %}
If you enable this feature but your app doesn't require it for any functionality, your app may be rejected by Apple for: "The app declares support for audio in the UIBackgroundModes key in your Info.plist but we are unable to locate any features that require persistent audio". In such a case, you should disable the feature, save your changes, rebuild your app, and resubmit it for review.
{% endhint %}

### Wake Lock

Prevent your app from automatically locking the screen.&#x20;

{% hint style="info" %}
If it's Enabled, the feature can be controlled by [Wake Lock](https://docs.buildnatively.com/guides/integration/control-style-and-colors)
{% endhint %}

# Browser Support

The CreativeEditor SDK requires specific APIs to fully function. For video-related features, the required APIs are only supported in certain browsers. As a result, the list of supported browsers is currently limited to the following:

| Supported Browser | Graphics Editing | Video Editing |
| --- | --- | --- |
| Chrome | **114** or newer | **114** or newer |
| Chrome Android | **114** or newer | not supported |
| Chrome iOS | **114** or newer (on iOS/iPadOS 15 or newer) | not supported |
| Edge | **114** or newer | **114** or newer |
| Firefox | **115** or newer | not supported |
| Safari | **15.6** or newer | **26.0** or newer |
| Safari iOS | **15.6** or newer (on iOS/iPadOS 15 or newer) | not supported |

For our video features, unsupported browsers will display a warning dialog informing about them not supported when they are being used to access CE.SDK video functionality.

While other browsers based on the Chromium project might work fine (Arc, Brave, Opera, Vivaldi etc.) they are not officially supported.

## Host Platform Restrictions[#](#host-platform-restrictions)

All supported browsers rely on the host’s platform APIs for different kind of functionality (e.g. video support). Check our [known editor limitations](vue/compatibility-139ef9/) for more details on these.

---



[Source](https:/img.ly/docs/cesdk/vue/automation-715209)
# Source: https://docs.logrocket.com/docs/performance-impact-of-the-mobile-sdk.md

# Performance Impact of the Mobile SDK

The LogRocket Mobile SDK is designed to avoid a negative performance impact to your app. We're committed to keeping it that way and to being transparent about what our SDK does on your app.

## Will this slow down my app?

LogRocket’s Mobile SDK is built to work smoothly within your app without slowing it down. We achieve this by focusing on several key areas:

1. We keep the time our SDK spends on your app's main thread as short as possible.
2. We minimize bandwidth usage to provide a smooth and responsive experience while conserving data and battery life.
3. Our SDK uses minimal storage on your users' devices by limiting disk usage
4. We pause recording when large images could impact your app's performance

### Main Thread Usage

There’s only one part of the SDK that has to work on the main thread — the process which captures what's currently on the screen. We've optimized this process to minimize any impact and to keep the app running smoothly. This screen capture process also happens on average just once per second, which means it uses less than one frame per second and leaves plenty of resources for your app to run seamlessly.

To prevent LogRocket view capture from causing screen hitching while processing complex views, we've put in place a hard time limit on view captures. This can be adjusted at your own risk by setting init config option `viewCaptureTimeoutThreshold` to another value greater or less than the default of 100.

If LogRocket view capture is unable to capture all views in high fidelity within the `viewCaptureTimeoutThreshold`, the remaining views are captured as wireframes. Wireframe capture can be disabled by setting `viewCaptureAdditionalWireframeDuration` to 0.

### Bandwidth Usage

When your device is on a fast internet connection, LogRocket sends recording data directly to our servers. We use a highly optimized wire format to minimize total upload volume. - this means our system keeps data usage low, typically around 15KB a second.

Apps with lots of images might use a bit more data initially, although LogRocket won’t capture large images to support optimal performance.

If your device goes offline, the data is temporarily stored until the connection is restored, then it’s sent once you're back online.

### Disk Usage

We store event data on your device temporarily to make sure it's safe and doesn't get lost. We've fine-tuned how we save and send this data to reduce the amount of work your device has to do.

Event data is streamed to cache storage for on-device persistence. We have optimized our disk access to minimize IO (Input/Output) cycles while writing and uploading the data to LogRocket servers. The more I/O cycles an app performs, the more it engages the device’s storage and processing resources. This can impact performance and battery life, which is why optimizing I/O cycles—making sure they happen efficiently and only when necessary—is important.

The data is saved in a way that allows the device to free up space if it’s needed for more important tasks. To do this, we write to temporary storage that can be reclaimed by the operating system if application critical storage space is required.

### Capturing Images

Image processing and capture can be expensive, both in compute time and bandwidth usage. Because of this, we skip capturing images that are large enough that capturing them might slow down your app. This way, your app stays fast and responsive without any interruptions. We recommend ensuring your image sources are appropriately sized and compressed in order to improve replay completeness.

In the event the SDK skips capture of an image due to size, a grey placeholder matching the uncaptured image's dimensions and position will be rendered in session replay.
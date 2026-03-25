# Source: https://www.mux.com/docs/guides/monitor-avplayer.md

# Monitor AVPlayer
This guide walks through integration with iOS and TVOS AVPlayer player to collect video performance metrics with Mux data.
Mux Data integration for AVPlayer supports applications running on iOS 12.0 or newer, tvOS 12.0 or newer, and Mac Catalyst that use `AVPlayerViewController`, `AVPlayerLayer`, or a standalone `AVPlayer` playing audio or if presented with a fixed size. Applications running on visionOS 1.0 and higher are also supported if they use `AVPlayerViewController` or a standalone `AVPlayer` playing audio or if presented with a fixed size.

This integration uses Mux's core Objective-C SDK and the full source can be seen here: [muxinc/mux-stats-sdk-avplayer](https://github.com/muxinc/mux-stats-sdk-avplayer). This SDK is packaged as an xcframework.

## Features

The following data can be collected by the Mux Data SDK when you use the \{featureDef.name} SDK, as described
&#x20;       below.

```md
- Engagement metrics
- Quality of Experience Metrics
- Available for deployment from a package manager
- Custom Dimensions
- Average Bitrate metrics and `renditionchange` events
- Request metrics
- Ads metrics
- Customizable Error Tracking
- Custom Beacon Domain
- Extraction of HLS Session Data
- Live Stream Latency metric

```

Notes:

```md
Packaged with: cocoapods, SPM and carthage. Request Latency is not available.
```

## 1. Install the Mux Data SDK

## Installation

### Installing in Xcode with Swift Package Manager

1. In Xcode click "File" > "Swift Packages" > "Add Package Dependency..."
2. The package repository URL is `https://github.com/muxinc/mux-stats-sdk-avplayer.git`

```
https://github.com/muxinc/mux-stats-sdk-avplayer.git
```

3. Click `Next`.
4. Since the `MUXSDKStats` follows SemVer, we recommend setting the "Rules" to install the latest version and choosing the option "Up to Next Major". [Here's an overview of the different SPM Dependency Rules and their semantics](https://developer.apple.com/documentation/xcode/adding-package-dependencies-to-your-app#Decide-on-package-requirements).

### Installing in Package.swift

Open your Package.swift file, add the following to `dependencies`:

```swift
    .package(
      url: "https://github.com/muxinc/mux-stats-sdk-avplayer",
      .upToNextMajor(from: "4.0.0")
    ),
```

Note that `MUXSDKStats` has a dependency on `MuxCore`, so you will see that `MuxCore` gets installed as well.

> As of Xcode 14.3.1 integrating the Mux SDKs as part of a shared framework using Swift Package Manager library targets is now supported. [An example for setting this up is available here](https://github.com/muxinc/examples/tree/main/swift-data-library-installation).

### Installing with CocoaPods

To install with CocoaPods, modify your Podfile to use frameworks by including `use_frameworks!` and then add the following pods to your Podfile:

```
pod 'Mux-Stats-AVPlayer', '~>4.0'
```

This will install `Mux-Stats-AVPlayer` and the latest current release of our [core Objective-C Library](https://github.com/muxinc/stats-sdk-objc).

Next, add correct import statement into your application.

```objc

@import MUXSDKStats;

```

```swift

import MUXSDKStats

```



## 2. Initialize the monitor for your AVPlayer instance

Get your `ENV_KEY` from the [Mux environments dashboard](https://dashboard.mux.com/environments).

<Callout type="info" title="Env Key is different than your API token">
  `ENV_KEY` is a client-side key used for Mux Data monitoring. These are not to be confused with API tokens which are created in the admin settings dashboard and meant to access the Mux API from a trusted server.
</Callout>

<Image src="/docs/images/env-key.png" width={2004} height={250} />

The example below uses `monitorAVPlayerViewController(_:withPlayerName:customerData:)`. If you are using `AVPlayerLayer`, use `monitorAVPlayerLayer(_:withPlayerName:customerData:)` instead.

The `playerName` parameter is a string that identifies this instance of your player. When calling `destroyPlayer(_:)` or `videoChange(forPlayer:with:)` later on, you will need this string. Each instance of a player that runs simultaneously in your application should have a different `playerName`.

<Callout type="warning">
  **If you are using SwiftUI**, attach the monitor in the `onAppear` action for your view. This ensures that the Mux Data SDK is able to get the dimensions of the view which is used to calculate video quality metrics.
</Callout>

```objc

MUXSDKCustomerPlayerData *playerData = [[MUXSDKCustomerPlayerData alloc] initWithPropertyKey:@"ENV_KEY"];

MUXSDKCustomerVideoData *videoData = [MUXSDKCustomerVideoData new];
// insert videoData metadata
videoData.videoTitle = @"Title1";
videoData.videoSeries = @"animation";

MUXSDKCustomerData *customerData = [[MUXSDKCustomerData alloc] initWithCustomerPlayerData:playerData
                                                                                videoData:videoData
                                                                                 viewData:nil
                                                                               customData:nil
                                                                               viewerData:nil];

_playerBinding = [MUXSDKStats monitorAVPlayerViewController:_avplayerController 
                                             withPlayerName:@"mainPlayer" 
                                               customerData:customerData];


```

```swift

let playerData = MUXSDKCustomerPlayerData(environmentKey: "ENV_KEY")
playerData?.playerName = "playerName"

let videoData = MUXSDKCustomerVideoData()
videoData.videoTitle = "Title1"
videoData.videoSeries = "animation"

guard let customerData = MUXSDKCustomerData(
    customerPlayerData: playerData,
    videoData: videoData,
    viewData: nil,
    customData: nil,
    viewerData: nil
) else {
    return
}

let playerBinding = MUXSDKStats.monitorAVPlayerViewController(
    playerViewController,
    withPlayerName: "playerName",
    customerData: customerData
)
// if you're using AVPlayerLayer instead of AVPlayerViewController use this instead:
// MUXSDKStats.monitorAVPlayerLayer(playerLayer, withPlayerName: "playerName", customerData: customerData)

```



For more complete examples check the [demo app in the repo](https://github.com/muxinc/mux-stats-sdk-avplayer/tree/master/Examples).

After you've integrated, start playing a video in your player. A few minutes after you stop watching, you'll see the results in your Mux data dashboard. Login to the dashboard and find the environment that corresponds to your `env_key` and look for video views.

## 3. Make your data actionable

The only required field is `env_key`. But without some more metadata the metrics in your dashboard will lack the necessary information to take meaningful actions. Metadata allows you to search and filter on important fields in order to diagnose issues and optimize the playback experience for your end users.

Metadata fields are provided via the `MUXSDKCustomerPlayerData` and `MUXSDKCustomerVideoData` objects.

For the full list of properties, see the MuxCore headers in the [latest stats-sdk-objc release](https://github.com/muxinc/stats-sdk-objc/releases/latest).

For more details about each property, view the [Make your data actionable](/docs/guides/make-your-data-actionable-with-metadata) guide.

```objc

MUXSDKCustomerPlayerData *playerData = [[MUXSDKCustomerPlayerData alloc] initWithPropertyKey:@"ENV_KEY"];
playerData.viewerUserId = @"1234";
playerData.experimentName = @"player_test_A";
playerData.playerName = @"iOS AVPlayer";
playerData.playerVersion = @"1.0.0";

MUXSDKCustomerVideoData *videoData = [MUXSDKCustomerVideoData new];
videoData.videoTitle = @"Big Buck Bunny";
videoData.videoId = @"bigbuckbunny";
videoData.videoSeries = @"animation";
videoData.videoDuration = @(120000); // in milliseconds
videoData.videoIsLive = @NO;
videoData.videoCdn = @"cdn";

MUXSDKCustomerViewData *viewData= [[MUXSDKCustomerViewData alloc] init];
viewData.viewSessionId = @"some session id";

MUXSDKCustomData *customData = [[MUXSDKCustomData alloc] init];
[customData setCustomData1:@"my-data-string"];
[customData setCustomData2:@"my-custom-dimension-2"];

MUXSDKCustomerViewerData *viewerData = [[MUXSDKCustomerViewerData alloc] init];
viewerData.viewerApplicationName = @"MUX DemoApp";

MUXSDKCustomerData *customerData = [[MUXSDKCustomerData alloc] initWithCustomerPlayerData:playerData
                                                                                videoData:videoData
                                                                                 viewData:viewData
                                                                               customData:customData
                                                                               viewerData:viewerData];


_playerBinding = [MUXSDKStats monitorAVPlayerViewController:_avplayerController 
                                             withPlayerName:@"mainPlayer"
                                               customerData:customerData];

```

```swift

guard let playerData = MUXSDKCustomerPlayerData(environmentKey: "ENV_KEY") else {
    return
}
playerData.playerName = "playerName"
playerData.viewerUserId = "1234"
playerData.experimentName = "player_test_A"
playerData.playerVersion = "1.0.0"

let videoData = MUXSDKCustomerVideoData()
videoData.videoId = "abcd123"
videoData.videoTitle = "My Great Video"
videoData.videoSeries = "Weekly Great Videos"
videoData.videoDuration = 120000 // in milliseconds
videoData.videoIsLive = false
videoData.videoCdn = "cdn"

let viewerData = MUXSDKCustomerViewerData()
viewerData.viewerApplicationName = "MUX video-demo"

guard let customerData = MUXSDKCustomerData(
    customerPlayerData: playerData,
    videoData: videoData,
    viewData: nil,
    customData: nil,
    viewerData: viewerData
) else {
    return
}
let playerBinding = MUXSDKStats.monitorAVPlayerViewController(
    playerViewController,
    withPlayerName: "playerName",
    customerData: customerData
)

// if you're using AVPlayerLayer instead of AVPlayerViewController use this instead:
// MUXSDKStats.monitorAVPlayerLayer(playerLayer, withPlayerName: "playerName", customerData: customerData)

```



## 4. Set or update metadata after monitor

There are some cases where you may not have the full set of metadata until after the video playback has started. In this case, you should omit the values when you first call `monitorAVPlayerLayer`, `monitorAVPlayerViewController`, or `monitorAVPlayer`. Then, once you have the metadata, update it by calling `setCustomerData(_:forPlayer:)`.

```objc

// Sometime later before the player is destroyed you can do this:
// The player name ("mainPlayer" in this example) should be a player that
// you have already called one of the `monitorAVPlayer` methods with
// In this example we are updating videoData, but the same can be done
// for updating playerData, customData or viewData
// Note that the values in customerData passed as nil will keep previously set data
// Note that viewerData can't be updated

MUXSDKCustomerVideoData *videoData = [MUXSDKCustomerVideoData new];
videoData.videoTitle = @"Big Buck Bunny";
videoData.videoId = @"bigbuckbunny";

MUXSDKCustomerData *customerData = [[MUXSDKCustomerData alloc] init];
customerData.customerVideoData = videoData;

[MUXSDKStats setCustomerData:customerData
                   forPlayer:@"mainPlayer"];

```

```swift

// Example: after monitoring, you need to update `customerData` with new metadata.
// In this example we are updating `videoData`, but the same process can be 
// used for updating `playerData`, `customData` or `viewData`.

// Note: The player name ("mainPlayer" in this example) should be a player that
// has been defined in steps 1-3.
// Note: All values in customerData passed as nil will keep previously set data.
// Note: `viewerData` object cannot be updated.

let videoData = MUXSDKCustomerVideoData()
videoData.videoTitle = "Big Buck Bunny"
videoData.videoId = "bigbuckbunny"

guard let customerData = MUXSDKCustomerData(
    customerPlayerData: nil,
    videoData: videoData,
    viewData: nil,
    customData: nil,
    viewerData: nil
) else {
    return
}

MUXSDKStats.setCustomerData(customerData, forPlayer: "mainPlayer")

```



## 5. Advanced

## Changing the Video

There are two cases where the underlying tracking of the video view need to be reset. First, when you load a new source URL into an existing player, and second when the program within a singular stream changes (such as a program within a live stream).

Note: You do not need to change the video info when changing to a different source of the same video content (e.g. different resolution or video format).

### New source

When you change to a new video (in the same player) you need to update the information that Mux knows about the current video. Examples of when this is needed are:

* The player advances to the next video in a playlist
* The user selects a different video to play

This is done by calling `videoChange(forPlayer:with:)` which will remove all previous video data and reset all metrics for the video view. You can include any metadata when changing the video but you should only need to update the values that start with `video_`.

It is required to call `videoChange(forPlayer:with:)` immediately before telling the player which new source to play. This recommendation changed in `v1.2.0`.

It is also required to call `play()` for player after replacing the current item.

If you have new player data you can include it in the `customerData` you pass to `videoChange(forPlayer:with:)`.

```swift

let videoData = MUXSDKCustomerVideoData()
videoData.videoId = "abcd123"
videoData.videoTitle = "My Great Video"
videoData.videoSeries = "Weekly Great Videos"
videoData.videoDuration = 120000 // in milliseconds
videoData.videoIsLive = false
videoData.videoCdn = "cdn"

let customerData = MUXSDKCustomerData(
    customerPlayerData: nil,
    videoData: videoData,
    viewData: nil
)

MUXSDKStats.videoChange(forPlayer: "AVPlayer", with: customerData)

// you should have AVPlayer and AVPlayerItem at this point
player.replaceCurrentItem(with: playerItem)

// call play() on the player here to start playback
player.play()

```



### New program (in single stream)

In some cases, you may have the program change within a stream, and you may want to track each program as a view on its own. An example of this is a live stream that streams multiple programs back to back, with no interruptions.

In this case, call `programChange(forPlayer:with:)`. This will remove all previous video data and reset all metrics for the video view, creating a new video view. You can include any metadata when changing the video but you should only need to update the values that start with `video_`.

```swift

let videoData = MUXSDKCustomerVideoData()
videoData.videoId = "abcd123"
videoData.videoTitle = "My Great Video"
videoData.videoSeries = "Weekly Great Videos"
videoData.videoDuration = 120000 // in milliseconds
videoData.videoIsLive = false
videoData.videoCdn = "cdn"

let customerData = MUXSDKCustomerData(
    customerPlayerData: nil,
    videoData: videoData,
    viewData: nil
)

MUXSDKStats.programChange(forPlayer: "AVPlayer", with: customerData)

```



## Usage with Google Interactive Media Ads (IMA)

If you are using Google Interactive Media Ads, and specifically either the iOS SDK `GoogleAds-IMA-iOS-SDK` or the tvOS SDK `GoogleAds-IMA-tvOS-SDK` then we have another
plugin library that integrates tracking of ad playback events. You should have a fully functioning Google Ads IMA integration working in your iOS or tvOS application first.

<Callout type="info">
  The `v0.14.0` and higher releases of the Mux Google Ads IMA plugin expose a new API. If you've already integrated an earlier version [documentation is available to migrate to the new API](/docs/guides/monitor-avplayer#steps-to-migrate-existing-ima-integration-to-new-api).
</Callout>

### Installation

### Swift Package Manager

#### Installing in Xcode with Swift Package Manager

1. In Xcode click "File" > "Swift Packages" > "Add Package Dependency..."
2. The package repository URL is `https://github.com/muxinc/mux-stats-google-ima.git`

#### Installing as a dependency in Package.swift manifest

In order to install in your iOS application open your `Package.swift` file, add the following to dependencies:

```swift
.package(
  url: "https://github.com/muxinc/mux-stats-google-ima",
  .upToNextMajor(from: "0.14.0")
)
```

### Cocoapods

The Mux Google IMA plugin is available through CocoaPods. To install it, add the following line to your Podfile:

```ruby
pod 'Mux-Stats-Google-IMA'
```

### Steps for new IMA integrations

1. Import the SDK: `import MuxStatsGoogleIMAPlugin` in Swift  `#import <MuxStatsGoogleIMAPlugin/MuxStatsGoogleIMAPlugin.h>` in Objective-C
2. After initializing the Mux monitor with `monitorAVPlayerViewController` or `monitorAVPlayerLayer`, save this value to a variable (below it's called `playerBinding`)
3. Create an `adListener` instance using the `playerBinding` you created above and your applications IMA ads loader by calling `MUXSDKIMAAdListener(playerBinding: playerBinding!, monitoringAdsLoader: yourAdsLoader)`.
4. Add `IMAAdsManager` monitoring by calling `adListener.monitorAdsManager(yourIMAAdsManager)`
5. Notify `adListener` when you send your ad request

* For client-side ads, the most common case, use `imaListener.clientAdRequest(yourIMAAdsRequest)` to forward each `IMAAdsRequest` you initiate
* For server-side ads using [Dynamic Ad Insertion](https://developers.google.com/interactive-media-ads/docs/sdks/ios/dai), use `imaListener.daiAdRequest(yourIMAStreamRequest)` to forward each `IMAAdsRequest` you initiate

6. `MUXSDKIMAAdListener` will automatically intercept `IMAAdsLoader` and `IMAAdsManager` delegate calls

### Steps to migrate existing IMA integration to new API

1. Replace calls to `MuxImaLister` with `MUXSDKIMAAdListener`. `MuxImaListener` supports the same new API so this step is optional, the remaining steps are applicable to `MuxImaListener`. As of `v0.14.0``MuxImaLister` is deprecated and will be removed in a future release.
2. Supply an `IMAAdsLoader` when calling the `MUXSDKIMAAdListener` initializer. Make sure your IMAAdsLoader delegate **is configured before this step**.
3. MUXSDKIMAAdListener will forward `IMAAdsLoaderDelegate` calls to your delegate.
4. When you've created a new `IMAAdsManager`, like you've done with `IMAAdsLoader`, configure your own  `IMAAdsManagerDelegate` first and then call `monitorAdsManager`.
5. MUXSDKIMAAdListener will forward `IMAAdsManagerDelegate` calls to your delegate.
6. Remove calls to `dispatchEvent`, `dispatchError`, and `onContentPauseOrResume` from your integration.

```objc

#import<MuxStatsGoogleIMAPlugin/MuxStatsGoogleIMAPlugin.h>

- (void)viewDidLoad {
  // Follow the instructions from pod 'GoogleAds-IMA-iOS-SDK' to set up
  // your adsLoader and set your ViewController as the delegate
  //
  // From your ViewController, when you call either
  //    monitorAVPlayerViewController:withPlayerName:playerData:videoData:
  //    monitorAVPlayerLayer:withPlayerName:playerData:videoData:
  //
  // You will get back a MUXSDKPlayerBinding object
  [MUXSDKPlayerBinding *playerBinding] = [MUXSDKStats monitorAVPlayerViewController:_avplayerController
                                                                     withPlayerName:DEMO_PLAYER_NAME
                                                                       customerData:customerData];
  //
  // Use the MUXSDKPlayerBinding object to initialize the MuxImaListener class
  //
  _adsListener = [[MUXSDKIMAAdListener alloc] initWithPlayerBinding:playerBinding 
                                                   monitorAdsLoader:adsLoader];

  //...

  // When you send your ad request, you must report it to the IMA listener so it can properly track state
  [_adsListener clientAdRequest:request]; // for Client-Side Ads (the usual case)
  // OR
  [_adsListener daiAdRequest:daiRequest]; // for Dynamic Server-Side Ads (DAI/SSAI)
}
// when the adsLoader fires adsLoadedWithData you get a
// reference to the adsManager. Set your ViewController as the delegate
// for the adsManager
- (void)adsLoader:(IMAAdsLoader *)loader adsLoadedWithData:(IMAAdsLoadedData *)adsLoadedData {
    _adsManager = adsLoadedData.adsManager;
    // Set your adsManager delegate before passing it to adsListener for monitoring
    _adsManager.delegate = self;
    IMAAdsRenderingSettings *adsRenderingSettings = [[IMAAdsRenderingSettings alloc] init];
    adsRenderingSettings.webOpenerPresentingController = self;
    [_adsManager initializeWithAdsRenderingSettings:adsRenderingSettings];
    [_adsListener monitorAdsManager: _adsManager];
}

//
- (void)adsManager:(IMAAdsManager *)adsManager didReceiveAdEvent:(IMAAdEvent *)event {
    // When the SDK notified us that ads have been loaded, play them.
    if (event.type == kIMAAdEvent_LOADED) {
        [_adsManager start];
    }
}

- (void)adsManager:(IMAAdsManager *)adsManager didReceiveAdError:(IMAAdError *)error {
    [_avplayer play];
}

- (void)adsManagerDidRequestContentPause:(IMAAdsManager *)adsManager {
    [_avplayer pause];
}

- (void)adsManagerDidRequestContentResume:(IMAAdsManager *)adsManager {
    [_avplayer play];
}

```

```swift

import MuxCore
import MUXSDKStats
import GoogleInteractiveMediaAds
import MuxStatsGoogleIMAPlugin

var adsListener: MUXSDKIMAAdListener?

override func viewDidLoad() {
  super.viewDidLoad()
  // Follow the instructions from pod 'GoogleAds-IMA-iOS-SDK' to set up
  // your adsLoader and set your ViewController as the delegate
  //
  // From your ViewController, when you call either
  //    monitorAVPlayerViewController
  //    monitorAVPlayerLayer
  //
  // You will get back a MUXSDKPlayerBinding object

  // Configure your ads loader delegate before initializing MUXSDKIMAAdListener
  adsLoader.delegate = self

  // Setup your content players AVPlayerViewController or AVPlayerLayer
  let playerViewController = AVPlayerViewController()

  let playerBinding = MUXSDKStats.monitorAVPlayerViewController(
    self, 
    withPlayerName: playName, 
    customerData: customerData
  )

  // Use the MUXSDKPlayerBinding object to initialize the MuxImaListener class
  // Save a reference to adsListener, we'll use a property
  let adsListener = MUXSDKIMAAdListener(
    playerBinding: playerBinding!,
    monitorAdsLoader: adsLoader
  )
  self.adsListener = adsListener
  // ... 

  // When you send your ad request, you must report it to the IMA listener so it can properly track state
  adsListener.clientAdRequest(request) // for Client-Side Ads (the usual case)
  // OR
  adsListener.daiAdRequest(daiAdRequest) // for Dynamic Server-Side Ads (SSAI)
}

// the adsLoader delegate will fire this and give access to the adsManager
// the application needs to register as a delegate for the adsManager too
func adsLoader(_ loader: IMAAdsLoader!, adsLoadedWith adsLoadedData: IMAAdsLoadedData!) {
    adsManager = adsLoadedData.adsManager;
    adsManager.delegate = self;
    adsListener?.monitorAdsManager(adsManager)
}

// all of these events get fired by the adsManager delegate
// when this happens, the application needs to do some stuff and send the events
// to our sdk
func adsManager(_ adsManager: IMAAdsManager!, didReceive event: IMAAdEvent!) {
    if (event.type == kIMAAdEvent_LOADED) {
      adsManager.start()
    }
}

func adsManager(_ adsManager: IMAAdsManager!, didReceive error: IMAAdError!)
    avPlayer.play()
}

func adsManagerDidRequestContentPause(_ adsManager: IMAAdsManager!) {
    avPlayer.pause()
}

func adsManagerDidRequestContentResume(_ adsManager: IMAAdsManager!) {
    avPlayer.play()
}

```



If you have enabled Picture in Picture support and are using the `IMAPictureInPictureProxy`, you will need an additional step in order to track ad related metrics correctly.

```objc

#import<MuxStatsGoogleIMAPlugin/MuxStatsGoogleIMAPlugin.h>

- (void)viewDidLoad {
  // Follow the instructions from pod 'GoogleAds-IMA-iOS-SDK' to set up
  // your adsLoader and set your ViewController as the delegate
  //
  // From your ViewController, when you call either
  //    monitorAVPlayerViewController:withPlayerName:playerData:videoData:
  //    monitorAVPlayerLayer:withPlayerName:playerData:videoData:
  //
  // You will get back a MUXSDKPlayerBinding object
  [MUXSDKPlayerBinding *playerBinding] = [MUXSDKStats monitorAVPlayerViewController:_avplayerController
                                                                     withPlayerName:DEMO_PLAYER_NAME
                                                                       customerData:customerData];
  //
  // Use the MUXSDKPlayerBinding object to initialize the MuxImaListener class
  //
  _adsListener = [[MUXSDKIMAAdListener alloc] initWithPlayerBinding:playerBinding 
                                                   monitorAdsLoader:adsLoader];
  [_adsListener setPictureInPicture:YES];

  //...

  // When you send your ad request, you must report it to the IMA listener so it can properly track state
  [_adsListener clientAdRequest:request]; // for Client-Side Ads (the usual case)
  // OR
  [_adsListener daiAdRequest:daiRequest]; // for Dynamic Server-Side Ads (DAI/SSAI)
}
// when the adsLoader fires adsLoadedWithData you get a
// reference to the adsManager. Set your ViewController as the delegate
// for the adsManager
- (void)adsLoader:(IMAAdsLoader *)loader adsLoadedWithData:(IMAAdsLoadedData *)adsLoadedData {
    _adsManager = adsLoadedData.adsManager;
    // Set your adsManager delegate before passing it to adsListener for monitoring
    _adsManager.delegate = self;
    IMAAdsRenderingSettings *adsRenderingSettings = [[IMAAdsRenderingSettings alloc] init];
    adsRenderingSettings.webOpenerPresentingController = self;
    [_adsManager initializeWithAdsRenderingSettings:adsRenderingSettings];
    [_adsListener monitorAdsManager: _adsManager];
}

//
- (void)adsManager:(IMAAdsManager *)adsManager didReceiveAdEvent:(IMAAdEvent *)event {
    // When the SDK notified us that ads have been loaded, play them.
    if (event.type == kIMAAdEvent_LOADED) {
        [_adsManager start];
    }
}

- (void)adsManager:(IMAAdsManager *)adsManager didReceiveAdError:(IMAAdError *)error {
    [_avplayer play];
}

- (void)adsManagerDidRequestContentPause:(IMAAdsManager *)adsManager {
    [_avplayer pause];
}

- (void)adsManagerDidRequestContentResume:(IMAAdsManager *)adsManager {
    [_avplayer play];
}

```

```swift

import MuxCore
import MUXSDKStats
import GoogleInteractiveMediaAds
import MuxStatsGoogleIMAPlugin

var adsListener: MUXSDKIMAAdListener?

override func viewDidLoad() {
  super.viewDidLoad()
  // Follow the instructions from pod 'GoogleAds-IMA-iOS-SDK' to set up
  // your adsLoader and set your ViewController as the delegate
  //
  // From your ViewController, when you call either
  //    monitorAVPlayerViewController
  //    monitorAVPlayerLayer
  //
  // You will get back a MUXSDKPlayerBinding object

  // Configure your ads loader delegate before initializing MUXSDKIMAAdListener
  adsLoader.delegate = self

  // Setup your content players AVPlayerViewController or AVPlayerLayer
  let playerViewController = AVPlayerViewController()

  let playerBinding = MUXSDKStats.monitorAVPlayerViewController(
    self, 
    withPlayerName: playName, 
    customerData: customerData
  )

  // Use the MUXSDKPlayerBinding object to initialize the MuxImaListener class
  // Save a reference to adsListener, we'll use a property
  let adsListener = MUXSDKIMAAdListener(
    playerBinding: playerBinding!,
    monitorAdsLoader: adsLoader
  )
  adsListener.setPictureInPicture(true)
  self.adsListener = adsListener
  // ... 

  // When you send your ad request, you must report it to the IMA listener so it can properly track state
  adsListener.clientAdRequest(request) // for Client-Side Ads (the usual case)
  // OR
  adsListener.daiAdRequest(daiAdRequest) // for Dynamic Server-Side Ads (SSAI)
}

// the adsLoader delegate will fire this and give access to the adsManager
// the application needs to register as a delegate for the adsManager too
func adsLoader(_ loader: IMAAdsLoader!, adsLoadedWith adsLoadedData: IMAAdsLoadedData!) {
    adsManager = adsLoadedData.adsManager;
    adsManager.delegate = self;
    adsListener?.monitorAdsManager(adsManager)
}

// all of these events get fired by the adsManager delegate
// when this happens, the application needs to do some stuff and send the events
// to our sdk
func adsManager(_ adsManager: IMAAdsManager!, didReceive event: IMAAdEvent!) {
    if (event.type == kIMAAdEvent_LOADED) {
      adsManager.start()
    }
}

func adsManager(_ adsManager: IMAAdsManager!, didReceive error: IMAAdError!)
    avPlayer.play()
}

func adsManagerDidRequestContentPause(_ adsManager: IMAAdsManager!) {
    avPlayer.pause()
}

func adsManagerDidRequestContentResume(_ adsManager: IMAAdsManager!) {
    avPlayer.play()
}

```



For a complete example project written in Swift with UIKit, check out the `Example/DemoApp` folder of [muxinc/mux-stats-google-ima](https://github.com/muxinc/mux-stats-google-ima)

You can find more examples in the "/Examples" directory of [muxinc/mux-stats-sdk-avplayer](https://github.com/muxinc/mux-stats-sdk-avplayer) on GitHub. All of these apps have examples with Google IMA ads. `video-demo` is an iOS app written in Swift and `TVDemoApp` is a TVOS app written in objective-c

## Track orientation change events

As of 1.3.0 Mux-Stats-AVPlayer can optionally track `orientationchange` events. To use this functionality, call the `orientationChange(forPlayer:with:)` method.

These events will show up on the events log on the view views page.

```objc

@implementation ViewController

  - (void)viewWillTransitionToSize:(CGSize)size
       withTransitionCoordinator:(id<UIViewControllerTransitionCoordinator>)coordinator {
    [super viewWillTransitionToSize:size withTransitionCoordinator:coordinator];
    [coordinator animateAlongsideTransition:^(id<UIViewControllerTransitionCoordinatorContext> context) {} completion:^(id<UIViewControllerTransitionCoordinatorContext> context) {
        [MUXSDKStats orientationChangeForPlayer:DEMO_PLAYER_NAME withOrientation:[self viewOrientationForSize:size]];

    }];
    }

  - (MUXSDKViewOrientation) viewOrientationForSize:(CGSize)size {
      return (size.width > size.height) ? MUXSDKViewOrientationLandscape : MUXSDKViewOrientationPortrait;
  }

@end

```

```swift

class VideoPlayerController: AVPlayerViewController {
    override func viewWillTransition(to size: CGSize, with coordinator: UIViewControllerTransitionCoordinator) {
        super.viewWillTransition(to: size, with: coordinator)
        MUXSDKStats.orientationChange(forPlayer: "playerName", with: self.viewOrientationForSize(size: size))
    }

    func viewOrientationForSize(size: CGSize) -> MUXSDKViewOrientation {
        return (size.width > size.height) ? MUXSDKViewOrientation.landscape : MUXSDKViewOrientation.portrait
    }
}

```



## Usage with AVQueuePlayer

To use with `AVQueuePlayer`  you will need to follow these steps:

1. Listen for `AVPlayerItemDidPlayToEndTime` in your application
2. When that notification fires, call `videoChange(forPlayer:with:)`

Here is an example that sets up a `AVQueuePlayer` with two items, and listener after the first item finishes playing and passes in new `videoData`.

```swift

class AVQueuePlayerViewController: AVPlayerViewController {
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        guard let url1 = URL(string: "https://stream.mux.com/xwatk58X7MkCRBA47f01U9bGHt1lklEW5.m3u8") else {
            return
        }
        
        guard let url2 = URL(string: "https://stream.mux.com/HEp7gv53NFjtbZPZB8s02ZiNixXUgYgT7.m3u8") else {
            return
        }
        
        let item1 = AVPlayerItem(url: url1)
        let item2 = AVPlayerItem(url: url2)
        
        NotificationCenter.default.addObserver(
            self,
            selector: #selector(self.playerItemDidReachEnd),
            name: NSNotification.Name.AVPlayerItemDidPlayToEndTime,
            object: item1
        )
        
        let playerData = MUXSDKCustomerPlayerData(environmentKey: "ENV_KEY")
        playerData?.playerName = "AVPlayer"
        
        let videoData = MUXSDKCustomerVideoData()
        videoData.videoIsLive = false
        videoData.videoTitle = "Title1"
        
        guard let customerData = MUXSDKCustomerData(
            customerPlayerData: playerData,
            videoData: videoData,
            viewData: nil
        ) else {
            return
        }
        
        MUXSDKStats.monitorAVPlayerViewController(self, withPlayerName: "AVPlayer", customerData: customerData)
        
        player = AVQueuePlayer(items: [item1, item2])
        player?.play()
    }
    
    @objc func playerItemDidReachEnd(notification: NSNotification) {
        let videoData = MUXSDKCustomerVideoData()
        videoData.videoTitle = "Title2"
        videoData.videoId = "RollerbladingCoder2"
        
        guard let customerData = MUXSDKCustomerData(
            customerPlayerData: nil,
            videoData: videoData,
            viewData: nil
        ) else {
            return
        }
        
        MUXSDKStats.videoChange(forPlayer: "AVPlayer", with: customerData)
    }
}

```



## Overriding device metadata

By default, the Mux Data SDK for iOS collects data about your users' device to report on the dashboard. If you wish to provide your own device metadata, you can use `CustomerViewerData` to override the detected values.

```objc

// ... set up videoData, playerData, etc

MUXSDKCustomerViewerData *viewerData = [[MUXSDKCustomerViewerData alloc] init];
viewerData.viewerApplicationName = @"MUX DemoApp";
viewerData.viewerDeviceCategory = "kiosk";
viewerData.viewerDeviceModel = "ABC-12345";
viewerData.viewerDeviceManufacturer = "Example Display Systems, Inc";
MUXSDKCustomerData *customerData = [[MUXSDKCustomerData alloc] initWithCustomerPlayerData:playerData
                                                                                videoData:videoData
                                                                                  viewData:viewData
                                                                                customData:customData
                                                                                viewerData:viewerData];
_playerBinding = [MUXSDKStats monitorAVPlayerViewController:_avplayerController withPlayerName:DEMO_PLAYER_NAME customerData:customerData];


```

```swift

// ... set up videoData, playerData, etc

let viewerData = MUXSDKCustomerViewerData()
viewerData.viewerDeviceCategory = "kiosk"
viewerData.viewerDeviceModel = "ABC-12345"
viewerData.viewerDeviceManufacturer = "Example Display Systems, Inc"

let customerData = MUXSDKCustomerData(
    customerPlayerData: playerData,
    videoData: videoData,
    viewData: viewData,
    customData: customData,
    viewerData: viewerData
)

```



## Handling errors manually

By default, `automaticErrorTracking` is enabled which means the Mux SDK will catch errors that the player throws and track an `error` event. Error tracking is meant for fatal errors. When an error is thrown it will mark the view as having encountered an error in the Mux dashboard and the view will no longer be monitored.

If you want to disable automatic error tracking and track errors manually, you can do so by passing `false` as the `automaticErrorTracking` parameter to the `monitorAVPlayerLayer`, `monitorAVPlayerViewController`, or `monitorAVPlayer` method you are using.

Whether automatic error tracking is enabled or disabled, you can dispatch errors manually with `dispatchError(_:withMessage:forPlayer:)`.

```objc

_avplayer = player;
_avplayerController.player = _avplayer;

NSString *playerName = @"iOS AVPlayer"
NSString *environmentKey = @"yourEnvironmentKey";

MUXSDKCustomData *customData = [[MUXSDKCustomData alloc] init];
[customData setCustomData1:@"my-custom-dimension"];

MUXSDKCustomerPlayerData *playerData = [[MUXSDKCustomerPlayerData alloc] initWithEnvironmentKey:environmentKey];

MUXSDKCustomerVideoData *videoData = [[MUXSDKCustomerVideoData alloc] init];
videoData.videoTitle = @"Your Video Title";

MUXSDKCustomerViewData *viewData= [[MUXSDKCustomerViewData alloc] init];
viewData.viewSessionId = @"some session id";

MUXSDKCustomerViewerData *viewerData = [[MUXSDKCustomerViewerData alloc] init];
viewerData.viewerApplicationName = @"MUX DemoApp";

MUXSDKCustomerData *customerData = [[MUXSDKCustomerData alloc] initWithCustomerPlayerData:playerData
                                                                                videoData:videoData
                                                                                 viewData:viewData
                                                                               customData:customData
                                                                               viewerData:viewerData];


_playerBinding = [MUXSDKStats monitorAVPlayerViewController:_avplayerController 
                                             withPlayerName:playerName 
                                               customerData:customerData
                                               automaticErrorTracking: NO];

// later you can dispatch an error yourself
[MUXSDKStats dispatchError: @"1234"
               withMessage: @"Something is not right"
                 forPlayer: playerName];

```

```swift

let playerName = "iOS AVPlayer"

let playerData = MUXSDKCustomerPlayerData(environmentKey: "ENV_KEY")

let videoData = MUXSDKCustomerVideoData()
videoData.videoTitle = "Your Video Title"

guard let customerData = MUXSDKCustomerData(
    customerPlayerData: playerData,
    videoData: videoData,
    viewData: nil,
    customData: nil,
    viewerData: nil
) else {
    return
}

let playerBinding = MUXSDKStats.monitorAVPlayerViewController(
    playerViewController,
    withPlayerName: playerName,
    customerData: customerData,
    automaticErrorTracking: false
)

// Later, you can dispatch an error yourself
MUXSDKStats.dispatchError(
    "1234",
    withMessage: "Something is not right",
    forPlayer: playerName
)

```



## Error Categorization

Set custom error metadata to distinguish between fatal errors or warnings and classify errors as playback failures or business exceptions. Errors categorized as warnings or as business exceptions are not considered playback failures, meaning these errors are excluded from alerting, giving a more accurate picture of the health of your system with less noise from alerts. You can find [more general information on Error Categorization here](/docs/guides/error-categorization).

This is an example of how to categorize an error event to be a warning.

```objc

_avplayer = player;
_avplayerController.player = _avplayer;

NSString *playerName = @"iOS AVPlayer";
NSString *environmentKey = @"yourEnvironmentKey";

MUXSDKCustomData *customData = [[MUXSDKCustomData alloc] init];
[customData setCustomData1:@"my-custom-dimension"];

MUXSDKCustomerPlayerData *playerData = [[MUXSDKCustomerPlayerData alloc] initWithPropertyKey:environmentKey];

MUXSDKCustomerVideoData *videoData = [MUXSDKCustomerVideoData new];
videoData.videoTitle = @"Your Video Title";

MUXSDKCustomerViewData *viewData= [[MUXSDKCustomerViewData alloc] init];
viewData.viewSessionId = @"some session id";

MUXSDKCustomerViewerData *viewerData = [[MUXSDKCustomerViewerData alloc] init];
viewerData.viewerApplicationName = @"MUX DemoApp";

MUXSDKCustomerData *customerData = [[MUXSDKCustomerData alloc] initWithCustomerPlayerData:playerData
                                                                                videoData:videoData
                                                                                 viewData:viewData
                                                                               customData:customData
                                                                               viewerData:viewerData];

_playerBinding = [MUXSDKStats monitorAVPlayerViewController:_avplayerController 
                                             withPlayerName:playerName 
                                               customerData:customerData];

// later you can dispatch an error yourself
[MUXSDKStats dispatchError: @"1234"
               withMessage: @"Something is not right"
                  severity: MUXSDKErrorSeverityWarning
              errorContext: @"Error context"
                 forPlayer: playerName];

```

```swift

let playerName = "iOS AVPlayer"

let playerData = MUXSDKCustomerPlayerData(environmentKey: "ENV_KEY")

let videoData = MUXSDKCustomerVideoData()
videoData.videoTitle = "Your Video Title"

guard let customerData = MUXSDKCustomerData(
  customerPlayerData: playerData,
  videoData: videoData,
  viewData: nil,
  customData: nil,
  viewerData: nil
) else {
  return
}

let playerBinding = MUXSDKStats.monitorAVPlayerViewController(
  playerViewController,
  withPlayerName: playerName,
  customerData: customerData
)

// Later, you can dispatch an error yourself
MUXSDKStats.dispatchError(
  "1234",
  withMessage: "Something is not right",
  severity: MUXSDKErrorSeverity.warning,
  errorContext: "Error Context",
  forPlayer: playerName
)

```



This is an example of how to categorize an error event as a business exception.

```objc

// Call this method from the source of the business exception with parameters appropriate to your integration.
- (void)dispatchBusinessExceptionWithPlayerName:(NSString *)playerName
                              playerErrorSeverity:(MUXSDKErrorSeverity)errorSeverity
                              playerErrorCode:(NSString *)playerErrorCode
                              playerErrorMessage:(NSString *)playerErrorMessage
                              playerErrorContext:(NSString *)playerErrorContext {
  [MUXSDKStats dispatchError: playerErrorCode,
                 withMessage: playerErrorMessage,
                    severity: MUXSDKErrorSeverityWarning,
         isBusinessException: YES,
                errorContext: playerErrorContext,
                   forPlayer: playerName];
}

```

```swift

// Call this method from the source of the business exception with parameters appropriate to your integration.
func dispatchBusinessException(playerName: String,
                               playerErrorCode: String,
                               playerErrorMessage: String,
                               playerErrorContext: String) {
  MUXSDKStats.dispatchError(
    playerErrorCode,
    withMessage: playerErrorMessage,
    severity: MUXSDKErrorSeverity.warning,
    isBusinessException: true,
    errorContext: playerErrorContext,
    forPlayer: playerName
  )
}

```



## App Store warning: ITMS-90809: Deprecated API Usage

It has come up a few times that users of our iOS library get this warning from Apple.

> Apple will stop accepting submissions of apps that use UIWebView APIs . See https://developer.apple.com/documentation/uikit/uiwebview for more information.

If you run `grep -r "UIWebView" .` in your project you will see a match coming from the `dSYM/` directory in Mux-Core. At first glance, we too thought our SDK was triggering this warning.

However, after looking into this with several different applications we found that the warning was not being triggered by our SDK. In every case it was coming from another 3rd party.

Note that none of the Mux iOS libraries (including `Mux-Core` and `Mux-Stats-AVPlayer`) use `UIWebView`. If you are getting this warning you must have another SDK that is using `UIWebView`.

The reason there is some confusion around this and the reason you get a match in the `dSYM/` directory in Mux-Core is because our SDK links to `UIKit` and targets a version of iOS that *may include* `UIWebView`.  The `dSYM` files are used for debugging purposes and they do not contain any functional code. You may see that this same confusion came up in other SDKs like Mapbox and Stripe (listed below).

### Resources:

* [Mux issue #32](https://github.com/muxinc/mux-stats-sdk-avplayer/issues/32)
* [Mux issue #53](https://github.com/muxinc/mux-stats-sdk-avplayer/issues/53)
* [Mapbox issue #373](https://github.com/mapbox/ios-sdk-examples/issues/373)
* [Stripe issue #82](https://github.com/stripe/stripe-terminal-ios/issues/82#issuecomment-625406168)

<LinkedHeader step={steps[6]} />

### Current release

#### v4.11.0

Improvements:

* Observe and report changes in network connection type

Fixes:

* Use Foundation networking for request metrics to avoid missing values from AVMetrics

### Previous releases

#### v4.10.0

Updates:

* Add (incubating) playbackModeChange API
* Add cumulative ad playing time and total content time metric tracking. The metrics track the "wall-clock" time spent with video playing during a view, excluding buffering, seeking, and startup time.

#### v4.9.0

Improvements:

* Move calls to [`AVPlayerItem.currentDate()`](https://developer.apple.com/documentation/avfoundation/avplayeritem/currentdate\(\)) and [`AVPlayerItem.accessLog()`](https://developer.apple.com/documentation/avfoundation/avplayeritem/accesslog\(\)) off the main thread.

#### v4.8.2

Fixes:

* Disable Text-Based API (.tbd) generation for framework builds. CocoaPods fails to strip these, and this can lead to App Store upload errors.

#### v4.8.1

Fixes:

* Fix crash `Invalid parameter not satisfying: tag != nil` introduced in v4.8.0

#### v4.8.0

Improvements:

* Use AVMetrics to generate bandwidth metric events for HLS streams (iOS 18+, tvOS 18+, visionOS 2+). This also enables automatic CDN change tracking via the `X-CDN` header for these OS versions.

#### v4.7.0

Improvements:

* Fix crash when AVPlayer is used off the main thread
* Moves some calls to AVAsset to the background to avoid blocking the main thread
* Fixes mismatched bitrate/size reporting in rendition change events

#### v4.6.0

Improvements:

* Builds from source for both Swift Package Manager and CocoaPods for more flexible integration in your projects
* Various tidying-up of public header files

Fixes:

* Fixes an issue where some customer viewer data fields were not being sent

#### v4.4.0

Improvements:

* Updates the MuxCore dependency to 5.3.x
* preserve debugging symbols from framework build

Fixes:

* update package spec with missing macCatalyst platform

#### v4.3.0

Improvements:

* Update MuxCore to v5.2.0

#### v4.2.0

Fixes:

* Send ended when an AVPlayerItem finishes playing to completion

#### v4.1.2

Improvements:

* Update MuxCore to v5.1.2

#### v4.1.1

Improvements:

* Update MuxCore to v5.1.1

#### v4.1.0

Improvements:

* Automatically dispatch a `viewend` when a new `AVPlayerItem` becomes the player `currentItem`.

Fixes:

* No longer dispatch `viewinit` if the player `currentItem` is replaced with `nil`.

#### v4.0.0

New:

* Error events can be categorized with warning or fatal severity levels.
* Error events can be categorized as business exceptions.

Improvements:

* Player error details (same as listed above) are no longer deduplicated and are explicitly included with each error event sent to Mux.

API Changes:

* The minimum deployment targets for the SDK are now iOS 12 and tvOS 12.
* Removes deprecated `MUXSDKStats` APIs.

#### v3.6.2

Fixes:

* A crash that occurred when monitoring playback using AirPlay.

#### v3.6.1

Improvements:

* Include privacy manifest file

#### v3.6.0

Improvements:

* Applications running on `visionOS` can monitor metrics for `AVPlayerViewController` or `AVPlayer` with a fixed player size. We recommend testing your `visionOS` application's AVPlayer monitoring integration on both the simulator and a physical device prior to deploying to the App Store.

Fixes:

* A memory leak has been fixed that occurred when tearing down monitoring of a standalone `AVPlayer` with a fixed player size.

Known Issues:

* Installation using Cocoapods on `visionOS` applications is not currently supported. Installation on `iOS` and `tvOS` using Cocoapods is not affected.
* Monitoring `AVPlayerLayer` playback on `visionOS` applications is not supported at this time.
* Views from playback on `visionOS` will always indicate Used Fullscreen to be `false`.

#### v3.5.1

Fixes:

* Add referential safety checks when dispatching session data

#### v3.5.0

API Changes:

* Expose reporting an error context parameter alongside customer errors

Known Issues:

* Including a `SESSION-DATA` tag in the manifest of a monitored HLS stream may cause a crash in v3.5.0 or earlier of `MUXSDKStats`. To resolve the issue limit `SESSION-DATA` tags only to applications that use `MUXSDKStats` v3.5.1 or higher.

#### v3.4.2

Fixes:

* Pin MuxCore to specific version consistent across Cocoapods and Swift Package Manager

#### v3.4.1

Fixes:

* Add state check when dispatching viewend event

Improvements:

* Update MuxCore dependency

#### v3.4.0

API Changes:

* Monitor AVPlayer with a fixed player size
* Set custom player software name and version values when initializing a new binding

Improvements

* Documentation revisions
* Audio-only monitoring example

#### v3.3.3

Fixes:

* Set the player width and height dimensions to the entire area of the screen where the player is present. Before this change, player width and height were set to the width and height of the video drawn on screen. Letterboxed or pillarboxed areas of the player were previously excluded as a result.

Player width and height dimensions are now equal to the `AVPlayerLayer` bounds or `AVPlayerViewController` view bounds, depending on which is used. Previously `AVPlayerViewController` `videoBounds` or `AVPlayerLayer` videoRect\` were used to set the player width and height.

Upscale Percentage or Downscale Percentage calculations are not affected if the player draws the video with the same aspect ratio as the video resolution.

#### v3.3.2

Fixes:

* Crash when removing a time observer from the wrong AVPlayer instance during monitoring teardown
  Improvements:
* Add Swift Package Manager example application

#### v3.3.1

Improvements:

* Update MuxCore with backfilled header nullability annotations to remove build warnings

#### v3.3.0

Updates:

* Add `drmType` to `MUXSDKCustomerViewData` so you can track this field if you wish

Improvements:

* System reliability updates during large events

#### v3.2.1

Fixes:

* Fix ad metadata not being reported

#### v3.2.0

Fixes:

* Fix wrong viewer time when finishing seek after an ad break

#### v3.1.0

Updates:

* Add Frame Drop Metrics (#172)
* Add 5 more Custom Dimensions (6 through 10) to `MUXSDKCustomData`

#### v3.0.0

Updates:

* Add fields to `CustomerViewerData` allowing them to override detected device metadata values
* Add Request ID metadata property to BandwidthMetricData
* Add Customer overrides for Device Metadata

Breaking:

* Due to Xcode 14, support for iOS and tvOS versions 9 and 10 have been removed. This may result in a warning for client applications with deployment versions below iOS/tvOS 11. For more information [see the last 'Deprecations' block in the release notes](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-14-release-notes).

Improvements:

* Update to MuxCore 4.0.0, Xcode 14
* Improve HLS/DASH segment request metrics (#165)

#### v2.13.2

* Fix an issue with certain error conditions not being properly recognized on the data dashboard

#### v2.13.1

* Relax muxcore pod dependency version, can now update any to 3.x version, 3.12 or higher
* Start a new View if a View receives events after 1 hour of inactivity

#### v2.12.1

* Fix: Crash in `AVMetadataItem` inspection when dispatching session data
* Fix: State check for `isPaused`

#### v2.12.0

* Fix: Register seek events when state is buffering
* Capture HLS session data and send event to core

#### v2.11.0

* Set Xcode build setting `APPLICATION_EXTENSION_API_ONLY = YES`
* Fix: Update rendition change logic to fire events after playback has started

#### v2.10.0

* Fix: Missing programmatic seek events for iOS 15.0
* Add picture in picture ads compatibility with mux-stats-google-ima 0.7.0

#### v2.9.0

* Fix: Missing programmatic seek latency metric and sequencing bugs
* Fix: Clear customer metadata stored under `playerName` when `destroyPlayer` is called
* Add Carthage binary project specification
* Add internal device detection properties

#### v2.8.0

* Fixes a bug that caused missing seek events when seeking programmatically

#### v2.7.0

* Add `player_live_edge_program_time`
* Add `player_program_time`

#### v2.6.0

* Allow overriding of viewer information (application name)
* Tests for AVQueuePlayer
* Custom beacon collection domains
* Adds `programChangeForPlayer:withCustomerData:`

#### v2.5.0

* Consolidates  `MUXSDKCustomerViewData`, `MUXSDKCustomerVideoData`, and `MUXSDKCustomerPlayerData` into `MUXSDKCustomerData` and deprecates methods that treat these as separate arguments
* Adds support for custom dimensions

#### v2.4.2

* Replaces `identifierForVendor` with alternative UUID
* Fixes race condition when checking viewer connection type

#### v2.4.1

* Fixes a bug when disabling automatic video change that could sometimes result in views not being split apart and/or having a high seek latency.

#### v2.4.0

* Automatically build statically linked frameworks
* Removes use of categories
* Updates documentation

#### v2.3.2

* Adds a new method to disable built in `videochange` calls when using `AVQueuePlayer`. This method can be called as:

```
[MUXSDKStats setAutomaticVideoChange:PLAYER_NAME enabled:false];
```

#### v2.2.2

* Fixes a code signing is missing error for Mac Catalyst
* Fixes a crash from a KVO observer being removed incorrectly
* Fixes bugs in seeking tracking for tvOS

#### v2.2.1

* Fixes a bug where AirPlay rebuffering was incorrectly reported as paused

#### v2.2.0

* Add Swift PM support

#### v2.1.0

* Submits `viewer_device_model` field
* Updates our implementation of the Google IMA SDK in demo apps to work with the latest version
* Automated UI test for ads

#### v2.0.0

This release moves the build process to use [XCFramework bundle type](https://developer.apple.com/videos/play/wwdc2019/416/). For iOS, there are no changes required to your application code.

If you are using this SDK with TVOS the name of the module has changed (the `Tv` suffix is no longer needed):

TVOS before 2.0:

```objc
@import MuxCoreTv;
@import MUXSDKStatsTv;
```

TVOS after 2.0:

```objc
@import MuxCore;
@import MUXSDKStats;
```

#### v1.7.0

* Adds support for `view_session_id`.
* Adds support for `player_remote_played` - this will be true when a video is shown over AirPlay.

#### v1.6.0

* Add `viewer_connection_type` for iOS (either `wifi` or `cellular`). Detecting `viewer_connection` type is done off the main thread to make sure this doesn't interfere with the performance of your application. Note that `viewer_connection_type` is omitted from TVOS because in versions before TVOS 12 there is no reliable way to detect `wifi` vs. `ethernet`.

#### v1.4.1

* (bugfix) `monitorAVPlayerLayer` with optional argument `automaticErrorTracking` was misnamed to `withAutomaticErrorTracking`. This has been changed to the correct name which is consistent with the corresponding `monitorAVPlayerViewController` method (thanks @hlung in [#58](https://github.com/muxinc/mux-stats-sdk-avplayer/pull/58))
* (bugfix) nullability warnings for MUXSDKStats (thanks @hlung in [#58](https://github.com/muxinc/mux-stats-sdk-avplayer/pull/58))

#### v1.4.0

* add option to disable automatic error tracking when calling either `monitorAVPlayerViewController` or `monitorAVPlayerLayer`
* add `MUXSDKStats.dispatchError` method to manually dispatch an error

You probably will not need to use these features, but if your player is throwing noisy non-fatal errors or you want to catch the player errors yourself and take precise control over the error code and error message then you now have that ability.

Dispatching an error should only be used for fatal errors. When the player goes into the error state then it is no longer being tracked and the view will show up as having encountered an error in the Mux dashboard.

#### v1.3.8

* Performance updates that optimize main thread usage.

#### v1.3.7

* Bug fix: Update our framework build process to be compatible with `carthage 0.35.0`. See the [GitHub issue](https://github.com/muxinc/mux-stats-sdk-avplayer/issues/54) for more details. The gist of it is that Carthage no longer ignores dSYM files, so those need to be packaged up correctly with the framework.

#### v1.3.6

* Bug fix: Rebuild frameworks without importing UIKit (we don't use it). This came to our attention when it was reported that our SDK was triggering this warning from Apple “The App Store will no longer accept new apps using UIWebView as of April 2020 and app updates using UIWebView as of December 2020.”

#### v1.3.5

* Bug fix for usage with `AVQueuePlayer`. Unlike other methods of changing the `playerItem` on an `AVPlayer` instance, when `AVQueuePlayer` progresses from one item to the next the `rate` observer does not fire so we have to handle it in a special case. See instructions above for usage with `AVQueuePlayer`.

#### v1.3.4

* Update scaling logic to report upscaling based on logical resolution, not physical resolution. This will result in lower upscaling percentages, but correlates more closely with perceived visual quality

#### v1.3.3

* Fix a bug to make sure all needed header files are included in the `tvOS` framework

#### v1.3.2

* Fix a bug in request metrics tracking, request metric event timestamps should always be sent in Unix millisecond timestamps, not seconds.

#### v1.3.1

* Fix an issue where multiple AVPlayer instances that are tracked simultaneously report the same throughput metrics.

#### v1.3.0

* Add support for `orientationchange` events. This can be dispatched with `MUXSDKStats orientationChangeForPlayer: withOrientation:`
* Add support for automatically tracking `renditionchange` events. You can see this new event in the events list for a view.
* Improve implementation for bandwidth metrics calculation. Instead of polling for changes on the access log, use `AVPlayerItemNewAccessLogEntryNotification`
* Fix bug in `programChange` so that it works consistently now
* Dispatch `viewend` when `destoryPlayer` is called. Previously this was not called which didn't affect metrics, but resulted in a `viewdropped` event in the events list.

#### v1.2.1

* Fix bug that prevents request metrics tracking from working. AVPlayer gives us `requestStart` and `requestResponseEnd`, so with those data points we can track throughput. This bug fix requires Mux-Stats-Core v2.1.3 or greater. Run `pod update Mux-Stats-AVPlayer`  and `pod update Mux-Stats-Core` to get the latest versions.

#### v1.2.0

* Fix bug in Mux-Stats-AVPlayer that prevents `videoChangeForPlayer` from working
* Fix bug in AVPlayer SDK where it misses initial play event at times if SDK is initialized too late. This could cause some iOS views to not be displayed in the monitoring dashboard, and to potentially have incomplete metrics such as Video Startup Time.
* Add ability to optionally pass in new player data when calling `videoChangeForPlayer`: `videoChangeForPlayer:withPlayerData:withVideoData`

#### v1.1.3

* Fix a bug to prevent an edge-case scenario where crashes can happen after calling `destroyPlayer` when observers have not yet bet set up on the player instance.

#### v1.1.2

* bump dependency version of Mux-Stats-Core to 2.1

#### v1.1.1

* bugfix - report the correct Mux Plugin Version. This SDK was erroneously reporting the incorrect 'Mux Plugin Version' attribute for views

#### v1.1.0

* Added new static method to `MUXSDKStats` `updateCustomerDataForPlayer:withPlayerData:withVideoData`. This allows a developer to update customerPlayerData and/or customerVideoData after the SDK has been initialized. Not all metadata can be changed if it was previously set, but all metadata that was not set initially can be updated to the intended values.

#### v1.0.2

* Fix a bug that caused slowness when loading AVPlayer due to checking currentItem.asset.duration before the duration was loaded

#### v1.0.1

* Fix a bug with incorrect source video duration

#### v1.0.0

* Extract GoogleAds-IMA-iOS-SDK into a separate library (Mux-Stats-Google-IMA). The reason for this change was to remove the hard dependency on GoogleAds-IMA-iOS-SDK
* In order to implement ad events tracking, please follow the instructions to use this library (Mux-Stats-AVPlayer) in conjunction with Mux-Stats-Google-IMA and GoogleAds-IMA-iOS-SDK

#### 0.1.5

* add support for tracking ad playback with GoogleAds-IMA-iOS-SDK

#### 0.1.1

* add support for AVPlayer monitoring

# Source: https://www.mux.com/docs/guides/monitor-jw-player-ios.md

# Monitor JW Player (iOS)
This guide walks through integration with [JW Player](https://www.jwplayer.com/) for the web to collect video performance metrics with Mux data.
In order to integrate Mux Data tracking for your JW Player, you will need to be using JW Player `3.x` or later. You will need to already have a JW Player license key and an iOS app with a working implementation of `JWPlayer-SDK`.

## Features

The following data can be collected by the Mux Data SDK when you use the \{featureDef.name} SDK, as described
&#x20;       below.

```md
- Engagement metrics
- Quality of Experience Metrics
- Live Stream Latency metric

```

Notes:

```md
No notes provided
```

## 1. Install Mux Data SDK

```
pod 'Mux-Stats-JWPlayer', '~> 0.3'
```

This will install `Mux-Stats-JWPlayer` and the latest current release of our [core Objective-C library](https://github.com/muxinc/stats-sdk-objc).

## 2. Initialize the Mux monitor

Get your `ENV_KEY` from the [Mux environments dashboard](https://dashboard.mux.com/environments).

<Callout type="info" title="Env Key is different than your API token">
  `ENV_KEY` is a client-side key used for Mux Data monitoring. These are not to be confused with API tokens which are created in the admin settings dashboard and meant to access the Mux API from a trusted server.
</Callout>

<Image src="/docs/images/env-key.png" width={2004} height={250} />

Next, import `MUXSDKStatsJWPlayer` into your application and call `MUXSDKStatsJWPlayer.monitorJWPlayerController`, passing in your JW player instance and metadata.

```swift
import MUXSDKStatsJWPlayer;

class VideoPlayerController: UIViewController {
   var player: JWPlayerController?

  override func viewDidLoad ()
      super.viewDidLoad()
    let config = JWConfig()
    config.file = "http://example.com/hls.m3u8"
    player = JWPlayerController(config: config)
  }

  override func viewDidAppear(_ animated: Bool) {
      super.viewDidAppear(animated)
        player!.view!.frame = self.view.bounds
      view.addSubview(player!.view)

      let playName = "iOS JW player"
      let playerData = MUXSDKCustomerPlayerData(environmentKey: "ENV_KEY");
      // insert player metadata
      let videoData = MUXSDKCustomerVideoData();
      // insert video metada
      MUXSDKStatsJWPlayer.monitorJWPlayerController(player!, name: playName, delegate: nil, playerData: playerData!, videoData: videoData)
            player!.play()
  }
}
```

## Register a delegate (optional)

If your own ViewController implements `<JWPlayerDelegate>` and you want to use it, then pass that in as the delegate argument to `monitorJWPlayerController`. See the example below:

```swift
override func viewDidAppear(_ animated: Bool) {
    super.viewDidAppear(animated)
    player!.view!.frame = self.view.bounds
    view.addSubview(player!.view)

    let playName = "iOS JW player"
    let playerData = MUXSDKCustomerPlayerData(environmentKey: "ENV_KEY");
    // insert player metadata
    let videoData = MUXSDKCustomerVideoData();
    // insert video metada
    // pass in `self` as the delegate
    MUXSDKStatsJWPlayer.monitorJWPlayerController(player!, name: playName, delegate: self, playerData: playerData!, videoData: videoData)
    player!.play()
}

// example of implementing a delegate method
func onReady(_ event: JWEvent & JWReadyEvent) {
  // this will get called when JWPlayer triggers onPlay
}
```

## 3. Make your data actionable

The only required field is `env_key`. But without some more metadata the metrics in your dashboard will lack the necessary information to take meaningful actions. Metadata allows you to search and filter on important fields in order to diagnose issues and optimize the playback experience for your end users.

Metadata fields are provided via the `MUXSDKCustomerPlayerData` and `MUXSDKCustomerVideoData` objects.

For the full list of properties view the header files for this interfaces:

* [MUXSDKCustomerPlayerData.h](https://github.com/muxinc/stats-sdk-objc/blob/master/XCFramework/MuxCore.xcframework/ios-arm64/MuxCore.framework/Headers/MUXSDKCustomerPlayerData.h)
* [MUXSDKCustomerVideoData.h](https://github.com/muxinc/stats-sdk-objc/blob/master/XCFramework/MuxCore.xcframework/ios-arm64/MuxCore.framework/Headers/MUXSDKCustomerVideoData.h)

For more details about each property, view the [Make your data actionable](/docs/guides/make-your-data-actionable-with-metadata) guide.

```swift
let playName = "iOS AVPlayer"
let playerData = MUXSDKCustomerPlayerData(environmentKey: "ENV_KEY");
playerData.viewerUserId = "1234"
playerData.experimentName = "player_test_A"
// note that the 'playerName' field here is unrelated to the 'playName' variable above
playerData.playerName = "My Main Player"
playerData.playerVersion = "1.0.0"

let videoData = MUXSDKCustomerVideoData();
videoData.videoId = "abcd123"
videoData.videoTitle = "My Great Video"
videoData.videoSeries = "Weekly Great Videos"
videoData.videoDuration = 120000 // in milliseconds
videoData.videoIsLive = false
videoData.videoCdn = "cdn"

MUXSDKStatsJWPlayer.monitorJWPlayerController(player!, name: playName, delegate: self, playerData: playerData!, videoData: videoData)
```

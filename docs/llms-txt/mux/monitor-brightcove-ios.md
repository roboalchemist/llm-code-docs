# Source: https://www.mux.com/docs/guides/monitor-brightcove-ios.md

# Monitor Brightcove (iOS)
This guide walks through integration with [Brightcove iOS player](https://player.support.brightcove.com/) to collect video performance metrics with Mux Data.
Brightcove's native SDK for iOS is based on `AVPlayerLayer`. You will need to be using Brightcove's iOS player version `6.x`.

## Features

The following data can be collected by the Mux Data SDK when you use the \{featureDef.name} SDK, as described
&#x20;       below.

```md
- Engagement metrics
- Quality of Experience Metrics

```

Notes:

```md
No notes provided
```

## 1. Install Mux Data SDK

```
pod 'Mux-Stats-AVPlayer', '~>3.0'
```

This will install `Mux-Stats-AVPlayer` and the latest current release of our [core Objective-C Library](https://github.com/muxinc/stats-sdk-objc). There will be no breaking updates in major versions, so you can safely run `pod update` for future versions.

Next, add correct import statement into your application.

## 2. Initialize AVPlayerLayer monitor

Get your `ENV_KEY` from the [Mux environments dashboard](https://dashboard.mux.com/environments).

<Callout type="info" title="Env Key is different than your API token">
  `ENV_KEY` is a client-side key used for Mux Data monitoring. These are not to be confused with API tokens which are created in the admin settings dashboard and meant to access the Mux API from a trusted server.
</Callout>

<Image src="/docs/images/env-key.png" width={2004} height={250} />

In your application, you will need to hook into Brightcove's SDK lifecycle events in order to access the underlying `AVPlayerLayer` instance.

```objc
@import BrightcovePlayerSDK;
@import MUXSDKStats;

@property (nonatomic, copy) NSString *trackedPlayerName;

- (void)playbackController:(id<BCOVPlaybackController>)controller didAdvanceToPlaybackSession:(id<BCOVPlaybackSession>)session
{
    // Destroy previous MUXSDKStats if this signifies the other view ended
    // Note: you may want to handle this in another lifecycle event, if you
    // have one that signifies when the video playback has ended/exited.
    if (self.trackedPlayerName != nil) {
        [MUXSDKStats destroyPlayer:self.trackedPlayerName];
    }

    MUXSDKCustomerPlayerData *playerData = [[MUXSDKCustomerPlayerData alloc] initWithEnvironmentKey:@"ENV_KEY"];
    [playerData setPlayerName: @"Brightcove SDK w/ Mux"];
    // set additional player metadata here
    MUXSDKCustomerVideoData *videoData = [MUXSDKCustomerVideoData new];
    [videoData setVideoId:@"EXAMPLE ID"];
    // set additional video metadata here
    self.trackedPlayerName = @"example_player_name";
    [MUXSDKStats monitorAVPlayerLayer:session.playerLayer withPlayerName:self.trackedPlayerName playerData:playerData videoData:videoData];
}
```

Refer to the detailed guide for AVPlayer to finish setup.

<GuideCard
  title="Detailed AVPlayer guide"
  description="After getting a reference to your AVPlayerLayer instance, finish configuring it."
  links={[
    {title: "Read the guide", href: "/docs/guides/monitor-avplayer"},
  ]}
/>

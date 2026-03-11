# Source: https://www.mux.com/docs/guides/monitor-chromecast.md

# Monitor Chromecast
This guide walks through integration with Chromecast to collect video performance metrics with Mux data.
Mux Data is the best way to monitor video streaming performance.

Integration is easy - just initialize the Mux SDK, pass in some metadata, and you're up and running in minutes.

This documents integration instructions for Chromecast. For other players, see the additional Integration Guides.

## Features

The following data can be collected by the Mux Data SDK when you use the \{featureDef.name} SDK, as described
&#x20;       below.

```md
- Engagement metrics
- Quality of Experience Metrics
- Web metrics such as Player Startup Time, Page Load Time, etc
- Average Bitrate metrics and `renditionchange` events
- Request metrics
- Customizable Error Tracking
- Custom Beacon Domain

```

Notes:

```md
Average Bitrate metrics available in v4.2.11 and newer.
```

## 1. Include the Mux Data SDK

Mux supports Chromecast applications that are built on top of the Cast Application Framework [CAF](https://developers.google.com/cast/docs/caf_receiver_overview) Receiver SDK. The CAF Receiver SDK supports the following [streaming protocols](https://developers.google.com/cast/docs/media#delivery-methods-and-adaptive-streaming-protocols).

A Chromecast application contains two main components: a sender and a receiver. The Mux Data SDK is integrated at the receiver side; include the `chromecast-mux.js` JavaScript file within your custom receiver application. You can use the Mux-hosted version of the script to receive automatic updates. (The API will not change within major versions, as in `chromecast/MAJOR_VERSION/chromecast-mux.js`).

```npm
npm install --save @mux/mux-data-chromecast
```

```yarn
yarn add @mux/mux-data-chromecast
```

```cdn
<script src="//src.litix.io/chromecast/4/chromecast-mux.js"></script>
```



## 2. Initialize Mux Data

Get your `ENV_KEY` from the [Mux environments dashboard](https://dashboard.mux.com/environments).

<Callout type="info" title="Env Key is different than your API token">
  `ENV_KEY` is a client-side key used for Mux Data monitoring. These are not to be confused with API tokens which are created in the admin settings dashboard and meant to access the Mux API from a trusted server.
</Callout>

<Image src="/docs/images/env-key.png" width={2004} height={250} />

To monitor video playback within your Chromecast application, pass the `PlayerManager` instance to `initChromecastMux` along with SDK options and metadata.

You can initialize within a message interceptor for the `LOAD` event, or immediately on app load as before. This suggestion changed in version 4.0.0 and newer.

```js
import initChromecastMux from '@mux/mux-data-chromecast';

var app = {
  init: function () {
    const context = cast.framework.CastReceiverContext.getInstance();
    const playerManager = context.getPlayerManager();
    let firstPlay = true;
    let playerInitTime = initChromecastMux.utils.now();

    playerManager.setMessageInterceptor(cast.framework.messages.MessageType.LOAD, loadRequestData => {
      if (firstPlay) {
        initChromecastMux(playerManager, {
          debug: false,
          data : {
            env_key: 'ENV_KEY', // required

            // Metadata
            player_name: 'Custom Player', // ex: 'My Main Player'
            player_init_time: playerInitTime,

            // ... additional metadata
          }
        });
      }

      return loadRequestData;
    });

    context.start();
  }
};

$(document).ready(function () {
  app.init();
});
```

After you've finished integration, the quickest way to see that the SDK is loaded is to pass `debug: true` in the options passed to the SDK. With this flag enabled, you can open the debug console, and you should start seeing debug statements from \[mux] when you click play on the video.

After playing a video, a few minutes after you stop watching, you'll see the results in your Mux account. We'll also email you when your first video view has been recorded. Log in to the dashboard and find the environment that corresponds to your env\_key and look for video views.

Note that it may take a few minutes for views to show up in the Mux Data dashboard.

## 3. Make your data actionable

[Detailed Documentation](/docs/guides/make-your-data-actionable-with-metadata)

Options are provided via the `data` object passed in the call to `initChromecastMux`.

All metadata details except for `env_key` are optional, however you'll be able to compare and see more interesting results as you include more details. This gives you more metrics and metadata about video streaming, and allows you to search and filter on important fields like the player version, CDN, and video title.

For more information, see the [Metadata Guide](/docs/guides/make-your-data-actionable-with-metadata).

## 4. Set or update metadata after initialization

There are some cases where you may not have the full set of metadata until after the video playback has started. In this case, you should omit the values when you first call `initChromecastMux`. Then, once you have the metadata, you can update the metadata with the `updateData` method.

```js
playerManager.mux.updateData({ video_title: 'My Updated Great Video' });
```

## 5. Changing the video

There are two cases where the underlying tracking of the video view need to be reset:

1. **New source:** When you load a new source URL into an existing player.
2. **New program:** When the program within a singular stream changes (such as a program change within a continuous live stream).

Note: You do not need to change the video info when changing to a different source of the same video content (e.g. different resolution or video format).

### New source

If your application plays multiple videos back-to-back in the same video player, you need to signal when a new video starts to the Mux SDK. Examples of when this is needed are:

* The player advances to the next video in a playlist
* The user selects a different video to play

In order to signal the Mux SDK that a new view is starting, you will need to emit a `videochange` event, along with metadata about the new video. See metadata in [Make your data actionable](/docs/guides/make-your-data-actionable-with-metadata) for the full list of video details you can provide. You can include any metadata when changing the video but you should only need to update the values that start with `video_`.

It's best to change the video info immediately after telling the player which new source to play.

The source change should be done by intercepting the `cast.framework.messages.MessageType.LOAD` message and doing the following:

```js
playerManager.setMessageInterceptor(cast.framework.messages.MessageType.LOAD, loadRequestData => {
  // It's important to only call this on subsequent videos being loaded, not
  // the first playback (where you call `initChromecastMux`).
  if (!firstVideo) {
    playerManager.mux.emit('videochange', { ... });
  }

  return loadRequestData;
});
```

### New program

In some cases, you may have the program change within a stream, and you may want to track each program as a view on its own. An example of this is a live stream that streams multiple programs back to back, with no interruptions.

In this case, you emit a `programchange` event, including the updated metadata for the new program within the continuous stream. This will remove all previous video data and reset all metrics for the video view, creating a new video view. See [Metadata](/docs/guides/make-your-data-actionable-with-metadata) for the list of video details you can provide. You can include any metadata when changing the video but you should only need to update the values that start with `video`.

Note: The `programchange` event is intended to be used *only* while the player is currently not paused. If you emit this event while the player is paused, the resulting view will not track video startup time correctly, and may also have incorrect watch time. Do not emit this event while the player is paused.

## 6. Advanced options

### Customize error tracking behavior

<Callout type="error" title="Errors are fatal">
  Errors tracked by mux are considered fatal meaning that they are the result of playback failures. If errors are non-fatal they should not be captured.
</Callout>

By default, `@mux/mux-data-chromecast` will track errors emitted from the video element as fatal errors. If a fatal error happens outside of the context of the player, you can emit a custom error to the mux monitor.

```js
playerManager.mux.emit('error', {
  player_error_code: 100,
  player_error_message: 'Description of error',
  player_error_context: 'Additional context for the error'
});
```

When triggering an error event, it is important to provide values for `player_error_code` and `player_error_message`. The `player_error_message` should provide a generalized description of the error as it happened. The `player_error_code` must be an integer, and should provide a category of the error. If the errors match up with the [HTML Media Element Error](https://developer.mozilla.org/en-US/docs/Web/API/MediaError), you can use the same codes as the corresponding HTML errors. However, for custom errors, you should choose a number greater than or equal to `100`.

In general you should not send a distinct code for each possible error message, but rather group similar errors under the same code. For instance, if your library has two different conditions for network errors, both should have the same `player_error_code` but different messages.

The error message and code are combined together and aggregated with all errors that occur in your environment in order to find the most common errors that occur. To make error aggregation as useful as possible, these values should be general enough to provide useful information but not specific to each individual error (such as stack trace).

You can use `player_error_context` to provide instance-specific information derived from the error such as stack trace or segment-ids where an error occurred. This value is not aggregated with other errors and can be used to provide detailed information. *Note: Please do not include any personally identifiable information from the viewer in this data.*

### Error translator

If your player emits error events that are not fatal to playback or the errors are unclear and/or do not have helpful information in the default error message and codes you might find it helpful to use an error translator or disable automatic error tracking all together.

```js
function errorTranslator (error) {
  return {
    player_error_code: translateCode(error.player_error_code),
    player_error_message: translateMessage(error.player_error_message),
    player_error_context: translateContext(error.player_error_context)
  };
}

initChromecastMux(playerManager, {
  debug: false,
  errorTranslator: errorTranslator,
  data : {
    env_key: 'ENV_KEY', // required
    // Metadata
    player_name: 'Custom Player', // ex: 'My Main Player'
    // ... additional metadata
  }
});

```

If you return `false` from your `errorTranslator` function then the error will not be tracked. Do this for non-fatal errors that you want to ignore. If your `errorTranslator` function itself raises an error, then it will be silenced and the player's original error will be used.

### Disable automatic error tracking

In the case that you want full control over what errors are counted as fatal or not, you may want to consider turning off Mux's automatic error tracking completely. This can be done by passing `automaticErrorTracking: false` in the configuration object.

```js
initChromecastMux(playerManager, {
  debug: false,
  automaticErrorTracking: false,
  data : {
    env_key: 'ENV_KEY', // required
    // Metadata
    player_name: 'Custom Player', // ex: 'My Main Player'
    // ... additional metadata
  }
});
```

### Customize beacon collection domain

If you have [integrated a custom domain for Data collection](/docs/guides/integrate-a-data-custom-domain), specify your custom domain by setting `beaconCollectionDomain`.

```js
initChromecastMux(playerManager, {
  debug: false,
  beaconCollectionDomain: 'CUSTOM_DOMAIN', // ex: 'foo.bar.com'
  data: {
    env_key: "ENV_KEY",
    // ...
  }
});
```

## Destroying the Monitor

There are certain use cases where you want to stop monitoring playback within a player (for instance if the player is no longer being used, you are recycling players, or you are shutting down the application). In this case, you should make sure to destroy the monitor. This can be done by simply calling `playerManager.mux.destroy()`.

<LinkedHeader step={steps[7]} />

### Current release

#### v4.16.18

* fix issue where playing time might accumulate for paused players
  * Updated dependency: `mux-embed` to v5.17.1

### Previous releases

#### v4.16.17

* add compatibility for dash.js 5
  * Updated dependency: `mux-embed` to v5.17.0

#### v4.16.16

* Update parsing of initial value for player\_playback\_mode
  * Updated dependency: `mux-embed` to v5.16.1

#### v4.16.15

* Add Playback Range Tracker for new engagement metrics
  * Updated dependency: `mux-embed` to v5.16.0

#### v4.16.14

* Automatically detect playback mode changes for HTML 5 Video
  * Updated dependency: `mux-embed` to v5.15.0

#### v4.16.13

* Emit a renditionchange event at the start of views to eanble updated rendition tracking.
  * Updated dependency: `mux-embed` to v5.14.0

#### v4.16.12

* Add ad type metadata to Ad Events
* Add support for the upcoming Playback Mode changes:
  * Updated dependency: `mux-embed` to v5.13.0

#### v4.16.11

* SDKs will no longer immediately send error events that are flagged as warnings. Fatal errors will still immediately be sent.
  * Updated dependency: `mux-embed` to v5.12.0

#### v4.16.10

* Allow dev to specify page starting load and page finished loading times to calculate Page Load Time
  * Updated dependency: `mux-embed` to v5.11.0

#### v4.16.9

* Adds support for cdnchange events
  * Updated dependency: `mux-embed` to v5.10.0

#### v4.16.8

* Submit Aggregate Startup Time when autoplay is set
  * Updated dependency: `mux-embed` to v5.9.1

#### v4.16.7

* Update `mux-embed` to v5.9.0

#### v4.16.6

* Update `mux-embed` to v5.8.3

#### v4.16.5

* Update `mux-embed` to v5.8.2

#### v4.16.4

* Update `mux-embed` to v5.8.1

#### v4.16.3

* Update `mux-embed` to v5.8.0

#### v4.16.2

* Update `mux-embed` to v5.7.0

#### v4.16.1

* Update `mux-embed` to v5.6.0

#### v4.16.0

* Update mechanism for generating unique IDs, used for `view_id` and others

* Update `mux-embed` to v5.5.0

#### v4.15.3

* \[chore] internal build process fix (no functional changes)
* Update `mux-embed` to v5.4.3

#### v4.15.2

* Update `mux-embed` to v5.4.2

#### v4.15.1

* Update `mux-embed` to v5.4.1

#### v4.15.0

* Add updateData function that allows Mux Data metadata to be updated mid-view.

* Update `mux-embed` to v5.4.0

#### v4.14.6

* Update `mux-embed` to v5.3.3

#### v4.14.5

* Update `mux-embed` to v5.3.2

#### v4.14.4

* Update `mux-embed` to v5.3.1

#### v4.14.3

* Update `mux-embed` to v5.3.0

#### v4.14.2

* Update `mux-embed` to v5.2.1

#### v4.14.1

* Update `mux-embed` to v5.2.0

#### v4.14.0

* Target ES5 for bundles and validate bundles are ES5

* Update `mux-embed` to v5.1.0

#### v4.13.0

* TypeScript type changes only.

* Update `mux-embed` to v5.0.0

#### v4.12.4

* Update `mux-embed` to v4.30.0

#### v4.12.3

* Update `mux-embed` to v4.29.0

#### v4.12.2

* Update `mux-embed` to v4.28.1

#### v4.12.1

* Update `mux-embed` to v4.28.0

#### v4.12.0

* fix an issue where seek latency could be unexpectedly large

* fix an issue where seek latency does not include time at end of a view

* Update `mux-embed` to v4.27.0

#### v4.11.5

* Update `mux-embed` to v4.26.0

#### v4.11.4

* Update `mux-embed` to v4.25.1

#### v4.11.3

* \[advanced-use] Add option to turn off automatic ad tracking for Chromecast applications

#### v4.11.2

* Update `mux-embed` to v4.25.0

#### v4.11.1

* Fix an issue where certain ad providers may result in javascript errors

#### v4.11.0

* Fix an issue where beacons over a certain size could get hung and not be sent

* Update `mux-embed` to v4.24.0

#### v4.10.0

* Fix an issue where tracking rebuffering can get into an infinite loop

* Update `mux-embed` to v4.23.0

#### v4.9.0

* fix an issue where retrieving ad information on chromecast can throw an exception

* Update `mux-embed` to v4.22.0

#### v4.8.0

* Include Ad metadata in ad events

* Update `mux-embed` to v4.21.0

#### v4.7.0

* * Added capturing player dimensions with device pixel ratio considered
  * Added capturing dropped frames

* Update `mux-embed` to v4.20.0

#### v4.6.2

* Update `mux-embed` to v4.19.0

#### v4.6.1

* Update `mux-embed` to v4.18.0

#### v4.6.0

* Support `player_error_context` in `errorTranslator`

* Update `mux-embed` to v4.17.0

#### v4.5.0

* Adds support for new and updated fields: `renditionchange`, error, DRM type, dropped frames, and new custom fields

* Update `mux-embed` to v4.16.0

#### v4.4.0

* Expose `utils` on SDK initialization function to expose `utils.now()` for `player_init_time`

* Update `mux-embed` to v4.15.0

#### v4.3.5

* Update `mux-embed` to v4.14.0

#### v4.3.4

* Update `mux-embed` to v4.13.4

#### v4.3.3

* Update `mux-embed` to v4.13.3

#### v4.3.2

* Update `mux-embed` to v4.13.2

#### v4.3.1

* Fixes an issue with accessing the global object
* Update `mux-embed` to v4.13.1

#### v4.3.0

* Upgraded internal webpack version

* Improve Chromecast rebuffering metrics

* Update `mux-embed` to v4.13.0

#### v4.2.15

* Publish package to NPM

#### v4.2.14

* Update `mux-embed` to v4.12.1

#### v4.2.13

* Update `mux-embed` to v4.12.0

#### v4.2.12

* Update `mux-embed` to v4.11.0

#### v4.2.11

* Listen for Chromecast BITRATE\_CHANGED event, update the video source width and height, then call Mux `renditionchange` with the new bitrate

#### v4.2.10

* Update `mux-embed` to v4.10.0

#### v4.2.9

* Update `mux-embed` to v4.9.4

#### v4.2.8

* Use common function for generating short IDs
* Update `mux-embed` to v4.9.3

#### v4.2.7

* Update `mux-embed` to v4.9.2

#### v4.2.6

* Update `mux-embed` to v4.9.1

#### v4.2.5

* Update `mux-embed` to v4.9.0

#### v4.2.4

* Update `mux-embed` to v4.8.0

#### v4.2.3

* Update `mux-embed` to v4.7.0

#### v4.2.2

* Update `mux-embed` to v4.6.2

#### v4.2.1

* Update `mux-embed` to v4.6.1

#### v4.2.0

* Bump mux-embed to 4.6.0

#### v4.1.1

* Fix an issue where `player.mux.destroy()` would raise an exception if called without any parameters.

#### v4.1.0

* Update `mux-embed` to v4.2.0
* Fix an issue where views that resulted from `programchange` may not have been tracked correctly
* Fix an issue where if `destroy` was called multiple times, it would raise an exception

#### v4.0.0

* Remove automatic video change tracking. You must now emit `videochange` events to signal a change. This should be done inside an interceptor for the `LOAD` event.
* Fix an issue where `ended` events were sent at the wrong time.
* Ensure that tracking is paused on the Chromecast `STOPPED` event.

#### v3.1.0

* Update mux-embed to v4.1.1
* Add support for custom dimensions
* Fix an issue where `player_remote_played` was not functioning. This value defaults to `true` if not set

#### v3.0.0

* Update mux-embed to v4.0.0
* Update device model appropriately for various Chromecast devices
* Support server-side device detection

#### v2.0.1

* Bug fix: Ensure the `video_source_url` is detected

#### v2.0.0

* Support ad event tracking
* Default `videochange` detection to false - this can still be enabled if required
* Clean up error tracking to report only fatal errors
* Minor optimisations and bug fixes

#### v1.0.0

* Support customizing error handling (via configuring automaticErrorTracking and errorTranslator).
* Do not shut down on REQUEST\_STOP.
* Expose `playerManager.mux.destroy()` to stop monitoring the player instance.
* Clean up better and minor bug fix around destroying monitor.

#### v0.1.0

* Initial SDK created.

# Source: https://www.mux.com/docs/guides/monitor-akamai-media-player.md

# Monitor Akamai media player
This guide walks through integration with [Akamai Media Player](https://www.akamai.com/us/en/products/media-delivery/adaptive-media-player.jsp) to collect video performance metrics with Mux data.
## Features

The following data can be collected by the Mux Data SDK when you use the \{featureDef.name} SDK, as described
&#x20;       below.

```md
- Engagement metrics
- Quality of Experience Metrics
- Web metrics such as Player Startup Time, Page Load Time, etc
- Custom Dimensions

```

Notes:

```md
No notes provided
```

## 1. Load \`@mux/mux-data-akamai\` as a plugin

Get your `ENV_KEY` from the [Mux environments dashboard](https://dashboard.mux.com/environments).

<Callout type="info" title="Env Key is different than your API token">
  `ENV_KEY` is a client-side key used for Mux Data monitoring. These are not to be confused with API tokens which are created in the admin settings dashboard and meant to access the Mux API from a trusted server.
</Callout>

<Image src="/docs/images/env-key.png" width={2004} height={250} />

```npm
npm install --save @mux/mux-data-akamai
```

```yarn
yarn add @mux/mux-data-akamai
```

```cdn
<script src="http://src.litix.io/akamai/3/akamai-mux.js"></script>
```



Register the mux plugin with the `akamai` object.

```html

<div id="my-player"></div>
<script>
akamai.amp.AMP.create("#my-player", {
  // ... other player configuration
  plugins: {
    mux: {
      resources: [
        {src: "http://src.litix.io/akamai/3/akamai-mux.js", type: "text/javascript"},
      ],
      debug: false,
      data: {
        env_key: 'ENV_KEY', // required
        // Metadata
        player_name: '', // ex: 'My Main Player'
        // ... and other metadata
      }
    }
  }
});
</script>

```

```javascript

import initAkamaiMux from "@mux/mux-data-akamai";

initAkamaiMux(akamai);

akamai.amp.AMP.create("#my-player", {
  // ... other player configuration
  plugins: {
    mux: {
      debug: false,
      data: {
        env_key: 'ENV_KEY', // required
        // Metadata
        player_name: '', // ex: 'My Main Player'
        // ... and other metadata
      }
    }
  }
});

```



## 2. Make your data actionable

The only required field in the `data` key that you pass into `plugins.mux` is `env_key`. But without some metadata the metrics in your dashboard will lack the necessary information to take meaningful actions. Metadata allows you to search and filter on important fields in order to diagnose issues and optimize the playback experience for your end users.

Pass in metadata under the `data` on initialization.

```js
akamai.amp.AMP.create("#my-player", {
  // ... other player configuration
  plugins: {
    mux: {
      resources: [
        {src: "http://src.litix.io/akamai/3/akamai-mux.js", type: "text/javascript"},
      ],
      debug: false,
      data: {
        env_key: 'ENV_KEY', // required
        // Site Metadata
        viewer_user_id: '', // ex: '12345'
        experiment_name: '', // ex: 'player_test_A'
        sub_property_id: '', // ex: 'cus-1'
        // Player Metadata
        player_name: '', // ex: 'My Main Player'
        player_version: '', // ex: '1.0.0'
        // Video Metadata
        video_id: '', // ex: 'abcd123'
        video_title: '', // ex: 'My Great Video'
        video_series: '', // ex: 'Weekly Great Videos'
        video_duration: '', // in milliseconds, ex: 120000
        video_stream_type: '', // 'live' or 'on-demand'
        video_cdn: '' // ex: 'Fastly', 'Akamai'
      }
    }
  }
});
```

For more information, view [Make your data actionable](/docs/guides/make-your-data-actionable-with-metadata).

## 3. Changing the video

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

```js
// player is the instance returned by the `akamai.amp.AMP.create` function
player.mux.emit('videochange', {
  video_id: 'abc345',
  video_title: 'My Other Great Video',
  video_series: 'Weekly Great Videos',
  // ...
});
```

### New program

In some cases, you may have the program change within a stream, and you may want to track each program as a view on its own. An example of this is a live stream that streams multiple programs back to back, with no interruptions.

In this case, you emit a `programchange` event, including the updated metadata for the new program within the continuous stream. This will remove all previous video data and reset all metrics for the video view, creating a new video view. See [Metadata](/docs/guides/make-your-data-actionable-with-metadata) for the list of video details you can provide. You can include any metadata when changing the video but you should only need to update the values that start with `video`.

Note: The `programchange` event is intended to be used *only* while the player is currently not paused. If you emit this event while the player is paused, the resulting view will not track video startup time correctly, and may also have incorrect watch time. Do not emit this event while the player is paused.

```js
// player is the instance returned by the `akamai.amp.AMP.create` function
player.mux.emit('programchange', {
  video_id: 'abc345',
  video_title: 'My Other Great Video',
  video_series: 'Weekly Great Videos',
  // ...
});
```

## 4. Advanced options

### Disable cookies

By default, Mux plugins for HTML5-based players use a cookie to track playback across subsequent page views in order to understand viewing sessions. This cookie includes information about the tracking of the viewer, such as an anonymized viewer ID that Mux generates for each user. None of this information is personally-identifiable, but you can disable the use of this cookie if desired. For instance, if your site or application is targeted towards children under 13, you should disable the use of cookies. For information about the specific data tracked in the cookie, please refer to: [What information is stored in Mux Data HTML cookies](/docs/guides/ensure-data-privacy-compliance#what-information-is-stored-in-mux-data-html-cookies).

This is done by setting `disableCookies: true` in the options.

```js
akamai.amp.AMP.create("#my-player", {
  // ... other player configuration
  plugins: {
    mux: {
      resources: [
        {src: "http://src.litix.io/akamai/3/akamai-mux.js", type: "text/javascript"},
      ],
      debug: false,
      disableCookies: true,
      data: {
        env_key: 'ENV_KEY', // required
        // Metadata
        player_name: '', // ex: 'My Main Player'
        // ... and other metadata
      }
    }
  }
});
```

### Over-ride 'do not track' behavior

By default, Mux plugins for HTML5-based players do not respect [Do Not Track](https://www.eff.org/issues/do-not-track) when set within browsers. This can be enabled in the options passed to Mux, via a setting named `respectDoNotTrack`. The default for this is `false`. If you would like to change this behavior, pass `respectDoNotTrack: true`.

```js
akamai.amp.AMP.create("#my-player", {
  // ... other player configuration
  plugins: {
    mux: {
      resources: [
        {src: "http://src.litix.io/akamai/3/akamai-mux.js", type: "text/javascript"},
      ],
      debug: false,
      respectDoNotTrack: true,
      data: {
        env_key: 'ENV_KEY', // required
        // Metadata
        player_name: '', // ex: 'My Main Player'
        // ... and other metadata
      }
    }
  }
});
```

### Customize error tracking behavior

<Callout type="error" title="Errors are fatal">
  Errors tracked by mux are considered fatal meaning that they are the result of playback failures. If errors are non-fatal they should not be captured.
</Callout>

By default, `@mux/mux-data-akamai` will track errors emitted from the video element as fatal errors.

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
  };
}

akamai.amp.AMP.create("#my-player", {
  // ... other player configuration
  plugins: {
    mux: {
      resources: [
        {src: "http://src.litix.io/akamai/3/akamai-mux.js", type: "text/javascript"},
      ],
      debug: false,
      respectDoNotTrack: true,
      errorTranslator,
      data: {
        env_key: 'ENV_KEY', // required
        // Metadata
        player_name: '', // ex: 'My Main Player'
        // ... and other metadata
      }
    }
  }
});
```

If you return `false` from your `errorTranslator` function then the error will not be tracked. Do this for non-fatal errors that you want to ignore. If your `errorTranslator` function itself raises an error, then it will be silenced and the player's original error will be used.

### Disable automatic error tracking

In the case that you want full control over what errors are counted as fatal or not, you may want to consider turning off Mux's automatic error tracking completely. This can be done by passing `automaticErrorTracking: false` in the configuration object.

```js
akamai.amp.AMP.create("#my-player", {
  // ... other player configuration
  plugins: {
    mux: {
      resources: [
        {src: "http://src.litix.io/akamai/3/akamai-mux.js", type: "text/javascript"},
      ],
      debug: false,
      respectDoNotTrack: true,
      automaticErrorTracking: false,
      data: {
        env_key: 'ENV_KEY', // required
        // Metadata
        player_name: '', // ex: 'My Main Player'
        // ... and other metadata
      }
    }
  }
});
```

### Ads tracking with `@mux/mux-data-akamai`

Ad events are tracked automatically if your player is configured for ads. No additional configuration is needed.

### Customize beacon collection domain

If you have [integrated a custom domain for Data collection](/docs/guides/integrate-a-data-custom-domain), specify your custom domain by setting `beaconCollectionDomain`.

```js
akamai.amp.AMP.create("#my-player", {
  // ... other player configuration
  plugins: {
    mux: {
      resources: [
        {src: "http://src.litix.io/akamai/3/akamai-mux.js", type: "text/javascript"},
      ],
      // ... various configuration options
      beaconCollectionDomain: 'CUSTOM_DOMAIN', // ex: 'foo.bar.com'
      data: {
        env_key: 'ENV_KEY', // required
        // Metadata
        player_name: '', // ex: 'My Main Player'
        player_init_time: playerInitTime // ex: 1451606400000
        // ... and other metadata
      }
    }
  }
});
```

<LinkedHeader step={steps[5]} />

### Current release

#### v3.11.18

* fix issue where playing time might accumulate for paused players
  * Updated dependency: `mux-embed` to v5.17.1

### Previous releases

#### v3.11.17

* add compatibility for dash.js 5
  * Updated dependency: `mux-embed` to v5.17.0

#### v3.11.16

* Update parsing of initial value for player\_playback\_mode
  * Updated dependency: `mux-embed` to v5.16.1

#### v3.11.15

* Add Playback Range Tracker for new engagement metrics
  * Updated dependency: `mux-embed` to v5.16.0

#### v3.11.14

* Automatically detect playback mode changes for HTML 5 Video
  * Updated dependency: `mux-embed` to v5.15.0

#### v3.11.13

* Emit a renditionchange event at the start of views to eanble updated rendition tracking.
  * Updated dependency: `mux-embed` to v5.14.0

#### v3.11.12

* Add ad type metadata to Ad Events
* Add support for the upcoming Playback Mode changes:
  * Updated dependency: `mux-embed` to v5.13.0

#### v3.11.11

* SDKs will no longer immediately send error events that are flagged as warnings. Fatal errors will still immediately be sent.
  * Updated dependency: `mux-embed` to v5.12.0

#### v3.11.10

* Allow dev to specify page starting load and page finished loading times to calculate Page Load Time
  * Updated dependency: `mux-embed` to v5.11.0

#### v3.11.9

* Adds support for cdnchange events
  * Updated dependency: `mux-embed` to v5.10.0

#### v3.11.8

* Submit Aggregate Startup Time when autoplay is set
  * Updated dependency: `mux-embed` to v5.9.1

#### v3.11.7

* Update `mux-embed` to v5.9.0

#### v3.11.6

* Update `mux-embed` to v5.8.3

#### v3.11.5

* Update `mux-embed` to v5.8.2

#### v3.11.4

* Update `mux-embed` to v5.8.1

#### v3.11.3

* Update `mux-embed` to v5.8.0

#### v3.11.2

* Update `mux-embed` to v5.7.0

#### v3.11.1

* Update `mux-embed` to v5.6.0

#### v3.11.0

* Update mechanism for generating unique IDs, used for `view_id` and others

* Update `mux-embed` to v5.5.0

#### v3.10.10

* \[chore] internal build process fix (no functional changes)
* Update `mux-embed` to v5.4.3

#### v3.10.9

* Update `mux-embed` to v5.4.2

#### v3.10.8

* Update `mux-embed` to v5.4.1

#### v3.10.7

* Update `mux-embed` to v5.4.0

#### v3.10.6

* Update `mux-embed` to v5.3.3

#### v3.10.5

* Update `mux-embed` to v5.3.2

#### v3.10.4

* Update `mux-embed` to v5.3.1

#### v3.10.3

* Update `mux-embed` to v5.3.0

#### v3.10.2

* Update `mux-embed` to v5.2.1

#### v3.10.1

* Update `mux-embed` to v5.2.0

#### v3.10.0

* Target ES5 for bundles and validate bundles are ES5

* Update `mux-embed` to v5.1.0

#### v3.9.0

* Minor refactors to have strict typing and type inferences available.

* Update `mux-embed` to v5.0.0

#### v3.8.4

* Update `mux-embed` to v4.30.0

#### v3.8.3

* Update `mux-embed` to v4.29.0

#### v3.8.2

* Update `mux-embed` to v4.28.1

#### v3.8.1

* Update `mux-embed` to v4.28.0

#### v3.8.0

* fix an issue where seek latency could be unexpectedly large

* fix an issue where seek latency does not include time at end of a view

* Update `mux-embed` to v4.27.0

#### v3.7.3

* Update `mux-embed` to v4.26.0

#### v3.7.2

* Update `mux-embed` to v4.25.1

#### v3.7.1

* Update `mux-embed` to v4.25.0

#### v3.7.0

* Fix an issue where beacons over a certain size could get hung and not be sent

* Update `mux-embed` to v4.24.0

#### v3.6.0

* Fix an issue where tracking rebuffering can get into an infinite loop

* Update `mux-embed` to v4.23.0

#### v3.5.5

* Update `mux-embed` to v4.22.0

#### v3.5.4

* Update `mux-embed` to v4.21.0

#### v3.5.3

* Update `mux-embed` to v4.20.0

#### v3.5.2

* Update `mux-embed` to v4.19.0

#### v3.5.1

* Update `mux-embed` to v4.18.0

#### v3.5.0

* Support `player_error_context` in `errorTranslator`

* Update `mux-embed` to v4.17.0

#### v3.4.0

* Adds support for new and updated fields: `renditionchange`, error, DRM type, dropped frames, and new custom fields

* Update `mux-embed` to v4.16.0

#### v3.3.6

* Update `mux-embed` to v4.15.0

#### v3.3.5

* Update `mux-embed` to v4.14.0

#### v3.3.4

* Update `mux-embed` to v4.13.4

#### v3.3.3

* Update `mux-embed` to v4.13.3

#### v3.3.2

* Update `mux-embed` to v4.13.2

#### v3.3.1

* Fixes an issue with accessing the global object
* Update `mux-embed` to v4.13.1

#### v3.3.0

* Upgraded internal webpack version

* Export a function to register the mux plugin with Akamai

* Update `mux-embed` to v4.13.0

#### v3.2.14

* Publish package to NPM

#### v3.2.13

* Update `mux-embed` to v4.12.1

#### v3.2.12

* Update `mux-embed` to v4.12.0

#### v3.2.11

* Update `mux-embed` to v4.11.0

#### v3.2.10

* Update `mux-embed` to v4.10.0

#### v3.2.9

* Update `mux-embed` to v4.9.4

#### v3.2.8

* Update `mux-embed` to v4.9.3

#### v3.2.7

* Update `mux-embed` to v4.9.2

#### v3.2.6

* Update `mux-embed` to v4.9.1

#### v3.2.5

* Update `mux-embed` to v4.9.0

#### v3.2.4

* Fix an issue with removing `player_error_code` and `player_error_message` when the error code is `1`.
  Also stops emitting `MEDIA_ERR_ABORTED` as errors.
* Update `mux-embed` to v4.8.0

#### v3.2.3

* Update `mux-embed` to v4.7.0

#### v3.2.2

* Update `mux-embed` to v4.6.2

#### v3.2.1

* Update `mux-embed` to v4.6.1

#### v3.2.0

* Bump mux-embed to 4.6.0

#### v3.1.0

* Update `mux-embed` to v4.2.0
* Fix an issue where views that resulted from `programchange` may not have been tracked correctly
* Fix an issue where if `destroy` was called multiple times, it would raise an exception

#### v3.0.0

* Update `mux-embed` to v4.1.1
* Fix an issue where `player_remote_played` would not be reported correctly

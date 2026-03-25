# Source: https://www.mux.com/docs/guides/monitor-nexplayer.md

# Monitor NexPlayer
This guide walks through integration with [NexPlayer](https://nexplayersdk.com/) to collect video performance metrics with Mux Data.
<Callout type="warning">
  # Third-party integration

  This integration is managed and operated by [NexPlayer](https://github.com/NexPlayer/NexPlayer_HTML5_Mux).
  Feedback should be made on the GitHub repo's [Issues](https://github.com/NexPlayer/NexPlayer_HTML5_Mux/issues) page or by contacting NexPlayer support by [email](mailto:supportmadrid@nexplayer.com).
</Callout>

## 1. Install NexPlayer\_HTML5\_Mux

Add the NexPlayer\_HTML5\_Mux plugin to your project by cloning the [GitHub repo](https://github.com/NexPlayer/NexPlayer_HTML5_Mux) or installing using yarn/npm.

```npm

npm install --save https://github.com/NexPlayer/NexPlayer_HTML5_Mux.git

```

```yarn

yarn add https://github.com/NexPlayer/NexPlayer_HTML5_Mux.git

```



## 2. Initialize Mux Data

Get your `ENV_KEY` from the [Mux environments dashboard](https://dashboard.mux.com/environments).

<Callout type="info" title="Env Key is different than your API token">
  `ENV_KEY` is a client-side key used for Mux Data monitoring. These are not to be confused with API tokens which are created in the admin settings dashboard and meant to access the Mux API from a trusted server.
</Callout>

<Image src="/docs/images/env-key.png" width={2004} height={250} />

Add NexPlayer as you normally would to your solution including recommended CSS styling. In addition, you will need to import the Mux SDK and `NexMuxHandShake.js` into the `<head />` and set the `window.muxPlayerInitTime` to the current date/time.

<Callout type="warning">
  # NexPlayer minimum version

  Be sure to use the NexPlayer SDK v5.5.3.1 as it contains necessary functionality to integrate with Mux.
</Callout>

```html
<head>
  <style type="text/css">
    #player_container {
      position: relative;
      padding-top: 28%;
      padding-bottom: 28%;
      left: 28%;
    }

    #player {
      background-color: #191828;
      position: absolute;
      top: 0%;
      width: 50%;
      height: 50%;
    }
  </style>
  <script type="text/javascript" src="https://src.litix.io/core/4/mux.js"></script>
  <script type="text/javascript" src="https://nexplayer.nexplayersdk.com/5.5.3.1/nexplayer.js"></script>
  <script type="text/javascript" src="../node_modules/NexPlayer_HTML5_Mux/app/NexMuxHandShake.js"></script>
  <script type="text/javascript">window.muxPlayerInitTime = Date.now();</script>
</head>
```

Initialize your instance of NexPlayer with a configuration that includes the NexPlayer\_HTML5\_Mux plugin that activates Mux Data. Be sure to replace the `ENV_KEY` and `NEXPLAYER_KEY` with respective values.

```html

<div id="player_container">
  <div id="player" />
</div>

<script type="text/javascript">
  var muxConfiguration = {
    debug: false,
    data: {
      env_key: 'ENV_KEY'

      // Metadata
      player_name: '', // ex: 'My Main Player'
      player_init_time: window.muxPlayerInitTime // ex: 1451606400000

      // ... and other metadata
    },
  };

  var player = null;
  var videoElem = null;
  let nexMux = null;

  var callBackWithPlayers = function (nexplayerInstance, videoElement) {
    player = nexplayerInstance;
    videoElem = videoElement;

    videoElem.addEventListener("loadeddata", function() {
      nexMux = new NexMuxHandShake();
      nexMux.useAdMetrics = true;
      nexMux.initMuxData(muxConfiguration);
    });
  }

  nexplayer.Setup({
    key: 'NEXPLAYER_KEY',
    div: document.getElementById('player'),
    callbacksForPlayer: callBackWithPlayers,
    src: 'https://stream.mux.com/yb2L3z3Z4IKQH02HYkf9xPToVYkOC85WA.m3u8',
  });
</script>

```



## 3. Make your data actionable

The only required field in the options that you pass into the NexPlayer\_HTML5\_Mux plugin is `ENV_KEY`. But without some metadata the metrics in your dashboard will lack the necessary information to take meaningful actions. Metadata allows you to search and filter on important fields in order to diagnose issues and optimize the playback experience for your end users.

Pass in metadata under the `muxConfiguration` on initialization.

```js
var muxConfiguration = {
  debug: false,
  data: {
    env_key: 'ENV_KEY', // required
    // Site Metadata
    viewer_user_id: '', // ex: '12345'
    experiment_name: '', // ex: 'player_test_A'
    sub_property_id: '', // ex: 'cus-1'
    // Player Metadata
    player_name: 'NexPlayer', // ex: 'My Main Player'
    player_version:  '', // ex: '1.0.0'
    player_init_time: window.muxPlayerInitTime, // ex: 1451606400000
    // Video Metadata
    video_id: '', // ex: 'abcd123'
    video_title: '', // ex: 'My Great Video'
    video_series: '', // ex: 'Weekly Great Videos'
    video_duration: '', // in milliseconds, ex: 120000
    video_stream_type: '', // 'live' or 'on-demand'
    video_cdn: '' // ex: 'Fastly', 'Akamai'
  },
};
```

For more information, view [Make your data actionable](/docs/guides/make-your-data-actionable-with-metadata).

## 4. Changing the video

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
// nexMux is the instance returned by the 
// `new NexMuxHandShake()` in the above example
nexMux.videoChange({
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
// nexMux is the instance returned by the 
// `new NexMuxHandShake()` in the above example
nexMux.programChange({
  video_id: 'abc345',
  video_title: 'My Other Great Video',
  video_series: 'Weekly Great Videos',
  // ...
});
```

## 5. Advanced options

### Disable cookies

By default, Mux plugins for HTML5-based players use a cookie to track playback across subsequent page views in order to understand viewing sessions. This cookie includes information about the tracking of the viewer, such as an anonymized viewer ID that Mux generates for each user. None of this information is personally-identifiable, but you can disable the use of this cookie if desired. For instance, if your site or application is targeted towards children under 13, you should disable the use of cookies. For information about the specific data tracked in the cookie, please refer to: [What information is stored in Mux Data HTML cookies](/docs/guides/ensure-data-privacy-compliance#what-information-is-stored-in-mux-data-html-cookies).

This is done by setting `disableCookies: true` in the options.

```js
var muxConfiguration = {
  debug: false,
  disableCookies: true,
  data: {
    env_key: 'ENV_KEY', // required
    ...
  },
};
```

### Over-ride 'do not track' behavior

By default, Mux plugins for HTML5-based players do not respect [Do Not Track](https://www.eff.org/issues/do-not-track) when set within browsers. This can be enabled in the options passed to Mux, via a setting named `respectDoNotTrack`. The default for this is `false`. If you would like to change this behavior, pass `respectDoNotTrack: true`.

```js
var muxConfiguration = {
  debug: false,
  respectDoNotTrack: true,
  data: {
    env_key: 'ENV_KEY', // required
    ...
  },
};
```

### Disable automatic error tracking

In the case that you want full control over what errors are counted as fatal or not, you may want to consider turning off Mux's automatic error tracking completely. This can be done by passing `automaticErrorTracking: false` in the configuration object.

```js
var muxConfiguration = {
  debug: false,
  automaticErrorTracking: false,
  data: {
    env_key: 'ENV_KEY', // required
    ...
  },
};
```

### Customize beacon collection domain

If you have [integrated a custom domain for Data collection](/docs/guides/integrate-a-data-custom-domain), specify your custom domain by setting `beaconCollectionDomain`.

```js
var muxConfiguration = {
  debug: false,
  beaconCollectionDomain: 'CUSTOM_DOMAIN', // ex: 'foo.bar.com'
  data: {
    env_key: 'ENV_KEY', // required
    ...
  },
};
```

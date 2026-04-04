# Source: https://hlsjs.video-dev.org/api-docs/

Title: Hls class

URL Source: https://hlsjs.video-dev.org/api-docs/

Markdown Content:
[Home](https://hlsjs.video-dev.org/api-docs/index.html)>[hls.js](https://hlsjs.video-dev.org/api-docs/hls.js.html)>[Hls](https://hlsjs.video-dev.org/api-docs/hls.js.hls.html)

The `Hls` class is the core of the HLS.js library used to instantiate player instances.

**Signature:**

`export default class Hls implements HlsEventEmitter`
**Implements:**[HlsEventEmitter](https://hlsjs.video-dev.org/api-docs/hls.js.hlseventemitter.html)

[](https://hlsjs.video-dev.org/api-docs/#constructors)Constructors
------------------------------------------------------------------

| Constructor | Modifiers | Description |
| --- | --- | --- |
| [(constructor)(userConfig)](https://hlsjs.video-dev.org/api-docs/hls.js.hls._constructor_.html) |  | Creates an instance of an HLS client that can attach to exactly one `HTMLMediaElement`. |

[](https://hlsjs.video-dev.org/api-docs/#properties)Properties
--------------------------------------------------------------

| Property | Modifiers | Type | Description |
| --- | --- | --- | --- |
| [abrEwmaDefaultEstimate](https://hlsjs.video-dev.org/api-docs/hls.js.hls.abrewmadefaultestimate.html) | `readonly` | number |  |
| [allAudioTracks](https://hlsjs.video-dev.org/api-docs/hls.js.hls.allaudiotracks.html) | `readonly` | [MediaPlaylist](https://hlsjs.video-dev.org/api-docs/hls.js.mediaplaylist.html)[] | Get the complete list of audio tracks across all media groups |
| [allSubtitleTracks](https://hlsjs.video-dev.org/api-docs/hls.js.hls.allsubtitletracks.html) | `readonly` | [MediaPlaylist](https://hlsjs.video-dev.org/api-docs/hls.js.mediaplaylist.html)[] | get the complete list of subtitle tracks across all media groups |
| [audioTrack](https://hlsjs.video-dev.org/api-docs/hls.js.hls.audiotrack.html) |  | number | index of the selected audio track (index in audio track lists) |
| [audioTracks](https://hlsjs.video-dev.org/api-docs/hls.js.hls.audiotracks.html) | `readonly` | [MediaPlaylist](https://hlsjs.video-dev.org/api-docs/hls.js.mediaplaylist.html)[] | Get the list of selectable audio tracks |
| [autoLevelCapping](https://hlsjs.video-dev.org/api-docs/hls.js.hls.autolevelcapping.html) |  | number | Capping/max level value that should be used by automatic level selection algorithm (`ABRController`) |
| [autoLevelEnabled](https://hlsjs.video-dev.org/api-docs/hls.js.hls.autolevelenabled.html) | `readonly` | boolean | True when automatic level selection enabled |
| [bandwidthEstimate](https://hlsjs.video-dev.org/api-docs/hls.js.hls.bandwidthestimate.html) |  | number | Returns the current bandwidth estimate in bits per second, when available. Otherwise, `NaN` is returned. |
| [bufferedToEnd](https://hlsjs.video-dev.org/api-docs/hls.js.hls.bufferedtoend.html) | `readonly` | boolean | returns true when all SourceBuffers are buffered to the end |
| [bufferingEnabled](https://hlsjs.video-dev.org/api-docs/hls.js.hls.bufferingenabled.html) | `readonly` | boolean | Returns state of fragment loading toggled by calling `pauseBuffering()` and `resumeBuffering()`. |
| [capLevelToPlayerSize](https://hlsjs.video-dev.org/api-docs/hls.js.hls.capleveltoplayersize.html) |  | boolean | Whether level capping is enabled. Default value is set via `config.capLevelToPlayerSize`. |
| [config](https://hlsjs.video-dev.org/api-docs/hls.js.hls.config.html) | `readonly` | [HlsConfig](https://hlsjs.video-dev.org/api-docs/hls.js.hlsconfig.html) | The runtime configuration used by the player. At instantiation this is combination of `hls.userConfig` merged over `Hls.DefaultConfig`. |
| [currentLevel](https://hlsjs.video-dev.org/api-docs/hls.js.hls.currentlevel.html) |  | number | Index of quality level (variant) currently played |
| [DefaultConfig](https://hlsjs.video-dev.org/api-docs/hls.js.hls.defaultconfig.html) | `static` | [HlsConfig](https://hlsjs.video-dev.org/api-docs/hls.js.hlsconfig.html) | Get the default configuration applied to new instances. |
| [drift](https://hlsjs.video-dev.org/api-docs/hls.js.hls.drift.html) | `readonly` | number | null | the rate at which the edge of the current live playlist is advancing or 1 if there is none |
| [ErrorDetails](https://hlsjs.video-dev.org/api-docs/hls.js.hls.errordetails.html) | `static` `readonly` | typeof [ErrorDetails](https://hlsjs.video-dev.org/api-docs/hls.js.errordetails.html) |  |
| [ErrorTypes](https://hlsjs.video-dev.org/api-docs/hls.js.hls.errortypes.html) | `static` `readonly` | typeof [ErrorTypes](https://hlsjs.video-dev.org/api-docs/hls.js.errortypes.html) |  |
| [Events](https://hlsjs.video-dev.org/api-docs/hls.js.hls.events.html) | `static` `readonly` | typeof [Events](https://hlsjs.video-dev.org/api-docs/hls.js.events.html) |  |
| [firstAutoLevel](https://hlsjs.video-dev.org/api-docs/hls.js.hls.firstautolevel.html) | `readonly` | number |  |
| [firstLevel](https://hlsjs.video-dev.org/api-docs/hls.js.hls.firstlevel.html) |  | number | Return "first level": like a default level, if not set, falls back to index of first level referenced in manifest |
| [forceStartLoad](https://hlsjs.video-dev.org/api-docs/hls.js.hls.forcestartload.html) | `readonly` | boolean | set to true when startLoad is called before MANIFEST_PARSED event |
| [hasEnoughToStart](https://hlsjs.video-dev.org/api-docs/hls.js.hls.hasenoughtostart.html) | `readonly` | boolean | Whether or not enough has been buffered to seek to start position or use `media.currentTime` to determine next load position |
| [inFlightFragments](https://hlsjs.video-dev.org/api-docs/hls.js.hls.inflightfragments.html) | `readonly` | [InFlightFragments](https://hlsjs.video-dev.org/api-docs/hls.js.inflightfragments.html) |  |
| [interstitialsManager](https://hlsjs.video-dev.org/api-docs/hls.js.hls.interstitialsmanager.html) | `readonly` | [InterstitialsManager](https://hlsjs.video-dev.org/api-docs/hls.js.interstitialsmanager.html) | null | returns Interstitials Program Manager |
| [latency](https://hlsjs.video-dev.org/api-docs/hls.js.hls.latency.html) | `readonly` | number | Estimated position (in seconds) of live edge (ie edge of live playlist plus time sync playlist advanced) |
| [latestLevelDetails](https://hlsjs.video-dev.org/api-docs/hls.js.hls.latestleveldetails.html) | `readonly` | [LevelDetails](https://hlsjs.video-dev.org/api-docs/hls.js.leveldetails.html) | null |  |
| [levels](https://hlsjs.video-dev.org/api-docs/hls.js.hls.levels.html) | `readonly` | [Level](https://hlsjs.video-dev.org/api-docs/hls.js.level.html)[] |  |
| [liveSyncPosition](https://hlsjs.video-dev.org/api-docs/hls.js.hls.livesyncposition.html) | `readonly` | number | null | Position (in seconds) of live sync point (ie edge of live position minus safety delay defined by ```hls.config.liveSyncDuration```) |
| [loadingEnabled](https://hlsjs.video-dev.org/api-docs/hls.js.hls.loadingenabled.html) | `readonly` | boolean | Returns whether loading, toggled with `startLoad()` and `stopLoad()`, is active or not`. |
| [loadLevel](https://hlsjs.video-dev.org/api-docs/hls.js.hls.loadlevel.html) |  | number | Return the quality level of the currently or last (of none is loaded currently) segment |
| [loadLevelObj](https://hlsjs.video-dev.org/api-docs/hls.js.hls.loadlevelobj.html) | `readonly` | [Level](https://hlsjs.video-dev.org/api-docs/hls.js.level.html) | null |  |
| [logger](https://hlsjs.video-dev.org/api-docs/hls.js.hls.logger.html) | `readonly` | [ILogger](https://hlsjs.video-dev.org/api-docs/hls.js.ilogger.html) | The logger functions used by this player instance, configured on player instantiation. |
| [lowLatencyMode](https://hlsjs.video-dev.org/api-docs/hls.js.hls.lowlatencymode.html) |  | boolean | get mode for Low-Latency HLS loading |
| [mainForwardBufferInfo](https://hlsjs.video-dev.org/api-docs/hls.js.hls.mainforwardbufferinfo.html) | `readonly` | [BufferInfo](https://hlsjs.video-dev.org/api-docs/hls.js.bufferinfo.html) | null |  |
| [manualLevel](https://hlsjs.video-dev.org/api-docs/hls.js.hls.manuallevel.html) | `readonly` | number | Level set manually (if any) |
| [maxAutoLevel](https://hlsjs.video-dev.org/api-docs/hls.js.hls.maxautolevel.html) | `readonly` | number | max level selectable in auto mode according to autoLevelCapping |
| [maxBufferLength](https://hlsjs.video-dev.org/api-docs/hls.js.hls.maxbufferlength.html) | `readonly` | number |  |
| [maxHdcpLevel](https://hlsjs.video-dev.org/api-docs/hls.js.hls.maxhdcplevel.html) |  | [HdcpLevel](https://hlsjs.video-dev.org/api-docs/hls.js.hdcplevel.html) |  |
| [maxLatency](https://hlsjs.video-dev.org/api-docs/hls.js.hls.maxlatency.html) | `readonly` | number | maximum distance from the edge before the player seeks forward to ```hls.liveSyncPosition``` configured using ```liveMaxLatencyDurationCount``` (multiple of target duration) or ```liveMaxLatencyDuration``` |
| [media](https://hlsjs.video-dev.org/api-docs/hls.js.hls.media.html) | `readonly` | HTMLMediaElement | null |  |
| [MetadataSchema](https://hlsjs.video-dev.org/api-docs/hls.js.hls.metadataschema.html) | `static` `readonly` | typeof [MetadataSchema](https://hlsjs.video-dev.org/api-docs/hls.js.metadataschema.html) |  |
| [minAutoLevel](https://hlsjs.video-dev.org/api-docs/hls.js.hls.minautolevel.html) | `readonly` | number | min level selectable in auto mode according to config.minAutoBitrate |
| [nextAutoLevel](https://hlsjs.video-dev.org/api-docs/hls.js.hls.nextautolevel.html) |  | number | next automatically selected quality level |
| [nextLevel](https://hlsjs.video-dev.org/api-docs/hls.js.hls.nextlevel.html) |  | number | Index of next quality level loaded as scheduled by stream controller. |
| [nextLoadLevel](https://hlsjs.video-dev.org/api-docs/hls.js.hls.nextloadlevel.html) |  | number | get next quality level loaded |
| [pathwayPriority](https://hlsjs.video-dev.org/api-docs/hls.js.hls.pathwaypriority.html) |  | string[] | null | ContentSteering pathwayPriority getter/setter |
| [pathways](https://hlsjs.video-dev.org/api-docs/hls.js.hls.pathways.html) | `readonly` | string[] | ContentSteering pathways getter |
| [playingDate](https://hlsjs.video-dev.org/api-docs/hls.js.hls.playingdate.html) | `readonly` | Date | null | get the datetime value relative to media.currentTime for the active level Program Date Time if present |
| [sessionId](https://hlsjs.video-dev.org/api-docs/hls.js.hls.sessionid.html) | `readonly` | string |  |
| [startLevel](https://hlsjs.video-dev.org/api-docs/hls.js.hls.startlevel.html) |  | number | Return the desired start level for the first fragment that will be loaded. The default value of -1 indicates automatic start level selection. Setting hls.nextAutoLevel without setting a startLevel will result in the nextAutoLevel value being used for one fragment load. |
| [startPosition](https://hlsjs.video-dev.org/api-docs/hls.js.hls.startposition.html) | `readonly` | number | Get the startPosition set on startLoad(position) or on autostart with config.startPosition |
| [subtitleDisplay](https://hlsjs.video-dev.org/api-docs/hls.js.hls.subtitledisplay.html) |  | boolean | Whether subtitle display is enabled or not |
| [subtitleTrack](https://hlsjs.video-dev.org/api-docs/hls.js.hls.subtitletrack.html) |  | number | index of the selected subtitle track (index in subtitle track lists) |
| [subtitleTracks](https://hlsjs.video-dev.org/api-docs/hls.js.hls.subtitletracks.html) | `readonly` | [MediaPlaylist](https://hlsjs.video-dev.org/api-docs/hls.js.mediaplaylist.html)[] | get alternate subtitle tracks list from playlist |
| [targetLatency](https://hlsjs.video-dev.org/api-docs/hls.js.hls.targetlatency.html) |  | number | null | target distance from the edge as calculated by the latency controller |
| [ttfbEstimate](https://hlsjs.video-dev.org/api-docs/hls.js.hls.ttfbestimate.html) | `readonly` | number | get time to first byte estimate {number} |
| [url](https://hlsjs.video-dev.org/api-docs/hls.js.hls.url.html) | `readonly` | string | null | Gets the currently loaded URL |
| [userConfig](https://hlsjs.video-dev.org/api-docs/hls.js.hls.userconfig.html) | `readonly` | Partial<[HlsConfig](https://hlsjs.video-dev.org/api-docs/hls.js.hlsconfig.html)> | The configuration object provided on player instantiation. |
| [version](https://hlsjs.video-dev.org/api-docs/hls.js.hls.version.html) | `static` `readonly` | string | Get the video-dev/hls.js package version. |

[](https://hlsjs.video-dev.org/api-docs/#methods)Methods
--------------------------------------------------------

| Method | Modifiers | Description |
| --- | --- | --- |
| [attachMedia(data)](https://hlsjs.video-dev.org/api-docs/hls.js.hls.attachmedia.html) |  | Attaches Hls.js to a media element |
| [createController(ControllerClass, components)](https://hlsjs.video-dev.org/api-docs/hls.js.hls.createcontroller.html) |  |  |
| [destroy()](https://hlsjs.video-dev.org/api-docs/hls.js.hls.destroy.html) |  | Dispose of the instance |
| [detachMedia()](https://hlsjs.video-dev.org/api-docs/hls.js.hls.detachmedia.html) |  | Detach Hls.js from the media |
| [emit(event, name, eventObject)](https://hlsjs.video-dev.org/api-docs/hls.js.hls.emit.html) |  |  |
| [getMediaDecodingInfo(level, audioTracks)](https://hlsjs.video-dev.org/api-docs/hls.js.hls.getmediadecodinginfo.html) |  | returns mediaCapabilities.decodingInfo for a variant/rendition |
| [getMediaSource()](https://hlsjs.video-dev.org/api-docs/hls.js.hls.getmediasource.html) | `static` | Get the MediaSource global used for MSE playback (ManagedMediaSource, MediaSource, or WebKitMediaSource). |
| [isMSESupported()](https://hlsjs.video-dev.org/api-docs/hls.js.hls.ismsesupported.html) | `static` | Check if the required MediaSource Extensions are available. |
| [isSupported()](https://hlsjs.video-dev.org/api-docs/hls.js.hls.issupported.html) | `static` | Check if MediaSource Extensions are available and isTypeSupported checks pass for any baseline codecs. |
| [listenerCount(event)](https://hlsjs.video-dev.org/api-docs/hls.js.hls.listenercount.html) |  |  |
| [listeners(event)](https://hlsjs.video-dev.org/api-docs/hls.js.hls.listeners.html) |  |  |
| [loadSource(url)](https://hlsjs.video-dev.org/api-docs/hls.js.hls.loadsource.html) |  | Set the source URL. Can be relative or absolute. |
| [off(event, listener, context, once)](https://hlsjs.video-dev.org/api-docs/hls.js.hls.off.html) |  |  |
| [on(event, listener, context)](https://hlsjs.video-dev.org/api-docs/hls.js.hls.on.html) |  |  |
| [once(event, listener, context)](https://hlsjs.video-dev.org/api-docs/hls.js.hls.once.html) |  |  |
| [pauseBuffering()](https://hlsjs.video-dev.org/api-docs/hls.js.hls.pausebuffering.html) |  | Prevents stream controller from loading new segments until `resumeBuffering` is called. This allows for media buffering to be paused without interupting playlist loading. |
| [recoverMediaError()](https://hlsjs.video-dev.org/api-docs/hls.js.hls.recovermediaerror.html) |  | When the media-element fails, this allows to detach and then re-attach it as one call (convenience method). Automatic recovery of media-errors by this process is configurable. |
| [removeAllListeners(event)](https://hlsjs.video-dev.org/api-docs/hls.js.hls.removealllisteners.html) |  |  |
| [removeLevel(levelIndex)](https://hlsjs.video-dev.org/api-docs/hls.js.hls.removelevel.html) |  |  |
| [resumeBuffering()](https://hlsjs.video-dev.org/api-docs/hls.js.hls.resumebuffering.html) |  | Resumes stream controller segment loading after `pauseBuffering` has been called. |
| [setAudioOption(audioOption)](https://hlsjs.video-dev.org/api-docs/hls.js.hls.setaudiooption.html) |  | Find and select the best matching audio track, making a level switch when a Group change is necessary. Updates `hls.config.audioPreference`. Returns the selected track, or null when no matching track is found. |
| [setSubtitleOption(subtitleOption)](https://hlsjs.video-dev.org/api-docs/hls.js.hls.setsubtitleoption.html) |  | Find and select the best matching subtitle track, making a level switch when a Group change is necessary. Updates `hls.config.subtitlePreference`. Returns the selected track, or null when no matching track is found. |
| [startLoad(startPosition, skipSeekToStartPosition)](https://hlsjs.video-dev.org/api-docs/hls.js.hls.startload.html) |  | Start loading data from the stream source. Depending on default config, client starts loading automatically when a source is set. |
| [stopLoad()](https://hlsjs.video-dev.org/api-docs/hls.js.hls.stopload.html) |  | Stop loading of any stream data. |
| [swapAudioCodec()](https://hlsjs.video-dev.org/api-docs/hls.js.hls.swapaudiocodec.html) |  | Swap through possible audio codecs in the stream (for example to switch from stereo to 5.1) |
| [transferMedia()](https://hlsjs.video-dev.org/api-docs/hls.js.hls.transfermedia.html) |  | Detach HTMLMediaElement, MediaSource, and SourceBuffers without reset, for attaching to another instance |
| [trigger(event, eventObject)](https://hlsjs.video-dev.org/api-docs/hls.js.hls.trigger.html) |  |  |

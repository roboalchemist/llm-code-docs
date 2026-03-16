# Source: https://html.spec.whatwg.org/multipage/media.html

Title: HTML Standard

URL Source: https://html.spec.whatwg.org/multipage/media.html

Markdown Content:
HTML

Living Standard — Last Updated 16 March 2026

← 4.8.5 The iframe element — Table of Contents — 4.8.12 The map element →
4.8.8 The video element
4.8.9 The audio element
4.8.10 The track element
4.8.11 Media elements
4.8.11.1 Error codes
4.8.11.2 Location of the media resource
4.8.11.3 MIME types
4.8.11.4 Network states
4.8.11.5 Loading the media resource
4.8.11.6 Offsets into the media resource
4.8.11.7 Ready states
4.8.11.8 Playing the media resource
4.8.11.9 Seeking
4.8.11.10 Media resources with multiple media tracks
4.8.11.10.1 AudioTrackList and VideoTrackList objects
4.8.11.10.2 Selecting specific audio and video tracks declaratively
4.8.11.11 Timed text tracks
4.8.11.11.1 Text track model
4.8.11.11.2 Sourcing in-band text tracks
4.8.11.11.3 Sourcing out-of-band text tracks
4.8.11.11.4 Guidelines for exposing cues in various formats as text track cues
4.8.11.11.5 Text track API
4.8.11.11.6 Event handlers for objects of the text track APIs
4.8.11.11.7 Best practices for metadata text tracks
4.8.11.12 Identifying a track kind through a URL
4.8.11.13 User interface
4.8.11.14 Time ranges
4.8.11.15 The TrackEvent interface
4.8.11.16 Events summary
4.8.11.17 Security and privacy considerations
4.8.11.18 Best practices for authors using media elements
4.8.11.19 Best practices for implementers of media elements
4.8.8 The video element
✔MDN
✔MDN
Categories:
Flow content.
Phrasing content.
Embedded content.
If the element has a controls attribute: Interactive content.
Palpable content.
Contexts in which this element can be used:
Where embedded content is expected.
Content model:
If the element has a src attribute: zero or more track elements, then transparent, but with no media element descendants.
If the element does not have a src attribute: zero or more source elements, then zero or more track elements, then transparent, but with no media element descendants.
Tag omission in text/html:
Neither tag is omissible.
Content attributes:
Global attributes
src — Address of the resource
crossorigin — How the element handles crossorigin requests
poster — Poster frame to show prior to video playback
preload — Hints how much buffering the media resource will likely need
autoplay — Hint that the media resource can be started automatically when the page is loaded
playsinline — Encourage the user agent to display video content within the element's playback area
loop — Whether to loop the media resource
muted — Whether to mute the media resource by default
controls — Show user agent controls
width — Horizontal dimension
height — Vertical dimension
Accessibility considerations:
For authors.
For implementers.
DOM interface:
[Exposed=Window]
interface HTMLVideoElement : HTMLMediaElement {
  [HTMLConstructor] constructor();

  [CEReactions, Reflect] attribute unsigned long width;
  [CEReactions, Reflect] attribute unsigned long height;
  readonly attribute unsigned long videoWidth;
  readonly attribute unsigned long videoHeight;
  [CEReactions, ReflectURL] attribute USVString poster;
  [CEReactions, Reflect] attribute boolean playsInline;
};

A video element is used for playing videos or movies, and audio files with captions.

Content may be provided inside the video element. User agents should not show this content to the user; it is intended for older web browsers which do not support video, so that text can be shown to the users of these older browsers informing them of how to access the video contents.

In particular, this content is not intended to address accessibility concerns. To make video content accessible to the partially sighted, the blind, the hard-of-hearing, the deaf, and those with other physical or cognitive disabilities, a variety of features are available. Captions can be provided, either embedded in the video stream or as external files using the track element. Sign-language tracks can be embedded in the video stream. Audio descriptions can be embedded in the video stream or in text form using a WebVTT file referenced using the track element and synthesized into speech by the user agent. WebVTT can also be used to provide chapter titles. For users who would rather not use a media element at all, transcripts or other textual alternatives can be provided by simply linking to them in the prose near the video element. [WEBVTT]

The video element is a media element whose media data is ostensibly video data, possibly with associated audio data.

The src, crossorigin, preload, autoplay, loop, muted, and controls attributes are the attributes common to all media elements.

The poster attribute gives the URL of an image file that the user agent can show while no video data is available. The attribute, if present, must contain a valid non-empty URL potentially surrounded by spaces.

If the specified resource is to be used, then, when the element is created or when the poster attribute is set, changed, or removed, the user agent must run the following steps to determine the element's poster frame (regardless of the value of the element's show poster flag):

If there is an existing instance of this algorithm running for this video element, abort that instance of this algorithm without changing the poster frame.

If the poster attribute's value is the empty string or if the attribute is absent, then there is no poster frame; return.

Let url be the result of encoding-parsing a URL given the poster attribute's value, relative to the element's node document.

If url is failure, then return. There is no poster frame.

Let request be a new request whose URL is url, client is the element's node document's relevant settings object, destination is "image", initiator type is "video", credentials mode is "include", and whose use-URL-credentials flag is set.

Fetch request. This must delay the load event of the element's node document.

If an image is thus obtained, the poster frame is that image. Otherwise, there is no poster frame.

The image given by the poster attribute, the poster frame, is intended to be a representative frame of the video (typically one of the first non-blank frames) that gives the user an idea of what the video is like.

The playsinline attribute is a boolean attribute. If present, it serves as a hint to the user agent that the video ought to be displayed "inline" in the document by default, constrained to the element's playback area, instead of being displayed fullscreen or in an independent resizable window.

The absence of the playsinline attribute does not imply that the video will display fullscreen by default. Indeed, most user agents have chosen to play all videos inline by default, and in such user agents the playsinline attribute has no effect.

A video element represents what is given for the first matching condition in the list below:

When no video data is available (the element's readyState attribute is either HAVE_NOTHING, or HAVE_METADATA but no video data has yet been obtained at all, or the element's readyState attribute is any subsequent value but the media resource does not have a video channel)
The video element represents its poster frame, if any, or else transparent black with no natural dimensions.
When the video element is paused, the current playback position is the first frame of video, and the element's show poster flag is set
The video element represents its poster frame, if any, or else the first frame of the video.
When the video element is paused, and the frame of video corresponding to the current playback position is not available (e.g. because the video is seeking or buffering)
When the video element is neither potentially playing nor paused (e.g. when seeking or stalled)
The video element represents the last frame of the video to have been rendered.
When the video element is paused
The video element represents the frame of video corresponding to the current playback position.
Otherwise (the video element has a video channel and is potentially playing)
The video element represents the frame of video at the continuously increasing "current" position. When the current playback position changes such that the last frame rendered is no longer the frame corresponding to the current playback position in the video, the new frame must be rendered.

Frames of video must be obtained from the video track that was selected when the event loop last reached step 1.

Which frame in a video stream corresponds to a particular playback position is defined by the video stream's format.

The video element also represents any text track cues whose text track cue active flag is set and whose text track is in the showing mode, and any audio from the media resource, at the current playback position.

Any audio associated with the media resource must, if played, be played synchronized with the current playback position, at the element's effective media volume. The user agent must play the audio from audio tracks that were enabled when the event loop last reached step 1.

In addition to the above, the user agent may provide messages to the user (such as "buffering", "no video loaded", "error", or more detailed information) by overlaying text or icons on the video or other areas of the element's playback area, or in another appropriate manner.

User agents that cannot render the video may instead make the element represent a link to an external video playback utility or to the video data itself.

When a video element's media resource has a video channel, the element provides a paint source whose width is the media resource's natural width, whose height is the media resource's natural height, and whose appearance is the frame of video corresponding to the current playback position, if that is available, or else (e.g. when the video is seeking or buffering) its previous appearance, if any, or else (e.g. because the video is still loading the first frame) blackness.

video.videoWidth
✔MDN
video.videoHeight
✔MDN

These attributes return the natural dimensions of the video, or 0 if the dimensions are not known.

The natural width and natural height of the media resource are the dimensions of the resource in CSS pixels after taking into account the resource's dimensions, aspect ratio, clean aperture, resolution, and so forth, as defined for the format used by the resource. If an anamorphic format does not define how to apply the aspect ratio to the video data's dimensions to obtain the "correct" dimensions, then the user agent must apply the ratio by increasing one dimension and leaving the other unchanged.

The videoWidth IDL attribute must return the natural width of the video in CSS pixels. The videoHeight IDL attribute must return the natural height of the video in CSS pixels. If the element's readyState attribute is HAVE_NOTHING, then the attributes must return 0.

Whenever the natural width or natural height of the video changes (including, for example, because the selected video track was changed), if the element's readyState attribute is not HAVE_NOTHING, the user agent must queue a media element task given the media element to fire an event named resize at the media element.

The video element supports dimension attributes.

In the absence of style rules to the contrary, video content should be rendered inside the element's playback area such that the video content is shown centered in the playback area at the largest possible size that fits completely within it, with the video content's aspect ratio being preserved. Thus, if the aspect ratio of the playback area does not match the aspect ratio of the video, the video will be shown letterboxed or pillarboxed. Areas of the element's playback area that do not contain the video represent nothing.

In user agents that implement CSS, the above requirement can be implemented by using the style rule suggested in the Rendering section.

The natural width of a video element's playback area is the natural width of the poster frame, if that is available and the element currently represents its poster frame; otherwise, it is the natural width of the video resource, if that is available; otherwise the natural width is missing.

The natural height of a video element's playback area is the natural height of the poster frame, if that is available and the element currently represents its poster frame; otherwise it is the natural height of the video resource, if that is available; otherwise the natural height is missing.

The default object size is a width of 300 CSS pixels and a height of 150 CSS pixels. [CSSIMAGES]

User agents should provide controls to enable or disable the display of closed captions, audio description tracks, and other additional data associated with the video stream, though such features should, again, not interfere with the page's normal rendering.

User agents may allow users to view the video content in manners more suitable to the user, such as fullscreen or in an independent resizable window. User agents may even trigger such a viewing mode by default upon playing a video, although they should not do so when the playsinline attribute is specified. As with the other user interface features, controls to enable this should not interfere with the page's normal rendering unless the user agent is exposing a user interface. In such an independent viewing mode, however, user agents may make full user interfaces visible, even if the controls attribute is absent.

User agents may allow video playback to affect system features that could interfere with the user's experience; for example, user agents could disable screensavers while video playback is in progress.

This example shows how to detect when a video has failed to play correctly:

<script>
 function failed(e) {
   // video playback failed - show a message saying why
   switch (e.target.error.code) {
     case e.target.error.MEDIA_ERR_ABORTED:
       alert('You aborted the video playback.');
       break;
     case e.target.error.MEDIA_ERR_NETWORK:
       alert('A network error caused the video download to fail part-way.');
       break;
     case e.target.error.MEDIA_ERR_DECODE:
       alert('The video playback was aborted due to a corruption problem or because the video used features your browser did not support.');
       break;
     case e.target.error.MEDIA_ERR_SRC_NOT_SUPPORTED:
       alert('The video could not be loaded, either because the server or network failed or because the format is not supported.');
       break;
     default:
       alert('An unknown error occurred.');
       break;
   }
 }
</script>
<p><video src="tgif.vid" autoplay controls onerror="failed(event)"></video></p>
<p><a href="tgif.vid">Download the video file</a>.</p>
4.8.9 The audio element
✔MDN
✔MDN
Categories:
Flow content.
Phrasing content.
Embedded content.
If the element has a controls attribute: Interactive content.
If the element has a controls attribute: Palpable content.
Contexts in which this element can be used:
Where embedded content is expected.
Content model:
If the element has a src attribute: zero or more track elements, then transparent, but with no media element descendants.
If the element does not have a src attribute: zero or more source elements, then zero or more track elements, then transparent, but with no media element descendants.
Tag omission in text/html:
Neither tag is omissible.
Content attributes:
Global attributes
src — Address of the resource
crossorigin — How the element handles crossorigin requests
preload — Hints how much buffering the media resource will likely need
autoplay — Hint that the media resource can be started automatically when the page is loaded
loop — Whether to loop the media resource
muted — Whether to mute the media resource by default
controls — Show user agent controls
Accessibility considerations:
For authors.
For implementers.
DOM interface:
[Exposed=Window,
 LegacyFactoryFunction=Audio(optional DOMString src)]
interface HTMLAudioElement : HTMLMediaElement {
  [HTMLConstructor] constructor();
};

An audio element represents a sound or audio stream.

Content may be provided inside the audio element. User agents should not show this content to the user; it is intended for older web browsers which do not support audio, so that text can be shown to the users of these older browsers informing them of how to access the audio contents.

In particular, this content is not intended to address accessibility concerns. To make audio content accessible to the deaf or to those with other physical or cognitive disabilities, a variety of features are available. If captions or a sign language video are available, the video element can be used instead of the audio element to play the audio, allowing users to enable the visual alternatives. Chapter titles can be provided to aid navigation, using the track element and a WebVTT file. And, naturally, transcripts or other textual alternatives can be provided by simply linking to them in the prose near the audio element. [WEBVTT]

The audio element is a media element whose media data is ostensibly audio data.

The src, crossorigin, preload, autoplay, loop, muted, and controls attributes are the attributes common to all media elements.

audio = new Audio([ url ])
✔MDN

Returns a new audio element, with the src attribute set to the value passed in the argument, if applicable.

A legacy factory function is provided for creating HTMLAudioElement objects (in addition to the factory methods from DOM such as createElement()): Audio(src). When invoked, the legacy factory function must perform the following steps:

Let document be the current global object's associated Document.

Let audio be the result of creating an element given document, "audio", and the HTML namespace.

Set an attribute value for audio using "preload" and "auto".

If src is given, then set an attribute value for audio using "src" and src. (This will cause the user agent to invoke the object's resource selection algorithm before returning.)

Return audio.

4.8.10 The track element
✔MDN
✔MDN
Categories:
None.
Contexts in which this element can be used:
As a child of a media element, before any flow content.
Content model:
Nothing.
Tag omission in text/html:
No end tag.
Content attributes:
Global attributes
kind — The type of text track
src — Address of the resource
srclang — Language of the text track
label — User-visible label
default — Enable the track if no other text track is more suitable
Accessibility considerations:
For authors.
For implementers.
DOM interface:
[Exposed=Window]
interface HTMLTrackElement : HTMLElement {
  [HTMLConstructor] constructor();

  [CEReactions] attribute DOMString kind;
  [CEReactions, ReflectURL] attribute USVString src;
  [CEReactions, Reflect] attribute DOMString srclang;
  [CEReactions, Reflect] attribute DOMString label;
  [CEReactions, Reflect] attribute boolean default;

  const unsigned short NONE = 0;
  const unsigned short LOADING = 1;
  const unsigned short LOADED = 2;
  const unsigned short ERROR = 3;
  readonly attribute unsigned short readyState;

  readonly attribute TextTrack track;
};

The track element allows authors to specify explicit external timed text tracks for media elements. It does not represent anything on its own.

The kind attribute is an enumerated attribute with the following keywords and states:

Keyword	State	Brief description
subtitles	Subtitles	Transcription or translation of the dialogue, suitable for when the sound is available but not understood (e.g. because the user does not understand the language of the media resource's audio track). Overlaid on the video.
captions	Captions	Transcription or translation of the dialogue, sound effects, relevant musical cues, and other relevant audio information, suitable for when sound is unavailable or not clearly audible (e.g. because it is muted, drowned-out by ambient noise, or because the user is deaf). Overlaid on the video; labeled as appropriate for the hard-of-hearing.
descriptions	Descriptions	Textual descriptions of the video component of the media resource, intended for audio synthesis when the visual component is obscured, unavailable, or not usable (e.g. because the user is interacting with the application without a screen while driving, or because the user is blind). Synthesized as audio.
chapters	Chapters metadata	Tracks intended for use from script. Not displayed by the user agent.
metadata	Metadata

The attribute's missing value default is the subtitles state, and its invalid value default is the metadata state.

The src attribute gives the URL of the text track data. The value must be a valid non-empty URL potentially surrounded by spaces. This attribute must be present.

The element has an associated track URL (a string), initially the empty string.

When the element's src attribute is set, run these steps:

Let trackURL be failure.

Let value be the element's src attribute value.

If value is not the empty string, then set trackURL to the result of encoding-parsing-and-serializing a URL given value, relative to the element's node document.

Set the element's track URL to trackURL if it is not failure; otherwise to the empty string.

If the element's track URL identifies a WebVTT resource, and the element's kind attribute is not in the chapters metadata or metadata state, then the WebVTT file must be a WebVTT file using cue text. [WEBVTT]

The srclang attribute gives the language of the text track data. The value must be a valid BCP 47 language tag. This attribute must be present if the element's kind attribute is in the subtitles state. [BCP47]

If the element has a srclang attribute whose value is not the empty string, then the element's track language is the value of the attribute. Otherwise, the element has no track language.

The label attribute gives a user-readable title for the track. This title is used by user agents when listing subtitle, caption, and audio description tracks in their user interface.

The value of the label attribute, if the attribute is present, must not be the empty string. Furthermore, there must not be two track element children of the same media element whose kind attributes are in the same state, whose srclang attributes are both missing or have values that represent the same language, and whose label attributes are again both missing or both have the same value.

If the element has a label attribute whose value is not the empty string, then the element's track label is the value of the attribute. Otherwise, the element's track label is an empty string.

The default attribute is a boolean attribute, which, if specified, indicates that the track is to be enabled if the user's preferences do not indicate that another track would be more appropriate.

Each media element must have no more than one track element child whose kind attribute is in the subtitles or captions state and whose default attribute is specified.

Each media element must have no more than one track element child whose kind attribute is in the description state and whose default attribute is specified.

Each media element must have no more than one track element child whose kind attribute is in the chapters metadata state and whose default attribute is specified.

There is no limit on the number of track elements whose kind attribute is in the metadata state and whose default attribute is specified.

track.readyState

Returns the text track readiness state, represented by a number from the following list:

track.NONE (0)

The text track not loaded state.

track.LOADING (1)

The text track loading state.

track.LOADED (2)

The text track loaded state.

track.ERROR (3)

The text track failed to load state.

track.track

Returns the TextTrack object corresponding to the text track of the track element.

The readyState attribute must return the numeric value corresponding to the text track readiness state of the track element's text track, as defined by the following list:

NONE (numeric value 0)
The text track not loaded state.
LOADING (numeric value 1)
The text track loading state.
LOADED (numeric value 2)
The text track loaded state.
ERROR (numeric value 3)
The text track failed to load state.

The track IDL attribute must, on getting, return the track element's text track's corresponding TextTrack object.

The kind IDL attribute must reflect the content attribute of the same name, limited to only known values.

This video has subtitles in several languages:

<video src="brave.webm">
 <track kind=subtitles src=brave.en.vtt srclang=en label="English">
 <track kind=captions src=brave.en.hoh.vtt srclang=en label="English for the Hard of Hearing">
 <track kind=subtitles src=brave.fr.vtt srclang=fr lang=fr label="Français">
 <track kind=subtitles src=brave.de.vtt srclang=de lang=de label="Deutsch">
</video>

(The lang attributes on the last two describe the language of the label attribute, not the language of the subtitles themselves. The language of the subtitles is given by the srclang attribute.)

4.8.11 Media elements

HTMLMediaElement objects (audio and video, in this specification) are simply known as media elements.

✔MDN
enum CanPlayTypeResult { "" /* empty string */, "maybe", "probably" };
typedef (MediaStream or MediaSource or Blob) MediaProvider;

[Exposed=Window]
interface HTMLMediaElement : HTMLElement {

  // error state
  readonly attribute MediaError? error;

  // network state
  [CEReactions, ReflectURL] attribute USVString src;
  attribute MediaProvider? srcObject;
  readonly attribute USVString currentSrc;
  [CEReactions] attribute DOMString? crossOrigin;
  const unsigned short NETWORK_EMPTY = 0;
  const unsigned short NETWORK_IDLE = 1;
  const unsigned short NETWORK_LOADING = 2;
  const unsigned short NETWORK_NO_SOURCE = 3;
  readonly attribute unsigned short networkState;
  [CEReactions] attribute DOMString preload;
  readonly attribute TimeRanges buffered;
  undefined load();
  CanPlayTypeResult canPlayType(DOMString type);

  // ready state
  const unsigned short HAVE_NOTHING = 0;
  const unsigned short HAVE_METADATA = 1;
  const unsigned short HAVE_CURRENT_DATA = 2;
  const unsigned short HAVE_FUTURE_DATA = 3;
  const unsigned short HAVE_ENOUGH_DATA = 4;
  readonly attribute unsigned short readyState;
  readonly attribute boolean seeking;

  // playback state
  attribute double currentTime;
  undefined fastSeek(double time);
  readonly attribute unrestricted double duration;
  object getStartDate();
  readonly attribute boolean paused;
  attribute double defaultPlaybackRate;
  attribute double playbackRate;
  attribute boolean preservesPitch;
  readonly attribute TimeRanges played;
  readonly attribute TimeRanges seekable;
  readonly attribute boolean ended;
  [CEReactions, Reflect] attribute boolean autoplay;
  [CEReactions, Reflect] attribute boolean loop;
  Promise<undefined> play();
  undefined pause();

  // controls
  [CEReactions, Reflect] attribute boolean controls;
  attribute double volume;
  attribute boolean muted;
  [CEReactions, Reflect="muted"] attribute boolean defaultMuted;

  // tracks
  [SameObject] readonly attribute AudioTrackList audioTracks;
  [SameObject] readonly attribute VideoTrackList videoTracks;
  [SameObject] readonly attribute TextTrackList textTracks;
  TextTrack addTextTrack(TextTrackKind kind, optional DOMString label = "", optional DOMString language = "");
};

The media element attributes, src, crossorigin, preload, autoplay, loop, muted, and controls, apply to all media elements. They are defined in this section.

Media elements are used to present audio data, or video and audio data, to the user. This is referred to as media data in this section, since this section applies equally to media elements for audio or for video. The term media resource is used to refer to the complete set of media data, e.g. the complete video file, or complete audio file.

A media resource has an associated origin, which is either "none", "multiple", "rewritten", or an origin. It is initially set to "none".

A media resource can have multiple audio and video tracks. For the purposes of a media element, the video data of the media resource is only that of the currently selected track (if any) as given by the element's videoTracks attribute when the event loop last reached step 1, and the audio data of the media resource is the result of mixing all the currently enabled tracks (if any) given by the element's audioTracks attribute when the event loop last reached step 1.

Both audio and video elements can be used for both audio and video. The main difference between the two is simply that the audio element has no playback area for visual content (such as video or captions), whereas the video element does.

Each media element has a unique media element event task source.

To queue a media element task with a media element element and a series of steps steps, queue an element task on the media element's media element event task source given element and steps.

4.8.11.1 Error codes
✔MDN
media.error
✔MDN

Returns a MediaError object representing the current error state of the element.

Returns null if there is no error.

All media elements have an associated error status, which records the last error the element encountered since its resource selection algorithm was last invoked. The error attribute, on getting, must return the MediaError object created for this last error, or null if there has not been an error.

[Exposed=Window]
interface MediaError {
  const unsigned short MEDIA_ERR_ABORTED = 1;
  const unsigned short MEDIA_ERR_NETWORK = 2;
  const unsigned short MEDIA_ERR_DECODE = 3;
  const unsigned short MEDIA_ERR_SRC_NOT_SUPPORTED = 4;

  readonly attribute unsigned short code;
  readonly attribute DOMString message;
};
media.error.code
✔MDN

Returns the current error's error code, from the list below.

media.error.message
✔MDN

Returns a specific informative diagnostic message about the error condition encountered. The message and message format are not generally uniform across different user agents. If no such message is available, then the empty string is returned.

Every MediaError object has a message, which is a string, and a code, which is one of the following:

MEDIA_ERR_ABORTED (numeric value 1)
The fetching process for the media resource was aborted by the user agent at the user's request.
MEDIA_ERR_NETWORK (numeric value 2)
A network error of some description caused the user agent to stop fetching the media resource, after the resource was established to be usable.
MEDIA_ERR_DECODE (numeric value 3)
An error of some description occurred while decoding the media resource, after the resource was established to be usable.
MEDIA_ERR_SRC_NOT_SUPPORTED (numeric value 4)
The media resource indicated by the src attribute or assigned media provider object was not suitable.

To create a MediaError, given an error code which is one of the above values, return a new MediaError object whose code is the given error code and whose message is a string containing any details the user agent is able to supply about the cause of the error condition, or the empty string if the user agent is unable to supply such details. This message string must not contain only the information already available via the supplied error code; for example, it must not simply be a translation of the code into a string format. If no additional information is available beyond that provided by the error code, the message must be set to the empty string.

The code getter steps are to return this's code.

The message getter steps are to return this's message.

4.8.11.2 Location of the media resource

The src content attribute on media elements gives the URL of the media resource (video, audio) to show. The attribute, if present, must contain a valid non-empty URL potentially surrounded by spaces.

If the itemprop attribute is specified on the media element, then the src attribute must also be specified.

The crossorigin content attribute on media elements is a CORS settings attribute.

If a media element is created with a src attribute, the user agent must immediately invoke the media element's resource selection algorithm.

If a src attribute of a media element is set or changed, the user agent must invoke the media element's media element load algorithm. (Removing the src attribute does not do this, even if there are source elements present.)

✔MDN

The crossOrigin IDL attribute must reflect the crossorigin content attribute, limited to only known values.

A media provider object is an object that can represent a media resource, separate from a URL. MediaStream objects, MediaSource objects, and Blob objects are all media provider objects.

Each media element can have an assigned media provider object, which is a media provider object. When a media element is created, it has no assigned media provider object.

media.srcObject [ = source ]
⚠MDN

Allows the media element to be assigned a media provider object.

media.currentSrc
✔MDN

Returns the URL of the current media resource, if any.

Returns the empty string when there is no media resource, or it doesn't have a URL.

The currentSrc IDL attribute must initially be set to the empty string. Its value is changed by the resource selection algorithm defined below.

The srcObject IDL attribute, on getting, must return the element's assigned media provider object, if any, or null otherwise. On setting, it must set the element's assigned media provider object to the new value, and then invoke the element's media element load algorithm.

There are three ways to specify a media resource: the srcObject IDL attribute, the src content attribute, and source elements. The IDL attribute takes priority, followed by the content attribute, followed by the elements.

4.8.11.3 MIME types

A media resource can be described in terms of its type, specifically a MIME type, in some cases with a codecs parameter. (Whether the codecs parameter is allowed or not depends on the MIME type.) [RFC6381]

Types are usually somewhat incomplete descriptions; for example "video/mpeg" doesn't say anything except what the container type is, and even a type like "video/mp4; codecs="avc1.42E01E, mp4a.40.2"" doesn't include information like the actual bitrate (only the maximum bitrate). Thus, given a type, a user agent can often only know whether it might be able to play media of that type (with varying levels of confidence), or whether it definitely cannot play media of that type.

A type that the user agent knows it cannot render is one that describes a resource that the user agent definitely does not support, for example because it doesn't recognize the container type, or it doesn't support the listed codecs.

The MIME type "application/octet-stream" with no parameters is never a type that the user agent knows it cannot render. User agents must treat that type as equivalent to the lack of any explicit Content-Type metadata when it is used to label a potential media resource.

Only the MIME type "application/octet-stream" with no parameters is special-cased here; if any parameter appears with it, it will be treated just like any other MIME type. This is a deviation from the rule that unknown MIME type parameters should be ignored.

media.canPlayType(type)
✔MDN

Returns the empty string (a negative response), "maybe", or "probably" based on how confident the user agent is that it can play media resources of the given type.

The canPlayType(type) method must return the empty string if type is a type that the user agent knows it cannot render or is the type "application/octet-stream"; it must return "probably" if the user agent is confident that the type represents a media resource that it can render if used with this audio or video element; and it must return "maybe" otherwise. Implementers are encouraged to return "maybe" unless the type can be confidently established as being supported or not. Generally, a user agent should never return "probably" for a type that allows the codecs parameter if that parameter is not present.

This script tests to see if the user agent supports a (fictional) new format to dynamically decide whether to use a video element:

<section id="video">
 <p><a href="playing-cats.nfv">Download video</a></p>
</section>
<script>
 const videoSection = document.getElementById('video');
 const videoElement = document.createElement('video');
 const support = videoElement.canPlayType('video/x-new-fictional-format;codecs="kittens,bunnies"');
 if (support === "probably") {
   videoElement.setAttribute("src", "playing-cats.nfv");
   videoSection.replaceChildren(videoElement);
 }
</script>

The type attribute of the source element allows the user agent to avoid downloading resources that use formats it cannot render.

4.8.11.4 Network states
media.networkState
✔MDN

Returns the current state of network activity for the element, from the codes in the list below.

As media elements interact with the network, their current network activity is represented by the networkState attribute. On getting, it must return the current network state of the element, which must be one of the following values:

NETWORK_EMPTY (numeric value 0)
The element has not yet been initialized. All attributes are in their initial states.
NETWORK_IDLE (numeric value 1)
The element's resource selection algorithm is active and has selected a resource, but it is not actually using the network at this time.
NETWORK_LOADING (numeric value 2)
The user agent is actively trying to download data.
NETWORK_NO_SOURCE (numeric value 3)
The element's resource selection algorithm is active, but it has not yet found a resource to use.

The resource selection algorithm defined below describes exactly when the networkState attribute changes value and what events fire to indicate changes in this state.

4.8.11.5 Loading the media resource
media.load()
✔MDN

Causes the element to reset and start selecting and loading a new media resource from scratch.

All media elements have a can autoplay flag, which must begin in the true state, and a delaying-the-load-event flag, which must begin in the false state. While the delaying-the-load-event flag is true, the element must delay the load event of its document.

When the load() method on a media element is invoked, the user agent must run the media element load algorithm.

A media element has an associated boolean is currently stalled, which is initially false.

The media element load algorithm consists of the following steps.

Set this element's is currently stalled to false.

Abort any already-running instance of the resource selection algorithm for this element.

Let pending tasks be a list of all tasks from the media element's media element event task source in one of the task queues.

For each task in pending tasks that would resolve pending play promises or reject pending play promises, immediately resolve or reject those promises in the order the corresponding tasks were queued.

Remove each task in pending tasks from its task queue.

Basically, pending events and callbacks are discarded and promises in-flight to be resolved/rejected are resolved/rejected immediately when the media element starts loading a new resource.

If the media element's networkState is set to NETWORK_LOADING or NETWORK_IDLE, queue a media element task given the media element to fire an event named abort at the media element.

If the media element's networkState is not set to NETWORK_EMPTY, then:

Queue a media element task given the media element to fire an event named emptied at the media element.

If a fetching process is in progress for the media element, the user agent should stop it.

If the media element's assigned media provider object is a MediaSource object, then detach it.

Forget the media element's media-resource-specific tracks.

If readyState is not set to HAVE_NOTHING, then set it to that state.

If the paused attribute is false, then:

Set the paused attribute to true.

Take pending play promises and reject pending play promises with the result and an "AbortError" DOMException.

If seeking is true, set it to false.

Set the current playback position to 0.

Set the official playback position to 0.

If this changed the official playback position, then queue a media element task given the media element to fire an event named timeupdate at the media element.

Set the timeline offset to Not-a-Number (NaN).

Update the duration attribute to Not-a-Number (NaN).

The user agent will not fire a durationchange event for this particular change of the duration.

Set the playbackRate attribute to the value of the defaultPlaybackRate attribute.

Set the error attribute to null and the can autoplay flag to true.

Invoke the media element's resource selection algorithm.

Playback of any previously playing media resource for this element stops.

The resource selection algorithm for a media element is as follows. This algorithm is always invoked as part of a task, but one of the first steps in the algorithm is to return and continue running the remaining steps in parallel. In addition, this algorithm interacts closely with the event loop mechanism; in particular, it has synchronous sections (which are triggered as part of the event loop algorithm). Steps in such sections are marked with ⌛.

Set the element's networkState attribute to the NETWORK_NO_SOURCE value.

Set the element's show poster flag to true.

Set the media element's delaying-the-load-event flag to true (this delays the load event).

Await a stable state, allowing the task that invoked this algorithm to continue. The synchronous section consists of all the remaining steps of this algorithm until the algorithm says the synchronous section has ended. (Steps in synchronous sections are marked with ⌛.)

⌛ If the media element's blocked-on-parser flag is false, then populate the list of pending text tracks.

⌛ If the media element has an assigned media provider object, then let mode be object.

⌛ Otherwise, if the media element has no assigned media provider object but has a src attribute, then let mode be attribute.

⌛ Otherwise, if the media element does not have an assigned media provider object and does not have a src attribute, but does have a source element child, then let mode be children and let candidate be the first such source element child in tree order.

⌛ Otherwise, the media element has no assigned media provider object and has neither a src attribute nor a source element child:

⌛ Set the networkState to NETWORK_EMPTY.

⌛ Set the element's delaying-the-load-event flag to false. This stops delaying the load event.

End the synchronous section and return.

⌛ Set the media element's networkState to NETWORK_LOADING.

⌛ Queue a media element task given the media element to fire an event named loadstart at the media element.

Run the appropriate steps from the following list:

If mode is object

⌛ Set the currentSrc attribute to the empty string.

End the synchronous section, continuing the remaining steps in parallel.

Run the resource fetch algorithm with the assigned media provider object. If that algorithm returns without aborting this one, then the load failed.

Failed with media provider: Reaching this step indicates that the media resource failed to load. Take pending play promises and queue a media element task given the media element to run the dedicated media source failure steps with the result.

Wait for the task queued by the previous step to have executed.

Return. The element won't attempt to load another resource until this algorithm is triggered again.

If mode is attribute

⌛ If the src attribute's value is the empty string, then end the synchronous section, and jump down to the failed with attribute step below.

⌛ Let urlRecord be the result of encoding-parsing a URL given the src attribute's value, relative to the media element's node document when the src attribute was last changed.

⌛ If urlRecord is not failure, then set the currentSrc attribute to the result of applying the URL serializer to urlRecord.

End the synchronous section, continuing the remaining steps in parallel.

If urlRecord is not failure, then run the resource fetch algorithm with urlRecord. If that algorithm returns without aborting this one, then the load failed.

Failed with attribute: Reaching this step indicates that the media resource failed to load or that urlRecord is failure. Take pending play promises and queue a media element task given the media element to run the dedicated media source failure steps with the result.

Wait for the task queued by the previous step to have executed.

Return. The element won't attempt to load another resource until this algorithm is triggered again.

Otherwise (mode is children)

⌛ Let pointer be a position defined by two adjacent nodes in the media element's child list, treating the start of the list (before the first child in the list, if any) and end of the list (after the last child in the list, if any) as nodes in their own right. One node is the node before pointer, and the other node is the node after pointer. Initially, let pointer be the position between the candidate node and the next node, if there are any, or the end of the list, if it is the last node.

As nodes are inserted, removed, and moved into the media element, pointer must be updated as follows:

If a new node is inserted or moved between the two nodes that define pointer
Let pointer be the point between the node before pointer and the new node. In other words, insertions at pointer go after pointer.
If the node before pointer is removed
Let pointer be the point between the node after pointer and the node before the node after pointer. In other words, pointer doesn't move relative to the remaining nodes.
If the node after pointer is removed
Let pointer be the point between the node before pointer and the node after the node before pointer. Just as with the previous case, pointer doesn't move relative to the remaining nodes.

Other changes don't affect pointer.

⌛ Process candidate: If candidate does not have a src attribute, or if its src attribute's value is the empty string, then end the synchronous section, and jump down to the failed with elements step below.

⌛ If candidate has a media attribute whose value does not match the environment, then end the synchronous section, and jump down to the failed with elements step below.

⌛ Let urlRecord be the result of encoding-parsing a URL given candidate's src attribute's value, relative to candidate's node document when the src attribute was last changed.

⌛ If urlRecord is failure, then end the synchronous section, and jump down to the failed with elements step below.

⌛ If candidate has a type attribute whose value, when parsed as a MIME type (including any codecs described by the codecs parameter, for types that define that parameter), represents a type that the user agent knows it cannot render, then end the synchronous section, and jump down to the failed with elements step below.

⌛ Set the currentSrc attribute to the result of applying the URL serializer to urlRecord.

End the synchronous section, continuing the remaining steps in parallel.

Run the resource fetch algorithm with urlRecord. If that algorithm returns without aborting this one, then the load failed.

Failed with elements: Queue a media element task given the media element to fire an event named error at candidate.

Await a stable state. The synchronous section consists of all the remaining steps of this algorithm until the algorithm says the synchronous section has ended. (Steps in synchronous sections are marked with ⌛.)

⌛ Forget the media element's media-resource-specific tracks.

⌛ Find next candidate: Let candidate be null.

⌛ Search loop: If the node after pointer is the end of the list, then jump to the waiting step below.

⌛ If the node after pointer is a source element, let candidate be that element.

⌛ Advance pointer so that the node before pointer is now the node that was after pointer, and the node after pointer is the node after the node that used to be after pointer, if any.

⌛ If candidate is null, jump back to the search loop step. Otherwise, jump back to the process candidate step.

⌛ Waiting: Set the element's networkState attribute to the NETWORK_NO_SOURCE value.

⌛ Set the element's show poster flag to true.

⌛ Queue a media element task given the media element to set the element's delaying-the-load-event flag to false. This stops delaying the load event.

End the synchronous section, continuing the remaining steps in parallel.

Wait until the node after pointer is a node other than the end of the list. (This step might wait forever.)

Await a stable state. The synchronous section consists of all the remaining steps of this algorithm until the algorithm says the synchronous section has ended. (Steps in synchronous sections are marked with ⌛.)

⌛ Set the element's delaying-the-load-event flag back to true (this delays the load event again, in case it hasn't been fired yet).

⌛ Set the networkState back to NETWORK_LOADING.

⌛ Jump back to the find next candidate step above.

The dedicated media source failure steps with a list of promises promises are the following steps:

Set the error attribute to the result of creating a MediaError with MEDIA_ERR_SRC_NOT_SUPPORTED.

Forget the media element's media-resource-specific tracks.

Set the element's networkState attribute to the NETWORK_NO_SOURCE value.

Set the element's show poster flag to true.

Fire an event named error at the media element.

Reject pending play promises with promises and a "NotSupportedError" DOMException.

Set the element's delaying-the-load-event flag to false. This stops delaying the load event.

To verify a media response given a response response, a media resource resource, and "entire resource" or a (number, number or "until end") tuple byteRange:

If response is a network error, then return false.

If byteRange is "entire resource", then return true.

Let internalResponse be response's unsafe response.

If internalResponse's status is 200, then return true.

If internalResponse's status is not 206, then return false.

If the result of extracting content-range values from internalResponse is failure, then return false.

Note that the extracted values are not used, and in particular are not compared to byteRange. So this step serves as syntactic validation of the `Content-Range` header, but if the `Content-Range` values on the response mismatch the `Range` values on the request, that is not considered a failure.

Let origin be "rewritten" if internalResponse's URL is null; otherwise internalResponse's URL's origin.

Let previousOrigin be resource's origin.

If any of the following are true:

previousOrigin is "none";

origin and previousOrigin are "rewritten"; or

origin and previousOrigin are origins, and origin is same origin with previousOrigin,

then set resource's origin to origin.

Otherwise, if response is CORS-cross-origin, then return false.

Otherwise, set resource's origin to "multiple".

This ensures that opaque responses with range headers do not leak information by being patched together with other responses from different origins.

Return true.

The resource fetch algorithm for a media element and a given URL record or media provider object is as follows:

Let mode be remote.

If the algorithm was invoked with media provider object, then set mode to local.

Otherwise:

Let isTopLevelSelfFetch be false.

Let settingsObject be the media element's node document's relevant settings object.

Let global be the media element's node document's relevant global object.

If all of the following conditions are true:

global is a Window object;

global's navigable is not null;

global's navigable's parent is null; and

settingsObject's creation URL equals the URL record,

then set isTopLevelSelfFetch to true.

Let stringOrEnvironment be "top-level-self-fetch" if isTopLevelSelfFetch is true; otherwise settingsObject.

Let object be the result of obtaining a blob object using the URL record's blob URL entry and stringOrEnvironment.

If object is a media provider object, then set mode to local.

If mode is remote, then let the current media resource be the resource given by the URL record passed to this algorithm; otherwise, let the current media resource be the resource given by the media provider object. Either way, the current media resource is now the element's media resource.

Remove all media-resource-specific text tracks from the media element's list of pending text tracks, if any.

Run the appropriate steps from the following list:

If mode is remote

Optionally, run the following substeps. This is the expected behavior if the user agent intends to not attempt to fetch the resource until the user requests it explicitly (e.g. as a way to implement the preload attribute's none keyword).

Set the networkState to NETWORK_IDLE.

Queue a media element task given the media element to fire an event named suspend at the element.

Queue a media element task given the media element to set the element's delaying-the-load-event flag to false. This stops delaying the load event.

Wait for the task to be run.

Wait for an implementation-defined event (e.g., the user requesting that the media element begin playback).

Set the element's delaying-the-load-event flag back to true (this delays the load event again, in case it hasn't been fired yet).

Set the networkState to NETWORK_LOADING.

Let destination be "audio" if the media element is an audio element, or "video" otherwise.

Let request be the result of creating a potential-CORS request given current media resource's URL record, destination, and the current state of the media element's crossorigin content attribute.

Set request's client to the media element's node document's relevant settings object.

Set request's initiator type to destination.

Let byteRange, which is "entire resource" or a (number, number or "until end") tuple, be the byte range required to satisfy missing data in media data. This value is implementation-defined and may rely on codec, network conditions or other heuristics. The user-agent may determine to fetch the resource in full, in which case byteRange would be "entire resource", to fetch from a byte offset until the end, in which case byteRange would be (number, "until end"), or to fetch a range between two byte offsets, in which case byteRange would be a (number, number) tuple representing the two offsets.

If byteRange is not "entire resource", then:

If byteRange[1] is "until end", then add a range header to request given byteRange[0].

Otherwise, add a range header to request given byteRange[0] and byteRange[1].

Fetch request, with processResponse set to the following steps given response response:

Let global be the media element's node document's relevant global object.

Let updateMedia be to queue a media element task given the media element to run the first appropriate steps from the media data processing steps list below. (A new task is used for this so that the work described below occurs relative to the appropriate media element event task source rather than using the networking task source.)

Let processEndOfMedia be the following step: If the fetching process has completed without errors, including decoding the media data, and if all of the data is available to the user agent without network access, then, the user agent must move on to the final step below. This might never happen, e.g. when streaming an infinite resource such as web radio, or if the resource is longer than the user agent's ability to cache data.

If the result of verifying response given the current media resource and byteRange is false, then abort these steps.

Otherwise, incrementally read response's body given updateMedia, processEndOfMedia, an empty algorithm, and global.

Update the media data with the contents of response's unsafe response obtained in this fashion. response can be CORS-same-origin or CORS-cross-origin; this affects whether subtitles referenced in the media data are exposed in the API and, for video elements, whether a canvas gets tainted when the video is drawn on it.

The media element stall timeout is an implementation-defined length of time, which should be about three seconds. When a media element that is actively attempting to obtain media data has failed to receive any data for a duration equal to the media element stall timeout, the user agent must queue a media element task given the media element to:

Set the element's is currently stalled to true.

Fire an event named stalled at the element.

User agents may allow users to selectively block or slow media data downloads. When a media element's download has been blocked altogether, the user agent must act as if it was stalled (as opposed to acting as if the connection was closed). The rate of the download may also be throttled automatically by the user agent, e.g. to balance the download with other connections sharing the same bandwidth.

User agents may decide to not download more content at any time, e.g. after buffering five minutes of a one hour media resource, while waiting for the user to decide whether to play the resource or not, while waiting for user input in an interactive resource, or when the user navigates away from the page. When a media element's download has been suspended, the user agent must queue a media element task given the media element to set the networkState to NETWORK_IDLE and fire an event named suspend at the element. If and when downloading of the resource resumes, the user agent must queue a media element task given the media element to set the networkState to NETWORK_LOADING. Between the queuing of these tasks, the load is suspended (so progress events don't fire, as described above).

The preload attribute provides a hint regarding how much buffering the author thinks is advisable, even in the absence of the autoplay attribute.

When a user agent decides to completely suspend a download, e.g., if it is waiting until the user starts playback before downloading any further content, the user agent must queue a media element task given the media element to set the element's delaying-the-load-event flag to false. This stops delaying the load event.

Although the above steps give an algorithm for issuing requests, the user agent may use other means besides those exact ones, especially in the face of error conditions. For example, the user agent may reconnect to the server or switch to a streaming protocol. The user agent must only consider the resource erroneous, and proceed into the error branches of the above steps, if the user agent has given up trying to fetch the resource.

To determine the format of the media resource, the user agent must use the rules for sniffing audio and video specifically.

While the load is not suspended (see below), every 350ms (±200ms) or for every byte received, whichever is least frequent, queue a media element task given the media element to:

Set the element's is currently stalled to false.

Fire an event named progress at the element.

While the user agent might still need network access to obtain parts of the media resource, the user agent must remain on this step.

For example, if the user agent has discarded the first half of a video, the user agent will remain at this step even once the playback has ended, because there is always the chance the user will seek back to the start. In fact, in this situation, once playback has ended, the user agent will end up firing a suspend event, as described earlier.

Otherwise (mode is local)

The resource described by the current media resource, if any, contains the media data. It is CORS-same-origin.

If the current media resource is a raw data stream (e.g. from a File object), then to determine the format of the media resource, the user agent must use the rules for sniffing audio and video specifically. Otherwise, if the data stream is pre-decoded, then the format is the format given by the relevant specification.

Whenever new data for the current media resource becomes available, queue a media element task given the media element to run the first appropriate steps from the media data processing steps list below.

When the current media resource is permanently exhausted (e.g. all the bytes of a Blob have been processed), if there were no decoding errors, then the user agent must move on to the final step below. This might never happen, e.g. if the current media resource is a MediaStream.

The media data processing steps list is as follows:

If the media data cannot be fetched at all, due to network errors, causing the user agent to give up trying to fetch the resource
If the media data can be fetched but is found by inspection to be in an unsupported format, or can otherwise not be rendered at all

DNS errors, HTTP 4xx and 5xx errors (and equivalents in other protocols), and other fatal network errors that occur before the user agent has established whether the current media resource is usable, as well as the file using an unsupported container format, or using unsupported codecs for all the data, must cause the user agent to execute the following steps:

The user agent should cancel the fetching process.

Abort this subalgorithm, returning to the resource selection algorithm.

If the media resource is found to have an audio track

Create an AudioTrack object to represent the audio track.

Update the media element's audioTracks attribute's AudioTrackList object with the new AudioTrack object.

Let enable be unknown.

If either the media resource or the URL of the current media resource indicate a particular set of audio tracks to enable, or if the user agent has information that would facilitate the selection of specific audio tracks to improve the user's experience, then: if this audio track is one of the ones to enable, then set enable to true, otherwise, set enable to false.

This could be triggered by media fragment syntax, but it could also be triggered e.g. by the user agent selecting a 5.1 surround sound audio track over a stereo audio track.

If enable is still unknown, then, if the media element does not yet have an enabled audio track, then set enable to true, otherwise, set enable to false.

If enable is true, then enable this audio track, otherwise, do not enable this audio track.

Fire an event named addtrack at this AudioTrackList object, using TrackEvent, with the track attribute initialized to the new AudioTrack object.

If the media resource is found to have a video track

Create a VideoTrack object to represent the video track.

Update the media element's videoTracks attribute's VideoTrackList object with the new VideoTrack object.

Let enable be unknown.

If either the media resource or the URL of the current media resource indicate a particular set of video tracks to enable, or if the user agent has information that would facilitate the selection of specific video tracks to improve the user's experience, then: if this video track is the first such video track, then set enable to true, otherwise, set enable to false.

This could again be triggered by media fragment syntax.

If enable is still unknown, then, if the media element does not yet have a selected video track, then set enable to true, otherwise, set enable to false.

If enable is true, then select this track and unselect any previously selected video tracks, otherwise, do not select this video track. If other tracks are unselected, then a change event will be fired.

Fire an event named addtrack at this VideoTrackList object, using TrackEvent, with the track attribute initialized to the new VideoTrack object.

Once enough of the media data has been fetched to determine the duration of the media resource, its dimensions, and other metadata

This indicates that the resource is usable. The user agent must follow these substeps:

Establish the media timeline for the purposes of the current playback position and the earliest possible position, based on the media data.

Update the timeline offset to the date and time that corresponds to the zero time in the media timeline established in the previous step, if any. If no explicit time and date is given by the media resource, the timeline offset must be set to Not-a-Number (NaN).

Set the current playback position and the official playback position to the earliest possible position.

Update the duration attribute with the time of the last frame of the resource, if known, on the media timeline established above. If it is not known (e.g. a stream that is in principle infinite), update the duration attribute to the value positive Infinity.

The user agent will queue a media element task given the media element to fire an event named durationchange at the element at this point.

For video elements, set the videoWidth and videoHeight attributes, and queue a media element task given the media element to fire an event named resize at the media element.

Further resize events will be fired if the dimensions subsequently change.

Set the readyState attribute to HAVE_METADATA.

A loadedmetadata DOM event will be fired as part of setting the readyState attribute to a new value.

Let jumped be false.

If the media element's default playback start position is greater than zero, then seek to that time, and let jumped be true.

Set the media element's default playback start position to zero.

Let the initial playback position be 0.

If either the media resource or the URL of the current media resource indicate a particular start time, then set the initial playback position to that time and, if jumped is still false, seek to that time.

For example, with media formats that support media fragment syntax, the fragment can be used to indicate a start position.

If there is no enabled audio track, then enable an audio track. This will cause a change event to be fired.

If there is no selected video track, then select a video track. This will cause a change event to be fired.

Once the readyState attribute reaches HAVE_CURRENT_DATA, after the loadeddata event has been fired, set the element's delaying-the-load-event flag to false. This stops delaying the load event.

A user agent that is attempting to reduce network usage while still fetching the metadata for each media resource would also stop buffering at this point, following the rules described previously, which involve the networkState attribute switching to the NETWORK_IDLE value and a suspend event firing.

The user agent is required to determine the duration of the media resource and go through this step before playing.

Once the entire media resource has been fetched (but potentially before any of it has been decoded)

Fire an event named progress at the media element.

Set the networkState to NETWORK_IDLE and fire an event named suspend at the media element.

If the user agent ever discards any media data and then needs to resume the network activity to obtain it again, then it must queue a media element task given the media element to set the networkState to NETWORK_LOADING.

If the user agent can keep the media resource loaded, then the algorithm will continue to its final step below, which aborts the algorithm.

If the connection is interrupted after some media data has been received, causing the user agent to give up trying to fetch the resource

Fatal network errors that occur after the user agent has established whether the current media resource is usable (i.e. once the media element's readyState attribute is no longer HAVE_NOTHING) must cause the user agent to execute the following steps:

The user agent should cancel the fetching process.

Set the error attribute to the result of creating a MediaError with MEDIA_ERR_NETWORK.

Set the element's networkState attribute to the NETWORK_IDLE value.

Set the element's delaying-the-load-event flag to false. This stops delaying the load event.

Fire an event named error at the media element.

Abort the overall resource selection algorithm.

If the media data is corrupted

Fatal errors in decoding the media data that occur after the user agent has established whether the current media resource is usable (i.e. once the media element's readyState attribute is no longer HAVE_NOTHING) must cause the user agent to execute the following steps:

The user agent should cancel the fetching process.

Set the error attribute to the result of creating a MediaError with MEDIA_ERR_DECODE.

Set the element's networkState attribute to the NETWORK_IDLE value.

Set the element's delaying-the-load-event flag to false. This stops delaying the load event.

Fire an event named error at the media element.

Abort the overall resource selection algorithm.

If the media data fetching process is aborted by the user

The fetching process is aborted by the user, e.g. because the user pressed a "stop" button, the user agent must execute the following steps. These steps are not followed if the load() method itself is invoked while these steps are running, as the steps above handle that particular kind of abort.

The user agent should cancel the fetching process.

Set the error attribute to the result of creating a MediaError with MEDIA_ERR_ABORTED.

Fire an event named abort at the media element.

If the media element's readyState attribute has a value equal to HAVE_NOTHING, set the element's networkState attribute to the NETWORK_EMPTY value, set the element's show poster flag to true, and fire an event named emptied at the element.

Otherwise, set the element's networkState attribute to the NETWORK_IDLE value.

Set the element's delaying-the-load-event flag to false. This stops delaying the load event.

Abort the overall resource selection algorithm.

If the media data can be fetched but has non-fatal errors or uses, in part, codecs that are unsupported, preventing the user agent from rendering the content completely correctly but not preventing playback altogether

The server returning data that is partially usable but cannot be optimally rendered must cause the user agent to render just the bits it can handle, and ignore the rest.

If the media resource is found to declare a media-resource-specific text track that the user agent supports

If the media data is CORS-same-origin, run the steps to expose a media-resource-specific text track with the relevant data.

Cross-origin videos do not expose their subtitles, since that would allow attacks such as hostile sites reading subtitles from confidential videos on a user's intranet.

Final step: If the user agent ever reaches this step (which can only happen if the entire resource gets loaded and kept available): abort the overall resource selection algorithm.

When a media element is to forget the media element's media-resource-specific tracks, the user agent must remove from the media element's list of text tracks all the media-resource-specific text tracks, then empty the media element's audioTracks attribute's AudioTrackList object, then empty the media element's videoTracks attribute's VideoTrackList object. No events (in particular, no removetrack events) are fired as part of this; the error and emptied events, fired by the algorithms that invoke this one, can be used instead.

The preload attribute is an enumerated attribute with the following keywords and states:

Keyword	State	Brief description
auto	Automatic	Hints to the user agent that the user agent can put the user's needs first without risk to the server, up to and including optimistically downloading the entire resource.
none	None	Hints to the user agent that either the author does not expect the user to need the media resource, or that the server wants to minimize unnecessary traffic. This state does not provide a hint regarding how aggressively to actually download the media resource if buffering starts anyway (e.g. once the user hits "play").
metadata	Metadata	Hints to the user agent that the author does not expect the user to need the media resource, but that fetching the resource metadata (dimensions, track list, duration, etc.), and maybe even the first few frames, is reasonable. If the user agent precisely fetches no more than the metadata, then the media element will end up with its readyState attribute set to HAVE_METADATA; typically though, some frames will be obtained as well and it will probably be HAVE_CURRENT_DATA or HAVE_FUTURE_DATA. When the media resource is playing, hints to the user agent that bandwidth is to be considered scarce, e.g. suggesting throttling the download so that the media data is obtained at the slowest possible rate that still maintains consistent playback.

The attribute's empty value default is the Automatic state.

The attribute's missing value default and invalid value default are both implementation-defined, though the Metadata state is suggested as a compromise between reducing server load and providing an optimal user experience.

The attribute can be changed even once the media resource is being buffered or played; the descriptions in the table above are to be interpreted with that in mind.

Authors might switch the attribute from "none" or "metadata" to "auto" dynamically once the user begins playback. For example, on a page with many videos this might be used to indicate that the many videos are not to be downloaded unless requested, but that once one is requested it is to be downloaded aggressively.

The preload attribute is intended to provide a hint to the user agent about what the author thinks will lead to the best user experience. The attribute may be ignored altogether, for example based on explicit user preferences or based on the available connectivity.

The preload IDL attribute must reflect the content attribute of the same name, limited to only known values.

The autoplay attribute can override the preload attribute (since if the media plays, it naturally has to buffer first, regardless of the hint given by the preload attribute). Including both is not an error, however.

media.buffered
✔MDN

Returns a TimeRanges object that represents the ranges of the media resource that the user agent has buffered.

The buffered attribute must return a new static normalized TimeRanges object that represents the ranges of the media resource, if any, that the user agent has buffered, at the time the attribute is evaluated. User agents must accurately determine the ranges available, even for media streams where this can only be determined by tedious inspection.

Typically this will be a single range anchored at the zero point, but if, e.g. the user agent uses HTTP range requests in response to seeking, then there could be multiple ranges.

User agents may discard previously buffered data.

Thus, a time position included within a range of the objects return by the buffered attribute at one time can end up being not included in the range(s) of objects returned by the same attribute at later times.

Returning a new object each time is a bad pattern for attribute getters and is only enshrined here as it would be costly to change it. It is not to be copied to new APIs.

4.8.11.6 Offsets into the media resource
media.duration
✔MDN

Returns the length of the media resource, in seconds, assuming that the start of the media resource is at time zero.

Returns NaN if the duration isn't available.

Returns Infinity for unbounded streams.

media.currentTime [ = value ]
✔MDN

Returns the official playback position, in seconds.

Can be set, to seek to the given time.

A media resource has a media timeline that maps times (in seconds) to positions in the media resource. The origin of a timeline is its earliest defined position. The duration of a timeline is its last defined position.

Establishing the media timeline: if the media resource somehow specifies an explicit timeline whose origin is not negative (i.e. gives each frame a specific time offset and gives the first frame a zero or positive offset), then the media timeline should be that timeline. (Whether the media resource can specify a timeline or not depends on the media resource's format.) If the media resource specifies an explicit start time and date, then that time and date should be considered the zero point in the media timeline; the timeline offset will be the time and date, exposed using the getStartDate() method.

If the media resource has a discontinuous timeline, the user agent must extend the timeline used at the start of the resource across the entire resource, so that the media timeline of the media resource increases linearly starting from the earliest possible position (as defined below), even if the underlying media data has out-of-order or even overlapping time codes.

For example, if two clips have been concatenated into one video file, but the video format exposes the original times for the two clips, the video data might expose a timeline that goes, say, 00:15..00:29 and then 00:05..00:38. However, the user agent would not expose those times; it would instead expose the times as 00:15..00:29 and 00:29..01:02, as a single video.

In the rare case of a media resource that does not have an explicit timeline, the zero time on the media timeline should correspond to the first frame of the media resource. In the even rarer case of a media resource with no explicit timings of any kind, not even frame durations, the user agent must itself determine the time for each frame in an implementation-defined manner.

An example of a file format with no explicit timeline but with explicit frame durations is the Animated GIF format. An example of a file format with no explicit timings at all is the JPEG-push format (multipart/x-mixed-replace with JPEG frames, often used as the format for MJPEG streams).

If, in the case of a resource with no timing information, the user agent will nonetheless be able to seek to an earlier point than the first frame originally provided by the server, then the zero time should correspond to the earliest seekable time of the media resource; otherwise, it should correspond to the first frame received from the server (the point in the media resource at which the user agent began receiving the stream).

At the time of writing, there is no known format that lacks explicit frame time offsets yet still supports seeking to a frame before the first frame sent by the server.

Consider a stream from a TV broadcaster, which begins streaming on a sunny Friday afternoon in October, and always sends connecting user agents the media data on the same media timeline, with its zero time set to the start of this stream. Months later, user agents connecting to this stream will find that the first frame they receive has a time with millions of seconds. The getStartDate() method would always return the date that the broadcast started; this would allow controllers to display real times in their scrubber (e.g. "2:30pm") rather than a time relative to when the broadcast began ("8 months, 4 hours, 12 minutes, and 23 seconds").

Consider a stream that carries a video with several concatenated fragments, broadcast by a server that does not allow user agents to request specific times but instead just streams the video data in a predetermined order, with the first frame delivered always being identified as the frame with time zero. If a user agent connects to this stream and receives fragments defined as covering timestamps 2010-03-20 23:15:00 UTC to 2010-03-21 00:05:00 UTC and 2010-02-12 14:25:00 UTC to 2010-02-12 14:35:00 UTC, it would expose this with a media timeline starting at 0s and extending to 3,600s (one hour). Assuming the streaming server disconnected at the end of the second clip, the duration attribute would then return 3,600. The getStartDate() method would return a Date object with a time corresponding to 2010-03-20 23:15:00 UTC. However, if a different user agent connected five minutes later, it would (presumably) receive fragments covering timestamps 2010-03-20 23:20:00 UTC to 2010-03-21 00:05:00 UTC and 2010-02-12 14:25:00 UTC to 2010-02-12 14:35:00 UTC, and would expose this with a media timeline starting at 0s and extending to 3,300s (fifty five minutes). In this case, the getStartDate() method would return a Date object with a time corresponding to 2010-03-20 23:20:00 UTC.

In both of these examples, the seekable attribute would give the ranges that the controller would want to actually display in its UI; typically, if the servers don't support seeking to arbitrary times, this would be the range of time from the moment the user agent connected to the stream up to the latest frame that the user agent has obtained; however, if the user agent starts discarding earlier information, the actual range might be shorter.

In any case, the user agent must ensure that the earliest possible position (as defined below) using the established media timeline, is greater than or equal to zero.

The media timeline also has an associated clock. Which clock is used is user-agent defined, and may be media resource-dependent, but it should approximate the user's wall clock.

Media elements have a current playback position, which must initially (i.e. in the absence of media data) be zero seconds. The current playback position is a time on the media timeline.

Media elements also have an official playback position, which must initially be set to zero seconds. The official playback position is an approximation of the current playback position that is kept stable while scripts are running.

Media elements also have a default playback start position, which must initially be set to zero seconds. This time is used to allow the element to be seeked even before the media is loaded.

Each media element has a show poster flag. When a media element is created, this flag must be set to true. This flag is used to control when the user agent is to show a poster frame for a video element instead of showing the video contents.

The currentTime attribute must, on getting, return the media element's default playback start position, unless that is zero, in which case it must return the element's official playback position. The returned value must be expressed in seconds. On setting, if the media element's readyState is HAVE_NOTHING, then it must set the media element's default playback start position to the new value; otherwise, it must set the official playback position to the new value and then seek to the new value. The new value must be interpreted as being in seconds.

If the media resource is a streaming resource, then the user agent might be unable to obtain certain parts of the resource after it has expired from its buffer. Similarly, some media resources might have a media timeline that doesn't start at zero. The earliest possible position is the earliest position in the stream or resource that the user agent can ever obtain again. It is also a time on the media timeline.

The earliest possible position is not explicitly exposed in the API; it corresponds to the start time of the first range in the seekable attribute's TimeRanges object, if any, or the current playback position otherwise.

When the earliest possible position changes, then: if the current playback position is before the earliest possible position, the user agent must seek to the earliest possible position; otherwise, if the user agent has not fired a timeupdate event at the element in the past 15 to 250ms and is not still running event handlers for such an event, then the user agent must queue a media element task given the media element to fire an event named timeupdate at the element.

Because of the above requirement and the requirement in the resource fetch algorithm that kicks in when the metadata of the clip becomes known, the current playback position can never be less than the earliest possible position.

If at any time the user agent learns that an audio or video track has ended and all media data relating to that track corresponds to parts of the media timeline that are before the earliest possible position, the user agent may queue a media element task given the media element to run these steps:

Remove the track from the audioTracks attribute's AudioTrackList object or the videoTracks attribute's VideoTrackList object as appropriate.

Fire an event named removetrack at the media element's aforementioned AudioTrackList or VideoTrackList object, using TrackEvent, with the track attribute initialized to the AudioTrack or VideoTrack object representing the track.

The duration attribute must return the time of the end of the media resource, in seconds, on the media timeline. If no media data is available, then the attributes must return the Not-a-Number (NaN) value. If the media resource is not known to be bounded (e.g. streaming radio, or a live event with no announced end time), then the attribute must return the positive Infinity value.

The user agent must determine the duration of the media resource before playing any part of the media data and before setting readyState to a value greater than or equal to HAVE_METADATA, even if doing so requires fetching multiple parts of the resource.

When the length of the media resource changes to a known value (e.g. from being unknown to known, or from a previously established length to a new length), the user agent must queue a media element task given the media element to fire an event named durationchange at the media element. (The event is not fired when the duration is reset as part of loading a new media resource.) If the duration is changed such that the current playback position ends up being greater than the time of the end of the media resource, then the user agent must also seek to the time of the end of the media resource.

If an "infinite" stream ends for some reason, then the duration would change from positive Infinity to the time of the last frame or sample in the stream, and the durationchange event would be fired. Similarly, if the user agent initially estimated the media resource's duration instead of determining it precisely, and later revises the estimate based on new information, then the duration would change and the durationchange event would be fired.

Some video files also have an explicit date and time corresponding to the zero time in the media timeline, known as the timeline offset. Initially, the timeline offset must be set to Not-a-Number (NaN).

The getStartDate() method must return a new Date object representing the current timeline offset.

The loop attribute is a boolean attribute that, if specified, indicates that the media element is to seek back to the start of the media resource upon reaching the end.

4.8.11.7 Ready states
media.readyState
✔MDN

Returns a value that expresses the current state of the element with respect to rendering the current playback position, from the codes in the list below.

Media elements have a ready state, which describes to what degree they are ready to be rendered at the current playback position. The possible values are as follows; the ready state of a media element at any particular time is the greatest value describing the state of the element:

HAVE_NOTHING (numeric value 0)

No information regarding the media resource is available. No data for the current playback position is available. Media elements whose networkState attribute are set to NETWORK_EMPTY are always in the HAVE_NOTHING state.

HAVE_METADATA (numeric value 1)

Enough of the resource has been obtained that the duration of the resource is available. In the case of a video element, the dimensions of the video are also available. No media data is available for the immediate current playback position.

HAVE_CURRENT_DATA (numeric value 2)

Data for the immediate current playback position is available, but either not enough data is available that the user agent could successfully advance the current playback position in the direction of playback at all without immediately reverting to the HAVE_METADATA state, or there is no more data to obtain in the direction of playback. For example, in video this corresponds to the user agent having data from the current frame, but not the next frame, when the current playback position is at the end of the current frame; and to when playback has ended.

HAVE_FUTURE_DATA (numeric value 3)

Data for the immediate current playback position is available, as well as enough data for the user agent to advance the current playback position in the direction of playback at least a little without immediately reverting to the HAVE_METADATA state, and the text tracks are ready. For example, in video this corresponds to the user agent having data for at least the current frame and the next frame when the current playback position is at the instant in time between the two frames, or to the user agent having the video data for the current frame and audio data to keep playing at least a little when the current playback position is in the middle of a frame. The user agent cannot be in this state if playback has ended, as the current playback position can never advance in this case.

HAVE_ENOUGH_DATA (numeric value 4)

All the conditions described for the HAVE_FUTURE_DATA state are met, and, in addition, either of the following conditions is also true:

The user agent estimates that data is being fetched at a rate where the current playback position, if it were to advance at the element's playbackRate, would not overtake the available data before playback reaches the end of the media resource.
The user agent has entered a state where waiting longer will not result in further data being obtained, and therefore nothing would be gained by delaying playback any further. (For example, the buffer might be full.)

In practice, the difference between HAVE_METADATA and HAVE_CURRENT_DATA is negligible. Really the only time the difference is relevant is when painting a video element onto a canvas, where it distinguishes the case where something will be drawn (HAVE_CURRENT_DATA or greater) from the case where nothing is drawn (HAVE_METADATA or less). Similarly, the difference between HAVE_CURRENT_DATA (only the current frame) and HAVE_FUTURE_DATA (at least this frame and the next) can be negligible (in the extreme, only one frame). The only time that distinction really matters is when a page provides an interface for "frame-by-frame" navigation.

When the ready state of a media element whose networkState is not NETWORK_EMPTY changes, the user agent must follow the steps given below:

Apply the first applicable set of substeps from the following list:

If the previous ready state was HAVE_NOTHING, and the new ready state is HAVE_METADATA

Queue a media element task given the media element to fire an event named loadedmetadata at the element.

Before this task is run, as part of the event loop mechanism, the rendering will have been updated to resize the video element if appropriate.

If the previous ready state was HAVE_METADATA and the new ready state is HAVE_CURRENT_DATA or greater

If this is the first time this occurs for this media element since the load() algorithm was last invoked, the user agent must queue a media element task given the media element to fire an event named loadeddata at the element.

If the new ready state is HAVE_FUTURE_DATA or HAVE_ENOUGH_DATA, then the relevant steps below must then be run also.

If the previous ready state was HAVE_FUTURE_DATA or more, and the new ready state is HAVE_CURRENT_DATA or less

If the media element was potentially playing before its readyState attribute changed to a value lower than HAVE_FUTURE_DATA, and the element has not ended playback, and playback has not stopped due to errors, paused for user interaction, or paused for in-band content, the user agent must queue a media element task given the media element to fire an event named timeupdate at the element, and queue a media element task given the media element to fire an event named waiting at the element.

If the previous ready state was HAVE_CURRENT_DATA or less, and the new ready state is HAVE_FUTURE_DATA

The user agent must queue a media element task given the media element to fire an event named canplay at the element.

If the element's paused attribute is false, the user agent must notify about playing for the element.

If the new ready state is HAVE_ENOUGH_DATA

If the previous ready state was HAVE_CURRENT_DATA or less, the user agent must queue a media element task given the media element to fire an event named canplay at the element, and, if the element's paused attribute is false, notify about playing for the element.

The user agent must queue a media element task given the media element to fire an event named canplaythrough at the element.

If the element is not eligible for autoplay, then the user agent must abort these substeps.

The user agent may run the following substeps:

Set the paused attribute to false.
If the element's show poster flag is true, set it to false and run the time marches on steps.
Queue a media element task given the element to fire an event named play at the element.
Notify about playing for the element.

Alternatively, if the element is a video element, the user agent may start observing whether the element intersects the viewport. When the element starts intersecting the viewport, if the element is still eligible for autoplay, run the substeps above. Optionally, when the element stops intersecting the viewport, if the can autoplay flag is still true and the autoplay attribute is still specified, run the following substeps:

Run the internal pause steps and set the can autoplay flag to true.
Queue a media element task given the element to fire an event named pause at the element.

The substeps for playing and pausing can run multiple times as the element starts or stops intersecting the viewport, as long as the can autoplay flag is true.

User agents do not need to support autoplay, and it is suggested that user agents honor user preferences on the matter. Authors are urged to use the autoplay attribute rather than using script to force the video to play, so as to allow the user to override the behavior if so desired.

It is possible for the ready state of a media element to jump between these states discontinuously. For example, the state of a media element can jump straight from HAVE_METADATA to HAVE_ENOUGH_DATA without passing through the HAVE_CURRENT_DATA and HAVE_FUTURE_DATA states.

The readyState IDL attribute must, on getting, return the value described above that describes the current ready state of the media element.

The autoplay attribute is a boolean attribute. When present, the user agent (as described in the algorithm described herein) will automatically begin playback of the media resource as soon as it can do so without stopping.

Authors are urged to use the autoplay attribute rather than using script to trigger automatic playback, as this allows the user to override the automatic playback when it is not desired, e.g. when using a screen reader. Authors are also encouraged to consider not using the automatic playback behavior at all, and instead to let the user agent wait for the user to start playback explicitly.

4.8.11.8 Playing the media resource
media.paused
✔MDN

Returns true if playback is paused; false otherwise.

media.ended
✔MDN

Returns true if playback has reached the end of the media resource.

media.defaultPlaybackRate [ = value ]
✔MDN

Returns the default rate of playback, for when the user is not fast-forwarding or reversing through the media resource.

Can be set, to change the default rate of playback.

The default rate has no direct effect on playback, but if the user switches to a fast-forward mode, when they return to the normal playback mode, it is expected that the rate of playback will be returned to the default rate of playback.

media.playbackRate [ = value ]
✔MDN

Returns the current rate playback, where 1.0 is normal speed.

Can be set, to change the rate of playback.

media.preservesPitch
MDN

Returns true if pitch-preserving algorithms are used when the playbackRate is not 1.0. The default value is true.

Can be set to false to have the media resource's audio pitch change up or down depending on the playbackRate. This is useful for aesthetic and performance reasons.

media.played

Returns a TimeRanges object that represents the ranges of the media resource that the user agent has played.

media.play()
✔MDN

Sets the paused attribute to false, loading the media resource and beginning playback if necessary. If the playback had ended, will restart it from the start.

media.pause()
✔MDN

Sets the paused attribute to true, loading the media resource if necessary.

The paused attribute represents whether the media element is paused or not. The attribute must initially be true.

A media element is a blocked media element if its readyState attribute is in the HAVE_NOTHING state, the HAVE_METADATA state, or the HAVE_CURRENT_DATA state, or if the element has paused for user interaction or paused for in-band content.

A media element is said to be potentially playing when its paused attribute is false, the element has not ended playback, playback has not stopped due to errors, and the element is not a blocked media element.

A waiting DOM event can be fired as a result of an element that is potentially playing stopping playback due to its readyState attribute changing to a value lower than HAVE_FUTURE_DATA.

A media element is said to be eligible for autoplay when all of the following are true:

its can autoplay flag is true;

its paused attribute is true;

it has an autoplay attribute specified;

its node document's active sandboxing flag set does not have the sandboxed automatic features browsing context flag set; and

its node document is allowed to use the "autoplay" feature.

A media element is said to be allowed to play if the user agent and the system allow media playback in the current context.

For example, a user agent could allow playback only when the media element's Window object has transient activation, but an exception could be made to allow playback while muted.

A media element is said to have ended playback when:

The element's readyState attribute is HAVE_METADATA or greater, and

Either:

The current playback position is the end of the media resource, and

The direction of playback is forwards, and

The media element does not have a loop attribute specified.

Or:

The current playback position is the earliest possible position, and

The direction of playback is backwards.

The ended attribute must return true if, the last time the event loop reached step 1, the media element had ended playback and the direction of playback was forwards, and false otherwise.

A media element is said to have stopped due to errors when the element's readyState attribute is HAVE_METADATA or greater, and the user agent encounters a non-fatal error during the processing of the media data, and due to that error, is not able to play the content at the current playback position.

A media element is said to have paused for user interaction when its paused attribute is false, the readyState attribute is either HAVE_FUTURE_DATA or HAVE_ENOUGH_DATA, and the user agent has reached a point in the media resource where the user has to make a selection for the resource to continue.

It is possible for a media element to have both ended playback and paused for user interaction at the same time.

When a media element that is potentially playing stops playing because it has paused for user interaction, the user agent must queue a media element task given the media element to fire an event named timeupdate at the element.

A media element is said to have paused for in-band content when its paused attribute is false, the readyState attribute is either HAVE_FUTURE_DATA or HAVE_ENOUGH_DATA, and the user agent has suspended playback of the media resource in order to play content that is temporally anchored to the media resource and has a nonzero length, or to play content that is temporally anchored to a segment of the media resource but has a length longer than that segment.

One example of when a media element would be paused for in-band content is when the user agent is playing audio descriptions from an external WebVTT file, and the synthesized speech generated for a cue is longer than the time between the text track cue start time and the text track cue end time.

When the current playback position reaches the end of the media resource when the direction of playback is forwards, then the user agent must follow these steps:

If the media element has a loop attribute specified, then seek to the earliest possible position of the media resource and return.

As defined above, the ended IDL attribute starts returning true once the event loop returns to step 1.

Queue a media element task given the media element and the following steps:

Fire an event named timeupdate at the media element.

If the media element has ended playback, the direction of playback is forwards, and paused is false, then:

Set the paused attribute to true.

Fire an event named pause at the media element.

Take pending play promises and reject pending play promises with the result and an "AbortError" DOMException.

Fire an event named ended at the media element.

When the current playback position reaches the earliest possible position of the media resource when the direction of playback is backwards, then the user agent must only queue a media element task given the media element to fire an event named timeupdate at the element.

The word "reaches" here does not imply that the current playback position needs to have changed during normal playback; it could be via seeking, for instance.

The defaultPlaybackRate attribute gives the desired speed at which the media resource is to play, as a multiple of its intrinsic speed. The attribute is mutable: on getting it must return the last value it was set to, or 1.0 if it hasn't yet been set; on setting the attribute must be set to the new value.

The defaultPlaybackRate is used by the user agent when it exposes a user interface to the user.

The playbackRate attribute gives the effective playback rate, which is the speed at which the media resource plays, as a multiple of its intrinsic speed. If it is not equal to the defaultPlaybackRate, then the implication is that the user is using a feature such as fast forward or slow motion playback. The attribute is mutable: on getting it must return the last value it was set to, or 1.0 if it hasn't yet been set; on setting, the user agent must follow these steps:

If the given value is not supported by the user agent, then throw a "NotSupportedError" DOMException.

Set playbackRate to the new value, and if the element is potentially playing, change the playback speed.

When the defaultPlaybackRate or playbackRate attributes change value (either by being set by script or by being changed directly by the user agent, e.g. in response to user control), the user agent must queue a media element task given the media element to fire an event named ratechange at the media element. The user agent must process attribute changes smoothly and must not introduce any perceivable gaps or muting of playback in response.

The preservesPitch getter steps are to return true if a pitch-preserving algorithm is in effect during playback. The setter steps are to correspondingly switch the pitch-preserving algorithm on or off, without any perceivable gaps or muting of playback. By default, such a pitch-preserving algorithm must be in effect (i.e., the getter will initially return true).

The played attribute must return a new static normalized TimeRanges object that represents the ranges of points on the media timeline of the media resource reached through the usual monotonic increase of the current playback position during normal playback, if any, at the time the attribute is evaluated.

Returning a new object each time is a bad pattern for attribute getters and is only enshrined here as it would be costly to change it. It is not to be copied to new APIs.

Each media element has a list of pending play promises, which must initially be empty.

To take pending play promises for a media element, the user agent must run the following steps:

Let promises be an empty list of promises.

Copy the media element's list of pending play promises to promises.

Clear the media element's list of pending play promises.

Return promises.

To resolve pending play promises for a media element with a list of promises promises, the user agent must resolve each promise in promises with undefined.

To reject pending play promises for a media element with a list of promises promises and an exception name error, the user agent must reject each promise in promises with error.

To notify about playing for a media element, the user agent must run the following steps:

Take pending play promises and let promises be the result.

Queue a media element task given the element and the following steps:

Fire an event named playing at the element.

Resolve pending play promises with promises.

When the play() method on a media element is invoked, the user agent must run the following steps.

If the media element is not allowed to play, then return a promise rejected with a "NotAllowedError" DOMException.

If the media element's error attribute is not null and its code is MEDIA_ERR_SRC_NOT_SUPPORTED, then return a promise rejected with a "NotSupportedError" DOMException.

This means that the dedicated media source failure steps have run. Playback is not possible until the media element load algorithm clears the error attribute.

Let promise be a new promise and append promise to the list of pending play promises.

Run the internal play steps for the media element.

Return promise.

The internal play steps for a media element are as follows:

If the media element's networkState attribute has the value NETWORK_EMPTY, invoke the media element's resource selection algorithm.

If the playback has ended and the direction of playback is forwards, seek to the earliest possible position of the media resource.

This will cause the user agent to queue a media element task given the media element to fire an event named timeupdate at the media element.

If the media element's paused attribute is true, then:

Change the value of paused to false.

If the show poster flag is true, set the element's show poster flag to false and run the time marches on steps.

Queue a media element task given the media element to fire an event named play at the element.

If the media element's readyState attribute has the value HAVE_NOTHING, HAVE_METADATA, or HAVE_CURRENT_DATA, queue a media element task given the media element to fire an event named waiting at the element.

Otherwise, the media element's readyState attribute has the value HAVE_FUTURE_DATA or HAVE_ENOUGH_DATA: notify about playing for the element.

Otherwise, if the media element's readyState attribute has the value HAVE_FUTURE_DATA or HAVE_ENOUGH_DATA, take pending play promises and queue a media element task given the media element to resolve pending play promises with the result.

The media element is already playing. However, it's possible that promise will be rejected before the queued task is run.

Set the media element's can autoplay flag to false.

When the pause() method is invoked, and when the user agent is required to pause the media element, the user agent must run the following steps:

If the media element's networkState attribute has the value NETWORK_EMPTY, invoke the media element's resource selection algorithm.

Run the internal pause steps for the media element.

The internal pause steps for a media element are as follows:

Set the media element's can autoplay flag to false.

If the media element's paused attribute is false, run the following steps:

Change the value of paused to true.

Take pending play promises and let promises be the result.

Queue a media element task given the media element and the following steps:

Fire an event named timeupdate at the element.

Fire an event named pause at the element.

Reject pending play promises with promises and an "AbortError" DOMException.

Set the official playback position to the current playback position.

If the element's playbackRate is positive or zero, then the direction of playback is forwards. Otherwise, it is backwards.

When a media element is potentially playing and its Document is a fully active Document, its current playback position must increase monotonically at the element's playbackRate units of media time per unit time of the media timeline's clock. (This specification always refers to this as an increase, but that increase could actually be a decrease if the element's playbackRate is negative.)

The element's playbackRate can be 0.0, in which case the current playback position doesn't move, despite playback not being paused (paused doesn't become true, and the pause event doesn't fire).

This specification doesn't define how the user agent achieves the appropriate playback rate — depending on the protocol and media available, it is plausible that the user agent could negotiate with the server to have the server provide the media data at the appropriate rate, so that (except for the period between when the rate is changed and when the server updates the stream's playback rate) the client doesn't actually have to drop or interpolate any frames.

Any time the user agent provides a stable state, the official playback position must be set to the current playback position.

While the direction of playback is backwards, any corresponding audio must be muted. While the element's playbackRate is so low or so high that the user agent cannot play audio usefully, the corresponding audio must also be muted. If the element's playbackRate is not 1.0 and preservesPitch is true, the user agent must apply pitch adjustment to preserve the original pitch of the audio. Otherwise, the user agent must speed up or slow down the audio without any pitch adjustment.

When a media element is potentially playing, its audio data played must be synchronized with the current playback position, at the element's effective media volume. The user agent must play the audio from audio tracks that were enabled when the event loop last reached step 1.

When a media element is not potentially playing, audio must not play for the element.

Media elements that are potentially playing while not in a document must not play any video, but should play any audio component. Media elements must not stop playing just because all references to them have been removed; only once a media element is in a state where no further audio could ever be played by that element may the element be garbage collected.

It is possible for an element to which no explicit references exist to play audio, even if such an element is not still actively playing: for instance, it could be unpaused but stalled waiting for content to buffer, or it could be still buffering, but with a suspend event listener that begins playback. Even a media element whose media resource has no audio tracks could eventually play audio again if it had an event listener that changes the media resource.

Each media element has a list of newly introduced cues, which must be initially empty. Whenever a text track cue is added to the list of cues of a text track that is in the list of text tracks for a media element, that cue must be added to the media element's list of newly introduced cues. Whenever a text track is added to the list of text tracks for a media element, all of the cues in that text track's list of cues must be added to the media element's list of newly introduced cues. When a media element's list of newly introduced cues has new cues added while the media element's show poster flag is not set, then the user agent must run the time marches on steps.

When a text track cue is removed from the list of cues of a text track that is in the list of text tracks for a media element, and whenever a text track is removed from the list of text tracks of a media element, if the media element's show poster flag is not set, then the user agent must run the time marches on steps.

When the current playback position of a media element changes (e.g. due to playback or seeking), the user agent must run the time marches on steps. To support use cases that depend on the timing accuracy of cue event firing, such as synchronizing captions with shot changes in a video, user agents should fire cue events as close as possible to their position on the media timeline, and ideally within 20 milliseconds. If the current playback position changes while the steps are running, then the user agent must wait for the steps to complete, and then must immediately rerun the steps. These steps are thus run as often as possible or needed.

If one iteration takes a long time, this can cause short duration cues to be skipped over as the user agent rushes ahead to "catch up", so these cues will not appear in the activeCues list.

The time marches on steps are as follows:

Let current cues be a list of cues, initialized to contain all the cues of all the hidden or showing text tracks of the media element (not the disabled ones) whose start times are less than or equal to the current playback position and whose end times are greater than the current playback position.

Let other cues be a list of cues, initialized to contain all the cues of hidden and showing text tracks of the media element that are not present in current cues.

Let last time be the current playback position at the time this algorithm was last run for this media element, if this is not the first time it has run.

If the current playback position has, since the last time this algorithm was run, only changed through its usual monotonic increase during normal playback, then let missed cues be the list of cues in other cues whose start times are greater than or equal to last time and whose end times are less than or equal to the current playback position. Otherwise, let missed cues be an empty list.

Remove all the cues in missed cues that are also in the media element's list of newly introduced cues, and then empty the element's list of newly introduced cues.

If the time was reached through the usual monotonic increase of the current playback position during normal playback, and if the user agent has not fired a timeupdate event at the element in the past 15 to 250ms and is not still running event handlers for such an event, then the user agent must queue a media element task given the media element to fire an event named timeupdate at the element. (In the other cases, such as explicit seeks, relevant events get fired as part of the overall process of changing the current playback position.)

The event thus is not to be fired faster than about 66Hz or slower than 4Hz (assuming the event handlers don't take longer than 250ms to run). User agents are encouraged to vary the frequency of the event based on the system load and the average cost of processing the event each time, so that the UI updates are not any more frequent than the user agent can comfortably handle while decoding the video.

If all of the cues in current cues have their text track cue active flag set, none of the cues in other cues have their text track cue active flag set, and missed cues is empty, then return.

If the time was reached through the usual monotonic increase of the current playback position during normal playback, and there are cues in other cues that have their text track cue pause-on-exit flag set and that either have their text track cue active flag set or are also in missed cues, then immediately pause the media element.

In the other cases, such as explicit seeks, playback is not paused by going past the end time of a cue, even if that cue has its text track cue pause-on-exit flag set.

Let events be a list of tasks, initially empty. Each task in this list will be associated with a text track, a text track cue, and a time, which are used to sort the list before the tasks are queued.

Let affected tracks be a list of text tracks, initially empty.

When the steps below say to prepare an event named event for a text track cue target with a time time, the user agent must run these steps:

Let track be the text track with which the text track cue target is associated.

Create a task to fire an event named event at target.

Add the newly created task to events, associated with the time time, the text track track, and the text track cue target.

Add track to affected tracks.

For each text track cue in missed cues, prepare an event named enter for the TextTrackCue object with the text track cue start time.

For each text track cue in other cues that either has its text track cue active flag set or is in missed cues, prepare an event named exit for the TextTrackCue object with the later of the text track cue end time and the text track cue start time.

For each text track cue in current cues that does not have its text track cue active flag set, prepare an event named enter for the TextTrackCue object with the text track cue start time.

Sort the tasks in events in ascending time order (tasks with earlier times first).

Further sort tasks in events that have the same time by the relative text track cue order of the text track cues associated with these tasks.

Finally, sort tasks in events that have the same time and same text track cue order by placing tasks that fire enter events before those that fire exit events.

Queue a media element task given the media element for each task in events, in list order.

Sort affected tracks in the same order as the text tracks appear in the media element's list of text tracks, and remove duplicates.

For each text track in affected tracks, in the list order, queue a media element task given the media element to fire an event named cuechange at the TextTrack object, and, if the text track has a corresponding track element, to then fire an event named cuechange at the track element as well.

Set the text track cue active flag of all the cues in the current cues, and unset the text track cue active flag of all the cues in the other cues.

Run the rules for updating the text track rendering of each of the text tracks in affected tracks that are showing, providing the text track's text track language as the fallback language if it is not the empty string. For example, for text tracks based on WebVTT, the rules for updating the display of WebVTT text tracks. [WEBVTT]

For the purposes of the algorithm above, a text track cue is considered to be part of a text track only if it is listed in the text track list of cues, not merely if it is associated with the text track.

If the media element's node document stops being a fully active document, then the playback will stop until the document is active again.

When a media element is removed from a Document, the user agent must run the following steps:

Await a stable state, allowing the task that removed the media element from the Document to continue. The synchronous section consists of all the remaining steps of this algorithm. (Steps in the synchronous section are marked with ⌛.)

⌛ If the media element is in a document, return.

⌛ Run the internal pause steps for the media element.

4.8.11.9 Seeking
media.seeking

Returns true if the user agent is currently seeking.

media.seekable
✔MDN

Returns a TimeRanges object that represents the ranges of the media resource to which it is possible for the user agent to seek.

media.fastSeek(time)
MDN

Seeks to near the given time as fast as possible, trading precision for speed. (To seek to a precise time, use the currentTime attribute.)

This does nothing if the media resource has not been loaded.

The seeking attribute must initially have the value false.

The fastSeek(time) method must seek to the time given by time, with the approximate-for-speed flag set.

When the user agent is required to seek to a particular new playback position in the media resource, optionally with the approximate-for-speed flag set, it means that the user agent must run the following steps. This algorithm interacts closely with the event loop mechanism; in particular, it has a synchronous section (which is triggered as part of the event loop algorithm). Steps in that section are marked with ⌛.

Set the media element's show poster flag to false.

If the media element's readyState is HAVE_NOTHING, return.

If the element's seeking IDL attribute is true, then another instance of this algorithm is already running. Abort that other instance of the algorithm without waiting for the step that it is running to complete.

Set the seeking IDL attribute to true.

If the seek was in response to a DOM method call or setting of an IDL attribute, then continue the script. The remainder of these steps must be run in parallel. With the exception of the steps marked with ⌛, they could be aborted at any time by another instance of this algorithm being invoked.

If the new playback position is later than the end of the media resource, then let it be the end of the media resource instead.

If the new playback position is less than the earliest possible position, let it be that position instead.

If the (possibly now changed) new playback position is not in one of the ranges given in the seekable attribute, then let it be the position in one of the ranges given in the seekable attribute that is the nearest to the new playback position. If two positions both satisfy that constraint (i.e. the new playback position is exactly in the middle between two ranges in the seekable attribute), then use the position that is closest to the current playback position. If there are no ranges given in the seekable attribute, then set the seeking IDL attribute to false and return.

If the approximate-for-speed flag is set, adjust the new playback position to a value that will allow for playback to resume promptly. If new playback position before this step is before current playback position, then the adjusted new playback position must also be before the current playback position. Similarly, if the new playback position before this step is after current playback position, then the adjusted new playback position must also be after the current playback position.

For example, the user agent could snap to a nearby key frame, so that it doesn't have to spend time decoding then discarding intermediate frames before resuming playback.

Queue a media element task given the media element to fire an event named seeking at the element.

Set the current playback position to the new playback position.

If the media element was potentially playing immediately before it started seeking, but seeking caused its readyState attribute to change to a value lower than HAVE_FUTURE_DATA, then a waiting event will be fired at the element.

This step sets the current playback position, and thus can immediately trigger other conditions, such as the rules regarding when playback "reaches the end of the media resource" (part of the logic that handles looping), even before the user agent is actually able to render the media data for that position (as determined in the next step).

The currentTime attribute returns the official playback position, not the current playback position, and therefore gets updated before script execution, separate from this algorithm.

Wait until the user agent has established whether or not the media data for the new playback position is available, and, if it is, until it has decoded enough data to play back that position.

Await a stable state. The synchronous section consists of all the remaining steps of this algorithm. (Steps in the synchronous section are marked with ⌛.)

⌛ Set the seeking IDL attribute to false.

⌛ Run the time marches on steps.

⌛ Queue a media element task given the media element to fire an event named timeupdate at the element.

⌛ Queue a media element task given the media element to fire an event named seeked at the element.

The seekable attribute must return a new static normalized TimeRanges object that represents the ranges of the media resource, if any, that the user agent is able to seek to, at the time the attribute is evaluated.

If the user agent can seek to anywhere in the media resource, e.g. because it is a simple movie file and the user agent and the server support HTTP Range requests, then the attribute would return an object with one range, whose start is the time of the first frame (the earliest possible position, typically zero), and whose end is the same as the time of the first frame plus the duration attribute's value (which would equal the time of the last frame, and might be positive Infinity).

The range might be continuously changing, e.g. if the user agent is buffering a sliding window on an infinite stream. This is the behavior seen with DVRs viewing live TV, for instance.

Returning a new object each time is a bad pattern for attribute getters and is only enshrined here as it would be costly to change it. It is not to be copied to new APIs.

User agents should adopt a very liberal and optimistic view of what is seekable. User agents should also buffer recent content where possible to enable seeking to be fast.

For instance, consider a large video file served on an HTTP server without support for HTTP Range requests. A browser could implement this by only buffering the current frame and data obtained for subsequent frames, never allow seeking, except for seeking to the very start by restarting the playback. However, this would be a poor implementation. A high quality implementation would buffer the last few minutes of content (or more, if sufficient storage space is available), allowing the user to jump back and rewatch something surprising without any latency, and would in addition allow arbitrary seeking by reloading the file from the start if necessary, which would be slower but still more convenient than having to literally restart the video and watch it all the way through just to get to an earlier unbuffered spot.

Media resources might be internally scripted or interactive. Thus, a media element could play in a non-linear fashion. If this happens, the user agent must act as if the algorithm for seeking was used whenever the current playback position changes in a discontinuous fashion (so that the relevant events fire).

4.8.11.10 Media resources with multiple media tracks

A media resource can have multiple embedded audio and video tracks. For example, in addition to the primary video and audio tracks, a media resource could have foreign-language dubbed dialogues, director's commentaries, audio descriptions, alternative angles, or sign-language overlays.

media.audioTracks
✔MDN

Returns an AudioTrackList object representing the audio tracks available in the media resource.

media.videoTracks
✔MDN

Returns a VideoTrackList object representing the video tracks available in the media resource.

The audioTracks attribute of a media element must return a live AudioTrackList object representing the audio tracks available in the media element's media resource.

The videoTracks attribute of a media element must return a live VideoTrackList object representing the video tracks available in the media element's media resource.

There are only ever one AudioTrackList object and one VideoTrackList object per media element, even if another media resource is loaded into the element: the objects are reused. (The AudioTrack and VideoTrack objects are not, though.)

4.8.11.10.1 AudioTrackList and VideoTrackList objects
✔MDN

The AudioTrackList and VideoTrackList interfaces are used by attributes defined in the previous section.

✔MDN
[Exposed=Window]
interface AudioTrackList : EventTarget {
  readonly attribute unsigned long length;
  getter AudioTrack (unsigned long index);
  AudioTrack? getTrackById(DOMString id);

  attribute EventHandler onchange;
  attribute EventHandler onaddtrack;
  attribute EventHandler onremovetrack;
};

[Exposed=Window]
interface AudioTrack {
  readonly attribute DOMString id;
  readonly attribute DOMString kind;
  readonly attribute DOMString label;
  readonly attribute DOMString language;
  attribute boolean enabled;
};

[Exposed=Window]
interface VideoTrackList : EventTarget {
  readonly attribute unsigned long length;
  getter VideoTrack (unsigned long index);
  VideoTrack? getTrackById(DOMString id);
  readonly attribute long selectedIndex;

  attribute EventHandler onchange;
  attribute EventHandler onaddtrack;
  attribute EventHandler onremovetrack;
};

[Exposed=Window]
interface VideoTrack {
  readonly attribute DOMString id;
  readonly attribute DOMString kind;
  readonly attribute DOMString label;
  readonly attribute DOMString language;
  attribute boolean selected;
};
media.audioTracks.length
✔MDN
media.videoTracks.length
✔MDN

Returns the number of tracks in the list.

audioTrack = media.audioTracks[index]
videoTrack = media.videoTracks[index]

Returns the specified AudioTrack or VideoTrack object.

audioTrack = media.audioTracks.getTrackById(id)
✔MDN
videoTrack = media.videoTracks.getTrackById(id)
✔MDN

Returns the AudioTrack or VideoTrack object with the given identifier, or null if no track has that identifier.

audioTrack.id
✔MDN
videoTrack.id
✔MDN

Returns the ID of the given track. This is the ID that can be used with a fragment if the format supports media fragment syntax, and that can be used with the getTrackById() method.

audioTrack.kind
✔MDN
videoTrack.kind
✔MDN

Returns the category the given track falls into. The possible track categories are given below.

audioTrack.label
✔MDN
videoTrack.label
✔MDN

Returns the label of the given track, if known, or the empty string otherwise.

audioTrack.language
✔MDN
videoTrack.language
✔MDN

Returns the language of the given track, if known, or the empty string otherwise.

audioTrack.enabled [ = value ]
✔MDN

Returns true if the given track is active, and false otherwise.

Can be set, to change whether the track is enabled or not. If multiple audio tracks are enabled simultaneously, they are mixed.

media.videoTracks.selectedIndex
✔MDN

Returns the index of the currently selected track, if any, or −1 otherwise.

videoTrack.selected [ = value ]
✔MDN

Returns true if the given track is active, and false otherwise.

Can be set, to change whether the track is selected or not. Either zero or one video track is selected; selecting a new track while a previous one is selected will unselect the previous one.

An AudioTrackList object represents a dynamic list of zero or more audio tracks, of which zero or more can be enabled at a time. Each audio track is represented by an AudioTrack object.

A VideoTrackList object represents a dynamic list of zero or more video tracks, of which zero or one can be selected at a time. Each video track is represented by a VideoTrack object.

Tracks in AudioTrackList and VideoTrackList objects must be consistently ordered. If the media resource is in a format that defines an order, then that order must be used; otherwise, the order must be the relative order in which the tracks are declared in the media resource. The order used is called the natural order of the list.

Each track in one of these objects thus has an index; the first has the index 0, and each subsequent track is numbered one higher than the previous one. If a media resource dynamically adds or removes audio or video tracks, then the indices of the tracks will change dynamically. If the media resource changes entirely, then all the previous tracks will be removed and replaced with new tracks.

The AudioTrackList length and VideoTrackList length attribute getters must return the number of tracks represented by their objects at the time of getting.

The supported property indices of AudioTrackList and VideoTrackList objects at any instant are the numbers from zero to the number of tracks represented by the respective object minus one, if any tracks are represented. If an AudioTrackList or VideoTrackList object represents no tracks, it has no supported property indices.

To determine the value of an indexed property for a given index index in an AudioTrackList or VideoTrackList object list, the user agent must return the AudioTrack or VideoTrack object that represents the indexth track in list.

The AudioTrackList getTrackById(id) and VideoTrackList getTrackById(id) methods must return the first AudioTrack or VideoTrack object (respectively) in the AudioTrackList or VideoTrackList object (respectively) whose identifier is equal to the value of the id argument (in the natural order of the list, as defined above). When no tracks match the given argument, the methods must return null.

The AudioTrack and VideoTrack objects represent specific tracks of a media resource. Each track can have an identifier, category, label, and language. These aspects of a track are permanent for the lifetime of the track; even if a track is removed from a media resource's AudioTrackList or VideoTrackList objects, those aspects do not change.

In addition, AudioTrack objects can each be enabled or disabled; this is the audio track's enabled state. When an AudioTrack is created, its enabled state must be set to false (disabled). The resource fetch algorithm can override this.

Similarly, a single VideoTrack object per VideoTrackList object can be selected, this is the video track's selection state. When a VideoTrack is created, its selection state must be set to false (not selected). The resource fetch algorithm can override this.

The AudioTrack id and VideoTrack id attributes must return the identifier of the track, if it has one, or the empty string otherwise. If the media resource is in a format that supports media fragment syntax, the identifier returned for a particular track must be the same identifier that would enable the track if used as the name of a track in the track dimension of such a fragment. [INBAND]

For example, in Ogg files, this would be the Name header field of the track. [OGGSKELETONHEADERS]

The AudioTrack kind and VideoTrack kind attributes must return the category of the track, if it has one, or the empty string otherwise.

The category of a track is the string given in the first column of the table below that is the most appropriate for the track based on the definitions in the table's second and third columns, as determined by the metadata included in the track in the media resource. The cell in the third column of a row says what the category given in the cell in the first column of that row applies to; a category is only appropriate for an audio track if it applies to audio tracks, and a category is only appropriate for video tracks if it applies to video tracks. Categories must only be returned for AudioTrack objects if they are appropriate for audio, and must only be returned for VideoTrack objects if they are appropriate for video.

For Ogg files, the Role header field of the track gives the relevant metadata. For DASH media resources, the Role element conveys the information. For WebM, only the FlagDefault element currently maps to a value. Sourcing In-band Media Resource Tracks from Media Containers into HTML has further details. [OGGSKELETONHEADERS] [DASH] [WEBMCG] [INBAND]

Return values for AudioTrack's kind and VideoTrack's kind
Category	Definition	Applies to...	Examples
"alternative"	A possible alternative to the main track, e.g. a different take of a song (audio), or a different angle (video).	Audio and video.	Ogg: "audio/alternate" or "video/alternate"; DASH: "alternate" without "main" and "commentary" roles, and, for audio, without the "dub" role (other roles ignored).
"captions"	A version of the main video track with captions burnt in. (For legacy content; new content would use text tracks.)	Video only.	DASH: "caption" and "main" roles together (other roles ignored).
"descriptions"	An audio description of a video track.	Audio only.	Ogg: "audio/audiodesc".
"main"	The primary audio or video track.	Audio and video.	Ogg: "audio/main" or "video/main"; WebM: the "FlagDefault" element is set; DASH: "main" role without "caption", "subtitle", and "dub" roles (other roles ignored).
"main-desc"	The primary audio track, mixed with audio descriptions.	Audio only.	AC3 audio in MPEG-2 TS: bsmod=2 and full_svc=1.
"sign"	A sign-language interpretation of an audio track.	Video only.	Ogg: "video/sign".
"subtitles"	A version of the main video track with subtitles burnt in. (For legacy content; new content would use text tracks.)	Video only.	DASH: "subtitle" and "main" roles together (other roles ignored).
"translation"	A translated version of the main audio track.	Audio only.	Ogg: "audio/dub". DASH: "dub" and "main" roles together (other roles ignored).
"commentary"	Commentary on the primary audio or video track, e.g. a director's commentary.	Audio and video.	DASH: "commentary" role without "main" role (other roles ignored).
"" (empty string)	No explicit kind, or the kind given by the track's metadata is not recognized by the user agent.	Audio and video.	

The AudioTrack label and VideoTrack label attributes must return the label of the track, if it has one, or the empty string otherwise. [INBAND]

The AudioTrack language and VideoTrack language attributes must return the BCP 47 language tag of the language of the track, if it has one, or the empty string otherwise. If the user agent is not able to express that language as a BCP 47 language tag (for example because the language information in the media resource's format is a free-form string without a defined interpretation), then the method must return the empty string, as if the track had no language. [INBAND]

The AudioTrack enabled attribute, on getting, must return true if the track is currently enabled, and false otherwise. On setting, it must enable the track if the new value is true, and disable it otherwise. (If the track is no longer in an AudioTrackList object, then the track being enabled or disabled has no effect beyond changing the value of the attribute on the AudioTrack object.)

Whenever an audio track in an AudioTrackList that was disabled is enabled, and whenever one that was enabled is disabled, the user agent must queue a media element task given the media element to fire an event named change at the AudioTrackList object.

An audio track that has no data for a particular position on the media timeline, or that does not exist at that position, must be interpreted as being silent at that point on the timeline.

The VideoTrackList selectedIndex attribute must return the index of the currently selected track, if any. If the VideoTrackList object does not currently represent any tracks, or if none of the tracks are selected, it must instead return −1.

The VideoTrack selected attribute, on getting, must return true if the track is currently selected, and false otherwise. On setting, it must select the track if the new value is true, and unselect it otherwise. If the track is in a VideoTrackList, then all the other VideoTrack objects in that list must be unselected. (If the track is no longer in a VideoTrackList object, then the track being selected or unselected has no effect beyond changing the value of the attribute on the VideoTrack object.)

Whenever a track in a VideoTrackList that was previously not selected is selected, and whenever the selected track in a VideoTrackList is unselected without a new track being selected in its stead, the user agent must queue a media element task given the media element to fire an event named change at the VideoTrackList object. This task must be queued before the task that fires the resize event, if any.

A video track that has no data for a particular position on the media timeline must be interpreted as being transparent black at that point on the timeline, with the same dimensions as the last frame before that position, or, if the position is before all the data for that track, the same dimensions as the first frame for that track. A track that does not exist at all at the current position must be treated as if it existed but had no data.

For instance, if a video has a track that is only introduced after one hour of playback, and the user selects that track then goes back to the start, then the user agent will act as if that track started at the start of the media resource but was simply transparent until one hour in.

The following are the event handlers (and their corresponding event handler event types) that must be supported, as event handler IDL attributes, by all objects implementing the AudioTrackList and VideoTrackList interfaces:

Event handler	Event handler event type
onchange
✔MDN
	change
onaddtrack
✔MDN
	addtrack
onremovetrack
✔MDN
	removetrack
4.8.11.10.2 Selecting specific audio and video tracks declaratively

The audioTracks and videoTracks attributes allow scripts to select which track should play, but it is also possible to select specific tracks declaratively, by specifying particular tracks in the fragment of the URL of the media resource. The format of the fragment depends on the MIME type of the media resource. [RFC2046] [URL]

In this example, a video that uses a format that supports media fragment syntax is embedded in such a way that the alternative angles labeled "Alternative" are enabled instead of the default video track.

<video src="myvideo#track=Alternative"></video>
4.8.11.11 Timed text tracks
4.8.11.11.1 Text track model

A media element can have a group of associated text tracks, known as the media element's list of text tracks. The text tracks are sorted as follows:

The text tracks corresponding to track element children of the media element, in tree order.

Any text tracks added using the addTextTrack() method, in the order they were added, oldest first.

Any media-resource-specific text tracks (text tracks corresponding to data in the media resource), in the order defined by the media resource's format specification.

A text track consists of:

The kind of text track

This decides how the track is handled by the user agent. The kind is represented by a string. The possible strings are:

subtitles
captions
descriptions
chapters
metadata

The kind of track can change dynamically, in the case of a text track corresponding to a track element.

A label

This is a human-readable string intended to identify the track for the user.

The label of a track can change dynamically, in the case of a text track corresponding to a track element.

When a text track label is the empty string, the user agent should automatically generate an appropriate label from the text track's other properties (e.g. the kind of text track and the text track's language) for use in its user interface. This automatically-generated label is not exposed in the API.

An in-band metadata track dispatch type

This is a string extracted from the media resource specifically for in-band metadata tracks to enable such tracks to be dispatched to different scripts in the document.

For example, a traditional TV station broadcast streamed on the web and augmented with web-specific interactive features could include text tracks with metadata for ad targeting, trivia game data during game shows, player states during sports games, recipe information during food programs, and so forth. As each program starts and ends, new tracks might be added or removed from the stream, and as each one is added, the user agent could bind them to dedicated script modules using the value of this attribute.

Other than for in-band metadata text tracks, the in-band metadata track dispatch type is the empty string. How this value is populated for different media formats is described in steps to expose a media-resource-specific text track.

A language

This is a string (a BCP 47 language tag) representing the language of the text track's cues. [BCP47]

The language of a text track can change dynamically, in the case of a text track corresponding to a track element.

A readiness state

One of the following:

Not loaded

Indicates that the text track's cues have not been obtained.

Loading

Indicates that the text track is loading and there have been no fatal errors encountered so far. Further cues might still be added to the track by the parser.

Loaded

Indicates that the text track has been loaded with no fatal errors.

Failed to load

Indicates that the text track was enabled, but when the user agent attempted to obtain it, this failed in some way (e.g., URL could not be parsed, network error, unknown text track format). Some or all of the cues are likely missing and will not be obtained.

The readiness state of a text track changes dynamically as the track is obtained.

A mode

One of the following:

Disabled

Indicates that the text track is not active. Other than for the purposes of exposing the track in the DOM, the user agent is ignoring the text track. No cues are active, no events are fired, and the user agent will not attempt to obtain the track's cues.

Hidden

Indicates that the text track is active, but that the user agent is not actively displaying the cues. If no attempt has yet been made to obtain the track's cues, the user agent will perform such an attempt momentarily. The user agent is maintaining a list of which cues are active, and events are being fired accordingly.

Showing

Indicates that the text track is active. If no attempt has yet been made to obtain the track's cues, the user agent will perform such an attempt momentarily. The user agent is maintaining a list of which cues are active, and events are being fired accordingly. In addition, for text tracks whose kind is subtitles or captions, the cues are being overlaid on the video as appropriate; for text tracks whose kind is descriptions, the user agent is making the cues available to the user in a non-visual fashion; and for text tracks whose kind is chapters, the user agent is making available to the user a mechanism by which the user can navigate to any point in the media resource by selecting a cue.

A list of zero or more cues

A list of text track cues, along with rules for updating the text track rendering. For example, for WebVTT, the rules for updating the display of WebVTT text tracks. [WEBVTT]

The list of cues of a text track can change dynamically, either because the text track has not yet been loaded or is still loading, or due to DOM manipulation.

Each text track has a corresponding TextTrack object.

Each media element has a list of pending text tracks, which must initially be empty, a blocked-on-parser flag, which must initially be false, and a did-perform-automatic-track-selection flag, which must also initially be false.

When the user agent is required to populate the list of pending text tracks of a media element, the user agent must add to the element's list of pending text tracks each text track in the element's list of text tracks whose text track mode is not disabled and whose text track readiness state is loading.

Whenever a track element's parent node changes, the user agent must remove the corresponding text track from any list of pending text tracks that it is in.

Whenever a text track's text track readiness state changes to either loaded or failed to load, the user agent must remove it from any list of pending text tracks that it is in.

When a media element is created by an HTML parser or XML parser, the user agent must set the element's blocked-on-parser flag to true. When a media element is popped off the stack of open elements of an HTML parser or XML parser, the user agent must honor user preferences for automatic text track selection, populate the list of pending text tracks, and set the element's blocked-on-parser flag to false.

The text tracks of a media element are ready when both the element's list of pending text tracks is empty and the element's blocked-on-parser flag is false.

Each media element has a pending text track change notification flag, which must initially be unset.

Whenever a text track that is in a media element's list of text tracks has its text track mode change value, the user agent must run the following steps for the media element:

If the media element's pending text track change notification flag is set, return.

Set the media element's pending text track change notification flag.

Queue a media element task given the media element to run these steps:

Unset the media element's pending text track change notification flag.

Fire an event named change at the media element's textTracks attribute's TextTrackList object.

If the media element's show poster flag is not set, run the time marches on steps.

The task source for the tasks listed in this section is the DOM manipulation task source.

A text track cue is the unit of time-sensitive data in a text track, corresponding for instance for subtitles and captions to the text that appears at a particular time and disappears at another time.

Each text track cue consists of:

An identifier

An arbitrary string.

A start time

The time, in seconds and fractions of a second, that describes the beginning of the range of the media data to which the cue applies.

An end time

The time, in seconds and fractions of a second, that describes the end of the range of the media data to which the cue applies, or positive Infinity for an unbounded text track cue.

A pause-on-exit flag

A boolean indicating whether playback of the media resource is to pause when the end of the range to which the cue applies is reached.

Some additional format-specific data

Additional fields, as needed for the format, including the actual data of the cue. For example, WebVTT has a text track cue writing direction and so forth. [WEBVTT]

An unbounded text track cue is a text track cue with a text track cue end time set to positive Infinity. An active unbounded text track cue cannot become inactive through the usual monotonic increase of the current playback position during normal playback (e.g. a metadata cue for a chapter in a live event with no announced end time.)

The text track cue start time and text track cue end time can be negative. (The current playback position can never be negative, though, so cues entirely before time zero cannot be active.)

Each text track cue has a corresponding TextTrackCue object (or more specifically, an object that inherits from TextTrackCue — for example, WebVTT cues use the VTTCue interface). A text track cue's in-memory representation can be dynamically changed through this TextTrackCue API. [WEBVTT]

A text track cue is associated with rules for updating the text track rendering, as defined by the specification for the specific kind of text track cue. These rules are used specifically when the object representing the cue is added to a TextTrack object using the addCue() method.

In addition, each text track cue has two pieces of dynamic information:

The active flag

This flag must be initially unset. The flag is used to ensure events are fired appropriately when the cue becomes active or inactive, and to make sure the right cues are rendered.

The user agent must synchronously unset this flag whenever the text track cue is removed from its text track's text track list of cues; whenever the text track itself is removed from its media element's list of text tracks or has its text track mode changed to disabled; and whenever the media element's readyState is changed back to HAVE_NOTHING. When the flag is unset in this way for one or more cues in text tracks that were showing prior to the relevant incident, the user agent must, after having unset the flag for all the affected cues, apply the rules for updating the text track rendering of those text tracks. For example, for text tracks based on WebVTT, the rules for updating the display of WebVTT text tracks. [WEBVTT]

The display state

This is used as part of the rendering model, to keep cues in a consistent position. It must initially be empty. Whenever the text track cue active flag is unset, the user agent must empty the text track cue display state.

The text track cues of a media element's text tracks are ordered relative to each other in the text track cue order, which is determined as follows: first group the cues by their text track, with the groups being sorted in the same order as their text tracks appear in the media element's list of text tracks; then, within each group, cues must be sorted by their start time, earliest first; then, any cues with the same start time must be sorted by their end time, latest first; and finally, any cues with identical end times must be sorted in the order they were last added to their respective text track list of cues, oldest first (so e.g. for cues from a WebVTT file, that would initially be the order in which the cues were listed in the file). [WEBVTT]

4.8.11.11.2 Sourcing in-band text tracks

A media-resource-specific text track is a text track that corresponds to data found in the media resource.

Rules for processing and rendering such data are defined by the relevant specifications, e.g. the specification of the video format if the media resource is a video. Details for some legacy formats can be found in Sourcing In-band Media Resource Tracks from Media Containers into HTML. [INBAND]

When a media resource contains data that the user agent recognizes and supports as being equivalent to a text track, the user agent runs the steps to expose a media-resource-specific text track with the relevant data, as follows.

Associate the relevant data with a new text track and its corresponding new TextTrack object. The text track is a media-resource-specific text track.

Set the new text track's kind, label, and language based on the semantics of the relevant data, as defined by the relevant specification. If there is no label in that data, then the label must be set to the empty string.

Associate the text track list of cues with the rules for updating the text track rendering appropriate for the format in question.

If the new text track's kind is chapters or metadata, then set the text track in-band metadata track dispatch type as follows, based on the type of the media resource:

If the media resource is an Ogg file
The text track in-band metadata track dispatch type must be set to the value of the Name header field. [OGGSKELETONHEADERS]
If the media resource is a WebM file
The text track in-band metadata track dispatch type must be set to the value of the CodecID element. [WEBMCG]
If the media resource is an MPEG-2 file
Let stream type be the value of the "stream_type" field describing the text track's type in the file's program map section, interpreted as an 8-bit unsigned integer. Let length be the value of the "ES_info_length" field for the track in the same part of the program map section, interpreted as an integer as defined by Generic coding of moving pictures and associated audio information. Let descriptor bytes be the length bytes following the "ES_info_length" field. The text track in-band metadata track dispatch type must be set to the concatenation of the stream type byte and the zero or more descriptor bytes bytes, expressed in hexadecimal using ASCII upper hex digits. [MPEG2]
If the media resource is an MPEG-4 file
Let stsd box be the first stsd box of the first stbl box of the first minf box of the first mdia box of the text track's trak box in the first moov box of the file, or null if no such stsd box exists. If stsd box is null, or if stsd box has neither a mett box nor a metx box, then the text track in-band metadata track dispatch type must be set to the empty string. Otherwise, if stsd box has a mett box, then the text track in-band metadata track dispatch type must be set to either the concatenation of the string "mett", a U+0020 SPACE character, and the value of the first mime_format field of the first mett box of stsd box, or the empty string if that field is absent in that box. Otherwise, if stsd box has no mett box but has a metx box, then the text track in-band metadata track dispatch type must be set to either the concatenation of the string "metx", a U+0020 SPACE character, and the value of the first namespace field of the first metx box of stsd box, or the empty string if that field is absent in that box. [MPEG4]

Populate the new text track's list of cues with the cues parsed so far, following the guidelines for exposing cues, and begin updating it dynamically as necessary.

Set the new text track's readiness state to loaded.

Set the new text track's mode to the mode consistent with the user's preferences and the requirements of the relevant specification for the data.

For instance, if there are no other active subtitles, and this is a forced subtitle track (a subtitle track giving subtitles in the audio track's primary language, but only for audio that is actually in another language), then those subtitles might be activated here.

Add the new text track to the media element's list of text tracks.

Fire an event named addtrack at the media element's textTracks attribute's TextTrackList object, using TrackEvent, with the track attribute initialized to the text track's TextTrack object.

4.8.11.11.3 Sourcing out-of-band text tracks

When a track element is created, it must be associated with a new text track (with its value set as defined below) and its corresponding new TextTrack object.

The text track kind is determined from the state of the element's kind attribute according to the following table; for a state given in a cell of the first column, the kind is the string given in the second column:

State	String
Subtitles	subtitles
Captions	captions
Descriptions	descriptions
Chapters metadata	chapters
Metadata	metadata

The text track label is the element's track label.

The text track language is the element's track language, if any, or the empty string otherwise.

As the kind, label, and srclang attributes are set, changed, or removed, the text track must update accordingly, as per the definitions above.

Changes to the track URL are handled in the algorithm below.

The text track readiness state is initially not loaded, and the text track mode is initially disabled.

The text track list of cues is initially empty. It is dynamically modified when the referenced file is parsed. Associated with the list are the rules for updating the text track rendering appropriate for the format in question; for WebVTT, this is the rules for updating the display of WebVTT text tracks. [WEBVTT]

When a track element's parent element changes and the new parent is a media element, then the user agent must add the track element's corresponding text track to the media element's list of text tracks, and then queue a media element task given the media element to fire an event named addtrack at the media element's textTracks attribute's TextTrackList object, using TrackEvent, with the track attribute initialized to the text track's TextTrack object.

When a track element's parent element changes and the old parent was a media element, then the user agent must remove the track element's corresponding text track from the media element's list of text tracks, and then queue a media element task given the media element to fire an event named removetrack at the media element's textTracks attribute's TextTrackList object, using TrackEvent, with the track attribute initialized to the text track's TextTrack object.

When a text track corresponding to a track element is added to a media element's list of text tracks, the user agent must queue a media element task given the media element to run the following steps for the media element:

If the element's blocked-on-parser flag is true, then return.

If the element's did-perform-automatic-track-selection flag is true, then return.

Honor user preferences for automatic text track selection for this element.

When the user agent is required to honor user preferences for automatic text track selection for a media element, the user agent must run the following steps:

Perform automatic text track selection for subtitles and captions.

Perform automatic text track selection for descriptions.

If there are any text tracks in the media element's list of text tracks whose text track kind is chapters or metadata that correspond to track elements with a default attribute set whose text track mode is set to disabled, then set the text track mode of all such tracks to hidden.

Set the element's did-perform-automatic-track-selection flag to true.

When the steps above say to perform automatic text track selection for one or more text track kinds, it means to run the following steps:

Let candidates be a list consisting of the text tracks in the media element's list of text tracks whose text track kind is one of the kinds that were passed to the algorithm, if any, in the order given in the list of text tracks.

If candidates is empty, then return.

If any of the text tracks in candidates have a text track mode set to showing, return.

If the user has expressed an interest in having a track from candidates enabled based on its text track kind, text track language, and text track label, then set its text track mode to showing.

For example, the user could have set a browser preference to the effect of "I want French captions whenever possible", or "If there is a subtitle track with 'Commentary' in the title, enable it", or "If there are audio description tracks available, enable one, ideally in Swiss German, but failing that in Standard Swiss German or Standard German".

Otherwise, if there are any text tracks in candidates that correspond to track elements with a default attribute set whose text track mode is set to disabled, then set the text track mode of the first such track to showing.

When a text track corresponding to a track element experiences any of the following circumstances, the user agent must start the track processing model for that text track and its track element:

The track element is created.
The text track has its text track mode changed.
The track element's parent element changes and the new parent is a media element.

When a user agent is to start the track processing model for a text track and its track element, it must run the following algorithm. This algorithm interacts closely with the event loop mechanism; in particular, it has a synchronous section (which is triggered as part of the event loop algorithm). The steps in that section are marked with ⌛.

If another occurrence of this algorithm is already running for this text track and its track element, return, letting that other algorithm take care of this element.

If the text track's text track mode is not set to one of hidden or showing, then return.

If the text track's track element does not have a media element as a parent, return.

Run the remainder of these steps in parallel, allowing whatever caused these steps to run to continue.

Top: Await a stable state. The synchronous section consists of the following steps. (The steps in the synchronous section are marked with ⌛.)

⌛ Set the text track readiness state to loading.

⌛ Let URL be the track URL of the track element.

⌛ If the track element's parent is a media element, then let corsAttributeState be the state of the parent media element's crossorigin content attribute. Otherwise, let corsAttributeState be No CORS.

End the synchronous section, continuing the remaining steps in parallel.

If URL is not the empty string, then:

Let request be the result of creating a potential-CORS request given URL, "track", and corsAttributeState, and with the same-origin fallback flag set.

Set request's client to the track element's node document's relevant settings object.

Set request's initiator type to "track".

Fetch request.

The tasks queued by the fetching algorithm on the networking task source to process the data as it is being fetched must determine the type of the resource. If the type of the resource is not a supported text track format, the load will fail, as described below. Otherwise, the resource's data must be passed to the appropriate parser (e.g., the WebVTT parser) as it is received, with the text track list of cues being used for that parser's output. [WEBVTT]

The appropriate parser will incrementally update the text track list of cues during these networking task source tasks, as each such task is run with whatever data has been received from the network).

This specification does not currently say whether or how to check the MIME types of text tracks, or whether or how to perform file type sniffing using the actual file data. Implementers differ in their intentions on this matter and it is therefore unclear what the right solution is. In the absence of any requirement here, the HTTP specifications' strict requirement to follow the Content-Type header prevails ("Content-Type specifies the media type of the underlying data." ... "If and only if the media type is not given by a Content-Type field, the recipient MAY attempt to guess the media type via inspection of its content and/or the name extension(s) of the URI used to identify the resource.").

If fetching fails for any reason (network error, the server returns an error code, CORS fails, etc.), or if URL is the empty string, then queue an element task on the DOM manipulation task source given the media element to first change the text track readiness state to failed to load and then fire an event named error at the track element.

If fetching does not fail, but the type of the resource is not a supported text track format, or the file was not successfully processed (e.g., the format in question is an XML format and the file contained a well-formedness error that XML requires be detected and reported to the application), then the task that is queued on the networking task source in which the aforementioned problem is found must change the text track readiness state to failed to load and fire an event named error at the track element.

If fetching does not fail, and the file was successfully processed, then the final task that is queued by the networking task source, after it has finished parsing the data, must change the text track readiness state to loaded, and fire an event named load at the track element.

If, while fetching is ongoing, either:

the track URL changes so that it is no longer equal to URL, while the text track mode is set to hidden or showing; or
the text track mode changes to hidden or showing, while the track URL is not equal to URL,

...then the user agent must abort fetching, discarding any pending tasks generated by that algorithm (and in particular, not adding any cues to the text track list of cues after the moment the URL changed), and then queue an element task on the DOM manipulation task source given the track element that first changes the text track readiness state to failed to load and then fires an event named error at the track element.

Wait until the text track readiness state is no longer set to loading.

Wait until the track URL is no longer equal to URL, at the same time as the text track mode is set to hidden or showing.

Jump to the step labeled top.

Whenever a track element has its src attribute set, changed, or removed, the user agent must immediately empty the element's text track's text track list of cues. (This also causes the algorithm above to stop adding cues from the resource being obtained using the previously given URL, if any.)

4.8.11.11.4 Guidelines for exposing cues in various formats as text track cues

How a specific format's text track cues are to be interpreted for the purposes of processing by an HTML user agent is defined by that format. In the absence of such a specification, this section provides some constraints within which implementations can attempt to consistently expose such formats.

To support the text track model of HTML, each unit of timed data is converted to a text track cue. Where the mapping of the format's features to the aspects of a text track cue as defined in this specification are not defined, implementations must ensure that the mapping is consistent with the definitions of the aspects of a text track cue as defined above, as well as with the following constraints:

The text track cue identifier

Should be set to the empty string if the format has no obvious analogue to a per-cue identifier.

The text track cue pause-on-exit flag

Should be set to false.

4.8.11.11.5 Text track API
✔MDN
[Exposed=Window]
interface TextTrackList : EventTarget {
  readonly attribute unsigned long length;
  getter TextTrack (unsigned long index);
  TextTrack? getTrackById(DOMString id);

  attribute EventHandler onchange;
  attribute EventHandler onaddtrack;
  attribute EventHandler onremovetrack;
};
media.textTracks.length
✔MDN

Returns the number of text tracks associated with the media element (e.g. from track elements). This is the number of text tracks in the media element's list of text tracks.

media.textTracks[ n ]

Returns the TextTrack object representing the nth text track in the media element's list of text tracks.

textTrack = media.textTracks.getTrackById(id)
✔MDN

Returns the TextTrack object with the given identifier, or null if no track has that identifier.

A TextTrackList object represents a dynamically updating list of text tracks in a given order.

The textTracks attribute of media elements must return a TextTrackList object representing the TextTrack objects of the text tracks in the media element's list of text tracks, in the same order as in the list of text tracks.

✔MDN

The length attribute of a TextTrackList object must return the number of text tracks in the list represented by the TextTrackList object.

The supported property indices of a TextTrackList object at any instant are the numbers from zero to the number of text tracks in the list represented by the TextTrackList object minus one, if any. If there are no text tracks in the list, there are no supported property indices.

To determine the value of an indexed property of a TextTrackList object for a given index index, the user agent must return the indexth text track in the list represented by the TextTrackList object.

The getTrackById(id) method must return the first TextTrack in the TextTrackList object whose id IDL attribute would return a value equal to the value of the id argument. When no tracks match the given argument, the method must return null.

✔MDN
enum TextTrackMode { "disabled",  "hidden",  "showing" };
enum TextTrackKind { "subtitles",  "captions",  "descriptions",  "chapters",  "metadata" };

[Exposed=Window]
interface TextTrack : EventTarget {
  readonly attribute TextTrackKind kind;
  readonly attribute DOMString label;
  readonly attribute DOMString language;

  readonly attribute DOMString id;
  readonly attribute DOMString inBandMetadataTrackDispatchType;

  attribute TextTrackMode mode;

  readonly attribute TextTrackCueList? cues;
  readonly attribute TextTrackCueList? activeCues;

  undefined addCue(TextTrackCue cue);
  undefined removeCue(TextTrackCue cue);

  attribute EventHandler oncuechange;
};
textTrack = media.addTextTrack(kind [, label [, language ] ])

Creates and returns a new TextTrack object, which is also added to the media element's list of text tracks.

textTrack.kind
✔MDN

Returns the text track kind string.

textTrack.label
✔MDN

Returns the text track label, if there is one, or the empty string otherwise (indicating that a custom label probably needs to be generated from the other attributes of the object if the object is exposed to the user).

textTrack.language
✔MDN

Returns the text track language string.

textTrack.id
✔MDN

Returns the ID of the given track.

For in-band tracks, this is the ID that can be used with a fragment if the format supports media fragment syntax, and that can be used with the getTrackById() method.

For TextTrack objects corresponding to track elements, this is the ID of the track element.

textTrack.inBandMetadataTrackDispatchType
MDN

Returns the text track in-band metadata track dispatch type string.

textTrack.mode [ = value ]
✔MDN

Returns the text track mode, represented by a string from the following list:

"disabled"

The text track disabled mode.

"hidden"

The text track hidden mode.

"showing"

The text track showing mode.

Can be set, to change the mode.

textTrack.cues
✔MDN

Returns the text track list of cues, as a TextTrackCueList object.

textTrack.activeCues
✔MDN

Returns the text track cues from the text track list of cues that are currently active (i.e. that start before the current playback position and end after it), as a TextTrackCueList object.

textTrack.addCue(cue)
✔MDN

Adds the given cue to textTrack's text track list of cues.

textTrack.removeCue(cue)
✔MDN

Removes the given cue from textTrack's text track list of cues.

The addTextTrack(kind, label, language) method of media elements, when invoked, must run the following steps:

Create a new TextTrack object.

Create a new text track corresponding to the new object, and set its text track kind to kind, its text track label to label, its text track language to language, its text track readiness state to the text track loaded state, its text track mode to the text track hidden mode, and its text track list of cues to an empty list.

Initially, the text track list of cues is not associated with any rules for updating the text track rendering. When a text track cue is added to it, the text track list of cues has its rules permanently set accordingly.

Add the new text track to the media element's list of text tracks.

Queue a media element task given the media element to fire an event named addtrack at the media element's textTracks attribute's TextTrackList object, using TrackEvent, with the track attribute initialized to the new text track's TextTrack object.

Return the new TextTrack object.

The kind attribute must return the text track kind of the text track that the TextTrack object represents.

The label attribute must return the text track label of the text track that the TextTrack object represents.

The language attribute must return the text track language of the text track that the TextTrack object represents.

The id attribute returns the track's identifier, if it has one, or the empty string otherwise. For tracks that correspond to track elements, the track's identifier is the value of the element's id attribute, if any. For in-band tracks, the track's identifier is specified by the media resource. If the media resource is in a format that supports media fragment syntax, the identifier returned for a particular track must be the same identifier that would enable the track if used as the name of a track in the track dimension of such a fragment.

The inBandMetadataTrackDispatchType attribute must return the text track in-band metadata track dispatch type of the text track that the TextTrack object represents.

The mode attribute, on getting, must return the string corresponding to the text track mode of the text track that the TextTrack object represents, as defined by the following list:

"disabled"
The text track disabled mode.
"hidden"
The text track hidden mode.
"showing"
The text track showing mode.

On setting, if the new value isn't equal to what the attribute would currently return, the new value must be processed as follows:

If the new value is "disabled"

Set the text track mode of the text track that the TextTrack object represents to the text track disabled mode.

If the new value is "hidden"

Set the text track mode of the text track that the TextTrack object represents to the text track hidden mode.

If the new value is "showing"

Set the text track mode of the text track that the TextTrack object represents to the text track showing mode.

If the text track mode of the text track that the TextTrack object represents is not the text track disabled mode, then the cues attribute must return a live TextTrackCueList object that represents the subset of the text track list of cues of the text track that the TextTrack object represents whose end times occur at or after the earliest possible position when the script started, in text track cue order. Otherwise, it must return null. For each TextTrack object, when an object is returned, the same TextTrackCueList object must be returned each time.

The earliest possible position when the script started is whatever the earliest possible position was the last time the event loop reached step 1.

If the text track mode of the text track that the TextTrack object represents is not the text track disabled mode, then the activeCues attribute must return a live TextTrackCueList object that represents the subset of the text track list of cues of the text track that the TextTrack object represents whose active flag was set when the script started, in text track cue order. Otherwise, it must return null. For each TextTrack object, when an object is returned, the same TextTrackCueList object must be returned each time.

A text track cue's active flag was set when the script started if its text track cue active flag was set the last time the event loop reached step 1.

The addCue(cue) method of TextTrack objects, when invoked, must run the following steps:

If the text track list of cues does not yet have any associated rules for updating the text track rendering, then associate the text track list of cues with the rules for updating the text track rendering appropriate to cue.

If text track list of cues' associated rules for updating the text track rendering are not the same rules for updating the text track rendering as appropriate for cue, then throw an "InvalidStateError" DOMException.

If the given cue is in a text track list of cues, then remove cue from that text track list of cues.

Add cue to the TextTrack object's text track's text track list of cues.

The removeCue(cue) method of TextTrack objects, when invoked, must run the following steps:

If the given cue is not in the TextTrack object's text track's text track list of cues, then throw a "NotFoundError" DOMException.

Remove cue from the TextTrack object's text track's text track list of cues.

In this example, an audio element is used to play a specific sound-effect from a sound file containing many sound effects. A cue is used to pause the audio, so that it ends exactly at the end of the clip, even if the browser is busy running some script. If the page had relied on script to pause the audio, then the start of the next clip might be heard if the browser was not able to run the script at the exact time specified.

var sfx = new Audio('sfx.wav');
var sounds = sfx.addTextTrack('metadata');

// add sounds we care about
function addFX(start, end, name) {
  var cue = new VTTCue(start, end, '');
  cue.id = name;
  cue.pauseOnExit = true;
  sounds.addCue(cue);
}
addFX(12.783, 13.612, 'dog bark');
addFX(13.612, 15.091, 'kitten mew');

function playSound(id) {
  sfx.currentTime = sounds.getCueById(id).startTime;
  sfx.play();
}

// play a bark as soon as we can
sfx.oncanplaythrough = function () {
  playSound('dog bark');
}
// meow when the user tries to leave,
// and have the browser ask them to stay
window.onbeforeunload = function (e) {
  playSound('kitten mew');
  e.preventDefault();
}
✔MDN
[Exposed=Window]
interface TextTrackCueList {
  readonly attribute unsigned long length;
  getter TextTrackCue (unsigned long index);
  TextTrackCue? getCueById(DOMString id);
};
cuelist.length

Returns the number of cues in the list.

cuelist[index]

Returns the text track cue with index index in the list. The cues are sorted in text track cue order.

cuelist.getCueById(id)

Returns the first text track cue (in text track cue order) with text track cue identifier id.

Returns null if none of the cues have the given identifier or if the argument is the empty string.

A TextTrackCueList object represents a dynamically updating list of text track cues in a given order.

✔MDN

The length attribute must return the number of cues in the list represented by the TextTrackCueList object.

The supported property indices of a TextTrackCueList object at any instant are the numbers from zero to the number of cues in the list represented by the TextTrackCueList object minus one, if any. If there are no cues in the list, there are no supported property indices.

To determine the value of an indexed property for a given index index, the user agent must return the indexth text track cue in the list represented by the TextTrackCueList object.

✔MDN

The getCueById(id) method, when called with an argument other than the empty string, must return the first text track cue in the list represented by the TextTrackCueList object whose text track cue identifier is id, if any, or null otherwise. If the argument is the empty string, then the method must return null.

✔MDN
[Exposed=Window]
interface TextTrackCue : EventTarget {
  readonly attribute TextTrack? track;

  attribute DOMString id;
  attribute double startTime;
  attribute unrestricted double endTime;
  attribute boolean pauseOnExit;

  attribute EventHandler onenter;
  attribute EventHandler onexit;
};
cue.track

Returns the TextTrack object to which this text track cue belongs, if any, or null otherwise.

cue.id [ = value ]

Returns the text track cue identifier.

Can be set.

cue.startTime [ = value ]

Returns the text track cue start time, in seconds.

Can be set.

cue.endTime [ = value ]

Returns the text track cue end time, in seconds.

Returns positive Infinity for an unbounded text track cue.

Can be set.

cue.pauseOnExit [ = value ]

Returns true if the text track cue pause-on-exit flag is set, false otherwise.

Can be set.

✔MDN

The track attribute, on getting, must return the TextTrack object of the text track in whose list of cues the text track cue that the TextTrackCue object represents finds itself, if any; or null otherwise.

✔MDN

The id attribute, on getting, must return the text track cue identifier of the text track cue that the TextTrackCue object represents. On setting, the text track cue identifier must be set to the new value.

✔MDN

The startTime attribute, on getting, must return the text track cue start time of the text track cue that the TextTrackCue object represents, in seconds. On setting, the text track cue start time must be set to the new value, interpreted in seconds; then, if the TextTrackCue object's text track cue is in a text track's list of cues, and that text track is in a media element's list of text tracks, and the media element's show poster flag is not set, then run the time marches on steps for that media element.

✔MDN

The endTime attribute, on getting, must return the text track cue end time of the text track cue that the TextTrackCue object represents, in seconds or positive Infinity. On setting, if the new value is negative Infinity or a Not-a-Number (NaN) value, then throw a TypeError exception. Otherwise, the text track cue end time must be set to the new value. Then, if the TextTrackCue object's text track cue is in a text track's list of cues, and that text track is in a media element's list of text tracks, and the media element's show poster flag is not set, then run the time marches on steps for that media element.

✔MDN

The pauseOnExit attribute, on getting, must return true if the text track cue pause-on-exit flag of the text track cue that the TextTrackCue object represents is set; or false otherwise. On setting, the text track cue pause-on-exit flag must be set if the new value is true, and must be unset otherwise.

4.8.11.11.6 Event handlers for objects of the text track APIs

The following are the event handlers that (and their corresponding event handler event types) that must be supported, as event handler IDL attributes, by all objects implementing the TextTrackList interface:

Event handler	Event handler event type
onchange	change
onaddtrack	addtrack
onremovetrack	removetrack

The following are the event handlers that (and their corresponding event handler event types) that must be supported, as event handler IDL attributes, by all objects implementing the TextTrack interface:

Event handler	Event handler event type
oncuechange
✔MDN
	cuechange

The following are the event handlers (and their corresponding event handler event types) that must be supported, as event handler IDL attributes, by all objects implementing the TextTrackCue interface:

Event handler	Event handler event type
onenter
✔MDN
	enter
onexit
✔MDN
	exit
4.8.11.11.7 Best practices for metadata text tracks

This section is non-normative.

Text tracks can be used for storing data relating to the media data, for interactive or augmented views.

For example, a page showing a sports broadcast could include information about the current score. Suppose a robotics competition was being streamed live. The image could be overlaid with the scores, as follows:

In order to make the score display render correctly whenever the user seeks to an arbitrary point in the video, the metadata text track cues need to be as long as is appropriate for the score. For example, in the frame above, there would be maybe one cue that lasts the length of the match that gives the match number, one cue that lasts until the blue alliance's score changes, and one cue that lasts until the red alliance's score changes. If the video is just a stream of the live event, the time in the bottom right would presumably be automatically derived from the current video time, rather than based on a cue. However, if the video was just the highlights, then that might be given in cues also.

The following shows what fragments of this could look like in a WebVTT file:

WEBVTT

...

05:10:00.000 --> 05:12:15.000
matchtype:qual
matchnumber:37

...

05:11:02.251 --> 05:11:17.198
red:78

05:11:03.672 --> 05:11:54.198
blue:66

05:11:17.198 --> 05:11:25.912
red:80

05:11:25.912 --> 05:11:26.522
red:83

05:11:26.522 --> 05:11:26.982
red:86

05:11:26.982 --> 05:11:27.499
red:89

...

The key here is to notice that the information is given in cues that span the length of time to which the relevant event applies. If, instead, the scores were given as zero-length (or very brief, nearly zero-length) cues when the score changes, for example saying "red+2" at 05:11:17.198, "red+3" at 05:11:25.912, etc, problems arise: primarily, seeking is much harder to implement, as the script has to walk the entire list of cues to make sure that no notifications have been missed; but also, if the cues are short it's possible the script will never see that they are active unless it listens to them specifically.

When using cues in this manner, authors are encouraged to use the cuechange event to update the current annotations. (In particular, using the timeupdate event would be less appropriate as it would require doing work even when the cues haven't changed, and, more importantly, would introduce a higher latency between when the metadata cues become active and when the display is updated, since timeupdate events are rate-limited.)

4.8.11.12 Identifying a track kind through a URL

Other specifications or formats that need a URL to identify the return values of the AudioTrack kind or VideoTrack kind IDL attributes, or identify the kind of text track, must use the about:html-kind URL.

4.8.11.13 User interface

The controls attribute is a boolean attribute. If present, it indicates that the author has not provided a scripted controller and would like the user agent to provide its own set of controls.

If the attribute is present, or if scripting is disabled for the media element, then the user agent should expose a user interface to the user. This user interface should include features to begin playback, pause playback, seek to an arbitrary position in the content (if the content supports arbitrary seeking), change the volume, change the display of closed captions or embedded sign-language tracks, select different audio tracks or turn on audio descriptions, and show the media content in manners more suitable to the user (e.g. fullscreen video or in an independent resizable window). Other controls may also be made available.

Even when the attribute is absent, however, user agents may provide controls to affect playback of the media resource (e.g. play, pause, seeking, track selection, and volume controls), but such features should not interfere with the page's normal rendering. For example, such features could be exposed in the media element's context menu, platform media keys, or a remote control. The user agent may implement this simply by exposing a user interface to the user as described above (as if the controls attribute was present).

If the user agent exposes a user interface to the user by displaying controls over the media element, then the user agent should suppress any user interaction events while the user agent is interacting with this interface. (For example, if the user clicks on a video's playback control, mousedown events and so forth would not simultaneously be fired at elements on the page.)

Where possible (specifically, for starting, stopping, pausing, and unpausing playback, for seeking, for changing the rate of playback, for fast-forwarding or rewinding, for listing, enabling, and disabling text tracks, and for muting or changing the volume of the audio), user interface features exposed by the user agent must be implemented in terms of the DOM API described above, so that, e.g., all the same events fire.

Features such as fast-forward or rewind must be implemented by only changing the playbackRate attribute (and not the defaultPlaybackRate attribute).

Seeking must be implemented in terms of seeking to the requested position in the media element's media timeline. For media resources where seeking to an arbitrary position would be slow, user agents are encouraged to use the approximate-for-speed flag when seeking in response to the user manipulating an approximate position interface such as a seek bar.

media.volume [ = value ]
✔MDN

Returns the current playback volume, as a number in the range 0.0 to 1.0, where 0.0 is the quietest and 1.0 the loudest.

Can be set, to change the volume.

Throws an "IndexSizeError" DOMException if the new value is not in the range 0.0 .. 1.0.

media.muted [ = value ]
✔MDN

Returns true if audio is muted, overriding the volume attribute, and false if the volume attribute is being honored.

Can be set, to change whether the audio is muted or not.

A media element has a playback volume, which is a fraction in the range 0.0 (silent) to 1.0 (loudest). Initially, the volume should be 1.0, but user agents may remember the last set value across sessions, on a per-site basis or otherwise, so the volume may start at other values.

The volume IDL attribute must return the playback volume of any audio portions of the media element. On setting, if the new value is in the range 0.0 to 1.0 inclusive, the media element's playback volume must be set to the new value. If the new value is outside the range 0.0 to 1.0 inclusive, then, on setting, an "IndexSizeError" DOMException must be thrown instead.

A media element can also be muted. If anything is muting the element, then it is muted. (For example, when the direction of playback is backwards, the element is muted.)

The muted IDL attribute must return the value to which it was last set. When a media element is created, if the element has a muted content attribute specified, then the muted IDL attribute should be set to true; otherwise, the user agents may set the value to the user's preferred value (e.g. remembering the last set value across sessions, on a per-site basis or otherwise). While the muted IDL attribute is set to true, the media element must be muted.

Whenever either of the values that would be returned by the volume and muted IDL attributes change, the user agent must queue a media element task given the media element to fire an event named volumechange at the media element. Then, if the media element is not allowed to play, the user agent must run the internal pause steps for the media element.

A user agent has an associated volume locked (a boolean). Its value is implementation-defined and determines whether the playback volume takes effect.

An element's effective media volume is determined as follows:

If the user has indicated that the user agent is to override the volume of the element, then return the volume desired by the user.

If the user agent's volume locked is true, then return the system volume.

If the element's audio output is muted, then return zero.

Let volume be the playback volume of the audio portions of the media element, in range 0.0 (silent) to 1.0 (loudest).

Return volume, interpreted relative to the range 0.0 to 1.0, with 0.0 being silent, and 1.0 being the loudest setting, values in between increasing in loudness. The range need not be linear. The loudest setting may be lower than the system's loudest possible setting; for example the user could have set a maximum volume.

The muted content attribute on media elements is a boolean attribute that controls the default state of the audio output of the media resource, potentially overriding user preferences.

This attribute has no dynamic effect (it only controls the default state of the element).

This video (an advertisement) autoplays, but to avoid annoying users, it does so without sound, and allows the user to turn the sound on. The user agent can pause the video if it's unmuted without a user interaction.

<video src="adverts.cgi?kind=video" controls autoplay loop muted></video>
4.8.11.14 Time ranges
✔MDN

Objects implementing the TimeRanges interface represent a list of ranges (periods) of time.

[Exposed=Window]
interface TimeRanges {
  readonly attribute unsigned long length;
  double start(unsigned long index);
  double end(unsigned long index);
};
media.length
✔MDN

Returns the number of ranges in the object.

time = media.start(index)
✔MDN

Returns the time for the start of the range with the given index.

Throws an "IndexSizeError" DOMException if the index is out of range.

time = media.end(index)
✔MDN

Returns the time for the end of the range with the given index.

Throws an "IndexSizeError" DOMException if the index is out of range.

The length IDL attribute must return the number of ranges represented by the object.

The start(index) method must return the position of the start of the indexth range represented by the object, in seconds measured from the start of the timeline that the object covers.

The end(index) method must return the position of the end of the indexth range represented by the object, in seconds measured from the start of the timeline that the object covers.

These methods must throw "IndexSizeError" DOMExceptions if called with an index argument greater than or equal to the number of ranges represented by the object.

When a TimeRanges object is said to be a normalized TimeRanges object, the ranges it represents must obey the following criteria:

The start of a range must be greater than the end of all earlier ranges.
The start of a range must be less than or equal to the end of that same range.

In other words, the ranges in such an object are ordered, don't overlap, and don't touch (adjacent ranges are folded into one bigger range). A range can be empty (referencing just a single moment in time), e.g. to indicate that only one frame is currently buffered in the case that the user agent has discarded the entire media resource except for the current frame, when a media element is paused.

Ranges in a TimeRanges object must be inclusive.

Thus, the end of a range would be equal to the start of a following adjacent (touching but not overlapping) range. Similarly, a range covering a whole timeline anchored at zero would have a start equal to zero and an end equal to the duration of the timeline.

The timelines used by the objects returned by the buffered, seekable, and played IDL attributes of media elements must be that element's media timeline.

4.8.11.15 The TrackEvent interface
✔MDN
[Exposed=Window]
interface TrackEvent : Event {
  constructor(DOMString type, optional TrackEventInit eventInitDict = {});

  readonly attribute (VideoTrack or AudioTrack or TextTrack)? track;
};

dictionary TrackEventInit : EventInit {
  (VideoTrack or AudioTrack or TextTrack)? track = null;
};
event.track
✔MDN

Returns the track object (TextTrack, AudioTrack, or VideoTrack) to which the event relates.

The track attribute must return the value it was initialized to. It represents the context information for the event.

4.8.11.16 Events summary

This section is non-normative.

The following events fire on media elements as part of the processing model described above:

Event name	Interface	Fired when...	Preconditions
loadstart
✔MDN
	Event	The user agent begins looking for media data, as part of the resource selection algorithm.	networkState equals NETWORK_LOADING
progress
✔MDN
	Event	The user agent is fetching media data.	networkState equals NETWORK_LOADING
suspend
✔MDN
	Event	The user agent is intentionally not currently fetching media data.	networkState equals NETWORK_IDLE
abort
✔MDN
	Event	The user agent stops fetching the media data before it is completely downloaded, but not due to an error.	error is an object with the code MEDIA_ERR_ABORTED. networkState equals either NETWORK_EMPTY or NETWORK_IDLE, depending on when the download was aborted.
error
✔MDN
	Event	An error occurs while fetching the media data or the type of the resource is not a supported media format.	error is an object with the code MEDIA_ERR_NETWORK or higher. networkState equals either NETWORK_EMPTY or NETWORK_IDLE, depending on when the download was aborted.
emptied
✔MDN
	Event	A media element whose networkState was previously not in the NETWORK_EMPTY state has just switched to that state (either because of a fatal error during load that's about to be reported, or because the load() method was invoked while the resource selection algorithm was already running).	networkState is NETWORK_EMPTY; all the IDL attributes are in their initial states.
stalled
✔MDN
	Event	The user agent is trying to fetch media data, but data is unexpectedly not forthcoming.	networkState is NETWORK_LOADING.
loadedmetadata
✔MDN
	Event	The user agent has just determined the duration and dimensions of the media resource and the text tracks are ready.	readyState is newly equal to HAVE_METADATA or greater for the first time.
loadeddata
✔MDN
	Event	The user agent can render the media data at the current playback position for the first time.	readyState newly increased to HAVE_CURRENT_DATA or greater for the first time.
canplay
✔MDN
	Event	The user agent can resume playback of the media data, but estimates that if playback were to be started now, the media resource could not be rendered at the current playback rate up to its end without having to stop for further buffering of content.	readyState newly increased to HAVE_FUTURE_DATA or greater.
canplaythrough
✔MDN
	Event	The user agent estimates that if playback were to be started now, the media resource could be rendered at the current playback rate all the way to its end without having to stop for further buffering.	readyState is newly equal to HAVE_ENOUGH_DATA.
playing
✔MDN
	Event	Playback is ready to start after having been paused or delayed due to lack of media data.	readyState is newly greater than or equal to HAVE_FUTURE_DATA and paused is false, or paused is newly false and readyState is greater than or equal to HAVE_FUTURE_DATA. Even if this event fires, the element might still not be potentially playing, e.g. if the element is paused for user interaction or paused for in-band content.
waiting
✔MDN
	Event	Playback has stopped because the next frame is not available, but the user agent expects that frame to become available in due course.	readyState is less than or equal to HAVE_CURRENT_DATA, and paused is false. Either seeking is true, or the current playback position is not contained in any of the ranges in buffered. It is possible for playback to stop for other reasons without paused being false, but those reasons do not fire this event (and when those situations resolve, a separate playing event is not fired either): e.g., playback has ended, or playback stopped due to errors, or the element has paused for user interaction or paused for in-band content.
seeking
✔MDN
	Event	The seeking IDL attribute changed to true, and the user agent has started seeking to a new position.	
seeked
✔MDN
	Event	The seeking IDL attribute changed to false after the current playback position was changed.	
ended
✔MDN
	Event	Playback has stopped because the end of the media resource was reached.	currentTime equals the end of the media resource; ended is true.
durationchange
✔MDN
	Event	The duration attribute has just been updated.	
timeupdate
✔MDN
	Event	The current playback position changed as part of normal playback or in an especially interesting way, for example discontinuously.	
play
✔MDN
	Event	The element is no longer paused. Fired after the play() method has returned, or when the autoplay attribute has caused playback to begin.	paused is newly false.
pause
✔MDN
	Event	The element has been paused. Fired after the pause() method has returned.	paused is newly true.
ratechange
✔MDN
	Event	Either the defaultPlaybackRate or the playbackRate attribute has just been updated.	
resize	Event	One or both of the videoWidth and videoHeight attributes have just been updated.	Media element is a video element; readyState is not HAVE_NOTHING
volumechange
✔MDN
	Event	Either the volume attribute or the muted attribute has changed. Fired after the relevant attribute's setter has returned.	

The following event fires on source elements:

Event name	Interface	Fired when...
error	Event	An error occurs while fetching the media data or the type of the resource is not a supported media format.

The following events fire on AudioTrackList, VideoTrackList, and TextTrackList objects:

Event name	Interface	Fired when...
change
✔MDN
	Event	One or more tracks in the track list have been enabled or disabled.
addtrack
✔MDN
	TrackEvent	A track has been added to the track list.
removetrack
✔MDN
	TrackEvent	A track has been removed from the track list.

The following event fires on TextTrack objects and track elements:

Event name	Interface	Fired when...
cuechange
✔MDN
	Event	One or more cues in the track have become active or stopped being active.

The following events fire on track elements:

Event name	Interface	Fired when...
error	Event	An error occurs while fetching the track data or the type of the resource is not supported text track format.
load	Event	A track data has been fetched and successfully processed.

The following events fire on TextTrackCue objects:

Event name	Interface	Fired when...
enter
✔MDN
	Event	The cue has become active.
exit
✔MDN
	Event	The cue has stopped being active.
4.8.11.17 Security and privacy considerations

The main security and privacy implications of the video and audio elements come from the ability to embed media cross-origin. There are two directions that threats can flow: from hostile content to a victim page, and from a hostile page to victim content.

If a victim page embeds hostile content, the threat is that the content might contain scripted code that attempts to interact with the Document that embeds the content. To avoid this, user agents must ensure that there is no access from the content to the embedding page. In the case of media content that uses DOM concepts, the embedded content must be treated as if it was in its own unrelated top-level traversable.

For instance, if an SVG animation was embedded in a video element, the user agent would not give it access to the DOM of the outer page. From the perspective of scripts in the SVG resource, the SVG file would appear to be in a lone top-level traversable with no parent.

If a hostile page embeds victim content, the threat is that the embedding page could obtain information from the content that it would not otherwise have access to. The API does expose some information: the existence of the media, its type, its duration, its size, and the performance characteristics of its host. Such information is already potentially problematic, but in practice the same information can more or less be obtained using the img element, and so it has been deemed acceptable.

However, significantly more sensitive information could be obtained if the user agent further exposes metadata within the content, such as subtitles. That information is therefore only exposed if the video resource uses CORS. The crossorigin attribute allows authors to enable CORS. [FETCH]

Without this restriction, an attacker could trick a user running within a corporate network into visiting a site that attempts to load a video from a previously leaked location on the corporation's intranet. If such a video included confidential plans for a new product, then being able to read the subtitles would present a serious confidentiality breach.

4.8.11.18 Best practices for authors using media elements

This section is non-normative.

Playing audio and video resources on small devices such as set-top boxes or mobile phones is often constrained by limited hardware resources in the device. For example, a device might only support three simultaneous videos. For this reason, it is a good practice to release resources held by media elements when they are done playing, either by being very careful about removing all references to the element and allowing it to be garbage collected, or, even better, by setting the element's src attribute to an empty string. In cases where srcObject was set, instead set the srcObject to null.

Similarly, when the playback rate is not exactly 1.0, hardware, software, or format limitations can cause video frames to be dropped and audio to be choppy or muted.

4.8.11.19 Best practices for implementers of media elements

This section is non-normative.

How accurately various aspects of the media element API are implemented is considered a quality-of-implementation issue.

For example, when implementing the buffered attribute, how precise an implementation reports the ranges that have been buffered depends on how carefully the user agent inspects the data. Since the API reports ranges as times, but the data is obtained in byte streams, a user agent receiving a variable-bitrate stream might only be able to determine precise times by actually decoding all of the data. User agents aren't required to do this, however; they can instead return estimates (e.g. based on the average bitrate seen so far) which get revised as more information becomes available.

As a general rule, user agents are urged to be conservative rather than optimistic. For example, it would be bad to report that everything had been buffered when it had not.

Another quality-of-implementation issue would be playing a video backwards when the codec is designed only for forward playback (e.g. there aren't many key frames, and they are far apart, and the intervening frames only have deltas from the previous frame). User agents could do a poor job, e.g. only showing key frames; however, better implementations would do more work and thus do a better job, e.g. actually decoding parts of the video forwards, storing the complete frames, and then playing the frames backwards.

Similarly, while implementations are allowed to drop buffered data at any time (there is no requirement that a user agent keep all the media data obtained for the lifetime of the media element), it is again a quality of implementation issue: user agents with sufficient resources to keep all the data around are encouraged to do so, as this allows for a better user experience. For example, if the user is watching a live stream, a user agent could allow the user only to view the live video; however, a better user agent would buffer everything and allow the user to seek through the earlier material, pause it, play it forwards and backwards, etc.

When a media element that is paused is removed from a document and not reinserted before the next time the event loop reaches step 1, implementations that are resource constrained are encouraged to take that opportunity to release all hardware resources (like video planes, networking resources, and data buffers) used by the media element. (User agents still have to keep track of the playback position and so forth, though, in case playback is later restarted.)

← 4.8.5 The iframe element — Table of Contents — 4.8.12 The map element →

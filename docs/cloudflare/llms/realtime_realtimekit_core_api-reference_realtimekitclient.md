# Source: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/realtimekitclient/index.md

---

title: RealtimeKitClient · Cloudflare Realtime docs
lastUpdated: 2026-02-10T18:29:47.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/realtimekitclient/
  md: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/realtimekitclient/index.md
---

[]()

The RealtimeKitClient class is the main class of the web core library. An object of the RealtimeKitClient class can be created using `await RealtimeKitClient.init({ ... })`. Typically, an object of `RealtimeKitClient` is named `meeting`.

* [RealtimeKitClient](#module_RealtimeKitClient)

  * [module.exports](#exp_module_RealtimeKitClient--module.exports) ⏏

    * [new module.exports(context, controller)](#new_module_RealtimeKitClient--module.exports_new)

    * *instance*

      * [.participants](#module_RealtimeKitClient--module.exports+participants)
      * [.self](#module_RealtimeKitClient--module.exports+self)
      * [.meta](#module_RealtimeKitClient--module.exports+meta)
      * [.ai](#module_RealtimeKitClient--module.exports+ai)
      * [.plugins](#module_RealtimeKitClient--module.exports+plugins)
      * [.chat](#module_RealtimeKitClient--module.exports+chat)
      * [.polls](#module_RealtimeKitClient--module.exports+polls)
      * [.connectedMeetings](#module_RealtimeKitClient--module.exports+connectedMeetings)
      * [.**internals**](#module_RealtimeKitClient--module.exports+__internals__)
      * [.join()](#module_RealtimeKitClient--module.exports+join)
      * [.leave()](#module_RealtimeKitClient--module.exports+leave)
      *
      *

    * *static*

      * [.initMedia(\[options\], \[skipAwaits\], \[cachedUserDetails\])](#module_RealtimeKitClient--module.exports.initMedia)
      * [.init(options)](#module_RealtimeKitClient--module.exports.init)
      * [.setupContext(peerId, options, meetingId, args)](#module_RealtimeKitClient--module.exports.setupContext)

[]()

### module.exports ⏏

**Kind**: Exported class\
[]()

#### new module.exports(context, controller)

| Param | Type |
| - | - |
| context | `IContext` |
| controller | `Controller` |

[]()

#### module.exports.participants

The `participants` object consists of 4 maps of participants, `waitlisted`, `joined`, `active`, `pinned`. The maps are indexed by `peerId`s, and the values are the corresponding participant objects.

**Kind**: instance property of [`module.exports`](#exp_module_RealtimeKitClient--module.exports)\
[]()

#### module.exports.self

The `self` object can be used to manipulate audio and video settings, and other configurations for the local participant. This exposes methods to enable and disable media tracks, share the user's screen, etc.

**Kind**: instance property of [`module.exports`](#exp_module_RealtimeKitClient--module.exports)\
[]()

#### module.exports.meta

The `room` object stores information about the current meeting, such as chat messages, polls, room name, etc.

**Kind**: instance property of [`module.exports`](#exp_module_RealtimeKitClient--module.exports)\
[]()

#### module.exports.ai

The `ai` object is used to interface with AI features. You can obtain the live meeting transcript and use other meeting AI features such as summary, and agenda using this object.

**Kind**: instance property of [`module.exports`](#exp_module_RealtimeKitClient--module.exports)\
[]()

#### module.exports.plugins

The `plugins` object stores information about the plugins available in the current meeting. It exposes methods to activate and deactivate them.

**Kind**: instance property of [`module.exports`](#exp_module_RealtimeKitClient--module.exports)\
[]()

#### module.exports.chat

The chat object stores the chat messages that were sent in the meeting. This includes text messages, images, and files.

**Kind**: instance property of [`module.exports`](#exp_module_RealtimeKitClient--module.exports)\
[]()

#### module.exports.polls

The polls object stores the polls that were initiated in the meeting. It exposes methods to create and vote on polls.

**Kind**: instance property of [`module.exports`](#exp_module_RealtimeKitClient--module.exports)\
[]()

#### module.exports.connectedMeetings

The connectedMeetings object stores the connected meetings states. It exposes methods to create/read/update/delete methods for connected meetings.

**Kind**: instance property of [`module.exports`](#exp_module_RealtimeKitClient--module.exports)\
[]()

#### module.exports.\_\_internals\_\_

The **internals** object exposes the internal tools & utilities such as features and logger so that client can utilise the same to build their own feature based UI. Logger (**internals**.logger) can be used to send logs to servers to inform of issues, if any, proactively.

**Kind**: instance property of [`module.exports`](#exp_module_RealtimeKitClient--module.exports)\
[]()

#### module.exports.join()

The `join()` method can be used to join the meeting. A `roomJoined` event is emitted on `self` when the room is joined successfully.

**Kind**: instance method of [`module.exports`](#exp_module_RealtimeKitClient--module.exports)\
[]()

#### module.exports.leave()

The `leave()` method can be used to leave a meeting.

**Kind**: instance method of [`module.exports`](#exp_module_RealtimeKitClient--module.exports)\
[]()

####

***Deprecated***

**Kind**: instance method of [`module.exports`](#exp_module_RealtimeKitClient--module.exports)\
[]()

####

***Deprecated***

**Kind**: instance method of [`module.exports`](#exp_module_RealtimeKitClient--module.exports)

| Param | Type |
| - | - |
| \[state] | `LeaveRoomState` |

[]()

#### module.exports.initMedia(\[options], \[skipAwaits], \[cachedUserDetails])

**Kind**: static method of [`module.exports`](#exp_module_RealtimeKitClient--module.exports)

| Param | Type | Default |
| - | - | - |
| \[options] | `Object` | |
| \[options.video] | `boolean` | |
| \[options.audio] | `boolean` | |
| \[options.constraints] | `MediaConstraints` | |
| \[skipAwaits] | `boolean` | `false` |
| \[cachedUserDetails] | `CachedUserDetails` | |

[]()

#### module.exports.init(options)

The `init` method can be used to instantiate the RealtimeKitClient class. This returns an instance of RealtimeKitClient, which can be used to perform actions on the meeting.

**Kind**: static method of [`module.exports`](#exp_module_RealtimeKitClient--module.exports)

| Param | Description |
| - | - |
| options | The options object. |
| options.authToken | The authorization token received using the API. |
| options.baseURI | The base URL of the API. |
| options.defaults | The default audio and video settings. |

[]()

#### module.exports.setupContext(peerId, options, meetingId, args)

**Kind**: static method of [`module.exports`](#exp_module_RealtimeKitClient--module.exports)

| Param | Type |
| - | - |
| peerId | `string` |
| options | `RealtimeKitClientOptions` |
| meetingId | `string` |
| args | `any` |

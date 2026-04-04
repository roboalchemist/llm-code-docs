# Source: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkparticipant/index.md

---

title: RTKParticipant · Cloudflare Realtime docs
lastUpdated: 2026-02-10T18:29:47.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkparticipant/
  md: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkparticipant/index.md
---

[]()

This module represents a single participant in the meeting. The participant object can be accessed from one of the participant lists present in the `meeting.participants` object. For example,

```ts
const participant1 = meeting.participants.active.get(participantId);
const participant2 = meeting.participants.joined.get(participantId);
const participant3 = meeting.participants.active.toArray()[0];
const participant4 = meeting.participants.active.toArray().filter((p) => p.name === 'John');
```

* [RTKParticipant](#module_RTKParticipant)

  * [module.exports](#exp_module_RTKParticipant--module.exports) ⏏

    * [new module.exports(context, participant, self, roomSocket)](#new_module_RTKParticipant--module.exports_new)
    * [.id](#module_RTKParticipant--module.exports+id)
    * [.userId](#module_RTKParticipant--module.exports+userId)
    * [.name](#module_RTKParticipant--module.exports+name)
    * [.picture](#module_RTKParticipant--module.exports+picture)
    * [.customRTKParticipantId](#module_RTKParticipant--module.exports+customRTKParticipantId)
    *
    * [.device](#module_RTKParticipant--module.exports+device)
    * [.videoTrack](#module_RTKParticipant--module.exports+videoTrack)
    * [.audioTrack](#module_RTKParticipant--module.exports+audioTrack)
    * [.screenShareTracks](#module_RTKParticipant--module.exports+screenShareTracks)
    * [.videoEnabled](#module_RTKParticipant--module.exports+videoEnabled)
    * [.audioEnabled](#module_RTKParticipant--module.exports+audioEnabled)
    * [.screenShareEnabled](#module_RTKParticipant--module.exports+screenShareEnabled)
    * [.producers](#module_RTKParticipant--module.exports+producers)
    * [.manualProducerConfig](#module_RTKParticipant--module.exports+manualProducerConfig)
    * [.supportsRemoteControl](#module_RTKParticipant--module.exports+supportsRemoteControl)
    * [.presetName](#module_RTKParticipant--module.exports+presetName)
    * [.stageStatus](#module_RTKParticipant--module.exports+stageStatus)
    * [.telemetry](#module_RTKParticipant--module.exports+telemetry)
    * [.isPinned](#module_RTKParticipant--module.exports+isPinned)
    * [.setVideoEnabled(videoEnabled, \[emitEvent\])](#module_RTKParticipant--module.exports+setVideoEnabled)
    * [.setAudioEnabled(audioEnabled, \[emitEvent\])](#module_RTKParticipant--module.exports+setAudioEnabled)
    * [.setScreenShareEnabled(screenShareEnabled, \[emitEvent\])](#module_RTKParticipant--module.exports+setScreenShareEnabled)
    * [.pin()](#module_RTKParticipant--module.exports+pin)
    * [.unpin()](#module_RTKParticipant--module.exports+unpin)
    * [.setIsPinned(isPinned, \[emitEvent\])](#module_RTKParticipant--module.exports+setIsPinned)
    * [.disableAudio()](#module_RTKParticipant--module.exports+disableAudio)
    * [.kick()](#module_RTKParticipant--module.exports+kick)
    * [.disableVideo()](#module_RTKParticipant--module.exports+disableVideo)
    * [.registerVideoElement(videoElem)](#module_RTKParticipant--module.exports+registerVideoElement)
    * [.deregisterVideoElement(\[videoElem\])](#module_RTKParticipant--module.exports+deregisterVideoElement)
    * [.updateVideo(e)](#module_RTKParticipant--module.exports+updateVideo)

[]()

### module.exports ⏏

**Kind**: Exported class\
[]()

#### new module.exports(context, participant, self, roomSocket)

| Param | Type |
| - | - |
| context | `Context` |
| participant | `IRTKParticipant` |
| self | `Self` |
| roomSocket | `RoomSocketHandler` |

[]()

#### module.exports.id

The peer ID of the participant. The participants are indexed by this ID in the participant map.

**Kind**: instance property of [`module.exports`](#exp_module_RTKParticipant--module.exports)\
[]()

#### module.exports.userId

The user ID of the participant.

**Kind**: instance property of [`module.exports`](#exp_module_RTKParticipant--module.exports)\
[]()

#### module.exports.name

The name of the participant.

**Kind**: instance property of [`module.exports`](#exp_module_RTKParticipant--module.exports)\
[]()

#### module.exports.picture

The picture of the participant.

**Kind**: instance property of [`module.exports`](#exp_module_RTKParticipant--module.exports)\
[]()

#### module.exports.customRTKParticipantId

The custom id of the participant set during Add RTKParticipant REST API

**Kind**: instance property of [`module.exports`](#exp_module_RTKParticipant--module.exports)\
[]()

####

***Deprecated***

**Kind**: instance property of [`module.exports`](#exp_module_RTKParticipant--module.exports)\
[]()

#### module.exports.device

The device configuration of the participant.

**Kind**: instance property of [`module.exports`](#exp_module_RTKParticipant--module.exports)\
[]()

#### module.exports.videoTrack

The participant's video track.

**Kind**: instance property of [`module.exports`](#exp_module_RTKParticipant--module.exports)\
[]()

#### module.exports.audioTrack

The participant's audio track.

**Kind**: instance property of [`module.exports`](#exp_module_RTKParticipant--module.exports)\
[]()

#### module.exports.screenShareTracks

The participant's screenshare video and audio track.

**Kind**: instance property of [`module.exports`](#exp_module_RTKParticipant--module.exports)\
[]()

#### module.exports.videoEnabled

This is true if the participant's video is enabled.

**Kind**: instance property of [`module.exports`](#exp_module_RTKParticipant--module.exports)\
[]()

#### module.exports.audioEnabled

This is true if the participant's audio is enabled.

**Kind**: instance property of [`module.exports`](#exp_module_RTKParticipant--module.exports)\
[]()

#### module.exports.screenShareEnabled

This is true if the participant is screensharing.

**Kind**: instance property of [`module.exports`](#exp_module_RTKParticipant--module.exports)\
[]()

#### module.exports.producers

producers created by participant

**Kind**: instance property of [`module.exports`](#exp_module_RTKParticipant--module.exports)\
[]()

#### module.exports.manualProducerConfig

producer config passed during manual subscription

**Kind**: instance property of [`module.exports`](#exp_module_RTKParticipant--module.exports)\
[]()

#### module.exports.supportsRemoteControl

This is true if the participant supports remote control.

**Kind**: instance property of [`module.exports`](#exp_module_RTKParticipant--module.exports)\
[]()

#### module.exports.presetName

The preset of the participant.

**Kind**: instance property of [`module.exports`](#exp_module_RTKParticipant--module.exports)\
[]()

#### module.exports.stageStatus

Denotes the participants's current stage status.

**Kind**: instance property of [`module.exports`](#exp_module_RTKParticipant--module.exports)\
[]()

#### module.exports.telemetry

**Kind**: instance property of [`module.exports`](#exp_module_RTKParticipant--module.exports)\
[]()

#### module.exports.isPinned

Returns true if the participant is pinned.

**Kind**: instance property of [`module.exports`](#exp_module_RTKParticipant--module.exports)\
[]()

#### module.exports.setVideoEnabled(videoEnabled, \[emitEvent])

**Kind**: instance method of [`module.exports`](#exp_module_RTKParticipant--module.exports)

| Param | Type | Default |
| - | - | - |
| videoEnabled | `boolean` | |
| \[emitEvent] | `boolean` | `true` |

[]()

#### module.exports.setAudioEnabled(audioEnabled, \[emitEvent])

**Kind**: instance method of [`module.exports`](#exp_module_RTKParticipant--module.exports)

| Param | Type | Default |
| - | - | - |
| audioEnabled | `boolean` | |
| \[emitEvent] | `boolean` | `true` |

[]()

#### module.exports.setScreenShareEnabled(screenShareEnabled, \[emitEvent])

**Kind**: instance method of [`module.exports`](#exp_module_RTKParticipant--module.exports)

| Param | Type | Default |
| - | - | - |
| screenShareEnabled | `boolean` | |
| \[emitEvent] | `boolean` | `true` |

[]()

#### module.exports.pin()

Returns `participant.id` if user has permission to pin participants.

**Kind**: instance method of [`module.exports`](#exp_module_RTKParticipant--module.exports)\
[]()

#### module.exports.unpin()

Returns `participant.id` if user has permission to unpin participants.

**Kind**: instance method of [`module.exports`](#exp_module_RTKParticipant--module.exports)\
[]()

#### module.exports.setIsPinned(isPinned, \[emitEvent])

**Kind**: instance method of [`module.exports`](#exp_module_RTKParticipant--module.exports)

| Param | Type | Default |
| - | - | - |
| isPinned | `boolean` | |
| \[emitEvent] | `boolean` | `true` |

[]()

#### module.exports.disableAudio()

Disables audio for this participant. Requires the permission to disable participant audio.

**Kind**: instance method of [`module.exports`](#exp_module_RTKParticipant--module.exports)\
[]()

#### module.exports.kick()

Kicks this participant from the meeting. Requires the permission to kick a participant.

**Kind**: instance method of [`module.exports`](#exp_module_RTKParticipant--module.exports)\
[]()

#### module.exports.disableVideo()

Disables video for this participant. Requires the permission to disable video for a participant.

**Kind**: instance method of [`module.exports`](#exp_module_RTKParticipant--module.exports)\
[]()

#### module.exports.registerVideoElement(videoElem)

**Kind**: instance method of [`module.exports`](#exp_module_RTKParticipant--module.exports)

| Param | Type |
| - | - |
| videoElem | `HTMLVideoElement` |

[]()

#### module.exports.deregisterVideoElement(\[videoElem])

**Kind**: instance method of [`module.exports`](#exp_module_RTKParticipant--module.exports)

| Param | Type |
| - | - |
| \[videoElem] | `HTMLVideoElement` |

[]()

#### module.exports.updateVideo(e)

Internal method, do not use

**Kind**: instance method of [`module.exports`](#exp_module_RTKParticipant--module.exports)

| Param | Type |
| - | - |
| e | `HTMLVideoElement` |

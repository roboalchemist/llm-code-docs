# Source: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkstage/index.md

---

title: RTKStage · Cloudflare Realtime docs
lastUpdated: 2026-02-10T18:29:47.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkstage/
  md: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkstage/index.md
---

[]()

The RTKStage module represents a class to mange the RTKStage of the meeting RTKStage refers to a virtual area, where participants stream are visible to other participants. When a participant is off stage, they are not producing media but only consuming media from participants who are on RTKStage

* [RTKStage](#module_RTKStage)

  * [module.exports](#exp_module_RTKStage--module.exports) ⏏

    * [new module.exports(context, self, participants, stageSocketHandler, roomSocketHandler)](#new_module_RTKStage--module.exports_new)
    * [.telemetry](#module_RTKStage--module.exports+telemetry)
    * [.peerId](#module_RTKStage--module.exports+peerId)
    * [.getAccessRequests()](#module_RTKStage--module.exports+getAccessRequests)
    * [.requestAccess()](#module_RTKStage--module.exports+requestAccess)
    * [.cancelRequestAccess()](#module_RTKStage--module.exports+cancelRequestAccess)
    * [.grantAccess()](#module_RTKStage--module.exports+grantAccess)
    * [.denyAccess()](#module_RTKStage--module.exports+denyAccess)
    * [.join()](#module_RTKStage--module.exports+join)
    * [.leave()](#module_RTKStage--module.exports+leave)
    * [.kick(userIds)](#module_RTKStage--module.exports+kick)

[]()

### module.exports ⏏

**Kind**: Exported class\
[]()

#### new module.exports(context, self, participants, stageSocketHandler, roomSocketHandler)

| Param | Type |
| - | - |
| context | `Context` |
| self | `Self` |
| participants | `Participants` |
| stageSocketHandler | `RTKStageSocketHandler` |
| roomSocketHandler | `RoomSocketHandler` |

[]()

#### module.exports.telemetry

**Kind**: instance property of [`module.exports`](#exp_module_RTKStage--module.exports)\
[]()

#### module.exports.peerId

Returns the peerId of the current user

**Kind**: instance property of [`module.exports`](#exp_module_RTKStage--module.exports)\
[]()

#### module.exports.getAccessRequests()

Method to fetch all RTKStage access requests from viewers

**Kind**: instance method of [`module.exports`](#exp_module_RTKStage--module.exports)\
[]()

#### module.exports.requestAccess()

Method to send a request to privileged users to join the stage

**Kind**: instance method of [`module.exports`](#exp_module_RTKStage--module.exports)\
[]()

#### module.exports.cancelRequestAccess()

Method to cancel a previous RTKStage join request

**Kind**: instance method of [`module.exports`](#exp_module_RTKStage--module.exports)\
[]()

#### module.exports.grantAccess()

Method to grant access to RTKStage. This can be in response to a RTKStage Join request but it can be called on other users as well

`permissions.acceptRTKStageRequests` privilege required

**Kind**: instance method of [`module.exports`](#exp_module_RTKStage--module.exports)\
[]()

#### module.exports.denyAccess()

Method to deny access to RTKStage. This should be called in response to a RTKStage Join request

**Kind**: instance method of [`module.exports`](#exp_module_RTKStage--module.exports)\
[]()

#### module.exports.join()

Method to join the stage Users either need to have the permission in the preset or must be accepted by a priveleged user to call this method

**Kind**: instance method of [`module.exports`](#exp_module_RTKStage--module.exports)\
[]()

#### module.exports.leave()

Method to leave the stage Users must either be on the stage already or be accepted to join the stage to call this method

**Kind**: instance method of [`module.exports`](#exp_module_RTKStage--module.exports)\
[]()

#### module.exports.kick(userIds)

Method to kick a user off the stage

`permissions.acceptRTKStageRequests` privilege required

**Kind**: instance method of [`module.exports`](#exp_module_RTKStage--module.exports)

| Param | Type |
| - | - |
| userIds | `Array.<string>` |

# Source: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkmeta/index.md

---

title: RTKMeta · Cloudflare Realtime docs
lastUpdated: 2026-02-10T18:29:47.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkmeta/
  md: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkmeta/index.md
---

[]()

This consists of the metadata of the meeting, such as the room name and the title.

* [RTKMeta](#module_RTKMeta)

  * [module.exports](#exp_module_RTKMeta--module.exports) ⏏

    * [new module.exports(context, self, viewType, roomSocketHandler, meetingTitle)](#new_module_RTKMeta--module.exports_new)
    * [.selfActiveTab](#module_RTKMeta--module.exports+selfActiveTab)
    * [.broadcastTabChanges](#module_RTKMeta--module.exports+broadcastTabChanges)
    * [.viewType](#module_RTKMeta--module.exports+viewType)
    * [.meetingStartedTimestamp](#module_RTKMeta--module.exports+meetingStartedTimestamp)
    * [.meetingTitle](#module_RTKMeta--module.exports+meetingTitle)
    * [.sessionId](#module_RTKMeta--module.exports+sessionId)
    * [.meetingId](#module_RTKMeta--module.exports+meetingId)
    * [.setBroadcastTabChanges(broadcastTabChanges)](#module_RTKMeta--module.exports+setBroadcastTabChanges)
    * [.setSelfActiveTab(spotlightTab, tabChangeSource)](#module_RTKMeta--module.exports+setSelfActiveTab)

[]()

### module.exports ⏏

**Kind**: Exported class\
[]()

#### new module.exports(context, self, viewType, roomSocketHandler, meetingTitle)

| Param | Type |
| - | - |
| context | `Context` |
| self | `Self` |
| viewType | `string` |
| roomSocketHandler | `RoomSocketHandler` |
| meetingTitle | `string` |

[]()

#### module.exports.selfActiveTab

Represents the current active tab

**Kind**: instance property of [`module.exports`](#exp_module_RTKMeta--module.exports)\
[]()

#### module.exports.broadcastTabChanges

Represents whether current user is spotlighted

**Kind**: instance property of [`module.exports`](#exp_module_RTKMeta--module.exports)\
[]()

#### module.exports.viewType

The `viewType` tells the type of the meeting possible values are: GROUP\_CALL| LIVESTREAM | CHAT | AUDIO\_ROOM

**Kind**: instance property of [`module.exports`](#exp_module_RTKMeta--module.exports)\
[]()

#### module.exports.meetingStartedTimestamp

The timestamp of the time when the meeting started.

**Kind**: instance property of [`module.exports`](#exp_module_RTKMeta--module.exports)\
[]()

#### module.exports.meetingTitle

The title of the meeting.

**Kind**: instance property of [`module.exports`](#exp_module_RTKMeta--module.exports)\
[]()

#### module.exports.sessionId

(Experimental) The sessionId this meeting object is part of.

**Kind**: instance property of [`module.exports`](#exp_module_RTKMeta--module.exports)\
[]()

#### module.exports.meetingId

The room name of the meeting.

**Kind**: instance property of [`module.exports`](#exp_module_RTKMeta--module.exports)\
[]()

#### module.exports.setBroadcastTabChanges(broadcastTabChanges)

Sets current user as broadcasting tab changes

**Kind**: instance method of [`module.exports`](#exp_module_RTKMeta--module.exports)

| Param | Type |
| - | - |
| broadcastTabChanges | `boolean` |

[]()

#### module.exports.setSelfActiveTab(spotlightTab, tabChangeSource)

Sets current active tab for user

**Kind**: instance method of [`module.exports`](#exp_module_RTKMeta--module.exports)

| Param | Type |
| - | - |
| spotlightTab | `ActiveTab` |
| tabChangeSource | `TabChangeSource` |

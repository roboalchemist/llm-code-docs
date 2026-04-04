# Source: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkconnectedmeetings/index.md

---

title: RTKConnectedMeetings · Cloudflare Realtime docs
lastUpdated: 2026-02-10T18:29:47.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkconnectedmeetings/
  md: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkconnectedmeetings/index.md
---

[]()

This consists of the methods to faciliate connected meetings

* [RTKConnectedMeetings](#module_RTKConnectedMeetings)

  * [module.exports](#exp_module_RTKConnectedMeetings--module.exports) ⏏

    * [new module.exports(context)](#new_module_RTKConnectedMeetings--module.exports_new)
    * [.getRTKConnectedMeetings()](#module_RTKConnectedMeetings--module.exports+getRTKConnectedMeetings)
    * [.createMeetings(request)](#module_RTKConnectedMeetings--module.exports+createMeetings)
    * [.updateMeetings(request)](#module_RTKConnectedMeetings--module.exports+updateMeetings)
    * [.deleteMeetings(meetingIds)](#module_RTKConnectedMeetings--module.exports+deleteMeetings)
    * [.moveParticipants(sourceMeetingId, destinationMeetingId, participantIds)](#module_RTKConnectedMeetings--module.exports+moveParticipants)
    * [.moveParticipantsWithCustomPreset(sourceMeetingId, destinationMeetingId, participants)](#module_RTKConnectedMeetings--module.exports+moveParticipantsWithCustomPreset)

[]()

### module.exports ⏏

**Kind**: Exported class\
[]()

#### new module.exports(context)

| Param | Type |
| - | - |
| context | `Context` |

[]()

#### module.exports.getRTKConnectedMeetings()

get connected meeting state

**Kind**: instance method of [`module.exports`](#exp_module_RTKConnectedMeetings--module.exports)\
[]()

#### module.exports.createMeetings(request)

create connected meetings

**Kind**: instance method of [`module.exports`](#exp_module_RTKConnectedMeetings--module.exports)

| Param | Type |
| - | - |
| request | `Array.<{title: string}>` |

[]()

#### module.exports.updateMeetings(request)

update meeting title

**Kind**: instance method of [`module.exports`](#exp_module_RTKConnectedMeetings--module.exports)

| Param | Type |
| - | - |
| request | `Array.<{id: string, title: string}>` |

[]()

#### module.exports.deleteMeetings(meetingIds)

delete connected meetings

**Kind**: instance method of [`module.exports`](#exp_module_RTKConnectedMeetings--module.exports)

| Param | Type |
| - | - |
| meetingIds | `Array.<string>` |

[]()

#### module.exports.moveParticipants(sourceMeetingId, destinationMeetingId, participantIds)

Trigger event to move participants

**Kind**: instance method of [`module.exports`](#exp_module_RTKConnectedMeetings--module.exports)

| Param | Type | Description |
| - | - | - |
| sourceMeetingId | `string` | id of source meeting |
| destinationMeetingId | `string` | id of destination meeting |
| participantIds | `Array.<string>` | list of id of the participants |

[]()

#### module.exports.moveParticipantsWithCustomPreset(sourceMeetingId, destinationMeetingId, participants)

Trigger event to move participants with custom preset

**Kind**: instance method of [`module.exports`](#exp_module_RTKConnectedMeetings--module.exports)

| Param | Type | Description |
| - | - | - |
| sourceMeetingId | `string` | id of source meeting |
| destinationMeetingId | `string` | id of destination meeting |
| participants | `Array.<{id: string, presetId: string}>` | |

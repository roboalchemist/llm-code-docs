# Source: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkparticipantmap/index.md

---

title: RTKParticipantMap · Cloudflare Realtime docs
lastUpdated: 2026-02-10T18:29:47.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkparticipantmap/
  md: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkparticipantmap/index.md
---

[]()

This is a map of participants, indexed by `participant.id` (a participant's peer ID). This map emits an event whenever a participant present in the map emits an event. For example, when a participant is added to this map, a `participantJoined` event is emitted from the map. When a participant object emits an event `videoUpdate`, the map re-emits that event (provided the participant is present in the map).

* [RTKParticipantMap](#module_RTKParticipantMap)

  * [module.exports](#exp_module_RTKParticipantMap--module.exports) ⏏

    * [new module.exports(logger, \[options\])](#new_module_RTKParticipantMap--module.exports_new)
    * [.add(participant, \[emitEvent\])](#module_RTKParticipantMap--module.exports+add)
    * [.clear(\[emitEvent\], \[removeListeners\])](#module_RTKParticipantMap--module.exports+clear)
    * [.delete(participantId, \[emitEvent\], \[removeListeners\])](#module_RTKParticipantMap--module.exports+delete)

[]()

### module.exports ⏏

**Kind**: Exported class\
[]()

#### new module.exports(logger, \[options])

| Param | Type |
| - | - |
| logger | `Logger` |
| \[options] | `MapEvents` |

[]()

#### module.exports.add(participant, \[emitEvent])

**Kind**: instance method of [`module.exports`](#exp_module_RTKParticipantMap--module.exports)

| Param | Type | Default |
| - | - | - |
| participant | `T` | |
| \[emitEvent] | `boolean` | `true` |

[]()

#### module.exports.clear(\[emitEvent], \[removeListeners])

**Kind**: instance method of [`module.exports`](#exp_module_RTKParticipantMap--module.exports)

| Param | Type | Default |
| - | - | - |
| \[emitEvent] | `boolean` | `true` |
| \[removeListeners] | `boolean` | `false` |

[]()

#### module.exports.delete(participantId, \[emitEvent], \[removeListeners])

**Kind**: instance method of [`module.exports`](#exp_module_RTKParticipantMap--module.exports)

| Param | Type | Default |
| - | - | - |
| participantId | `string` | |
| \[emitEvent] | `boolean` | `true` |
| \[removeListeners] | `boolean` | `false` |

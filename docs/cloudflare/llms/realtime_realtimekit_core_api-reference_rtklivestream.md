# Source: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtklivestream/index.md

---

title: RTKLivestream · Cloudflare Realtime docs
lastUpdated: 2026-02-10T18:29:47.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtklivestream/
  md: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtklivestream/index.md
---

[]()

The RTKLivestream module represents the state of the current livestream, and allows to start/stop live streams.

* [RTKLivestream](#module_RTKLivestream)

  * [module.exports](#exp_module_RTKLivestream--module.exports) ⏏

    * [new module.exports(context, self)](#new_module_RTKLivestream--module.exports_new)
    * [.telemetry](#module_RTKLivestream--module.exports+telemetry)
    * [.setRTKLivestreamState(livestreamState)](#module_RTKLivestream--module.exports+setRTKLivestreamState)
    * [.start(\[livestreamConfig\])](#module_RTKLivestream--module.exports+start)
    * [.stop()](#module_RTKLivestream--module.exports+stop)

[]()

### module.exports ⏏

**Kind**: Exported class\
[]()

#### new module.exports(context, self)

| Param | Type |
| - | - |
| context | `Context` |
| self | `Self` |

[]()

#### module.exports.telemetry

**Kind**: instance property of [`module.exports`](#exp_module_RTKLivestream--module.exports)\
[]()

#### module.exports.setRTKLivestreamState(livestreamState)

**Kind**: instance method of [`module.exports`](#exp_module_RTKLivestream--module.exports)

| Param | Type |
| - | - |
| livestreamState | `RTKLivestreamState` |

[]()

#### module.exports.start(\[livestreamConfig])

Starts livestreaming the meeting.

**Kind**: instance method of [`module.exports`](#exp_module_RTKLivestream--module.exports)

| Param | Type |
| - | - |
| \[livestreamConfig] | `StartRTKLivestreamConfig` |

[]()

#### module.exports.stop()

Stops livestreaming the meeting.

**Kind**: instance method of [`module.exports`](#exp_module_RTKLivestream--module.exports)

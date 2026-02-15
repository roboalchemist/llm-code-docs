# Source: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkplugins/index.md

---

title: RTKPlugins · Cloudflare Realtime docs
lastUpdated: 2026-02-10T18:29:47.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkplugins/
  md: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkplugins/index.md
---

[]()

The RTKPlugins module consists of all the plugins in the meeting. It has 2 maps:

* `all`: Consists of all the plugins in the meeting.
* `active`: Consists of the plugins that are currently in use.

* [RTKPlugins](#module_RTKPlugins)

  * [module.exports](#exp_module_RTKPlugins--module.exports) ⏏

    * [new module.exports(logger)](#new_module_RTKPlugins--module.exports_new)
    * [.all](#module_RTKPlugins--module.exports+all)
    * [.active](#module_RTKPlugins--module.exports+active)

[]()

### module.exports ⏏

**Kind**: Exported class\
[]()

#### new module.exports(logger)

| Param | Type |
| - | - |
| logger | `Logger` |

[]()

#### module.exports.all

All plugins accessible by the current user.

**Kind**: instance property of [`module.exports`](#exp_module_RTKPlugins--module.exports)\
[]()

#### module.exports.active

All plugins that are currently enabled in the room.

**Kind**: instance property of [`module.exports`](#exp_module_RTKPlugins--module.exports)

# Source: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkthemepreset/index.md

---

title: RTKThemePreset · Cloudflare Realtime docs
lastUpdated: 2026-02-10T18:29:47.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkthemepreset/
  md: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkthemepreset/index.md
---

[]()

The RTKThemePreset class represents the meeting theme for the current participant

* [RTKThemePreset](#module_RTKThemePreset)

  * [module.exports](#exp_module_RTKThemePreset--module.exports) ⏏

    * [new module.exports(preset)](#new_module_RTKThemePreset--module.exports_new)

    * *instance*

      *
      *
      *
      *
      *
      * [.viewType](#module_RTKThemePreset--module.exports+viewType)
      * [.livestreamViewerQualities](#module_RTKThemePreset--module.exports+livestreamViewerQualities)
      * [.maxVideoStreams](#module_RTKThemePreset--module.exports+maxVideoStreams)
      * [.maxScreenShareCount](#module_RTKThemePreset--module.exports+maxScreenShareCount)
      *
      * [.disabledPlugins](#module_RTKThemePreset--module.exports+disabledPlugins)

    * *static*

      * [.fromResponse(preset)](#module_RTKThemePreset--module.exports.fromResponse)
      * [.default()](#module_RTKThemePreset--module.exports.default)
      * [.init(\[preset\], \[useDefault\])](#module_RTKThemePreset--module.exports.init)

[]()

### module.exports ⏏

**Kind**: Exported class\
[]()

#### new module.exports(preset)

| Param | Type |
| - | - |
| preset | `PresetV2CamelCased` |

[]()

####

***Deprecated***

**Kind**: instance property of [`module.exports`](#exp_module_RTKThemePreset--module.exports)\
[]()

####

***Deprecated***

**Kind**: instance property of [`module.exports`](#exp_module_RTKThemePreset--module.exports)\
[]()

####

***Deprecated***

**Kind**: instance property of [`module.exports`](#exp_module_RTKThemePreset--module.exports)\
[]()

####

***Deprecated***

**Kind**: instance property of [`module.exports`](#exp_module_RTKThemePreset--module.exports)\
[]()

####

***Deprecated***

**Kind**: instance property of [`module.exports`](#exp_module_RTKThemePreset--module.exports)\
[]()

#### module.exports.viewType

The `viewType` tells the type of the meeting possible values are: GROUP\_CALL| LIVESTREAM | CHAT | AUDIO\_ROOM

**Kind**: instance property of [`module.exports`](#exp_module_RTKThemePreset--module.exports)\
[]()

#### module.exports.livestreamViewerQualities

The `livestreamViewerQualities` specifies the allowed qualities of a stream, that can be viewed by a livestream viewer

**Kind**: instance property of [`module.exports`](#exp_module_RTKThemePreset--module.exports)\
[]()

#### module.exports.maxVideoStreams

The `maxVideoStreams` contains the maximum video streams for mobile and desktop

**Kind**: instance property of [`module.exports`](#exp_module_RTKThemePreset--module.exports)\
[]()

#### module.exports.maxScreenShareCount

The `maxScreenShareCount` contains the maximum possible concurrent screen shares

**Kind**: instance property of [`module.exports`](#exp_module_RTKThemePreset--module.exports)\
[]()

####

***Deprecated***

**Kind**: instance property of [`module.exports`](#exp_module_RTKThemePreset--module.exports)\
[]()

#### module.exports.disabledPlugins

The `disabledPlugins` property returns id of all disabled plugins

**Kind**: instance property of [`module.exports`](#exp_module_RTKThemePreset--module.exports)\
[]()

#### module.exports.fromResponse(preset)

**Kind**: static method of [`module.exports`](#exp_module_RTKThemePreset--module.exports)\
**Deprecated.**: Use init()

| Param | Type |
| - | - |
| preset | `PresetV2CamelCased` |

[]()

#### module.exports.default()

**Kind**: static method of [`module.exports`](#exp_module_RTKThemePreset--module.exports)\
**Deprecated.**: Use init()\
[]()

#### module.exports.init(\[preset], \[useDefault])

**Kind**: static method of [`module.exports`](#exp_module_RTKThemePreset--module.exports)

| Param | Type | Default |
| - | - | - |
| \[preset] | `PresetV2CamelCased` | |
| \[useDefault] | `boolean` | `true` |

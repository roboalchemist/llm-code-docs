# Source: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkplugin/index.md

---

title: RTKPlugin · Cloudflare Realtime docs
lastUpdated: 2026-02-10T18:29:47.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkplugin/
  md: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkplugin/index.md
---

[]()

The RTKPlugin module represents a single plugin in the meeting. A plugin can be obtained from one of the plugin arrays in `meeting.plugins`. For example,

```ts
const plugin1 = meeting.plugins.active.get(pluginId);
const plugin2 = meeting.plugins.all.get(pluginId);
```

* [RTKPlugin](#module_RTKPlugin)

  * [module.exports](#exp_module_RTKPlugin--module.exports) ⏏

    * [new module.exports(context, plugin, pluginSocketHandler, self, participants, chat, meetingTitle)](#new_module_RTKPlugin--module.exports_new)
    * [.telemetry](#module_RTKPlugin--module.exports+telemetry)
    * [.sendIframeEvent(message)](#module_RTKPlugin--module.exports+sendIframeEvent)
    * [.handleIframeMessage(iframeMessage)](#module_RTKPlugin--module.exports+handleIframeMessage)
    * [.sendData(payload)](#module_RTKPlugin--module.exports+sendData)
    * [.removeRTKPluginView(viewId)](#module_RTKPlugin--module.exports+removeRTKPluginView)
    * [.addRTKPluginView(iframe, viewId)](#module_RTKPlugin--module.exports+addRTKPluginView)
    * [.setActive(active)](#module_RTKPlugin--module.exports+setActive)
    * [.activateForSelf()](#module_RTKPlugin--module.exports+activateForSelf)
    * [.deactivateForSelf()](#module_RTKPlugin--module.exports+deactivateForSelf)
    *
    *
    * [.activate()](#module_RTKPlugin--module.exports+activate)
    * [.deactivate()](#module_RTKPlugin--module.exports+deactivate)

[]()

### module.exports ⏏

**Kind**: Exported class\
[]()

#### new module.exports(context, plugin, pluginSocketHandler, self, participants, chat, meetingTitle)

| Param | Type |
| - | - |
| context | `Context` |
| plugin | `RTKPluginResponse` |
| pluginSocketHandler | `RTKPluginSocketHandler` |
| self | `Self` |
| participants | `Participants` |
| chat | `Chat` |
| meetingTitle | `string` |

[]()

#### module.exports.telemetry

**Kind**: instance property of [`module.exports`](#exp_module_RTKPlugin--module.exports)\
[]()

#### module.exports.sendIframeEvent(message)

**Kind**: instance method of [`module.exports`](#exp_module_RTKPlugin--module.exports)

| Param | Type | Description |
| - | - | - |
| message | `RTKPluginIframeMessage` | Socket message forwarded to this plugin. |

[]()

#### module.exports.handleIframeMessage(iframeMessage)

**Kind**: instance method of [`module.exports`](#exp_module_RTKPlugin--module.exports)

| Param | Type |
| - | - |
| iframeMessage | `RTKPluginIframeMessage` |

[]()

#### module.exports.sendData(payload)

This method is used to send arbitrary data to the plugin.

**Kind**: instance method of [`module.exports`](#exp_module_RTKPlugin--module.exports)

| Param | Type | Description |
| - | - | - |
| payload | `SendDataOptions` | The payload that you want to send inside the plugin. |
| payload.eventName | `string` | Name of the event. This is used to listen for the event in plugin SDK. |
| payload.data | `any` | Data you wish to emit. It can assume any data type. |

[]()

#### module.exports.removeRTKPluginView(viewId)

This method is used for cleaning up event listeners attached to an iframe. It must be used before the iframe is removed from the DOM.

**Kind**: instance method of [`module.exports`](#exp_module_RTKPlugin--module.exports)

| Param | Type | Default | Description |
| - | - | - | - |
| viewId | `string` | `"default"` | ID of the view corresponding to this iframe. Default is 'default'. |

[]()

#### module.exports.addRTKPluginView(iframe, viewId)

This method adds the communcation layer between the plugin inside the iframe and the core application (meeting object) in the main window.

**Kind**: instance method of [`module.exports`](#exp_module_RTKPlugin--module.exports)

| Param | Type | Default | Description |
| - | - | - | - |
| iframe | `HTMLIFrameElement` \| `ReactNativeWebView` | | Iframe element to display this plugin. |
| viewId | `string` | `"default"` | ID of the view corresponding to this iframe. Default is 'default'. |

[]()

#### module.exports.setActive(active)

**Kind**: instance method of [`module.exports`](#exp_module_RTKPlugin--module.exports)

| Param | Type |
| - | - |
| active | `boolean` |

[]()

#### module.exports.activateForSelf()

**Kind**: instance method of [`module.exports`](#exp_module_RTKPlugin--module.exports)\
[]()

#### module.exports.deactivateForSelf()

**Kind**: instance method of [`module.exports`](#exp_module_RTKPlugin--module.exports)\
[]()

####

***Deprecated***

**Kind**: instance method of [`module.exports`](#exp_module_RTKPlugin--module.exports)\
[]()

####

***Deprecated***

**Kind**: instance method of [`module.exports`](#exp_module_RTKPlugin--module.exports)\
[]()

#### module.exports.activate()

Activate this plugin for all participants.

**Kind**: instance method of [`module.exports`](#exp_module_RTKPlugin--module.exports)\
[]()

#### module.exports.deactivate()

Deactivate this plugin for all participants.

**Kind**: instance method of [`module.exports`](#exp_module_RTKPlugin--module.exports)

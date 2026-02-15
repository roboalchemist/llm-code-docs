# Source: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkpip/index.md

---

title: RTKPip · Cloudflare Realtime docs
lastUpdated: 2026-02-10T18:29:47.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkpip/
  md: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkpip/index.md
---

## Functions

* [getInitials()](#getInitials)

  Code from ui-kit. Same method used in the avatar component

* [\_init(context, self)](#_init)

* [init(\[options\])](#init)

  Initialize PiP and prepare sources

* [disableSource(source)](#disableSource)

* [addSource(id, element, enabled, \[displayText\])](#addSource)

  Add a video source from the participant grid

* [updateSource(id, source)](#updateSource)

  Update a video source

* [removeSource(id)](#removeSource)

  Remove the video source for the participant

* [removePinnedSource(id)](#removePinnedSource)

  Remove the pinned source

* [removeAllSources()](#removeAllSources)

  Remove all sources

* [enable()](#enable)

  Enable PiP

[]()

Code from ui-kit. Same method used in the avatar component

**Kind**: global function\
[]()

**Kind**: global function

| Param | Type |
| - | - |
| context | `Context` |
| self | `Self` |

[]()

Initialize PiP and prepare sources

**Kind**: global function

| Param | Type |
| - | - |
| \[options] | `Object` |
| \[options.height] | `number` |
| \[options.width] | `number` |

[]()

**Kind**: global function

| Param | Type |
| - | - |
| source | `string` |

[]()

Add a video source from the participant grid

**Kind**: global function

| Param | Type | Description |
| - | - | - |
| id | `string` | id for the source (ex. participant id) |
| element | `HTMLVideoElement` | HTMLVideoElement for the video source |
| enabled | `boolean` | if source is enabled |
| \[displayText] | `string` | two character display text |

[]()

Update a video source

**Kind**: global function

| Param | Type |
| - | - |
| id | `string` |
| source | `any` |

[]()

Remove the video source for the participant

**Kind**: global function

| Param | Description |
| - | - |
| id | id for the source (ex. participant id) |

[]()

Remove the pinned source

**Kind**: global function

| Param | Description |
| - | - |
| id | id for the source (ex. participant id) |

[]()

Remove all sources

**Kind**: global function\
[]()

Enable PiP

**Kind**: global function

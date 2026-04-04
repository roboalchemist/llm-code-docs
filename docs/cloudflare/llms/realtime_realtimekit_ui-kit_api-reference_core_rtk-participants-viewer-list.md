# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-participants-viewer-list/index.md

---

title: rtk-participants-viewer-list · Cloudflare Realtime docs
description: API reference for rtk-participants-viewer-list component (Web
  Components (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-participants-viewer-list/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-participants-viewer-list/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `config` | `UIConfig1` | ❌ | `createDefaultConfig()` | Config |
| `hideHeader` | `boolean` | ✅ | - | Hide Viewer Count Header |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `search` | `string` | ✅ | - | Search |
| `size` | `Size1` | ✅ | - | Size |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |
| `view` | `ParticipantsViewMode` | ✅ | - | View mode for participants list |

## Usage Examples

### Basic Usage

```html
<rtk-participants-viewer-list></rtk-participants-viewer-list>
```

### With Properties

```html
<rtk-participants-viewer-list
 search="example">
</rtk-participants-viewer-list>
```

```html
<script>
  const el = document.querySelector("rtk-participants-viewer-list");


  el.hideHeader= true;
  el.meeting= meeting
</script>
```

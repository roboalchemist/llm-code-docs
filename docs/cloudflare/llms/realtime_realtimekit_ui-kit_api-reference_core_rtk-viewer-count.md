# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-viewer-count/index.md

---

title: rtk-viewer-count · Cloudflare Realtime docs
description: API reference for rtk-viewer-count component (Web Components (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-viewer-count/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-viewer-count/index.md
---

A component which shows count of total joined participants in a meeting.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `ViewerCountVariant` | ✅ | - | Viewer count variant |

## Usage Examples

### Basic Usage

```html
<rtk-viewer-count></rtk-viewer-count>
```

### With Properties

```html
<rtk-viewer-count
 variant="primary">
</rtk-viewer-count>
```

```html
<script>
  const el = document.querySelector("rtk-viewer-count");


  el.meeting= meeting
</script>
```

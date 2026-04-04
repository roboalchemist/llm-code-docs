# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-recording-indicator/index.md

---

title: rtk-recording-indicator · Cloudflare Realtime docs
description: API reference for rtk-recording-indicator component (Angular Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-recording-indicator/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-recording-indicator/index.md
---

A component which indicates the recording status of a meeting. It will not render anything if no recording is taking place.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-recording-indicator></rtk-recording-indicator>
```

### With Properties

```html
<!-- component.html -->
<rtk-recording-indicator
 [meeting]="meeting"
 size="md">
</rtk-recording-indicator>
```

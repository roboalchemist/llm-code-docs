# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-debugger-video/index.md

---

title: rtk-debugger-video · Cloudflare Realtime docs
description: API reference for rtk-debugger-video component (Angular Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-debugger-video/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-debugger-video/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size1` | ✅ | - | Size |
| `states` | `States1` | ✅ | - | States object |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-debugger-video></rtk-debugger-video>
```

### With Properties

```html
<!-- component.html -->
<rtk-debugger-video
 [meeting]="meeting"
 size="md">
</rtk-debugger-video>
```

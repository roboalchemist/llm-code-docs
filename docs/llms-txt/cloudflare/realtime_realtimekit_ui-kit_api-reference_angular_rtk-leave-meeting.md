# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-leave-meeting/index.md

---

title: rtk-leave-meeting · Cloudflare Realtime docs
description: API reference for rtk-leave-meeting component (Angular Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-leave-meeting/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-leave-meeting/index.md
---

A component which allows you to leave a meeting or end meeting for all, if you have the permission.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-leave-meeting></rtk-leave-meeting>
```

### With Properties

```html
<!-- component.html -->
<rtk-leave-meeting
 [meeting]="meeting">
</rtk-leave-meeting>
```

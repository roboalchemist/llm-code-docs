# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-debugger/index.md

---

title: rtk-debugger · Cloudflare Realtime docs
description: API reference for rtk-debugger component (Angular Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-debugger/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-debugger/index.md
---

A troubleshooting component to identify and fix any issues in the meeting.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-debugger></rtk-debugger>
```

### With Properties

```html
<!-- component.html -->
<rtk-debugger
 [meeting]="meeting"
 size="md">
</rtk-debugger>
```

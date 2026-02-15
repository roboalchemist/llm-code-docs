# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-clock/index.md

---

title: rtk-clock · Cloudflare Realtime docs
description: API reference for rtk-clock component (Angular Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-clock/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-clock/index.md
---

Shows the time elapsed in a meeting.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-clock></rtk-clock>
```

### With Properties

```html
<!-- component.html -->
<rtk-clock
 [meeting]="meeting"
 size="md">
</rtk-clock>
```

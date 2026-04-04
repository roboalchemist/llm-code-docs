# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-breakout-rooms-toggle/index.md

---

title: rtk-breakout-rooms-toggle · Cloudflare Realtime docs
description: API reference for rtk-breakout-rooms-toggle component (Angular Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-breakout-rooms-toggle/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-breakout-rooms-toggle/index.md
---

A button which toggles visibility of breakout rooms. You need to pass the `meeting` object to it.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ✅ | - | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ✅ | - | Language |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-breakout-rooms-toggle></rtk-breakout-rooms-toggle>
```

### With Properties

```html
<!-- component.html -->
<rtk-breakout-rooms-toggle
 [iconPack]="defaultIconPack"
 [meeting]="meeting"
 size="md">
</rtk-breakout-rooms-toggle>
```

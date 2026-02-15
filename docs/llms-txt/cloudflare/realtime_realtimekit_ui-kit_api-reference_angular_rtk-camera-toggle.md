# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-camera-toggle/index.md

---

title: rtk-camera-toggle · Cloudflare Realtime docs
description: API reference for rtk-camera-toggle component (Angular Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-camera-toggle/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-camera-toggle/index.md
---

A button which toggles your camera.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-camera-toggle></rtk-camera-toggle>
```

### With Properties

```html
<!-- component.html -->
<rtk-camera-toggle
 [meeting]="meeting"
 size="md"
 variant="button">
</rtk-camera-toggle>
```

# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-dialog-manager/index.md

---

title: rtk-dialog-manager · Cloudflare Realtime docs
description: API reference for rtk-dialog-manager component (Angular Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-dialog-manager/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-dialog-manager/index.md
---

A component which handles all dialog elements in a component such as:

* rtk-settings
* rtk-leave-meeting
* rtk-permissions-message
* rtk-image-viewer
* rtk-breakout-rooms-manager This components depends on the values from `states` object.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | UI Config |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-dialog-manager></rtk-dialog-manager>
```

### With Properties

```html
<!-- component.html -->
<rtk-dialog-manager
 [meeting]="meeting"
 size="md">
</rtk-dialog-manager>
```

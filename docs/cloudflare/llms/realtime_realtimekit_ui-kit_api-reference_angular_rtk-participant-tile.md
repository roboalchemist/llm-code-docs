# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-participant-tile/index.md

---

title: rtk-participant-tile · Cloudflare Realtime docs
description: API reference for rtk-participant-tile component (Angular Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-participant-tile/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-participant-tile/index.md
---

A component which plays a participants video and allows for placement of components like `rtk-name-tag`, `rtk-audio-visualizer` or any other component.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config object |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `isPreview` | `boolean` | ✅ | - | Whether tile is used for preview |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `nameTagPosition` | `\| 'bottom-left' \| 'bottom-right' \| 'bottom-center' \| 'top-left' \| 'top-right' \| 'top-center'` | ✅ | - | Position of name tag |
| `participant` | `Peer` | ✅ | - | Participant object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `'solid' \| 'gradient'` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-participant-tile></rtk-participant-tile>
```

### With Properties

```html
<!-- component.html -->
<rtk-participant-tile
 [isPreview]="true"
 [meeting]="meeting"
 [nameTagPosition]="| 'bottom-left'
    | 'bottom-right'
    | 'bottom-center'
    | 'top-left'
    | 'top-right'
    | 'top-center'">
</rtk-participant-tile>
```

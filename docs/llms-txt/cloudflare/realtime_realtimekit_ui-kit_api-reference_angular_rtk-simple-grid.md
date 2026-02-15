# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-simple-grid/index.md

---

title: rtk-simple-grid · Cloudflare Realtime docs
description: API reference for rtk-simple-grid component (Angular Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-simple-grid/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-simple-grid/index.md
---

A grid component which renders only the participants in a simple grid.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `aspectRatio` | `string` | ✅ | - | Aspect Ratio of participant tile Format: `width:height` |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | UI Config |
| `gap` | `number` | ✅ | - | Gap between participant tiles |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon Pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `participants` | `Peer[]` | ✅ | - | Participants |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-simple-grid></rtk-simple-grid>
```

### With Properties

```html
<!-- component.html -->
<rtk-simple-grid
 aspectRatio="example"
 gap="42"
 [meeting]="meeting">
</rtk-simple-grid>
```

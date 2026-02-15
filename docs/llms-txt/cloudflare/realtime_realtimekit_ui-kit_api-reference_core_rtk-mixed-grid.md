# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-mixed-grid/index.md

---

title: rtk-mixed-grid · Cloudflare Realtime docs
description: API reference for rtk-mixed-grid component (Web Components (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-mixed-grid/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-mixed-grid/index.md
---

A grid component which handles screenshares, plugins and participants.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `aspectRatio` | `string` | ✅ | - | Aspect Ratio of participant tile Format: `width:height` |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | UI Config |
| `gap` | `number` | ✅ | - | Gap between participant tiles |
| `gridSize` | `GridSize1` | ✅ | - | Grid size |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon Pack |
| `layout` | `GridLayout1` | ✅ | - | Grid Layout |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `participants` | `Peer[]` | ✅ | - | Participants |
| `pinnedParticipants` | `Peer[]` | ✅ | - | Pinned Participants |
| `plugins` | `RTKPlugin[]` | ✅ | - | Active Plugins |
| `screenShareParticipants` | `Peer[]` | ✅ | - | Screenshare Participants |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-mixed-grid></rtk-mixed-grid>
```

### With Properties

```html
<rtk-mixed-grid
 aspectRatio="example"
 gridSize="md">
</rtk-mixed-grid>
```

```html
<script>
  const el = document.querySelector("rtk-mixed-grid");


  el.gap= 42;
</script>
```

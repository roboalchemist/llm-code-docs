# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmixedgrid/index.md

---

title: RtkMixedGrid · Cloudflare Realtime docs
description: API reference for RtkMixedGrid component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmixedgrid/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmixedgrid/index.md
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

```tsx
import { RtkMixedGrid } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkMixedGrid />;
}
```

### With Properties

```tsx
import { RtkMixedGrid } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkMixedGrid
      aspectRatio="example"
      gap={42}
      gridSize="md"
    />
  );
}
```

# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksimplegrid/index.md

---

title: RtkSimpleGrid · Cloudflare Realtime docs
description: API reference for RtkSimpleGrid component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksimplegrid/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksimplegrid/index.md
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

```tsx
import { RtkSimpleGrid } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkSimpleGrid />;
}
```

### With Properties

```tsx
import { RtkSimpleGrid } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkSimpleGrid
      aspectRatio="example"
      gap={42}
      meeting={meeting}
    />
  );
}
```

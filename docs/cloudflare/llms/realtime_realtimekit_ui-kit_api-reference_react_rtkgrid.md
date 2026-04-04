# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkgrid/index.md

---

title: RtkGrid · Cloudflare Realtime docs
description: API reference for RtkGrid component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkgrid/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkgrid/index.md
---

The main grid component which abstracts all the grid handling logic and renders it for you.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `aspectRatio` | `string` | ✅ | - | The aspect ratio of each participant |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config object |
| `gap` | `number` | ✅ | - | Gap between participants |
| `gridSize` | `GridSize` | ✅ | - | Grid size |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `layout` | `GridLayout` | ✅ | - | Grid Layout |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `overrides` | `any` | ✅ | - | @deprecated |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkGrid } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkGrid />;
}
```

### With Properties

```tsx
import { RtkGrid } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkGrid
      aspectRatio="example"
      gap={42}
      gridSize="md"
    />
  );
}
```

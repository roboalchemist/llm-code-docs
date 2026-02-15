# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkai/index.md

---

title: RtkAi · Cloudflare Realtime docs
description: API reference for RtkAi component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkai/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkai/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `view` | `AIView` | ✅ | - | View type |

## Usage Examples

### Basic Usage

```tsx
import { RtkAi } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkAi />;
}
```

### With Properties

```tsx
import { RtkAi } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkAi
      meeting={meeting}
      size="md"
      view={aiview}
    />
  );
}
```

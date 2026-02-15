# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkjoinstage/index.md

---

title: RtkJoinStage · Cloudflare Realtime docs
description: API reference for RtkJoinStage component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkjoinstage/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkjoinstage/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | UI Config |
| `dataConfig` | `ModalDataConfig` | ✅ | - | Content Config |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkJoinStage } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkJoinStage />;
}
```

### With Properties

```tsx
import { RtkJoinStage } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkJoinStage
      dataConfig={modaldataconfig}
      meeting={meeting}
      size="md"
    />
  );
}
```

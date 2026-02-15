# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatselector/index.md

---

title: RtkChatSelector · Cloudflare Realtime docs
description: API reference for RtkChatSelector component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatselector/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatselector/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `config` | `UIConfig1` | ❌ | `createDefaultConfig()` | Config |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `overrides` | `Overrides1` | ❌ | `defaultOverrides` | UI Overrides |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States1` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkChatSelector } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkChatSelector />;
}
```

### With Properties

```tsx
import { RtkChatSelector } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkChatSelector
      meeting={meeting}
      size="md"
    />
  );
}
```

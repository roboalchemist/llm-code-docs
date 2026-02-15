# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdebuggersystem/index.md

---

title: RtkDebuggerSystem · Cloudflare Realtime docs
description: API reference for RtkDebuggerSystem component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdebuggersystem/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdebuggersystem/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size1` | ✅ | - | Size |
| `states` | `States1` | ✅ | - | States object |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkDebuggerSystem } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkDebuggerSystem />;
}
```

### With Properties

```tsx
import { RtkDebuggerSystem } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkDebuggerSystem
      meeting={meeting}
      size="md"
    />
  );
}
```

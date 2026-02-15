# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdebugger/index.md

---

title: RtkDebugger · Cloudflare Realtime docs
description: API reference for RtkDebugger component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdebugger/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdebugger/index.md
---

A troubleshooting component to identify and fix any issues in the meeting.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkDebugger } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkDebugger />;
}
```

### With Properties

```tsx
import { RtkDebugger } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkDebugger
      meeting={meeting}
      size="md"
    />
  );
}
```

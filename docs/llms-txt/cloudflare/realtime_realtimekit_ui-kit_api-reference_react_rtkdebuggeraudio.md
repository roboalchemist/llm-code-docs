# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdebuggeraudio/index.md

---

title: RtkDebuggerAudio · Cloudflare Realtime docs
description: API reference for RtkDebuggerAudio component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdebuggeraudio/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdebuggeraudio/index.md
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
import { RtkDebuggerAudio } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkDebuggerAudio />;
}
```

### With Properties

```tsx
import { RtkDebuggerAudio } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkDebuggerAudio
      meeting={meeting}
      size="md"
    />
  );
}
```

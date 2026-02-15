# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkclock/index.md

---

title: RtkClock · Cloudflare Realtime docs
description: API reference for RtkClock component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkclock/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkclock/index.md
---

Shows the time elapsed in a meeting.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |

## Usage Examples

### Basic Usage

```tsx
import { RtkClock } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkClock />;
}
```

### With Properties

```tsx
import { RtkClock } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkClock
      meeting={meeting}
      size="md"
    />
  );
}
```

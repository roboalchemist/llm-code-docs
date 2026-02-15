# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkbroadcastmessagemodal/index.md

---

title: RtkBroadcastMessageModal · Cloudflare Realtime docs
description: API reference for RtkBroadcastMessageModal component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkbroadcastmessagemodal/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkbroadcastmessagemodal/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `states` | `States1` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkBroadcastMessageModal } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkBroadcastMessageModal />;
}
```

### With Properties

```tsx
import { RtkBroadcastMessageModal } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkBroadcastMessageModal
      meeting={meeting}
    />
  );
}
```

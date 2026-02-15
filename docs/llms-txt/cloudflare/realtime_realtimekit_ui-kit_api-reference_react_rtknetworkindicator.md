# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtknetworkindicator/index.md

---

title: RtkNetworkIndicator · Cloudflare Realtime docs
description: API reference for RtkNetworkIndicator component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtknetworkindicator/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtknetworkindicator/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `isScreenShare` | `boolean` | ✅ | - | Is for screenshare |
| `meeting` | `Meeting` | ✅ | - | Meeting |
| `participant` | `Peer` | ✅ | - | Participant or Self |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkNetworkIndicator } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkNetworkIndicator />;
}
```

### With Properties

```tsx
import { RtkNetworkIndicator } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkNetworkIndicator
      isScreenShare={true}
      meeting={meeting}
      participant={participant}
    />
  );
}
```

# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtknametag/index.md

---

title: RtkNameTag · Cloudflare Realtime docs
description: API reference for RtkNameTag component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtknametag/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtknametag/index.md
---

A component which shows a participant's name.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `isScreenShare` | `boolean` | ✅ | - | Whether it is used in a screen share view |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `participant` | `Peer` | ✅ | - | Participant object |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `RtkNameTagVariant` | ✅ | - | Name tag variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkNameTag } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkNameTag />;
}
```

### With Properties

```tsx
import { RtkNameTag } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkNameTag
      isScreenShare={true}
      meeting={meeting}
      participant={participant}
    />
  );
}
```
